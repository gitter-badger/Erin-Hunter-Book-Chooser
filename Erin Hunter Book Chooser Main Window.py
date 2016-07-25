from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Erin Hunter Book Chooser")

label = Label( window, text = "Welcome to the Erin Hunter Book Chooser.\nPlease select your favorite animal below and the app will select your favorite Erin Hunter authored book.\n You can visit the website link displayed to learn more afterwards.\n")
            
label.pack( padx = 300, pady = 100 )


frame = Frame(window)

book = StringVar()


radio_1 = Radiobutton( frame, text='Cats', \
                               variable = book, value = ' Warriors by Erin Hunter.\nVisit warriorscats.com for more information.')
radio_2 = Radiobutton( frame, text='Bears', \
                               variable = book, value = ' Seekers by Erin Hunter.\nVisit seekrsbears.com for more information.')
radio_3 = Radiobutton(frame, text='Dogs', \
                                variable = book, value = ' Survivors by Erin Huter.\nVisit survivorsdogs.com for more information.')

radio_1.select()

def dialog():
    box.showinfo('Erin Hunter Book Selection', \
                 'Your Erin Hunter Book selection is:' + book.get() )

btn = Button( frame, text = 'Choose', command = dialog)

btn.pack(side = RIGHT, padx = 5)
radio_1.pack(side = LEFT)
radio_2.pack(side = LEFT)
radio_3.pack(side = LEFT)
frame.pack( padx = 30, pady = 30 )

window.mainloop()


window.mainloop()
    
