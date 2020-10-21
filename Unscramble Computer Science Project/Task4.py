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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


if __name__ == '__main__':
    total_num_text = [s for t in texts
                      for i, s in enumerate(t) if (i == 0 or i == 1)]
    total_rec_num_calls = [s for c in calls
                           for i, s in enumerate(c) if i == 1]
    excl_list = list(set(total_num_text + total_rec_num_calls))
    telmkter_list = [c[0] for c in calls if c[0] not in excl_list]
    telmkter_list_dedupe = list(set(telmkter_list))
    telmkter_list_dedupe.sort()
    print("These numbers could be telemarketers: ")
    for num in telmkter_list_dedupe:
        print(num)
