#ulam.py

import numpy

EMPTY_REMARK_NUMBER=-1

'''
UlamSpiral represents a Ulam spiral AS a numpy 2D array with a given size, start number and spin
'''

class UlamSpiral:

    def __init__(self, size, spin, start):
        '''
        spin describes the direction of filling the grid from center point
            0 = down right
            1 = down left
            2 = up right
            3 = up left 
            4 = right up
            5 = right down
            6 = left up
            7 = left down 
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

        #declare offsets for turning at corners
        if spin==0:
            self.xOff=1
            self.yOff=1

        if spin==1:
            self.xOff=1
            self.yOff=-1

        if spin==2:
            self.xOff=-1
            self.yOff=1

        if spin==3:
            self.xOff=-1
            self.yOff=-1

        if spin==4:
            self.xOff=1
            self.yOff=-1

        if spin==5:
            self.xOff=1
            self.yOff=1

        if spin==6:
            self.xOff=-1
            self.yOff=-1

        if spin==7:
            self.xOff=-1
            self.yOff=1

        self.grid = numpy.full((size,size), EMPTY_REMARK_NUMBER)

    def isOdd(self,n):
        return n % 2 != 0
    
    def isEven(self,n):
        return n % 2 == 0

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
                if self.grid[x,y]==EMPTY_REMARK_NUMBER:
                    return False
        return True
    
    def getNextIndex(self, currX, currY, currDirection):
        '''
        direction:
            0 -> down
            1 -> right
            2 -> up
            3 -> left
        '''
        #print(currX)
        
        #down
        if currDirection==0:
            print("DIR0")
            if currX+1>=self.size: return (-1,-1)
            if self.grid[currX+1,currY]==EMPTY_REMARK_NUMBER:
                print("DIR0 [DOWN] ->straight [DOWN]")
                return (currX+1,currY)
            if currY+1>=self.size: return (-1,-1)
            if self.grid[currX+1,currY+self.yOff]==EMPTY_REMARK_NUMBER:
                print("DIR0 [DOWN] ->turn [LEFT/RIGHT]")
                return (currX+1,currY+self.yOff)

        #right
        if currDirection==1:
            print("DIR1")
            if currX+1>=self.size: return (-1,-1)
            if self.grid[currX,currY+1]==EMPTY_REMARK_NUMBER:
                print("DIR1 [RIGHT] ->straight [RIGHT]")
                return (currX+1,currY)
            if currY+1>=self.size: return (-1,-1)
            if self.grid[currX+self.xOff,currY+1]==EMPTY_REMARK_NUMBER:
                print("DIR1 [RIGHT] ->turn [UP/DOWN]")
                return (currX+self.xOff,currY+1)
               
                    
            

        #return (0,0)

    def changeDirection(self, x, y, direction):
        neighbours = 0

        if not x+1>=self.size and self.grid[x+1,y] != EMPTY_REMARK_NUMBER:    
            neighbours += 1

        if not y+1>=self.size and self.grid[x,y+1] != EMPTY_REMARK_NUMBER:    
            neighbours += 1

        if not x+1>=self.size and not y+1>=self.size and self.grid[x+1,y+1] != EMPTY_REMARK_NUMBER:    
            neighbours += 1

        if not x-1<0 and self.grid[x-1,y] != EMPTY_REMARK_NUMBER:    
            neighbours += 1

        if not y-1<0 and self.grid[x,y-1] != EMPTY_REMARK_NUMBER:    
            neighbours += 1

        if not x-1<0 and not y-1<0 and self.grid[x-1,y-1] != EMPTY_REMARK_NUMBER:    
            neighbours += 1

        if neighbours<=1: return True
        return False

    def fillGrid(self):
        center = int(self.size / 2)
        print("center:" + str(center))
        
        #for n in range(start,size*size):
        self.grid[center,center] = self.start
        #self.grid[center + 1,center] = start + 1    

        print(self.grid)             

        lastX=center
        lastY=center
 
        lastCubeSize=1

        # 1 -> down
        # 2 -> right
        # 3 -> up
        # 4 -> left
        lastDirection=self.spin
    
        #print("lastDirection: " + str(lastDirection))

        #print(self.getNextIndex(lastX,lastY,lastDirection))

        print("change Directions?: " + str(self.changeDirection(lastX,lastY,lastDirection)))
        p = self.getNextIndex(lastX,lastY,lastDirection)
        print(p)
        lastX=p[0]
        lastY=p[1]

        self.grid[p]=self.start+1

        print(self.grid)

        print("change Directions?: " + str(self.changeDirection(lastX,lastY,lastDirection)))
        p = self.getNextIndex(lastX,lastY,lastDirection)
        print(p)
        lastX=p[0]
        lastY=p[1]

        self.grid[p]=self.start+1

        print(self.grid)

        '''
        while(not self.gridIsFilled()):
            print("last:" + str(lastX) + "," + str(lastY))
            
            start += 1     
            print("current n:" + str(start) 

        '''    

        









       
        
