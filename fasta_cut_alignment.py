__author__ = 'TramAnh'

infile = 'Data/fasta_output.txt'
alr_cut_file = 'Data/fasta_alr_cut.txt'

def get_sequence(infile, dict):
    with open(infile, 'rb') as f:
        value = ''
        key = ''
        for line in f:
            if '>' in line:
                if value and key:
                    dict[key] = value
                value = ''
                key = line.strip()[1:]
            else:
                value += line.strip()

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



dict= {}
get_sequence(infile, dict)

print 'Cut left:'
seq1, l_cut = get_lcut_position(dict)  # Return ['key', pos] => only consider the position
print seq1, l_cut

print '\nCut right:'
seq2, r_cut = get_rcut_position(dict)
print seq2, r_cut

write_cut_seq(dict, l_cut, r_cut)


# print dict
