#### CREDITS ####

image fin = "images/logos/fin.png"
image credit = "images/logos/credit.png"

label credits:

    $ show_happiness = False
    $ quick_menu = False

    play music "sound/credits.wav" fadein 3.0

    scene bg yellow
    with slowdissolve

    pause 2

    scene bg black
    with slowdissolve

    show fin with dissolve
    with Pause(4)

    scene credit with dissolve
    with Pause(6)


    scene bg black
    with slowdissolve

    stop music fadeout 3.0

    pause 3

    return
