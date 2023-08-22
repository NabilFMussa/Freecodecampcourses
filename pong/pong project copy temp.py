from cgitb import grey, text
from curses import BUTTON1_CLICKED
from distutils import command
from email.mime import image
from os import system
from pyexpat.errors import XML_ERROR_SUSPENDED
from random import random
from turtle import Screen, width
from typing import Counter
import pygame, sys
from logging import RootLogger, root
from tkinter import *
from PIL import ImageTk,Image
import random

pygame.init()

score_counter = 0
run = 0


def ballreset():



    global scoretimer, x_speed, y_speed
    currenttime = pygame.time.get_ticks()

    ball.center = (screen_width/2, screen_height/2)

    if currenttime-scoretimer < 2100:
        x_speed, y_speed = 0,0
    else:
        y_speed = 10*random.choice((1,-1))
        x_speed = 10* random.choice((1,-1))
        scoretimer = None

def endless():

    global x_speed, y_speed, screen_height, screen_width, ball, x_speed, y_speed, scoretimer
    if run == 0:
        pygame.init()
        clock = pygame.time.Clock()

 # this creates the screen 
        screen_width=1280
        screen_height=940
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("pygame pong")

 # colours
        red = (255,000,000)
        grey = (200, 200, 200)
        blue = (000, 000, 255)
        purple = (000, 000, 000)

        # objects in the game
        ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
        player = pygame.Rect(screen_width - 30, screen_height / 2 - 70, 10,140)
        player2 = pygame.Rect(30, screen_height/30, 10,5000)

        # ball speed
        x_speed = 10
        y_speed = 10
        #player speed
        player_speed = 0

        #score counter variables
        scorep1 = 0
        scorep2 = 0
        gamefont = pygame.font.Font("freesansbold.ttf", 64)


        scoretimer = None

        #game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                

                
                # player 1 input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        player_speed +=7
                    if event.key == pygame.K_UP:
                        player_speed -=7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        player_speed *= 0.00000000000000000000001
                    if event.key == pygame.K_UP:
                        player_speed *= 0.0000000000000000000000000000001
                

                        
            # players speed
            player.y += player_speed

            
            if player.top <=0 or player.bottom >= screen_height:
                player_speed *= -1

            
            # detects for collision with walls
            if ball.top <= 0 or ball.bottom >= screen_height:
                y_speed *= -1
            



            # iterates the score counter and resets the ball
            if ball.right >= screen_width:      
                scorep2 += 1
                scoretimer = pygame.time.get_ticks()
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-cowbell-sharp-hit-1743.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)

            if ball.left <= 0:      
                scorep1 += 1
                scoretimer = pygame.time.get_ticks()  
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-cowbell-sharp-hit-1743.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)
          
          
            # detects for collision with paddles
            if ball.colliderect(player) or ball.colliderect(player2):
                x_speed *= 1.10
                x_speed *= -1 
                player_speed *= 1.40
            if ball.colliderect(player):
                scorep1 += 1

                # adds sound effect after hit
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-game-ball-tap-2073.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)
            
            elif ball.colliderect(player) or ball.colliderect(player2):
                y_speed *= 1.10
                y_speed *= -1
                player_speed *= 1.40

            # adds sound effect after hit
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-game-ball-tap-2073.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0 )



            # this sets the balls speed(not collision)
            ball.x += x_speed
            ball.y += y_speed

            

            # creates the objects
            screen.fill("black")
            playertext = gamefont.render(f"{scorep1}", True, red)
            screen.blit(playertext,(880,470))
        

            if scorep2 == 1:
                wintext2 = gamefont.render(f"game over, your score is:",True, "white")
                scoretimer = 99999999999999999999999999999999999
                screen.blit(wintext2,(450,400))



            pygame.draw.rect(screen,red,player)
            pygame.draw.rect(screen,blue,player2)
            pygame.draw.ellipse(screen,"white",ball)
            pygame.draw.aaline(screen,"grey", (screen_width / 2, 0),(screen_width / 2, screen_height))
            
            if scoretimer:
                ballreset()

            pygame.display.flip()
            clock.tick(60)

def multiplayergame():

    global x_speed, y_speed, screen_height, screen_width, ball, x_speed, y_speed, scoretimer
    if run == 0:
        pygame.init()
        clock = pygame.time.Clock()

 # this creates the screen 
        screen_width=1280
        screen_height=940
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("pygame pong")

 # colours
        red = (255,000,000)
        grey = (200, 200, 200)
        blue = (000, 000, 255)
        purple = (000, 000, 000)

        # objects in the game
        ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
        player = pygame.Rect(screen_width - 30, screen_height / 2 - 70, 10,140)
        player2 = pygame.Rect(30, screen_height/2 - 70, 10,140)

        # ball speed
        x_speed = 10
        y_speed = 10
        #player speed

        player_speed = 0
        player2_speed = 0

        #score counter variables
        scorep1 = 0
        scorep2 = 0
        gamefont = pygame.font.Font("freesansbold.ttf", 64)


        scoretimer = None

        #game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                

                
                # player 1 input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        player_speed +=7
                    if event.key == pygame.K_UP:
                        player_speed -=7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        player_speed *= 0.00000000000000000000001
                    if event.key == pygame.K_UP:
                        player_speed *= 0.0000000000000000000000000000001
                
                # player 2 input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        player2_speed +=7
                    if event.key == pygame.K_w:
                        player2_speed -= 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        player2_speed *= 0.0000000000000000000000000001
                    if event.key == pygame.K_w:
                        player2_speed *= 0.0000000000000000000000000001
                        
            # players speed
            player2.y += player2_speed
            player.y += player_speed

            
            if player.top <=0 or player.bottom >= screen_height:
                player_speed *= -1
                
            if player2.top <=0 or player2.bottom >= screen_height:
                player2_speed *= -1
            
            # detects for collision with walls
            if ball.top <= 0 or ball.bottom >= screen_height:
                y_speed *= -1
            



            # iterates the score counter and resets the ball
            if ball.left <= 0:      
                scorep1 += 1
                scoretimer = pygame.time.get_ticks()  
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-cowbell-sharp-hit-1743.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)
 
            if ball.right >= screen_width:
                scorep2 += 1
                scoretimer = pygame.time.get_ticks()
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-cowbell-sharp-hit-1743.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)

          
            # detects for collision with paddles
            if ball.colliderect(player) or ball.colliderect(player2):
                x_speed *= 1.10
                x_speed *= -1 
                player2_speed *= 1.40
                player_speed *= 1.40
            # adds sound effect after hit
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-game-ball-tap-2073.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)
            
            
            elif ball.colliderect(player) or ball.colliderect(player2):
                y_speed *= 1.10
                y_speed *= -1
            # adds sound effect after hit
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-game-ball-tap-2073.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0 )
            # this sets the balls speed(not collision)
            ball.x += x_speed
            ball.y += y_speed

            

            # creates the objects
            screen.fill("black")
            playertext = gamefont.render(f"{scorep1}", True, red)
            screen.blit(playertext,(880,470))
            playertext = gamefont.render(f"{scorep2}", True, blue)
            screen.blit(playertext,(400,470))

            if scorep1 == 5:
                wintext1 = gamefont.render(f"player 1 wins", True, red)
                scoretimer = 9999999999999999999999999999999999
                screen.blit(wintext1,(640, 600))

            if scorep1 == 5:
                wintext2 = gamefont.render(f"game over", True, "white")
                screen.blit(wintext2,(500,250))

            if scorep2 == 5:                
                wintext2 = gamefont.render(f"game over", True, "white")
                screen.blit(wintext2,(500,250))

               
            if scorep2 == 5:
                wintext1 = gamefont.render(f"player 2 wins", True, blue)
                scoretimer = 99999999999999999999999999999999999
                screen.blit(wintext1,(640, 600))

            if scoretimer:
                scoretimer1 = gamefont.render(f"wait", True, "white")
                screen.blit(scoretimer1,(570,470))



            pygame.draw.rect(screen,red,player)
            pygame.draw.rect(screen,blue,player2)
            pygame.draw.ellipse(screen,"white",ball)
            pygame.draw.aaline(screen,"grey", (screen_width / 2, 0),(screen_width / 2, screen_height))
            
            if scoretimer:
                ballreset()

            
            if event.type == pygame.KEYUP:
                 if event.key==pygame.K_ESCAPE:
                   pygame.time.delay()
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_1:
                    pygame.time.delay()


            pygame.display.flip()
            clock.tick(60)

def exitmenu():
    root=Tk()
    root.title("exit screen")
    root.geometry("1920x1080")
    root.configure(bg='#000000')

    canvas = Canvas(root, width=1920, height=1080)
    canvas.create_text(100, 50, text="you have closed the game:", fill="black", font=('Helvetica 15 bold'))
    canvas.pack()

def hardmodesingleplayer():
    global x_speed, y_speed, screen_height, screen_width, ball, x_speed, y_speed, scoretimer
    if run == 0:
        pygame.init()
        clock = pygame.time.Clock()

 # this creates the screen 
        screen_width=1280
        screen_height=940
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("pygame pong")

 # colours
        red = (255,000,000)
        grey = (200, 200, 200)
        blue = (000, 000, 255)
        purple = (000, 000, 000)

        # objects in the game
        ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
        player = pygame.Rect(screen_width - 30, screen_height / 2 - 70, 10,140)
        ai = pygame.Rect(30, screen_height/2 - 70, 10,260)

        # ball speed
        x_speed = 10
        y_speed = 10
        #player speed
        player_speed = 0
        #ai speed
        ai_speed = 10

        # variables for score counter
        scorep1 = 0
        scorep2 = 0
        gamefont = pygame.font.Font("freesansbold.ttf", 64)

        scoretimer = None

        #game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                
                # player 1 input
                # player 1 input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        player_speed +=7
                    if event.key == pygame.K_UP:
                        player_speed -=7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        player_speed *= 0.00000000000000000000001
                    if event.key == pygame.K_UP:
                        player_speed *= 0.0000000000000000000000000000001

            
            if player.top <=0 or player.bottom >= screen_height:
                player_speed *= -1
            if ai.top <=0 or ai.bottom >= screen_height:
                ai_speed *= -1

            if ai.top < ball.y:
                ai.top += ai_speed
            if ai.bottom > ball.y:
                ai.bottom -= ai_speed

               

            # players speed
            player.y += player_speed

            if ball.top <= 0 or ball.bottom >= screen_height:
                y_speed *= -1
            
            # iterates score counter and resetes ball
            if ball.left <= 0:      
                scorep1 += 1
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-cowbell-sharp-hit-1743.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)
                scoretimer = pygame.time.get_ticks()

            if ball.right >= screen_width:
                scorep2 += 1
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-cowbell-sharp-hit-1743.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)
                scoretimer = pygame.time.get_ticks()

            # detects for collision with paddles
            if ball.colliderect(player) or ball.colliderect(ai):
                x_speed *= 1.10
                x_speed *= -1 
                
                
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-game-ball-tap-2073.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)
            elif ball.colliderect(player) or ball.colliderect(ai):
                y_speed *= 1.10
                y_speed *= -1
                pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-game-ball-tap-2073.wav")
                pygame.mixer.music.play(loops=1, start=0, fade_ms=0)
            
            # this sets the balls speed(not collision)
            ball.x += x_speed
            ball.y += y_speed


            # creates the objects
            screen.fill("black")
            playertext = gamefont.render(f"{scorep1}", True, red)
            screen.blit(playertext,(880,470))
            playertext = gamefont.render(f"{scorep2}", True, blue)
            screen.blit(playertext,(400,470))

            if scoretimer:
                scoretimer1 = gamefont.render(f"wait", True, "white")
                screen.blit(scoretimer1,(570,470))

            pygame.draw.rect(screen,red,player)
            pygame.draw.rect(screen,blue,ai)
            pygame.draw.ellipse(screen,"grey",ball)
            pygame.draw.aaline(screen,"grey", (screen_width / 2, 0),(screen_width / 2, screen_height))
            


            if scorep1 == 5:
                wintext1 = gamefont.render(f"player 1 wins", True, red)
                scoretimer = 9999999999999999999999999999999999
                screen.blit(wintext1,(640, 600))
               
            if scorep1 == 5:
                wintext2 = gamefont.render(f"game over", True, "white")
                screen.blit(wintext2,(500,250))
            if scorep2 == 5:
                wintext2 = gamefont.render(f"game over", True, "white")
                screen.blit(wintext2,(500,250))

            if scorep2 == 5:
                wintext1 = gamefont.render(f"player 2 wins", True, blue)
                scoretimer = 99999999999999999999999999999999999
                screen.blit(wintext1,(640, 600))

            if scoretimer:
                ballreset()

            pygame.display.flip()
            clock.tick(60)

def kill():
    root.destroy()
    return None

def menu2():
    root=Tk()
    root.title("mode selection")
    root.geometry("1920x1080")
    root.configure(bg='#000000')

   
    b = Button(root, text="singleplayer mode",padx=200, pady=50, command= lambda:[optionsmenusingleplayer(), kill()])
    b.configure(bg='grey')
    b.pack()
    
    b2 = Button(root, text=" multiplayer mode",padx=200, pady=50, command= lambda:[optionsmenumultiplayerplayer(), kill()])
    b2.configure(bg='grey')
    b2.pack(padx=100, pady=100)

    b3 = Button(root, text=" practise/ endless mode",padx=200, pady=50, command= lambda:[endlessmenu(), kill()])
    b3.configure(bg='grey')
    b3.pack(padx=100, pady=125)

def endlessmenu():
    root=Tk()
    root.geometry("1920x1080")
    root.configure(bg="#000000")

    
    b = Button(root, text="start game", padx=100, pady=50, command= lambda:[endless(), kill()])
    b.configure(bg="grey")
    b.pack()

    canvas = Canvas(root, width=1920, height=1080)
    canvas.create_text(100, 50, text="Instructions:", fill="black", font=('Helvetica 15 bold'))
    canvas.pack()

    canvas.create_text(650, 100, text="This is the practise mode just try your best not to let the ball past you:), press start game when you're ready to play", fill="black", font=('Helvetica 15'))
    canvas.pack()

    canvas.create_text(650, 200, text=" controls: UPARROW=up DOWNARROW=down" , fill="black", font=('Helvetica 15 bold'))
    canvas.pack()

def optionsmenumultiplayerplayer():
    root=Tk()
    root.geometry("1920x1080")
    root.configure(bg="#000000")

    
    b = Button(root, text="start game", padx=100, pady=50, command= lambda:[multiplayergame(), kill()])
    b.configure(bg="grey")
    b.pack()

    canvas = Canvas(root, width=1920, height=1080)
    canvas.create_text(100, 50, text="Instructions:", fill="black", font=('Helvetica 15 bold'))
    canvas.pack()

    canvas.create_text(650, 100, text="This is multiplayer mode you need another player to experience this properly, press start game when you're ready to play", fill="black", font=('Helvetica 15'))
    canvas.pack()

    canvas.create_text(650, 200, text=" for multiplayer player 1's controls: W=up S=down, player 2's controls: UPARROW=up DOWNARROW=down" , fill="black", font=('Helvetica 15 bold'))
    canvas.pack()

def optionsmenusingleplayer():



    root=Tk()
    root.geometry("1920x1080")
    root.configure(bg="#000000")

    
    b = Button(root, text="start game", padx=100, pady=50, command= lambda:[normalmodesingleplayer(), kill()])
    b.configure(bg="grey")
    b.pack()

    canvas = Canvas(root, width=1920, height=1080,)
    canvas.create_text(100, 50, text="Instructions:", fill="black", font=('Helvetica 15 bold'))
    canvas.pack()

    canvas.create_text(650, 100, text="This is the singleplayer mode enjoy:), press start game when you're ready to play", fill="black", font=('Helvetica 15'))
    canvas.pack()

    canvas.create_text(650, 200, text=" for your controls: UPARROW=up DOWNARROW=down" , fill="black", font=('Helvetica 15 bold'))
    canvas.pack()

root=Tk()
root.title("pong menu")
root.geometry("1920x1080")
root.configure(bg='#48bf91')

#importing images from directories
bg = PhotoImage(file="C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\pong.png")
start_btn = PhotoImage(file="C:\\Users\\youip\\oneDrive\\Desktop\\python\\pong\\start_btn.png")
exit_btn = PhotoImage(file="C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\exit_btn.png")
#background image canvas
canvas= Canvas(root, width= 1920, height= 1080, bg="#48bd91")
canvas.pack(fill="both", expand=True)
canvas.create_image(-150, 0, image=bg, anchor="nw")

pygame.mixer.music.load("C:\\Users\\youip\\OneDrive\\Desktop\\python\\pong\\mixkit-introduction-bell-sound-1150.wav")
pygame.mixer.music.play(loops=1, start=0, fade_ms=0)


b = Button(canvas, image=start_btn , padx=300, pady=100, command= lambda:[menu2(), kill()])
b.configure(bg='grey')
b.pack()

b2 = Button(canvas, image=exit_btn, padx=100, pady=50, command = kill)
b2.configure(bg='grey')
b2.pack(padx=100)




root.mainloop()

