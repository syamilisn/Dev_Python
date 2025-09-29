import datetime     #if imported else where shows error
x = datetime.datetime.now()
print(x)

y = str(x.hour) + ":"+ str(x.minute)+ ":" + str(x.second)
print(y, "Type: ", type(y))    #string

z = datetime.datetime(2001, 5, 18, 12, 12, 12)
print(z)

z1 = datetime.time(12, 12, 12)
print(z1, "Type: ", type(z1))

z2 = datetime.date(2001, 5, 18)
print(z2, "Type: ", type(z2))

#convert from DATETIME to STRING format (using stringFormat time method)
print(z.strftime("%B"))     #doesn't work for now(). Only for implicitly given date and time.
print("local date", x.strftime("%x"))
print("local time", x.strftime("%X"))
"""
    legal format codes
"""