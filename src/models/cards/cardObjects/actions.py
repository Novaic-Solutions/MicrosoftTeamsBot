from models.cards.cardModels import ActionObj, BodyElementObj, CardUtils
#from models.cards.cardModels import CardObj

#--------------------------------------------
# Action Objects
#--------------------------------------------
#-------------------------------------------------------------------------------------------------------
class CardActionSetObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.actions = CardUtils.createElements(kwargs['actions']) if 'actions' in kwargs else []
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.spacing = kwargs['spacing'] if 'spacing' in kwargs else None
        self.height = kwargs['height'] if 'height' in kwargs else None
        self.isVisible = kwargs['isVisible'] if 'isVisible' in kwargs else None
        self.separator = kwargs['separator'] if 'separator' in kwargs else False

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'ActionSet'
    
    @classmethod
    def get_type(cls):
        return 'ActionSet'

#-------------------------------------------------------------------------------------------------------
class CardActionExecuteObj(ActionObj):
    '''
        Gathers input fields, merges with optional data field, and sends an event to the client.
        Clients process the event by sending an Invoke activity of type adaptiveCard/action to the target Bot. 
        The inputs that are gathered are those on the current card, and in the case of a show card those on any parent cards. 
        See [Universal Action Model](https://docs.microsoft.com/en-us/adaptive-cards/authoring-cards/universal-action-model) 
        documentation for more details.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verb               = kwargs['verb'] if 'verb' in kwargs else None
        self.data               = kwargs['data'] if 'data' in kwargs else None
        self.associatedInputs   = kwargs['associatedInputs'] if 'associatedInputs' in kwargs else None
        self.iconUrl            = kwargs['iconUrl'] if 'iconUrl' in kwargs else None
        self.style              = kwargs['style'] if 'style' in kwargs else None
        self.isEnabled          = kwargs['isEnabled'] if 'isEnabled' in kwargs else None
        self.tooltip            = kwargs['tooltip'] if 'tooltip' in kwargs else None
        self.fallback           = kwargs['fallback'] if 'fallback' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Action.Execute'
    
    @classmethod
    def get_type(cls):
        return 'Action.Execute'
    
#-------------------------------------------------------------------------------------------------------
class CardActionOpenUrlObj(ActionObj):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url                = kwargs['url'] if 'url' in kwargs else None
        self.iconUrl            = kwargs['iconUrl'] if 'iconUrl' in kwargs else None
        self.style              = kwargs['style'] if 'style' in kwargs else None
        self.isEnabled          = kwargs['isEnabled'] if 'isEnabled' in kwargs else None
        self.tooltip            = kwargs['tooltip'] if 'tooltip' in kwargs else None
        self.fallback           = kwargs['fallback'] if 'fallback' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Action.OpenUrl'
    
    @classmethod
    def get_type(cls):
        return 'Action.OpenUrl'

#-------------------------------------------------------------------------------------------------------
# class CardActionShowCardObj(ActionObj):
#     '''
#         card - The Adaptive Card to show. Inputs in ShowCards will not be submitted if the submit button is located on a parent card.
#                 See https://docs.microsoft.com/en-us/adaptive-cards/authoring-cards/input-validation for more details.
#     '''
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.card               = CardObj._from_dict(kwargs['card']) if 'card' in kwargs else None
#         self.iconUrl            = kwargs['iconUrl'] if 'iconUrl' in kwargs else None
#         self.style              = kwargs['style'] if 'style' in kwargs else None
#         self.isEnabled          = kwargs['isEnabled'] if 'isEnabled' in kwargs else None
#         self.tooltip            = kwargs['tooltip'] if 'tooltip' in kwargs else None
#         self.fallback           = kwargs['fallback'] if 'fallback' in kwargs else None

#     @classmethod
#     def get_class_type(cls, typeCheck):
#         return typeCheck == 'Action.ShowCard'


#-------------------------------------------------------------------------------------------------------
class CardActionSubmitObj(ActionObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data               = kwargs['data'] if 'data' in kwargs else None
        self.associatedInputs   = kwargs['associatedInputs'] if 'associatedInputs' in kwargs else None
        self.iconUrl            = kwargs['iconUrl'] if 'iconUrl' in kwargs else None
        self.style              = kwargs['style'] if 'style' in kwargs else None
        self.isEnabled          = kwargs['isEnabled'] if 'isEnabled' in kwargs else None
        self.tooltip            = kwargs['tooltip'] if 'tooltip' in kwargs else None
        self.fallback           = kwargs['fallback'] if 'fallback' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Action.Submit'
    
    @classmethod
    def get_type(cls):
        return 'Action.Submit'

#-------------------------------------------------------------------------------------------------------
class CardActionToggleVisibilityObj(ActionObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.targetElements     = kwargs['targetElements'] if 'targetElements' in kwargs else None
        self.iconUrl            = kwargs['iconUrl'] if 'iconUrl' in kwargs else None
        self.style              = kwargs['style'] if 'style' in kwargs else None
        self.isEnabled          = kwargs['isEnabled'] if 'isEnabled' in kwargs else None
        self.tooltip            = kwargs['tooltip'] if 'tooltip' in kwargs else None
        self.fallback           = kwargs['fallback'] if 'fallback' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Action.ToggleVisibility'
    
    @classmethod
    def get_type(cls):
        return 'Action.ToggleVisibility'

#-------------------------------------------------------------------------------------------------------
class CardTargetElementObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elementId          = kwargs['elementId'] if 'elementId' in kwargs else None
        self.isVisible          = kwargs['isVisible'] if 'isVisible' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'TargetElement'
    
    @classmethod
    def get_type(cls):
        return 'TargetElement'