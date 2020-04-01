import PIL
from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

#from easy_ocr import ocr_image


Wsudoku = Image.open(r'sudoku.jpg')
Sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

#print(Wsudoku.format)
#print(Wsudoku.size)
#print(Wsudoku.mode)

width, height = Wsudoku.size

Aheight = []
Awidth = []

Cwidth = int(width/9)
Cheight = int(height/9)
for I in range(Cheight,height,Cheight):
    Aheight.append(I)
for J in range(0,width-Cwidth,Cwidth):
    Awidth.append(J)

AI = 0
AJ = 0

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

Cimage = Wsudoku.crop((Awidth[AJ],Awidth[AI],Aheight[AJ],Aheight[AI]))
#Ctext = ocr_image(Cimage,service='youdao')
#Ctext = pytesseract.image_to_string(Wsudoku)
#print(Ctext)
#Cimage.show()


#print(Awidth)
#print(Aheight)
#Wsudoku.show()



# solving

#for I in range(0,9):
#    for J in range(0,9):
#        test

def isRow(A,B,num):
    Ksudoku = []
    KSudoku = Sudoku[A].copy()
    return num in KSudoku
    
    
def isColl(A,B,num):
    MSudoku = []
    for I in range(0,9):
        MSudoku.append(Sudoku[I][B])
    return num in MSudoku

def isCube(A,B,num):
    if (A in range(0,3)) and (B in range(0,3)):
        C,D = 3,3
    elif (A in range(3,6)) and (B in range(0,3)):
        C,D = 6,3
    elif (A in range(6,9)) and (B in range(0,3)):
        C,D = 9,3
    elif (A in range(0,3)) and (B in range(3,6)):
        C,D = 3,6
    elif (A in range(3,6)) and (B in range(3,6)):
        C,D = 6,6
    elif (A in range(6,9)) and (B in range(3,6)):
        C,D = 9,6
    elif (A in range(0,3)) and (B in range(6,9)):
        C,D = 3,9
    elif (A in range(3,6)) and (B in range(6,9)):
        C,D = 6,9
    elif (A in range(6,9)) and (B in range(6,9)):
        C,D = 9,9
    
    for I in range(C-3,C):
        for J in range(D-3,D):
            if (I != A) or (J != B):
                if num==Sudoku[I][J]:
                    return True
    return False
nope = True
def null_possible():
    possible_num = []
    for I in range(0,9):
        possible_num.append([])
    for I in range(0,9):
        for J in range(0,9):
            possible_num[I].append([])
            
def possible():
    null_possible()
    for I in range(0,9):
        for J in range(0,9):
            if Sudoku[I][J] == 0:
                for number in range(1,10):
                    if (not isRow(I,J,number)) and (not isColl(I,J,number)) and (not isCube(I,J,number)):
                                print(I,J,number)
                                possible_num[I][J].append(number)
                                
                #print(possible_num)
    return possible_num

def try_solve():
    while 0 in Sudoku:
        possible_num = possible()
        if nope != True:
            for I in range(0,9):
                for J in range(0,9):
                    if len(possible_num[I][J]) == 1 and possible_num[I][J]!=[]:
                        Sudoku[I][J]=possible_num[I][J][0]
        #else:
        #    minlen = 9
        #    minlenposI = 0
        #    minlenposI = 0
        #    CSudoku = Sudoku.copy()
        #    for I in range(0,9):
        #        for J in range(0,9):
        #            if len(possible_num[I][J])<= minlen:
        #                minlen=len(possible_num[I][J])
        #                minlenposI=I
        #                minlenposJ=J
        #    Sudoku[I][J]=
    print(Sudoku)

def test():
    u = 6
    v = 6
    cislo = 6
    print(isRow(u,v,cislo))
    print(isColl(u,v,cislo))
    print(isCube(u,v,cislo))
print(try_solve())