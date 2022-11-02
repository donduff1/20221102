# Control
def control():
	
	sideList = inData()
	
# Model
def inData():
	
	sideList = []
	sideList.append(float( input('"A" oldal: ')))
	sideList.append(float( input('"B" oldal: ')))
	sideList.append(float( input('"C" oldal: ')))
	
	return sideList

#View
control()

