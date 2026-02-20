# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default money = 0
$money = 1000
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

    mc "{i}This is it.{/i}"

    None "chugga chugga chugga chugga choo choo!"

    mc "{i}A new start… a brand new language.{/i}"

    intercom "{noalt}\u0433\u04D0\u0484{/noalt}{alt}naxaldent...{/alt} stop {noalt}\u06D0\u06E6\u0996\u09EB\u0ACB\u0EBC{/noalt}{alt}...djalmbiandia{/alt}"

    mc "{i}Here’s my stop… I think.{/i}"


    # This ends the game.
    jump neighbours1

label neighbours1:

    define Neighbour = Character("Neighbour")
    define Unknown = Character("???")

    show mc
    with fade

    mc "{i}My house… Thank goodness for this convenient map.{/i}"

    mc "{i}I don’t have a lot to unpack.{/i}"

    Unknown "Hey {noalt}\u0ED7\u0F5D\u10FB \u1135\u11DF\u1FB7\u216E\u2124\u2238\u2464\u2548{/noalt}{alt}maoew knighlmaeirta{/alt}!"

    mc "Huh?"

    show Neighbour 
    with fade

    Unknown "{noalt}\u2290\u20AB \u2590\u258E\u258C\u25A5.{/noalt}{alt}fiyu... nahvaplex.{/alt}{noalt}\u3048\u3084 \u3191\u332f\uFB6B\uFC15\uFCD5.{/noalt}{alt}eyoor.. shompu..{/alt} next door."

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
        
        Neighbour "Oh {noalt}\u0996\u0AAC \u0ABE\u0C14\u0C0F\u0C36{/noalt}{alt}wallaboo . etzayre.{/noalt} nice {noalt}\u0973\u06A3{/noalt}{alt}wooo.{/noalt} meet you {noalt}\uFECA\u0637{/noalt}{alt}traaaloo{/alt}."

        show mc 
        with fade

        mc "{i}I wish I could say something more but I don’t know how.{/i}"

        jump neighbours2

    label N2:
        show Neighbour 
        with fade

        Neighbour "{noalt}\u0CAC\u0D2F\u0D3F \u04D4 \u0E07\u0E1F \u0EA7\u0F35\u0F78\u0F77\u0D0B{/noalt}{alt}denay tharaku yie cratsaladat{/alt} hahaha {noalt}\u10F4\u112D\u1120 \u117C \u11E1\u1E88\u1EF2\u1F63 \u2076\u2127\u2218\u2281 \u22D1 \u2320\u224F \u2574{/noalt}{alt}...budlakxkeoaryusheiyasooolathimagablonka..{/alt} hello."

        show mc 
        with fade 

        mc "{i}I can’t tell… were they laughing at me? But they said 'hello'...{/i}"

        jump neighbours2

label neighbours2:

    show Neighbour 
    with fade

    Neighbour "{noalt}\u20AB\u1FE9\u119A \u10DE \u0F9C\u0F3F\u0F4C\u0F31 \u0F5B\u113C \u1182{/noalt}{alt}Watellyiuchranksensionacton{/alt} you {noalt}\u301E\u301F \u309C \u3171\u3209\u30F4\u3047\u2660{/noalt}{alt}castlenienakeloen{/alt}. Bye bye {noalt}\u2731\u272C{/noalt}{alt}moar{/alt}~"

    show mc 
    with fade 

    mc "Uh, yes… bye bye."

    mc "{i}I barely understood anything in that conversation…{/i}"

    "Go into house"

    mc "{i}I have to learn the language soon. I don’t know how else I’ll manage living here. How would I make money?{/i}"

    "Stomach Growl"

    mc "{i}But first I need some food. The last time I ate was before the train ride.{/i}"

    mc "{i}I wonder what I could eat…{/i}"

    mc "{i}I can look in the fridge-{/i}"

    mc "{i}Right… I have no groceries yet. I should buy something-{/i}"

    mc "{i}But this is all my money before getting a job… How can I make more money while also getting something to eat?{/i}"

    mc "{i}Oh! I know.{/i}"

    mc "My specialty from back home too"

    mc "GAMBLING"

    jump casino



label casino:
    scene bg casino

    mc "{i}I feel right home... where I'm meant to be.{/i}"
    mc "{i}No matter what language, money speaks the same... and I speak money.{/i}"
    mc "{i}Time to start with the good old reliable - Blackjack.{/i}"
    mc "{i}Wait - what?? These cards don't have numbers or symbols... just words??{/i}"
    menu:
        "{i}I don't know if I can win in any of these other games... and Blackjack is my best bet...{/i}":
            jump blackjack
        "{i}Maybe I'll just try the good ol Roulette, no numbers there...{/i}":
            jump Roulette
    jump blackjack

label blackjack:
    mc "Deal me in."






label Roulette:
    show mc 
    with fade
    mc "Spin it up"
    pause 0.5
    default value = 0   
    default bet = 0
    $value = renpy.random.random()
    mc "How much should I bet?"
    menu:
        "1/10 of my money":
            $bet = money/10
        "1/6 of my money":
            $bet = money/6
        "1/4 of my money":
            $bet = money/4
        "1/3 of my money":
            $bet = money/3
        "1/2 of my money":
            $bet = money/2
        "ALL IN":
            $bet = money
    menu:
        "Red":
            if(value < 0.50):
                "You Won"
                $money = money + bet
                pause 2
                return
            else:
                "You Lost"
                $money = money - bet
                pause 2.0
                return
        "Black":
            if(value > 0.50):
                "You Won"
                $money = money + bet
                pause 2.0
                return
            else:
                "You Lost"
                $money = money - bet
                pause 2.0
                return



label groceryStore:
    show mc 
    with fade
    mc "Now I can truly start my new life! I’ve got ## dollars to spend on groceries"
    pause 0.5
    mc "What I truly want is chocolate, but I only know the words for egg"
    
    jump groceryStoreMinigame

label groceryStoreMinigame:































