label what_happened:

    "\"It's awfully cold out here,\" you say. Talking about the weather ... smooth going."

    "Then you remember something. The group of soldiers you saw earlier. They'd been headed in the same direction as him."

    "\"Did you see the Magitek Troopers come this way?\""

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

    "\"Hey, I'm not scared,\" you say. \"Just... worried, I guess. I mean, when I saw the Magitek troopers further down the valley, I wondered what was going on. This is the middle of nowhere.\""

    prompto "Did they see you come this way?"

    "\"No, I hid. I don't have any weapons on me.\" You look from his eyes to the gun and back again. \"Can I tag along with you?\""

    prompto "Sure. I mean, it'd be nice to have company."

    "He pauses."

    prompto "I'm Prompto, by the way. Nice to meet you."

    $ prompto_name = "Prompto"

    "You introduce yourself, and he nods as you speak your name."

    prompto "That's a real nice name. So, you wanted to know what happened, huh?"

    "You nod."

    show prompto pensiveraisedeyes
    with dissolve

    "He raises his eyes to the sky. The sun is pale and the way it glints off his hair reminds you of catkins in spring. He looks positively angelic, but whatever he's thinking about is clearly not so."

    prompto "Oh gods, where do I begin. What's happening ... it feels like it's all my fault."

    "You wait patiently for him to continue. Your toes feel more frozen than ever, even through your thick boots, but you don't shift. You don't want to stop him now."

    prompto "My friends and I, we got... separated, in Cartanica. Those Magitek Troopers attacked the train we were on. And now they're after me."

    "He sighs."

    prompto "I've been out here for days with nobody to talk to."

    prompto "I mean, you're real, aren't you? You're not just another hallucination?"

    show prompto sadlaugh
    with dissolve

    "He pauses, chuckles to himself."

    prompto "'Course, a hallucination's bound to say they're not anyway. Stupid question. Sorry."

    "You wonder briefly if he is crazy. Again, he seems cogent enough, and he's awfully sweet. But kindness is a rare thing in this world, and it's hard not to see it as a little suspect."

    "You were brought up following the word of Oracle, though, and you believe in compassion above all else. Anyone who has cause to doubt what they see with their own two eyes, no matter the reason, must be in need of reassurance."

    "But what can you say to make him believe you're real?"

    menu:

        "\"I'm not a hallucination.\"":

            jump deny_hallucination

        "(How am I supposed to respond to this?) ... ":

            jump keep_silent

        "\"Oh sure, I'm totally a figment of your imagination.\"":

            jump agree_hallucination

label deny_hallucination:

    "It's exactly what he said a hallucination would say, but you say it anyway. Luckily, you speak sincerely enough that he noticeably calms down."

    show prompto relievedsmile
    with dissolve

    prompto "Hah, well, even if you are, at least you're nice."

    $ happiness += 1

    "You haven't managed to completely convince him, but you suppose there's only so much you can do. You decide to let him lead the conversation from here."

    "Prompto studies you with curiosity, trying to figure out how you fit in with this environment. He seems as confused by you as you were by him."

    jump niflheim

label keep_silent:

    show prompto neutralsmile
    with dissolve

    prompto "Sorry. I just made things awkward, didn't I? Ah, forget it."

    $ happiness += 0

    "You try to apologise, or think of something to say that will fix the situation. But he's already moved on."

    jump niflheim

label agree_hallucination:

    "Prompto stares at you for a second."

    show prompto laugh
    with dissolve

    prompto "Hah! Dude, you almost had me there."

    "At first the sound of his laughter is a shock amid the silence of the snowdrifts. It's so light and so pure you find yourself quite drawn to it. He eventually stops and es his eyes, beaming your way."

    show prompto relievedsmile
    with dissolve

    prompto "No hallucination would {i}ever{/i} say that!"

    $ happiness += 2

    "You smile back, glad your dumb gambit paid off. It feels like the two of you have a lot in common."

    "\"Haha, yeah. I'm just a really good one, I guess!\" Then you scuff the toe of one boot lightly in the snow. \"But seriously, I've been travelling alone for days, too. I get it. At least, a little.\""

    prompto "Man, I can't even begin to describe how much that makes me feel better."

    "He looks at you, studies you, a question dancing on his lips. Finally, he asks."

    jump niflheim
