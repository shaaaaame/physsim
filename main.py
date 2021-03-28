# https://www.youtube.com/watch?v=HEfHFsfGXjs
# Thanks Mr Wright!

import pygame, pymunk, sys, math

def create_wall(space):
    body = pymunk.Body(1, 0, body_type=pymunk.Body.STATIC)
    body.position = (35, 400)
    body.center_of_gravity = (0, 0)
    shape = pymunk.Poly.create_box(body, (70, 800))
    shape.elasticity = 1
    shape.friction = 0
    shape.collision_type = 2
    space.add(body, shape)
    return shape

def draw_wall(wall):
    pygame.draw.polygon(screen, (0, 0, 0), [(0, 0), (70, 0), (70, 800), (0, 800)])

def create_ball(space, mass, pos, vel, colType):
    body = pymunk.Body(mass, math.inf , body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    body.velocity = (vel, 0)
    body.center_of_gravity = (0, 0)
    shape = pymunk.Poly.create_box(body, (50, 50))
    shape.collision_type = colType
    shape.elasticity = 1
    shape.friction = 0
    space.add(body, shape)
    return shape

def draw_ball(balls):
    for ball in balls:
        x = ball.body.position.x
        y = ball.body.position.y
        pygame.draw.polygon(screen, (255, 133, 162), [(x - 25, y - 25), (x + 25, y - 25), (x + 25, y + 25), (x - 25, y + 25)])

def collision(space, arbiter, data):
    global collisions
    global text
    collisions += 1
    text = font.render(str("Collisions : " + str(collisions)), True, (0, 0, 0))
    return True

def end(vel1, vel2):
    if vel1 >= 0:
        if vel1 < vel2:
            screen.blit(end_text, end_textRect)
            return True
    else:
        return False

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()

wall = create_wall(space)
balls = []

##collision types
collType_square1 = 0
collType_square2 = 1
collType_wall = 2

collisions = 0
handler_box = space.add_collision_handler(0, 1)
handler_wall = space.add_collision_handler(0, 2)
handler_box.begin = collision
handler_wall.begin = collision

#collision text
font = pygame.font.Font(None, 30)
text = font.render(str("Collisions : " + str(collisions)), True, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (700, 50)

#end text
font2 = pygame.font.Font(None, 50)
end_text = font2.render("END OF SIMULATION", True, (0, 0, 0))
end_textRect = text.get_rect()
end_textRect.center = (300, 400)

#buttons
button_text = font.render("Mass in power of 100 : ", True, (0, 0, 0))
button_textRect = button_text.get_rect()
button_textRect.center = (280, 35)
buttons = []
button0 = font.render("0", True, (0, 0, 0))
button1 = font.render("1", True, (0, 0, 0))
button2 = font.render("2", True, (0, 0, 0))
button3 = font.render("3", True, (0, 0, 0))
buttons.append(button0)
buttons.append(button1)
buttons.append(button2)
buttons.append(button3)

#state
started, running, pause = 0, 1, 2
state = running

#power for mass
power = None

while True:
    time_delta = clock.tick(2400)/ 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and power == None:
            x = 140
            y = 70
            for i in range(len(buttons)):
                if x <= mouse[0] <= x + 70 and y <= mouse[1] <= y + 70:
                    power = i
                x += 140

    if state == started:
        balls.append(create_ball(space, 1, (400, 400), 0, 0))
        if power <= 2:
            balls.append(create_ball(space, 100**power, (600, 400), -500, 1))
        else:
            balls.append(create_ball(space, 100**power, (600, 400), -100, 1))
        state = running

    if state == running:
        screen.fill((217, 217, 217))
        screen.blit(text, textRect)
        screen.blit(button_text, button_textRect )

        draw_wall(wall)
        draw_ball(balls)
        for ball in balls:
            #mass text
            mass_text = font.render(str(str(ball.body.mass) + " kg"), True, (0, 0, 0))
            mass_textRect = mass_text.get_rect()
            mass_textRect.center = (ball.body.position.x, 330)
            screen.blit(mass_text, mass_textRect)

        if len(balls) != 0:
            ended = end(balls[0].body.velocity.x, balls[1].body.velocity.x)

        #if power not selected, pause
        if power == None:
            state = pause

    elif state == pause:
        ##buttons
        mouse = pygame.mouse.get_pos()
        x = 140
        y = 70
        for button in buttons:
            if x <= mouse[0] <= x + 70 and y <= mouse[1] <= y + 70:
                pygame.draw.rect(screen, (255, 192, 203), [x, y, 70, 70])

            else:
                pygame.draw.rect(screen, (255, 105, 180), [x, y, 70, 70])
            screen.blit(button, (x + 30, y + 25))
            x += 140
        if power != None:
            button_text = font.render(str("Mass in power of 100 : " + str(power)), True, (0, 0, 0))
            state = started

    space.step(1/2400)
    pygame.display.update()
    clock.tick(2400)