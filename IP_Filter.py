#Programmer name: Tunmi:se Eboda
#Program date: december 9th, 2022
#My twenty-third tbh i lost count program 
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
    except:
        print()
        print(f'Error-- There is an issue with file {input_filename}. Please reenter: ')
    finally:
        if input1:
            input1.close()  # Close the file in the finally block
    return [compromised_ip, count, compromised_ip_dates, input1]


def output_file(output_filename):
    try:
        output = open(output_filename, "w")
        return output
    except:
        print()
        print(f'Error-- There is an issue with file {output_filename}. Please reenter: ')





input_filename = input('Enter the input file name: ')
input_ = input_file(input_filename)


total_ips = input_[1]
suspect_ip = len(input_[0])
percentage = suspect_ip/total_ips


while True:
    output_filename = input('Enter the output file name: ')
    output_ = output_file(output_filename)

    if(output_):
        print()
        print('Output Report')
        print('-------------')
        print('The total number of records in the file is: ',total_ips)
        print()
        print('The number of suspect IP addresses is: ', suspect_ip)
        print()
        print('The percentage of suspect IP addresses is: %.4f' % percentage)
        print()
        print('Suspect IP Addresses')
        print('--------------------')
        print()
        print('Ip Address = ', input_[0][0], ' Date and Time = ',input_[2][0])
        print()
        print('Ip Address = ', input_[0][1], ' Date and Time = ',input_[2][1])
        print()
        print('Ip Address = ', input_[0][2], ' Date and Time = ',input_[2][2])
        print()
        print('Ip Address = ', input_[0][3], ' Date and Time = ',input_[2][3])
        print()
        print('Ip Address = ', input_[0][4], ' Date and Time = ',input_[2][4])
        print()
        print('Ip Address = ', input_[0][5], ' Date and Time = ',input_[2][5])
        print()
        print('Ip Address = ', input_[0][6], ' Date and Time = ',input_[2][6])
        print()
        print('Ip Address = ', input_[0][7], ' Date and Time = ',input_[2][7])
        print()
        print('Ip Address = ', input_[0][8], ' Date and Time = ',input_[2][8])
        print()
        print('Ip Address = ', input_[0][9], ' Date and Time = ',input_[2][9])
        print()
        print('Ip Address = ', input_[0][10], ' Date and Time = ',input_[2][10])
        print()
        print('Ip Address = ', input_[0][11], ' Date and Time = ',input_[2][11])
        print()
        print('Ip Address = ', input_[0][12], ' Date and Time = ',input_[2][12])
        print()
        print('Ip Address = ', input_[0][13], ' Date and Time = ',input_[2][13])
        print()
        print('Ip Address = ', input_[0][14], ' Date and Time = ',input_[2][14])
        print()
        print('Ip Address = ', input_[0][15], ' Date and Time = ',input_[2][15])
        print()
        print('Ip Address = ', input_[0][16], ' Date and Time = ',input_[2][16])
        print()
        print('Ip Address = ', input_[0][17], ' Date and Time = ',input_[2][17])
        print()
        print('Ip Address = ', input_[0][18], ' Date and Time = ',input_[2][18])
        print()
        
        
        break
    else:
        continue

output_.close
print()
print('program complete')
