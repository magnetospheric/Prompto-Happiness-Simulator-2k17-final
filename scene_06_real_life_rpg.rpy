label real_life_rpg:

    "You're almost at the foot of the mountains now. Here, the snowdrifts run so deep you both sink in almost to your knees."

    if happiness > 4:

        "At first, Prompto laughs. But after a while the difficult terrain starts to get the better of you both."

    "Soon the frustration leads both of you to curse and stumble."

    show prompto dubious
    with dissolve

    prompto "Ugh, this is a total mess."

    prompto "You know, all those times when I said this was like a real-life RPG, I didn't actually expect it to have a, y'know, major character death. Or a deep backstory arc. Where you find out the character's tragic past or whatever. It's not fun when it happens to you."

    show prompto calmsmile
    with dissolve

    "He smiles, and blinks the tears away from his eyes."

    prompto "Yeah, I enjoy this stuff so much better in video games. Right now, it's just ... depressing."

    show prompto resigned
    with dissolve

    prompto "I probably sound like a stuck record by now, but ... I didn't want any of this to happen."

    "He looks pretty upset. It's clear he's blaming himself. You know this is the perfect moment to do something, so you..."

    menu:

        "Hug him":

            jump hug

        "Tell him everything will be okay":

            jump comfort

        "Crack a joke":

            jump joke

        "Stand there awkwardly":

            jump no_hug


label hug:

    "You stop moving forward."

    show prompto surprised
    with dissolve

    you "Hey."

    "You don't speak harshly at all, but the urgency in your voice makes him stop too."

    you "You don't sound like a stuck record."

    "And you hug him tight. Your hands are in a non-threatening position across his back and shoulders, and you simply focus on pouring out compassion, ready to stop should he give any indication he's uncomfortable. You barely know this man, but you can't stand to see him beat himself up."

    show prompto raisedeyes_closed # need eyesclosed version
    with dissolve

    "He leans into the hug."

    "You think you detect a slight sniffle as he buries his face in the crook of your shoulder. He seems to really appreciate the physical contact."

    $ happiness += 3

    show expression Text("Happiness increased a lot!",
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

    show prompto neutralsmile
    with dissolve

    "When he breaks contact, his eyes are a little misty, but he's happy."

    prompto "Whew! Uh, that wasn't what I expected, but it... it was nice. Thanks."

    you "Hey, no problem - I just hope it helped."

    jump continue_to_cavern


label comfort:

    you "It's clear you're doing your best. And that's all a friend could ask for."

    show prompto dubious_sidecast
    with dissolve

    prompto "I suppose..."

    "He doesn't look entirely convinced."

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

    jump continue_to_cavern


label joke:

    you "You know, if it's a real life RPG, then the hero always prevails. Right?{p=0.5}And every adventurer who gets separated from their friends {i}always{/i} gets reunited with them again."

    show prompto lightlaugh
    with dissolve

    prompto "Hah! I guess."

    prompto "Still don't think I've levelled up enough for this, though."

    you "Means you get more EXP, right?"

    show prompto widelaugh
    with dissolve

    "He chuckles."

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

    prompto "Aw man, we'd better get extra points for this terrain."

    jump continue_to_cavern


label no_hug:

    "You stand and stare, making no move to console him."

    prompto "I'm sorry. I'm sorry, this is... I'm just making things worse..."

    show prompto frightened_tightlipped
    with dissolve

    "He sniffs."

    prompto "I should go."

    if happiness <= 3:

        "He walks away."

        prompto "I'll find my way to Niflheim on my own. Please don't follow me."

        # need an image of his back here

        "You're left staring after him. His silhouette cuts a lonely figure against the snowy plains."

        "You call out, say something about how it isn't his fault, how you didn't mean to make him sad, but he's no longer listening."

        "Soon you can't see him at all."

        "The wind chill increases. You gather your clothes closer about you, and trudge off once more into the wilderness."

        return

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

    you "No, please don't! I'm the one who's sorry, I'm not very good at this comforting thing."

    prompto "Well... if you say so."

    jump continue_to_cavern


label continue_to_cavern:

    you "Let's keep going, then. We're almost there."

    # would be neat to have art of the mountainside here

    "You point at the mountainside. There's a small cavern that can be seen, and inside, the faint glow of blue protective glyphs. The haven awaits."

    show prompto calmsmile
    with dissolve

    "Prompto smiles, and sings jauntily as you both tackle the remaining snowdrifts separating you from the cavern."

    prompto "{i}There's no business like snow business!{/i}"

    "It's a variation on a musical number you remember seeing once in Tenebrae. You remember the film was about a sharpshooter, and you find it kind of cute, all things considered, that he'd be singing it."

    "He trails off, and you remember the next lines, and you don't supply them, although the words ring in your head just the same.{p=0.5}{i}Ain't no people like show people, they smile when they are low.{/i}"

    if happiness <= 4:

        "His attempts to lighten the mood are working; you feel your heart warm to him."

        "How can he stand being so nice when you've not exactly been comforting?"

    else:

        "The mood feels considerably lighter, however, and time seems to pass quickly."
