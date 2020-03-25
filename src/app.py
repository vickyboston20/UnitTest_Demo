from src.configmain import DataMap

data_map = DataMap("config.cfg")
path = data_map.get_location()
token = data_map.get_token()
print(f"{path}/empty.txt")
print(token)
