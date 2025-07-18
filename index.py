from datetime import datetime, tzinfo
from dateutil.relativedelta import relativedelta
from git import Repo
import util
import random


def mainProgram():
    currentDateTime = util.stripMiliSec(datetime.now().astimezone())
    setOriginDateTime = currentDateTime - relativedelta(years = 1)
    tempDateTime = setOriginDateTime

    # now = datetime.now()
    # now = util.stripMiliSec(now)
    repoPath = "./"
    repo = Repo(repoPath)
    
    # print(now)
    while True:
        tempDateTime = tempDateTime + relativedelta(days=random.randint(0, 4))
        if(tempDateTime>=(currentDateTime - relativedelta(weeks=1))):
            print('reached the limit')
            break
        writeToFile(tempDateTime, currentDateTime)
        repo.index.add(["log.txt"])
        repo.index.commit(f"Update log.txt with date: {tempDateTime}", commit_date=tempDateTime)
    # print(tempDateTime.strftime("%Y-%m-%d %H:%M:%S %z"))
    
        
        

def writeToFile(tempDateTime, currentDateTime):
    # temp = tempDateTime
    # print(f"Repo updated on {currentDateTime} for this: {setDateTime}\n")
    # listOfLogs.append(f"Repo updated on {currentDateTime} for this: {dateTime}\n")
    with open("log.txt", "a+") as logFile:
        logFile.write(f"Repo updated on {currentDateTime} for this: {tempDateTime}\n")



if( __name__ == "__main__" ):
    mainProgram()