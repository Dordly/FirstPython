# message = "Hello Eric, would you like to learn some Python today?"
# print(message)

# name = "ada loveLace"
# print(name.upper()) # upper()--大写   lower() --小写 title() -- 首字母大写
# print(name.lower())
# print(name.title(),name.lower())

# famous_person = 'Albert Einstein once said,"A person who never made a mistake never tried anything new."'
# messageTwo = famous_person
# print(messageTwo)

# nameNot = "\t Dordly With Dordly \n"

# print(nameNot)
# print(nameNot.lstrip())
# print(nameNot.rstrip())
# print(nameNot.strip())

# 列表
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# # 访问列表元素
# print(bicycles[0])
# print(bicycles[0].title())

# # 修改列表元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# # 在列表中添加元素
# motorcycles.append('ducati')
# print(motorcycles)

# # 在列表中插入元素
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# # 删除元素
# del motorcycles[0]
# print(motorcycles)

# # 使用pop()删除元素
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# # pop()可以指出最后的元素
# last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a " + last_owned.title() + ".")


# # 弹出列表中任何位置处的元素
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# print(motorcycles)

# # 注：使用了pop()之后，列表汇总的元素就不再存在pop()后的元素
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + "is too expensive for me")


# 组织列表
# 使用方法sort()来对列表进行----永久性排序----
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# # sort()按字母顺序排序
# cars.sort()
# print(cars)
# sort()按字母顺序倒叙-当reverse = True
# cars.sort(reverse=True)
# print(cars)

# # 使用函数sorted()来对列表进行临时性排序
# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# # 反转列表元素的排列顺序 reverse()
# cars.reverse()
# print(cars)

# 确定列表的长度
len(cars)
print(len(cars))


















