class Case_Fatality_Rate():

    def __init__(self, deaths = 0, recovered = 0, total_cases = 0):
        self.deaths = int(input('Enter number of deaths caused by the pademic: '))
        self.recovered = int(
            input('Enter number of the recovered from the pademic: '))
        self.total_cases = int(
            input('Enter Total cases confirmed from the pademic: '))

    def case_fatality_rate(self):
        fatality_rate = self.deaths/self.total_cases * 100
        return fatality_rate
    
    def recovery_rate(self):
        recovered_rate = self.recovered/self.total_cases * 100
        return recovered_rate

    def current_cases_rate(self):
        cases_rate = (self.total_cases-(self.recovered+self.deaths))/self.total_cases * 100
        return cases_rate