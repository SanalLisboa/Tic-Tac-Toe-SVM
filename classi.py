from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
from random import *
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
from sklearn import linear_model
moves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
def reset():
	global moves
	moves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
def train_model():
	data_set = np.loadtxt("data_set1")
	features = data_set[:,:9]
	labels = data_set[:,9:]
	# regr = linear_model.LinearRegression()
	# regr.fit(features, labels.ravel())
	param_gird = [{ "n_estimators": [10,100,1000] }]
	r = RandomForestClassifier()
	clf = GridSearchCV(r, param_gird) 
	clf.fit(features, labels)
	joblib.dump(clf, 'tic_tac_toe_model.pkl')

def classify_tic_tac_toe(train_set):
	train_set = np.array(train_set)
	train_set = train_set.reshape(1, -1)
	clf_load = joblib.load('tic_tac_toe_model.pkl')
	predicted = clf_load.predict(train_set)
	return predicted
def check(moves):
	for i in range(0, len(moves)):
		if moves[i] == 0:
			moves[i] = +1
			a, b = check_moves(moves)
			print(b)
			if b == "X wins":
				moves[i] = 0
				return True
			moves[i] = 0
	return False
def find_best_move(moves):
	for i in range(0, len(moves)):
		if moves[i] == 0:
			moves[i] = -1
			if check(moves) == True:
				return moves
			else:
				moves[i] = 0
	moves[int(classify_tic_tac_toe(moves)[0])] = -1
	return moves
	# for i in range(0, len(moves)):
	# 	if moves[i] == 0:
	# 		moves[i] = -1
	# 		check1, l = check_moves(moves)
	# 		if classify_tic_tac_toe(moves)[0] == -1 and check(moves) == False:
	# 			print(moves)
	# 			return moves
	# 		else:
	# 			moves[i] = 0
	# print('e')
	# for i in range(0, len(moves)):
	# 	if moves[i] == 0:
	# 		moves[i] = -1
	# 		check1, l = check_moves(moves)
	# 		if check(moves) == False:
	# 			print('e')
	# 			return moves
	# 		else:
	# 			moves[i] = 0
	# while True:
	# 	n = randint(0, 8)
	# 	if moves[n] == 0:
	# 		moves[n] = -1
	# 		break
	# return moves
def find_best_move1(moves):
	moves[int(classify_tic_tac_toe(moves)[0])] = +1
	return moves
def check_moves(moves):
	if moves[0] == -1 and moves[4] == -1 and moves[8] == -1:
		print("\nX wins")
		return True, "X wins"
	if moves[2] == -1 and moves[4] == -1 and moves[6] == -1:
		print("\nX wins")
		return True, "X wins"
	if moves[0] == -1 and moves[1] == -1 and moves[2] == -1:
		print("\nX wins")
		return True, "X wins"
	if moves[3] == -1 and moves[4] == -1 and moves[5] == -1:
		print("\nX wins")
		return True, "X wins"
	if moves[6] == -1 and moves[7] == -1 and moves[8] == -1:
		print("\nX wins")
		return True, 'X wins'
	if moves[0] == -1 and moves[3] == -1 and moves[6] == -1:
		print("\nX wins")
		return True, "X wins"
	if moves[1] == -1 and moves[4] == -1 and moves[7] == -1:
		print("\nX wins")
		return True, "X wins"
	if moves[2] == -1 and moves[5] == -1 and moves[8] == -1:
		print("\nX wins")
		return True, "X wins"
	if moves[0] == 1 and moves[4] == 1 and moves[8] == 1:
		print("\nO wins")
		return True, "O wins"
	if moves[2] == 1 and moves[4] == 1 and moves[6] == 1:
		print("\nO wins")
		return True, "O wins"
	if moves[0] == 1 and moves[1] == 1 and moves[2] == 1:
		print("\nO wins")
		return True, "O wins"
	if moves[3] == 1 and moves[4] == 1 and moves[5] == 1:
		print("\nO wins")
		return True, "O wins"
	if moves[6] == 1 and moves[7] == 1 and moves[8] == 1:
		print("\nO wins")
		return True, "O wins"
	if moves[0] == 1 and moves[3] == 1 and moves[6] == 1:
		print("\nO wins")
		return True, "O wins"
	if moves[1] == 1 and moves[4] == 1 and moves[7] == 1:
		print("\nO wins")
		return True, "O wins"
	if moves[2] == 1 and moves[5] == 1 and moves[8] == 1:
		print("\nO wins")
		return True, "O wins"
	if 0 not in moves:
		return True, 'Game Over'
	else:
		return False, 'Game Over'
def check_moves1(moves):
	if moves[0] == -1 and moves[4] == -1 and moves[8] == -1:
		print("\nX wins")
		return True
	if moves[2] == -1 and moves[4] == -1 and moves[6] == -1:
		print("\nX wins")
		return True
	if moves[0] == -1 and moves[1] == -1 and moves[2] == -1:
		print("\nX wins")
		return True
	if moves[3] == -1 and moves[4] == -1 and moves[5] == -1:
		print("\nX wins")
		return True
	if moves[6] == -1 and moves[7] == -1 and moves[8] == -1:
		print("\nX wins")
		return True
	if moves[0] == -1 and moves[3] == -1 and moves[6] == -1:
		print("\nX wins")
		return True
	if moves[1] == -1 and moves[4] == -1 and moves[7] == -1:
		print("\nX wins")
		return True
	if moves[2] == -1 and moves[5] == -1 and moves[8] == -1:
		print("\nX wins")
		return True
	if moves[0] == 1 and moves[4] == 1 and moves[8] == 1:
		print("\nO wins")
		return True
	if moves[2] == 1 and moves[4] == 1 and moves[6] == 1:
		print("\nO wins")
		return True
	if moves[0] == 1 and moves[1] == 1 and moves[2] == 1:
		print("\nO wins")
		return True
	if moves[3] == 1 and moves[4] == 1 and moves[5] == 1:
		print("\nO wins")
		return True
	if moves[6] == 1 and moves[7] == 1 and moves[8] == 1:
		print("\nO wins")
		return True
	if moves[0] == 1 and moves[3] == 1 and moves[6] == 1:
		print("\nO wins")
		return True
	if moves[1] == 1 and moves[4] == 1 and moves[7] == 1:
		print("\nO wins")
		return True
	if moves[2] == 1 and moves[5] == 1 and moves[8] == 1:
		print("\nO wins")
		return True
	if 0 not in moves:
		return True
	else:
		return False
def tic_tac_toe():
	play = 0
	moves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	while check_moves(moves) == False:
		for i in range(0, len(moves)):
			if (i) % 3 != 0:
				if moves[i] == -1:
					print('X', end=' ')
				elif moves[i] == 1:
					print('O',end = ' ')
				else:
					print('_',end = ' ')
			else:
				if moves[i] == -1:
					print('\nX', end=' ')
				elif moves[i] == 1:
					print('\nO',end = ' ')
				else:
					print('\n_',end = ' ')
		print('\n')
		position = int(input("\nselect position of your move:"))
		moves[position-1] = +1
		for i in range(0, len(moves)):
			if (i) % 3 != 0:
				if moves[i] == -1:
					print('X', end=' ')
				elif moves[i] == 1:
					print('O',end = ' ')
				else:
					print('_',end = ' ')
			else:
				if moves[i] == -1:
					print('\nX', end=' ')
				elif moves[i] == 1:
					print('\nO',end = ' ')
				else:
					print('\n_',end = ' ')
		if check_moves(moves):
			break
		print('\n')
		print("\nComputer playing:")
		moves = find_best_move(moves)
		play += 1
#tic_tac_toe()
def comp_tic_tac_toe():
	play = 0
	moves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	while check_moves1(moves) == False:
		for i in range(0, len(moves)):
			if (i) % 3 != 0:
				if moves[i] == -1:
					print('X', end=' ')
				elif moves[i] == 1:
					print('O',end = ' ')
				else:
					print('_',end = ' ')
			else:
				if moves[i] == -1:
					print('\nX', end=' ')
				elif moves[i] == 1:
					print('\nO',end = ' ')
				else:
					print('\n_',end = ' ')
		print('\n')
		moves = find_best_move1(moves)
		for i in range(0, len(moves)):
			if (i) % 3 != 0:
				if moves[i] == -1:
					print('X', end=' ')
				elif moves[i] == 1:
					print('O',end = ' ')
				else:
					print('_',end = ' ')
			else:
				if moves[i] == -1:
					print('\nX', end=' ')
				elif moves[i] == 1:
					print('\nO',end = ' ')
				else:
					print('\n_',end = ' ')
		if check_moves1(moves):
			print("\n\nno winner\n")
			break
		print('\n')
		moves = find_best_move(moves)
		play += 1
#train_model()
#comp_tic_tac_toe()