"""
Routes and views for the flask application.
"""
import sys, re, os
from datetime import datetime
from flask import render_template, request, jsonify
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
	message = ''
	try:
		questions = getQuestions(theme)
		formatted = formatQuestions(questions)
	except IOError:
		message = 'No questions found'
		print("error reading file")
	return render_template(
		'questions.html',
		title=theme,
		message=message,
		formatted=formatted
	)

@app.route('/questions/<title>/reply', methods=['POST'])
def ajaxReply(title):
	"""Renders the questions page and checks committed answer."""
	print(request.form.get('question'))
	print(request.form.get('answer'))
	try:
		questions = getQuestions(title)
		formatted = formatQuestions(questions)
	except IOError:
		message = 'No questions found'
		print("error reading file")
	answeredQuestion = formatted[int(request.form.get('question'))]
	if (answeredQuestion[-1] == 'a'):
		if (request.form.get('answer') == answeredQuestion[1]):
			return jsonify(correct=True, id=request.form.get('question'))
		else:
			return jsonify(correct=False, id=request.form.get('question'))
	elif (answeredQuestion[-1] == 'b'):
		if (request.form.get('answer') == answeredQuestion[2]):
			return jsonify(correct=True, id=request.form.get('question'))
		else:
			return jsonify(correct=False, id=request.form.get('question'))
	elif (answeredQuestion[-1] == 'c'):
		if (request.form.get('answer') == answeredQuestion[3]):
			return jsonify(correct=True, id=request.form.get('question'))
		else:
			return jsonify(correct=False, id=request.form.get('question'))
	elif (answeredQuestion[-1] == 'd'):
		if (request.form.get('answer') == answeredQuestion[4]):
			return jsonify(correct=True, id=request.form.get('question'))
		else:
			return jsonify(correct=False, id=request.form.get('question'))
	elif (answeredQuestion[-1] == 'e'):
		if (request.form.get('answer') == answeredQuestion[5]):
			return jsonify(correct=True, id=request.form.get('question'))
		else:
			return jsonify(correct=False, id=request.form.get('question'))
	else:
		return jsonify(correct=False, id=request.form.get('question'))


	
def getQuestions(theme):
	#fix add a settingsfile to hold filenames etc, atleast something else than theme.lower() + _questions.txt
	filename = os.path.join(APP_STATIC, 'files', (theme.lower() + '_questions.txt'))
	questions = []
	with open(filename, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			questions.append(line)
	return questions

def formatQuestions(questions):
	return_questions = []
	for question in questions:
		elementList = question.split('%%')
		elements = []
		for elem in elementList:
			elements.append(elem.strip())
		return_questions.append(elements)
	return return_questions