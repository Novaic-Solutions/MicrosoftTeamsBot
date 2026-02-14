from models.cards.cardModels import ActionObj, BodyElementObj, CardUtils

class CardImageSetObj(BodyElementObj):
    '''
        The ImageSet displays a collection of Images similar to a gallery. Acceptable formats are PNG, JPEG, and GIF
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type   = kwargs['type'] if 'type' in kwargs else None
        self.images = CardUtils.createElements(kwargs['images']) if 'images' in kwargs else None
        self.imageSize = kwargs['imageSize'] if 'imageSize' in kwargs else None
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.fallback = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height = kwargs['height'] if 'height' in kwargs else None
        self.spacing = kwargs['spacing'] if 'spacing' in kwargs else None
        self.separator = kwargs['separator'] if 'separator' in kwargs else None
        self.isVisible = kwargs['isVisible'] if 'isVisible' in kwargs else None
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'ImageSet'
    
    @classmethod
    def get_type(cls):
        return 'ImageSet'

class CardImageObj(BodyElementObj):
    '''
        Displays an image. Acceptable formats are PNG, JPEG, and GIF
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = kwargs['url'] if 'url' in kwargs else None
        self.altText = kwargs['altText'] if 'altText' in kwargs else None
        self.backgroundColor = kwargs['backgroundColor'] if 'backgroundColor' in kwargs else None
        self.height = kwargs['height'] if 'height' in kwargs else None
        self.horizontalAlignment = kwargs['horizontalAlignment'] if 'horizontalAlignment' in kwargs else None
        self.selectAction = kwargs['selectAction'] if 'selectAction' in kwargs else None
        self.size = kwargs['size'] if 'size' in kwargs else None
        self.style = kwargs['style'] if 'style' in kwargs else None
        self.width = kwargs['width'] if 'width' in kwargs else None
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.isVisible = kwargs['isVisible'] if 'isVisible' in kwargs else None
        self.separator = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing = kwargs['spacing'] if 'spacing' in kwargs else None
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Image'
    
    @classmethod
    def get_type(cls):
        return 'Image'