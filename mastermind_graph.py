from tkinter import *
from math import sqrt
from tkinter.messagebox import showinfo
from random import *
import winsound
root = Tk()
root.title("Mastermind")
canvas = Canvas(root, width=250, height=416,bg="navy",relief="sunken")
canvas.grid()

game = {
    'width': 176,
    'height': 416,
    'cell': [ 

    ]
}

color = ['deep pink','turquoise2','tomato','OliveDrab1']

r_One = 16

r_Two = 6

index = 0

x = 30

y = 390

l = []

winner = False

looser = False

def print_game(game):

    # Prints the game to the console.
    
    canvas.delete("all")

    for i in range(10,180,40):

        canvas.create_line(i,410,i,10, fill="antique white",dash=1)

    for i in range(10,440,40):

        canvas.create_line(10,i,170,i, fill="snow", width=2)

    canvas.create_line(0,420,0,0, fill="gray30", width=20)
    canvas.create_line(0,420,177,420, fill="gray30", width=16)
    canvas.create_line(177,0,177,420, fill="gray30", width=10)
    canvas.create_line(177,0,0,0, fill="gray30", width=16)

    y = game['height'] -1
    while 0 <= y :

        for x in range(30,game['width'],40):
            
            get_cell_value(game, x, y)

        y -= 1

    if len(game['cell']) == 0 :

            canvas.create_oval(30-r_One, 390-r_One, 30+r_One, 390+r_One, fill="deep pink",width=2,outline="dark goldenrod")


def get_cell_value(game, x, y):

    global r_One

    for cell in game['cell']:

        if cell['x'] == x and cell['y'] == y :

            
            canvas.create_oval(x-r_One, y-r, x+r_One, y+r_One, fill=cell['color'],width=2,outline="dark goldenrod")
            
def make_move(game, x, y,color):
        
    game['cell'].append({'x':x, 'y':y, 'color': color})

def on_key_press(event):
    global winner

    global looser

    if (not winner) and (not looser) :

        global color
        
        global index

        global game 

        global x

        global y

        key = event.keysym

        if key == "Left" :
            
            if index == 0  :

                index = 3

            elif index == 1 :

                index = 0

            elif index == 2 :

                index = 1

            elif index == 3 :

                index = 2

            if len(game['cell']) == 0 :

                canvas.create_oval(30-r_One, 390-r_One, 30+r_One, 390+r_One, fill=color[index],width=2,outline="dark goldenrod")

            else:

                canvas.create_oval(x-r_One, y-r_One, x+r_One, y+r_One, fill=color[index],width=2,outline="dark goldenrod")




        elif key == "Right" :

            if index == 0  :

                index = 1

            elif index == 1 :

                index = 2

            elif index == 2 :

                index = 3

            elif index == 3 :

                index = 0

            if len(game['cell']) == 0 :

                canvas.create_oval(30-r_One, 390-r_One, 30+r_One, 390+r_One, fill=color[index],width=2,outline="dark goldenrod")

            else:

                canvas.create_oval(x-r_One, y-r_One, x+r_One, y+r_One, fill=color[index],width=2,outline="dark goldenrod")

            

        elif key == "Return" :


            make_move(game,x,y,color[index])

            test = []

            nb = []

            if y == 30 and x == 150  :

                for cell in game['cell']:

                    for i in range(30,190,40):

                        if cell['y'] == y and cell['x'] == i :

                            test.append(cell['color'])


                nb = nbColorGoodAndWrongPlaces(l,test)

                if nb[0] == 4 :

                    winner = True

                if not winner :

                    looser = True

                    canvas.delete("all")

                    canvas.config(width=200,height=100,bg="black")


                    canvas.create_rectangle(50, 20, 150, 80, fill="dark goldenrod")

                    canvas.create_rectangle(65, 35, 135, 65, fill="navy")

                    canvas.create_line(0, 0, 50, 20, fill="dark goldenrod", width=3)

                    canvas.create_line(0, 100, 50, 80, fill="dark goldenrod", width=3)

                    canvas.create_line(150,20, 200, 0, fill="dark goldenrod", width=3)

                    canvas.create_line(150, 80, 200, 100, fill="dark goldenrod", width=3)

                    canvas.create_text(200 / 2, 100 / 2, text="↓ Loose.. ↓",font=("Georgia",11))

                    x = 200

                    y = 200

                    root.config(bg = "black")

                    label = Label(root, text="Damage .. \n",foreground="gold",background="black",font=("Georgia",40))

                    labell = Label(root, text=" Congratulation ! ",foreground="black",background="black",font=("Georgia",40))

                    labell.grid()

                    label.grid()

                    button = Button(root,text='Quit',command=close,height=2,width=8,activebackground="snow",activeforeground="dark goldenrod",bd=4,bg="grey")

                    button.grid()

            if x >= 150 :

                test = []

                for cell in game['cell']:

                    for i in range(30,190,40):

                        if cell['y'] == y and cell['x'] == i :

                            test.append(cell['color'])


                nb = nbColorGoodAndWrongPlaces(l,test)

                if nb[0] == 4 :

                    winner = True

                delta = 0

                while nb != [0,0] :

                    aleat = randint(0,1)

                    if aleat == 0 and nb[0] > 0 :

                        canvas.create_oval(195-r_Two+delta, y-r_Two, 195+r_Two+delta, y+r_Two, fill="white",width=2,outline="black")

                        nb[0] -= 1

                        delta += 15

                    elif nb[1] > 0 :

                        canvas.create_oval(195-r_Two+delta, y-r_Two, 195+r_Two+delta, y+r_Two, fill="black",width=1,outline="white")

                        nb[1] -= 1

                        delta += 15 

                
                if winner :

                    canvas.delete("all")

                    canvas.config(width=200,height=100,bg="black")


                    canvas.create_rectangle(50, 20, 150, 80, fill="dark goldenrod")

                    canvas.create_rectangle(65, 35, 135, 65, fill="navy")

                    canvas.create_line(0, 0, 50, 20, fill="dark goldenrod", width=3)

                    canvas.create_line(0, 100, 50, 80, fill="dark goldenrod", width=3)

                    canvas.create_line(150,20, 200, 0, fill="dark goldenrod", width=3)

                    canvas.create_line(150, 80, 200, 100, fill="dark goldenrod", width=3)

                    canvas.create_text(200 / 2, 100 / 2, text="☺ Win ☺",font=("Georgia",13))

                    x = 0

                    y = 0

                    root.config(bg = "black")

                    label = Label(root, text="Congratulation ! \n",foreground="gold",background="black",font=("Georgia",40))

                    label.grid()

                    button = Button(root,text='Quit',command=close,height=2,width=8,activebackground="snow",activeforeground="dark goldenrod",bd=4,bg="grey")

                    button.grid()


                x = 30

                y -= 40

            else:

                x += 40

            canvas.create_oval(x-r_One, y-r_One, x+r_One, y+r_One, fill="deep pink",width=2,outline="dark goldenrod")

            index = 0

def close():

    global root

    root.destroy()


def tirage():

    global l
   
    i=1

    while i<=4:

        n = randint(0,3)

        OneColor = color[n]

        l.append(OneColor)

        i=i+1



def nbColorGoodAndWrongPlaces(tirage,essai):

    nbGP=0

    nbWP=0

    e=list(essai)

    for i in range(0,4):

        if tirage[i]==e[i]:

            nbGP=nbGP+1

            e[i]='-'

        else:

            j=0

            wrongPlace=False

            while j<4 and wrongPlace==False:

                if tirage[i]==e[j]:

                    nbWP=nbWP+1

                    e[j]='-'

                    wrongPlace=True

                j=j+1
    
    answer = [nbGP,nbWP]

    return answer



tirage()