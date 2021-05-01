import csv
import sys
import numpy as np

if len(sys.argv) <= 1:
    print('No file provided')
    exit()

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    data = []
    for row in csv_reader:
        if line_count == 0:
                line_count += 1
        else:
            data.append(float(row[1]))
            line_count += 1

    std_dev = np.std(data)
    print('Standard deviation: %f' % (std_dev))
    print('2-Sigma: %f' % (std_dev*2))
    print('3-Sigma: %f' % (std_dev*3))

