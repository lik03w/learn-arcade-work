import arcade


#öffnet das fenster
arcade.open_window(800,800)


#beginn des malens
arcade.start_render()
arcade.draw_lrbt_rectangle_filled(0,800,0,400,arcade.csscolor.LIGHT_GREEN)
arcade.draw_lrbt_rectangle_filled(0,800,400,800,arcade.csscolor.BLUE)
arcade.draw_circle_filled(400,360,80,(255,255,255))
arcade.draw_circle_filled(400,450,40,(255,255,255))
arcade.draw_circle_filled(400,500,25,(255,255,255))
#beendet das aktive rendern
arcade.finish_render()


#hällt das fenster offen
arcade.run()
