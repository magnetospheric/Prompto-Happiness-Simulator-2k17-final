#### Game Start ####

#testing
label start:

    # TESTING NIFLHEIM #
    # set my starting variables:
    $ happiness = 4

    $ show_happiness = True

    $ prompto_name = "Prompto"
    $ your_name = "You"

    scene bg snowy_plains

    show prompto dubious
    with dissolve

    jump niflheim

label start01:

    # set my starting variables:
    $ happiness = 2

    $ show_happiness = False

    $ prompto_name = "Stranger"
    $ your_name = "You"

    # set the scene
    scene bg snowy_plains
    with fade

    # have some snowflake effects cross the screen

    "Nothing but endless snow for miles."

    "You've been walking for such a long time you can't feel your toes any more in your thick winter boots.{p=0.5}There's just the monotonous crunch-crunch-crunch of your footsteps on packed-down snow."

    "The sun is high, reflecting on the crystalline ground, and at first you think you're all alone, but then you spot a figure moving amid the distant sunlit shimmers."

    "Another person?"

    "Who could be out here?{p=0.5}Are they also on a pilgrimage?"

    "You pick up speed, anxious to talk to another human being.{p=0.5}The route from Tenebrae to Gralea is long and lonely for those not taking the train."

    show prompto downcast at left
    with dissolve

    "The figure is that of a young man. Striking blond hair pokes out from under a warm woollen cap to glint in the sunlight. He's swamped in a bulky winter coat that makes his legs look stick-thin beneath it."

    "It looks like he's lost in thought.{p=0.5}But from this distance, you can't really tell.{p=0.5}You approach slowly."

    you "Hi."

    show prompto surprised at left
    with dissolve

    prompto "Oh! I ... I didn't expect to see anyone else out here."

    prompto "A-are you okay?"

    "Why is he asking how I am?{p=0.5}He's clearly the one who's not okay."

    menu:

        "Apologise for surprising him":

            jump apology

        "Ask if he's okay instead":

            jump console

        "Ask how he got here":

            jump pragmatic

label apology:

    you "Sorry for startling you like that."

    prompto "Oh, no, really. It's okay."

    you "No, I should have called out earlier or something."

    show prompto sadsmile
    with dissolve

    $ show_happiness = True

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

    "He smiles, but his expression is sad, like he recognises what you're doing."

    prompto "You don't need to blame yourself. Seriously."

    "So he says, but he clearly looks like he appreciates it.{p=0.5}He looks a little more relaxed now, and you're pleased to see it, but you're now even more worried at what he could be doing out here all alone."

    "You want to ask him, but you don't want to make him uncomfortable."

    "Maybe a change of topic would be better?"

    jump what_happened

label console:

    you "Hey, don't worry about me. Honestly, I'm more concerned about you. You look a bit ... upset."

    prompto "M-me? Oh, uh ... "

    show prompto semidowncast
    with dissolve

    "He averts his gaze again, gripping his arm hard like he's testing he's real."

    prompto " ... I'm fine. I guess."

    "You get the impression he doesn't like the spotlight being focussed so intently on him.{p=0.5}But he at least seems a little bit happy that you cared."

    show prompto downcastsmile
    with dissolve

    $ show_happiness = True

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

    prompto "Thanks for asking."

    "You decide to change the subject slightly. Focus on the world around you."

    jump what_happened

label pragmatic:

    you "How did you get here?"

    "He looks wary."

    prompto "I'm sorry. I don't really know you. So, uh..."

    prompto "I mean, you get it, right?"

    $ show_happiness = True

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

    "You think you understand.{p=0.5}But it does make you wonder all the more what could have happened."

    "Either way, it seems you've made him uncomfortable."

    "Perhaps it's time to change the subject."

    jump what_happened
