import json,xmltodict

print('input the file path(press Enter to use default file(test.xml))')
path = input('path: ')
if(path==''):
    path='test.xml'
file = open(path,'r')
data=file.read().replace('\n', '')
xml = xmltodict.parse(data, attr_prefix='', cdata_key='')
file.close()

json_data=json.dumps(xml['current'], sort_keys=True, indent=4)

f = open('data.json', 'w')
f.write(json_data)
f.close()

print(json_data)
print('=============================')
print('finished!')
