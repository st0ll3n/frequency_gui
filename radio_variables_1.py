# ["0xfe", "0xfe", "0x94", "0xe0", "0x00", "0x00", "0x60", "0x50", "0x03", "0x00", "0xfd"]
# ["0xfe", "0xfe", "0x94", "0xe0", "0x03", "0xfd"] # read frequency
# todo: attach certain commands to fill in the variables with elif commands?
# todo:  html file changes radio = by button,
import csv
with open ('changable_var.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter=',')
    line_count=0
    for row in csv_reader:
                #  Article1=row['Test1']
                #  Article2=row['Test2']
                #  print(Article1)
                #  print(Article2)
                #  todo: write loop for checking for radio commented above is trash, and placeholder
                #  the above is for reading radio from csv file set by variable_to_csv.py
        csv_file.close()
radio = 1  # change this to 0 to read the frequency, or 1 to send the frequency in the if statement
radio_frequency = 3955
hihi = "0xfe"
hiradio = "0x94"
hicomp = "0xe0"
hicom6 = "0x00"
hiend = "0xfd"
if radio == 1:  # write frequency
    print("send radio frequency")
    hicom1 = "0x00"
    # todo: set radio_frequency variables to convert from radio_frequency
    hicom2 = "0x00"
    hicom3 = "0x60"
    hicom4 = "0x95"
    hicom5 = "0x03"
    # end of radio frequency
    hihihi = [hihi, hihi, hiradio, hicomp, hicom1, hicom2, hicom3, hicom4, hicom5, hicom6, hiend]
#elif radio == 0: # read frequency
#    hicom1 = "0x03"
#    hihihi = [hihi, hihi, hiradio, hicomp, hicom1, hiend]
#    print("get radio frequency")
else:
    print('radio variable has to be = 0 or 1')
# todo: create a loop for constantly(at an interval) getting the frequency, until radio=1, either here or send request
