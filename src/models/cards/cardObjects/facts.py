from models.cards.cardModels import ActionObj, BodyElementObj, CardUtils


class CardFactSetObj(BodyElementObj):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.facts          = CardUtils.createElements(kwargs['facts']) if 'facts' in kwargs else []
        self.fallback       = kwargs['fallback'] if 'fallback' in kwargs else None
        self.id             = kwargs['id'] if 'id' in kwargs else None
        self.isVisible      = kwargs['isVisible'] if 'isVisible' in kwargs else None
        self.separator      = kwargs['separator'] if 'separator' in kwargs else False
        self.spacing        = kwargs['spacing'] if 'spacing' in kwargs else None
        self.height         = kwargs['height'] if 'height' in kwargs else None


    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'FactSet'
    
    @classmethod
    def get_type(cls):
        return 'FactSet'
    

class CardFactObj(BodyElementObj):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = kwargs['title'] if 'title' in kwargs else None
        self.value = kwargs['value'] if 'value' in kwargs else None


    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Fact'
    
    @classmethod
    def get_type(cls):
        return 'Fact'