dictTest = {
    "key1":"value1",
    "key2":"value2",
    }
print('dictTest=')
print(dictTest)

lol = [['a','b'],['c','d'],['e','f']]
print(dict(lol))

dict2={
    'keyA':'valueA',
    'keyB':'valueB',
    }
print('value A=')
print(dict2.get('keyA','No keyA'))
print('value C=')
print(dict2.get('keyC','No keyC'))

dict2['keyA']='valueA2'
dict2['keyC']='valueC'
print(dict2)

print('value A=')
print(dict2.get('keyA','No keyA'))
print('value C=')
print(dict2.get('keyC','No keyC'))

addDict = {'keyD':'valueD','keyE':'valeuE'}
dict2.update(addDict)
print (dict2)

dict3={
    'keyI':'valueI',
    'keyII':'valueII',
    'keyIII':'valueIII',
    'keyIV':'valueIV',
    'keyV':'valueV',
    }
print(dict3)

del dict3['keyI']
print (dict3)

newDict3=dict3.copy()

dict3.clear()
print('dict3=')
print(dict3)
print("newDict3:")
print(newDict3)

print('for loop')
for d in newDict3:
    print(d)   #keys
for d in newDict3.values():
    print(d)   #values
for d in newDict3.items():
    print(d)   #items


