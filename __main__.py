#!/usr/bin/python

import sys
from os import listdir
from os import getcwd
from os.path import isfile, join
from parsing import read_log
from plot import plot

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: __main__.py <dir for log files>")
        print("Use . for current directory")
        sys.exit()
    else:
        print("loading data from " + sys.argv[1])
        all_data = []
        files = [f for f in listdir(sys.argv[1]) if isfile(f)]
        for f in files:
            if f.endswith('.log'):
                all_data.append(read_log(f))
        best_epoch = data[-1][0]
        del data[-1]
        plot(data, len(data[0]), best_epoch, labels=['Train', 'Validation', 'Test'])
