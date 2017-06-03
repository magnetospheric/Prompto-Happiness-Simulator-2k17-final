
label camera_ask:

    menu:

        "Mention the camera":

            jump camera

        "Leave it. There may be sad memories attached":

            jump final_doubts

label valley:

    prompto "So tell me something about this place. You must know a lot, if you're on the pilgrimage."

    you "Well, this mountain range isn't particularly special. Beyond it is said to be Shiva's domain."

    you "The valley we just crossed is the Valley of Saint Lucis."

    prompto "What, really?"

    you "Yeah. Hardly anyone calls it that any more, though. It's an old name."

    prompto "Why out here, though? The name Lucis is an Insomnian thing."

    you "Eh, if you go as far back as Solheim, there's more influences than you'd expect. But I just know what my parents told me, really."

    you "I don't keep track beyond that. I just follow the Oracle's teachings."

    "Prompto's breath catches in his throat."

    prompto "About that... Have you heard? About Lady Lunafreya?"

    "When he speaks her name it's a little stilted, as if she were a dear friend.{p=0.5}You know everyone can get like this over celebrities, but in this boy's case you know it's a lot more than that."

    "Noctis. Lady Lunafreya. The promise of a marriage. And you remember the news reports. This poor kid, he must have seen a lot."

    you "I heard while I was in Tenebrae. It's terribly sad."

    "He agrees, and he returns to his food."

label camera:

    "You think now is probably a good time to change the subject."

    you "Hey, is that a camera?"

    you "Maybe you should take a photo now."

    prompto "Oh, you mean, like a selfie?"

    you "Why not?"

label campfire_comfort:

    "You both set up a campfire in the cozy confines of the cavern. There seems to be plenty of room for the smoke to dissipate safely."

    you "This friend have a name?"

    prompto "Yeah. Noctis."

    you "Oh, like the Crown Prince of Insomnia?"

    "He nods, a little too anxiously. You suspect but say nothing."

    you "Popular name, these days. He from Leide or something?"

    prompto "Y-yeah."

    "He's a terrible liar, but a really cute one.{p=0.5}With this inadvertent revelation, you understand a bit more about why the soldiers may be after him."

    "However he became separated from Noctis in Cartanica, it's clear he's shouldering a lot of the blame for what must be a tricky situation."

    you "Can I just say one thing?"

    prompto "Sure"

    you "Your friend, Noctis. He's really lucky to have someone like you. "

    prompto "You... you really mean that?"

    you "Of course I do."

    "He may not be aware of it himself, but he's leaned forwards slightly as you've been speaking."

    menu:

        "Hug him again":

            jump end

        "Keep your distance"


label end:

    "The end"

    return
