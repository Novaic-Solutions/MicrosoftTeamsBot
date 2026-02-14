from models.cards.cardModels import ActionObj, BodyElementObj, CardUtils

class CardContainerObj(BodyElementObj):
    '''
        Base class for all container objects

        type            - string
        items           - list of BodyElementObj. The Card elements to render inside the container.
        selectAction - ActionObj. An action that will be invoked when the container is tapped or selected.
        style           - string. Style hint for Container
        verticalContentAlignment - string. Vertical alignment of content within container
        bleed           - boolean. When true, draw a separating line between this container and the previous element. Default value is false
        backgroundImage - string. Background image for container
        minHeight       - string. Minimum height of container
        rtl             - boolean. When true, elements in this container are right-aligned. Default value is false
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items                      = CardUtils.createElements(kwargs['items']) if 'items' in kwargs else list()
        self.selectAction               = kwargs['selectAction'] if 'selectAction' in kwargs else None
        self.style                      = kwargs['style'] if 'style' in kwargs else None
        self.verticalContentAlignment   = kwargs['verticalContentAlignment'] if 'verticalContentAlignment' in kwargs else None
        self.bleed                      = kwargs['bleed'] if 'bleed' in kwargs else False
        self.backgroundImage            = kwargs['backgroundImage'] if 'backgroundImage' in kwargs else ""
        self.minHeight                  = kwargs['minHeight'] if 'minHeight' in kwargs else ""
        self.rtl                        = kwargs['rtl'] if 'rtl' in kwargs else False

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Container'
    
    @classmethod
    def get_type(cls):
        return 'Container'