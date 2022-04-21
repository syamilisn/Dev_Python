import sys
sys.path.append("..")

from PY1_Basics import displayFunc
obj = displayFunc()

#VARIABLES
a = "Alice"
x = 1
y = 22.22

Func1 = {
    1: {'name': 'len(var)', 'desc':'Length of String.', 'ip': a, 'op': len(a) },
    2: {'name': 'str(var)', 'desc':'Converts to String.', 'ip': x, 'op': str(x)},
    3: {'name': 'int(var)', 'desc':'Converts to Int.', 'ip': y, 'op': int(y)},
    4: {'name': 'float(var)', 'desc':'Converts to Float.', 'ip': x, 'op': float(x)},
}


for i in Func1:
    obj.displayFunc(i, Func1[i]['name'], Func1[i]['desc'], Func1[i]['ip'], Func1[i]['op'])