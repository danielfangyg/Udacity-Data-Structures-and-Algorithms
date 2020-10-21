"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


if __name__ == '__main__':
    total_num_text = [s for t in texts
                      for i, s in enumerate(t) if (i == 0 or i == 1)]
    total_num_calls = [s for c in calls
                       for i, s in enumerate(c) if (i == 0 or i == 1)]
    total_num = total_num_text + total_num_calls
    total_num_dedupe = set(total_num)
    total_len = len(total_num_dedupe)
    print("There are {} different telephone " +
          "numbers in the records.".format(total_len))
