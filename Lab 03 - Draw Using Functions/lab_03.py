import arcade
import random

#öffnet das fenster
arcade.open_window(800,800)

#start des renderns
arcade.start_render()

#malt den hintergrund
arcade.draw_lrbt_rectangle_filled(0,800,0,600,(196, 196, 196))
arcade.draw_ellipse_filled(20,650,20,10,(196, 196, 196))


#
def kleiner_stern_weiß(pos_x,pos_y):
    arcade.draw_ellipse_filled(pos_x, pos_y, 20, 10, (196, 196, 196))

def Krater(x,y):
    arcade.draw_circle_outline(x,y,20,(0,0,0))
    random_int = random.randint(1,10)
    kreis_modifier = random.randint(-3, 3)
    for i in range(3):
        arcade.draw_circle_filled(x + kreis_modifier,y + kreis_modifier,random_int,(75, 79, 76))

def sternen_himmerl():
    for i in range (0,800,50):
        j = random.randint(600,800)
        kleiner_stern_weiß(i,j)

def krater_feld(reihen_durchlauf):
    for i in range(reihen_durchlauf):
        for j in range(0,800,40):
            tmp = random.randint(0,600)
            Krater(j,tmp)

sternen_himmerl()
krater_feld(1)
arcade.finish_render()

#hällt das fenster offen
arcade.run()
