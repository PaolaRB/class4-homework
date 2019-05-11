import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Script to transpose a Dataset')
parser.add_argument('file_path', type=str, help='File path of the dataset')
args = parser.parse_args()

file_path = args.file_path

if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')


file = open(file_path)
corrected_file = []

for line in file.readlines():
    line_values = line.split(',')
    corrected_line = []
    for value in line_values:
        try:
            corrected_line.append(int(value))
        except:
            try:
                corrected_line.append(float(value))
            except:
                corrected_line.append(str(value))
    corrected_file.append(corrected_line)


print("Total records in corrected_file list = " + str(len(corrected_file)))
print("First row - slice 10: " + str(corrected_file[0][0:10]))
file.close()


# saving the data in a file without transposing columns
#file_path_no_trs = "/data/corrected_file_no_transposing.txt"
file_path_no_trs = "/app/data/corrected_file_no_transposing.txt"
with open(file_path_no_trs, '+w') as file_handler:
    for item in corrected_file:
        file_handler.write("{}\n".format(item))


transposed_list = []
for column in corrected_file[0]:
    transposed_list.append([])

for line in corrected_file:
    for idx, column in enumerate(line):
        transposed_list[idx].append(column)

print("Total records in transposed_list = " + str(len(transposed_list)))
print("First row - slice 10: " + str(transposed_list[0][0:10]))

#file_path = "/data/corrected_file_with_transposing.txt"
file_path = "/app/data/corrected_file_with_transposing.txt"
with open(file_path, '+w') as write_handler:
    for item in transposed_list:
        write_handler.write("{}\n".format(item))


print("------------- Reading with Pandas -------------- ")
file_path = args.file_path
df = pd.read_csv(file_path, sep=",", header=None)
print("-------------- Dataframe.head(5)---------------")
print(df.head(5))
print("--------------Standard deviation - first five values ------")
print(df.std().head(5))
print("--------------Mean - first five values---------------------")
print(df.mean().head(5))
