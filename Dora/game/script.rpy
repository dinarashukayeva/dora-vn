# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default money = 0
define mc = Character("MC")
define c = Character("Cashier")
define intercom = Character("Train Conductor, Intercom")
define dealer = Character("Dealer")
define f = Character("flier")
define n = Character("Neighbour")
image bg train:
    "train.webp"
    matrixcolor BrightnessMatrix(renpyBrightness)

init python:
    if persistent.text_font_size is None:
        persistent.text_font_size = 0

    if persistent.dyslexic_font is None:
        persistent.dyslexic_font = False

    if persistent.renpyBrightness is None:
        persistent.renpyBrightness = 0.0

    def apply_brightness(st, at):
        return Transform("train.webp", matrixcolor=BrightnessMatrix(persistent.renpyBrightness)), 0
    

image bg train = DynamicDisplayable(apply_brightness)

# The game starts here.

label start:
    $ money = 1000
    $ day = 0
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
    define Unknown = Character("???")

    show bg house
    show mc
    with fade

    mc "{i}My house… Thank goodness for this convenient map.{/i}"

    mc "{i}I don’t have a lot to unpack.{/i}"

    Unknown "Hey {noalt}\u0ED7\u0F5D\u10FB \u1135\u11DF\u1FB7\u216E\u2124\u2238\u2464\u2548{/noalt}{alt}maoew knighlmaeirta{/alt}!"

    mc "Huh?"

    show n 
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
        show n
        with fade
        
        n "Oh {noalt}\u0996\u0AAC \u0ABE\u0C14\u0C0F\u0C36{/noalt}{alt}wallaboo . etzayre.{/noalt} nice {noalt}\u0973\u06A3{/noalt}{alt}wooo.{/noalt} meet you {noalt}\uFECA\u0637{/noalt}{alt}traaaloo{/alt}."

        show mc 
        with fade

        mc "{i}I wish I could say something more but I don’t know how.{/i}"

        jump neighbours2

    label N2:
        show n 
        with fade

        n "{noalt}\u0CAC\u0D2F\u0D3F \u04D4 \u0E07\u0E1F \u0EA7\u0F35\u0F78\u0F77\u0D0B{/noalt}{alt}denay tharaku yie cratsaladat{/alt} hahaha {noalt}\u10F4\u112D\u1120 \u117C \u11E1\u1E88\u1EF2\u1F63 \u2076\u2127\u2218\u2281 \u22D1 \u2320\u224F \u2574{/noalt}{alt}...budlakxkeoaryusheiyasooolathimagablonka..{/alt} hello."

        show mc 
        with fade 

        mc "{i}I can’t tell… were they laughing at me? But they said 'hello'...{/i}"

        jump neighbours2

label neighbours2:
    scene outside
    show n 
    with fade

    n "{noalt}\u20AB\u1FE9\u119A \u10DE \u0F9C\u0F3F\u0F4C\u0F31 \u0F5B\u113C \u1182{/noalt}{alt}Watellyiuchranksensionacton{/alt} you {noalt}\u301E\u301F \u309C \u3171\u3209\u30F4\u3047\u2660{/noalt}{alt}castlenienakeloen{/alt}. Bye bye {noalt}\u2731\u272C{/noalt}{alt}moar{/alt}~"

    show mc 
    with fade 

    mc "Uh, yes… bye bye."

    mc "{i}I barely understood anything in that conversation…{/i}"

    "Go into house"

    mc "{i}I have to learn the language soon. I don’t know how else I’ll manage living here. How would I make money?{/i}"

    "Stomach Growls"

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
        "{i}Roulette is probably a safer option if I can't read the numbers...{/i}":
            jump Roulette
    jump blackjack

label blackjack:
    mc "Deal me in."
    $ bet = 0
    label betinput:
        $ bet = int(renpy.input (_("Input your bet. You have $[money] left."), allow="0123456789."))
        if bet > money:
            mc "{i}I don't have enough money for that bet...{/i}"
            jump betinput
        else:
            $ money -= bet
    $ dealerscore = 0
    $ playerscore = 0
    $ playeraces = 0
    $ dealeraces = 0

    # Deal cards
    $ playerdraw = renpy.random.randint(1,13) # 1st player draw
    # [insert card sprite into scene here]
    if playerdraw > 10:
        $ playerdraw = 10
    elif playerdraw == 1:
        $ playeraces += 1
    $ playerscore += playerdraw
    $ playerdraw = renpy.random.randint(1,13) # Second player draw
    # [insert card sprite into scene here]
    if playerdraw > 10:
        $ playerdraw = 10
    elif playerdraw == 1:
        $ playeraces += 1
        $ playerscore += playerdraw

    $ dealerdraw = renpy.random.randint(1,13)
    # [insert card sprite into scene here]
    if dealerdraw > 10:
        $ dealerdraw = 10
    elif dealerdraw == 1:
        $ dealeraces += 1
    $ dealerscore += dealerdraw
    # [insert facedown dealer card sprite]
    label playerChoice:
        # Have buttons appear
        menu:
            "Hit":
                $ playerdraw = renpy.random.randint(1,13)
                # [insert card sprite into scene here]
                if playerdraw > 10:
                    $ playerdraw = 10
                elif playerdraw == 1:
                    $ playeraces += 1
                $ playerscore += playerdraw
                jump checkPlayer
            "Stand":
                jump stand
            # Space for split option later if desired
            "Double Down":
                if money < bet:
                    mc "{i}Looks like I don't have enough money to double down here...{/i}"
                    jump playerChoice
                $ money -= bet
                $ bet += bet
                $ playerdraw = renpy.random.randint(1,13)
                # [insert card sprite into scene here]
                if playerdraw > 10:
                    $ playerdraw = 10
                elif playerdraw == 1:
                    $ playeraces += 1
                $ playerscore += playerdraw
                if playerscore > 21:
                    if playeraces > 0:
                        $ playerscore -= 10
                        $ playeraces -= 1
                        jump stand
                    else:
                        jump lose
                elif playerscore == 21:
                    jump win
                else:
                    jump stand
    label checkPlayer:
        if playerscore > 21:
            if playeraces > 0:
                $ playerscore -= 10
                $ playeraces -= 1
                jump playerChoice
            else:
                jump lose
        elif playerscore == 21:
            jump win
        else:
            jump playerChoice
    label stand:
        # [remove facedown card sprite]
        while dealerscore < 21:
            $ dealerdraw = renpy.random.randint(1,13)
            # [insert card sprite into scene here]
            if dealerdraw > 10:
                $ dealerdraw = 10
            elif dealerdraw == 1:
                $ dealeraces += 1
            $ dealerscore += dealerdraw
        jump checkDealer
    label checkDealer:
        if dealerscore > 21:
            if dealeraces > 0:
                $ dealerscore -= 10
                $ dealeraces -= 1
                jump compare
            else:
                jump win
        elif dealerscore == 21:
            jump lose
        else:
            jump compare
        label compare:
            if playerscore > dealerscore:
                jump win
            else:
                jump lose
    label win:
        if playerscore == 21:
            dealer "Wow, blackjack! Congratulations!" # someone put some unicode here
            $ money += bet * 3
        else:
            dealer "Congratulations, you win!" # someone put some unicode here
            $ money += bet * 2
        jump postgamemenu
    label lose:
        dealer "Sorry, looks like you lose." # someone put some unicode here
        jump postgamemenu
    label postgamemenu:
        menu:
            "Continue playing":
                if money == 0:
                    mc "{i}I'm a bit too poor to keep gambling...{/i}"
                    jump postgamemenu
                jump betinput
            "Stop playing":
                mc "{i}Time to call it there, I think I've earned enough for today.{/i}"
                jump groceryStore

label Roulette:
    show mc 
    with fade
    mc "Spin it up"
    pause 0.5
    default value = 0   
    default bet = 0
    $value = renpy.random.random()
    mc "How much should I bet? I have $[money]."
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
            if(value < 0.4857):
                "You Won"
                $money = money + bet
                pause 2
                jump roulettepostgame
            else:
                "You Lost"
                $money = money - bet
                pause 2.0
                jump roulettepostgame
        "Black":
            if(value > 0.4857 and value < 0.9714):
                "You Won"
                $money = money + bet
                pause 2.0
                jump roulettepostgame
            else:
                "You Lost"
                $money = money - bet
                pause 2.0
                jump roulettepostgame
        "Green":
            if(value > 0.9714):
                "You Won"
                $money = money + bet*17
                pause 2.0
                jump roulettepostgame
            else:
                "You Lost"
                $money = money - bet
                pause 2.0
                jump roulettepostgame
    label roulettepostgame:
        menu:
            "Continue playing":
                if money < 1:
                    mc "{i}I'm a bit too poor to keep gambling...{/i}"
                    jump roulettepostgame
                jump Roulette
            "Stop playing":
                mc "{i}Time to call it there, I think I've earned enough for today.{/i}"
        jump groceryStore

label groceryStore:
    scene bg grocery
    with None
    show mc 
    with fade
    mc "{i}Now I can truly start my new life! I’ve got [money] dollars to spend on groceries{/i}"
    pause 0.5
    mc "{i}What I truly want is chocolate, but I only know the words for egg...{/i}"
    mc "{i}A flier with pictures! I've gotta memorize the words on this to be able to buy what I need.{/i}"
    f "milk: \u273F\u22B0, bread: \u263E\u2630, chocolate: \u22CB\u21E7"
    
    jump groceryStoreMinigame1

label groceryStoreMinigame1:
    $items = []
    mc "{i}The first thing I'm looking for is milk. Which aisle would that be in?{/i}"
    menu:
        "\u2761 \u2752, \u273F \u22B0, \uFE41 \u27A2":
            mc "{i}Correct! Found what I needed."
            $items.append("milk")
            jump groceryStoreMinigame2
        "\u2727 \u2711, \u2710 \u2659, \u264B \u27AD":
            mc "{i}Aww, no milk here...{/i}"
            jump groceryStoreMinigame2

label groceryStoreMinigame2:
    mc "{i}Now I need bread.{/i}"
    menu:
        "\u3030\u3057, \u273F\u2736, \u2711\u270D":
            mc "{i}Aww, no bread here...{/i}"
            jump groceryStoreMinigame3
        "\u3007\u300F, \u263E\u2630, \u3014\u3037":
            mc "{i}Correct! Found what I needed.{/i}"
            $items.append("bread")
            jump groceryStoreMinigame3

label groceryStoreMinigame3:
    mc "{i}Last but not least, chocolate!{/i}"
    menu:
        "\u2727 \u2711, \u264B \u27AD, \u273F \u22B0":
            mc "{i}Aww, no chocolate here...{/i}"
            jump groceryStorePost
        "\u22CB\u21E7, \u273F\u2736, \u2711\u270D":
            mc "{i}Correct! Found what I needed.{/i}"
            $items.append("chocolate")
            jump groceryStorePost

label groceryStorePost:
    if len(items) < 3:
        mc "{i}I didn't find everything I needed... guess I'll pick up some eggs as well.{/i}"
        $items.append("eggs")
    mc "{i}Now I only need to pay for everything I got!{/i}"
    scene bg cashier
    show c
    with fade
    c "add unicode later: Hello, would you like to pay?"
    mc "Umm. Yes!"
    $item_str = ""
    python:
        for i in items:
            item_str = item_str + ", " + i
    mc "{i} I ended up with [item_str].{/i}"
    $cost = len(items) * 20

    #have the cost be the only thing not blurred i think. or rely on your blackjack knowledge?
    c "add unicode later: That will be [cost]$."
    if money >= cost:
        mc "Thank you!"
        $money -= cost
    else:
        mc "{i}I don't have enough...{/i}"
        mc "{i}I'll put this stuff back.{/i}"
    jump home

    label home:
        mc "{i}Finally home! I will need to pass the language exam soon. I should practice... Tomorrow.{/i}"
        None "It's a new day!"
        jump new_day_neighbour

    label day2_neighbour:
        mc "{i} It's my neighbour from the first day!"
        n "add unicode later (less than before): Hello! It's good to see you again!"
        mc "Hello! ..."
