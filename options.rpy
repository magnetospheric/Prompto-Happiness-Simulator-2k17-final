## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Prompto Happiness Simulator 2k17")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "PromptoHappinessSimulator2k17"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 30


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "PromptoHappinessSimulator2k17-1495668039"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    is_load_screen = False
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


    def big_tag(tag, argument, contents):

        size = int(argument) * 20

        return [
                (renpy.TEXT_TAG, u"size={}".format(size)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/size"),
            ]

    config.custom_text_tags["big"] = big_tag

 #renpy.music.register_channel(name, mixer=None, loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
$ renpy.music.set_volume(0.5)
$ renpy.sound.set_volume(0.5)

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"


####################
#### Characters ####
####################

define prompto = DynamicCharacter('prompto_name', color="#fff2b5", ctc="ctc_blink", ctc_position="fixed")
define you = DynamicCharacter('your_name', color="#b2b1c4", ctc="ctc_blink", ctc_position="fixed")
define narrator = Character(ctc="ctc_blink", ctc_position="fixed")

image ctc_blink = LiveComposite(
    (65, 65),
    (930, 685), "ctc_base",
    (930, 685), "glow",
    )

image ctc_base:
    "images/ui/next_button_small.png"
    linear 0.8 alpha 0.95
    repeat

image glow:
    "images/ui/next_button_hover_small.png"
    linear 0.8 alpha 0.0
    "images/ui/next_button_hover_small.png"
    linear 0.8 alpha 0.5
    repeat


#### Character Images ####
# submissive
image prompto downcast  = "images/characters/prompto_downcast.png"
image prompto semidowncast  = "images/characters/prompto_semidowncast.png"
image side prompto semidowncast  = "images/characters/prompto_semidowncast.png"
image prompto regrets  = "images/characters/prompto_regrets.png"
image prompto resigned = "images/characters/prompto_resigned.png"
image prompto frightened_tightlipped  = "images/characters/prompto_frightened_tightlipped.png"

# raised looks
image prompto raisedeyes = "images/characters/prompto_raisedeyes.png"
image prompto raisedeyes_closed = "images/characters/prompto_raisedeyes_closed.png"

# side looks
image prompto dubious_sidecast  = "images/characters/prompto_dubious_sidecast.png"
image prompto frightened_sidecast  = "images/characters/prompto_frightened_sidecast.png"

# shock
image prompto surprised  = "images/characters/prompto_surprised.png"
image prompto dubious  = "images/characters/prompto_dubious.png"
image prompto frightened  = "images/characters/prompto_frightened.png"

# actions
#image prompto scrutinisinggun  = "images/characters/prompto_scrutisninggun.png"
image nextbutton = "images/ui/next_button.png"

# smiles
image prompto sadsmile  = "images/characters/prompto_sadsmile.png"
image prompto neutralsmile  = "images/characters/prompto_neutralsmile.png"
image prompto calmsmile  = "images/characters/prompto_calmsmile.png"
image prompto downcastsmile  = "images/characters/prompto_downcastsmile.png"
image side prompto downcastsmile  = "images/characters/prompto_downcastsmile.png"
#image prompto sadlaugh = "images/characters/prompto_sadlaugh.png"

# laughs
image prompto lightlaugh = "images/characters/prompto_lightlaugh.png"
image prompto widelaugh = "images/characters/prompto_widelaugh.png"
#image prompto relievedsmile = "images/characters/prompto_relievedsmile.png"

#### Background Images ####
image bg snowy_plains = 'images/backgrounds/snowy_plains.png'
image bg distant_mountain = 'images/backgrounds/distant_mountain.png'
image bg plains_with_mountain = 'images/backgrounds/plains_with_mountain.png'
image bg cavern = 'images/backgrounds/cavern.png'
image bg black = "images/backgrounds/black_bg.png"
image black = "images/backgrounds/black_bg.png"
image yellow = "images/backgrounds/yellow_bg.png"

#image snow = SnowBlossom("images/sprites/big_snow.png", count=50)

# Animations and transitions #

image snow:
        choice (show_snow == True):
            Fixed(
                    SnowBlossom(im.Alpha("images/sprites/big_snow.png",0.75), count=2, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/medium_snow.png",0.9), count=7, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/small_snow.png",0.95), count=10, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/tiny_snow.png",0.99), count=20, start=5, yspeed=(40,80)) )
        choice (show_snow == False):
            Fixed(
                    SnowBlossom(im.Alpha("images/sprites/big_snow.png",0.0), count=1, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/medium_snow.png",0.0), count=1, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/small_snow.png",0.0), count=1, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/tiny_snow.png",0.0), count=1, start=5, yspeed=(40,80)) )


define slowfade = Fade(2.0, 0.0, 2.0)
define slowdissolve = Dissolve(8)
define mediumdissolve = Dissolve(5)
define fastdissolve = Dissolve(2)



# MUSIC #

define config.main_menu_music = "sound/menu.wav"
define audio.menu = "sound/menu.wav"
define audio.credits = "sound/credits.wav"
define audio.snowplains = "sound/snowplains.wav"
define audio.footsteps = "sound/footsteps.wav"
define audio.breath_in = "sound/breath_in.wav"
define audio.thunder = "sound/thunder.wav"
define audio.thunder_distant = "sound/thunder_distant.wav"
define audio.magitek = "sound/magitek.wav"
