import vk_api, vk_captchasolver as vc
from time import sleep
from random import randint


vk_session = vk_api.VkApi(token='88e0310cbb6bbe02f592ef634baa845e1875f715f01a21b65196ce1f07adb19c6ac6cca6735b00a981fee')
vk = vk_session.get_api()


tr = True

sms = 'Взаимная подписка. Добавлю в течении 5 - минут! \nhttps://vk.com/id667769478'
while tr:
	o = ['о', 'o', '0']
	f = ['ф', 'f']
	m = ['m', 'м']
	n = ['н', 'H']
	p = ['р', 'p']
	a = ['a', 'а']
	s = ['s', 'с', 'c']
	b = ['b', 'б', '6']
	v = ['v', 'B', 'в']
	t = ['t', 'т']
	e = ['e', 'e']
	k = ['k', 'к']
	l = ['l', 'л']
	u = ['u', 'и']

	def z(mmm):
		zz = randint(0,int(len(mmm))-1)
		bykva = mmm[zz]
		return bykva

	def split(s):
		    return [char for char in s]

	spisok = split(sms)



	dd = ''
	for i in spisok:
		oo = i
		i = i.lower()
		if str(i) == 'a':
			dd += str(z(a))
		elif str(i) == 'ф':
			dd += str(z(f))
		elif str(i) == 'м':
			dd += str(z(m))
		elif str(i) == 'н':
			dd += str(z(n))
		elif str(i) == 'р':
			dd += str(z(p))
		elif str(i) == 'с':
			dd += str(z(s))
		elif str(i) == 'б':
			dd += str(z(b))
		elif str(i) == 'в':
			dd += str(z(v))
		elif str(i) == 'т':
			dd += str(z(t))
		elif str(i) == 'е':
			dd += str(z(e))
		elif str(i) == 'к':
			dd += str(z(k))
		elif str(i) == 'л':
			dd += str(z(l))
		elif str(i) == 'и':
			dd += str(z(u))
		else:
			dd += str(oo)

	sleep(randint(15, 60))
	try:
		vk.wall.post(owner_id=-68101640, friends_only=0, from_group=0, message=dd, close_comments=1)
	except KeyboardInterrupt:
		tr = False
	except vk_api.Captcha:
		cycle = True
		while cycle:
			try:
				vk.wall.post(owner_id=-68101640, friends_only=0, from_group=0, message=dd, close_comments=1)
			except vk_api.Captcha as cptch:
				result_solve_captcha = vc.solve(sid=int(cptch.sid), s=1)
				try:
					cptch.try_again(result_solve_captcha)
					cycle = False
				except vk_api.Captcha as cptch2:
			except:
				pass
	except:
		break
