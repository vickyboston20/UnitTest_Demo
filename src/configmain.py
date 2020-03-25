import configparser as cfg


class DataMap:
    def __init__(self, config):
        self.location = self.read_location_from_config_file(config)
        self.token = self.read_token_from_config_file(config)

    @staticmethod
    def read_location_from_config_file(config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('DataMapperSection', 'location')

    @staticmethod
    def read_token_from_config_file(config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('DataMapperSection', 'token')

    def get_location(self):
        return self.location

    def get_token(self):
        return self.token
