#Name: Rramon Isaku
#Date: April 23, 2023
#Assignment: Week 6


def main():
    intro()

    try:
      miles_needed = int(input('Enter the number of miles driven: '))
      miles_to_kilometers(miles_needed)

    except:
      print("An exception occured, try again by entering only a number.")
      print()
      main()

def intro():
  print('This program converts measurements in miles to kilometers.')
  print('For your reference, the formula is:')
  print(' 1 mile = 1.60934 kilometers')
  print()

def miles_to_kilometers(miles):
  kilometers = miles * 1.60934
  print("The stated miles of " + str(miles) + " is equal to " + str(kilometers),'kilometers.')

main()
