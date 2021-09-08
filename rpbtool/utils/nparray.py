import numpy as np

def mesh_cor(x_max, y_max, **kwargs):
    x_min, y_min, z_min, w_min = 0, 0, 0, 0

    w_max = kwargs.get('w_max', None)
    w_axis = np.arange(w_min, w_max, dtype='int32') if 'w_max' in kwargs else None

    z_max = kwargs.get('z_max', None)
    z_axis = np.arange(z_min, z_max, dtype='int32') if 'z_max' in kwargs else None

    x_axis = np.arange(x_min, x_max, dtype='int32')
    y_axis = np.arange(y_min, y_max, dtype='int32')

    if w_axis is not None:
        mesh_coor = np.vstack(np.meshgrid(y_axis, x_axis, z_axis, w_axis)).reshape(4, -1).T
    elif z_axis is not None:
        mesh_coor = np.vstack(np.meshgrid(y_axis, x_axis, z_axis)).reshape(3, -1).T
    else:
        mesh_coor = np.vstack(np.meshgrid(y_axis, x_axis)).reshape(2, -1).T

    # swap and output is # output: method,band
    mesh_coor[:, [1, 0]] = mesh_coor[:, [0, 1]]
    return mesh_coor