# ╔═══════════════HI═════════════════╗
# ║    Hi user, welcome to my game   ║
# ╠═════════════CREATOR══════════════╣
# ║    Original code by nln.nolan    ║
# ╠══════════════DATE════════════════╣
# ║      Created on 24/10/2022       ║
# ╚══════════════════════════════════╝


# Import
from kandinsky import *
from turtle import *
from ion import *
from time import *

# colors
_colorBlack = (0,0,0)
_colorWhite = (255,255,255)
_colorGrey = (100,100,100)
_colorGrey20 = (80,80,80)
_colorGrey30 = (70,70,70)

_colorGold = (255,200,0)
_colorGreen = (20,200,70)
_colorRed = (200,20,20)


reset()
draw_string("Black  ",5,2)
fill_rect(70,4,13,13,'black')
draw_string("shift",260,2)
draw_string("Paint X",130,2)
showturtle()

#----------barre red----------#

# bar haut
fill_rect(0,0,350,2,_colorRed)

# bar bas
fill_rect(0,220,350,2,_colorRed)

# bar gauche
fill_rect(0,0,2,300,_colorRed)

# bar droite
fill_rect(318,0,2,300,_colorRed)

#----------End bars red----------


#----------Play----------
def Play():
  # Var
  pensizePlayer = 1
  speed = 3
  positionX = position()[0]
  positionY = position()[1]

  play = 1
  while play == 1:
#   to advance UP            
    if keydown(KEY_UP):
      setheading(90)
      forward(speed)
      positionY -= speed
      sleep(0.02)

#   to advance Down
    if keydown(KEY_DOWN):
      setheading(270)
      forward(speed)
      positionY += speed
      sleep(0.02)


#   to advance Left
    if keydown(KEY_LEFT):
      setheading(180)
      forward(speed)
      positionX -= speed
      sleep(0.02)


#   to advance Right
    if keydown(KEY_RIGHT):
      setheading(0)
      forward(speed)
      positionX += speed
      sleep(0.02)



#   Reset drawing
    if keydown(KEY_BACKSPACE):
      fill_rect(0,0,500,500,'gray')
      draw_string("! CLEAN UP !",100,100,(0,)*3,('red'))


      #----------bars red----------

      # bar haut
      fill_rect(0,0,350,5,('red'))

      # bar bas
      fill_rect(0,217,350,5,('red'))

      # bar gauche
      fill_rect(0,0,5,300,('red'))

      # bar droite
      fill_rect(315,0,5,300,('red'))

      #----------End bars red----------

      sleep(3)
      reset()
      reset()
      draw_string("Black  ",5,2)
      fill_rect(70,4,13,13,'black')
      draw_string("shift",260,2)
      draw_string("Paint X",130,2)
      showturtle()

      # bar haut
      fill_rect(0,0,350,2,_colorRed)

      # bar bas
      fill_rect(0,220,350,2,_colorRed)

      # bar gauche
      fill_rect(0,0,2,300,_colorRed)

      # bar droite
      fill_rect(318,0,2,300,_colorRed)

      #----------End bars red----------


#   Magnify pen size -
    if keydown(KEY_MINUS):
      pensizePlayer -= 1
      if pensizePlayer == 0:
        pensizePlayer += 1
      pensize(pensizePlayer)
      sleep(0.1)

#   Magnify pen size +
    if keydown(KEY_PLUS):
      pensizePlayer += 1
      pensize(pensizePlayer)
      sleep(0.1)


#   Do not write
    if keydown(KEY_MULTIPLICATION):
      pendown()


#   To write
    if keydown(KEY_DIVISION):
      penup()

#   Border
    positionX = position()[0]
    positionY = position()[1]

    if positionX <= -156:
      goto(positionX+speed,positionY)
      positionX += speed
    
    if positionX >= 156:
      goto(positionX-speed,positionY)
      positionX -= speed

    if positionY >= 90:
      goto(positionX,positionY-speed)
      positionY -= speed

    if positionY <= -106:
      goto(positionX,positionY+speed)
      positionY += speed

#   help page
    if keydown(KEY_SHIFT):
      play = 0
      HelpSheet()

      
#   colors
    if keydown(KEY_ZERO):
      color('black')
      draw_string("Black  ",5,2)
      fill_rect(70,4,13,13,'black')      


    if keydown(KEY_ONE):
      color('blue')
      draw_string("Blue  ",5,2)
      fill_rect(70,4,13,13,'blue')      
      

    if keydown(KEY_TWO):
      color('red')
      draw_string("Red  ",5,2)
      fill_rect(70,4,13,13,'red')      


    if keydown(KEY_THREE):
      color('green')
      draw_string("Green  ",5,2)
      fill_rect(70,4,13,13,'green')      


    if keydown(KEY_FOUR):
      color('yellow')
      draw_string("Yellow  ",5,2)
      fill_rect(70,4,13,13,'yellow')      

      
    if keydown(KEY_FIVE):
      color('brown')
      draw_string("Brown  ",5,2)
      fill_rect(70,4,13,13,'brown')      


    if keydown(KEY_SIX):
      color('pink')
      draw_string("Pink  ",5,2)
      fill_rect(70,4,13,13,'pink')      


    if keydown(KEY_SEVEN):
      color('orange')
      draw_string("Orange  ",5,2)
      fill_rect(70,4,13,13,'orange')      


    if keydown(KEY_EIGHT):
      color('purple')
      draw_string("Purple  ",5,2)
      fill_rect(70,4,13,13,'purple')
      
    
    if keydown(KEY_NINE):
      color('gray')
      draw_string("Gray  ",5,2)
      fill_rect(70,4,13,13,'gray')


#----------Help Sheet----------
def HelpSheet():
  reset()
        
  fill_rect(0,0,500,500,_colorGrey)

  #----------Bars Green----------#

  # bar haut
  fill_rect(0,0,350,5,_colorGreen)

  # bar bas
  fill_rect(0,217,350,5,_colorGreen)

  # bar gauche
  fill_rect(0,0,5,300,_colorGreen)

  # bar droite
  fill_rect(315,0,5,300,_colorGreen)

  #----------End Bars Green----------#

  draw_string("Help Sheet",110,10,_colorWhite, _colorGrey30)

  draw_string("alpha",260,10,_colorWhite, _colorGrey30)

  draw_string("-------------",95,30,_colorWhite, _colorGrey)

  draw_string("Colors :",15,60,_colorWhite, _colorGrey20)

  draw_string("0123456789",15,80,_colorWhite, _colorGrey)

  draw_string("Movement :",155,60,_colorWhite, _colorGrey20)

  draw_string("Direction Arrow",155,80,_colorWhite, _colorGrey)

  draw_string("Pen size",15,120,_colorWhite, _colorGrey20)

  draw_string("+ -",15,140,_colorWhite, _colorGrey)

  draw_string("Pen Show/",155,120,_colorWhite, _colorGrey20)
  draw_string("Hidden :",155,140,_colorWhite, _colorGrey20)
  
  draw_string("% x",155,160,_colorWhite, _colorGrey)


  draw_string("By nln.nolan",10,195,_colorWhite, _colorGrey)

  sleep(0.5)

  helpSheet = 1
  while helpSheet == 1:
    # Go Back
    if keydown(KEY_ALPHA):
      reset()
      draw_string("Black  ",5,2)
      fill_rect(70,4,13,13,'black')
      draw_string("shift",260,2)
      draw_string("Paint X",130,2)
      showturtle()

      #----------Bars Red----------

      # bar haut
      fill_rect(0,0,350,2,_colorRed)

      # bar bas
      fill_rect(0,220,350,2,_colorRed)

      # bar gauche
      fill_rect(0,0,2,300,_colorRed)

      # bar droite
      fill_rect(318,0,2,300,_colorRed)

      #----------End Bars Red----------

      sleep(0.5)
      helpSheet = 0
      Play()


Play()
