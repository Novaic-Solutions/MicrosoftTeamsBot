import json
import copy

import config

from os import listdir
from os.path import isfile, join

from models.cards.cardModels import CardObj
from models.baseModel import Base

class CardActions(Base):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)


    #8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    def getCurrentQueuePosition(pos):
        queueCard = config.CURRENT_SESSIONS['cards']['queuePosition']['cardObj']
        queueCard.body[0]['columns'][1]['items'][0]['text'] = str(pos)
        return queueCard