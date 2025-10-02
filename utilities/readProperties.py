import configparser
import os
config = configparser.RawConfigParser()
# config.read("./Configuration/config.ini")

# config_path = os.path.join(os.path.dirname(__file__), "Configuration", "config.ini")
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Configuration", "config.ini")

config.read(config_path)


# config = configparser.RawConfigParser()
# # Go up one directory from 'utilities'
# config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Configuration", "config.ini")
read_files = config.read(config_path)


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

print("Config path:", config_path)
print("Files read:", read_files)
print("Sections found:", config.sections())
