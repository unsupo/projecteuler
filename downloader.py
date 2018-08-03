from bs4 import BeautifulSoup
import urllib2
import os


baseurl='https://projecteuler.net/'
problem='problem='
dir_path = os.path.dirname(os.path.realpath(__file__))

c="""
def main():
    return 1

if __name__ == '__main__':
    print main()
"""


def createProblem(num):
    url=baseurl+problem+str(num)
    response = urllib2.urlopen(url)
    webContent = response.read()
    soup = BeautifulSoup(webContent, 'html.parser')
    title=soup.select("#content > h2")
    # Create directory if it doesn't exist
    directory=dir_path+"/problem_"+str(num)
    if not os.path.exists(directory):
        os.makedirs(directory)
    readme=directory+"/README.md"
    contents="# "+title[0].string+"\n"
    stuff=soup.select("#content > div.problem_content > p")
    stuff = "\n".join([i.string for i in stuff])
    contents+=stuff
    if not os.path.exists(readme):
        f=open(readme,'w+')
        f.write(contents)
    dir=directory+"/python"
    pyfile=dir+"/answer.py"
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.exists(pyfile):
        f=open(pyfile,"w+")
        f.write(c)

if __name__ == '__main__':
    createProblem(2)