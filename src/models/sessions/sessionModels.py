import uuid
from models.baseModel import Base

class SessionObject(Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sessionId                  = kwargs['sessionId'] if 'sessionId' in kwargs else str(uuid.uuid4())


class ChannelConversation(SessionObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tenantId                   = kwargs.get('tenantId', None)
        self.channelId                  = kwargs.get('channelId', None)
        self.channelName                = kwargs.get('channelName', None)
        self.channelType                = kwargs.get('channelType', None)


class GroupChatConversation(SessionObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



