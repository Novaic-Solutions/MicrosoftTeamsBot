import tornado.escape
import tornado.httpclient
import tornado.web
import json

from botbuilder.schema import Activity

from models.sessions.http.httpModels import RequestObject
from bot.botAdapter import DevopsAdapter



class ApiMessages(tornado.web.RequestHandler):

    def initialize(self, messageQueue):
        self.messageQueue = messageQueue
        #self.adapter = DevopsAdapter()

    #----------------------------------------------------------------------------------------------------
    async def post(self):

        if "application/json" in self.request.headers["Content-Type"]:
            reqBody = json.loads(self.request.body)

        else:
            self.clear()
            self.set_status(status_code=415)
            self.flush()
            self.finish()
            return

        auth_header = self.request.headers["Authorization"] if "Authorization" in self.request.headers else ""

        #------------------------------------------------------------------------
        #         #   Create the activity object
        #------------------------------------------------------------------------
        newRequestObject = RequestObject(reqBody, auth_header)

        
        self.messageQueue.put_nowait(newRequestObject)

        self.set_status(status_code=201)
        self.write("Success")