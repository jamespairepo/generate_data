import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:

    reader = csv.reader(f)
    header_row = next(reader)

    # get dates, highs, lows
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# plot high, low temps
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# format plot
ax.set_title("daily high, low temps, 2018")
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("temp (F)", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
