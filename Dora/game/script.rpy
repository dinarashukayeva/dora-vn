# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mc = Character("MC")
define intercom = Character("Train Conductor, Intercom")
image bg train:
    "train.webp"
    matrixcolor BrightnessMatrix(renpyBrightness)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg train

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.

    mc "{i}(This is it.){/i}"

    None "chugga chugga chugga chugga choo choo!"

    mc "{i}(A new start… a brand new language){/i}"

    intercom "\u042A\u04B2\u2762 stop \u2711\u27B3\u2727"

    mc "{i}Here’s my stop… I think.{/i}"


    # This ends the game.

    jump neighbours1

label neighbours1:

    define Neighbour = Character("Neighbour")

    show mc
    with fade

    mc "My house… Thank goodness for this convenient map."

    pause 1.5

    mc "I don’t have a lot to unpack."

    pause 1.0

    Neighbour "Hey ๛༜Ⴉ ኆᏜᕩᗄᗡᬛ!"

    mc "Huh?"

    pause 0.5

    show Neighbour 
    with fade

    Neighbour "𮸽🤂 <NAME> and this is <name>. I live next door."

    show mc
    with fade

    mc "Oh they must be my neighbour."

    menu:
        "Hi.":
            jump N1
        "Hello, it’s a pleasure to meet you. I hope I can be a good neighbour to you.":
            jump N2

    label N1:
        show Neighbour
        with fade
        
        Neighbour "Oh well it’s nice to meet you too."

        show mc 
        with fade

        mc "I wish I could say something more but I don’t know how."

        jump neighbours2

    label N2:
        show Neighbour 
        with fade

        Neighbour "Neighbour: Don’t think I caught all that hahaha but I assume you said something along the lines of “hello”."

        show mc 
        with fade 

        mc "I can’t tell… were they laughing at me? But they said hello"

        jump neighbours2

label neighbours2:

    show Neighbour 
    with fade

    Neighbour "Well I better be off. I hope you can settle in nicely. Bye bye now~"

    show mc 
    with fade 

    mc "Uh, yes… bye bye."

    pause 0.5

    mc "I barely understood anything in that conversation…"

    "Go into house"

    mc "I have to learn the language soon. I don’t know how else I’ll manage living here. How would I make money?"

    "Stomache Growls"

    mc "But first I need some food. The last time I ate was before the train ride."
    
    pause 0.5

    mc "I wonder what I could eat…"

    "Look inside the empty fridge."

    mc "Right… I have no groceries yet. I should buy something-"

    pause 0.5

    mc "But this is all my money before getting a job… How can I make more money while also getting something to eat?"

    mc "Oh! I know."

    mc "My specialty from back home too"

    pause 2.0

    mc "GAMBLING"





label casino:
    scene bg casino

    mc "{i}I feel right home... where I'm meant to be.{/i}"
    mc "{i}No matter what language, money speaks the same... and I speak money.{/i}"
    mc "{i}Time to start with the good old reliable - Blackjack.{/i}"
    mc "{i}Wait - what?? These cards don't have numbers or symbols... just words??{/i}"
    mc "{i}I don't know if I can win in any of these other games... and Blackjack is my best bet...{/i}"
    mc "Deal me in."
    jump blackjack

label blackjack:

































