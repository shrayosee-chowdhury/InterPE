import tkinter as tk 
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
           buttons[combo[0]].config(bg="blue")
           buttons[combo[1]].config(bg="blue")
           buttons[combo[2]].config(bg="blue")
           messagebox.showinfo("tic_tac_toe" , f"Player {buttons[combo[0]]["text"]} wins!")
           root.quit()

def button_click(index):
    if buttons [index]["text"] == "" and not winner:
       buttons[index]["text"] = current_player
       check_winner()
       toggle_player()

def toggle_player():
     global current_player 
     current_player = "x" if current_player == "o" else "o"
     label.config (text=f"player {current_player}'s turn")

root =tk.Tk()
root.title("tic_tac_toe")

buttons =[]
for i in range(9):
    button = tk.Button(root, text="", font=("Calibri", 25), width=8, height=3, command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

    
current_player ="x"
winner= False

label =tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()









    