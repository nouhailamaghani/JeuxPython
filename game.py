import pygame
import pytmx
import pyscroll

from player import Player

pygame.init()


class Game:
    def __init__(self):
        # Créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((800, 600))

        # Définir le nom de la fenêtre
        pygame.display.set_caption("Pygame - Aventure")

        # Charger la carte (tmx)
        tmxdata = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmxdata)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Générer un joueur
        player_position = tmxdata.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y)
        #definir une liste collision
        self.walls =[]

        for obj in tmxdata.objects:
            if obj.name == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        # Dessiner le groupe des calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
    def handele_input(self):
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
    def run(self):
        clock = pygame.time.Clock()
        # Boucle du jeu
        running = True

        while running:
            self.handele_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)
        pygame.quit()
