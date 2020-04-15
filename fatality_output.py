from case_fatality_rate import *
import sys


def main():
    print('Welcome  Choose any of the following to proceed')
    print("________________________________\nPress 1---> Mortality Rate\nPress 2---> Recovery Rate\nPress 3---> Active Cases Rate\nPress 4---> Exit\n________________________________")
    

    case_fatality = Case_Fatality_Rate()
    while(1):
        entry = int(input('Reply with any of the above choices: '))
        if entry == 1:
            death_rate = case_fatality.case_fatality_rate()
            print('The death rate for Covid-19 is: %0.2f' % death_rate, '%')
        elif entry == 2:
            recovery_rate = case_fatality.recovery_rate()
            print('The recovery rate for Covid 19 is: %0.2f' %
                  recovery_rate, '%')
        elif entry == 3:
            current_cases = case_fatality.current_cases_rate()
            print('The Current active case for Covid-19 is: %0.2f' %
                  current_cases, '%')
        elif entry == 4:
            print("Exiting...")
            sys.exit(0)
        else:
            print('Invalid choice try again')


print(main())
