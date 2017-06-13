#### CREDITS ####

image fin = "images/logos/fin.png"
image credit = "images/logos/credit.png"

label credits:

    scene bg cavern

    $ show_happiness = False

    play music "sound/credits.wav" fadein 3.0

    $ quick_menu = False
    
    show black
    with fastdissolve
    $ renpy.pause(2.0, hard = True)


    show fin with dissolve
    $ renpy.pause(4.0, hard = True)

    show credit with dissolve
    $ renpy.pause(6.0, hard = True)

    show black
    with slowdissolve

    stop music fadeout 3.0

    $ renpy.pause(3.0, hard = True)

    return
