tuple1=('dinesh','cbit',7.0,9392382020, [1,2,3])
print(tuple1)
print(tuple1[2])
print(tuple1[-1])
print(len(tuple1))
print(tuple1.count('Dinesh'))


tuple2 = ( 10,3.14,'true','hello',[1,2,3,],("a","b","c"))

print("Integer:",tuple2[0])
print("Float:",  tuple2[1])
print("Boolean:",tuple2[2])
print("String:", tuple2[3])
print("List:",   tuple2[4])
print("Tuple:",  tuple2[5])

print( tuple2[4][1])
print( tuple2[5][2])
print(len(tuple2))
print(tuple2.count('hello'))

set1={1,2,3,1,2,3,'dinesh',2.02}
set1.add(5)
print(set1)

dict1={'name':'dinesh','age':21,'collage':'cbit','add':'vkb'}
print(dict1['name'])
print(dict1['age'])
print(dict1['add'])
print(dict1)

dict2={(1,2,3):'tuple'}
print(dict2)

dict3={'name':'dinesh','age':21,'collage':'cbit','add':'vkb'}
print(dict3.keys())
print(dict3.items())
print(dict3.values())


froset=frozenset((1,2,3,4,5,1,2,3,4,5))
print(froset)