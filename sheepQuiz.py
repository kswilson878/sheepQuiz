

from logging.config import stopListening
import random
import sys
import pygame
from pygame.locals import *
pygame.init()
import os
window_width = 1000
window_height = 500
score = 0
# sets the questions, answers, and options up for the quiz

questions = [
        '''What are William & Mary's school colors? ''',
        "What is our mascot?",
        "When was the school founded? ",
        "William & Mary is the second school chronologically built in the United States. What was the first?",
        "We have the first intercollegiate fraternity in the country. What is the name of it?",
        "How many semesters does a student at William and Mary have to complete their degree within?",
        "Which of the following options were we NOT the first to offer a degree in?",
        "What is our student-to-faculty ratio?",
        "Which is not a name of a dorm at william and mary in the Botetourt Complex??",
        "Which state is William & Mary in?",
        "True or False: William & Mary was the first institution of higher education to have a law school",
        "Which of these buildings is the oldest academic building in continuous use in the US?",
        "Which of these is not a famous alum of William & Mary?",
        "Which of these is not in the W&M Triathlon?",
        "What is the nickname for William & Mary athletic teams?",
        "Which part of the Coll Curriculum is study abroad typically classified under?"
        ]
option1 =["blue and black","griffin","1770", "Yale", "Delta Gamma", "10", "modern languages", "10 to 1", "Gooch ", "The United States of America", "True", "The Wren Building", "Henry Clay", "streaking the sunken gardens", "The Tribe", "Coll 150"
]
option2=["green and gold", "eagle", 
'1645 ', "Harvard", "Phi Beta Kappa", "8", "political economy","12 to 1", "Stith", "Maryland", "False", "Chancellor's Hall", "Glenn Close", "ringing the wren building bell", "The William's and The Mary's","Coll 200"
]
option3=[
"green and orange","bullfrog", "1688", "University of Pennsylvania ", "Beta Beta Beta", "12", "modern history","20 to 3", "Nicholson", "Virginia", "", "James Blair Hall", "Stephen Colbert", "jumping the governor's palace wall","The Presidentials", "Coll 300"
]
option4=["blue and yellow","lion","1693","None of the above", "Phi Sigma Pi", "9", "religious studies", "5 to 1" ,"Spotswood", "D.C.", "", "Jefferson Hall", "Jon Stewart", "swimming in the crim dell", "The Colonials", "Coll 400"
]
question_answers = [
        "b","a","d", "b", "b", "a", "d", "b", "b", "c", "a", "a","c", "b","a", "c"
    ]
       
window = pygame.display.set_mode((window_width, window_height))
game_images = {}
framepersecond = 32

# decides on a random student picture to use from the choices
studentRandom = random.randint(1,3)
if (studentRandom==1):
    student_image = 'wmStudent.PNG'
if (studentRandom==2):
    student_image = 'student2.PNG'
if (studentRandom==3):
    student_image = 'student3.PNG'
horizontal = 230
horizontalStudent = 30
vertical = 400
sheepImage = 'sheep 2.png'

#runs the quiz by starting the info screen and setting the horizontal and vertical aspects for the sheep
def run_quiz():
    horizontal = 230
    vertical = int(window_width/2)
    
    infoScreen()

# this function sets up the title / info screen for the game. once the user is ready to start, it 
# generates a random question mumber from the list using the generate question function and then displays 
# that question on the question screen.
def infoScreen():
    X = window_width
    Y = window_height
    white = (255, 255, 255)
    black = (23,23,23)
    font = pygame.font.Font('freesansbold.ttf', 35)
    text = font.render("THE GREAT SWEM SHEEP ESCAPE QUIZ!", True, white)
    textRect = text.get_rect()
    textRect.center = (400,  100)
    font = pygame.font.Font('freesansbold.ttf', 15)
    text3 = font.render("In this quiz game, you will play as one of the kidnapped swem sheep", True, white)
    textRect3 = text3.get_rect()
    textRect3.center = (700,  200)
    text4 = font.render("as it tries to escape its captors. answer questions correct", True, white)
    textRect4 = text4.get_rect()
    textRect4.center = (700,  220)
    text5= font.render("and move across the sunken gardens but get it wrong ", True, white)
    textRect5 = text5.get_rect()
    textRect5.center = (700,  240)
    text6= font.render("and your captor moves towards you!  ", True, white)
    textRect6= text6.get_rect()
    textRect6.center = (700,  260)
    font = pygame.font.Font('freesansbold.ttf', 20)
    playButton = font.render("PLAY GAME", True, black, white)
    textRect2 = playButton.get_rect()
    textRect2.center = (700,  400)
    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Welcome to the Game! Please Help the Sheep!')
    sheepImageInfo= 'yellowSheep.PNG'
    game_images['sheepInfo'] = pygame.image.load(
    sheepImageInfo).convert_alpha()
    while True:
        window.blit(game_images['sheepInfo'], (200, 200))
        display_surface.blit(text, textRect)
        display_surface.blit(playButton, textRect2)
        display_surface.blit(text3, textRect3)
        display_surface.blit(text4, textRect4)
        display_surface.blit(text5, textRect5)
        display_surface.blit(text6, textRect6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if textRect2.collidepoint(mousePos):
                    questionScreen(generateQuestion(), score, horizontal,horizontalStudent)
            if (event.type == KEYDOWN and event.key == K_SPACE):
                questionScreen(generateQuestion(), score, horizontal,horizontalStudent)
        pygame.display.update()
#this function decides a random question to ask then returns the number
def generateQuestion():
    size = int(questions.__len__())
    questionNumber = random.randint(0,size-1)
    return questionNumber

#this function controls the screen every time the user is answering a question.
# it displays the question, as well as the sheep and its pursuer on the sunken gardens
# once the user clicks on an answer, it moves to the answer screen
def questionScreen(questionNum, score, horizontal, horizontalStudent):
    isGameOver(horizontal, horizontalStudent)
    background = (64,75,93)
    white = (255, 255, 255)
    black = (23,23,23)
    bg = pygame.image.load("sunken.jpg")

    X = window_width
    Y = window_height
    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Question')
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(questions[questionNum], True, white, black)
    textRect = text.get_rect()
    textRect.center = (X // 2,  Y //2-80)
    text2= font.render(option1[questionNum], True, white, black)
    textRect2 = text2.get_rect()
    textRect2.center = (X // 2,  Y //2-50)
    text3= font.render(option2[questionNum], True, white, black)
    textRect3 = text3.get_rect()
    textRect3.center = (X // 2,  Y //2-20)
    text4 = font.render(option3[questionNum], True, white, black)
    textRect4 = text4.get_rect()
    textRect4.center = (X // 2,  Y //2+10)
    text5 = font.render(option4[questionNum], True, white, black)
    textRect5 = text5.get_rect()
    textRect5.center = (X // 2,  Y //2+40)
    while True:

        display_surface.blit(bg, (0, 0))

        game_images['sheep'] = pygame.image.load(
        sheepImage).convert_alpha()
        game_images['student'] = pygame.image.load(
        student_image).convert_alpha()
        window.blit(game_images['sheep'], (horizontal, vertical))
        window.blit(game_images['student'], (horizontalStudent, vertical))
        display_surface.blit(text, textRect)
        display_surface.blit(text2, textRect2)
        display_surface.blit(text3, textRect3)
        display_surface.blit(text4, textRect4)
        display_surface.blit(text5, textRect5)
        inputAnswer=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if textRect2.collidepoint(mousePos):
                    inputAnswer = "a"
                if textRect3.collidepoint(mousePos):
                    inputAnswer = "b"
                if textRect4.collidepoint(mousePos):
                    inputAnswer = "c"
                if textRect5.collidepoint(mousePos):
                    inputAnswer = "d"        
            pygame.display.update()
        if(inputAnswer!=0):
            answer = inputAnswer
            if answer == question_answers[questionNum]:
                answerScreen(questionNum, True, score, horizontal, horizontalStudent)
            else:
                answerScreen(questionNum, False,score, horizontal, horizontalStudent)
            
# this function controls the answer screen. if the user answered correctly, it 
# removes that question and its related options and answer from the list and 
# then moves the sheep. it the user answers wrong, it moves the student
def answerScreen(questionNum, correct, score, horizontal, horizontalStudent):
    isGameOver(horizontal,horizontalStudent)
    stopRepeats= 0

    if (correct==True):
        score= score+1
        del questions[questionNum]
        del question_answers[questionNum]
        del option1[questionNum]
        del option2[questionNum]
        del option3[questionNum]        
        del option4[questionNum]
        white = (255, 255, 255)
        black = (23,23,23)
        bg = pygame.image.load("sunken.jpg")

        X = window_width
        Y = window_height
        display_surface = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('Question Correct!')
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render("Yay, that was correct! Your score is now " +str(score) , True, white, black)
        textRect = text.get_rect()
        textRect.center = (X // 2,  Y //2-80)
        text2 = font.render("Please press the spacebar to continue helping the sheep!!!" , True, white, black)
        textRect2 = text.get_rect()
        textRect2.center = (X // 2,  Y //2-40)
    
        while True:
            display_surface.blit(bg, (0, 0))
            game_images['sheep'] = pygame.image.load(
            sheepImage).convert_alpha()
            game_images['student'] = pygame.image.load(
            student_image).convert_alpha()
            if (stopRepeats==0):
                horizontal= horizontal + 100
                stopRepeats=1
            window.blit(game_images['sheep'], (horizontal, vertical))
            window.blit(game_images['student'], (horizontalStudent, vertical))
            display_surface.blit(text, textRect)
            display_surface.blit(text2, textRect2)

            inputAnswer=0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    quit()
                if (event.type == KEYDOWN and \
                                          event.key == K_SPACE):
                                        
                    questionScreen(generateQuestion(), score, horizontal, horizontalStudent)
            pygame.display.update()
    if (correct==False):
        white = (255, 255, 255)
        black = (23,23,23)
        bg = pygame.image.load("sunken.jpg")

        X = window_width
        Y = window_height
        display_surface = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('Question Wrong!')
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Aw, that was incorrect! Your score is still " +str(score) , True, white, black)
        textRect = text.get_rect()
        textRect.center = (X // 2,  Y //2-80)
        font = pygame.font.Font('freesansbold.ttf', 27)

        text2 = font.render("Please press the spacebar to continue helping the sheep!!!" , True, white, black)
        textRect2 = text.get_rect()
        textRect2.center = (X // 2,  Y //2-40)
    
        while True:

            display_surface.blit(bg, (0, 0))

            game_images['sheep'] = pygame.image.load(
            sheepImage).convert_alpha()
            game_images['student'] = pygame.image.load(
            student_image).convert_alpha()
            if (stopRepeats==0):
                horizontalStudent = horizontalStudent + 100
                stopRepeats=1
            window.blit(game_images['sheep'], (horizontal, vertical))
            window.blit(game_images['student'], (horizontalStudent, vertical))
            display_surface.blit(text, textRect)
            display_surface.blit(text2, textRect2)

            inputAnswer=0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if (event.type == KEYDOWN and \
                                          event.key == K_SPACE):
                    
                    questionScreen(generateQuestion(), score, horizontal,horizontalStudent)

            pygame.display.update()
# this function is called multiple times to determine if the game is over.
# if the user has won and escaped the sunken gardens, it calls the win function
# if the student caught up to the sheep, it calls the lose function.
def isGameOver(horizontal,horizontalStudent):
    if horizontal >= window_width or horizontal <= horizontalStudent:
        if(horizontal>window_width):
            win()
        if (horizontal<=horizontalStudent):
            lose()
        return True
    return False
  
  
# this controls the winning screen, in which the sheep has successfully made
# it to the library.
def win():
    green =(38,107,0)
    gold = (255,225,0)
    bg = pygame.image.load("swem.jpg")

    X = 800
    Y =500
    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('YOU WON!')
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render('CONGRATS YOU WON!', True, green, gold)
    textRect = text.get_rect()
    textRect.center = (200, 100)
    text2 = font.render('THE YELLOW SHEEP MADE IT BACK TO SWEM!', True, green, gold)
    textRect2 = text2.get_rect()
    textRect2.center = (350, 200)
    while True:
 
        window.blit(bg, (0, 0))
        window.blit(game_images['sheep'], (400, 400))
        display_surface.blit(text, textRect)
        display_surface.blit(text2, textRect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
#this controls the losing screen, in which the sheep remains captured.
def lose():
    black = (23,23,23)
    red = (253,32,0)
    bg = pygame.image.load("studentsLose.jpg")

    X = 700
    Y = 500
    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('YOU LOST! :(')
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(" YOU LOST!" , True, red, black)
    textRect = text.get_rect()
    textRect.center = (300,390)
    font = pygame.font.Font('freesansbold.ttf', 20)

    text2= font.render(" THE YELLOW SHEEP WERE CAPTURED " , True, red, black)
    textRect2 = text2.get_rect()
    textRect2.center = (300,430)
    text3 =font.render("BY THE WILLIAM & MARY STUDENTS :(( " , True, red, black)
    textRect3 = text3.get_rect()
    textRect3.center = (300,450)
    while True:
        window.blit(bg, (0, 0))

        window.blit(game_images['sheep'], (150, 20))
        display_surface.blit(text, textRect)
        display_surface.blit(text2, textRect2)
        display_surface.blit(text3, textRect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()



  
# this is the main function where the program starts. it calls the function to run the game.
if __name__ == "__main__":
  
    pygame.init()
    run_quiz()

  