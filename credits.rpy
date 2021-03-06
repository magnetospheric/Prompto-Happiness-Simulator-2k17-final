#### CREDITS ####

image fin = "images/logos/fin.png"
image thanks = "images/logos/thanks.png"
image credit = "images/logos/credit.png"

label credits:

    $ show_say = False

    scene bg cavern

    show black
    with fastestdissolve
    $ renpy.pause(1.0, hard = True)

    show fin with dissolve
    $ renpy.pause(6.0, hard = True)

    show thanks with dissolve
    $ renpy.pause(6.0, hard = True)

    show credit with dissolve
    $ renpy.pause(4.0, hard = True)

    show black
    with slowdissolve

    stop music fadeout 3.0

    $ renpy.pause(3.0, hard = True)

    return
