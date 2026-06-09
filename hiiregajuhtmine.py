# Impordime vajalikud teegid
import pygame
import random

# Käivitame pygame'i
pygame.init()

# Määrame akna laiuse ja kõrguse
laius, korgus = 640, 480

# Loome mänguakna
ekraan = pygame.display.set_mode((laius, korgus))

# Määrame akna pealkirja
pygame.display.set_caption("Hiir")

# Taustavärv (helesinine)
TAUST = (150, 200, 245)

# Loend ringide salvestamiseks
ringid = []

# Muutuja programmi tööshoidmiseks
running = True

# Peatsükkel töötab seni, kuni aken suletakse
while running:

    # Kontrollime kõiki sündmusi
    for event in pygame.event.get():

        # Kui vajutatakse akna sulgemisnuppu
        if event.type == pygame.QUIT:
            running = False

        # Kui tehakse hiireklõps
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Salvestame klõpsu koordinaadid
            x, y = event.pos

            # Lisame uue ringi loendisse
            ringid.append({
                "x": x,  # x-koordinaat
                "y": y,  # y-koordinaat

                # Juhuslik värv (boonus)
                "varv": (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            })

    # Täidame tausta helesinise värviga
    ekraan.fill(TAUST)

    # Joonistame kõik ringid ekraanile
    for ring in ringid:

        pygame.draw.circle(
            ekraan,                     # kuhu joonistada
            ring["varv"],               # ringi värv
            (ring["x"], ring["y"]),     # ringi asukoht
            10,                         # raadius 10 pikslit
            2                           # ainult ääris, paksus 2
        )

    # Uuendame ekraani
    pygame.display.flip()

# Sulgeme pygame'i korrektselt
pygame.quit()
