"""# import requi9red module
import sys
  
# append the path of the
# parent directory
sys.path.append("..")
  
# import method from sibling
# module
from sibB import methodB
  
# call method
s = methodB()
print(s)"""
import sys
import os
sys.path.append(os.path.abspath('../sibB'))
import B
B.methodB()