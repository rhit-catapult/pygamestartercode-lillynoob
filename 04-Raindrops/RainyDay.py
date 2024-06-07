import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # DONE 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5,15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # DONE 11: Change the  y  position of this Raindrop by its speed.
        self.y += self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # DONE 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        # DONE 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y+5), 2)



class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        # Done 16: Initialize this Hero, as follows:
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0
        #     - Store the screen.
        #     - Set the initial position of this Hero to x and y.
        #     - Create an image of this Hero WITH    an umbrella to the given with_umbrella_filename.
        #     - Create an image of this Hero WITHOUT an umbrella to the given without_umbrella_filename.
        #     - Set the "last hit time" to 0.
        #   Use instance variables:
        #      screen  x  y  image_umbrella   image_no_umbrella  last_hit_time.


    def draw(self):
        """ Draws this sprite onto the screen. """
        # DONE 17: Draw (blit) this Hero, at this Hero's position, WITHOUT an umbrella:

        # DONE 21: Instead draw (blit) this Hero, at this Hero's position, as follows:

        current_image = self.image_no_umbrella

        if time.time() > self.last_hit_time + 1:
            current_image = self.image_no_umbrella
        else:
            current_image = self.image_umbrella

        self.screen.blit(current_image, (self.x, self.y))

        #     If the current time is greater than this Hero's last_hit_time + 1,
        #       draw this Hero WITHOUT an umbrella,
        #       otherwise draw this Hero WITH an umbrella.
        pass

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        # DONE 19: Return True if this Hero is currently colliding with the given Raindrop.
        hero_hit_box = pygame.Rect(self.x,self.y, self.image_umbrella.get_width(), self.image_umbrella.get_height())
        return hero_hit_box.collidepoint(raindrop.x,raindrop.y)

class Cloud:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x,self.y))

    def rain(self):
        drop = Raindrop(self.screen, random.randint(self.x, self.x+300), self.y+100)
        self.raindrops.append(drop)


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Rainy Day")
    clock = pygame.time.Clock()
    mike = Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    cloud = Cloud(screen, 300, 50, "cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 5
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 5
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 5
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 5


        screen.fill((255,255,255))

        cloud.draw()

        cloud.rain()
        for rain in cloud.raindrops:
            rain.move()
            rain.draw()
            if mike.hit_by(rain):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(rain)
            if alyssa.hit_by(rain):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(rain)
            if rain.off_screen():
                cloud.raindrops.remove(rain)

        mike.draw()
        alyssa.draw()
        pygame.display.update()



main()