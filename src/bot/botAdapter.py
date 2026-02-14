import asyncio

from botbuilder.core.bot_framework_adapter import BotFrameworkAdapterSettings
import config
import sys

from typing import Callable
from datetime import datetime

from bot.botHandler import BotLogic

from botbuilder.core import BotFrameworkAdapterSettings, TurnContext, BotFrameworkAdapter
from botbuilder.schema import Activity, ActivityTypes


class DevopsAdapter(BotFrameworkAdapter):

    def __init__(self, *args, **kwargs):
        SETTINGS = BotFrameworkAdapterSettings(config.CONFIG_OPTS['clientId'], 
                                               config.CONFIG_OPTS['clientSecretValue'])

        super().__init__(SETTINGS, *args, **kwargs)

        self.bot_logic = BotLogic()


    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    # Catch-all for errors.
    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    async def on_error(self, context: TurnContext, error: Exception):
        #888888888888888888888888888888888888888888888888888888888888888888888888888
        # This check writes out errors to console log .vs. app insights.
        # NOTE: In production environment, you should consider logging this to Azure
        #       application insights.
        #888888888888888888888888888888888888888888888888888888888888888888888888888
        print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)

        #888888888888888888888888888888888888888888888888888888888888888888888888888
        # Send a message to the user
        #888888888888888888888888888888888888888888888888888888888888888888888888888
        await context.send_activity("The bot encountered an error or bug.")
        await context.send_activity("To continue to run this bot, please fix the bot source code.")

        #888888888888888888888888888888888888888888888888888888888888888888888888888
        # Send a trace activity if we're talking to the Bot Framework Emulator
        #888888888888888888888888888888888888888888888888888888888888888888888888888
        if context.activity.channel_id == "emulator":
            #88888888888888888888888888888888888888888888888888888888888888888888888
            # Create a trace activity that contains the error object
            #88888888888888888888888888888888888888888888888888888888888888888888888
            trace_activity = Activity(
                label="TurnError",
                name="on_turn_error Trace",
                timestamp=datetime.utcnow(),
                type=ActivityTypes.trace,
                value=f"{error}",
                value_type="https://www.botframework.com/schemas/error",
            )

            #88888888888888888888888888888888888888888888888888888888888888888888888
            # Send a trace activity, which will be displayed 
            # in Bot Framework Emulator
            #88888888888888888888888888888888888888888888888888888888888888888888888
            await context.send_activity(trace_activity)


    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    # Overrides the Adapter's process_activity() method
    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    async def process_activity(self, req, auth_header: str):
        '''
            Overrides the Adapter's process_activity() method
        '''
        return await super().process_activity(req, auth_header, self.bot_logic.sort_activity)