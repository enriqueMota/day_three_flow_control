print("""
                 ___
               ,-----,
              /\|   |/\         I am the genie guarding the sacred treasure,
             |-- \_/ --|         answer my questions correctly in order to get
          .-----/   \-----.      your reward, but be warned, down this path, many
         /   ,   . .   ,   \      evils and final destinations await you. This is a
        /  /`|    |    |'\, \      challenge not design to be taken for granted and only
        `\ \  \-  |  -/  /`/'      for the brave and of pure heart, if you do not have what
          `\\_)`-- --'(_//           it takes, it's best if you just leave now.
            |_|`-- --'|_|  _______     
             ,'`-   -'`.,-'       `-.
            |\--------/||            `-.      _,------.
           |\---------/`|    .--.       `----'   ___--.`--.
            |\---------/\. ."    `.            ,'      `---'
             ``-._______.-'        `-._______.-'

""")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("Where do you wish to go, left or right? ")

if direction.lower() == 'left':
    action = input("What do you want to do next, swim or wait? ")
    if action.lower() != 'wait':
        print("A trout was waiting for you, you should've waited. Game Over")
    else:
        door = input("Which door color do you want to open? ")
        if door.lower() == 'yellow':
            print("Congrats! You Win!")
        elif door.lower() == 'red':
            print(
                "You entered hell, there was fire behind the red door. Game Over."
            )
        elif door.lower() == 'blue':
            print(
                "I hope you had insurance, hungry beasts were waiting for you. Game Over."
            )
        else:
            print("See you in another life, looser. Game Over.")
else:
    print("I hope you had a will ready, you'll fall into a hole. Game Over.")


# https://replit.com/@enriqueMota/treasure-island-start#main.py