import json
import uuid
from datetime import datetime
from models.baseModel import Base

class SupportObj(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channelId      = kwargs['channelId'] if 'channelId' in kwargs else None
        self.channelName    = kwargs['channelName'] if 'channelName' in kwargs else None
        self.userName       = kwargs['userName'] if 'userName' in kwargs else None
        self.teamName       = kwargs['teamName'] if 'teamName' in kwargs else None
        self.queuePosition  = kwargs['queuePosition'] if 'queuePosition' in kwargs else None
        self.issueId        = kwargs['issueId'] if 'issueId' in kwargs else None
        self.issueObj       = SupportIssueObj(kwargs['issueObj']) if 'issueObj' in kwargs else None

    @classmethod
    def _new_object(cls, data):
        pass


class SupportIssueObj(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.summary        = kwargs['summary'] if 'summary' in kwargs else None
        self.pipelineUrl    = kwargs['pipelineUrl'] if 'pipelineUrl' in kwargs else None
        self.repoName       = kwargs['repoName'] if 'repoName' in kwargs else None
        self.title          = kwargs['title'] if 'title' in kwargs else None
        self.status         = kwargs['status'] if 'status' in kwargs else None
        self.assignedTo     = kwargs['assignedTo'] if 'assignedTo' in kwargs else None