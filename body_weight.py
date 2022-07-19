# A program to determine how much water you should drink
# Based on 8oz of water per 20 lbs of body weight

print('What is your weight in lbs?')
bodyWeight = input() #get body weight
print('You should be drinking ' +str(int(bodyWeight) / 20 * 8) + ' oz of water daily.') #divide body weight by 20 and multiply by 8
