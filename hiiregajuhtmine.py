import pygame, sys, random

pygame.init()

# ekraan
screenX = 640
screenY = 480
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("ringid")

clock = pygame.time.Clock()

# värvid
background = (25, 30, 45)
white = (255, 255, 255)

# font
font = pygame.font.SysFont(None, 36)

# ringide loend
circles = []

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()

            # olemasolevad ringid muutuvad suuremaks
            for circle in circles:
                circle[3] += 2

            color = (
                random.randint(80, 255),
                random.randint(80, 255),
                random.randint(80, 255)
            )

            radius = random.randint(8, 30)

            # x, y, värv, raadius
            circles.append([mouseX, mouseY, color, radius])

            # korraga maksimaalselt 10 ringi
            if len(circles) > 10:
                circles.pop(0)

    screen.fill(background)

    # ringide joonistamine
    for circle in circles:
        x = circle[0]
        y = circle[1]
        color = circle[2]
        radius = circle[3]

        # suurem läbipaistev vari/halo
        pygame.draw.circle(screen, color, (x, y), radius + 5)

        # põhiring
        pygame.draw.circle(screen, color, (x, y), radius)

        # valge ääris
        pygame.draw.circle(screen, white, (x, y), radius, 2)

        # väike hele täpp ringi sees
        pygame.draw.circle(screen, white, (x - radius // 3, y - radius // 3), max(2, radius // 5))

    # mitu ringi on ekraanil
    text = font.render("Ringe: " + str(len(circles)) + " / 10", True, white)
    screen.blit(text, (20, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()