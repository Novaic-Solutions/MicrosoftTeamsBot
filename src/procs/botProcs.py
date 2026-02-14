import inspect
import time
import asyncio
import queue
from multiprocessing import Process, JoinableQueue

import config
import session
from web.webServer import DevopsBotWebServer
from bot.botAdapter import DevopsAdapter
#from models.procs.procModels import TaskRequest, TaskResponse, ProcRequest

#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------
class WebServerProcess(Process):
    '''
        Runs the Tornado Web Server whos endpoint is used to receive messages from Teams.
    '''
    def __init__(self,  requestQueue: JoinableQueue, *args, **kwargs):
        super().__init__()
        
        self.requestQueue = requestQueue

    #-------------------------------------------------------------------------------------------------------------------------------
    async def startWebServer(self):
        webserver = DevopsBotWebServer(self.requestQueue)
        await webserver.start()

    #-------------------------------------------------------------------------------------------------------------------------------
    def run(self):
        print("Starting Web Server")
        asyncio.run(self.startWebServer())

#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------
class BotProcess(Process):

    def __init__(self, requestQueue: JoinableQueue, *args, **kwargs):
        super().__init__()
        
        session._prepare_sessions()

        self.requestQueue = requestQueue
        self.botAdapter = DevopsAdapter()

    #-------------------------------------------------------------------------------------------------------------------------------
    def run(self):
        print("Starting Bot Process")
        
        while True:
            
            try:

                incRequest = self.requestQueue.get_nowait()
                self.requestQueue.task_done()

                asyncio.run(self.botAdapter.process_activity(incRequest.activity, incRequest.auth_header))

            except queue.Empty:
                time.sleep(1)
        