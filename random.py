# -*-coding:utf-8 -*-
# 随机对位

import random2


def ListRemove(listA, listB):
	for i in listA:
		if i in listB:
			listB.remove(i)
	return listB


list = open('Contestant.txt', 'r', encoding='utf-8')
s = list.readlines()
list.close()
for line in s:
	listB = line.split()

while listB != []:
	e = random2.sample(listB, 2)
	print(e)
	ListRemove(e, listB)

