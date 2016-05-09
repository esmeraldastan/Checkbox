import Tkinter, tkFont 
#Graphical User Interface (GUI)
root = Tkinter.Tk()
root.title('ChaseRekz')
#canvas = Tkinter.Canvas(root, height = 300, width = 600, relief = Tkinter.RAISED, bg= 'blue')
#canvas.grid()

#checkbox = canvas.create_rectangle( 100, 200, 200, 300, dash = [1,4])
#check = canvas.create_line(100, 250, 150, 300, 220, 150, fill = 'green', width = 20)
#message = canvas.create_text(380, 250, text = 'Try this!', font = ('Arial', -100))

#######################
#Checkbox
#####################

#box = Tkinter.Checkbutton(root, text='This is a checkbot.')
#box.grid(row=1, column=0)



times_pressed =0

def pressed(x):
    
    try:
        del editor
    except:
        pass
    global times_pressed
    times_pressed = x
    #recreates the text box
    customFont = tkFont.Font(family = 'Serif', size = 40)
    editor = Tkinter.Text(width = 25, height =4, font =(customFont))
    editor.grid(row = 0, column = 0) 
    
    #adds the text to the box
    editor.insert(Tkinter.END, " Number of puppies killed: ")
    editor.insert(Tkinter.END, times_pressed)
    editor.see(Tkinter.END)
    
    #disable chrging the text box
    editor.config(state = Tkinter.DISABLE)
    #editor.config(state = Tkinter.NORMAL)
    
button = Tkinter.Button(root, text= 'Add 1', height = 5, command = lambda: pressed(1))
button.grid(row = 1, column= 0, pady = 100)

button2 = Tkinter.Button(root, text= 'Add 2', height = 5, command = lambda: pressed(2))
button2.grid(row = 1, column= 1, pady = 100)

button3 = Tkinter.Button(root, text= 'Add 3', height = 5, command = lambda: pressed(3))
button3.grid(row = 1, column= 2, pady = 100)

button4 = Tkinter.Button(root, text= 'Add 4', height = 5, command = lambda: pressed(4))
button4.grid(row = 1, column= 3, pady = 100)

button5 = Tkinter.Button(root, text= 'Add 5', height = 5, command = lambda: pressed(5))
button5.grid(row = 1, column= 4, pady = 100)
'''
radio =[0]*4 #creat a list
data = Tkinter.IntVar()
for i in range(4):
    radio[i]= Tkinter.Radiobutton(root, text=str(i), variable = data, value = i)
    radio[i].grid(row = 2, column = i)
data.set(3)'''

root.mainloop()