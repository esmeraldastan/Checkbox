import Tkinter, tkFont 
#Graphical User Interface (GUI)
root = Tkinter.Tk()
root.title('ChaseRekz')
canvas = Tkinter.Canvas(root, height = 300, width = 600, relief = Tkinter.RAISED, bg= 'blue')
canvas.grid()


#scrolbar

scrollbar = Tkinter.Scrollbar(root)
scrollbar.grid(row = 0, column = 6 , rowspan = 4)
#checkbox = canvas.create_rectangle( 100, 200, 200, 300, dash = [1,4])
#check = canvas.create_line(100, 250, 150, 300, 220, 150, fill = 'green', width = 20)
#message = canvas.create_text(380, 250, text = 'Try this!', font = ('Arial', -100))

######################
#Checkbox
#####################

#box = Tkinter.Checkbutton(root, text='This is a checkbot.')
#box.grid(row=1, column=0)



times_pressed =0

def pressed():
    
    try:
        del editor
    except:
        pass
    global times_pressed
    times_pressed += 1
    #recreates the text box
    customFont = tkFont.Font(family = 'Serif', size = 40)
    editor = Tkinter.Text(width = 20, height =2, font = customFont)
    editor.grid(row = 0, column = 0) 
    
    #adds the text to the box
    editor.insert(Tkinter.END, " Number of puppies killed: ")
    editor.insert(Tkinter.END, data.get())
    editor.see(Tkinter.END)
    
    #disable chrging the text box
    editor.config(state = Tkinter.DISABLE)
    #editor.config(state = Tkinter.NORMAL)
    

    #stuff
            
button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = root.destroy)
button.grid(row = 1, column= 4)

def quit():
    global root
    root.destroy()

def newWindow():
    root2 = Tkinter.Tk()
    editor2 = Tkinter.Text(master = root2, width= 45, height = 0)
    editor2.grid( row= 0 , column = 0, sticky = (Tkinter.N, Tkinter.W, Tkinter.E))
    editor2.insert(Tkinter.END,"heyyo")
    editor2.see(Tkinter.END)
    
    button2 = Tkinter.Button(root2, text= 'New Window', height = 5, command = newWindow)
    button2.grid(row = 1, column= 1)
    
def add():
    global times_pressed
    times_pressed += 1
    editor.insert(Tkinter.END, 'hello' + str(times_pressed)
    editor.insert(Tkinter.END,"hype")
    
    button = Tkinter.Button(root2, text= 'QUIT', width = 10, height = 5, command = root2.destroy)
    button.grid(row = 1, column= 0) 
 
         
button2 = Tkinter.Button(root, text= 'New Window', height = 5, command = newWindow)
button2.grid(row = 1, column= 5)
    #stuff



radio =[0]*4 #creat a list
data = Tkinter.IntVar()
for i in range(4):
    radio[i]= Tkinter.Radiobutton(root, text=str(i), variable = data, value = i)
    radio[i].grid(row = 3, column = i)
data.set(3)



root.mainloop()