#VARIABLES
a = "Alice"
b = "bob buntsman"
x = 1
y = 22.22
#print("\nFUNCTION : PURPOSE = OPERATION")
def addQuotesIfStr(var):
    if type(var) == str:
        return '\"'+ var +'\"'
    else:
        return var

def displayFunc(id, name, desc,ip,op):
    """A function that returns definition of a built-in function."""
    ip_new = addQuotesIfStr(ip)
    op_new = addQuotesIfStr(op)
    print(f"{id}. {name}")
    print(f"\n\tDefinition : {desc}")
    print(f"\n\tInput : {ip_new}\t\tType : {type(ip)}")
    print(f"\n\tOutput : {op_new}\t\tType : {type(op)}")
    print("-"*100)

print("-"*100)
displayFunc(1,"len(var) -->", "Length of String.", a , len(a) )
functions = dict()
Func1 = {
    1: {'name': 'len(var)', 'desc':'Length of String.', 'ip': a, 'op': len(a) },
    2: {'name': 'str(var)', 'desc':'Converts to String.', 'ip': x, 'op': str(x)},
    3: {'name': 'int(var)', 'desc':'Converts to Int.', 'ip': y, 'op': int(y)},
    4: {'name': 'float(var)', 'desc':'Converts to Float.', 'ip': x, 'op': float(x)},
    5: {'name': 'var.upper()', 'desc':'Converts to Uppercase.', 'ip': a, 'op': a.upper()},
    6: {'name': 'var.isupper()', 'desc':'Checks if Uppercase.', 'ip': a, 'op': a.isupper()},
    7: {'name': 'var.lower()', 'desc':'Converts to Lowercase.', 'ip': a, 'op': a.lower()},
    8: {'name': 'var.islower()', 'desc':'Checks if Lowercase.', 'ip': a, 'op': a.islower()},
    9: {'name': 'var.title()', 'desc':'Capital first letter, each word.', 'ip':b, 'op': b.title()},
    10: {'name': 'var.capitalize()', 'desc':'Capital first letter.', 'ip': b, 'op': b.capitalize()},
    11: {'name': 'var.split()', 'desc':'Divides string.', 'ip': b, 'op': b.split()},
    12: {'name': 'var.count()', 'desc':'Counts characters.', 'ip': b, 'op': b.count('b')},
    13: {'name': 'var.swapcase()', 'desc':'Switches case of characters.', 'ip': a, 'op': a.swapcase()},

    
}
"""
for i in Func1:
    print(f"\n{i}. {Func1[i]}")
"""
for i in Func1:
    displayFunc(i, Func1[i]['name'], Func1[i]['desc'], Func1[i]['ip'], Func1[i]['op'])

