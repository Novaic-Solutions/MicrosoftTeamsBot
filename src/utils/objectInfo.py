
def printActivityInfo(turn_context):
    '''
        Prints the info and objects stored within a turn context.
    '''

    formattedString = """
        --------------- TURN CONTEXT ---------------
        activity.action: {activityAction}
        activity.attachments: {activityAttachments}
        activity.caller_id: {activityCallerId}
        activity.channel_id: {activityChannelId}
        activity.code: {activityCode}
        activity.conversation: {activityConversation}
        activity.delivery_mode: {activityDeliveryMode}
        activity.expiration: {activityExpiration}
        activity.id:   {activityId}
        activity.input_hint: {activityInputHint}
        activity.label: {activityLabel}
        activity.listen_for: {activityListenFor}
        activity.local_timestamp: {activityLocalTimestamp}
        activity.local_timezone: {activityLocalTimezone}
        activity.members_added: {activityMembersAdded}
        activity.members_removed: {activityMembersRemoved}
        activity.name: {activityName}
        activity.recipient: {activityRecipient}
        activity.reply_to_id: {activityReplyToId}
        activity.service_url: {activityServiceUrl}
        activity.speak: {activitySpeak}
        activity.summary: {activitySummary}
        activity.timestamp: {activityTimestamp}
        activity.text: {activityText}
        activity.topic_name: {activityTopicName}
        activity.type: {activityType}
        activity.value_type: {activityValueType}
        ------------------------------------------
        ------------------------------------------
        """
    tContAct = turn_context.activity.as_dict()

    print(formattedString.format(
        activityAction=turn_context.activity.action,
        activityAttachments=getAttachmentInfo(turn_context.activity.attachments),
        activityCallerId=turn_context.activity.caller_id,
        activityChannelId=turn_context.activity.channel_id,
        activityCode=turn_context.activity.code,
        activityConversation = getConversationAccountInfo(turn_context.activity.conversation) if 'conversation' in tContAct else "None",
        activityDeliveryMode=turn_context.activity.delivery_mode,
        activityExpiration=turn_context.activity.expiration,
        activityId=turn_context.activity.id,
        activityInputHint=turn_context.activity.input_hint,
        activityLabel=turn_context.activity.label,
        activityListenFor=turn_context.activity.listen_for,
        activityLocalTimestamp=turn_context.activity.local_timestamp,
        activityLocalTimezone=turn_context.activity.local_timezone,
        activityMembersAdded=getChannelAccountInfo(turn_context.activity.members_added) if 'members_added' in tContAct else "None",
        activityMembersRemoved=getChannelAccountInfo(turn_context.activity.members_removed) if 'members_removed' in tContAct else "None",
        activityName=turn_context.activity.name,
        activityRecipient=getChannelAccountInfo(turn_context.activity.recipient) if 'recipient' in tContAct else "None",
        activityReplyToId=turn_context.activity.reply_to_id,
        activityServiceUrl=turn_context.activity.service_url,
        activitySpeak=turn_context.activity.speak,
        activitySummary=turn_context.activity.summary,
        activityTimestamp=turn_context.activity.timestamp,
        activityText=turn_context.activity.text,
        activityTopicName=turn_context.activity.topic_name,
        activityType=turn_context.activity.type,
        activityValueType=turn_context.activity.value_type
    ))


def getAttachmentInfo(attachments):
    '''
        Prints the info and objects stored within an attachment.
    '''
    attachmentStrings = ""
    
    if not attachments:
        return attachmentStrings
    
    for attachment in attachments:
        formattedString = """
            --------------- ATTACHMENT ---------------
            attachment.content_type: {attachmentContentType}    
            attachment.content_url: {attachmentContentUrl}
            attachment.content: {attachmentContent}
            attachment.name: {attachmentName}
            attachment.thumbnail_url: {attachmentThumbnailUrl}
            ------------------------------------------""".format(
            attachmentContentType=attachment.content_type,
            attachmentContentUrl=attachment.content_url,
            attachmentContent=attachment.content,
            attachmentName=attachment.name,
            attachmentThumbnailUrl=attachment.thumbnail_url
        )
        attachmentStrings += formattedString

    return attachmentStrings


def getChannelAccountInfo(channelAccount):
    '''
        Prints the info and objects stored within a channel account.
    '''

    if not channelAccount:
        return "None"

    formattedString = """
        -------------- CHANNEL ACCOUNT ----------------
        channel_account.id: {channelAccountId}
        channel_account.name: {channelAccountName}
        channel_account.role: {channelAccountRole}
        ------------------------------------------------""".format(
        channelAccountId=channelAccount.id,
        channelAccountName=channelAccount.name,
        channelAccountRole=channelAccount.role
    )
    return formattedString


def getConversationAccountInfo(conversationAccount):
    '''
        Prints the info and objects stored within a conversation account.
    '''

    if not conversationAccount:
        return "None"

    formattedString = """
        -------------- CONVERSATION ACCOUNT ----------------
        conversation_account.conversation_type: {conversationAccountConversationType}
        conversation_account.id: {conversationAccountId}
        conversation_account.is_group: {conversationAccountIsGroup}
        conversation_account.name: {conversationAccountName}
        conversation_account.role: {conversationAccountRole}
        ----------------------------------------------------""".format(
        conversationAccountConversationType=conversationAccount.conversation_type,
        conversationAccountId=conversationAccount.id,
        conversationAccountIsGroup=conversationAccount.is_group,
        conversationAccountName=conversationAccount.name,
        conversationAccountRole=conversationAccount.role
    )
    return formattedString


def getConversationReferenceInfo(conversationReference):
    '''
        Prints the info and objects stored within a conversation reference.
    '''

    if not conversationReference:
        return "None"

    formattedString = """
        conversation_reference.activity_id: {conversationReferenceActivityId}
        conversation_reference.bot: {conversationReferenceBot}
        conversation_reference.channel_id: {conversationReferenceChannelId}
        conversation_reference.conversation: {conversationReferenceConversation}
        conversation_reference.locale: {conversationReferenceLocale}
        conversation_reference.service_url: {conversationReferenceServiceUrl}
        conversation_reference.user: {conversationReferenceUser}
    """.format(
        conversationReferenceActivityId=conversationReference.activity_id,
        conversationReferenceBot=conversationReference.bot,
        conversationReferenceChannelId=conversationReference.channel_id,
        conversationReferenceConversation=conversationReference.conversation,
        conversationReferenceLocale=conversationReference.locale,
        conversationReferenceServiceUrl=conversationReference.service_url,
        conversationReferenceUser=conversationReference.user
    )
    return formattedString


def displayInfo(obj):
    print("----------------------------------------------------------------------------------------------")
    print("-----                                  Object Info                                       -----")
    print("----------------------------------------------------------------------------------------------")
    objDictionary = obj.as_dict()
    template = "{:<40} --- {}"

    for key,val in objDictionary.items():
        print(template.format(key,val))
        print("-----------------------------------------------------")