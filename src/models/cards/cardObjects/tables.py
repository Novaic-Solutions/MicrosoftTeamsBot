from models.cards.cardModels import ActionObj, BodyElementObj, CardUtils

class CardTableObj(BodyElementObj):
    '''

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns                        = CardUtils.createElements(kwargs['columns']) if 'columns' in kwargs else list()
        self.rows                           = CardUtils.createElements(kwargs['rows']) if 'rows' in kwargs else list()
        self.firstRowAsHeaders              = kwargs['firstRowAsHeaders'] if 'firstRowAsHeaders' in kwargs else None
        self.showGridLines                  = kwargs['showGridLines'] if 'showGridLines' in kwargs else None
        self.gridStyle                      = kwargs['gridStyle'] if 'gridStyle' in kwargs else None
        self.horizontalCellContentAlignment = kwargs['horizontalCellContentAlignment'] if 'horizontalCellContentAlignment' in kwargs else None
        self.verticalCellContentAlignment   = kwargs['verticalCellContentAlignment'] if 'verticalCellContentAlignment' in kwargs else None
        self.fallback                       = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height                         = kwargs['height'] if 'height' in kwargs else None
        self.separator                      = kwargs['separator'] if 'separator' in kwargs else None
        self.spacing                        = kwargs['spacing'] if 'spacing' in kwargs else None
        self.id                             = kwargs['id'] if 'id' in kwargs else None
        self.isVisible                      = kwargs['isVisible'] if 'isVisible' in kwargs else None
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Table'
    
    @classmethod
    def get_type(cls):
        return 'Table'


class CardTableRowObj(BodyElementObj):
    '''
        rtl - bool - When `true` content in this container should be presented right to left. When 'false' content in this container should be presented left to right. 
                     When unset layout direction will inherit from parent container or column. If unset in all ancestors, the default platform behavior will apply.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cells                          = CardUtils.createElements(kwargs['cells']) if 'cells' in kwargs else list()
        self.selectAction                   = kwargs['selectAction'] if 'selectAction' in kwargs else None
        self.style                          = kwargs['style'] if 'style' in kwargs else None
        self.verticalContentAlignment       = kwargs['verticalContentAlignment'] if 'verticalContentAlignment' in kwargs else None
        self.bleed                          = kwargs['bleed'] if 'bleed' in kwargs else None
        self.backgroundImage                = kwargs['backgroundImage'] if 'backgroundImage' in kwargs else None
        self.minHeight                      = kwargs['minHeight'] if 'minHeight' in kwargs else None
        self.rt1                            = kwargs['rt1'] if 'rt1' in kwargs else False
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'TableRow'
    
    @classmethod
    def get_type(cls):
        return 'TableRow'

class CardTableCellObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items                          = CardUtils.createElements(kwargs['items']) if 'items' in kwargs else list()
        self.selectAction                   = kwargs['selectAction'] if 'selectAction' in kwargs else None
        self.style                          = kwargs['style'] if 'style' in kwargs else None
        self.verticalContentAlignment       = kwargs['verticalContentAlignment'] if 'verticalContentAlignment' in kwargs else None
        self.bleed                          = kwargs['bleed'] if 'bleed' in kwargs else None
        self.backgroundImage                = kwargs['backgroundImage'] if 'backgroundImage' in kwargs else None
        self.minHeight                      = kwargs['minHeight'] if 'minHeight' in kwargs else None
        self.rt1                            = kwargs['rt1'] if 'rt1' in kwargs else False
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'TableCell'
    
    @classmethod
    def get_type(cls):
        return 'TableCell'


class CardTableColumnObj(BodyElementObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width                          = kwargs['width'] if 'width' in kwargs else None
        self.verticalContentAlignment       = kwargs['verticalContentAlignment'] if 'verticalContentAlignment' in kwargs else None
        self.horizontalContentAlignment     = kwargs['horizontalContentAlignment'] if 'horizontalContentAlignment' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'TableColumnDefinition'
    
    @classmethod
    def get_type(cls):
        return 'TableColumnDefinition'

