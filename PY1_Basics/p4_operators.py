print("**Math Operators from Highest to Lowest Precedence**")
a = 3
b = 2
add = f"\na + b = {a+b}"
sub = f"\na - b = {a-b}"
mul = f"\na * b = {a*b}"
div = f"\na / b = {a/b}"
div_int = f"\na // b = {a//b}"
div_mod = f"\na % b = {a%b}"
exp = f"\na ** b = {a**b}"
#result = add + sub + mul + div + div_int + div_mod + exp
result_inOrder = exp + div_mod + div_int + div + mul + sub + add
#print('\nOperations result:\n',result)
print('\nResult in order of precendence:\n',result_inOrder)

expn1 = "(5 - 1) * ((7 + 1) / (3 - 1))"
res1 = (5 - 1) * ((7 + 1) / (3 - 1))
print(f"\n{expn1} = {res1}")

