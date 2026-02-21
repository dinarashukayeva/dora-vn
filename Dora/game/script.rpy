# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default money = 0
define mc = Character("MC")
define c = Character("Cashier")
define intercom = Character("Train Conductor, Intercom")
define dealer = Character("Dealer")
define n = Character("Neighbour")
image bg train:
    "train.webp"
    matrixcolor BrightnessMatrix(renpyBrightness)

init python:
    import re

    if persistent.text_font_size is None:
        persistent.text_font_size = 0

    if persistent.dyslexic_font is None:
        persistent.dyslexic_font = False

    if persistent.renpyBrightness is None:
        persistent.renpyBrightness = 0.0

    def dyslexic_text_filter(s):
        if not persistent.dyslexic_font:
            return s
        # Split into Ren'Py tags and plain text segments
        parts = re.split(r'(\{[^}]*\})', s)
        result = []
        for part in parts:
            if part.startswith('{') and part.endswith('}'):
                # Ren'Py tag — leave as-is
                result.append(part)
            else:
                # Wrap runs of non-ASCII chars in a Unicode-capable font
                processed = []
                in_unicode = False
                for char in part:
                    if ord(char) > 127:
                        if not in_unicode:
                            processed.append('{font=Arial Unicode.ttf}')
                            in_unicode = True
                        processed.append(char)
                    else:
                        if in_unicode:
                            processed.append('{/font}')
                            in_unicode = False
                        processed.append(char)
                if in_unicode:
                    processed.append('{/font}')
                result.append(''.join(processed))
        return ''.join(result)

    config.say_menu_text_filter = dyslexic_text_filter

    def apply_brightness(st, at):
        return Transform("train.webp", matrixcolor=BrightnessMatrix(persistent.renpyBrightness)), 0
    

image bg train = DynamicDisplayable(apply_brightness)

# The game starts here.

label start:
    $ money = 1000
    $ debt = 0
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

    if day == 0:
        mc "{i}I feel right home... where I'm meant to be.{/i}"
        mc "{i}No matter what language, money speaks the same... and I speak money.{/i}"
        mc "{i}Time to start with the good old reliable - Blackjack.{/i}"
        mc "{i}Wait - what?? These cards don't have numbers or symbols... just words??{/i}"
    else:
        mc "{i}Back to the grind!{/i}"
    menu:
        "{i}I don't know if I can win in any of these other games... and Blackjack is my best bet...{/i}":
            if day == 0:
                mc "{i}Probably have a better shot once I learn the numbers... {b}maybe I should keep track of what each character means?{/b}{/i}"
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
    $ unicodenumbers = {"\u0586": 1, "\u0681": 2, "\u0E1F": 3, "\u10E6": 4, "\u0ED7": 5, "\u315D": 6, "\u210C": 7, "\u2204": 8, "\uFFA2": 9, "\uFEFC": 10, "\u2735": 11, "\u3147": 12, "\u1197": 13}
    $ flippedunicodenumbers = {v: k for k, v in unicodenumbers.items()}
    $ playercards = ""
    $ dealercards = ""

    # Deal cards
    $ playerdraw = renpy.random.randint(1,13) # 1st player draw
    $ playercards += flippedunicodenumbers[playerdraw]
    if playerdraw > 10:
        $ playerdraw = 10
    elif playerdraw == 1:
        $ playeraces += 1
    $ playerscore += playerdraw
    $ playerdraw = renpy.random.randint(1,13) # Second player draw
    $ playercards += flippedunicodenumbers[playerdraw]
    if playerdraw > 10:
        $ playerdraw = 10
    elif playerdraw == 1:
        $ playeraces += 1
    $ playerscore += playerdraw

    $ dealerdraw = renpy.random.randint(1,13)
    $ dealercards += flippedunicodenumbers[dealerdraw]
    if dealerdraw > 10:
        $ dealerdraw = 10
    elif dealerdraw == 1:
        $ dealeraces += 1
    $ dealerscore += dealerdraw
    # [insert facedown dealer card sprite]
    label playerChoice:
        # Have buttons appear
        menu:
            "Your cards: [playercards]\nDealer's cards: [dealercards]{fast}"
            "Hit":
                $ playerdraw = renpy.random.randint(1,13)
                $ playercards += flippedunicodenumbers[playerdraw]
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
                $ playercards += flippedunicodenumbers[playerdraw]
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
        while dealerscore < 17:
            $ dealerdraw = renpy.random.randint(1,13)
            $ dealercards += flippedunicodenumbers[dealerdraw]
            "Player Cards: [playercards]\nDealer Cards: [dealercards]"
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
            dealer "\u23CF\u0C20, blackjack! \u0B9E\u235F" # someone put some unicode here
            $ money += bet * 3
        else:
            dealer "\u0B9E\u235F, \u0D17win!" # someone put some unicode here
            $ money += bet * 2
        jump postgamemenu
    label lose:
        dealer "\u0933, \u0554\u0462\u0D17 lose." # someone put some unicode here
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
                mc "{i}Hopefully I learned some numbers from that session.{/i}"
                jump neighbour_loan

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
        jump neighbour_loan

label neighbour_loan:
    if money < 200:
        scene bg mansion_outside
        with None
        show n
        with fade
        n "unicode here: Hey do you need a loan"
        mc "im running low on money."
        n "i'll give you 200$ (joshua this has to be whatever the price of the exp)"
        mc "{i}My neighbour gave me 200 dollars! I'll have to pay them back eventually.{/i}"
        $money += 200
        $debt += 200
    elif money > debt and debt > 0:
        scene bg mansion_outside
        with None
        show n
        with fade
        n "unicode here: Hello! do you have my money"
        menu:
            "Pay them back":
                mc "Thank you! idk somone fix this dialogue pls"
                $ money -= debt
                jump groceryStore
            "Pay them back but be mean about it":
                mc "fine >:("
                jump groceryStore
    
    if day == 0:
        jump groceryStore
    else: 
        jump home

label groceryStore:
    scene bg house
    with None
    show mc 
    with fade
    mc "{i}Now I can truly start my new life! I’ve got [money] dollars to spend on groceries{/i}"
    mc "{i}There's a grocery store that speaks English, but those prices are absurd... {/i}"
    mc "{i}Maybe the local store down the street has some better deals, but I'll have to learn the language...{/i}"
    scene bg grocery
    with fade
    pause 0.5
    $ keywords = {"\u273F": "milk", "\u22B0": "apples", "\u263E": "cheese", "\u2630": "bread", "\u22CB": "potatoes", "\u21E7": "beef"}
    $ todayswords = renpy.random.sample(list(keywords.keys()), 2)
    $ wanteditems = keywords[todayswords[0]] + " and " + keywords[todayswords[1]]
    mc "{i}Today, I'm looking to get [wanteditems].{/i}"
    $ allwords = ["\u273F", "\u22B0", "\u263E", "\u2630", "\u22CB", "\u21E7", "\u2761", "\u2752", "\uFE41", "\u27A2", "\u3007", "\u300F", "\u2727", "\u2711", "\u2710", "\u2659"]
    $ renpy.random.shuffle(allwords)
    $ aisle1 = ""
    $ aisle2 = ""
    $ aisle3 = ""
    $ aisle4 = ""
    python:
        for i in allwords[:4]:
            aisle1 += i
        for i in allwords[4:8]:
            aisle2 += i
        for i in allwords[8:12]:
            aisle3 += i
        for i in allwords[12:]:
            aisle4 += i
    $ aislesleft = 2
    $ collecteditems = []

    if day == 0:
        mc "{i}As I expected, I won't be able to read these aisles. I know that each item in the store is {b}1 character long{/b}, and each aisle appears to have 4 items each."
        mc "{i}If I try enough times, eventually I should be able to learn what each character means.{/i}"
    jump groceryStoreMinigameAisles

label groceryStoreMinigameAisles:
    mc "{i}Looks like there's 4 aisles to choose from, but I only have time to check [aislesleft] more aisles before the store closes.{/i}"
    $ founditems = []
    menu:
        "[aisle1]":
            python:
                for i in allwords[:4]:
                    if i in todayswords:
                        founditems.append(keywords[i])
                        todayswords.remove(i)
            jump groceryStoreMinigameCheck
        "[aisle2]":
            python:
                for i in allwords[4:8]:
                    if i in todayswords:
                        founditems.append(keywords[i])
                        todayswords.remove(i)
            jump groceryStoreMinigameCheck
        "[aisle3]":
            python:
                for i in allwords[8:12]:
                    if i in todayswords:
                        founditems.append(keywords[i])
                        todayswords.remove(i)
            jump groceryStoreMinigameCheck
        "[aisle4]":
            python:
                for i in allwords[12:]:
                    if i in todayswords:
                        founditems.append(keywords[i])
                        todayswords.remove(i)
            jump groceryStoreMinigameCheck

label groceryStoreMinigameCheck:
    if founditems == []:
        mc "{i}Aww, nothing that I need here...{/i}"
    else:
        $ founditemsstring = ""
        python:
            for i in founditems:
                founditemsstring += i + ", "
                collecteditems.append(i)
            founditemsstring = founditemsstring[:-2]
        mc "Found: [founditemsstring]!"
    $ aislesleft -= 1
    if todayswords == [] or aislesleft == 0:
        jump groceryStorePost
    jump groceryStoreMinigameAisles

label groceryStorePost:
    $ cost = len(collecteditems) * 50
    if len(collecteditems) < 2:
        mc "{i}I didn't find everything I needed... guess I'll have to pick up the rest from the expensive store...{/i}"
        $ cost += 100 * (2 - len(collecteditems))
        
    #have the cost be the only thing not blurred i think. or rely on your blackjack knowledge?
    c "add unicode later: That will be $[cost]."
    $money -= cost
    mc "Thank you! {i}Looks like I have $[money] left.{/i}"

    if day == 0:
        jump home_end
    else:
        jump home

    label home_end:
        scene bg home
        with fade
        mc "{i}Finally home! I will need to pass the language exam soon. I should practice... Tomorrow.{/i}"
        jump new_day

    label new_day_neighbour:
        mc "{i} It's my neighbour from before. {/i}"
        n "add unicode later (less than before?): Hello! It's good to see you again! Are you going to the grocery store?"
        mc "Hello! DUDE IDK HOW TO DO THIS someone  has to write diaLOG"
        jump groceryStore

    label new_day:
        scene bg home
        with fade
        $ day += 1
        $ time = 0
        if day == 1:
            mc "It's my 2nd day here!"
        elif day == 2:
            mc "It's my 3rd day here!"
        else:
            mc "It's my [day]th day here!"
        jump home

    label home:
        mc "{i}What should I do?{/i}"
        menu:
            "Attempt the language exam":
                jump exam
            "Go GAMBLING":
                mc "wait you haven't updated the casino code yet noooo-"
                $time += 1
                jump casino
            "Go to the grocery store":
                mc "wait you haven't updated the grocery store code yet noooo-"
                $time += 1
                jump new_day_neighbour
            "Study the language":
                $time += 1
                mc "i haven't done anything here yet"
                jump practice

    label exam:
        mc "you haven't coded the exam yet lol"


    label practice: 