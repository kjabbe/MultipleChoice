# Multiple Choice "Engine"

Tool to practice on multiple choice questions, scaleable on both number of questions and courses/themes.  

Provide questions in the static/files folder, add name to the list of courses/themes in the home view.
At the moment support for questions with 4 answers and one correct, hopefully dynamic ranges shortly      
Questions file should be a .txt file and have the following format:  
ANSWERS=a,d,c,a,b  
QUESTION %% ANSWER_A %% ANSWER_B %% ANSWER_C %% ANSWER_D %% CORRECT (a, b, c or d)  

Written using the python Flask framework. Initial project template gotten from the Microsofts Azure platform.  