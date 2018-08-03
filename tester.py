import importlib
import os
import re
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

def readFile(fname):
    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content

def getAnswer(probNum):
    answers=readFile(dir_path+"/answers.txt")
    for i in answers:
        if i.startswith("Problem "+"%03d" % (probNum,)):
            return i.split(":")[-1].strip()

if __name__ == '__main__':
    problems=[i for i in os.listdir(dir_path) if re.match('problem_[0-9]+',i)]

    for i in problems:
        f=i+"/python/"
        print f
        sys.path.insert(0, f)
        import answer as f
        reload(f)
        ans=getAnswer(int(i.replace("problem_","")))
        a=str(f.main())
        if ans == a:
            print "\tCorrect:\t"+a
        else:
            print "\tWrong:\tcorrect="+ans+"\tyours="+a
        sys.path=sys.path[1:]

