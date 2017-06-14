label inside_haven:

    stop sound fadeout 1.0

    hide snow with dissolve
    $ show_snow = False

    scene bg cavern
    with dissolve

    "The entrance to the haven is frosted and slippery, but once you're both inside, the air feels drier, and you both relax noticeably."

    show prompto lightlaugh
    with dissolve

    prompto "Hah, we got here just in time, look."

    "Behind you, the sun has finally sunk from sight. There's not a single light in the valley. Here, with the glow of the haven around you, the world feels softer."

    "You put down your pack and immediately see to getting a fire going."

    "Prompto seems keen to help out, and soon you have a small campfire set up in the cozy confines of the cavern. There seems to be plenty of room for the smoke to dissipate safely."

    "You boil some water, make some coffee."

    you "Fancy some? It's warm."

    show prompto calmsmile
    with dissolve

    prompto "Sure. I mean, I don't usually like hot drinks but..."

    "He takes a sip."

    show prompto surprised
    with dissolve

    prompto "Ah! It's bitter."

    you "Heh, sorry. I have strong taste in coffee."

    show prompto raisedeyes_closed
    with dissolve

    prompto "But oh, it's so warm, though. Aw yeah, that does the trick."

    "He's taken his gloves off to let the cup's warmth seep through to his fingers more easily."

    you "Hey, we should get some food going."

    show prompto surprised
    with dissolve

    if trailbar_selected == True:

        prompto "You - you mean me, too? You sure, dude? You already gave me that bar, I don't wanna..."

        "You cut in."

    else:

        prompto "You - you mean me, too?"

    you "Of course."

    prompto "Ah! Thank you. I really mean it - you might have guessed, but I didn't exactly have time to grab any supplies."

    "You already figured this, so you nod, and tell him it's really no problem. Then you open your bag, take out your food rations."

    if tangerine_selected == True:

        "You chuck the aforementioned tangerine back his way."

        you "In case you wanted it. You mentioned earlier..."

        prompto "Hah, yeah. Thanks!"

        "He unpeels the fruit, leans back against the cavern wall, and relaxes. After a while, he asks."

    else:

        "While you fish out some packets of instant soup, Prompto leans back against the cavern wall and asks."

    jump valley

label valley:

    show prompto dubious
    with dissolve

    prompto "So tell me something about this place. You must know a lot, if you're on the pilgrimage."

    you "Well, this mountain range isn't particularly special. Beyond it is said to be Shiva's domain."

    you "The valley we just crossed is the Valley of Saint Lucis."

    show prompto surprised
    with dissolve

    prompto "What, really? Saint? That doesn't make much sense..."

    you "Yeah, it sounds weird at first. Hardly anyone calls it that any more, though. It's an old name."

    prompto "Why out here, though? The name Lucis is an Insomnian thing."

    you "Eh, apparently they called the first King of Lucis a saint, not long after Solheim fell. He was a healer too, or something."

    you "Not many records of that any more, though. I just know what my parents told me, really. They were scholars, so they knew more than your average folk."

    you "I don't keep track beyond that. I just follow the Oracle's teachings."

    play sound breath_in noloop

    show prompto frightened
    with dissolve

    "Prompto's breath catches in his throat."

    prompto "About that... Have you heard? About Lady Lunafreya?"

    "When he speaks her name it's a little stilted, as if she were a dear friend.{p=0.5}You know everyone can get like this over celebrities, but in this boy's case you get the feeling it's a lot more than that."

    you "I heard while I was in Tenebrae. It's terribly sad."

    show prompto frightened_tightlipped
    with dissolve

    "He agrees, and returns to his coffee."

    prompto "I wanted to go see her wedding dress. They'd put it on display in Altissia but we - we didn't have time in the end. My friend, he had to..."

    prompto "Gods, I miss him."

    jump campfire_comfort


label camera_ask:

    menu:

        "Mention the camera":

            jump camera

        "Leave it. There may be sad memories attached":

            jump valley


label camera:

    "You think now is probably a good time to change the subject."

    you "Hey, is that a camera?"

    you "Maybe you should take a photo now."

    prompto "Oh, you mean, like a selfie?"

    you "Why not?"


label campfire_comfort:

    you "This friend have a name?"

    show prompto surprised
    with dissolve

    prompto "Yeah. Noctis."

    you "Oh, like the Insomnian prince?"

    show prompto dubious
    with dissolve

    "He nods, a little too anxiously. You suspect but say nothing."

    you "Popular name, these days. He from Leide or something?"

    show prompto surprised
    with dissolve

    prompto "Y-yeah."

    "He's a terrible liar, but a cute one.{p=0.5}With this inadvertent revelation, you understand a bit more about why the soldiers may be after him."

    "Noctis. Lady Lunafreya. The promise of a marriage. You remember the news reports - you know what happened in Altissia. This poor kid, he must have seen a lot."

    "However he became separated from Noctis in Cartanica, it's clear he's shouldering a lot of the blame for what must be a tricky situation."

    you "Can I just say one thing?"

    prompto "Sure."

    you "Your friend, Noctis. He's really lucky to have someone like you."

    prompto "You... you really mean that?"

    you "Of course I do."

    "He may not be aware of it himself, but he's leaned forwards slightly as you've been speaking."

    if already_hugged == True:

        menu:

            "Hug him again":

                jump end

            "Keep your distance":

                jump end_nohug
    else:

        menu:

            "Hug him again":

                jump end

            "Keep your distance":

                jump end_nohug


label end:

    scene bg cavern

    if already_hugged == True:

        "You surprise him with another hug. You haven't even given yourself time to think. It just felt right."

    else:

        "You surprise him with a hug. You haven't even given yourself time to think. It just felt right."

    you "Whatever's happened, you didn't deserve it. Neither you nor your friend."

    show prompto raisedeyes_closed
    with dissolve

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

    "He hugs back, grips your shoulders."

    prompto "Thank you. Really, I mean it."

    show prompto sadsmile
    with dissolve

    "When he breaks from the embrace, his eyes are misty. But he's happy, and gods, you wish he could look that way forever."

    "You're glad you met him."

    "You made his day somewhat brighter, and for that you're grateful."

    "You smile at each other, both glad to have such good company, as the day fades slowly into night."

    $ show_happiness = False

    $ quick_menu = False

    stop music fadeout 3.0

    $ renpy.pause(3.0, hard = True)

    play music "sound/credits.wav" fadein 3.0

    scene bg cavern

    show prompto sadsmile

    menu:

        ".":

            jump credits



label end_nohug:

    "You don't want to push your luck by hugging him again, no matter how much he looks like he needs it."

    "So you stay your ground, and carry on tending to the fire."

    show prompto calmsmile
    with dissolve

    prompto "Thank you for saying those things. Really, I mean it."

    "He seems calmer now. Much more so than when you first met him, out on the snow field."

    "But if you could change anything, you'd wish he was a little happier. If only you could do it all again."

    "But for now, he is content."

    $ show_happiness = False

    $ quick_menu = False

    $ results = True

    stop music fadeout 3.0

    $ renpy.pause(3.0, hard = True)

    play music "sound/credits.wav" fadein 3.0

    scene bg cavern

    show prompto calmsmile

    menu:

        ".":

            jump credits
