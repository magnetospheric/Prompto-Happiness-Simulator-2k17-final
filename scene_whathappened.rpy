label what_happened:

    "\"It's awfully cold out here,\" you say. Talking about the weather ... smooth going."

    "Then you remember something. The group of soldiers you saw earlier. They'd been headed in the same direction as him."

    "\"Did you see the Magitek soldiers come this way?\""

    show prompto frightened
    with dissolve

    "He starts trembling. This is when you notice the gun. It's stuffed carelessly into his pocket, like he's trying to ignore its presence."

    "\"What exactly happened here?\" You keep your voice level, but you make a point of looking at the gun."

    prompto "Oh, uh ... "

    show prompto scrutinisinggun
    with dissolve

    prompto "*whispers*  I don't know why he let me have this back."

    show prompto regrets
    with dissolve

    prompto "Oh gods, where do I begin. What's happening ... it feels like it's all my fault."

    prompto "I mean, you're real, aren't you. You're not just another hallucination?"

    show prompto sadlaugh
    with dissolve

    "He pauses, chuckles to himself."

    prompto "'Course, a hallucination's bound to say they're not anyway. Stupid question. Sorry."

    menu:

        "I'm not a hallucination.":

            jump deny_hallucination

        "(How am I supposed to respond to this?) ... ":

            jump keep_silent

        "Oh sure, I'm totally a figment of your imagination.":

            jump agree_hallucination

label deny_hallucination:

    "You speak sincerely enough that he noticeably calms down."

    jump niflheim

label keep_silent:


    jump niflheim

label agree_hallucination:

    "Prompto stares at you for a second."

    prompto "Hah! Dude, you almost had me there."

    show prompto sadlaugh
    with dissolve

    "At first the sound of his laughter is a shock amid the silence of the snowdrifts. It's so light and so pure you find yourself drawn to it."

    ""

    prompto "No hallucination would EVER say that!"

    $ happiness += 2

    show prompto relievedsmile
    with dissolve

    jump niflheim
