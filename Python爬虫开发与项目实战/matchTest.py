# coding:utf-8
import re
# 将正则表达式编译为pattern对象
# pattern = re.compile(r'\d+') 

# result1 = re.match(pattern, '192abc') # 1.  从字符串的开头开始，一直向后匹配，直到找到相同的，不同返回None,否则反之
# if result1:
# 	print (result1.group())
# else:
# 	print ('false1')

# result2 = re.match(pattern,'abc192')
# if result2:
# 	print (result2.group())
# else:
# 	print ('false2')

# result1 = re.search(pattern, 'abc123')  #2. 整体查询搜索
# if result1:
# 	print (result1.group())
# else:
# 	print (false)

# print (re.split(pattern, 'A1B2C3D4'))   # 3. re.split(pattern,string[,maxsplit])按照能够匹配的子串将string分割后返回列表，maxsplit用于指定最大分割次数，若不指定，则全部分割

# print (re.findall(pattern,'A1B2C3D4'))   #4. re.findall(pattern,string[,flags]),搜索整个string，以列表形式返回能匹配的全部子串

# matchiter = re.finditer(pattern, 'A1B2C3D4') #5.  re.finditer(pattern,string[,flags]) 搜索整个String,以迭代器形式返回能匹配的全部Match对象
# for match in matchiter:
# 	print (match.group())

#6. re.sub(pattern,repl,string[,count])
# p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')  # 使用名称引用
# s = 'i say, hello world!'
# print (p.sub(r'\g<word2> \g<word1>', s))
# p = re.compile(r'(\w+) (\w+)') # 使用编号
# print (p.sub(r'\2 \1', s))
# def func(m):
# 	return m.group(1).title() + ' ' + m.group(2).title()
# print (p.sub(func, s))


#7. re.subn(pattern,repl,string[,count])  返回(sub(repl,string[,count]),替换次数)
# s = 'I say Hello world!'
# p = re.compile(r'(\w+) (\w+)')
# print (p.subn(r'\2 \1', s))
# def func(m):
# 	return m.group(1).title() + ' ' + m.group(2).title()
# print (p.subn(func, s))


# 备注：
#      string --- 匹配时所使用的文本
#      re --- 匹配时所使用的Pattern对象
#
#
#
#
#
#
#
#

# 练习
# pattern = re.compile(r'(\w+) (\w+) (?P<word>.*)')
# match = pattern.match( 'I love you! ')
# print ("match.string:",match.string)
# print ("match.re:", match.re)
# print ("match.pos:", match.pos)
# print ("match.endpos:", match.endpos)
# print ("match.lastindex:",match.lastindex)
# print ("match.lastgroup:",match.lastgroup)
# print ("match.group(1, 2):",match.group(1, 2))
# print ("match.groups(3):",match.groups(3))
# print ("match.groupdict(2):",match.groupdict(2))
# print ("match.start(3):",match.start(3))
# print ("match.end(3):",match.end(3))
# print ("match.expand(r'\2 \1 \3'):",match.expand(r'\2 \1 \3'))









































