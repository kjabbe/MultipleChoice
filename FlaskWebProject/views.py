"""
Routes and views for the flask application.
"""
import sys, re, os
from datetime import datetime
from flask import render_template, request
from FlaskWebProject import app
import os
# __file__ refers to the file settings.py 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
params = []

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
	if (request.args.get('ans', '')):
		 params.append(request.args.get('ans', ''))
	try:
		(answers, questions) = getQuestions(theme)
		formatted = []
		if (len(answers) == len(questions)):
			message = ""
			for question in questions:
				newQ = question.split('%%')
				newQ.append(answers.pop(0))
				formatted.append(newQ)
		else:
			message = "Missmatch between questions and answers"	
	except IOError:
		print("error reading file")
	return render_template(
		'contact.html',
		title=theme,
		message=message,
		formatted=formatted,
		params=params
	)

@app.route('/questions/<theme>')
def answer(theme, formatted, question, answer, correct):
	"""Renders the about page."""
	return render_template(
		'contact.html',
		title=theme,
		year=datetime.now().year,
		message='Your application description page.'
	)

def getQuestions(theme):
	#fix add a settingsfile to hold filenames etc, atleast something else than theme.lower() + _questions.txt
	filename = os.path.join(APP_STATIC, 'files', (theme.lower() + '_questions.txt'))
	print (filename)
	answersRegex = re.compile('ANSWERS=')
	ans = []
	questions = []
	with open(filename, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			if (answersRegex.match(line)):
				ans = (line.replace('ANSWERS=','').split(','))
				print (ans)
			else:
				questions.append(line)
	return (ans, questions)

#def formatQuestions(questions, answers):
#	for i in range(len(questions)):
		