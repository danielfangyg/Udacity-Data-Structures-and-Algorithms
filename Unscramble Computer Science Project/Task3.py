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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def get_prefix(num_str):
    if " " in num_str:
        return num_str.split(" ")[0]
    elif ")" in num_str:
        return num_str.split(")")[0].split("(")[1]
    else:
        assert int(num_str[:3]) == 140
        return num_str[:3]


if __name__ == '__main__':
    '''Part A'''
    called_by_B = [c[1] for c in calls if c[0][:5] == "(080)"]
    prefixes = [get_prefix(num) for num in called_by_B]
    prefixes_dedupe = list(set(prefixes))
    prefixes_dedupe.sort()
    print("The numbers called by people in Bangalore have codes:")
    for prefix in prefixes_dedupe:
        print(prefix)

    '''Part B'''
    dict_prefix = {p: prefixes.count(p) for p in prefixes}
    perc = round(100 * dict_prefix["080"]/len(prefixes), 2)
    print("{} percent of calls from fixed lines in Bangalore " +
          "are calls to other fixed lines in Bangalore.".format(perc))
