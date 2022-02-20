from distutils.log import error


a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
e = a+b
f = a-2*b
if f == 0:
    print ("float division by zero", error)
else:
    d = e-c/f
    print ('result', d)