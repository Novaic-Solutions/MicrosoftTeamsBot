#import logging
import config
#from utils.cardUtils import turnContext
from typing import Union
from botbuilder.core.teams import TeamsActivityHandler
from botbuilder.core import InvokeResponse, TurnContext, CardFactory, MessageFactory
from botbuilder.core.turn_context import TurnContext
from botbuilder.schema import ChannelAccount

from core.messages.handler import MessageHandler


class BotLogic(TeamsActivityHandler):
    def __init__(self, trackingRequest=None, trackingResponse=None):
        super().__init__()
        self.msgs = MessageHandler()
        # For use with multiprocessing later down the line
        self.trackingReqQueue = trackingRequest
        self.trackingRespQueue = trackingResponse


    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    #   Wrapping the Activity Handler's on_turn() method
    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    async def sort_activity(self, turn_context: TurnContext):
        '''
            Sorts the incoming activity based on its type
            Used in place of the built in  on_turn() function
        '''
        print("--- SORT ACTIVITY INSIDE BOTLOGIC ---")
        print("-------------------------------------\n")
        await self.on_turn(turn_context)
        

    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    #   Message in channel
    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    async def on_invoke_activity(self, turn_context: TurnContext) -> InvokeResponse:
        '''
        '''
        print("--- ON INVOKE ACTIVITY INSIDE BOTLOGIC ---")
        await super().on_invoke_activity(turn_context)


    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    #   Message in channeliim
    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    async def on_message_activity(self, turn_context: TurnContext):
        print("--- ON MESSAGE ACTIVITY INSIDE BOTLOGIC ---")
        await self.msgs.printContextInfo(turn_context)

        message, sendUpdate = await self.msgs.determineResponse(turn_context)
        sendUpdate = False

        if message:
            # Replace the last message with the current one
            if sendUpdate:
                await turn_context.update_activity(message)
            
            # Send a new message
            else:
                resourceResponse = await turn_context.send_activity(message)


    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    #   Member joins channel
    #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    async def on_members_added_activity(self, members_added: ChannelAccount, turn_context: TurnContext):
        print("--- ON MEMBERS ADDED ACTIVITY INSIDE BOTLOGIC ---")
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")