__author__ = 'TramAnh'

import csv

infile = 'Data/alignment/fasta_output.txt'
alr_cut_file = 'Data/alignment/fasta_alr_cut.txt'
csv_file = 'Data/alignment/trainval_aligned.csv'

def get_sequence(infile, dict):
    with open(infile, 'rb') as f:
        value = ''
        key = ''
        for line in f:
            if '>' in line:     # Header '>..' line. Add (k,v) to dict and reset value and key
                if value and key:
                    dict[key] = value
                value = ''
                key = line.strip()[1:]
            else:
                value += line.strip()   # Concatenate value

def put_seq_to_array(infile):
    arr = []
    with open(infile, 'rb') as f:
        id=''
        wt_seq = ''
        m_seq = ''
        temp = ''
        for line in f:
            line = line.strip()
            if '>' in line:
                if 'W' in line:
                    if id:
                        m_seq = temp
                        arr.append([wt_seq, m_seq])
                        temp = ''
                if 'M' in line:
                    wt_seq = temp
                    id = line[1:-1]
                    temp = ''
            else:
                temp += line.strip()
    return arr

def get_lcut_position(dict):
    half = len(dict)/2

    max_pos =0
    seq_name = ''
    for key in dict:
        half_seq = dict[key][:half]
        pos = half_seq.rfind('-')
        max_pos1 = max(pos, max_pos)
        seq_name = key if max_pos1 != max_pos else seq_name
        max_pos = max_pos1

    return seq_name, max_pos

def get_rcut_position(dict):
    half = len(dict)/2

    min_pos = half
    seq_name = ''
    for key in dict:
        half_seq = dict[key][half:]
        try:
            pos = half_seq.index('-')        # Return -1 if cant find
        except:
            pos = half
        min_pos1 = min(pos, min_pos)
        seq_name = key if min_pos1 != min_pos else seq_name
        min_pos = min_pos1

    rcut = half+ min_pos

    return seq_name, rcut

def write_cut_seq(dict, lcut, rcut):
    with open(alr_cut_file, 'wb') as f:
        for key in dict:
            f.write(key+'\n')
            f.write(dict[key][lcut+1:rcut]+'\n')

def write_arr_to_csv(arr, lcut, rcut):
    with open(csv_file, 'wb') as f:
        csvwriter = csv.writer(f)
        for each in arr:
            wt = each[0][lcut+1:rcut]
            m = each[1][lcut+1:rcut]
            csvwriter.writerow([wt, m])


dict= {}
get_sequence(infile, dict)

arr = put_seq_to_array(infile)

print 'Cut left:'
seq1, l_cut = get_lcut_position(dict)  # Return ['key', pos] => only consider the position
print seq1, l_cut

print '\nCut right:'
seq2, r_cut = get_rcut_position(dict)
print seq2, r_cut
#
# write_cut_seq(dict, l_cut, r_cut)

write_arr_to_csv(arr, l_cut, r_cut)


# print dict
