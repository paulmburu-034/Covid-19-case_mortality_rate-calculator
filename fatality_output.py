from case_fatality_rate import *


def main():
    print('Welcome  Choose any of the following to proceed')
    print('1 : Mortality rate')
    print('2 : Recovery rate')
    print('3 : Active cases rate')

    entry = int(input('Reply with any of the above choices: '))
    start = 1
    case_fatality = Case_Fatality_Rate()
    while start == 1:
        if entry == 1:
            death_rate = case_fatality.case_fatality_rate()
            print('The death rate for Covid-19 is: %0.2f' % death_rate, '%')
            break
        elif entry == 2:
            recovery_rate = case_fatality.recovery_rate()
            print('The recovery rate for Covid 19 is: %0.2f' %
                  recovery_rate, '%')
        elif entry == 3:
            current_cases = case_fatality.current_cases_rate()
            print('The Current active case for Covid-19 is: %0.2f' %
                  current_cases, '%')
        else:
            print('Invalid choice try again')
            start = 0


print(main())
