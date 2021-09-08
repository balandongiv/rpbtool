import os



def check_make_folder(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def load_file(fname,warning_level=None):
    import pickle
    if not os.path.isfile(fname):
        if warning_level is not None:

            raise ValueError ('Try to upload something that not there')

    with open(fname, 'rb') as handle:
        file = pickle.load(handle)
    return file



def easy_sort_idx(wind_name, window_size):
    import numpy as np
    '''
    Extract the 2D coordinate only for window with the 0s on it. This usually helpfull to sort the figure
    '''
    # window_size, txt = 7,['-25:-20', '-20:-15', '-15:10', '-10:-5', '-5:0', '0:5', '5:10']
    ref_val = [i for i in range(len(wind_name)) if '0' in wind_name[i].split(":")]
    bt, lf = np.tril_indices(window_size, -1)
    pos_window = 0

    indices = np.where(bt == ref_val[pos_window])
    idx_pair_for_easy_sorting = [bt[indices], lf[indices]]

    # old approach
    # idx_pair = np.tril_indices ( window_size, -1 )
    # lateral = idx_pair [0].tolist ()
    #
    # idx2 = [idc for idc, val_x in enumerate ( lateral ) if val_x in [ref_val[pos_window]]]
    # idx_pair_for_easy_sorting = [i [idx2] for i in idx_pair]
    return idx_pair_for_easy_sorting




def get_sub_folder(path):
    return [f.path for f in os.scandir(path) if f.is_dir()]