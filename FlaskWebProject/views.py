"""
Routes and views for the flask application.
"""
import sys, re, os, random
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
	themes = ['URNmedSvar', 'TTM4137_2014', 'TTM4137_2013', 'TTM4137_2012', 'TTM4137_2010', 'TTM4137_2009', 'TTM4137_2008', 'TTM4137_2007']
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
	randomSorted = []
	try:
		questions = getQuestions(theme)
		formatted = formatQuestions(questions)
		#for i in range(len(formatted)):
		#	size = len(formatted)-i
		#	if (size >= 1):
		#		r = random.randint(0,size-1)
		#	else:
		#		r = 0
		#	randomSorted.append(formatted[r])
		#	formatted.pop(r)
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
	try:
		questions = getQuestions(title)
		formatted = formatQuestions(questions)
	except IOError:
		message = 'No questions found'
		print("error reading file")
	questionDict = formatted[int(request.form.get('question'))]
	if (questionDict['correct'] == request.form.get('answer')):
		return jsonify(correct=True, id=request.form.get('question'))
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
	qid = 0
	for question in questions:
		form = {}
		form['id'] = qid
		elementList = question.split('	')
		form['question'] = elementList.pop(0)
		correctAlt = elementList.pop(-1)
		if (correctAlt == 'a'):
			form['correct'] = elementList[0]
		elif (correctAlt == 'b'):
			form['correct'] = elementList[1]
		elif (correctAlt == 'c'):
			form['correct'] = elementList[2]
		elif (correctAlt == 'd'):
			form['correct'] = elementList[3]
		elif (correctAlt == 'e'):
			form['correct'] = elementList[4]
		form['answers'] = sorted(elementList, key=lambda k: random.random())
		qid = qid + 1
		return_questions.append(form)
	return return_questions
