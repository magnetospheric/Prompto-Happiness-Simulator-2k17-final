label to_mountain_haven:

    you "So, are you headed towards Niflheim?"

    "You can't imagine why anyone would be out here if they weren't either coming or going from the damn place."

    show prompto semidowncast
    with dissolve

    prompto "Yeah. I guess."

    "He doesn't seem keen to reveal any more at this stage."

    #if he has a low happiness rating:
    if happiness >= 4:
        show prompto downcastsmile
        with dissolve
        "But he does seem to have perked up a bit. Perhaps you've made a good impression?"
    elif happiness >= 3:
        "He still seems awfully sad."
    elif happiness <= 2:
        "It seems he doesn't really trust you."

    if happiness >= 4:
        show side prompto downcastsmile:
            alpha 1.0
            time 1.5
            linear 0.5 alpha 0.0
    else:
        show side prompto semidowncast:
            alpha 1.0
            time 1.5
            linear 0.5 alpha 0.0

    show prompto dubious_sidecast:
        alpha 0.0
        time 1.5
        linear 0.5 alpha 1.0

    "There's a sound on the horizon like a gunshot. {alpha=0.0}ooooooooooooooooooooooooooooooooooooo{/alpha}{nw}" # 3.5 second delay

    "There's a sound on the horizon like a gunshot.{fast} Prompto flinches."

    "You snap to attention, fearing it may be some of those troopers Prompto has been running from.{p=0.5}But it's just thunder."

    prompto "I sure don't like the look of those snow clouds."

    you "Come on. We should get going before nightfall. The daemons are pretty rough in these parts, and we don't want to get caught up in a storm too."

    show prompto dubious
    with dissolve

    "He nods."

    prompto "You... probably know this land better than I do. Got any ideas?"

    "You point at the distant mountains."

    #cut to view of mountains for a bit
    scene bg distant_mountain
    with dissolve

    pause 0.5

    you "There's a haven way over in those mountains."

    scene bg snowy_plains

    show prompto surprised
    with dissolve

    prompto "It's safe?"

    you "Yeah, the military don't use it; they prefer their dropships. It's just for pilgrims, really."

    show prompto dubious
    with dissolve

    "He considers."

    prompto "Okay. Let's go."

    scene bg plains_with_mountain
    with dissolve

    if happiness <= 2:

        jump nofood

    if happiness >= 3:

        show prompto downcastsmile
        with dissolve

        "You both start the long trek towards the mountains. The snowy plains don't seem nearly as isolating now that you're walking with him."

        "And he seems happy to have company - or so the contented smile plastered across his face would indicate."

        "You remember you have food in your rucksack.{p=0.5}You fumble about, and pull out..."

        menu:

            "A trail bar":

                jump trailbar

            "A tangerine":

                jump tangerine

            "Candy":

                jump candy

label trailbar:

    "Prompto's eyes widen."

    show prompto lightlaugh
    with dissolve

    prompto "Ooh, an energy bar!"

    $ happiness += 2

    show expression Text("Happiness increased!",
    size=35,
    yalign=0.5,
    xalign=0.5,
    drop_shadow=(1, 1),
    color="#fff",
    outlines=[ (8, "#efefef", 0, 0), (2, "#323345", 0, 0) ]
    ) as text
    with dissolve

    pause 0.5

    hide text
    with dissolve

    you "Sort of. It's a trail bar. You're not allergic to nuts, are you?"

    "His response is to chuckle and take the bar, beaming all the while."

    show prompto widelaugh
    with dissolve

    "He bites into the bar delightedly."

    prompto "Mmm! Protein, energy, yeah - everything the body needs!"

    you "Perfect for a hike."

    prompto "Yeah!"

    "You pull out a bar for yourself, and together you cross the snowy plains, talking and joking as you go."

    jump human

label tangerine:

    show prompto dubious
    with dissolve

    "He eyes the fruit suspiciously."

    prompto "I... don't really like tangerines."

    prompto "Besides, gloves."

    "He holds his gloved hands out, waving them about to illustrate what he means."

    "Good point. You don't want to risk either of you getting frostbite."

    show prompto neutralsmile
    with dissolve

    prompto "Thanks for the offer, though. Maybe when we're stopped. Fruit's actually a super good idea. Vitamins, and stuff, y'know."

    $ happiness += 1

    show expression Text("Happiness increased... slightly",
    size=35,
    yalign=0.5,
    xalign=0.5,
    drop_shadow=(1, 1),
    color="#fff",
    outlines=[ (8, "#efefef", 0, 0), (2, "#323345", 0, 0) ]
    ) as text
    with dissolve

    pause 0.5

    hide text
    with dissolve

    you "Yeah, that's why I picked it. Maybe later, then?"

    "He nods, and you both continue on your way."

    jump human

label candy:

    show prompto frightened_tightlipped
    with dissolve

    "He looks at the candy wistfully. You spot some deep internal struggle going on."

    show prompto frightened_sidecast
    with dissolve

    prompto "I really shouldn't.{p=0.5}Sorry."

    $ happiness += 0

    show expression Text("No increase in happiness",
    size=35,
    yalign=0.5,
    xalign=0.5,
    drop_shadow=(1, 1),
    color="#fff",
    outlines=[ (8, "#efefef", 0, 0), (2, "#323345", 0, 0) ]
    ) as text
    with dissolve

    pause 0.5

    hide text
    with dissolve

    "You feel a little guilty, although his avoidance is not something you could have predicted.{p=0.5}Your eyes search his for answers, but he shies away."

    "You leave the subject alone, and, somewhat reluctantly, stuff the candy back into your bag."

    show prompto frightened_tightlipped
    with dissolve

    jump human

label nofood:

    show prompto dubious
    with dissolve

    "You both start the long trek towards the mountains. The snowy plains don't seem nearly as isolating now that you're walking with him. Surely he feels the same, because although he's guarded, hand hovering near his gun, he still asked you to join him."

    "You remember you have food in your rucksack."

    you "I have some trail food, if you're hungry."

    prompto "Ah... no, thanks."

    jump human
