import config
from models.baseModel import Base
from models.cards.cardModels import CardObj


class AdaptiveCardObj(CardObj):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema                             = "http://adaptivecards.io/schemas/adaptive-card.json"
        self.version                            = config.CONFIG_OPTS['cardSchemaVersion']
        self.type                               = "AdaptiveCard"
        self.actions                            = kwargs['actions'] if 'actions' in kwargs else list()
        self.body                               = kwargs['body'] if 'body' in kwargs else list()


    @classmethod
    def get_class_type(cls, typeCheck):
        return typeCheck == 'AdaptiveCard'