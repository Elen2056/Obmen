#Выводим красиво с помощью PrettyPrinter

import requests
import json
import pprint

# настраиваем PrettyPrinter
p = pprint.PrettyPrinter(indent=4)  # indent=4 - значит отступ в 4 пробела

result = requests.get('https://open.er-api.com/v6/latest/USD')
data = json.loads(result.text)

p.pprint(data)  # "красиво" выводим на экран данные
