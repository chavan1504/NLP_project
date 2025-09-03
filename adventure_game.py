### Print a welcome message
print("🏚️ Welcome to the Haunted Mansion!")
print("You are a distant family member of a rich millionaire who has just passed away, leaving this mysterious mansion to you.")
print("Rumors say there's a hidden treasure of diamonds 💎 somewhere inside...")
print("You gather your courage and step inside the creaky old house.")
print("Do you want to enter the living room or the dining room?")

### Prompt user for a choice
roomChoice = input("> ").lower()

if roomChoice == "living room":
    print("\nYou enter the living room.")
    print("As you walk in, you see a sleeping pitbull 🐕 guarding some gold jewelry.")
    print("Do you want to steal the jewelry from the pitbull? (yes/no)")

    pitBullChoice = input("> ").lower()

    if pitBullChoice == "yes":
        print("You attempt to steal the jewelry, but the pitbull wakes up and attacks you!")
        print("💀 You are now dead. Game Over.")
    elif pitBullChoice == "no":
        print("You decide not to disturb the pitbull.")
        print("As you turn around, you notice a **hidden staircase** behind an old bookshelf!")
        print("Do you want to go down the hidden staircase? (yes/no)")

        stairChoice = input("> ").lower()
        if stairChoice == "yes":
            print("\nYou carefully walk down the creaky stairs into a **dark basement**.")
            print("You find three doors labeled A, B, and C. One of them leads to the treasure, the others lead to traps!")
            print("Which door do you choose? (A/B/C)")

            doorChoice = input("> ").lower()

            if doorChoice == "a":
                print("You open the door and find a room full of bats 🦇 that attack you!")
                print("💀 You are now dead. Game Over.")
            elif doorChoice == "b":
                print("You open the door and step into a room filled with ancient paintings and dusty chests.")
                print("Inside one chest, you discover a **mysterious golden key** 🔑.")
                print("A secret passage opens behind the chest!")
                print("Do you want to enter the secret passage? (yes/no)")

                passageChoice = input("> ").lower()
                if passageChoice == "yes":
                    print("\nYou crawl through the passage and arrive at a **giant locked door**.")
                    print("You use the golden key 🔑, and the door creaks open...")
                    print("🌟 Inside, you find a **hidden treasure chamber** filled with glittering diamonds 💎!")
                    print("🎉 Congratulations! You found the hidden treasure and became the richest person alive!")
                else:
                    print("You decide not to enter the passage and leave the mansion safely.")
            elif doorChoice == "c":
                print("You open the door, but the floor collapses and you fall into a spike pit!")
                print("💀 You are now dead. Game Over.")
            else:
                print("Invalid choice. Please enter A, B, or C.")
        else:
            print("You leave the living room safely without exploring further.")
    else:
        print("Invalid choice. Please enter yes or no.")

elif roomChoice == "dining room":
    print("\nYou chose to go into the dining room.")
    print("As you walk in, you see a shiny vase on the table.")
    print("Do you want to open the vase? (yes/no)")

    vaseChoice = input("> ").lower()

    if vaseChoice == "yes":
        print("You open the vase and find a pile of bones! 🦴")
        print("But inside, you also notice a tiny **map** hidden beneath the bones.")
        print("The map shows a secret attic where the diamonds might be hidden!")
        print("Do you want to follow the map to the attic? (yes/no)")

        atticChoice = input("> ").lower()
        if atticChoice == "yes":
            print("\nYou climb up a narrow staircase into the dusty attic.")
            print("You find an old chest with a **combination lock**.")
            print("The map says: 'The code is the sum of 12 and 23.' What code do you enter?")

            code = input("> ")
            if code == "35":
                print("✅ Correct code! The chest creaks open...")
                print("🌟 Inside, you find the **treasure of diamonds** 💎!")
                print("🎉 Congratulations! You won the game!")
            else:
                print("❌ Wrong code! A hidden trapdoor opens beneath you and you fall into darkness...")
                print("💀 Game Over.")
        else:
            print("You ignore the map and leave the dining room safely.")
    elif vaseChoice == "no":
        print("You decide not to open the shiny vase.")
        print("As you turn to leave, you hear a cracking sound coming from the corner.")
        print("A dark figure with glowing red eyes launches at you, knocking you unconscious.")
        print("You wake up in your bed. It was all a dream... or was it?")
    else:
        print("Invalid choice. Please enter yes or no.")
else:
    print("Invalid choice. Please enter living room or dining room.")
