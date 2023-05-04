import tkinter as tk
def remaining_spots():
    spots = []
    for i in range(3):
        for j in range(3):
            if board[i][j]['text'] == '':
                spots.append((i,j))
    return spots
def check_win():
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != '':
            return 'win'
    for j in range(3):
        if board[0][j]['text'] == board[1][j]['text'] == board[2][j]['text'] != '':
            return 'win'
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
        return 'win'
    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
        return 'win'
    elif remaining_spots() == []:
        return 'draw'
    else:
        return -1
player = 'O'
def gameplay(a,b):
    global player
    if board[a][b]['text'] == '' and check_win() == -1:
        if player == 'O':
            board[a][b].config(text='X', bg = 'pink')
            if check_win() == -1:
                player = 'X'
                label.config(text=("Player O's turn"))
            elif check_win() == 'win':
                label.config(text=("Player X wins"))
            elif check_win() == 'draw':
                label.config(text="Draw!")
        elif player == 'X':
            board[a][b].config(text='O', bg = 'light blue')
            if check_win() == -1:
                player = 'O'
                label.config(text=("Player X's turn"))
            elif check_win() == 'win':
                label.config(text=("Player O wins"))
            elif check_win() == 'draw':
                label.config(text="Draw!")


root = tk.Tk()
root.title('Tic Tac Toe')
root.resizable(300,300)
board=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        board[i][j] = tk.Button(text='',bd= 10, font=('normal',50,'normal'),width=6,height=2,command=lambda a=i,b=j: gameplay(a,b))
        board[i][j].grid(row=i,column=j)
label = tk.Label(text="It's X's turn",font=('normal',22,'bold'))
label.grid(row=3,column=1)

def again():
    for i in range(3):
        for j in range(3):
            board[i][j]['text']= ''
            board[i][j].config(bg='white')
button=tk.Button(text='Restart',font=('normal',15,'bold'),fg='purple',command=again)
button.grid(row=4,column=1)

root.mainloop()