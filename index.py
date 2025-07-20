from datetime import datetime
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta
from git import Repo
import util
import random



def mainProgram():
    load_dotenv() # Load environment variables
    currentDateTime = util.stripMiliSec(datetime.now().astimezone())
    setOriginDateTime = currentDateTime - relativedelta(years = 1)
    tempDateTime = setOriginDateTime
    repoPath = "./"
    repo = Repo(repoPath)
    origin = repo.remote("origin")

    while True:
        tempDateTime = tempDateTime + relativedelta(days=random.randint(0,3))
        # The last commit date ends around a week ago
        if(tempDateTime>=(currentDateTime - relativedelta(weeks=1))):
            print('reached the limit')
            break
        writeToFile(tempDateTime, currentDateTime)
        
        # Stage the file for commit
        repo.index.add(["log.txt"])
        
        
        # Committer Date: Timestamp when the commit was made
        # Author Date: Timestamp when the commit was authored
        # Here we set both to the same value for simplicity
        # GitHub's Activity Graph depends on the authored timestamp
        repo.index.commit(f"Update log.txt with date: {tempDateTime}", commit_date=tempDateTime, author_date=tempDateTime)
    origin.push()

def writeToFile(tempDateTime, currentDateTime):

    with open("log.txt", "a+") as logFile:
        logFile.write(f"Repo updated on {currentDateTime} for this: {tempDateTime}\n")


if( __name__ == "__main__" ):
    mainProgram()