#JS  object notation
#ele é estruturas por chaves e valores (dicionarios)

#Json e usado para trocar informaçoes entre sistemas backend
# e o formato ultilizada pelas APIs 
#capturar as informaçoes da internet 

#capturar umas informaçao da internet
import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'

#capturar essas informaçoes em dados json 

pega_json = urllib.request.urlopen(url).read().decode()

##converter esses valore em dicionarios para manipulaçao 

dic_json = json.loads(pega_json)

##iterar os valores do dicionario

for c in dic_json.values():
    print(c)

print(dic_json)

for p in dic_json['people']:
    print(p['name'])

## cria um arquivo json com os valores extraidos

with open('arquivos/nomes.json','w+') as f:
    json.dump(dic_json,f,indent=4)
    