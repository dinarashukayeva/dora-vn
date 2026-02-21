# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MC")
define intercom = Character("Train Conductor, Intercom")
define dealer = Character("Dealer")
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

    show eileen happy

    # These display lines of dialogue.

    mc "{i}(This is it.){/i}"

    None "chugga chugga chugga chugga choo choo!"

    mc "{i}(A new start… a brand new language){/i}"

    intercom "\u042A\u04B2\u060E stop ઔ७ࠁೋ"

    mc "{i}Here’s my stop… I think.{/i}"


    # This ends the game.

    return

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
    $ money = 1000
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
































