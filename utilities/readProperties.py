import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info', 'baseURL')
        return  url

    @staticmethod
    def getUsername():
        username = config.get('common_info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password
