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
# -- scene_05_campfire.rpy


#### SPLASHSCREEN ####

image producer = "images/logos/producer.png"
image author = "images/logos/author.png"
image title = "images/logos/title.png"

label splashscreen:
    scene black
    with Pause(1)

    #play sound "ping.ogg"

    show producer with dissolve
    with Pause(2)

    scene author with dissolve
    with Pause(2)

    scene title with dissolve
    with Pause(2)

    return
