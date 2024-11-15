points = 0
body_count = []
while True:
    alien_color = input("What color is the alien?:\n")
    if alien_color.lower() == "quit":
        print("Thanks for playing!")
        break
    if alien_color.lower() == "green":
        print("5 points")
        points += 5
        body_count.append('green')
    elif alien_color.lower() == "red":
        print("10 points")
        points += 10
        body_count.append('red')
    elif alien_color.lower() == "yellow":
        print("15 points")
        points += 15
        body_count.append('yellow')
    else:
        print("You missed")
    
print(f"High Score: {points}")
print(body_count)