#!/bin/python3

# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
# and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_percent = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    meal_cost += meal_percent + tax
    meal_cost = round(meal_cost)
    print("The total meal cost is {} dollars.".format(meal_cost))
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
