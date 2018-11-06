# import csv
import numpy as np

# open file
# input = raw_input('Please enter your file name with path(CSV format): ')
# filename = '{0}{1}'.format('../input/', input)
# handle = open(filename, 'r')
handle = open('../input/h1b_input.csv', 'r')
contents = handle.read()
handle.close()
rows = contents.split('\n')
h1b = np.array([[i for i in r.split(';')] for r in rows if r])

# seperate the whole list to its header and its body
h1b_header = list(h1b[0])
h1b_stat = h1b[1:]

def get_top10_occupations(h1b_header, h1b_stat):
    # get the index of occupation and status
    if 'CASE_STATUS' in h1b_header:
        status_idx = h1b_header.index('CASE_STATUS')
    elif 'STATUS' in h1b_header:
        status_idx = h1b_header.index('STATUS')
    if 'SOC_NAME' in h1b_header:
        soc_name_idx = h1b_header.index('SOC_NAME')
    elif 'LCA_CASE_SOC_NAME' in h1b_header:
        soc_name_idx = h1b_header.index('LCA_CASE_SOC_NAME')
    soc_name = list(h1b_stat[:,soc_name_idx])
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
        row = [i, str(status_num), str("{:.0%}".format(round(float(status_num)/len(h1b_stat),1)))]
        occupation.append(row)
    # sort top10
    sorted_ocp = sorted(sorted(occupation, key=lambda a:a[0]),key = lambda a:a[1], reverse=True)
    # write file
    output = open('../output/top_10_occupations.txt','w')
    output.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    for row in sorted_ocp:
        output.write(';'.join(row)+'\n')
    output.close()
    return sorted_ocp

def get_top10_state(h1b_header, h1b_stat):

    # get the index of occupation and status
    if 'CASE_STATUS' in h1b_header:
        status_idx = h1b_header.index('CASE_STATUS')
    elif 'STATUS' in h1b_header:
        status_idx = h1b_header.index('STATUS')
    if 'LCA_CASE_WORKLOC1_STATE' in h1b_header:
        state_idx = h1b_header.index('LCA_CASE_WORKLOC1_STATE')
    elif 'WORKSITE_STATE' in h1b_header:
        state_idx = h1b_header.index('WORKSITE_STATE')
    state = list(h1b_stat[:,state_idx])
    status = list(h1b_stat[:,status_idx])
    # counting
    states = []
    uniq_state = set(state)
    for i in uniq_state:
        state_num = 0
        status_num = 0
        for j in range(len(state)):
            if state[j] == i:
                state_num += 1
                if status[j] == 'CERTIFIED':
                    status_num += 1
        percentage = "{:.0%}".format(round(float(status_num)/len(h1b_stat),1))
        row = [i, str(status_num), str("{:.0%}".format(round(float(status_num)/len(h1b_stat),1)))]
        states.append(row)

    # sort top10
    sorted_state = sorted(sorted(states, key=lambda a:a[0]),key = lambda a:a[1], reverse=True)

    # write file
    output = open('../output/top_10_states.txt','w')
    output.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    for row in sorted_state:
        output.write(';'.join(row)+'\n')
    output.close()
    return sorted_state

# run functions
get_top10_occupations(h1b_header, h1b_stat)
get_top10_state(h1b_header, h1b_stat)
