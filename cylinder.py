#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: November 2019
# This program calculates the volume of a cylinder using parameters


def calculate_volume(r, h):
    # calculate volume and return volume

    import math

    # process
    volume = math.pi * (r**2) * h

    return volume


def main():
    # this function gets radius and height from user.

    try:
        # input
        radius_from_user = int(input("Enter the radius of a cylinder (cm): "))
        height_from_user = int(input("Enter the height of a cylinder (cm): "))
        print("")

        r = radius_from_user
        h = height_from_user

        # call functions
        volume = calculate_volume(r, h)

        # output
        print("The volume is {0:,.2f} cm^3".format(volume))

    except ValueError:
        print("Please enter a valid integer")


if __name__ == "__main__":
    main()
