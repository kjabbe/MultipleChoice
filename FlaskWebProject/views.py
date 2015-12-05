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
	themes = ['TTM4137']
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

@app.route('/questions/<title>/<item>/<qid>')
def checkAnswer(title, item, qid):
	"""Renders the about page."""
	mod = qid
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
	question = formatted[int(mod)]
	if (question[-1] == 'a'):
		pos = 1
	elif (question[-1] == 'b'):
		pos = 2
	elif (question[-1] == 'c'):
		pos = 3
	elif (question[-1] == 'd'):
		pos = 4
	else:
		pos = 0	
	correct = 0
	if (item == question[pos]):
		correct = 1
	elif (item != question[pos] and len(item) > 0):
		correct = 2
	return render_template(
		'contact.html',
		title=title,
		message=message,
		formatted=formatted,
		correct=correct,
		mod=mod
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
			line = line.replace('?', '')
			if (answersRegex.match(line)):
				ans = (line.replace('ANSWERS=','').split(','))
			else:
				questions.append(line)
	
	return (ans, questions)

#def formatQuestions(questions, answers):
#	for i in range(len(questions)):
		