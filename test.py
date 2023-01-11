from ivyorm import Datasource

test = Datasource('test_schema.json')

#test.drop()
#test.create()
arr = {'addressID':100,'fdfd':1,'code':'something'}

result = test.insert(arr)
#print(test.id)


#test.where([['id','178','=','OR']])
#test.where([['id','177','=']])
test.field(['ID','code']).order([['ID','DESC']]).limit(3).select()
print(123)
print(test.data)
print(456)

arr = {'addressID':100,'code':'something else','ID':2}
test.update(arr)

print(987)
print(test.error)
