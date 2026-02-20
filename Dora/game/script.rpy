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

    show eileen happy

    # These display lines of dialogue.

    mc "{i}(This is it.){/i}"

    None "chugga chugga chugga chugga choo choo!"

    mc "{i}(A new start… a brand new language){/i}"

    intercom "\u042A\u04B2\u2762 stop \u2711\u27B3\u2727"

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

































