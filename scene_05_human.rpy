label human:

    if happiness >= 5:
        show prompto downcastsmile
        with dissolve
    else:
        show prompto dubious
        with dissolve

    "The wind blusters about, picking up loose snowflakes and casting them into the air like dice."

    "It's getting colder, and the closer you get to the mountains, the more your cheeks grow numb. Your eyelashes are freezing over. Your face feels ruddy and blistery."

    "Prompto, on the other hand, looks just as angelic as ever. Not even a red flush from the exertion."

    play sound magitek noloop

    pause 0.2

    show prompto dubious_sidecast
    with dissolve

    "A cry issues out on the breeze. You've heard such a thing before, once when you saw a Magitek unit failing."

    "It had been doing its evening patrol in Gralea, and something had gone wrong in its circuitry, presumably.{p=0.5}But you'll never forget how it sounded pained, shrieking like a dying animal."

    "Prompto seems shaken by the noise."

    play sound footsteps loop

    if happiness <= 3:

        "But he says nothing. You walk on together in silence."

        jump real_life_rpg

    else:

        "After a while, he speaks."

        show prompto frightened
        with dissolve

        prompto "Hey."

        "You raise your eyebrows, wait for him to continue."

        prompto "This might sound super weird, but..."

        prompto "Do I look human to you?"

        prompto "Because {i}he's{/i} making me doubt it."

        show prompto frightened_sidecast
        with dissolve

        "He looks off to the side. There's something haunted in the way he does it, like he's expecting shadows round every corner."

        "What an odd question. You don't quite know how to answer it, and in the time you spend deliberating, Prompto continues to talk."

        prompto "He makes me doubt everything."

        "Who is this 'he', you want to ask.{p=0.5}But Prompto isn't focussing; he casts his eyes hopelessly towards the sky."

        show prompto raisedeyes
        with dissolve

        prompto "I just wanted to go on a road trip with my best bud. See him get married, try some gelato in Altissia. Maybe ride a chocobo or two."

        menu:

            "Pester him about the strange man he mentioned.":

                jump ardyn

            "Ask him what his best friend is like.":

                jump noctis

            "Mention you really like chocobos.":

                jump chocobos

label chocobos:

    you "Oh! Chocobos? I {i}love{/i} chocobos."

    show prompto lightlaugh
    with dissolve

    "His face lights up."

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

    prompto "They're the best, huh?"

    "Then he hums a familiar tune. You recognise it as the chocobo song, a nursery rhyme of sorts. It's pretty universal, and you find yourself joining in."

    show prompto widelaugh
    with dissolve

    "He laughs."

    you "You ever ride one?"

    show prompto lightlaugh
    with dissolve

    prompto "Ha! Yeah - just a few times. I went to Wiz's Chocobo Ranch in Duscae before... {p=0.5}Well. It was an awesome place."

    you "That with your friend you mentioned?"

    show prompto dubious
    with dissolve

    "He nods, and his expression turns sad again."

    menu:

        "Ask him what his best friend is like":

            jump noctis

        "Talk more about chocobos instead":

            jump dont_ask

    "Your mind keeps drifting back to that odd question, though. {i}\'Do I look human?\'{/i}{p=0.5}What kind of thing makes a person ask something like that?"

    jump real_life_rpg


label noctis:

    you "This friend you keep talking about. What's he like?"

    "You're hoping that perhaps giving him the chance to open up will help him feel better, but he doesn't seem keen on answering."

    "He plays with the ends of his coat sleeve. It's clear he's thinking hard."

    show prompto dubious_sidecast
    with dissolve

    prompto "I don't think I'm ready to talk about him just yet."

    you "Hey, no worries. I'm sorry I asked."

    show prompto dubious
    with dissolve

    prompto "No, it's okay."

    show prompto calmsmile
    with dissolve

    prompto "I know you meant well."

    $ happiness += 1

    show expression Text("Slight increase in happiness",
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

    jump real_life_rpg

label ardyn:

    you "Who's this \'he\'? This guy making you doubt everything?"

    show prompto frightened_sidecast
    with dissolve

    "He turns awfully silent. The sprinkling sound of snow beneath your feet becomes agonisingly loud."

    show prompto frightened_tightlipped
    with dissolve

    prompto "I {i}really{/i} don't wanna talk about him."

    "He shudders and it's so strong it's like someone's just walked over his grave. Then he blanks you, keeps walking like nothing's happened."

    $ happiness -= 1

    show expression Text("Happiness decreased",
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

    jump real_life_rpg

label dont_ask:

    "You decide it's best not to dredge up the subject of his friend right now."

    "After all, if they really did get separated in Cartanica, he's probably worried sick about him."

    "The last thing he needs is the memory refreshed."

    you "Well, I've never ridden a chocobo. Always wanted to."

    show prompto lightlaugh
    with dissolve

    prompto "Oh! It's super fun. If we ever wind up in Duscae again, I'll show you how it's done."

    you "You'd show me? Really?"

    $ happiness += 1

    show expression Text("Happiness increased",
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

    prompto "Duuude, of course!"

    jump real_life_rpg
