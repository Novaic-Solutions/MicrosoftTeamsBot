import uuid
import logging
from datetime import datetime

from cards import cardGenerator

logger = logging.getLogger("chatbot")

class DataHandler():


	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	#	Class will be used for data sharing across the web and listener.
	#	tenantId = "e45cbcc1-1760-419a-a16b-35802285b3b3"
 	#	a60b73ff-680b-45eb-8577-486ee9352eff
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def __init__(self, tenantId="e45cbcc1-1760-419a-a16b-35802285b3b3"):
		self.settings = self.createSettings(tennant=tenantId)
		self.cards = cardGenerator.generateCards()
		self.currentConversations = dict()
		self.currentQueue = list()
		self.trackedChannels = self.getTrackedChannels()

	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	#	Add a new "conversation" or thread to the session data.
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def addTracking(self, activity):
		logger.info(f"Adding Tracking --> {activity['id']}")
		self.currentQueue.append(activity['id'])
		trackingObj = {
			activity['id']: {
				"channelId": activity['conversation']['id'].split(';')[0],
				"threadId": activity['conversation']['id'],
				"created": datetime.now().isoformat(),
				"lastReply": datetime.now().isoformat(),
				"isSupportChannel": False,
				"issueInfo": {
					"usersName":"",
					"pipelineUrl": "",
					"issueSummary": ""
				},
				"currentFormCard":"",
				"currentCardPos": len(self.currentQueue)-1
			}
		}
		self.currentConversations.update(trackingObj)


	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	#
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def createSettings(self, tennant=""):
		settings = {
							"applicationId": "370af14c-137b-4193-9432-eaf85ddbb231",
							"objectId": "a60b73ff-680b-45eb-8577-486ee9352eff",
							"authUrl": f"https://login.microsoftonline.com/{tennant}/oauth2/v2.0/authorize",
							"tokenUrl": f"https://login.microsoftonline.com/{tennant}/oauth2/v2.0/token",
							"graphUrl":"https://graph.microsoft.com/v1.0",
							"state": str(uuid.uuid4()),
							"session_state": "",
							"code": "",
							"scope": "",
							"clientSecretId": "887bffa9-2897-4436-beba-107da846f95b",
							"clientSecretValue": "",
							"tenantId": tennant,
							"redirectUrl": "https://localhost:3978/auth_callback",
							"accessToken": "",
							"refreshToken": "",
							"teamId": "5f8ed42c-3d50-40b7-9bee-41124ce3d439",
							"channelId": "19%3ad242b3b66b304bfe99e11e8a213e3f54%40thread.skype",
							"serviceAccount": "svcazsp-entauto-devopsbot-poc"
						}
		#	In order to set the FROM field, the permission for Teamwork.Migrate.All is required.
		settings["scope"] = "ChannelMessage.Read.All "
		settings["scope"] +="ChannelMessage.Send "
		settings["scope"] +="ChannelMessage.ReadWrite "
		settings["scope"] +="Channel.ReadBasic.All "
		settings["scope"] +="ChannelMember.Read.All "
		settings["scope"] +="offline_access"

		return settings

	def getTrackedChannels(self):
		channelIds = [
			"19:3990058504e741e2bccfb346368817cd@thread.tacv2"
		]
		return channelIds

	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	#
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def showCurrentValues(self):
		'''
		Used for debugging the current persistent session data. Print it all out
		'''
		logger.debug("------------------------------------------------------------------------")
		logger.debug("                      Current Session Data")
		logger.debug("------------------------------------------------------------------------")
		logger.debug("Settings")
		logger.debug("---------")
		logger.debug("---------")
		for key,val in self.settings.items():
			logger.debug("{:<40} | {:150}".format(str(key),str(val)))
			logger.debug("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

		logger.debug("Tracked Channels")
		logger.debug("-----------------")
		logger.debug("-----------------")
		for chanId in self.trackedChannels:
			logger.debug(chanId)
			logger.debug("------------------------------------------------------------------------------------------------------")
	
		logger.debug(f"Current Queue ---> {self.currentQueue}")


		logger.debug("Current Conversations")
		logger.debug("-------------------------")
		logger.debug("-------------------------")
		for key,val in self.currentConversations.items():
			logger.debug(key)
			logger.debug("---------------")
			for x,y in val.items():
				logger.debug("{:<40}| {:<150}".format(str(x),str(y)))
				logger.debug('-----------------------------')

	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	#
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def updateTracking(self, activity):
		convoId = activity['conversation']['id'].split('=')[1]

		logger.info(f"Updating Tracking --> {convoId}")
		updateInfo = {
			"created": datetime.now().isoformat(),
			"lastReply": datetime.now().isoformat()
		}

		if "value" in activity:
			
			if self.currentConversations[convoId]['currentFormCard'] == activity['reply_to_id']:
				updateInfo.update({"issueInfo":activity['value']})

			else:
				logger.warn("Somehow got a response for a card that doesnt exist? I think? I dont know")

		logger.info(f"Updating Tracking Object: {updateInfo}")
		self.currentConversations[convoId].update(updateInfo)

	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	#
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def checkTrackingStatus(self, activity):
		logger.debug(f"Currently Tracking: {self.currentConversations}")
		conversation = activity['conversation']['id'].split(';')
		channelId = conversation[0]
		conversationId = conversation[1].split('=')[1]

		if channelId in self.trackedChannels:
			
			if conversationId in self.currentConversations:
				self.updateTracking(activity)
				return True, True

			else:
				self.addTracking(activity)
				return False, True

		return False, False

	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	# Updates the issue queue json
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def updateCurrentIssueQueue(self, data):
		#queueList = [self.currentConversations[id]['issueInfo'] for id in self.currentQueue]
		logger.debug(f"New Issue for Queue: \n{data}\n")
		pos = len(self.currentQueue)
		convoId = data['conversation']['id'].split('=')[1]
		self.cards['issueQueue']['cardJson']['body'][1]['rows'].append(cardGenerator.newIssueRow(pos, data['value'], convoId))

	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	#
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def getCurrentPositionCard(self):
		return cardGenerator.getCurrentQueuePosition(len(self.currentQueue))


	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	#	Remove an issue from the queue
	#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	def removeIssueFromQueue(self, id):
		logger.info(f"Removing Issue: {id}")
		del self.cards['issueQueue']['cardJson']['body'][1]['rows'][self.currentConversations[id]['currentCardPos']]
		self.currentQueue.remove(id)
		del self.currentConversations[id]
		# NOTE: Should have the queue position update possibly, because they maintain their number on the card.

	# #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    # #
	# # NOTE: Would like to have these split out into a separate process specifically for managing the
	# #		tracked threads as well as cleaning up and managing the settings data.
	# #
	# #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	# def updatingTrackingStatus(self, message):
	# 	if message['replyToId'] not in self.settings['trackedThreads']:
	# 		newTrackingObj = {
	# 			message['replyToId']: {
	# 				"channelId": message['channelIdentity']['channelId'],
	# 				"teamId":  message['channelIdentity']['teamId'],
	# 				"created": datetime.now().isoformat(),
	# 				"lastReply": datetime.now().isoformat(),
	# 				"replyMessageId": message['id']
	# 			}
	# 		}
	# 		self.settings['trackedThreads'].update(newTrackingObj)
	# 		logger.info(f"Now Tracking {newTrackingObj}")

	# 	elif message['replyToId'] in self.settings['trackedThreads']:
	# 		self.settings['trackedThreads'][message['replyToId']]['replyMessageId'] = message['id']
	# 		self.settings['trackedThreads'][message['replyToId']]['lastReply'] = datetime.now().isoformat()

	# #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	# #
	# #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
	# def checkTrackingStatus(self, message):
	# 	if message['id'] in self.settings['trackedThreads']:
	# 		return True
	# 	return False