import unittest
import datetime
def get_symbol():
    symbol = input("Please enter the symbol you want: ")
    return symbol
def get_chart():
    chart = input("\nPlease enter the chart you want to create(1 or 2): ")
    return chart
def get_timeseries():
    timeseries = input("\nPlease enter the time series you desire(1-4): ")
    return timeseries
def get_startdate():
    start_date = input("\nPlease enter the start date you want(YYYY-MM-DD): ")
    return start_date
def get_enddate():
    end_date = input("\nPlease enter the end date you want(YYYY-MM-DD): ")
    return end_date

#self.assertTrue()
#self.assertEqual()
class test_inputs(unittest.TestCase):
#test the symbols capitalized and alpha characters
    def test_symbol(self):
        symbol = get_symbol()
        self.assertTrue(symbol.isupper(),True)
        self.assertTrue(len(symbol) >= 0 )
        self.assertTrue(len(symbol)<=10)

# check to see if the input is 1 or 2 
    def test_chart(self):
        chart_choice = get_chart()
        try:
            self.assertTrue(int(chart_choice ==1) or int(chart_choice == 2))
        except AssertionError:
            pass

#check to see if input is 1-4 one character
    def test_timeseries(self):
        time_series = get_timeseries()
        self.assertIn(int(time_series), range(1,5))

#Test the input format and the numbers range for month and day. limit 1980's furthest date
    def test_start_date(self):
        start_date = get_startdate()
        Y , M , D = start_date.split("-")[0], start_date.split("-")[1],start_date.split("-")[2]
        #tests the length of the date entry
        self.assertTrue(len(D) == 2)
        self.assertTrue(len(M) == 2)
        self.assertTrue(len(Y) == 4)
        #tests if the input is valid
        dates = datetime.datetime.now()
        self.assertTrue(int(D) >=1 or int(D) <= 31)
        self.assertTrue(int(M) >=1 or int(M)<= 12)
        self.assertTrue(int(Y) >= 1980 or int(Y) <= dates.year)
#Test the input format and the numbers range for month and day. cant pass current date.
    def test_end_date(self):
        end_date = get_enddate()
        Y , M , D = end_date.split("-")[0], end_date.split("-")[1],end_date.split("-")[2]
        #tests the length of the date entry
        self.assertTrue(len(D) == 2)
        self.assertTrue(len(M) == 2)
        self.assertTrue(len(Y) == 4)
        #tests if the input is valid
        dates = datetime.datetime.now()
        self.assertTrue(int(D) >=1 or int(D) <= 31)
        self.assertTrue(int(M) >=1 or int(M)<= 12)
        self.assertTrue(int(Y) >= 1980 or int(Y) <= dates.year)


if __name__ == "__main__":
    unittest.main()