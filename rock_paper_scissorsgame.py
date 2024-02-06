from tkinter import *
from random import  randint
from tkinter import ttk

root = Tk()
root.title("ROCK, PAPER, SCISSORS")
#root.iconbitmap('C:\Users\Anumita\PycharmProjects\gui projects\passwordgenerator.py')
root.geometry("500x500")

root.config(bg="white")
rock=PhotoImage(file="rock.png")
paper=PhotoImage(file= "paper.png")
scissors=PhotoImage(file= "scissors.png")

image_list=[rock,paper,scissors]

pick_number = randint(0,2)

image_label = Label(root, image=image_list[pick_number],bd=0)

def spin():
    pick_number = randint(0,2)
    image_label.config( image=image_list[pick_number])
    if user_chooice.get()== "rock":
        user_chooice_value = 0
    elif user_chooice.get()=="paper":
        user_chooice_value =1
    elif user_chooice.get()=="scissors":
        user_chooice_value = 2


    if user_chooice_value==0:#rock
        if pick_number==0:
            win_lose_label.config(text='ITS A TIE! SPIN AGAIN ')
        elif pick_number==1:
            win_lose_label.config(text='paper beats rock! you loose ')
        elif pick_number==2:
            win_lose_label.config(text='rock smashes scissors! you won ')

    if user_chooice_value==1:#paper
        if pick_number==1:
            win_lose_label.config(text='ITS A TIE! SPIN AGAIN ')
        elif pick_number==0:
            win_lose_label.config(text='paper beats rock! you won')
        elif pick_number==2:
            win_lose_label.config(text='scisoors cut paper! you loose ')


    if user_chooice_value==2:#scissors
        if pick_number==2:
            win_lose_label.config(text='ITS A TIE! SPIN AGAIN ')
        elif pick_number==0:
            win_lose_label.config(text='rock smasshes scissors! you loose ')
        elif pick_number==1:
            win_lose_label.config(text='scissors cut papers! you won ')




user_chooice = ttk.Combobox(root, value=('rock','paper','scissors'))
user_chooice.current(0)
user_chooice.pack(pady=20)


spin_button = Button(root,text="SPIN!" , command=spin)
spin_button.pack(pady=10)

win_lose_label = Label(root,text="", font= ("Segoe UI Variable",20),bg="white")
win_lose_label.pack(pady=55)






image_label.pack(pady=20)







root.mainloop()
