#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('    |   |  ')
    print('  ' + board[7] +  ' | ' + board[8] + ' | ' + board[9])
    print('    |   |  ')
    print('-----------')
    print('    |   |  ')
    print('  ' + board[4] +  ' | ' + board[5] + ' | ' + board[6])
    print('    |   |  ')
    print('-----------')
    print('    |   |  ')
    print('  ' + board[1] +  ' | ' + board[2] + ' | ' + board[3])
    print('    |   |  ')


# In[2]:


test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[3]:


def player_input():
    '''
    output=player1_marker,player2_marker
    '''
    marker=''
    while not(marker=='X'or marker=='O'):
        marker1=input('player1 is choose: x or o').upper()
        if marker1=='X':
            return('X','O')
        else:
            return('O','X')


# In[4]:


player_input()


# In[5]:


def place_marker(board,marker,position):
    board[position]=marker


# In[6]:


test_board


# In[7]:


place_marker(test_board,'%',3)
display_board(test_board)


# In[8]:


def win_check(board,mark):
    return((board[7]==mark and board[8]==mark and board[9]==mark)or
    (board[4]==mark and board[5]==mark and board[6]==mark)or
    (board[1]==mark and board[2]==mark and board[3]==mark)or
    (board[7]==mark and board[4]==mark and board[1]==mark)or
    (board[8]==mark and board[5]==mark and board[2]==mark)or
    (board[9]==mark and board[6]==mark and board[3]==mark)or
    (board[7]==mark and board[5]==mark and board[3]==mark)or
    (board[9]==mark and board[5]==mark and board[1]==mark))


# In[9]:


display_board(test_board)
win_check(test_board,'X')


# In[10]:


import random
def first_choose():
    flip=random.randint(0,1)
    if flip ==0:
        return 'player1'
    else:
        return 'player2'   


# In[11]:


def space_check(board,position):
    return board[position]==''


# In[12]:


def full_board_check(board):
    for i in range(1-10):
        if space_check(board,i):
            return False
        return True
    


# In[13]:


def player_choice(board):
    position=0
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('player choose position:(1-9)'))
    return position


# In[14]:


def replay():
    choice=input('play again yes or no')
    return choice=='Yes'


# In[15]:


print('Welcome to Tic Tac Toe game!!!')
while True:
    theBoard=['']*10
    player1_marker,player2_marker=player_input()
    turn=first_choose()
    print(turn +' will go first play the game')
    play_game=input('ready to play yes? or no?')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn =='player1':
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('player 1 has win the game!!!')
                game_on=False
            
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('This game was Tie!!!')
                    break
                else:
                    turn='player2'
        else:
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('player 2 has win the game!!!')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('This game was Tie!!!')
                    break
                else:
                    turn='player1'
    if not replay():
        break

