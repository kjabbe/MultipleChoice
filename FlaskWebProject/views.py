"""
Routes and views for the flask application.
"""
import sys, re, os
from datetime import datetime
from flask import render_template, request
from FlaskWebProject import app
# __file__ refers to the file settings.py 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

app.debug = True

@app.route('/')
@app.route('/home')
def home():
	"""Renders the home page."""
	themes = ['TTM4137', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222', 'TTM4222']
	return render_template(
		'index.html',
		title='Multiple Choice',
		year=datetime.now().year,
		themes=themes
	)

@app.route('/questions/<theme>')
def questions(theme):
	"""Renders the questions page."""
	correct = 0
	try:
		(answers, questions) = getQuestions(theme)
		formatted = []
		if (len(answers) == len(questions)):
			message = ""
			qid = len(questions)
			for question in questions:
				newQ = question.split('%%')
				rans = []
				
				for s in newQ:
					rans.append(s.strip())
				rans.append(answers.pop(0))
				formatted.append(rans)
		else:
			message = "Missmatch between questions and answers"	
	except IOError:
		print("error reading file")
	return render_template(
		'contact.html',
		title=theme,
		message=message,
		formatted=formatted,
		correct=correct,
	)

@app.route('/questions/<title>/<item>/<qid>/<cur>')
def checkAnswer(title, item, qid, cur):
	"""Renders the about page."""
	#try:
	#	cur = literal_eval(cur)
	#except:
	cur = cur.replace('[', '')
	cur = cur.replace(']', '')
	cur = cur.replace('\'', '')
	cur = cur.split(',')
	test = cur
	cur = []
	for c in test:
		cur.append(c.strip())
	mod = qid
	print ('"' + cur[-1] + '"')
	if (cur[-1] == 'a'):
		pos = 1
	elif (cur[-1] == 'b'):
		pos = 2
	elif (cur[-1] == 'c'):
		pos = 3
	elif (cur[-1] == 'd'):
		pos = 4
	else:
		pos = 0	
	correct = 0
	if (item == cur[pos]):
		correct = 1
	elif (item != cur[pos] and len(item) > 0):
		correct = 2
	try:
		(answers, questions) = getQuestions(title)
		formatted = []
		if (len(answers) == len(questions)):
			message = ""
			qid = len(questions)
			for question in questions:
				newQ = question.split('%%')
				rans = []
				
				for s in newQ:
					rans.append(s.strip())
				rans.append(answers.pop(0))
				formatted.append(rans)
		else:
			message = "Missmatch between questions and answers"	
	except IOError:
		print("error reading file")
	return render_template(
		'contact.html',
		title=title,
		message=message,
		formatted=formatted,
		correct=correct,
		mod=mod,
		test1=test,
		test2=item
	)

def getQuestions(theme):
	#fix add a settingsfile to hold filenames etc, atleast something else than theme.lower() + _questions.txt
	filename = os.path.join(APP_STATIC, 'files', (theme.lower() + '_questions.txt'))
	answersRegex = re.compile('ANSWERS=')
	ans = []
	questions = []
	with open(filename, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			if (answersRegex.match(line)):
				ans = (line.replace('ANSWERS=','').split(','))
			else:
				questions.append(line)
	
	return (ans, questions)

#def formatQuestions(questions, answers):
#	for i in range(len(questions)):
		