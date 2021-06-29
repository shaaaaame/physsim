import pygame, pymunk, sys, math, random

from Rutherford.AlphaParticle import AlphaParticle
from Rutherford.GoldParticle import GoldParticle

def Emitter(timeCounter, timeBetweenParticles, particles, prevY):

    #ensures that no collision between alpha particles
    y = random.randint(0, 800)
    while abs(y - prevY) < alphaParticle.radius * 2:
        y = random.randint(0, 800)
    pos = (0, y)


    if timeCounter >= timeBetweenParticles:
        particles.append(alphaParticle.CreateAlphaParticle(space, particleVelocity, pos))
        return 0, y #reset timeCounter
    else:
        return timeCounter, y

def SetGoldParticles():
    x = 650
    y = 250
    goldParticles.append(goldParticle.CreateGoldParticle(space,(x, y) ))
    goldParticles.append(goldParticle.CreateGoldParticle(space, (x, y + 300)))

#initialise pygame & pymunk
pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()

#initialise particles
alphaParticle = AlphaParticle()
alphaParticles = []

goldParticle = GoldParticle()
goldParticles = []

#emitter settings
timeCounter = 0
timeBetweenParticles = 0.5
prevY = 400
particleVelocity = 100

#setting up gold particles
SetGoldParticles()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #emitter
    timeCounter, prevY = Emitter(timeCounter, timeBetweenParticles, alphaParticles, prevY)
    timeCounter += 1/60

    for gold in goldParticles:
        for alpha in alphaParticles:
            if goldParticle.IsNear(alpha.body.position, gold.body.position):
                print("Alpha Particle nearby!")
                goldParticle.ApplyForce(alpha, gold)

    #drawing onto screen
    screen.fill((255, 255, 255))
    alphaParticle.DrawAlphaParticle(alphaParticles, screen)
    goldParticle.DrawGoldParticle(goldParticles, screen)

    space.step(1/60) #increase by delta time
    pygame.display.update() ##update frame
    clock.tick(120) ##limit frames
