__author__ = 'dwight'

# Write a program that calculates and displays a person’s body mass index (BMI). The BMI is often used to determine
# whether a person is overweight or underweight for his or her height. A person’s BMI is calculated with the following
# formula:
#       BMI = weight * 703 / height^2
# where weight is measured in pounds and height is measured in inches.

def main():
    weight = float(input('Enter your weight (pounds): '))
    height = float(input('Enter your height (inches): '))

    print('Your BMI is', format(calc_bmi(weight, height), '.2f'))


def calc_bmi(weight, height):
    return (weight * 703) / (height * height)


main()