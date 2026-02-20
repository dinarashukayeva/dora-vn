# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


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





































