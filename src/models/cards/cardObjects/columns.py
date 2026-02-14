from models.cards.cardModels import ActionObj, BodyElementObj, CardUtils
#------------------------------------------
#   COLUMNS
#------------------------------------------
class CardColumnSetObj(BodyElementObj):
    '''
        columns - array of Column objects
        selectAction - Action to execute when the ColumnSet is clicked or tapped
        style       - Style hint for ColumnSet
        bleed       - When true, draw a separating line between each column. Default value is false
        minHeight   - Minimum height of the ColumnSet
        horizontalAlignment - Horizontal alignment for ColumnSet
        fallback    - Fallback content for clients that don’t support ColumnSet
        height      - Height of the ColumnSet
        separator   - Draw a separating line between this element and the previous element in the parent container. Default value is false
        spacing     - Spacing between columns
        id          - Element Id
        isVisible   - Is Visible

    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns            = CardUtils.createElements(kwargs['columns']) if 'columns' in kwargs else list()
        self.selectAction       = kwargs['selectAction'] if 'selectAction' in kwargs else None
        self.style              = kwargs['style'] if 'style' in kwargs else None
        self.bleed              = kwargs['bleed'] if 'bleed' in kwargs else False
        self.minHeight          = kwargs['minHeight'] if 'minHeight' in kwargs else ""
        self.horizontalAlignment= kwargs['horizontalAlignment'] if 'horizontalAlignment' in kwargs else None
        self.fallback           = kwargs['fallback'] if 'fallback' in kwargs else None
        self.height             = kwargs['height'] if 'height' in kwargs else None
        self.separator          = kwargs['separator'] if 'separator' in kwargs else False
        self.spacing            = kwargs['spacing'] if 'spacing' in kwargs else None
        self.id                 = kwargs['id'] if 'id' in kwargs else None
        self.isVisible          = kwargs['isVisible'] if 'isVisible' in kwargs else None
    
    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'ColumnSet'
    
    @classmethod
    def get_type(cls):
        return 'ColumnSet'



class CardColumnObj(BodyElementObj):
    '''
        items   - array of CardElement objects
        backgroundImage - Background image for column
        bleed   - When true, draw a separating line between this column and the previous column. Default value is false
        fallback - Fallback content for clients that don’t support this column type
        minHeight - Minimum height of the column
        rtl     - When true, elements in this column are right-aligned. Default value is false
        separator - Draw a separating line between this element and the previous element in the parent container. Default value is false
        spacing - Spacing between this column and the previous column
        selectAction - Action to execute when the Column is clicked or tapped
        style   - Style hint for Column
        verticalContentAlignment - Vertical alignment for content within column
        width   - Width of the column
        id      - Element Id
        isVisible - Is Visible

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items              = CardUtils.createElements(kwargs['items']) if 'items' in kwargs else list()
        self.backgroundImage    = kwargs['backgroundImage'] if 'backgroundImage' in kwargs else ""
        self.bleed              = kwargs['bleed'] if 'bleed' in kwargs else False
        self.fallback           = kwargs['fallback'] if 'fallback' in kwargs else None
        self.minHeight          = kwargs['minHeight'] if 'minHeight' in kwargs else ""
        self.rtl                = kwargs['rtl'] if 'rtl' in kwargs else False
        self.separator          = kwargs['separator'] if 'separator' in kwargs else False
        self.spacing            = kwargs['spacing'] if 'spacing' in kwargs else None
        self.selectAction       = kwargs['selectAction'] if 'selectAction' in kwargs else None
        self.style              = kwargs['style'] if 'style' in kwargs else None
        self.verticalContentAlignment   = kwargs['verticalContentAlignment'] if 'verticalContentAlignment' in kwargs else ""
        self.width              = kwargs['width'] if 'width' in kwargs else ""
        self.id                 = kwargs['id'] if 'id' in kwargs else None
        self.isVisible          = kwargs['isVisible'] if 'isVisible' in kwargs else None

    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'Column'
    
    @classmethod
    def get_type(cls):
        return 'Column'

