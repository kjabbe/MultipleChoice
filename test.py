import re
def getQuestions(theme):
	filename = theme + '_questions.txt'
	answersRegex = re.compile('ANSWERS=')
	ans = []
	questions = []
	with open(filename) as f:
		for line in f:
			if (answersRegex.match(line)):
				ans = line.replace('ANSWERS=','').split(',')
			else:
				questions.append(line)
	print (ans)
	print (questions)
	return (ans, questions)

getQuestions('ttm4137')
