import os

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Use the material, Python Docs and Google as much as you want
#
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True
# Notes:
# * Use the already imported "os" module to check whether a given filename exists

def does_file_exist(filename):
    return filename in os.listdir()

# Purpose: get the contents of a given file and return them; if the file cannot be
# found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened // close(filename)
# * Use readlines() to read the contents
# * Use should use does_file_exist()

def get_file_contents(filename):
    if does_file_exist(filename):
        f = open(filename)
        text_file = f.readlines()
        return text_file
    else:
        return "This file cannot be found!"

# Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# boolean argument "include_header_row" is True, return the first header row
# from the filename as well (if it is False, omit that row)
# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# * should use get_file_contents() - N.B. as should any subsequent
# functions you write, using anything previously built if and where necessary

def christmas_day_air_quality(filename, include_header_row=False):
    def is_xmas_day(line):
        return '25/12' in line
    
    if include_header_row:
        xmas_day = [line for line in get_file_contents(filename) if line[0:5] == '25/12' or line[0:4] == 'Date']
        return xmas_day
    xmas_day = list(filter(is_xmas_day, get_file_contents(filename)))
    return xmas_day

# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;

def christmas_day_average_air_quality(filename):
    if does_file_exist(filename):
        xmas_data = list(filter(lambda line : '25/12' in line.split(';')[0], get_file_contents(filename)))
        all_xmas_pt_data = list(map(lambda value : int(value.split(';')[3]),xmas_data))
        avg_rounded = round(sum(all_xmas_pt_data)/len(all_xmas_pt_data), 2)
    return  avg_rounded

# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together\

def get_averages_for_month(filename):
    if does_file_exist(filename):
        monthly_avg = {}
        for i in range(1, 13):
            j = '%02d' % i
            month_data = list(filter(lambda line : j in line.split(';')[0][3:5], get_file_contents(filename)))
            month_selected_column = list(map(lambda value : int(value.split(';')[3]),month_data))
            avg = round(sum(month_selected_column)/len(month_selected_column), 2)   
            monthly_avg[i] = avg
    return monthly_avg

# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"

def create_march_data(filename):
    with open('AirQualityMarch.csv', 'x') as march_file: #open file and assign variable
        march_file.writelines(row for row in get_file_contents(filename) if '/03/' in row or 'Date' in row) #.writelines + list comprehension takes line by line from one file and writes in the new one

# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year

def create_monthly_responses(filename):
    os.mkdir('monthly_responses')
    list_of_months = list(set(row[3:10] for row in get_file_contents(filename)[1:])) #creates a list of months based on the index[3:10] of line. In this specific file, [3:10] represents 'mm/YYYY'. Uses set so it is not repeated. At the end, filename[1:] skips the firsts line(header)
    for month in list_of_months:
        with open(f'monthly_responses/{month.replace("/", "-")}.csv', 'x') as monthly_data: # monthly_responses/mm/YYYY becomes monthly_responses/mm-YYYY.csv with the f-string.
            monthly_data.writelines(row for row in get_file_contents(filename) if month in row[3:10] or 'Date' in row)
            #the line above does the same as the previous functions:
            #it uses file.writelines(listcomprehension) so it writes line by line from the original file to the new one. 