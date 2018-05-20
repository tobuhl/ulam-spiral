#ulam.py

import numpy

EMPTY_REMARK=-1

'''
UlamSpiral represents a Ulam spiral as a numpy 2D array with a given size, start number, spin and increment
'''

class UlamSpiral:

    def __init__(self, size, spin, start, incrementNumber):
        '''
        spin describes the direction of filling the grid from center point
            0 = down right
            1 = right up
            2 = up left
            3 = left down 
            4 = down left
            5 = left up
            6 = up right
            7 = right down

        0,1,2,3 represents a counter-clockwise filling manner and 4,5,6,7 a clockwise filling manner 
        '''        

        if start<0: 
            raise ValueError("Error: start must be 0 or greater!")
        self.start = start

        if self.isEven(size): 
            raise ValueError("Error: size must be odd!")
        self.size = size

        if spin<0 or spin>7:
            raise ValueError("Error: spin must be in range from 0 to 7!")
        self.spin = spin

        if spin<=3:
            self.clockwiseSpin=False
        else:
            self.clockwiseSpin=True

        self.grid = numpy.full((size,size), EMPTY_REMARK)
        self.incrementNumber = incrementNumber
        self.n = start

    def isOdd(self,n):
        return n % 2 != 0
    
    def isEven(self,n):
        return n % 2 == 0

    def increment(self):
        self.n += self.incrementNumber

    def isPrime(self,n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False

        #iterate limit is square root of n
        r = int(n**0.5)

        #iterate with steps of 5  
        f = 5
        while f <= r:
            #print '\t',f
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True

    def gridIsFilled(self):
        for x in range(0,self.size):
            for y in range(0,self.size):
                if self.grid[x,y]==EMPTY_REMARK:
                    return False
        return True
    
    def isCorner(self, x, y):
        neighbours = 0

        #lower neighbour
        if not x+1>=self.size and self.grid[x+1,y] != EMPTY_REMARK:    
            neighbours += 1

        #right neighbor
        if not y+1>=self.size and self.grid[x,y+1] != EMPTY_REMARK:    
            neighbours += 1

        #upper neighbour
        if not x-1<0 and self.grid[x-1,y] != EMPTY_REMARK:    
            neighbours += 1

        #left neighbour
        if not y-1<0 and self.grid[x,y-1] != EMPTY_REMARK:    
            neighbours += 1

        #lower right neighbour
        if not x+1>=self.size and not y+1>=self.size and self.grid[x+1,y+1] != EMPTY_REMARK:    
            neighbours += 1

        #upper left neighbour
        if not x-1<0 and not y-1<0 and self.grid[x-1,y-1] != EMPTY_REMARK:    
            neighbours += 1

        #lower left neighbour
        if not x+1>=self.size and not y-1<0 and self.grid[x+1,y-1] != EMPTY_REMARK:    
            neighbours += 1

        #upper right neighbour
        if not x-1<0 and not y+1>=self.size and self.grid[x-1,y+1] != EMPTY_REMARK:    
            neighbours += 1

        print("isCorner(): neighbours=" + str(neighbours))

        #only a single neighbour is set -> corner! 
        if neighbours<=2: return True
               
        return False

    def getNextIndex(self, currX, currY, currDirection):
        '''
        direction:
            0 -> down
            1 -> right
            2 -> up
            3 -> left
        '''
        
        #down
        if currDirection==0:
            if currX+1>=self.size: return (-1,-1)
            if self.grid[currX+1,currY]==EMPTY_REMARK:
                return (currX+1,currY)

        #right
        if currDirection==1:
            if currY+1>=self.size: return (-1,-1)
            if self.grid[currX,currY+1]==EMPTY_REMARK:
                return (currX,currY+1)
               
                    
        #up
        if currDirection==2:
            if currX-1<0: return (-1,-1)
            if self.grid[currX-1,currY]==EMPTY_REMARK:
                return (currX-1,currY)

        #left
        if currDirection==3:
            if currY-1<0: return (-1,-1)
            if self.grid[currX,currY-1]==EMPTY_REMARK:
                return (currX,currY-1)

    def getNextDirection(self, x, y, direction):
        '''
        direction:
            0 -> down
            1 -> right
            2 -> up
            3 -> left
        '''
        
        neighbours = 0
        newDirection = -1

        #lower neighbour
        if not x+1>=self.size and self.grid[x+1,y] != EMPTY_REMARK:    
            neighbours += 1

        #right neighbor
        if not y+1>=self.size and self.grid[x,y+1] != EMPTY_REMARK:    
            neighbours += 1

        #upper neighbour
        if not x-1<0 and self.grid[x-1,y] != EMPTY_REMARK:    
            neighbours += 1

        #left neighbour
        if not y-1<0 and self.grid[x,y-1] != EMPTY_REMARK:    
            neighbours += 1


        #a direction can only be changed at corners, so only if 2 neighbours are set the direction
        #is set and depends on the spin (clockwise or counter-clockwise) 

        #lower right neighbour
        if not x+1>=self.size and not y+1>=self.size and self.grid[x+1,y+1] != EMPTY_REMARK:   #DONE   
            neighbours += 1
            if self.clockwiseSpin:
                #go left
                newDirection=1
            else:
                #go down
                newDirection=0       

        #upper left neighbour
        if not x-1<0 and not y-1<0 and self.grid[x-1,y-1] != EMPTY_REMARK:  #DONE   
            neighbours += 1
            if self.clockwiseSpin:
                #go left 
                newDirection=3
            else:
                #go up
                newDirection=2

        #lower left neighbour
        if not x+1>=self.size and not y-1<0 and self.grid[x+1,y-1] != EMPTY_REMARK:  #DONE   
            neighbours += 1
            if self.clockwiseSpin:
                #go down
                newDirection=0
            else:
                #go left
                newDirection=3 

        #upper right neighbour
        if not x-1<0 and not y+1>=self.size and self.grid[x-1,y+1] != EMPTY_REMARK:    
            neighbours += 1
            if self.clockwiseSpin:
                #go up 
                newDirection=2
            else:
                #go right
                newDirection=1

        #only 2 neighbours-> corner! change direction
        if neighbours<=2: return newDirection
        
        
        #if more than 2 neighbours then a corner is not reached -> go straight ahead (use old direction from input)        
        return direction


    def fillGrid(self):
        n = self.start
        center = int(self.size / 2)  

        self.grid[center,center] = self.n
        self.increment()

        #0 = down right
        if self.spin==0:
            self.grid[center+1,center] = self.n
            self.increment()
    
            self.grid[center+1,center+1] = self.n
            self.increment()

            lastX=center+1
            lastY=center+1
            lastDirection=1
        
        #1 = right up    
        if self.spin==1:
            self.grid[center,center+1] = self.n
            self.increment()
    
            self.grid[center-1,center+1] = self.n
            self.increment()

            lastX=center-1
            lastY=center+1
            lastDirection=2

        #2 = up left
        if self.spin==2:
            self.grid[center-1,center] = self.n
            self.increment()
    
            self.grid[center-1,center-1] = self.n
            self.increment()

            lastX=center-1
            lastY=center-1
            lastDirection=3
        
        #3 = left down 
        if self.spin==3:
            self.grid[center,center-1] = self.n
            self.increment()
    
            self.grid[center+1,center-1] = self.n
            self.increment()

            lastX=center+1
            lastY=center-1
            lastDirection=0
        
        #4 = down left
        if self.spin==4:
            self.grid[center+1,center] = self.n
            self.increment()
    
            self.grid[center+1,center-1] = self.n
            self.increment()

            lastX=center+1
            lastY=center-1
            lastDirection=3

        #5 = left up
        if self.spin==5:
            self.grid[center,center-1] = self.n
            self.increment()
    
            self.grid[center-1,center-1] = self.n
            self.increment()

            lastX=center-1
            lastY=center-1  
            lastDirection=2      

        #6 = up right
        if self.spin==6:
            self.grid[center-1,center] = self.n
            self.increment()
    
            self.grid[center-1,center+1] = self.n
            self.increment()

            lastX=center-1
            lastY=center+1
            lastDirection=1

        #7 = right down
        if self.spin==7:
            self.grid[center,center+1] = self.n
            self.increment()
    
            self.grid[center+1,center+1] = self.n
            self.increment()  

            lastX=center+1
            lastY=center+1 
            lastDirection=0

        #after first 3 elements are set -> set rest until grid is filled
        while(not self.gridIsFilled()):
            lastDirection = self.getNextDirection(lastX,lastY,lastDirection)
            p = self.getNextIndex(lastX,lastY,lastDirection)

            lastX=p[0]
            lastY=p[1]

            self.grid[p]=self.n
            self.increment()

        print(self.grid)

     
