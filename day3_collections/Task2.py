temperatures=[22,24,25,28,30,29,27,26,24,22]
first_reading=temperatures[0]
last_reading=temperatures[-1]
print("First reading",first_reading)
print("Last reading",last_reading)
afternoon_peak=temperatures[3:6]
print("Afternoon Peak",afternoon_peak)
last_3_hours=temperatures[-3:]
print("Last 3 Hours",last_3_hours)