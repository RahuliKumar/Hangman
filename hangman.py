from graphics import*
import random,string
from random import choice
win=GraphWin('keyboard',1400,800)
dis=Text(Point(500,20),'WELCOME TO HANGMAN GAME')
dis.draw(win)
dis.setSize(20)
WORDLIST_FILENAME = "words.txt"
def loadWords():
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    return wordlist
def chooseWord(wordlist):
    return random.choice(wordlist)
a1=chooseWord(loadWords())
text1=Text(Point(170,80),'You have to guess a '+str(len(a1))+' letter word!')
text1.draw(win)
text1.setFill('Red')
text1.setStyle('bold')
text1.setSize(14)
text1=Text(Point(180,110),'Click on the letter you gussed (keyboard)')
text1.draw(win)
text1.setSize(14)
text1=Text(Point(164,140),'You can have total 7 wrong guesses')
text1.draw(win)
text1.setSize(14)
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k=[]
i,o=0,12
def isInside(p,rect):
    rectP1 = rect.getP1();
    rectP2 = rect.getP2();
    if(p.getX() >= rectP1.getX() and p.getX() <= rectP2.getX() and 
       p.getY() >= rectP1.getY() and p.getY() <= rectP2.getY()):
         return True;
    else:
	     return False;
def display(i):
    global circle1,oval1,line5,line6,line7,line8,line4,rect,line9
    if i==0:
        line3=Line(Point(680,600),Point(1200,600))
        line3.setWidth(6)
        line3.draw(win)
        rect=Rectangle(Point(750,480),Point(900,600))
        rect.setOutline('red')
        rect.setWidth(5)
        rect.draw(win)
        return ''
    if i==1:
        line1=Line(Point(1100,100),Point(1100,600))
        line1.setWidth(3)
        line1.draw(win)
        return ''
    if i==2:
        line2=Line(Point(800,100),Point(1100,100))
        line2.setWidth(3)
        line2.draw(win)
        return ''
    if i==3:
        line=Line(Point(820,100),Point(820,200))
        line.setWidth(3)
        line.draw(win)
        line4=Line(Point(820,100),Point(820,200))
        line4.setWidth(3)
        line4.draw(win)
        return ''
    if i==4:
        circle1=Circle(Point(820,230),30)
        circle1.setWidth(2)
        circle1.draw(win)
        return ''
    if i==5:
        oval1=Oval(Point(860,260),Point(790,410))
        oval1.setWidth(2)
        oval1.draw(win)
        return ''
    if i==6:
        line5=Line(Point(820,410),Point(820,480))
        line5.setWidth(2)
        line5.draw(win)
        line8=Line(Point(820,480),Point(812,480))
        line8.setWidth(2)
        line8.draw(win)
        line9=Line(Point(830,480),Point(822,480))
        line9.setWidth(2)
        line9.draw(win)
        line6=Line(Point(830,380),Point(830,480))
        line6.setWidth(2)
        line6.draw(win)
        return ''
    if i==7:
        line7=Line(Point(822,280),Point(822,340))
        line7.setWidth(2)
        line7.draw(win)
        rect.undraw()
        i1=0
        while i1<30:
            circle1.move(0,1)
            oval1.move(0,1)
            line4.move(0,1),line5.move(0,1),line6.move(0,1),line7.move(0,1),line8.move(0,1),line9.move(0,1)
            time.sleep(0.01)
            i1=i1+1
        text=Text(Point(830,550),'HANGED TILL DEATH')
        text.setFill('Red')
        text.setStyle('bold')
        text.draw(win)
        return ''
while i<2:#display board
            j=0
            while j<13:
                rect=Rectangle(Point(175+34*j,580+34*i),Point(209+34*j,614+34*i))
                k=k+[rect]
                text=Text(Point((175+34*j+209+34*j)/2,(580+34*i+614+34*i)/2),a[i+j+o*i])
                rect.setFill("Green")
                rect.draw(win)
                text.draw(win)
                text.setStyle('bold')
                j=j+1
            i=i+1
r=[]
for i in k:
    r=r+[i]
c=Rectangle(Point(175,580),Point(209+34*12,648))
def modify(x,temp):
    a12=''
    n=a1.upper()
    for i in range(len(a1)):
        if n[i]==x:
            temp[i]=x
    global b1
    b1=temp
    for j in temp:
        a12=a12+j+'   '
    return a12

def check(x):
    w=a1.upper()
    for i in w:
        if i==x:
            return True
    return False
b8=[]
for i in a1.upper():
        b8=b8+[i]
b2=[]
for i in a1.upper():
        b2=b2+[i]
def hint():
   for i in b1:
       for j in b8:
           if i==j:
               b8.remove(i)
   hin=choice(b8)
   return hin
def wait(a4):
    h,l=0,0
    global text6,text5,rect9,text32
    text6=text=Text(Point(140+(12)*len(a1),170),'YOUR CURRENT STATUS:'+modify('!',['_']*len(a1)))
    text6.setStyle('bold')
    text6.setSize(15)
    text6.draw(win)
    text2=Text(Point(140,500),'WRONG GUESSES:')
    text2.setStyle('bold')
    text2.setSize(15)
    text2.draw(win)
    text=Text(Point(240,500),str(0))
    text.setSize(15)
    text.draw(win)
    rect9=Rectangle(Point(45,520),Point(105,540))
    rect9.setOutline('red')
    rect9.draw(win)
    text8=Text(Point(75,530),'HINT:')
    text8.setStyle('bold')
    text8.setSize(15)
    text8.draw(win)
    text32=Text(Point(120,530),'')
    text32.setStyle('bold')
    text32.setSize(15)
    text32.draw(win)
    while True:
        if a4==8:
            text5=Text(Point(110+(10)*len(a1),300),'YOU ARE OUT OF GUESS,MAN HANGED')
            text5.setStyle('bold')
            text5.setSize(12)
            text5.setFill('Red')
            text5.draw(win)
            text5=Text(Point(110+(10)*len(a1),330),'THE WORD WAS:'+a1.upper())
            text5.setStyle('bold')
            text5.setSize(12)
            text5.draw(win)
            time.sleep(3)
            win.close()
            return ''
        inputP = win.getMouse()
        while  (not(isInside(inputP,rect9)) and not(isInside(inputP,c))):
            inputP = win.getMouse()
        if isInside(inputP,rect9):
            text32.undraw()
            text32=Text(Point(120,530),hint())
            text32.setStyle('bold')
            text32.setSize(15)
            text32.draw(win)
        for i in k:
            if isInside(inputP,i):
                i.setFill('Red')
                x=a[r.index(i)]
                if check(x):
                    if l==1:
                        text5.setText('')
                    l=0
                    text6.setText('')
                    text6=Text(Point(140+(12)*len(a1),170),'YOUR CURRENT STATUS:'+modify(x,b1))
                    text5.setText('')
                    text6.setStyle('bold')
                    text6.setFill('Blue')
                    text6.setSize(15)
                    text6.draw(win)
                    if b1==b2:
                        text6=Text(Point(160+(10)*len(a1),210),'CONGRATS! YOU SAVED THE MAN')
                        text5.setText('')
                        text6.setStyle('bold')
                        text6.setSize(18)
                        text6.setFill('Blue')
                        text6.draw(win)
                        text6=Text(Point(150+(10)*len(a1),280),'THANK U....EXITING IN FEW SECONDS')
                        text6.setSize(14)
                        text6.draw(win)
                        time.sleep(5)
                        win.close()
                        return ''
                else:
                    print display(h)
                    l=1
                    text.setText('')
                    text=Text(Point(240,500),str(h+1))
                    text.setSize(15)
                    text5=Text(Point(110+(10)*len(a1),240),'WRONG GUESS')
                    text5.setStyle('bold')
                    text5.setSize(20)
                    text5.setFill('Red')
                    text5.draw(win),text.draw(win)
                    h=h+1
                    a4=a4+1
                k.remove(i)
print wait(0)


    
