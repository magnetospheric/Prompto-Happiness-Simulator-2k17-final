# script for Prompto Happiness Simulator 2k17
# authored by Olly Ferrie
# created 07-05-2017
#last edited 08-05-2017


#### FILES USED ####
# -- settings.rpy
# -- scene_01_start.rpy
# -- scene_02_whathappened.rpy
# -- scene_03_niflheim.rpy
# -- scene_04_tomountainhaven.rpy
# -- scene_05_human.rpy
# -- scene_06_real_life_rpg.rpy
# -- scene_07_campfire_food.rpy
# -- credits.rpy



#### SPLASHSCREEN ####

image producer = "images/logos/producer.png"
image author = "images/logos/author.png"
image title = "images/logos/title.png"

label splashscreen:

    python:

        if not persistent.set_volumes:
            persistent.set_volumes = True

            _preferences.volumes['music'] = .70
            _preferences.volumes['sounds'] = .80

    play music "sound/Voglio_La_Pace-Snippet.wav" fadein 1.0

    scene black
    with Pause(1)

    show producer with dissolve
    with Pause(2)


    scene author with dissolve
    with Pause(2)


    scene title with dissolve
    with Pause(1)
    stop music fadeout 0.5
    pause 0.5

    return
