import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

df = pd.read_csv('/Users/FernandoWang/Downloads/online_news_popularity.csv', sep=', ', engine='python')

df['type'] = ''
df.loc[0: int(2.0 / 3 * len(df)), 'type'] = 'train'
df.loc[int(2.0 / 3 * len(df)): int(5.0 / 6 * len(df)), 'type'] = 'validation'
df.loc[int(5.0 / 6 * len(df)): , 'type'] = 'test'
df.describe()

X_train = df[df.type == 'train'][[col for col in df.columns if col not in ['url', 'shares', 'type']]]
y_train = np.log(df[df.type == 'train'].shares).reshape(-1,1)

X_val = df[df.type == 'validation'][[col for col in df.columns if col not in ['url', 'shares', 'type']]]
y_val = np.log(df[df.type == 'validation'].shares).reshape(-1,1)

X_test = df[df.type == 'test'][[col for col in df.columns if col not in ['url', 'shares', 'type']]]
y_test = np.log(df[df.type == 'test'].shares).reshape(-1,1)

X_train = np.hstack((np.ones_like(y_train), X_train))
X_val = np.hstack((np.ones_like(y_val), X_val))
X_test = np.hstack((np.ones_like(y_test), X_test))

def linreg(X, y, reg=0.0):
	eye = np.eye(X.shape[1])
	eye[0,0] = 0. # don't regularize bias term!
	X = np.matrix(X)
	y = np.matrix(y)
	return np.linalg.solve(X.transpose() * X + reg * eye, X.transpose() * y)
	# return np.linalg.lstsq(X.transpose() * X + reg * eye, X.transpose() * y)[0]

# theta_optimal = linreg(X_train, y_train, reg=9.34604374950277)

lamb = [random.uniform(0.0, 150.0) for i in range(150)]

def generateThetas(mode):
	if mode == "train":
		thetas = [linreg(X_train, y_train, reg=la) for la in lamb]
	elif mode == "val":
		thetas = [linreg(X_val, y_val, reg=la) for la in lamb]
	else:
		thetas = [linreg(X_test, y_test, reg=la) for la in lamb]
	return thetas

thetas = generateThetas("train")
# print (thetas[0]).item(0)
# thetasVal = [np.linalg.norm(theta) for theta in thetas]

# print thetas[0].shape
# print np.matrix(X_val[0]).transpose().shape
# print (thetas[0].transpose() * np.matrix(X_val[0]).transpose()).item(0, 0)
# print thetas[0].transpose() * np.matrix(X_val[0]).transpose().item(0)
# print y_val[0][0]

MSE = []
def generateMSE():
	for i in range(len(lamb)):
		s = 0
		thetaMat = np.matrix(thetas[i])
		xValMat = np.matrix(X_val[i])
		yReg = xValMat * thetaMat
		# print thetaMat.shape
		# print xValMat[i].shape
		# print y_val[i][0]
		# break
		for j in range(len(yReg)):
			# regYval = (thetas[i]).item(0) + (xValMat[j] * thetaMat).item(0)
			# print (thetas[i].transpose() * np.matrix(X_val[i]).transpose()).shape	
			s += (y_val.item(j) - yReg.item(j))**2		
		MSE.append((s * 1.0 / len(yReg)**0.5))

generateMSE()
# lambList = []		
# def generateEverything():
# 	for i in range(150):
# 		lambd = random.uniform(0.0, 150.0)
# 		lambList.append(lambd)
# 		theta = linreg(X_train, y_train, reg=lambd)

# 		thetaMat = np.matrix(theta)
# 		xValMat = np.matrix(X_val)
# 		yReg = xValMat * thetaMat

# 		s = 0
# 		for j in range(len(yReg)):
# 			diff = yReg.item(j) - y_val.item(j)
# 			sq = diff**2
# 			s += sq

# 		s / len(yReg)
# 		s ** 0.5
# 		MSE.append(s)


# lambdaLista = []
# thetaNormL = []
# RMSE_L = []

def generateLambda():
	for i in range(150):
		
def fuckMyLife():

	for index in range(150):
		lambdaNum = random.uniform(0.0,150.0)
		lambdaLista.append(lambdaNum)
		theta = linreg(X_train, y_train, reg=lambdaNum)
		theta_norm = np.linalg.norm(theta, 2, None, False)
		thetaNormL.append(theta_norm)

		theta_M = np.matrix(theta)
		X_valM = np.matrix(X_val)
		y = X_valM * theta_M
		# # print theta_M.shape
		# # print X_valM.shape
		
		# # print y.shape
		# print y_val.item(0)
		# break

		summation = 0
		for index in range(len(y)):
			diff = y.item(index) - y_val.item(index)
			square = diff ** 2
			summation += square

		summation /= len((y))
		summation ** (0.5)

		RMSE_L.append(summation)


# plot thetavalues versus lambda
# plt.plot(lamb[1:], thetasVal[1:])
# plot mse verses labmda
# fuckMyLife()

# plt.plot(lambdaLista, RMSE_L, "ro")
plt.plot(lamb, MSE, "ro")
plt.show()