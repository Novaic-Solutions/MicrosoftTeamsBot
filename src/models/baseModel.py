import json

class Base(object):
    """Base class for all classes in the project"""
    def __repr__(self):
        return f"{type(self).__name__}()"
    
    def __str__(self):
        return f"{type(self).__name__}()"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
    
    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, d):
        self.__dict__.update(d)

    def __iter__(self):
        return iter(self.__dict__.values())
    
    def __len__(self):
        return len(self.__dict__)
    
    def __contains__(self, key):
        return key in self.__dict__
    
    def __getitem__(self, key):
        return self.__dict__[key]
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def keys(self):
        return self.__dict__.keys()
    
    def values(self):
        return self.__dict__.values()
    
    @classmethod
    def _from_string(cls, string):
        return cls(**json.loads(string))
    
    @classmethod
    def _from_dict(cls, dict):
        return cls(**dict)
    
    def _to_dict(self):
        return self.__dict__
    
    

    #-------------------------------------------------------------------------------------------------------                            
    def dictify(self, obj):
        if isinstance(obj, Base):
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