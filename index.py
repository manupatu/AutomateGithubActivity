from datetime import datetime, tzinfo
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta
from git import Repo, Actor
import util
import random
import os


def mainProgram():
    load_dotenv() # Load environment variables
    currentDateTime = util.stripMiliSec(datetime.now().astimezone())
    setOriginDateTime = currentDateTime - relativedelta(years = 1)
    tempDateTime = setOriginDateTime

    # now = datetime.now()
    # now = util.stripMiliSec(now)
    repoPath = "./"
    repo = Repo(repoPath)
    name = os.getenv("NAME")
    email = os.getenv("EMAIL")
    if not name or not email:
        print("Environment variables NAME and EMAIL must be set.")
        return
    new_author = Actor(name, email)
    new_committer = Actor(name, email)
    
    # print(now)
    while True:
        tempDateTime = tempDateTime + relativedelta(days=random.randint(0, 4))
        if(tempDateTime>=(currentDateTime - relativedelta(weeks=1))):
            print('reached the limit')
            break
        writeToFile(tempDateTime, currentDateTime)
        repo.index.add(["log.txt"])
        # repo.index.commit(f"Update log.txt with date: {tempDateTime}", commit_date=tempDateTime)
    repo.index.commit("Change author", author = new_author, committer=new_committer, commit_date=tempDateTime)
    print(os.getenv("NAME"))
    # print(tempDateTime.strftime("%Y-%m-%d %H:%M:%S %z"))
    
        
        

def writeToFile(tempDateTime, currentDateTime):
    # temp = tempDateTime
    # print(f"Repo updated on {currentDateTime} for this: {setDateTime}\n")
    # listOfLogs.append(f"Repo updated on {currentDateTime} for this: {dateTime}\n")
    with open("log.txt", "a+") as logFile:
        logFile.write(f"Repo updated on {currentDateTime} for this: {tempDateTime}\n")



if( __name__ == "__main__" ):
    mainProgram()