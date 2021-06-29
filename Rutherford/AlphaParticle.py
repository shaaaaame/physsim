import math, pymunk, pygame

class AlphaParticle:
    charge = 2
    radius = 7.2
    mass = 6.64 #in kg * 10^-27

    ##creating particle in pymunk
    def CreateAlphaParticle(self, space, vel, pos):
        particle = AlphaParticle()

        body = pymunk.Body(particle.mass, math.inf, body_type=pymunk.Body.DYNAMIC)

        body.position = pos

        body.velocity = (vel, 0)
        body.center_of_gravity = (0, 0)

        shape = pymunk.Circle(body, particle.radius)
        shape.elasticity = 1
        shape.layer = 1
        shape.filter = pymunk.ShapeFilter(1)
        space.add(body, shape)
        return shape


    ##draw the particle in pygame
    def DrawAlphaParticle(self, particles, screen):
        for particle in particles:
            pygame.draw.circle(screen, (255, 0, 0), particle.body.position, AlphaParticle.radius)






