import math, pygame, pymunk

class GoldParticle:

    charge = 2
    radius = 7.2
    electronFieldRadius = 1.46 * 100
    mass = 327 #in kg * 10^-27
    chargeRadius = 40
    force = 20

    #creating particle in pymunk
    def CreateGoldParticle(self, space, pos):

        #nucleus
        particle = GoldParticle()

        body = pymunk.Body(particle.mass, math.inf, body_type=pymunk.Body.STATIC)
        body.position = pos
        body.center_of_gravity = (0, 0)

        shape = pymunk.Circle(body, particle.radius)
        shape.elasticity = 1
        shape.layers = 2
        space.add(body, shape)
        return shape

    #drawing particle + electron field in pygame
    def DrawGoldParticle(self, goldParticles, screen):
        for goldParticle in goldParticles:
            pygame.draw.circle(screen, (204,204,0), goldParticle.body.position, GoldParticle.radius)
            pygame.draw.circle(screen, (200, 200, 200), goldParticle.body.position, GoldParticle.electronFieldRadius, width=3)



    def IsNear(self, alphaPos, goldPos):
        particle = GoldParticle()

        if math.sqrt((alphaPos.x - goldPos.x)**2 + (alphaPos.y - goldPos.y)**2) < particle.chargeRadius:
            return True
        else:
            return False

    def ApplyForce(self, alphaParticle, goldParticle):
        direction = alphaParticle.body.position - goldParticle.body.position
        alphaParticle.body.apply_force_at_local_point(direction * GoldParticle.force, (0, 0))


