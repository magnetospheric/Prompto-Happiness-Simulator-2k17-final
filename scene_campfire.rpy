
label camera_ask:

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


label campfire_comfort:

    "You both set up a campfire in the cozy confines of the cavern. There seems to be plenty of room for the smoke to dissipate safely."

    menu:

        "Hug him again":

            jump end


label end:

    "The end"

    return
