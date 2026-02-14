import json
from botbuilder.schema import Activity

from models.baseModel import Base


class RequestBase(Base):
    '''
        Base class for all HTTP Requests coming in to the bot from the web server.

        Any incoming HTTP request from MS Teams will be converted to this, and from there
        it will be determined which type of request was sent.
    '''
    #----------------------------------------------------------------------------------------------------
    def _to_dict(self):
        newDict = dict()
        for key, value in self.__dict__.items():
            if value is None:
                continue
            else:
                if key == "from_property":
                    newKey = "from"
                else:
                    newKey=key
                newDict[newKey] = self.dictify(value)
        return newDict
    #----------------------------------------------------------------------------------------------------
    def _to_json(self):
        return json.dumps(self._to_dict())
    
    #----------------------------------------------------------------------------------------------------
    def _to_acitivity(self):
        return Activity().deserialize(self._to_dict())

    #----------------------------------------------------------------------------------------------------
    @classmethod
    def newRequestObject(cls, reqBody):
        if reqBody['type'] == "message":
            return ChatMessage(cls, **reqBody)
        else:
            TypeError(f"Unknown Request Type: {reqBody['type']}")

#---------------------------------------------------------------------------------------------------------------
class RequestObject(RequestBase):

    def __init__(self, activity, auth_header):
        super().__init__()
        self.activity = super().newRequestObject(activity)
        self.auth_header = auth_header

#---------------------------------------------------------------------------------------------------------------
class ChatMessage(RequestBase):
    '''       
    '''

    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.attachments                        = [Attachment(**x) for x in kwargs['attachments']] if 'attachments' in kwargs else None
        self.body                               = kwargs['body'] if 'body' in kwargs else None
        self.callerId                           = kwargs['callerId'] if 'callerId' in kwargs else None
        self.channelData                        = ChannelData(**kwargs['channelData']) if 'channelData' in kwargs else None
        self.channelId                          = kwargs['channelId'] if 'channelId' in kwargs else None
        self.conversation                       = Conversation(**kwargs['conversation']) if 'conversation' in kwargs else None
        self.entities                           = [Entity(**x) for x in kwargs['entities']] if 'entities' in kwargs else None
        self.from_property                      = FromProperty(**kwargs['from']) if 'from' in kwargs else None
        self.id                                 = kwargs['id'] if 'id' in kwargs else None
        self.locale                             = kwargs['locale'] if 'locale' in kwargs else None
        self.localTimestamp                     = kwargs['localTimestamp'] if 'localTimestamp' in kwargs else None
        self.localTimezone                      = kwargs['localTimezone'] if 'localTimezone' in kwargs else None
        self.recipient                          = Recipient(**kwargs['recipient']) if 'recipient' in kwargs else None
        self.replyToId                          = kwargs['replyToId'] if 'replyToId' in kwargs else None
        self.serviceUrl                         = kwargs['serviceUrl'] if 'serviceUrl' in kwargs else None
        self.text                               = kwargs['text'] if 'text' in kwargs else None
        self.textFormat                         = kwargs['textFormat'] if 'textFormat' in kwargs else None
        self.timestamp                          = kwargs['timestamp'] if 'timestamp' in kwargs else None
        self.type                               = kwargs['type'] if 'type' in kwargs else None
        self.value                              = kwargs['value'] if 'value' in kwargs else None

#---------------------------------------------------------------------------------------------------------------
class Attachment(RequestBase):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.contentType                        = kwargs['contentType'] if 'contentType' in kwargs else None
        self.contentUrl                         = kwargs['contentUrl'] if 'contentUrl' in kwargs else None
        self.content                            = kwargs['content'] if 'content' in kwargs else None
        self.name                               = kwargs['name'] if 'name' in kwargs else None
        self.thumbnailUrl                       = kwargs['thumbnailUrl'] if 'thumbnailUrl' in kwargs else None

#---------------------------------------------------------------------------------------------------------------
class Entity(RequestBase):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.country                            = kwargs['country'] if 'country' in kwargs else None
        self.locale                             = kwargs['locale'] if 'locale' in kwargs else None
        self.platform                           = kwargs['platform'] if 'platform' in kwargs else None
        self.timezone                           = kwargs['timezone'] if 'timezone' in kwargs else None
        self.type                               = kwargs['type'] if 'type' in kwargs else None

#---------------------------------------------------------------------------------------------------------------
class ChannelData(RequestBase):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.teamsChannelId                     = kwargs['teamsChannelId'] if 'teamsChannelId' in kwargs else None
        self.teamsTeamId                        = kwargs['teamsTeamId'] if 'teamsTeamId' in kwargs else None
        self.channel                            = kwargs['channel'] if 'channel' in kwargs else None
        self.legacy                             = kwargs['legacy'] if 'legacy' in kwargs else None
        self.source                             = kwargs['source'] if 'source' in kwargs else None
        self.team                               = kwargs['team'] if 'team' in kwargs else None
        self.tenant                             = kwargs['tenant'] if 'tenant' in kwargs else None

#---------------------------------------------------------------------------------------------------------------
class FromProperty(RequestBase):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.id                                 = kwargs['id'] if 'id' in kwargs else None
        self.name                               = kwargs['name'] if 'name' in kwargs else None
        self.aadObjectId                        = kwargs['aadObjectId'] if 'aadObjectId' in kwargs else None

#---------------------------------------------------------------------------------------------------------------
class Recipient(RequestBase):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.id                                 = kwargs['id'] if 'id' in kwargs else None
        self.name                               = kwargs['name'] if 'name' in kwargs else None

#---------------------------------------------------------------------------------------------------------------
class Conversation(RequestBase):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.isGroup                            = kwargs['isGroup'] if 'isGroup' in kwargs else True
        self.conversationType                   = kwargs['conversationType'] if 'conversationType' in kwargs else None
        self.id                                 = kwargs['id'] if 'id' in kwargs else None
        self.tenantId                           = kwargs['tenantId'] if 'tenantId' in kwargs else None
        self.name                               = kwargs['name'] if 'name' in kwargs else None

