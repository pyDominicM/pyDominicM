def grades(marks):

    if marks in range(0, 2):
        print("You have gotten grade U. You need "+str(2 - marks)+' more mark/s for the next grade.')
    elif marks in range(2, 4):
        print("You have gotten grade 1. You need "+str(4 - marks)+' more mark/s for the next grade.')
    elif marks in range(4, 13):
        print("You have gotten grade 2. You need "+str(13 - marks)+' more mark/s for the next grade.')
    elif marks in range(13, 22):
        print("You have gotten grade 3. You need "+str(22 - marks)+' more mark/s for the next grade.')
    elif marks in range(22, 31):
        print("You have gotten grade 4. You need "+str(31 - marks)+' more mark/s for the next grade.')
    elif marks in range(31, 41):
        print("You have gotten grade 5. You need "+str(41 - marks)+' more mark/s for the next grade.')
    elif marks in range(41, 54):
        print("You have gotten grade 6. You need "+str(54 - marks)+' more mark/s for the next grade.')
    elif marks in range(54, 67):
        print("You have gotten grade 7. You need "+str(67 - marks)+' more mark/s for the next grade.')
    elif marks in range(67, 80):
        print("You have gotten grade 8. You need "+str(80 - marks)+' more mark/s for the next grade.')
    elif marks == 80:
        print("You have gotten grade 9. Well done!")

    else:
        print("Error.")


grades(51)
