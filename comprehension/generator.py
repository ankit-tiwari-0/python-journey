# Generator
#           (expession for item in iterable if condition)
# [x for x in items]                           (x for x in item)
# make entire list in memory                    like a stream


daily_sales = [5, 10, 12, 7, 3, 8,  9, 15]

tota_cup = [sale for sale in daily_sales if sale > 5]

print(tota_cup)













# concept	Explanation
# What it is	A short way to create lists from existing lists
# Syntax	[expression for item in iterable if condition]
# Used for	Filtering or transforming data in lists
# Example	[sale for sale in daily_sales if sale > 5] → [10, 12, 7, 8, 9, 15]