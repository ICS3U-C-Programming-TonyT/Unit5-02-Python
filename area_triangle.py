#!/usr/bin/env python3
# Created By: Tony Tran
# Date: November. 24, 2023
# This program will calculate the area of a triangle using height and base in cm.


def calc_area(base, height):
    area = round((base * height) / 2, 2)
    print(f"The area of the triangle is {area}cm².")


def main():
    user_base = str(input("Enter the base of the triangle (cm): "))
    user_height = str(input("Enter the height of the triangle (cm): "))
    try:
        user_base = float(user_base)
        user_height = float(user_height)
    except ValueError:
        print(f"{user_base or user_height} is not a valid number.")
    else:
        if user_base or user_height >= 0:
            calc_area(user_base, user_height)
        else:
            print(f"Base and height must be greater than 0.")


if __name__ == "__main__":
    main()
