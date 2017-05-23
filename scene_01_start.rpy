#### Game Start ####

label start:

    # set my starting variables:
    $ happiness = 0

    $ show_happiness=True 

    $ prompto_name = "Stranger"

    # set the scene
    scene bg snowy_plains
    with fade

    # have some snowflake effects cross the screen

    "Nothing but endless snow for miles."

    "You've been walking for such a long time you can't feel your toes any more in your thick winter boots. There's just the monotonous crunch-crunch-crunch of your footsteps on packed-down snow."

    "The sun is high, reflecting on the crystalline ground, and at first you think you're all alone, but then you spot a figure moving amid the distant sunlit shimmers."

    "Who could be out here? \n Are they also on a pilgrimage? \n You pick up speed, anxious to talk to another human being. The route from Tenebrae to Gralea is long and lonely for those not taking the train."

    show prompto downcast at left
    with dissolve

    "It looks like he's lost in thought. But from this distance, you can't really tell. You approach slowly."

    "\"Hi.\""

    show prompto surprised at left
    with dissolve

    prompto "Oh! I ... I didn't expect to see anyone else out here."

    prompto "A-are you okay?"

    "Why is he asking how I am? He's clearly the one who's not okay."

    menu:

        "Apologise for surprising him":

            jump apology

        "Ask if he's okay instead":

            jump console

        "Ask how he got here":

            jump pragmatic

label apology:

    "\"Sorry for startling you like that.\""

    prompto "Oh, no, really. It's okay."

    "\"No, I should have called out earlier or something.\""

    show prompto sadsmile
    with dissolve

    "He smiles, but his expression is sad, like he recognises what you're doing."

    prompto "You don't need to blame yourself. Seriously."

    "So he says, but he clearly looks like he appreciates it. \n He looks a little more relaxed now, and you're pleased to see it, but you're now even more worried at what he could be doing out here all alone."

    $ happiness += 2

    "You decide to ask him."

    jump what_happened

label console:

    "\"Hey, don't worry about me. Honestly, I'm more concerned about you. You look a bit ... upset.\""

    prompto "M-me? Oh, uh ... "

    show prompto semidowncast
    with dissolve

    "He averts his gaze again, gripping his arm hard like he's testing he's real. "

    prompto " ... I'm fine. I guess."

    "You get the impression he doesn't like the spotlight being focussed so intently on him. \n But he at least seems a little bit happy that you cared."

    show prompto downcastsmile
    with dissolve

    prompto "Thanks for asking."

    $ happiness += 1

    "You decide to change the subject slightly. Focus on the world around you."

    jump what_happened

label pragmatic:

    "\"How did you get here?\""

    "He looks wary."

    prompto "I'm sorry. I don't really know you. So, uh..."

    prompto "I mean, you get it, right? "

    $ happiness += 0

    jump what_happened
