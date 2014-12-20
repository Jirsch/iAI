def createDomainFile(domainFileName, n):
  numbers = list(range(n)) # [0,...,n-1]
  pegs = ['a','b', 'c']
  domainFile = open(domainFileName, 'w') #use domainFile.write(str) to write to domainFile
  "*** YOUR CODE HERE ***"
  
  domainFile.close()  
        
  
def createProblemFile(problemFileName, n):
  numbers = list(range(n)) # [0,...,n-1]
  pegs = ['a','b', 'c']
  problemFile = open(problemFileName, 'w') #use problemFile.write(str) to write to problemFile
  "*** YOUR CODE HERE ***"
  
  problemFile.close()

import sys
if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Usage: hanoi.py n')
    sys.exit(2)
  
  n = int(float(sys.argv[1])) #number of disks
  domainFileName = 'hanoi' + str(n) + 'Domain.txt'
  problemFileName = 'hanoi' + str(n) + 'Problem.txt'
  
  createDomainFile(domainFileName, n)
  createProblemFile(problemFileName, n)