import csv
from radio_variables_1 import radio
radio = 0
with open("changable_var.csv", "a") as radio_read_write_csv:
    write = csv.writer(radio_read_write_csv)
    write.writerow(["radio", radio])