import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from tkinter import Tk, filedialog
import csv

# Create the Tkinter root window
root = Tk()
root.withdraw()  # Hide the root window

# Prompt the user to select multiple files
file_paths = filedialog.askopenfilenames(
    initialdir="Ref\CGGTTS",
    title="Select files",
    filetypes=(("All files", "*.*"),)
)

if file_paths:
    output_file = "rx-ref data.dat"  # Name of the combined output file
    lines_to_skip = 19  # Number of lines to skip from the beginning

    lines_rx_ref = []  # List to store the combined lines

    # Process each selected file
    for file_path in file_paths:
        # Open the file and skip the first 19 lines
        with open(file_path, "r") as infile:
            lines = infile.readlines()[lines_to_skip:]
            lines_rx_ref.extend(lines)

    # Write the combined lines to the output file
    with open(output_file, "w") as outfile:
        outfile.write("".join(lines_rx_ref))

else:
    print("No files selected.")

file_paths = filedialog.askopenfilenames(
    initialdir="ISTRAC Banglore",
    title="Select files",
    filetypes=(("All files", "*.*"),)
)

if file_paths:
    output_file = "ISTRAC data.dat"  # Name of the combined output file
    lines_to_skip = 19  # Number of lines to skip from the beginning

    lines_rx34 = []  # List to store the combined lines

    # Process each selected file
    for file_path in file_paths:
        # Open the file and skip the first 19 lines
        with open(file_path, "r") as infile:
            lines = infile.readlines()[lines_to_skip:]
            lines_rx34.extend(lines)

    # Write the combined lines to the output file
    with open(output_file, "w") as outfile:
        outfile.write("".join(lines_rx34))

    print("Lines combined successfully.")
else:
    print("No files selected.")

# Read the .dat file
with open('ISTRAC data.dat', 'r') as file:
    lines = file.readlines()

# Process each line in the file
for i in range(len(lines)):
    columns = lines[i].split()

    # Extract values from the desired columns
    first_column = columns[0]
    third_column = columns[2]
    fourth_column = columns[3]

    first_number = int(fourth_column[0:2])
    second_number = int(fourth_column[2:4])
    third_number = int(fourth_column[4:6])
    updated_first = first_number * 3600
    updated_second = second_number * 60
    updated_third = third_number*1
    decimal_value = (updated_first + updated_second + updated_third)*0.00001

    new_value = float(third_column) + float(decimal_value)
    eighth_column = columns[7]
    tenth_column = columns[9]

    # Multiply values by 0.1
    updated_eighth = float(eighth_column) * 0.1
    updated_tenth = float(tenth_column) * 0.1

    # Update the columns with the multiplied values
    columns[7] = str(updated_eighth)
    columns[9] = str(updated_tenth)

    columns[1] = str(new_value)

    # Create a new line with the selected columns
    new_line = f"{first_column} {new_value} {updated_eighth} {updated_tenth}\n"

    # Replace the original line with the new line
    lines[i] = new_line

# Write the updated data back to the .dat file
with open('ISTRAC data.dat', 'w') as file:
    file.writelines(lines)


# Read the .dat file
with open('rx-ref data.dat', 'r') as file:
    lines = file.readlines()

# Process each line in the file
for i in range(len(lines)):
    columns = lines[i].split()

    # Extract values from the desired columns
    first_column = columns[0]
    third_column = columns[2]
    fourth_column = columns[3]


    first_number = int(fourth_column[0:2])
    second_number = int(fourth_column[2:4])
    third_number = int(fourth_column[4:6])
    updated_first = first_number * 3600
    updated_second = second_number * 60
    updated_third = third_number * 1
    decimal_value = (updated_first + updated_second + updated_third)*0.00001

    new_value = float(third_column) + float(decimal_value)
    eighth_column = columns[7]
    tenth_column = columns[9]

        # Multiply values by 0.1
    updated_eighth = float(eighth_column) * 0.1
    updated_tenth = float(tenth_column) * 0.1

    # Update the columns with the multiplied values
    columns[7] = str(updated_eighth)
    columns[9] = str(updated_tenth)

    columns[1] = str(new_value)

    # Create a new line with the selected columns
    new_line = f"{first_column} {new_value} {updated_eighth} {updated_tenth}\n"

    # Replace the original line with the new line
    lines[i] = new_line

# Write the updated data back to the .dat file
with open('rx-ref data.dat', 'w') as file:
    file.writelines(lines)

def remove_row_by_element(file_path, element):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.split()[0] != element:
                lines.append(line)

    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)

    print(f"Row(s) with element '{element}' removed from '{file_path}'.")

# Usage example
element_to_remove = '6'

# remove_row_by_element('ISTRAC data.dat', element_to_remove)
# remove_row_by_element('rx-ref data.dat', element_to_remove)


def find_common_values(file1, file2):
    # Read and extract the first column from the first dataset
    with open(file1, 'r') as f1:
        first_column_1 = {line.split()[0] for line in f1}

    # Read and extract the first column from the second dataset
    with open(file2, 'r') as f2:
        first_column_2 = {line.split()[0] for line in f2}

    # Find the common values in both first columns
    common_values = first_column_1.intersection(first_column_2)

    return common_values

# Usage example
file1 = 'ISTRAC data.dat'
file2 = 'rx-ref data.dat'
common_values = find_common_values(file1, file2)
print(common_values)


def update_datasets(file1, file2, output_file1, output_file2):
    common_rows_file1 = []
    common_rows_file2 = []

    # Read and extract the first column from the first dataset
    with open(file1, 'r') as f1:
        rows_1 = [line.strip() for line in f1]
        first_column_1 = {line.split()[0] for line in rows_1}

    # Read and extract the first column from the second dataset
    with open(file2, 'r') as f2:
        rows_2 = [line.strip() for line in f2]
        first_column_2 = {line.split()[0] for line in rows_2}

    # Find the common values in both first columns
    common_values = first_column_1.intersection(first_column_2)

    # Find the common rows and append them to the respective lists
    for row in rows_1:
        if row.split()[0] in common_values:
            common_rows_file1.append(row)

    for row in rows_2:
        if row.split()[0] in common_values:
            common_rows_file2.append(row)

    # Write the common rows to the respective output files
    with open(output_file1, 'w') as f1_out:
        for row in common_rows_file1:
            f1_out.write(row + '\n')

    with open(output_file2, 'w') as f2_out:
        for row in common_rows_file2:
            f2_out.write(row + '\n')

    print(f"Common rows in '{file1}' have been saved in '{output_file1}'.")
    print(f"Common rows in '{file2}' have been saved in '{output_file2}'.")

# Usage example
file1 = 'ISTRAC data.dat'
file2 = 'rx-ref data.dat'
output_file1 = 'cva ISTRAC.dat'
output_file2 = 'cva rx-ref.dat'

update_datasets(file1, file2, output_file1, output_file2)

input_file = "cva rx-ref.dat"  # Path to the input .dat file
output_file = "avg cva rx-ref.dat"  # Path to the output file

group_sums = {}  # Dictionary to store the sums for each group
group_counts = {}  # Dictionary to store the counts for each group

# Read the input file and process the data
with open(input_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            values = line.split()
            second_column_value = float(values[1])
            fourth_column_value = float(values[3])

            # Add the value to the group's sum
            group_sums[second_column_value] = group_sums.get(second_column_value, 0) + fourth_column_value

            # Increment the count for the group
            group_counts[second_column_value] = group_counts.get(second_column_value, 0) + 1

# Calculate the average for each group
group_averages = {group: group_sums[group] / group_counts[group] for group in group_sums}

# Write the averages to the output file
with open(output_file, 'w') as file:
    for group, average in group_averages.items():
        file.write(f"{group}\t{average}\n")

input_file = "cva ISTRAC.dat"  # Path to the input .dat file
output_file = "avg cva ISTRAC.dat"  # Path to the output file

group_sums = {}  # Dictionary to store the sums for each group
group_counts = {}  # Dictionary to store the counts for each group

# Read the input file and process the data
with open(input_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            values = line.split()
            second_column_value = float(values[1])
            fourth_column_value = float(values[3])

            # Add the value to the group's sum
            group_sums[second_column_value] = group_sums.get(second_column_value, 0) + fourth_column_value

            # Increment the count for the group
            group_counts[second_column_value] = group_counts.get(second_column_value, 0) + 1

# Calculate the average for each group
group_averages = {group: group_sums[group] / group_counts[group] for group in group_sums}

# Write the averages to the output file
with open(output_file, 'w') as file:
    for group, average in group_averages.items():
        file.write(f"{group}\t{average}\n")

def find_difference(file1, file2, output_file):
    # Read and extract the first column from the first dataset
    with open(file1, 'r') as f1:
        lines_1 = [line.strip() for line in f1]
        first_column_1 = {line.split()[0] for line in lines_1}

    # Read and extract the first column from the second dataset
    with open(file2, 'r') as f2:
        lines_2 = [line.strip() for line in f2]
        first_column_2 = {line.split()[0] for line in lines_2}

    # Find the unique elements in the first column
    unique_elements = first_column_1.union(first_column_2)

    # Calculate the difference of the elements in the second column
    difference = []
    for element in unique_elements:
        second_col_1 = [line.split()[1] for line in lines_1 if line.split()[0] == element]
        second_col_2 = [line.split()[1] for line in lines_2 if line.split()[0] == element]

        if len(second_col_1) == 1 and len(second_col_2) == 1:
            diff = float(second_col_1[0]) - float(second_col_2[0])
            difference.append(f"{element} {diff}")

    # Sort the difference data based on the first column elements
    difference.sort(key=lambda x: float(x.split()[0]))

    # Write the difference of the elements to the output file
    with open(output_file, 'w') as output:
        for diff in difference:
            output.write(diff + '\n')

    print(f"Difference of elements in the second column has been saved in '{output_file}'.")

# Usage example
file1 = 'avg cva rx-ref.dat'
file2 = 'avg cva ISTRAC.dat'
output_file = 'cva difference.dat'

find_difference(file1, file2, output_file)

def plot_graph(file_path):
    x = []
    y = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.split()
            x.append(float(data[0]))
            y.append(float(data[1]))

    plt.plot(x, y,marker = 'o',color = 'blue')
    plt.xlabel('MJD',fontsize = 15)
    plt.ylabel('Time Difference ( ns)',fontsize = 15)
    plt.title('NaVIC Commom View time difference between two receivers ',fontsize = 25)
    plt.grid(b=True, which='major',  lw='1', color='black', linestyle='-')
    plt.grid(b=True, which='minor', axis='x', color='black', linestyle='--')
    plt.ticklabel_format(useOffset=False)
    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=15)
    #plt.tick_params([-5, -15, -25, -35, -45], minor=True)
    plt.show()

# Usage example
file_path = 'cva difference.dat'

plot_graph(file_path)

def plot_comparison(file1, file2):
    # Load the data from the first file
    data1 = np.loadtxt(file1)

    # Extract x and y values from the first file
    x1 = data1[:, 0]
    y1 = data1[:, 1]

    # Load the data from the second file
    data2 = np.loadtxt(file2)

    # Extract x and y values from the second file
    x2 = data2[:, 0]
    y2 = data2[:, 1]

    # Create the comparison plot
    plt.plot(x1, y1, label='Common View')
    plt.plot(x2, y2, label='All in View')
    plt.xlabel('MJD')
    plt.ylabel('Difference (in ns)')
    plt.title('Common View vs All in View')
    plt.legend()
    plt.show()

# Usage example
file1 = 'cva difference.dat'
file2 = 'ava plot.dat'

plot_comparison(file1, file2)