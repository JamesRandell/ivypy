from ivyorm import Datasource

db: dict = {
    "database":"test",
    "host":"localhost",
    "user":"root",
    "password":"root",
    "port":"5432"
}
test = Datasource('test_schema.json', db)
'''
#test.drop()
#test.create()
arr = {'addressID':100,'fdfd':1,'code':'something'}

result = test.insert(arr)
#print(test.id)


#test.where([['id','178','=','OR']])
#test.where([['id','177','=']])
test.field(['ID','code']).order([['ID','DESC']]).limit(3).select()


arr = {'addressID':100,'code':'else'}
test.update(arr)
'''

orm = Datasource('test_schema.json', db)
orm.where(['ID', 1])
orm.select()