import open3d as o3d
import numpy as np
from plyfile import PlyData
from phenotypy.pcd_tools import merge_pcd

def read_ply(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    if not pcd.has_colors():
        cloud_ply = PlyData.read(file_path)
        cloud_data = cloud_ply.elements[0].data
        ply_names = cloud_data.dtype.names

        if 'red' in ply_names:
            colors = np.vstack((cloud_data['red'] / 255, cloud_data['green'] / 255, cloud_data['blue'] / 255)).T
            pcd.colors = o3d.utility.Vector3dVector(colors)
        elif 'diffuse_red' in ply_names:
            colors = np.vstack((cloud_data['diffuse_red'] / 255, cloud_data['diffuse_green'] / 255,
                                cloud_data['diffuse_blue'] / 255)).T
            pcd.colors = o3d.utility.Vector3dVector(colors)
        else:
            print('Can not find color info in ', ply_names)

    return pcd

def read_plys(file_list):
    """
    read a bunch of ply (e.g. two ply), and merge them into one (without registration, just add x,y,z one by one)
    :param file_list: ['file1.ply', 'file2.ply']
    :return: o3d.geometry.pointclouds
    """
    pcd_list = []
    for file_path in file_list:
        pcd_list.append(read_ply(file_path))

    return merge_pcd(pcd_list)

def write_ply(file_path):
    pass