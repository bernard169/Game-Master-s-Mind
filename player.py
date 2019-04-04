import team

class Player():
    def __init__(self, playerName, characterName, infos = {}):
        self.__reputation = {}
        self.__infos = infos
        self.__playerName = playerName
        self.__characterName = characterName
        self.__infos = infos

    def editReputation (self, changes):
        pass
    
    def getReputation (self):
        return self.__reputation
    
    def retrieveInfos (self):
        pass
    
    def getInfos (self):
        return self.__infos
        