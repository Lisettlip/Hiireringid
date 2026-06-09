# Impordib pygame teegi mänguakna ja graafika jaoks
import pygame

# Impordib random teegi juhuslike värvide tegemiseks
import random

# Käivitab pygame'i moodulid
pygame.init()

# Määrab akna laiuse pikslites
laius = 640

# Määrab akna kõrguse pikslites
korgus = 480

# Loob akna antud mõõtmetega
ekraan = pygame.display.set_mode((laius, korgus))

# Määrab akna pealkirjaks "Hiir"
pygame.display.set_caption("Hiir")

# Salvestab helesinise taustavärvi RGB kujul
TAUST = (150, 200, 245)

# Loob tühja nimekirja ringide hoidmiseks
ringid = []

# Muutuja, mis hoiab programmi töös
running = True

# Peamine mängutsükkel
while running:

    # Käib läbi kõik pygame sündmused
    for event in pygame.event.get():

        # Kontrollib, kas kasutaja sulges akna
        if event.type == pygame.QUIT:

            # Lõpetab programmi töö
            running = False

        # Kontrollib, kas hiire nuppu vajutati
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Võtab hiireklõpsu x- ja y-koordinaadi
            x, y = event.pos

            # Lisab uue ringi nimekirja
            ringid.append({

                # Ringi x-koordinaat
                "x": x,

                # Ringi y-koordinaat
                "y": y,

                # Ringi juhuslik värv
                "varv": (

                    # Juhuslik punane väärtus
                    random.randint(0, 255),

                    # Juhuslik roheline väärtus
                    random.randint(0, 255),

                    # Juhuslik sinine väärtus
                    random.randint(0, 255)
                )
            })

            # Kontrollib, kas ringe on rohkem kui 10
            if len(ringid) > 10:

                # Kustutab kõige vanema ringi
                ringid.pop(0)

    # Värvib kogu akna taustavärviga üle
    ekraan.fill(TAUST)

    # Käib läbi kõik salvestatud ringid
    for ring in ringid:

        # Joonistab ringi ekraanile
        pygame.draw.circle(

            # Aken, kuhu joonistatakse
            ekraan,

            # Ringi värv
            ring["varv"],

            # Ringi asukoht
            (ring["x"], ring["y"]),

            # Ringi raadius
            10,

            # Ringi joone paksus
            2
        )

    # Uuendab ekraani sisu
    pygame.display.flip()

# Sulgeb pygame'i korrektselt
pygame.quit()
