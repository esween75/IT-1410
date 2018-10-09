import pygame
import Pic
# this example game draws 3 concentric circles on top of a single color background
# the circles move down every time frame
# the user can control the circles by:
# - clicking the left mouse button to relocate them
# - holding the UP key to move them up
# - pressing the A key to move them to the left of the window
# - holding the A key to gradually move them to the right
class Illustrate:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height

        self.Pic = pic.Pic(self.mWidth, self.mHeight)
        



        # DSU's colors
        self.mDSUTan = ( 229, 217, 189 )
        self.mDSUBlack = ( 2, 2, 2 )
        self.mDSULightRed = ( 186, 28, 33 )
        self.mDSUDarkRed = ( 136, 21, 24 )
        self.grey = (230,230,230)
        self.blue = ( 135, 206, 250)
        self.black = (  0,   0,   0)
        self.white = (255, 255, 255)
        self.green = (  0, 255,   0)
        self.red =   (200,   0,   0)
        self.yellow = (255, 255, 0 )
        # Sizes to draw circles
        self.mRadius1 = int( min( self.mWidth, self.mHeight ) / 10 )
        self.mRadius2 = int( self.mRadius1 * 0.7 )
        self.mRadius3 = int( self.mRadius1 * 0.4 )

        # Position to draw circles
        self.mDrawX = self.mWidth / 2
        self.mDrawY = 2 * self.mRadius1
        
        return

    # move the circles to the left side of the window every time the a button is pressed
    def actOnPressA( self ):
        self.mDrawX = self.mRadius1
        return

    # move the circles right every frame the a button is held down
    # don't let the circles go off the window
    def actOnHoldA( self ):
        self.mDrawX += self.mWidth / 20
        if self.mDrawX + self.mRadius1 > self.mWidth:
            self.mDrawX = self.mWidth - self.mRadius1
        return

    # raise the circles every frame the UP button is held down
    # don't let the circles go off the window
    def actOnHoldUP( self ):
        self.mDrawY -= self.mHeight / 20
        if self.mDrawY < self.mRadius1:
            self.mDrawY = self.mRadius1
        return

    # relocate the circles based on the mouse click
    # don't let the circles go off the window
    def actOnLeftClick( self, x, y ):
        self.mDrawX = x
        if self.mDrawX < self.mRadius1:
            self.mDrawX = self.mRadius1
        if self.mDrawX + self.mRadius1 > self.mWidth:
            self.mDrawX = self.mWidth - self.mRadius1
            
        self.mDrawY = y
        if self.mDrawY < self.mRadius1:
            self.mDrawY = self.mRadius1
        if self.mDrawY + self.mRadius1 > self.mHeight:
            self.mDrawY = self.mHeight - self.mRadius1
        return

    # move the circles down every frame according to how much time has passed
    # don't let the circles go off the window
    def evolve( self, dt ):
        dy = dt * ( self.mHeight / 5 )
        self.mDrawY += dy
        if self.mDrawY + self.mRadius1 > self.mHeight:
            self.mDrawY = self.mHeight - self.mRadius1
        return

    # draws the current state of the system
    def draw( self, surface ):
        
        # rectangle to fill the background
        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, self.blue, rect, 0 )

        # code added by eric(l) w h  (r) w h

        #house
        pygame.draw.rect(surface, self.red, (50,400,460,170), 0)

        #cloud
        pygame.draw.ellipse(surface, self.white, [350, 100, 200, 50])
        pygame.draw.ellipse(surface, self.grey, [500, 150, 150, 30])
        # birds
        pygame.draw.arc(surface, self.black, (400,50,30,20), 6, 3, 3)
        pygame.draw.arc(surface, self.black, (430,50,30,20), 6, 3, 3)


        pygame.draw.arc(surface, self.black, (500,50,30,20), 6, 3, 3)
        pygame.draw.arc(surface, self.black, (530,50,30,20), 6, 3, 3)
        
        pygame.draw.arc(surface, self.black, (590,70,30,20), 6, 3, 3)
        pygame.draw.arc(surface, self.black, (620,70,30,20), 6, 3, 3)
        
        #windows)
        pygame.draw.rect(surface, self.black, (60,420,80,50), 0)
        pygame.draw.rect(surface, self.green, (450,430,50,55), 0)

        #sun
        pygame.draw.circle(surface, self.yellow, [100, 100], 50, 0)
    
        #door
        pygame.draw.rect(surface, self.white, (300,500,60,70), 0)
        #door nob
        pygame.draw.circle(surface, self.black, [350, 540], 5, 0)
        
        #roof                                     
        pygame.draw.polygon(surface, self.black, [[300, 200], [50, 400],[510, 400]], 0)
        # three stacked, concentric circles @ current position
        #center = ( int( self.mDrawX ), int( self.mDrawY ) ) 
        #pygame.draw.circle( surface, self.mDSUDarkRed, center, self.mRadius1, 0 )
        #pygame.draw.circle( surface, self.mDSUBlack, center, self.mRadius2, 0 )
        #pygame.draw.circle( surface, self.mDSULightRed, center, self.mRadius3, 0 )

        # http://learnrich.org/pygame-drawing-shapes/ for shape examples
        return

    

