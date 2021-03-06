label what_happened:

    you "It's awfully cold out here..."

    "Talking about the weather{p=0.5}. . . {p=0.5}smooth going."

    "Then you remember something."

    "The group of soldiers you saw earlier ... they'd been headed in the same direction as him."

    show prompto surprised
    with dissolve

    you "Did you see the Magitek Troopers come this way?"

    play sound breath_in noloop

    show prompto frightened
    with dissolve

    "He starts trembling.{p=0.5}This is when you notice the gun. It's stuffed carelessly into his pocket, like he's trying to ignore its presence."

    show prompto frightened_tightlipped
    with dissolve

    "You can't not ask, at this point."

    you "What exactly happened here?"

    "You keep your voice level, but you make a point of looking at the gun."

    show prompto frightened
    with dissolve

    prompto "Oh, uh ... "

    show prompto frightened_sidecast
    with dissolve

    "He falters, plays with the gun idly, although he makes no attempt to cock it."

    show prompto regrets
    with dissolve

    prompto "{i}I don't know why he let me have this back.{/i}"

    "Who is 'he', you wonder.{p=0.5}Suddenly you're not worried about whether the gun really belongs to this young man.{p=0.5}You're more worried about whoever gave it to him."

    "You're overcome with the urge to protect him."

    show prompto frightened_sidecast
    with dissolve

    "He wrestles with his thoughts for a while. You're tempted to reach out to him, but it's best not to frighten him while he's holding the weapon.{p=0.5}Just in case."

    "The air feels suddenly bitter. Feels like there's eyes everywhere. Perhaps his jumpiness is rubbing off on you?"

    show prompto dubious
    with dissolve

    "But it soon subsides. The moment over, he tucks the weapon back into his pocket, and raises his eyes to yours once more."

    show prompto surprised
    with dissolve

    prompto "I'm not planning on using it. Unless those soldiers come back."

    show prompto dubious
    with dissolve

    you "Hey, I'm not scared.{p=0.5}Just... worried, I guess. I mean, when I saw the Magitek troopers further down the valley, I wondered what was going on. This is the middle of nowhere."

    show prompto surprised
    with dissolve

    prompto "Did they see you come this way?"

    you "No, I hid. I don't have any weapons on me."

    "You look from his eyes to the gun and back again."

    you "Can I tag along with you? At least for the time being."

    prompto "Sure. I mean, it'd be nice to have company."

    "He pauses."

    show prompto sadsmile
    with dissolve

    prompto "I'm Prompto, by the way. Nice to meet you."

    $ prompto_name = "Prompto"

    "You introduce yourself."

    jump setname

label setname:

    python:
        your_name = renpy.input("Type in your name.")
        your_name = your_name.strip()
        if not your_name:
            your_name = "Ilia"
    "[your_name], is that right?"

label justtobesure:

    menu:
        "Yes":
            jump after_user_name_set
        "No":
            $ your_name = ""
            jump setname

label after_user_name_set:

    "He nods as you speak your name."

    prompto "[your_name]. That's a real nice name. So, you wanted to know what happened, huh?"

    "You nod."

    you "Yeah, if it's not too much bother."

    show prompto raisedeyes
    with dissolve

    "He raises his eyes to the sky. The sun is pale and the way it glints off his hair reminds you of catkins in spring. He looks positively angelic, but whatever he's thinking about is clearly not."

    prompto "Oh gods, where do I begin?{p=0.5}What's happening ... it feels like it's all my fault."

    "You wait patiently for him to continue.{p=0.5}Your toes feel more frozen than ever, even through your thick boots, but you don't shift. You don't want to stop him now."

    prompto "My friends and I, we got... separated, in Cartanica. Those Magitek Troopers attacked the train we were on. And now they're after me."

    "He sighs."

    show prompto raisedeyes_closed
    with dissolve

    prompto "I've been out here for days with nobody to talk to."

    prompto "I mean, you're real, aren't you? You're not just another hallucination?"

    show prompto downcastsmile
    with dissolve

    "He pauses, chuckles to himself."

    prompto "'Course, a hallucination's bound to say they're not anyway. Stupid question. Sorry."

    "You wonder briefly if he is crazy.{p=0.5}Again, he seems cogent enough, and he's awfully sweet. But kindness is a rare thing in this world, and it's hard not to see it as a little suspect."

    "You were brought up following the word of the Oracle, though, and you believe in compassion above all else. Anyone who has cause to doubt what they see with their own two eyes, no matter the reason, must be in need of reassurance."

    "But what can you say to make him believe you're real?"

    menu:

        "I'm not a hallucination.":

            jump deny_hallucination

        "(How am I supposed to respond to this?) ... ":

            jump keep_silent

        "Oh sure, I'm totally a figment of your imagination.":

            jump agree_hallucination

label deny_hallucination:

    show prompto semidowncast
    with dissolve

    "It's exactly what he said a hallucination would say, but you say it anyway."

    "Luckily, you manage to speak sincerely enough that, after a moment, he noticeably calms down."

    show prompto downcastsmile
    with dissolve

    prompto "Hah, well, even if you are, at least you're nice."

    $ happiness += 1

    show expression Text("Happiness increased",
    size=35,
    yalign=0.5, # Centers the text -- Toward Bottom.
    xalign=0.5, # Centers the text -- Toward Right.
    drop_shadow=(1, 1),
    color="#fff",
    outlines=[ (8, "#efefef", 0, 0), (2, "#323345", 0, 0) ]
    ) as text
    with dissolve

    pause 0.5

    hide text
    with dissolve

    "You haven't managed to completely convince him, but you suppose there's only so much you can do. You decide to let him lead the conversation from here."

    show prompto dubious
    with dissolve

    "Prompto studies you with curiosity, trying to figure out how you fit in with this environment. He seems as confused by you as you are by him."

    jump niflheim

label keep_silent:

    "Your silence doesn't go down well."

    show prompto dubious
    with dissolve

    "He watches you anxiously."

    prompto "Sorry. I just made things awkward, didn't I? Ah, forget it."

    $ happiness += 0

    show expression Text("No increase in happiness",
    size=35,
    yalign=0.5, # Centers the text -- Toward Bottom.
    xalign=0.5, # Centers the text -- Toward Right.
    drop_shadow=(1, 1),
    color="#fff",
    outlines=[ (8, "#efefef", 0, 0), (2, "#323345", 0, 0) ]
    ) as text
    with dissolve

    pause 0.5

    hide text
    with dissolve

    "You try to apologise, or think of something to say that will fix the situation. But he's already moved on."

    jump niflheim

label agree_hallucination:

    show prompto surprised
    with dissolve

    "Prompto stares at you for a second."

    show prompto widelaugh
    with dissolve

    prompto "Hah! Dude, you almost had me there."

    "At first the sound of his laughter is a shock amid the silence of the snowdrifts. It's so light and so pure you find yourself quite drawn to it."

    "He eventually stops and raises his eyes, beaming your way."

    show prompto lightlaugh
    with dissolve

    prompto "No hallucination would {i}ever{/i} say that!"

    $ happiness += 2

    show expression Text("Happiness increased!",
    size=35,
    yalign=0.5, # Centers the text -- Toward Bottom.
    xalign=0.5, # Centers the text -- Toward Right.
    drop_shadow=(1, 1),
    color="#fff",
    outlines=[ (8, "#efefef", 0, 0), (2, "#323345", 0, 0) ]
    ) as text
    with dissolve

    pause 0.5

    hide text
    with dissolve

    "You smile back, glad your dumb gambit paid off. It feels like the two of you have a lot in common."

    you "Haha, yeah. I'm just a really good one, I guess!"

    "Then you scuff the toe of one boot lightly in the snow."

    you "But seriously, I've been travelling alone for days, too. I get it. At least, a little."

    prompto "Man, I can't even begin to describe just how much better that makes me feel."

    show prompto dubious
    with dissolve

    "He looks at you, studies you, a question dancing on his lips.{p=0.5}Finally, he asks."

    jump niflheim
