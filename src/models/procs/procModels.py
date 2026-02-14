# from models.baseModels import Base

# #------------------------------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------------------------------
# class TaskRequest(Base):
#     '''
#         A request sent to a task process to be executed.
#     '''
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.taskName = kwargs['taskName'] if 'taskName' in kwargs else "taskName"
#         self.taskType = kwargs['taskType'] if 'taskType' in kwargs else "taskType"
#         self.taskData = kwargs['taskData'] if 'taskData' in kwargs else None

# #------------------------------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------------------------------
# class TaskResponse(Base):
#     '''
#         A response from a task process after execution.

#         taskName:       Name of the this task.  
#     '''
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.taskName = kwargs['taskName'] if 'taskName' in kwargs else "taskName"
#         self.taskData = kwargs['taskData'] if 'taskData' in kwargs else None
#         self.taskSuccess = kwargs['taskSuccess'] if 'taskSuccess' in kwargs else False
#         self.taskResult = kwargs['taskResult'] if 'taskResult' in kwargs else None
#         self.taskError = kwargs['taskError'] if 'taskError' in kwargs else None

# #------------------------------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------------------------------------
# class ProcRequest(Base):
#     '''
#         Request for managing the Task Processes

#         procName:   Name of the process to be managed.
#         taskType:   Type of task to be executed.
#         action:     Action to be performed on the process.
#         total:      Total number of processes to be started.
#         target:     Target function to be executed.
#     '''
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.procName       = kwargs['procName'] if 'procName' in kwargs else ""
#         self.taskType       = kwargs['taskType'] if 'taskType' in kwargs else ""
#         self.action         = kwargs['action'] if 'action' in kwargs else ""
#         self.total          = kwargs['total'] if 'total' in kwargs else 1
#         self.target         = kwargs['target'] if 'target' in kwargs else None