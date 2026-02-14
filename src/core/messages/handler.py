import config
import session
from botbuilder.core import CardFactory, MessageFactory
from utils import objectInfo
from models.cards.cardModels import CardObj

#logger = logging.getLogger("chatbot")

class MessageHandler():
#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    async def printContextInfo(self, turn_context):
        print("----------------------------------------------------------------------------------------------")
        print("-----               MessageHandler.printContextInfo Turn Context                         -----")
        print("----------------------------------------------------------------------------------------------")
        print("::Context Activity::")
        objectInfo.printActivityInfo(turn_context)
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")
        
#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    async def determineResponse(self, turn_context):
        '''
            This performs the logic to check if a card should be sent or if a card is being responded back to.
        '''
        message = None
        getResponseId = False
        sendUpdate = False
        activity = turn_context.activity.as_dict()

        # Determine if the message is from a group chat or a channel thread
        if activity['conversation']['conversation_type'] == "channel":
            return self.channelChat(message, getResponseId, sendUpdate, activity)

        if activity['conversation']['conversation_type'] == "groupChat":
            return self.groupChat(message, getResponseId, sendUpdate, activity)

#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    def groupChat(self, message, getResponseId, sendUpdate, activity):
        
        # Check if the first character is an !, which will invoke the bot
        if ("text" in activity) and (activity['text'][0] == "!"):
            
            #-------------------------------------------------------
            # Command was issued, mistakenly or not
            # Add in the logic from the GMF repo that allowe me
            # to setup commands and shit with json config files.
            # for now just barf out the queue
            #-------------------------------------------------------
            if activity['text'].lower() == "!queue":
                message = MessageFactory.attachment(CardFactory.adaptive_card(self.dhandler.cards['issueQueue']['cardJson']))
        
        # Card response from the group chat
        if self.isCardResponse(activity):

            if activity['value']['id'] == "issueComplete":
                message = MessageFactory.attachment(CardFactory.adaptive_card(self.dhandler.cards['issueQueue']['cardJson']))
                message.id = activity['id']
                sendUpdate = True

        return message, getResponseId, sendUpdate

#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    def channelChat(self, message, getResponseId, sendUpdate, activity):        
        message = MessageFactory.attachment(CardFactory.adaptive_card(session.SESSION['cards']['supportIssue']['cardObj']._to_dict()))
        sendUpdate = True

        return message, sendUpdate


#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    def isCardResponse(self, activity):

        print("Checking Response to determine if its a response from a card interaction")
        
        if ("value" in activity) and ("text" not in activity):

            print("Its a card response")

            if "id" not in activity['value']:

                print("The card used was missing the id field from the data and should be fixed.")
                return False
        
            return True

        print("Just a normal message")
        return False