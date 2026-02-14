import tornado.web
import asyncio
import traceback
import tornado.process
import tornado.netutil
import config
from datetime import datetime

from tornado.options import options, define
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.schema import Activity, ActivityTypes

from web.msgs import ApiMessages
 


define("debug", default=False, help="run in debug mode")

#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#   HTTP Webserver, any activity in teams is sent to this endpoint.
#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
class DevopsBotWebServer():

    def __init__(self, requestQueue):
        self.requestQueue = requestQueue

    async def start(self):
        '''
            Starts the Tornado HTTP Webserver
        '''
        #NOTE: Here, instead of passing in the adapter and bot, we pass in the activityQueue for multiproc
        app = tornado.web.Application(
            [
                #(r"/api/messages", ApiMessages, dict(adapt=self.adapter, bot=self.bot)),
                (r"/api/messages", ApiMessages, dict(messageQueue=self.requestQueue)),
            ],
            debug=options.debug,
        )

        http_server = tornado.httpserver.HTTPServer(app)

        http_server.listen(config.CONFIG_OPTS['port'])

        await asyncio.Event().wait()