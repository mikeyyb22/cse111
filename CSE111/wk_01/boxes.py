import math

"""
In our modern world economy, many items are manufactured in large factories, 
then packed in boxes and shipped to distribution centers and retail stores. 
A common question for employees who pack items is “How many boxes do we need?”
"""

itemnumber = int(input('Input number of manufactured items: '))
itemsperbox = int(input('Input number of items packed per box: '))

totalboxes = math.ceil(itemnumber / itemsperbox)

print(f'You will need {totalboxes} boxes.')
