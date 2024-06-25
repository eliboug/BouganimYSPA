import matplotlib.pyplot as plt
from datetime import datetime
# all dates in the set
dates = [
    datetime(2024, 5, 1), datetime(2024, 5, 2), datetime(2024, 5, 3),
    datetime(2024, 5, 4), datetime(2024, 5, 5), datetime(2024, 5, 6),
    datetime(2024, 5, 7), datetime(2024, 5, 8), datetime(2024, 5, 9),
    datetime(2024, 5, 10), datetime(2024, 5, 11), datetime(2024, 5, 12),
    datetime(2024, 5, 13), datetime(2024, 5, 14), datetime(2024, 5, 15),
    datetime(2024, 5, 16), datetime(2024, 5, 17), datetime(2024, 5, 18),
    datetime(2024, 5, 19), datetime(2024, 5, 20), datetime(2024, 5, 21),
    datetime(2024, 5, 22), datetime(2024, 5, 23), datetime(2024, 5, 24),
    datetime(2024, 5, 25), datetime(2024, 5, 26), datetime(2024, 5, 27),
    datetime(2024, 5, 28), datetime(2024, 5, 29), datetime(2024, 5, 30),
    datetime(2024, 5, 31)
]
# all corresponding high temps
hightemps = [72, 68, 68, 56, 61, 63, 68, 81, 84, 80, 70, 63, 62, 65, 64, 66, 66, 66, 65, 68, 72, 68, 65, 57, 59, 64, 59, 62, 74, 72, 69]
# graphing
plt.scatter(dates, hightemps)
plt.title("Daily Highs in San Francisco in May 2024")
plt.xlabel("Date")
plt.ylabel("Temperature in Fahrenheit")
# formatting 
plt.gcf().autofmt_xdate()
# display graph
plt.show()
