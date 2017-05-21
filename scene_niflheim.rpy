label niflheim:

    prompto "So what are you doing here, then?"

    "\"I'm on the pilgrim's trail. I've just been to Tenebrae - now I'm headed back home to Niflheim.\""

    menu:

        "Tell him you like Niflheim.":

            jump like_niflheim

        "Express your dissatisfaction with Niflheim.":

            jump hate_niflheim


label like_niflheim:

    jump to_mountain_haven


label hate_niflheim:

    jump to_mountain_haven


label to_mountain_haven

    "\"So, are you headed to Niflheim or something?\""

    prompto "Yeah. I guess."

    "He doesn't seem keen to reveal any more at this stage."

    #if he has a low happiness rating:
     #"He still seems awfully sad"
    #if he has the lowest happiness rating
     #"He still seems awfully sad, and it seems he doesn't really trust you"
    # if he has a high happiness rating
     #"But he does seem to have perked up a bit."
    "\"Come on. We should get going before nightfall. There's a haven way over in those mountains."

    #cut to view of mountains for a bit

    # if he has low / high happiness, say slightly different things here
    "You both start the long trek towards the mountains. The snowy plains don't seem nearly as isolating now that you're walking with him. And he seems happy to have company - or so the contented smile plastered across his face would indicate."
    "You both start the long trek towards the mountains. The snowy plains don't seem nearly as isolating now that you're walking with him. Surely he feels the same, because although he's guarded, hand hovering near his gun, he still asked you to join him."
