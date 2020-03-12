import random #randomint

r = random.randint(1, 100)
while True:
	num = input('請猜數字:')
	num = int(num)
	if num == r:
		print('猜中了!')
		break
	elif num > r:
		print('大於答案')
	elif num < r:
		print('小於答案')