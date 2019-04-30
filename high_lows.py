import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get high temperatures from files 
filename_one = 'death_valley_2014.csv'
with open(filename_one) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get current dates low and high temperatures from file
    dates_one, highs_one, lows_one = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_one.append(current_date)
            highs_one.append(high)
            lows_one.append(low)
          
filename_two = 'sitka_weather_2014.csv'
with open(filename_two) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get current dates low and high temperatures from file
    dates_two, highs_two, lows_two = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_two.append(current_date)
            highs_two.append(high)
            lows_two.append(low)

# Plot data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates_one, highs_one, c='red')
plt.plot(dates_one, lows_one, c = 'blue')
plt.fill_between(dates_one, highs_one, lows_one, facecolor = 'blue', 
    alpha=.1)

plt.plot(dates_two, highs_two, c='green')
plt.plot(dates_two, lows_two, c = 'yellow')
plt.fill_between(dates_two, highs_two, lows_two, facecolor = 'green', 
    alpha=.5)

# Format plot
title = "Daily high and low temperatures - 2014 \nDeath Valley, CA"
plt.title(title, fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.ylim((20, 120))

plt.show()
