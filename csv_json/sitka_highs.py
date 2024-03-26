import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:

    reader = csv.reader(f)
    header_row = next(reader)

    # get dates and high temps
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# plot high temps
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")

# format plot
ax.set_title("daily high temps, 2018")
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("temp (F)", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
