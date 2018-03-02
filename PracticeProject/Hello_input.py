# encoding=utf8
# 函数input()的工作原理
# message = input("muscle , It strengthens your heart, lungs, and muscles. ")
# print(message)


# # while循环
# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# 	current_number +=1 


# # 让用户选择何时退出
# prompt = "\nTell me something, and I will repeat it back to you:" 
# prompt += "\nEnter 'quit' to end the program. "
# message = "" 
# while message != 'quit':
# 	message = input(prompt) 
# 	print(message)

# 在列表之间移动元素
# 首先 创建一个待验证用户列表
# # 和一个用于存储已验证用户的空列表 
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# #   每个用户 直到 有未  用户为止
# # 将每个 过  的列表都移到已  用户列表中  
# while unconfirmed_users:
# 	current_user = unconfirmed_users.pop() 
# 	print("Verifying user: " + current_user.title())
# 	confirmed_users.append(current_user)
# # 显示所有已  的用户
# print("\nThe following users have been confirmed:") 

# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())


# # 删除包含特定值的所有列表元素
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
# print(pets)
# while 'cat' in pets:
# 	pets.remove('cat')
# 	print(pets)



# # 使用用户输入来填充字典
# responses = {}
# # 设置一个标志 指出调查是否继续 
# polling_active = True
# while polling_active:
# 	# 提示输入被调查者的名字和回答
# 	name = input("\nWhat is your name? ")
# 	response = input("Which mountain would you like to climb someday? ")
# 	# 将答卷存储在字典中
# 	responses[name] = response
# 	# 看看是否还有人要参与调查
# 	repeat = input("Would you like to let another person respond? (yes/ no) ")
# 	if repeat == 'no':
# 		polling_active = False
# 		# 调查结束，显示结果
# 		print("\n--- Poll Results ---")
# 		for name, response in responses.items():
# 			print(name + " would like to climb " + response + ".")



# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
# from PIL import Image, ImageDraw, ImageFont

# def add_num(img):
#     draw = ImageDraw.Draw(img)
#     myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
#     fillcolor = "#ff0000"
#     width, height = img.size
#     draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
#     img.save('result.jpg','jpeg')

#     return 0
# if __name__ == '__main__':
#     image = Image.open('image.jpg')
#     add_num(image)


# #  实参和形参 ---------- 位置实参
# def describe_pet(animal_type, pet_name):
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')


# # 关键字实参
# def describe_pet(animal_type, pet_name):
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type = 'hmster', pet_name = 'harry')


# # 返回简单值
# def get_formatted_name(first_name,last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()

# musican = get_formatted_name('jimi', 'hendrix')
# print(musican)


# # 让实参变成可选的
# def get_formatted_name(first_name, middle_name, last_name):
# 	full_name = first_name + ' ' + middle_name + ' ' + last_name
# 	return full_name.title()

# musican = get_formatted_name('john', 'lee', 'hooker')
# print(musican)






















































































