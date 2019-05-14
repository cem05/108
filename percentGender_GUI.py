#Write and test a program that asks user for number of males and females registered in class and display the percentages of males & females in the class.

#remember EVERY INPUT & OUTPUT MUST BE DEFINED!!

from graphics import *
def main():
    win = GraphWin("Percent Gender", 400, 400)
    win.setCoords(0.0, 0.0, 4.0, 4.0)

    #draw interface and labels
    Text(Point(1.75,3.75), 'This program is used to calculate \n Percent gender of the class.').draw(win)

    Text(Point(1,3.25), 'Enter # Female Students: ').draw(win)
    Finput = Entry(Point(2.25,3.25), 4)
##    Finput.setText("   ")  THIS THREW AN ERROR
    Finput.setText('1')
    Finput.draw(win)
    Text(Point(1.60,0.75), 'Female Percent: ').draw(win)
    Foutput = Text(Point(2.5,0.75),'  ')
    Foutput.draw(win)

    Text(Point(1,3), 'Enter # Male Students: ').draw(win)
    Minput = Entry(Point(2.25,3.0), 4)
##    Minput.setText("   ")  THIS THREW AN ERROR!
    Minput.setText('1')
    Minput.draw(win)
    Text(Point(1.60,0.50), 'Male Percent:').draw(win)
    Moutput = Text(Point(2.5, 0.50),' ')
    Moutput.draw(win)
    
    button = Text(Point(2.0,2.0),"Click to \n Calculate!")
    button.draw(win)
    Rectangle(Point(1.5,1.5), Point(2.5,2.5)).draw(win)
    
 #wait for a mouse click
    win.getMouse()

    #convert input
    numF = int(Finput.getText())
    numM = int(Minput.getText())
    Fpercent = numF / (numM + numF)*100
    Mpercent = numM / (numF + numM)*100

    #display output and change button
    Foutput.setText("%0.0f" % Fpercent)
    Moutput.setText("%0.0f" % Mpercent)
    button.setText('Quit')

    # wait for click and then quit
    win.getMouse()
    win.close()
main()

