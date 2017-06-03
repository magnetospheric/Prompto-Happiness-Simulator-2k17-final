label niflheim:

    prompto "So, your turn. What are you doing here?"

    you "I'm on the pilgrim's trail. I've just been to Tenebrae - now I'm headed back home to Niflheim."

    show prompto semidowncast
    with dissolve

    prompto "Niflheim, huh?"

    "He doesn't sound very enthused."

    menu:

        "Tell him you like Niflheim.":

            jump like_niflheim

        "Express your dissatisfaction with Niflheim.":

            jump hate_niflheim


label like_niflheim:

    you "Yeah - I live in the capital, Gralea. It's pretty nice."

    show prompto dubious
    with dissolve

    prompto "You think?"

    you "Sure, I mean, Niflheim's the strongest military nation on Eos. Rather be there than anywhere else."

    "He looks like he has so many things he wants to say, but he holds his tongue.{p=0.5}His eyes say everything he needs to."

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

    "You consider justifying yourself, but you don't want to upset him any further. An awkward silence falls between you."

    "Eventually you have to ask."

    jump to_mountain_haven


label hate_niflheim:

    you "Yeah... I'm not looking forward to returning."

    show prompto surprised
    with dissolve

    prompto "How come?"

    "It's a loaded question. It's clear he doesn't like the place, but he seems scared of saying so outright."

    you "I don't really like living there, to be honest with you. Especially the capital city, Gralea.{p=0.5}It's overcrowded, and us ordinary citizens are treated, well, little better than machines."

    show prompto sadsmile
    with dissolve

    "He smiles sadly."

    prompto "I know the feeling."

    prompto "I don't like Niflheim either."

    you "I'm glad thats something we have in common."

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

    jump to_mountain_haven
