from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)
missile_sound = games.load_sound("sounds/missle.wav")
games.music.load("sounds/gamenoise.mp4")


choice = None
while choice!=0

print(
    """
    0 - Quit
    1 - Play missile sound
    2 - Loop missile sound
    3 - Stop missile sound
    4 - Play theme music
    5 - Loop theme music
    6 - Stop theme music
    """
    choice = input("Choice: ")
    print()
    #exit
    if choice == "0":
        print("Goodbye")

    #Play missile sound
    elif choice == "1":
        missile_sound.play()
        print("Playing missile sound.")
    #Loop missile sound
elif choice == "2":
    )



