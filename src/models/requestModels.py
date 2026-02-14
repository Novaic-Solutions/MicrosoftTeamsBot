from models.baseModel import Base

class RequestObj(Base):
    '''
    
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.userName       = kwargs['userName'] if 'userName' in kwargs else None
        self.teamName       = kwargs['teamName'] if 'teamName' in kwargs else None
        self.requestType    = kwargs['requestType'] if 'requestType' in kwargs else None
        self.channelId      = kwargs['channelId'] if 'channelId' in kwargs else None
        self.channelName    = kwargs['channelName'] if 'channelName' in kwargs else None
        self.requestData    = kwargs['requestData'] if 'requestData' in kwargs else None

class RequestData(Base):
    '''
    
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
