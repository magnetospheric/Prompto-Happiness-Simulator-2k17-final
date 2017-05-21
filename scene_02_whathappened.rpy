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

    "Who is 'he', you wonder. His words indicate that the gun belongs to him. But he doesn't look the dangerous type. You're more worried about whoever gave the gun back to him."
    "Suddenly you're overcome with the urge to protect him."

    prompto "I'm not planning on using it. Unless those soldiers come back."

    "\"Hey, I'm not scared,\" you say. \"Just... worried, I guess. I saw the Magitek troopers further down the valley."

    prompto "Did they see you come this way?"

    "\"No, I hid. I don't have any weapons on me.\""

    "\"Can I tag along with you?\""

    prompto "Sure, I mean. It'd be nice to have company."

    prompto "You wanted to know what happened, huh?"

    "\"If you don't mind. I just want to know what \""

    "He raises his eyes to the sky"

    prompto "Oh gods, where do I begin. What's happening ... it feels like it's all my fault."

    prompto "I mean, you're real, aren't you. You're not just another hallucination?"

    show prompto sadlaugh
    with dissolve

    "He pauses, chuckles to himself."

    prompto "'Course, a hallucination's bound to say they're not anyway. Stupid question. Sorry."

    "You wonder briefly if he is mad. Again, he seems cogent enough, and he seems sweet. But kindness is a rare thing in this world, and it's hard not to see it as even a little suspicious."

    "You were brought up following the word of Oracle, though, and while your first instinct is to be suspicious, your belief in compassion overrides it. Anyone who has cause to doubt what they see with their own two eyes, no matter the reason, must be feeling frightened."

    menu:

        "I'm not a hallucination.":

            jump deny_hallucination

        "(How am I supposed to respond to this?) ... ":

            jump keep_silent

        "Oh sure, I'm totally a figment of your imagination.":

            jump agree_hallucination

label deny_hallucination:

    "You speak sincerely enough that he noticeably calms down."

    $ happiness += 1

    show prompto relievedsmile
    with dissolve

    jump niflheim

label keep_silent:

    $ happiness += 0

    show prompto relievedsmile
    with dissolve

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
