# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("L")
define kira = Character("Kira")

# The game starts here.

label start:
    image l = "images/l(1).png"
    image kira = "images/kira(1).png"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show l:
        zoom 4
        xalign 0.5
        yalign 1.0

    # These display lines of dialogue.

    e "le gusta lo kinky nasty y aunque sea fancy se pone kranky si lo hago romantic."

    e "watashi wa goy desu"

    show kira at right:
        zoom 4

    kira "calla w"

    # This ends the game.

    return
