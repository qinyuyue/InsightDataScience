import csv
import numpy as np

# open file
# filename = raw_input('Please enter your file name(with CSV format): ')
# with open (filename, 'r') as f:
# with open ('test.csv', 'rb') as f:
#     reader = csv.reader(f, delimiter=';')
#     h1b = list(reader)

# h1b = csv.reader(open('test.csv'), delimiter=';', quotechar=';')

# h1b = np.genfromtxt('test.csv', delimiter=';')
# print h1b

handle = open('test1.csv', 'r')
contents = handle.read()
handle.close()
rows = contents.split('\n')
h1b = np.array([[i for i in r.split(';')] for r in rows if r])

# h1b = np.asarray(h1b)
# for i in range(5):
#     print np.shape(h1b[i])
# seperate the whole list to its header and its body
h1b_header = list(h1b[0])
h1b_stat = h1b[1:]
# print h1b_stat

# status = h1b_header.index('STATUS')
# soc_code = h1b_header.index('LCA_CASE_SOC_CODE')
# state = h1b_header.index('LCA_CASE_WORKLOC1_STATE')

# top 10 occupation name
def get_top10_occupations(h1b_header, h1b_stat):
    # write file

    # get the index of occupation and status
    status_idx = h1b_header.index('STATUS')
    soc_name_idx = h1b_header.index('LCA_CASE_SOC_NAME')
    # print soc_name_idx
    # print h1b[:,14]
    # get the column of occupation and status
    soc_name = list(h1b_stat[:,soc_name_idx])
    # print soc_name
    status = list(h1b_stat[:,status_idx])

    # counting
    occupation = []
    uniq_soc_name = set(soc_name)
    # print uniq_soc_name
    for i in uniq_soc_name:
        soc_num = 0
        status_num = 0
        for j in range(len(soc_name)):
            if soc_name[j] == i:
                soc_num += 1
                if status[j] == 'CERTIFIED':
                    status_num += 1
        # percentage = float(status_num/soc_num)
        # print percentage
        row = [i, str(status_num), str(round(float(status_num)/soc_num,1))]
        # output.write(str(row))
        occupation.append(row)
        print ';'.join(row)
        # print i, soc_num, status_num
        # freq.update({i:num})

    # sort top10
    sorted_ocp = sorted(sorted(occupation, key=lambda a:a[0]),key = lambda a:a[1], reverse=True)

    output = open('top_10_occupations.txt','w')
    for row in sorted_ocp:
        output.write(';'.join(row)+'\n')
    output.close()
    return sorted_ocp
print get_top10_occupations(h1b_header, h1b_stat)
