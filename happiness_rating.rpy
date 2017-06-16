init python:

    #This controls when the love-points floater appears.
    show_happiness=False

    ## ------------ Happiness Floater ----------------------

    def stats_overlay():

        # --- Happiness Bar -------
        if show_happiness:
            # set up a transparent frame to put things in
            ui.frame(
                xalign = 0.96,
                ypos = 0.04,
                style = "title_frame",
            )

            ui.vbox(xalign = 0)

            ui.text ("HAPPINESS",
                xalign = 0.05,
                ypos = 2,
                color = "#ededda",
                size=20)

            ui.bar(max_happiness, happiness,
                style="my_bar")

            ui.close() #closes vbox


    config.overlay_functions.append(stats_overlay)


    # def end_rating():
    #
    #     # --- Happiness Bar -------
    #     if show_rating:
    #
    #         # set up a transparent frame to put things in
    #         ui.frame(
    #         xalign = 0.96,
    #         ypos = 0.04,
    #         style = "title_frame",
    #         )
    #
    #         ui.vbox(xalign = 0)
    #
    #         if happiness == 20:
    #
    #
    #
    #         ui.close() #closes vbox
    #         # elif happiness >= 18:
    #         #
    #         # elif happiness >= 15:
    #         #
    #         # elif happiness >= 11:
    #         #
    #         # elif happiness >= 6:
    #         #
    #         # elif happiness >= 2:
    #
    #         ui.text ("HAPPINESS",
    #             xalign = 0.05,
    #             ypos = 2,
    #             color = "#ededda",
    #             size=20)
    #
    #         ui.bar(max_happiness, happiness,
    #             style="my_bar")
    #
    #
    #
    #
    # config.overlay_functions.append(stats_overlay)
    #

init -2 python:
    happiness = 2
    max_happiness = 18.6

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

    style.my_bar.thumb = "ui/thumb.png"
    style.my_bar.thumb_shadow = None
    style.my_bar.thumb_offset = 16

    style.my_bar.font = "fonts/AvantGarde-Book.ttf"


    style.title_frame = Style(style.default)
    style.title_frame.background = Frame("ui/bar_title_bg.png")
