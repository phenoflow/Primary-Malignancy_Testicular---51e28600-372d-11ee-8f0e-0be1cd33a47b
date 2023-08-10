# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"15148.0","system":"med"},{"code":"15989.0","system":"med"},{"code":"19475.0","system":"med"},{"code":"21786.0","system":"med"},{"code":"2961.0","system":"med"},{"code":"36325.0","system":"med"},{"code":"38510.0","system":"med"},{"code":"48808.0","system":"med"},{"code":"64602.0","system":"med"},{"code":"7740.0","system":"med"},{"code":"91509.0","system":"med"},{"code":"9476.0","system":"med"},{"code":"96429.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_testicular-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["primary-malignancy_testicular---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["primary-malignancy_testicular---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["primary-malignancy_testicular---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
