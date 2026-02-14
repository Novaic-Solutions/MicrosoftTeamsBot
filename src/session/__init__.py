import json
from pathlib import Path
from os import listdir
from os.path import isfile, join


import config
from core.cards.cardActions import CardActions
from models.cards.cardModels import CardObj


SESSION = dict()

#-------------------------------------------------------------------------------------------------------
def _prepare_sessions():
    SESSION['cards'] = loadCardFiles()
    #print(f"Cards: {SESSION['cards']}")

    #print("\n\n TESTING")
    test = SESSION['cards']['adaptiveTest']['cardObj']._to_dict()
    #print(test)

#-------------------------------------------------------------------------------------------------------
def loadCardFiles():
        '''
            Card Files are stored in dictionarys.
            Schema:
                {
                    "cardName":   {
                        "cardObj": Class relating to the card type,
                        "cardValueId": Either the valueId of the card or NON_SUBMIT. NON_SUBMIT is used for cards that do not have a submit action.
                    },
                }
        '''
        onlyfiles = [f for f in listdir(config.CONFIG_OPTS['cardFileDirectory']) if isfile(join(config.CONFIG_OPTS['cardFileDirectory'], f))]
        allCards = dict()

        for cardFile in onlyfiles:
            cardName = cardFile.split('.')[0]

            with open(config.CONFIG_OPTS['cardFileDirectory']+"\\"+cardFile, "r+") as cardFileObj:
                #print(f"\nLoading Card: {cardName}")
                
                valueId = "NON_SUBMIT"
                cardDict = json.load(cardFileObj)

                if "actions" in cardDict:
                    for act in cardDict['actions']:
                        if act['type'] == "Action.Submit":
                            valueId = act['data']['id']

                allCards[cardName] = {
                    "cardObj": CardObj._from_dict(cardDict),
                    "cardValueId": valueId
                }

                #print(f"Card Loaded: {allCards[cardName]['cardObj']}")

        return allCards