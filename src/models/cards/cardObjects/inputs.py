from models.cards.cardModels import ActionObj, BodyElementObj, CardUtils

#--------------------------------------------
# Input Objects
#--------------------------------------------
class CardInputTextObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.isMultiline                    = kwargs['isMultiline'] if 'isMultiline' in kwargs else None
        self.maxLength                      = kwargs['maxLength'] if 'maxLength' in kwargs else None
        self.placeholder                    = kwargs['placeholder'] if 'placeholder' in kwargs else None
        self.regex                          = kwargs['regex'] if 'regex' in kwargs else None
        self.style                          = kwargs['style'] if 'style' in kwargs else None
        self.inlineAction                   = kwargs['inlineAction'] if 'inlineAction' in kwargs else None
        self.value                          = kwargs['value'] if 'value' in kwargs else None
        self.id                             = kwargs['id'] if 'id' in kwargs else None
        self.errorMessage                   = kwargs['errorMessage'] if 'errorMessage' in kwargs else None
        self.isRequired                     = kwargs['isRequired'] if 'isRequired' in kwargs else None
        self.label                          = kwargs['label'] if 'label' in kwargs else None
        self.fallback                       = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height                         = kwargs['height'] if 'height' in kwargs else None
        self.separator                      = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing                        = kwargs['spacing'] if 'spacing' in kwargs else None
        self.isVisible                      = kwargs['isVisible'] if 'isVisible' in kwargs else None
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Input.Text'
    
    @classmethod
    def get_type(cls):
        return 'Input.Text'

#-------------------------------------------------------------------------------------------------------
class CardInputDateObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max                           = kwargs['max'] if 'max' in kwargs else None
        self.min                           = kwargs['min'] if 'min' in kwargs else None
        self.placeholder                   = kwargs['placeholder'] if 'placeholder' in kwargs else None
        self.value                         = kwargs['value'] if 'value' in kwargs else None
        self.id                            = kwargs['id'] if 'id' in kwargs else None
        self.errorMessage                  = kwargs['errorMessage'] if 'errorMessage' in kwargs else None
        self.isRequired                    = kwargs['isRequired'] if 'isRequired' in kwargs else None
        self.label                         = kwargs['label'] if 'label' in kwargs else None
        self.fallback                      = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height                        = kwargs['height'] if 'height' in kwargs else None
        self.separator                     = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing                       = kwargs['spacing'] if 'spacing' in kwargs else None
        self.isVisible                     = kwargs['isVisible'] if 'isVisible' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Input.Date'
    
    @classmethod
    def get_type(cls):
        return 'Input.Date'

#-------------------------------------------------------------------------------------------------------
class CardInputChoiceObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title                          = kwargs['title'] if 'title' in kwargs else None
        self.value                          = kwargs['value'] if 'value' in kwargs else None
        self.data                           = kwargs['$data'] if '$data' in kwargs else None
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Input.Choice'
    
    @classmethod
    def get_type(cls):
        return 'Input.Choice'

#-------------------------------------------------------------------------------------------------------
class CardInputChoiceSetObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices                        = CardUtils.createElements(kwargs['choices']) if 'choices' in kwargs else None
        self.isMultiSelect                  = kwargs['isMultiSelect'] if 'isMultiSelect' in kwargs else None    
        self.style                          = kwargs['style'] if 'style' in kwargs else None
        self.value                          = kwargs['value'] if 'value' in kwargs else None
        self.placeholder                    = kwargs['placeholder'] if 'placeholder' in kwargs else None
        self.wrap                           = kwargs['wrap'] if 'wrap' in kwargs else None
        self.id                             = kwargs['id'] if 'id' in kwargs else None
        self.errorMessage                   = kwargs['errorMessage'] if 'errorMessage' in kwargs else None
        self.isRequired                     = kwargs['isRequired'] if 'isRequired' in kwargs else None
        self.label                          = kwargs['label'] if 'label' in kwargs else None
        self.fallback                       = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height                         = kwargs['height'] if 'height' in kwargs else None
        self.separator                      = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing                        = kwargs['spacing'] if 'spacing' in kwargs else None
        self.isVisible                      = kwargs['isVisible'] if 'isVisible' in kwargs else None        

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Input.ChoiceSet'
    
    @classmethod
    def get_type(cls):
        return 'Input.ChoiceSet'

#-------------------------------------------------------------------------------------------------------
class CardInputToggleObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title                          = kwargs['title'] if 'title' in kwargs else None
        self.value                          = kwargs['value'] if 'value' in kwargs else None
        self.valueOn                        = kwargs['valueOn'] if 'valueOn' in kwargs else None
        self.valueOff                       = kwargs['valueOff'] if 'valueOff' in kwargs else None
        self.id                             = kwargs['id'] if 'id' in kwargs else None
        self.wrap                           = kwargs['wrap'] if 'wrap' in kwargs else None
        self.errorMessage                   = kwargs['errorMessage'] if 'errorMessage' in kwargs else None
        self.isRequired                     = kwargs['isRequired'] if 'isRequired' in kwargs else None
        self.label                          = kwargs['label'] if 'label' in kwargs else None
        self.fallback                       = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height                         = kwargs['height'] if 'height' in kwargs else None
        self.separator                      = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing                        = kwargs['spacing'] if 'spacing' in kwargs else None
        self.isVisible                      = kwargs['isVisible'] if 'isVisible' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Input.Toggle'
    
    @classmethod
    def get_type(cls):
        return 'Input.Toggle'

#-------------------------------------------------------------------------------------------------------
class CardInputNumberObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max                           = kwargs['max'] if 'max' in kwargs else None
        self.min                           = kwargs['min'] if 'min' in kwargs else None
        self.placeholder                   = kwargs['placeholder'] if 'placeholder' in kwargs else None
        self.value                         = kwargs['value'] if 'value' in kwargs else None
        self.id                            = kwargs['id'] if 'id' in kwargs else None
        self.errorMessage                  = kwargs['errorMessage'] if 'errorMessage' in kwargs else None
        self.isRequired                    = kwargs['isRequired'] if 'isRequired' in kwargs else None
        self.label                         = kwargs['label'] if 'label' in kwargs else None
        self.fallback                      = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height                        = kwargs['height'] if 'height' in kwargs else None
        self.separator                     = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing                       = kwargs['spacing'] if 'spacing' in kwargs else None
        self.isVisible                     = kwargs['isVisible'] if 'isVisible' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Input.Number'
    
    @classmethod
    def get_type(cls):
        return 'Input.Number'

#-------------------------------------------------------------------------------------------------------
class CardInputTimeObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max                           = kwargs['max'] if 'max' in kwargs else None
        self.min                           = kwargs['min'] if 'min' in kwargs else None
        self.placeholder                   = kwargs['placeholder'] if 'placeholder' in kwargs else None
        self.value                         = kwargs['value'] if 'value' in kwargs else None
        self.id                            = kwargs['id'] if 'id' in kwargs else None
        self.errorMessage                  = kwargs['errorMessage'] if 'errorMessage' in kwargs else None
        self.isRequired                    = kwargs['isRequired'] if 'isRequired' in kwargs else None
        self.label                         = kwargs['label'] if 'label' in kwargs else None
        self.fallback                      = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height                        = kwargs['height'] if 'height' in kwargs else None
        self.separator                     = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing                       = kwargs['spacing'] if 'spacing' in kwargs else None
        self.isVisible                     = kwargs['isVisible'] if 'isVisible' in kwargs else None
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Input.Time'
    
    @classmethod
    def get_type(cls):
        return 'Input.Time'