#Griffin King
#U1L2
#Making a graph
import matplotlib.pyplot as plt
def graphed():

  
  with open("largestWeight.txt",'r') as File:
    largest = [ int(a[:-1]) for a in File.readlines()]
  with open("smallestWeight.txt",'r') as File:
    smallest = [ int(a[:-1]) for a in File.readlines()]
  with open("averageWeight.txt",'r') as File:
    average = [ int(a[:-1]) for a in File.readlines()]


  for data in [largest,average,smallest]:
    plt.plot(data)

    plt.title('MAX/MEAN/MIN Rat Weight')
    plt.xlabel('Generation')
    plt.ylabel('Weight in Grams')
    
    plt.legend(["Max","Mean","Min"])
    plt.show()
    plt.savefig('graph.png')

                             

      
