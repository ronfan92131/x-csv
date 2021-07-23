# input: csv file
# output: calculate average current, vlo and power
# what to do:
# read raw.txt file, line-by-line, until the end of file. 

from csv import reader 

import sys
import datetime

file_in = sys.argv[1]
# open file in read mode
with open(file_in, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    #csv_reader = reader(read_obj)
    csv_reader = reader(read_obj, delimiter = '\t')
    # Iterate over each row in the csv using reader object
    
    counter = 0
    power_sum = 0
    voltage_sum = 0
    current_sum = 0
    power_min = 100
    power_max = 0
    
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)
        elements = str(row).split(',')
        try:
            num = int(elements[0][2:])
            #print(str(num))         
            volt = float(elements[1])
            voltage_sum += volt
            curr = float(elements[2][:-2])
            current_sum += curr
            #print(str(num) + "  " + str(volt) + "  " + str(curr))            
            power = volt * curr;
            power_sum += power
            if power_min > power:
                power_min = power
            if power_max < power:
                power_max = power

            counter += 1
            
        except ValueError:
            pass      
    #print("total pts: " + str(counter)  + " total power: " + str(pow_sum))
    
    power_ave = power_sum/counter
    current_ave = current_sum/counter
    voltage_ave = voltage_sum/counter
    test_time = counter * 0.01
    #output format
    # filename
    # power_ave
    # power_min
    # power_max
    # current_ave
    # voltage_ave
    # counts
    # interval
    print(file_in)
    print(f'{power_ave:6.4f}')
    print(f'{power_min:6.4f}')
    print(f'{power_max:6.4f}')
    print(f'{current_ave:6.4f}')
    print(f'{voltage_ave:6.4f}')
    print(f'{test_time:6.2f}')
   # print(f'(test_time:6.2f)')
    #print("min: " + str(pow_min) + " ave: " + str(pow_ave) + " max: " + str(pow_max))