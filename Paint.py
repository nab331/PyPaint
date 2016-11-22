from GameData import *


class MyButton():
    def __init__( self , image , x , y ,  size , grow , name = 'NONE' , detail = ['Description'] , colour = coolblue , function = None):       

        self.file = pygame.image.load(image)
        self.size = size
        self.grow = grow
        self.colour = colour
        self.name = name
        self.detail = detail
        
        self.image = pygame.transform.scale(pygame.image.load(image),(self.size,self.size))
        self.image.set_alpha(25)


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

        self.function = function
        self.beingClicked = False

        

    def displayButton(self):
        self.mouse= pygame.mouse.get_pos()
        self.clicked= pygame.mouse.get_pressed()
        
        


        if self.rect.x<self.mouse[0]<self.rect.x+self.size  and  self.rect.y < self.mouse[1] < self.rect.y+self.size :           
            
            self.image = pygame.transform.scale(self.file,(self.grow,self.grow))
            window.blit(self.image,(self.rect.x - (self.grow - self.size)*0.5 ,self.rect.y  - (self.grow - self.size)*0.5 ))
            
            message_to_screen( window , self.name , self.colour , 30  , 733 , 30 , True) #The Title

            output.setAlpha( output.infobox , 200) #MAKES THE INFO BOX DARKER
            
##            for i in range(len(self.detail)):
##                message_to_screen( window , self.detail[i] , self.colour , 25  , 657 + i*25 ) #The Info

            
            
            
            if self.clicked==(1,0,0):
                paintData.selected = self   
                
                self.beingClicked = True

            else:
                self.beingClicked = False


                
                
        else:
            
            self.image = pygame.transform.scale(self.file,(self.size,self.size)) #Change image to the original size
            window.blit(self.image,(self.rect.x,self.rect.y)) #Display the icon
            
            output.setAlpha( output.infobox , output.ialpha) #makes the info box to the original colour


class ColourButton(): #Buttons
    def __init__( self , colour , x , y ,  size , grow , name ):       


        self.size = size
        self.grow = grow
        self.colour = colour
        self.name = name

        self.box = pygame.Surface((self.size,self.size))           
        self.box.fill( self.colour )

        self.rect = self.box.get_rect()
        self.rect.x = x
        self.rect.y = y
        

        self.beingClicked = False

        

    def displayColour(self):
        self.mouse= pygame.mouse.get_pos()
        self.clicked= pygame.mouse.get_pressed()
        
        


        if self.rect.x<self.mouse[0]<self.rect.x+self.size  and  self.rect.y < self.mouse[1] < self.rect.y+self.size :           

            
            self.box = pygame.Surface((self.grow,self.grow))
            self.box.fill( self.colour )            

   
            window.blit( self.box, (self.rect.x - (self.grow - self.size)*0.5 ,self.rect.y  - (self.grow - self.size)*0.5 ) )            
            message_to_screen( window , self.name , self.colour , 30  , 733 , 30 , True) #The Title

           
            
            
            if self.clicked==(1,0,0):
                paintData.primecolour = self.colour
                paintData.b_darkness = 0
                
                paintData.setColour()
                
                self.beingClicked = True

            else:
                self.beingClicked = False


                
                
        else:

            
            self.box = pygame.Surface((self.size,self.size))    #Change image to the original size
            self.box.fill( self.colour )


            window.blit(self.box ,(self.rect.x,self.rect.y)) #Display the icon



class Output:
    def __init__(self , bgcolour , toolspace ):
        self.bgcolour = bgcolour
        self.toolspace = toolspace
        self.bordercolour = tupadd(bgcolour , 10)

        self.border = pygame.Surface(( window_width -10 - 269 , window_height-20))              
        self.border.fill( self.bordercolour )
        
        self.box = pygame.Surface((250,window_height-20)) #menuBox
        self.setAlpha( self.box , 80 )                
        self.box.fill( self.toolspace )

        self.box2 = pygame.Surface((250,window_height-20)) #Used as background for the menu box            
        self.box2.fill( self.bgcolour )


        self.ialpha = 150 #For the infobox
        self.infobox = pygame.Surface( (250 - 20 ,100-50) ) 
        self.setAlpha( self.infobox , self.ialpha )                
        self.infobox.fill( self.bgcolour )

        
    

    def blitBackground(self):
        window.fill(self.bgcolour)
        window.blit(self.border, (269 ,10))


    def blitMenu( self ):
        window.blit(self.box2, (10,10))
        
        window.blit(self.box, (10,10))
        window.blit(self.infobox, (20, window_height - 50 - 20))
        


    def setAlpha( self , rectangle , alphaVal = 100 ):
        rectangle.set_alpha(alphaVal)

class Painting: #THE OUTPUT
    
    def __init__( self ):
        self.draw_list = []
        self.i = -1 #used for deletion
        self.cleaned_list = []


        self.undo_mode = False
        
    def get_position( self ):
        self.mouse = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed()
        if self.clicked==(1,0,0):
            #print str(self.mouse[0]) , " , "+str(self.mouse[1])
    
            if 290<[self.mouse][0][0]<967 and 25<[self.mouse][0][1]<763: #Inisde the border
                mouseCOD = [self.mouse]
                self.draw_list.append( [self.mouse , paintData.colour , int(paintData.b_size) ] )
                self.blit( mouseCOD )

        if self.undo_mode == True:
            self.undo()  


    def blit( self , cood ):

        
        pygame.draw.circle( window , paintData.colour , cood[0] , int(paintData.b_size))


    def undo(self):

        if len(self.draw_list)>0:
            self.draw_list.pop()


         
        output.blitBackground()
        output.blitMenu() 
        
        for i in self.draw_list:
            pygame.draw.circle( window , i[1] , i[0] , i[2])
            
        

    def cleanlist( self ):
        self.cleaned_list = []

        #Removing Duplicates
        for i in self.draw_list:
            if i not in self.cleaned_list:          
            
                self.cleaned_list.append(i)

    
        print len(self.draw_list)
        print len( self.cleaned_list )
    
class PaintData:
    def __init__( self ):
        self.selected = None
        self.b_size = 10
        self.b_darkness = 0
    
        self.primecolour = red
        self.setColour()
        



    def performFunctions( self ):
        self.blitDefault()


        if self.selected!=None:
            if self.selected.beingClicked == True:
                
                if self.selected.name == 'Brush Size +' and self.selected.name != 'Pencil':
                    self.b_size+=0.1

                elif self.selected.name == 'Brush Size -' and self.selected.name != 'Pencil':
                    if self.b_size>0:
                        self.b_size-=0.1

                if self.selected.name == 'Lighten Brush':
                    if self.b_darkness < 200:
                        self.b_darkness+=1
                        self.setColour()

                elif self.selected.name == 'Darken Brush':
                    if self.b_darkness > -200:
                        self.b_darkness-=1
                        self.setColour()
                        
                elif self.selected.name == 'Pencil':
                    self.colour = silver
                    self.b_size = 2

                if self.selected.name == 'Brush':
                    self.colour = red
                    self.b_size = 10

                elif self.selected.name == 'Eraser':
                    self.colour = output.bordercolour


                elif self.selected.name == 'Clear':

                    self.b_size = 10
                    output.blitBackground()
                    painting.draw_list = []
                    
    def setColour(self):
        self.colour = tupadd( self.primecolour , int(self.b_darkness) )
                    
    def blitDefault(self): #Blitting stuff like brushsize

        message_to_screen( window , "Shade : "+str(int(self.b_darkness*-1)) , coolyellow , 80  , 455 , 20 ) #BrushDarkness
        message_to_screen( window , "Size : "+str(int(self.b_size)) , coolgreen , 80  , 515 , 20 ) #BrushSize

        pygame.draw.circle( window , black , (135  , 630) , int(paintData.b_size)+2 ) #Outline
        pygame.draw.circle( window , paintData.colour , (135  , 630) , int(paintData.b_size)) #How the brushlooks
        
        
        
    

            
            
        
    





output = Output( (24, 39, 53)  , coolblue ) #The Background
painting = Painting()
paintData = PaintData()

brush = MyButton('Resources/brush.png' , 25  , 33 , 100 , 120  , 'Brush' , [ '*PAINT COLOURS*' , ' ' , 'Current Size : '] , coolred )
pencil = MyButton('Resources/color_pencil.png' , 130  , 39 , 100 , 120  , 'Pencil' , [ '*DRAW*' , ' ' ,  'Current Size : '] , carrot )
eraser = MyButton('Resources/eraser.png' , 30  , 176 , 100 , 120  , 'Eraser' , [ '*CLEARS SELECTED*' , ' ' ,  'Current Size : '] , coolblue )
rbin = MyButton('Resources//bin.png' , 135  , 176 , 100 , 120  , 'Clear' , [ '*CLEARS ALL*' , ' ' ,  'Current Size : '] , cloud )
#colour = MyButton('Resources/colour.png' , 82  , 320 , 100 , 120  , 'Colour' , [ '*CLEARS ALL*' , ' ' ,  'Current Size : '] , cloud )

bplus = MyButton('Resources/plus.png' , 31  , 510 , 35 , 45 , 'Brush Size +' , [ '**INCREASE SIZE**' , 'Current Size : '] , coolred )
bminus = MyButton('Resources/minus.png' , 200  , 510 , 35 , 50 , 'Brush Size -' , [ '**DECREASE SIZE**' , 'Current Size : '] , coolblue )

cplus = MyButton('Resources/plus.png' , 31  , 450 , 35 , 45 , 'Darken Brush' , [ '**INCREASE SIZE**' , 'Current Size : '] , coolred )
cminus = MyButton('Resources/minus.png' , 200  , 450 , 35 , 50 , 'Lighten Brush' , [ '**DECREASE SIZE**' , 'Current Size : '] , coolblue )

black_b = ColourButton( black , 150  , 330 ,  40 , 50 , 'Black' )
white_b = ColourButton( white , 190  , 330 ,  40 , 50 , 'White' )

red_b = ColourButton( red , 50  , 330 ,  20 , 25 , 'Red' )
cred_b = ColourButton( coolred , 50  , 350 ,  20 , 25 , 'Red' )

yellow_b = ColourButton( yellow , 70  , 330 ,  20 , 25 , 'Yellow' )
cyellow_b = ColourButton( coolyellow , 70  , 350 ,  20 , 25 , 'Yellow' )

blue_b = ColourButton( blue , 90  , 330 ,  20 , 25 , 'Blue' )
cblue_b = ColourButton( coolblue , 90  , 350 ,  20 , 25 , 'Blue' )

green_b = ColourButton( green , 110  , 330 ,  20 , 25 , 'Green' )
cgreen_b = ColourButton( coolgreen , 110  , 350 ,  20 , 25 , 'Green' )

#

skin_b = ColourButton( (255,160,122)  , 50  , 370 ,  20 , 25 , 'Skin' )
pink_b = ColourButton( (255,105,180) , 70  , 370 ,  20 , 25 , 'Yellow' )
brown_b = ColourButton( (139,69,19)  , 90  , 370 ,  20 , 25 , 'Blue' )
grey_b = ColourButton( (169,169,169) , 110  , 370 ,  20 , 25 , 'Green' )

def diplay_list():
    print "Executed"
    #clear Screen
    output.blitBackground()

    #Draw
    for i in painting.cleaned_list:
        pygame.draw.circle( window , i[1] , i[0] , i[2])
    



##green = Planet('Images/PlanetScreen/Green Planet.png' , 300 , 300 , 150 , 200 , 'level_Green' , 'Artemis' , ['Knowledge Center','Has Quizes and can keep track of financial situations'] , coolgreen )
##red = Planet('Images/PlanetScreen/Red Planet.png' , 500 , 300 , 150 , 200 , 'level_Red' , 'Zeus' , ['Home','Place where you review all your progress'] , coolred)
##yellow = Planet('Images/PlanetScreen/Black Planet.png' , 700 , 300 , 150 , 200 , 'level_Black' , 'Hades ' , ['The Mystery Planet','Planet that is in complete mystery']  , tupadd(silver,-70) )



def Paint():
    output.blitBackground()

    while True:       
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:                
                fullquit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run.blue_planet()
                    
                if event.key==pygame.K_RETURN:
                    painting.cleanlist()
                    print painting.cleaned_list

                if event.key == pygame.K_BACKSPACE:
                    painting.undo_mode = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_BACKSPACE:
                    painting.undo_mode = False

                

                
        # Draw Everythin
             



        #output.blitBackground()
        output.blitMenu()

        pencil.displayButton()
        brush.displayButton()
        eraser.displayButton()
        rbin.displayButton()
        #colour.displayButton()

        bplus.displayButton()
        bminus.displayButton()

        cplus.displayButton()
        cminus.displayButton()
        
        # # #
        black_b.displayColour()
        white_b.displayColour()
        
        red_b.displayColour()
        yellow_b.displayColour()
        blue_b.displayColour()
        green_b.displayColour()
        cred_b.displayColour()
        cyellow_b.displayColour()
        cblue_b.displayColour()
        cgreen_b.displayColour()

        skin_b.displayColour()
        pink_b.displayColour()
        brown_b.displayColour()
        grey_b.displayColour()
        
        #printCOOD( window , 0, 0 )

        # Update Function
        paintData.performFunctions()
        painting.get_position()
        
        
        # Logic Testing

        
        



        

        



        
        # Delay framerate
        clock.tick (FPS)
        # Update Screen
        
        pygame.display.update()
        
Paint()


