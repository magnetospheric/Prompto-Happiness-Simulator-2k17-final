init python:

    #This controls when the love-points floater appears.
    show_happiness=False

    ## ------------ Love Points Floater ----------------------

    def stats_overlay():

        # --- Giselle's Love Bar -------
        if show_happiness:
            ui.frame(
                #xalign = 0.9, #centered
                xalign = 0.96,
                ypos = 0.04,
            )

            ui.vbox(xalign = 0.5)
            ui.text ("HAPPINESS",
                xalign = 0.0)
            ui.bar(max_happiness, happiness,
                style="my_bar")

            ui.close()


    config.overlay_functions.append(stats_overlay)

init -2 python:
    happiness = 2
    max_happiness = 30

init -5 python:
    #custom bar
    style.my_bar = Style(style.default)
    style.my_bar.xalign = 0.5
    style.my_bar.xmaximum = 325 # bar width
    style.my_bar.ymaximum = 25 # bar height
    style.my_bar.left_gutter = 10
    style.my_bar.right_gutter = 10

    style.my_bar.left_bar = Frame("ui/bar_full.png", 0, 0)
    style.my_bar.right_bar = Frame("ui/bar_empty.png", 0, 0)
    #style.my_bar.hover_left_bar = Frame("ui/bar_hover.png", 0, 0)

    style.my_bar.thumb = "ui/thumb.png"
    style.my_bar.thumb_shadow = None
    style.my_bar.thumb_offset = 16

    style.my_bar.font = "fonts/AvantGarde-Book.ttf"
