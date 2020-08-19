# Setting Up Python
import math
import pygame
import random
from pygame import mixer

# Game Configuration
pygame.init()
screen = pygame.display.set_mode((800, 600))  # This is screen command and the int value is the size of the Game window
background = pygame.image.load('background.jpg')  # This will Load an Background image
pygame.display.set_caption("Space Invaders")  # This will Set An Caption or Title For Game
icon = pygame.image.load('space-invaders.png')  # This Will Set An Icon To The Game
pygame.display.set_icon(icon)  # This is an also icon command but this will implement this into the game
clock = pygame.time.Clock()  # This is FPS command This will apply a limit to your game fps limit.

# MUSIC
newsoung = mixer.music.load('Bakcground-music.mp3')
mixer.music.play(-1)
# Player Configuration
PlayerIMG = pygame.image.load('new.png')  # This is Will load An Player Image.
PlayerX = 370  # This is An X coordinate of player this will set the player into an Game Width.
PlayerY = 480  # This is An Y Coordinate Of Player This Will Set The Player Int An Game Height.
PlayerX_Change = 0  # This variable for player moment when in while loop we move the player the value save in it

# Enemy Configuration
EnemyIMG = []
EnemyX = []
EnemyY = []
EnemyX_Change = []
EnemyY_Change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    EnemyIMG.append(pygame.image.load('cyclops.png'))  # This will load an player image.
    EnemyX.append(random.randint(0, 800))  # This command will randomly place an enemy on X axis means on width.
    EnemyY.append(random.randint(50, 150))  # This command will randomly place an enemy on Y axis means on height.
    EnemyX_Change.append(5)  # This are the constant value of Enemy.
    EnemyY_Change.append(15.5)

# Bullet Configuration
BulletIMG = pygame.image.load('bullet (2).png')  # This will load or apply the bullet image.
BulletX = 0  # This is X-axis bullet position we wont use this because we only want our bullet to go upward direction in Y-axis.
BulletY = 480  # This will set the limit to Y-axis for bullet so it does not go away from screen.
BulletX_Change = 0
BulletY_Change = 20
# This is an speed of an bullet
Bullet_State = "ready"  # This is string when it ready it means bullet in stationary form but when its fire its moves away.

# score
Score_Value = 0
font = pygame.font.Font('freesansbold.ttf', 16) # This is for font printing or rendering.
textX = 50 # This are the font positions
textY = 550

# Game Over text
game_font = pygame.font.Font('freesansbold.ttf', 40)
game_fontX = 0
game_fontY = 0

# Fonts
Author_Name = pygame.font.Font('freesansbold.ttf', 8)
Author_NameX = 66
Author_NameY = 565

# Functions
def Author_Name_On_Side(x,y):
    A_name = Author_Name.render("Created By HarrisK ", True, (255,255,255))
    screen.blit(A_name,(x, y))

def game_over_text():
    g_over = game_font.render("GAME OVER ", True, (255, 255, 255)) # The value in bracket are RGB.
    screen.blit(g_over,(200, 250)) # This for printing on game screen.


def show_text(x, y):
    score = font.render("Total Score : " + str(Score_Value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def Player(x, y):  # This for an player image function for drawing the image.
    screen.blit(PlayerIMG, (x, y))


def Enemy(x, y, i):  # This for an enemy image function for drawing the image.
    screen.blit(EnemyIMG[i], (x, y))


def Fire_Bullet(x, y):  # This is an Bullet FX in this fx we set the position of bullet where it will be fire.
    global Bullet_State
    Bullet_State = "fire"
    screen.blit(BulletIMG, (x + 16, y + 10))


def is_Collison(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 100:
        print(distance)


running = True  # This is an Boolean Variable it help us to open and close The Game

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT means Close button on your top right corner.
            running = False  # when you set the variable into an FALSE this will close the program when you click on closse.

        # Event or Press Commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                PlayerX_Change = 10
            if event.key == pygame.K_LEFT:
                PlayerX_Change = -10
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
                if Bullet_State is "ready":
                    BulletX = PlayerX
                    Fire_Bullet(PlayerX, BulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                PlayerX_Change = 0.0

    # Player Configuration when it will goes less then 0 it will imediately
    # turns into 0 so player wont goes away from screen same the 736.
    # 0 is for left corner and 736 for right one.
    PlayerX += PlayerX_Change
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    # Enemy Configuration When Enemy Hit The Left One Corner Means It Will Try To
    # Goes Beyond Or less Than Zero Then It Will Turn into Y-axis of 2
    # means it will comedown by the value of 2 in Y-axis.
    for i in range(num_of_enemies):
        # Game Over
        # The Value i in list are for multiplie
        # value on the top i created the for loops for multiple enemies so whenever we want
        # to change the amount of enemies we will just increase the numbers.
        if EnemyY[i] > 400:
            for j in range(num_of_enemies):
                EnemyY[i] = 2000
            game_over_text()
            break
        EnemyX[i] += EnemyX_Change[i] # its means it will add one value to enemy everytime when its the wall.
        if EnemyX[i] <= 0:
            EnemyX_Change[i] = 10
            EnemyY[i] += EnemyY_Change[i]
        elif EnemyX[i] >= 736:
            EnemyX_Change[i] = -10
            EnemyY[i] += EnemyY_Change[i]
        collision = is_Collison(EnemyX[i], EnemyY[i], BulletX, BulletY) # those are collision fx that i created on top.
        if collision:
            collision_sound = mixer.Sound('explosion.wav') # this is for sound of enemy death.
            collision_sound.play()
            BulletY = 480
            Bullet_State = "ready"
            Score_Value += 1
            EnemyX[i] = random.randint(0, 800)
            EnemyX_Change[i] = 12
            EnemyX[i] += EnemyX_Change[i]
            EnemyY[i] = random.randint(50, 150)

        Enemy(EnemyX[i], EnemyY[i], i)

    # Bullet Configuration in first variable when player fire the bullet bullet will goes into
    # upward direction so when it complete the y-axis means when it reach the maximum value of y-axis 0
    # it will start back into 736 means bottom where player will be place.
    # if second if statement when player command bullet ready to fire it will minus.
    # the value of bullet into bullet_change means it will goes only into upward direction.
    if BulletY <= 0:
        BulletY = 400
        Bullet_State = "ready"
    if Bullet_State is "fire":
        Fire_Bullet(BulletX, BulletY)
        BulletY -= BulletY_Change

    Player(PlayerX, PlayerY)

    Author_Name_On_Side(Author_NameX, Author_NameY)
    show_text(textX, textY) # this is for the showing the text on screen
    clock.tick(60)  # Here 60 refers to 60 fps.
    pygame.display.update()  # This will keep the screen updated every loop.
