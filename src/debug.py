import os
import tqdm

valid_calsses = ['1011', '1012', '1013', '1100', '2050', '1040', '1030', '1120', '1110', '1135', '4000', '5010', '1003', '1002', '1070', '2010', '2000']
for file in tqdm.tqdm(os.listdir('data\\labels\\train')):
    path = 'data/labels/train/' + file
    with open(path) as f:
        content = f.readlines()
    for line in content:
        line = line.split(' ')
        # print(line[0])
        if line[0] not in valid_calsses:
            print(line[0])

        else:
            pass