label human:

    "The wind blusters about, picking up loose snowflakes and casting them into the air like dice."

    "It's getting colder, and the closer you get to the mountains, the more your cheeks grow numb. Your eyelashes are freezing over. Your face feels ruddy and blistery."

    "Prompto, on the other hand, looks just as angelic as ever. Not even a red flush from the exertion."

    if happiness <= 3:

        "You walk on together in silence."

        jump final_doubts

    else:

        "After a while, Prompto speaks."

        prompto "Hey."

        "You raise your eyebrows, wait for him to continue."

        prompto "Do I look human to you?"

        prompto "Because {i}he's{/i} making me doubt it."

        "He looks off to the side. There's something haunted in the way he does it, like he's expecting shadows round every corner."

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

    "His face lights up."

    prompto "They're the best, huh?"

    "Then he hums a familiar tune. You recognise it as the chocobo song, a nursery rhyme of sorts. It's pretty universal, and you find yourself joining in."

    "He laughs."

    "Your mind keeps drifting back to that odd question, though. {i}\'Do I look human?\'{/i}{p=0.5}What kind of thing makes a person ask something like that?"

    menu:

        "Mention the camera":

            jump camera

        "Leave it. There may be sad memories attached":

            jump final_doubts

label camera:

    "You think now is probably a good time to change the subject."

    you "Hey, is that a camera?"

    you "Maybe you should "

    prompto "Oh, you mean, like a selfie?"


label final_doubts:

    prompto "You know, all those times when I said this was like a real-life RPG, I didn't actually expect it to have a, y'know, major character death. Or a deep backstory arc. Where you find out the character's tragic past or whatever. It's not fun when it happens to you."

    "He smiles, and blinks the tears away from his eyes."

    prompto "Yeah, I enjoy this stuff so much better in video games. Right now, it's just ... depressing."

    prompto "I probably sound like a stuck record by now, but ... I didn't want any of this to happen."

    "He looks pretty upset..."

    menu:

        "Hug him":

            jump hug

        "Tell him everything will be okay":

            jump comfort

        "Crack a joke":

            jump no_hug

        "Stand there awkwardly":

            jump no_hug

label hug:

    "You stop moving forward."

    "\"Hey.\" You don't speak harshly at all, but the urgency in your voice makes him stop too."

    "\"You don't sound like a stuck record.\" And you hug him tight. Your hands are in a non-threatening position across his back and shoulders, and you simply focus on pouring out compassion, ready to stop should he give any indication he's uncomfortable. You barely know this man, but you can't stand to see him beat himself up."

    "He leans into the hug."

    "You think you detect a slight sniffle as he buries his face in the crook of your shoulder. He seems to really appreciate the physical contact."

    $ happiness += 2

    "When he breaks contact, his eyes are a little misty, but he's happy."

    prompto "Whew! Uh, that wasn't what I expected, but it... it was nice. Thanks."

    menu:

        "Hug him again":

            jump second_hug

        ""

label comfort:

    "It's clear you're doing your best. And that's all a friend could ask for."

    $ happiness += 1

label joke:

    $ happiness += 0

label no_hug:

    $ happiness -= 2
