height = input('請輸入身高(公分):')
weight = input('請輸入體重:')

height = float(height)
weight = float(weight)

bmi = weight / (height / 100 * height / 100)

if bmi < 18.5:
	print('你的bmi值為', bmi, '你體重過輕了啦!')
elif bmi >= 18.5 and bmi < 24:
	print('你的bmi值為', bmi, '不錯! 正常人')
elif bmi >= 24 and bmi < 27:
	print('你的bmi值為', bmi, '體重過重')
elif bmi >= 27 and bmi < 30:
	print('你的bmi值為', bmi, '輕度肥胖')
elif bmi >= 30 and bmi <35:
	print('你的bmi值為', bmi, '中度肥胖')
else:
	print('你的bmi值為', bmi, '重度肥胖')

