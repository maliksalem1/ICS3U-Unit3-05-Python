#!/usr/bin/env python3
# Created by: maliksalem1
# Created on: Oct 2022
# This program displays the month that represents numbers 1-12


def main():
    # This function finds the month that represents your number

    # Input
    number = input("Enter the number of a month(ex: 3 for March): ")
    print("")

    # Process and Output
    match number:
        case "1":
            print("January")
        case "2":
            print("February")
        case "3":
            print("March")
        case "4":
            print("April")
        case "5":
            print("May")
        case "6":
            print("June")
        case "7":
            print("July")
        case "8":
            print("August")
        case "9":
            print("September")
        case "10":
            print("October")
        case "11":
            print("November")
        case "12":
            print("December")
        case _:
            print("Invalid Number")

    print("\nDone.")


if __name__ == "__main__":
    main()
