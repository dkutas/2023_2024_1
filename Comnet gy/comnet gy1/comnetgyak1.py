# def is_Leap_Year(someYearInStr):
#     yearInInt = int(someYearInStr)
#     return yearInInt % 4 == 0 & (yearInInt % 100 != 0 | yearInInt % 400 == 0)

# with open ("years.txt","r") as f:
#     for line in f:
#         print(f"{line} is leap year") if is_Leap_Year(line) else print ( f"{line} is not leap year")


import json

with open ("points.json","r") as readFile:
    data = json.load(readFile)
    # there is no destructuring like this
    maxOverall = data["homework"]["max"] + data["mininet"]["max"] + data["zh"]["max"]
    currPoints = data["homework"]["point"] + data["mininet"]["point"]
    print (currPoints-maxOverall*0.5)