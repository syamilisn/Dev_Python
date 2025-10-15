def fwd(s:str)->str:
    return s[:]
def rev(s:str)->str:
    return s[::-1]
def rev_palin(s:str)->bool:
    return s[:] == s[::-1]
def rotate_left(s:str, n)->str:
    return s[n:]+s[:n]   
def rotate_right(s:str, n)->str:
    return s[-n:]+s[:-n]   
def rotate_deque(s:str, n)->str:
    d = deque(s)
    return ''.join([d.rotate(n)])  #right, -n left 
from collections import deque

def rotate_string(s, n, direction="right"):
    d = deque(s)
    if direction == "right":
        d.rotate(n)   # +n → right rotation
    else:
        d.rotate(-n)  # -n → left rotation
    return ''.join(d)
ip="hello"
ip1="madam"

print(f"forward: ip = {ip} res = {fwd(ip)}")
print(f"reverse: ip = {ip} res = {rev(ip)}")
print(f"reverse palin: ip = {ip1} {rev_palin(ip1)}")
print(f"rotate left: ip = {ip} res = {rotate_left(ip,2)}")
print(f"rotate right: ip = {ip} res = {rotate_right(ip,2)}")
print(f"rotate deque: ip = {ip} res = {rotate_deque(ip,2)}")
