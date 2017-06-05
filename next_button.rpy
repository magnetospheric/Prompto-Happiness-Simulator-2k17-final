init python:

    #This controls when the love-points floater appears.
    show_next=False

    ## ------------ Next Floater ----------------------

    def next_overlay():

        # --- Giselle's Love Bar -------
        if show_next:
            # set up a transparent frame to put things in
            ui.frame(
                xalign = 0.5,
                ypos = 0.04,
                style = "title_frame",
            )

            ui.vbox(xalign = 0)

            ui.text ("NEXT",
                xalign = 0.05,
                ypos = 2,
                color = "#ededda",
                size=20)

            ui.bar(max_next, next,
                style="next_bar")

            ui.close() #closes vbox


    config.overlay_functions.append(next_overlay)

init -2 python:
    next = 2
    max_next = 30

init -5 python:
    #custom bar
    style.next_bar = Style(style.default)
    style.next_bar.xalign = 0.5
    style.next_bar.xmaximum = 325 # bar width
    style.next_bar.ymaximum = 25 # bar height
    style.next_bar.left_gutter = 10
    style.next_bar.right_gutter = 10

    style.next_bar.left_bar = Frame("ui/bar_full.png", 0, 0)
    style.next_bar.right_bar = Frame("ui/bar_empty.png", 0, 0)

    style.next_bar.thumb = "ui/thumb.png"
    style.next_bar.thumb_shadow = None
    style.next_bar.thumb_offset = 16

    style.next_bar.font = "fonts/AvantGarde-Book.ttf"


    style.title_frame = Style(style.default)
    style.title_frame.background = Frame("ui/bar_title_bg.png")
