# # 字典
# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'],alien_0['points'])



# # 遍历字典
# user_0 = {
# 	'username' : 'efermi',
# 	'first' : 'enrico',
# 	'last' : 'fermi',
# }

# for key, value in user_0.items():
# 	print("\nKey: " + key)
# 	print("Value: " + value)

# # 遍历字典中的所有键
# favotite_languages = {
# 	'jen' : 'python',
# 	'sarah' : 'c',
# 	'edward' : 'ruby',
# 	'phil' : 'python',
# }

# friends = ['phil', 'sarah']
# for name in favotite_languages.keys():
# 	print(name.title())

# 	if name in friends:
# 		print(" Hi " + name.title() + ", I see your favorite language is" + favotite_languages[name].title() + "!")


# # 嵌套
# alien_0 = {
# 	'color' : 'green',
# 	'points' : '5',
# }
# alien_1 = {
# 	'color' : 'yellow',
# 	'points' : '15',
# }
# alien_2 = {
# 	'color' : 'red',
# 	'points' : '25',
# }

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
# 	print(alien)


# # 字典中存储列表
# # 存储所点比 的信息  
# pizza = {
# 	'crust': 'thick',
# 	'toppings': ['mushrooms', 'extra cheese'],
# }
# # 概述所点的比
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
# "with the following toppings:")

# for topping in pizza['toppings']:
#  	print("\t" + topping)

# # 在字典中存储字典
# users = {
# 	'aeinstein' : {
# 	'first' : 'albert',
# 	'last' : 'einstein',
# 	'location' : 'princeton',
# 	},
# 	'mcurie' : {
# 	'first' : 'marie',
# 	'last' : 'curie',
# 	'location' : 'paris',
# 	},

# }

# for username, user_info in users.items():
	
# 	print("\nUserName: " + username)
# 	full_name = user_info['first'] + " " + user_info['last']
# 	location = user_info['location']

# 	print("\tFull name: " + full_name.title())
# 	print("\tLocation: " + location.title())


# ---------------函数---------------
# 定义函数
# def greet_user():
# 	print("still!")

# greet_user()


# # 向函数传递信息
# def greet_user(username):
# 	print("Hello, " + username.title() + "!")

# greet_user('Dordly')






























































































