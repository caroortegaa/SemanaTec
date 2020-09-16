#io_utilities.py
#open es como si fuera una clase
filepath = './data/iris.data' #r de read

with open (filepath ,'r') as fp:
    data = fp.read()

data_lines = data.split('\n')
data_final = [f.split(',')for f in data_lines]

print (data_final)
