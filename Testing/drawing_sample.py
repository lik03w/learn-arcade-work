import arcade

#öffnet ein Fenster mit spezifizeirten länge und breite
arcade.open_window(600, 600, "Testfenster")



"""
So macht man blöcke fuer lange kommentare und unten werden die hintergrund Farbe festgegeben
"""
arcade.set_background_color((70, 156, 222))

#ab arcade start render beginnen wir mit dem rendern von inhalten
arcade.start_render()

#macht einen riesigen rechteck der größe der hälfte des bildschirms
arcade.draw_lrbt_rectangle_filled(0,600,0,300,(70,222,96))

#versuch bäume zu malen mit rechteck und ovalen form als blätter
#left, right, bottom , top,
arcade.draw_lrbt_rectangle_filled(80,100,280,350,arcade.csscolor.BURLYWOOD)
arcade.draw_circle_filled(90,370,40,arcade.color.AMAZON)
#def kleines_Haus():

#auch "baum" mit rechteck und ellipse aber anderen farben
arcade.draw_lrbt_rectangle_filled(180,200,280,350,arcade.csscolor.BURLYWOOD)
arcade.draw_ellipse_filled(190,370,50,80,arcade.color.MAGENTA)

#auch baum mit arc ansatz
arcade.draw_lrbt_rectangle_filled(280,300,280,350,arcade.csscolor.BURLYWOOD)
arcade.draw_arc_filled(290,350,50,80,arcade.csscolor.DARK_GREEN,0,180)


#neuer beim mit dreieck ansatz
arcade.draw_lrbt_rectangle_filled(380,400,280,350,arcade.csscolor.BURLYWOOD)
arcade.draw_triangle_filled(360,350, 420, 350, 390,430, arcade.csscolor.DARK_TURQUOISE)

#neuer baum mit polygon
arcade.draw_lrbt_rectangle_filled(480,500,280,350,arcade.csscolor.BURLYWOOD)
arcade.draw_polygon_filled(((460,350),(520,350),(470,370),(510,370),(480,375),(500,375),(490,385)),arcade.csscolor.LIGHT_SEA_GREEN)


#erstellen einer sonne
arcade.draw_circle_filled(520,560,70,arcade.csscolor.YELLOW)
#Sonnenstrahlen
arcade.draw_line(520, 560, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(520, 560, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(520, 560, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(520, 560, 500, 650, arcade.color.YELLOW, 3)

#Unterschrift bzw. text fuer das projekt
arcade.draw_text("Hier sind die Bunten Baeume!!!!", 250,270,arcade.color.BABY_BLUE_EYES)


#beenden des rendern
arcade.finish_render()

#laufenhalten des fensters sonst schließt er sich
arcade.run()