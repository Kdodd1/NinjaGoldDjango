from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
	try:
		request.session['gold']
	except KeyError as e:
		print(e)
		request.session['gold'] = 0

	if 'message' not in request.session:
		request.session['message'] = []

	return render(request, 'myapps/index.html')

def process(request):
	temp_list = request.session['message']

	if request.POST['building'] == 'farm':
		num = random.randint(10,20)
		request.session['gold'] += num
		temp_list.append({"message":'You earned ' + str(num) + ' gold from the farm! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})

	elif request.POST['building'] == 'cave':
		num = random.randint(5,10)
		request.session['gold'] += num
		temp_list.append({"message":'You earned ' + str(num) + ' gold from the cave! (' +
		            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})

	elif request.POST['building'] == 'house':
		num = random.randint(2,5)
		request.session['gold'] += num
		temp_list.append({"message":'You earned ' + str(num) + ' gold from the house!(' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})

	elif request.POST['building'] == 'casino':
		loseOrGain = random.randint(0,1)
		if loseOrGain == 0:
			num = random.randint(-50, 0)
			request.session['gold'] += num
			temp_list.append({"lose": 'lose', "message": 'You lost ' + str(num) + ' gold from the casino! (' +
			            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})
		elif loseOrGain ==1:
			num = random.randint(0,50)
			request.session['gold']+= num
			temp_list.append({"message":'You earned ' + str(num) + ' gold from the casino! (' +
			            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})
	request.session['message'] = temp_list
	print(request.session['message'])


	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')

# Create your views here.
