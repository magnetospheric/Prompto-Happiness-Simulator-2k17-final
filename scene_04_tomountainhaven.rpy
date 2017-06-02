label to_mountain_haven:

    you "So, are you headed to Niflheim or something?"

    "You can't imagine why anyone would be out here if they weren't."

    prompto "Yeah. I guess."

    "He doesn't seem keen to reveal any more at this stage."

    #if he has a low happiness rating:
    if happiness >= 4:
        "But he does seem to have perked up a bit. Perhaps you've made a good impression?"
    elif happiness >= 3:
        "He still seems awfully sad."
    elif happiness <= 2:
        "It seems he doesn't really trust you."

    you "Come on. We should get going before nightfall. The daemons are pretty rough in these parts.{p=0.5}There's a haven way over in those mountains."

    prompto "It's safe?"

    you "Yeah, the military don't use it. It's just for pilgrims, really."

    "He considers."

    prompto "Okay. Let's go."

    #cut to view of mountains for a bit

    if happiness <= 2:

        jump nofood

    if happiness >= 3:

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

    "Prompto's eyes light up."

    show prompto lightlaugh
    with dissolve

    prompto "Ooh, an energy bar!"

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

    "He eyes the fruit suspiciously."

    prompto "I... don't really like tangerines."

    prompto "Besides, gloves."

    "He holds his gloved hands out, waving them about to make the point."

    "Good point. You don't want to risk either of you getting frostbite."

    prompto "Thanks for the offer, though. Maybe when we're stopped. Fruit's actually a super good idea. Vitamins, and stuff."

    you "Yeah, that's why I picked it. Maybe later, then?"

    "He nods, and you both continue on your way."

    jump human

label candy:

    "He looks at the candy wistfully. You spot some deep internal struggle going on."

    prompto "I really shouldn't.{p=0.5}Sorry."

    jump human

label nofood:

    "You both start the long trek towards the mountains. The snowy plains don't seem nearly as isolating now that you're walking with him. Surely he feels the same, because although he's guarded, hand hovering near his gun, he still asked you to join him."

    "You remember you have food in your rucksack."

    you "I have some trail food, if you're hungry."

    prompto "Ah... no, thanks."

    jump human
