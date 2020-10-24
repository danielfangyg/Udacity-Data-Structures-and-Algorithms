"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

if __name__ == '__main__':
    time_dict = {}
    for c in calls:
        time_dict[c[0]] = time_dict.get(c[0], 0) + int(c[3])
        time_dict[c[1]] = time_dict.get(c[1], 0) + int(c[3])
    max_num = max(time_dict, key=time_dict.get)
    max_time = time_dict[max_num]
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_num, max_time))
