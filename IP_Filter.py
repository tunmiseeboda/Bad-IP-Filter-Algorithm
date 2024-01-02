#Programmer name: Tunmi:se Eboda
#Program date: december 9th, 2022
#Final coding project

import re

def input_file(input_filename):
    count = 0
    compromised_ip = []
    compromised_ip_dates = []
    input1 = None  # Initialize input1 outside the try block
    try:
        input1 = open(input_filename, "r")
        lines = input1.readlines()
        for line in lines:
            count += 1
            ip = line.split(" ")[0]
            dates = line.split(" ")[1:]
            test1 = re.search("168.193", ip)
            test2 = re.search("224.174", ip)
            test3 = re.search("233.012", ip)
            if test1 or test2 or test3:
                compromised_ip.append(ip)
                compromised_ip_dates.append(dates)
    except FileNotFoundError:
        print(f'\nError-- There is an issue with file {input_filename}. Please reenter: ')
    finally:
        if input1:
            input1.close()  # Close the file in the finally block
    return [compromised_ip, count, compromised_ip_dates, input1]


def output_file(output_filename):
    try:
        output = open(output_filename, "w")
        return output
    except IOError:
        print(f'\nError-- There is an issue with file {output_filename}. Please reenter: ')





input_filename = input('Enter the input file name: ')
input_ = input_file(input_filename)


total_ips = input_[1]
suspect_ip = len(input_[0])
percentage = suspect_ip/total_ips


while True:
    output_filename = input('Enter the output file name: ')
    output_ = output_file(output_filename)

    if(output_):
        print('\nOutput Report')
        print('-------------')
        print('The total number of records in the file is: ',total_ips)
        print('\nThe number of suspect IP addresses is: ', suspect_ip)
        print('\nThe percentage of suspect IP addresses is: %.4f' % percentage)
        print('\nSuspect IP Addresses')
        print('--------------------\n')
        
        for i in range(min(len(input_[0]), 19)):
              date_string = " ".join(input_[2][i])  # Remove brackets and newline characters
              output_.write("Ip Address = " + input_[0][i] + "   Date and Time = " + date_string + "\n")

        output_.close()  # Close the output file
        break

with open(output_filename, "r") as output:
    print(output.read())
print('program complete')
