"""
This will take a vcf file name as FILENAME, and will check all columns that have
more than 1bp in either REF or ALT and replace the value with the first
bp in the column

Jake Landers 2022
"""

import sys

if len(sys.argv) < 2:
    print("Input filename is required as first arguments")
    exit(1)


# file want to parse
FILENAME = sys.argv[1]

# hold new file in memory as creating
new_file_lines = []

# open in read mode
with open(FILENAME, "r", encoding="utf=8") as file:
    # loop over lines in the file
    for line in file:
        # ignore headers
        if line[0] == "#":
            new_file_lines.append(line)
        else:
            # vcf file has column headers as follows:
            # 0 = #CHROM | 1 = POS | 2 = ID | 3 = REF | 4 = ALT | 5 = QUAL
            # need to check index 3 and 4 for >1 chars. If so, then replace
            # both with an N.

            # split lines by tabs
            items = line.split("\t")
            # check ref
            if len(items[3]) > 1:
                items[3] = items[3][0]
            if len(items[4]) > 1:
                items[4] = items[4][0]

            # join line with tabs and add to new file
            new_file_lines.append("\t".join(items))

# concat all lines into a single string and write to new file
new_file_name = FILENAME.split(".")
new_file_name.pop()
new_file_name = "./" + ".".join(new_file_name) + ".modified.vcf"
new_file = open(new_file_name, "w", encoding="utf-8")
new_file.write("".join(new_file_lines))
new_file.close()
print(f"Successfully created file: {new_file_name}")
