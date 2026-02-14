import json
from models.baseModel import Base

class CardObj(object):

    def __init__(self, **kwargs):
        self.type       = kwargs['type'] if 'type' in kwargs else None
        self.version    = kwargs['version'] if 'version' in kwargs else None
        self.schema     = kwargs['schema'] if 'schema' in kwargs else None
        self.msTeams    = kwargs['msteams'] if 'msteams' in kwargs else None
        self.body       = CardUtils.createElements(kwargs['body']) if 'body' in kwargs else None
        self.actions    = CardUtils.createElements(kwargs['actions']) if 'actions' in kwargs else None

    #-------------------------------------------------------------------------------------------------------                            
    def dictify(self, obj):
        if isinstance(obj, CardAttributeObj):
            newObj = obj._to_dict()
            return self.dictify(newObj)

        elif isinstance(obj, list):
            objList = list()
            
            for subObj in obj:
                newObj = self.dictify(subObj)
                if newObj is None:
                    continue
                objList.append(newObj)
            return objList

        elif isinstance(obj, dict):
            objDict = dict()
            for key, value in obj.items():
                newVal = self.dictify(value)
                if newVal is None:
                    continue
                objDict[key] = newVal
            return objDict

        else:
            return obj

    #-------------------------------------------------------------------------------------------------------
    @classmethod
    def _from_dict(cls, dictObj):
        arguments = dict()
        for key, value in dictObj.items():
            if key == "$schema":
                arguments["schema"] = value
            elif key == "$data":
                arguments["data"] = value
            else:
                arguments[key] = value
        print(arguments)
        return cls(**arguments)
    
    #-------------------------------------------------------------------------------------------------------
    @classmethod
    def _from_string(cls, string):
        arguments = json.loads(string)
        return cls._from_dict(arguments)

    #-------------------------------------------------------------------------------------------------------
    def _to_json(self):
        '''
            Converts the object to a json string.
            Because the schema attribute has a dollar sign in it, it cannot be converted easily
            so the default functionality needed to be overwritten.
        '''        
        return json.dumps(self._to_dict())

    #-------------------------------------------------------------------------------------------------------
    def _to_dict(self):
        jsonDict = dict()
        for key, value in self.__dict__.items():
            if value is None:
                continue
            elif key == "schema":
                jsonDict["$schema"] = value
            elif key == "$data":
                jsonDict["$data"] = value
            else:
                jsonDict[key] = self.dictify(value)
        return jsonDict
    
    #-------------------------------------------------------------------------------------------------------
    def __iter__(self):
        return iter(self.__dict__.values())
    
    #-------------------------------------------------------------------------------------------------------
    def __len__(self):
        return len(self.__dict__)
    
    #-------------------------------------------------------------------------------------------------------
    def __contains__(self, key):
        return key in self.__dict__
    
    #-------------------------------------------------------------------------------------------------------
    def __getitem__(self, key):
        return self.__dict__[key]
    
    #-------------------------------------------------------------------------------------------------------
    def __setitem__(self, key, value):
        self.__dict__[key] = value



#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
class CardAttributeObj(Base):
    #-------------------------------------------------------------------------------------------------------
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'CardAttribute'
    
    def _to_dict(self):
        newDict = dict()
        for key,val in self.__dict__.items():
            if val is None:
                continue
            newDict[key] = val
        return newDict


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
class ActionObj(CardAttributeObj):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.type               = kwargs['type'] if 'type' in kwargs else None
        self.title              = kwargs['title'] if 'title' in kwargs else None
        self.mode               = kwargs['mode'] if 'mode' in kwargs else None
        self.id                 = kwargs['id'] if 'id' in kwargs else None
    
    #-------------------------------------------------------------------------------------------------------
    def _to_json(self):
        '''
            Converts the object to a json string.
            Because the schema attribute has a dollar sign in it, it cannot be converted easily
            so the default functionality needed to be overwritten.
        '''
        return json.dumps(self._to_dict())

    #-------------------------------------------------------------------------------------------------------
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Action'


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
class BodyElementObj(CardAttributeObj):

    def __init__(self, **kwargs):
        super().__init__()
        self.type                   = kwargs['type'] if 'type' in kwargs else None

    #-------------------------------------------------------------------------------------------------------
    def _to_json(self):
        '''
            Converts the object to a json string.
            Because the schema attribute has a dollar sign in it, it cannot be converted easily
            so the default functionality needed to be overwritten.
        '''
        return json.dumps(self._to_dict())
    

    #-------------------------------------------------------------------------------------------------------
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'BodyElement'
    
    @classmethod
    def get_type(cls):
        return 'BodyElement'


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
class CardUtils(object):
    
    #-------------------------------------------------------------------------------------------------------
    @staticmethod
    def checkElements(element):
        #print(f"Element Type: {element['type']}")
        for subClass in BodyElementObj.__subclasses__():
            #print(subClass)
            
            if subClass.get_class_type(element['type']):
                
                return subClass(**element)

        for subClass in ActionObj.__subclasses__():
            #print(subClass)
            if subClass.get_class_type(element['type']):
                return subClass(**element)
        
        raise ValueError(f"Unknown type: {element['type']}")

    #-------------------------------------------------------------------------------------------------------
    @staticmethod
    def createElements(body):
        if isinstance(body, list):
            newElements = list()
            for element in body:
                #print(f"Element: {element}")
                serializedElement = CardUtils.createElements(element)
                if not serializedElement:
                    raise ValueError(f"Unknown type: {type(element)}")
                newElements.append(serializedElement)
            return newElements

        elif isinstance(body, dict):
            newElement = CardUtils.checkElements(body)
            if not newElement:
                raise ValueError(f"Unknown value: {body}")
            return newElement
        else:
            raise ValueError(f"Unknown type: {type(body)}")