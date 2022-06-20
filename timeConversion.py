'''
Starting from the first hour of the day (12:00 AM or midnight to 12:59 AM), subtract 12 hours:

12:00 AM = 0:00
12:15 AM = 0:15
From 1:00 AM to 12:59 PM, the hours and minutes remain the same:

9:00 AM = 9:00
12:59 PM = 12:59
For times between 1:00 PM to 11:59 PM, add 12 hours:

3:17 PM = 15:17
11:59 PM = 23:59.
'''

def timeConversion(s):
    # Write your code here
    res=''
    if s[-2:]=='AM':
        res=s[:-2]
        if s[0:2]=='12':
            res='00'+s[2:-2]
    if s[-2:]=='PM':
        res=s[:-2]
        if int(s[0:2])<12:
            res=str(int(s[0:2])+12)+s[2:-2]
    return res


print("Escenario 1:")
entrada = '07:05:45PM'
print(entrada)
res = timeConversion(entrada)

print(res)

print("Escenario 2:")
entrada = '12:15:00AM'
print(entrada)
res = timeConversion(entrada)

print(res)

print("Escenario 3:")
entrada = '12:15:00PM'
print(entrada)
res = timeConversion(entrada)

print(res)

print("Escenario 4:")
entrada = '11:59:45PM'
print(entrada)
res = timeConversion(entrada)

print(res)

print("Escenario 5:")
entrada = '00:59:45PM'
print(entrada)
res = timeConversion(entrada)

print(res)

print("Escenario 6:")
entrada = '11:59:45AM'
print(entrada)
res = timeConversion(entrada)

print(res)





print("Escenario 7:")
entrada = '12:45:54PM'
print(entrada)
res = timeConversion(entrada)

print(res)