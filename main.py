import pygame
from game import Game,Player
 

pygame.init()




#generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall game")
screen=pygame.display.set_mode((1080,720))


#importer et charger l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

#charger le jeu
game = Game()


#charger notre joueur ( premier chargement)
"player = Player()"
# retrait de cette binitialisation car on cree deja Player() dans game.


running = True

#boucle tant que cette condition est vrai
while running:
    
    #appliquer l'arriere plan de notre jeu
    screen.blit(background,(0,-200))

    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

     
    #recuperer les projectiles du joueur
    for projectile in game.player.all_projectile:
        projectile.move(game.player)

    #recuperer les monstres du jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    #Appliquer l'image des projectiles
    game.player.all_projectile.draw(screen)

    #appliquer l'ensemble de image de mon groupe de monstre
    game.all_monsters.draw(screen)


    #verifier si le joueur veut aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width  < screen.get_width():
        game.player.move_right()
        print(pygame.K_RIGHT)
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
        print(pygame.K_LEFT )
        

    print(game.player.rect.x)

    #supprimer les monstres touchee par les projectiles

    ''' a verifier '''
    # Parcourir chaque monstre dans le groupe all_monsters
for monster in game.all_monsters:
    # Comparer la position x du monstre avec celle du projectile
    for projectile in game.player.all_projectile:
        if monster.rect.x == projectile.rect.x:
            # Code pour gérer la collision ou autre action
            print("Collision détectée")


    #mettre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #DETECTER si la touche espace est enclenche pour le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

            '''#quelle touche est utilisée
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            elif event.key == pygame.K_LEFT:
                game.player.move_left()'''