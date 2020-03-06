def isYearLeap(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True

def daysInMonth(year,month):
	if year < 1900 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month-1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
    days=0
    for m in range(1, month):
        md= daysInMonth(year, m)
        if md==None:
            return None
        print (md)
        days += md
        print(days)
    md=daysInMonth (year, month)
    if day>=1 and day <=md:
        return days + day
    else: return None
print(dayOfYear(2020, 2, 22))

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")