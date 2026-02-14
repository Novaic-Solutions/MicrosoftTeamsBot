from models.cards.cardModels import ActionObj, BodyElementObj


class CardTextBlockObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text                           = kwargs['text'] if 'text' in kwargs else None
        self.color                          = kwargs['color'] if 'color' in kwargs else None
        self.fontType                       = kwargs['fontType'] if 'fontType' in kwargs else None
        self.horizontalAlignment            = kwargs['horizontalAlignment'] if 'horizontalAlignment' in kwargs else None
        self.isSubtle                       = kwargs['isSubtle'] if 'isSubtle' in kwargs else None
        self.maxLines                       = kwargs['maxLines'] if 'maxLines' in kwargs else None
        self.size                           = kwargs['size'] if 'size' in kwargs else None
        self.weight                         = kwargs['weight'] if 'weight' in kwargs else None
        self.wrap                           = kwargs['wrap'] if 'wrap' in kwargs else None
        self.style                          = kwargs['style'] if 'style' in kwargs else None
        self.fallback                       = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height                         = kwargs['height'] if 'height' in kwargs else None
        self.id                             = kwargs['id'] if 'id' in kwargs else None
        self.separator                      = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing                        = kwargs['spacing'] if 'spacing' in kwargs else None
        self.isVisible                      = kwargs['isVisible'] if 'isVisible' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'TextBlock'
    
    @classmethod
    def get_type(cls):
        return 'TextBlock'