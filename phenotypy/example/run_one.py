import __init__
import phenotypy as pnt
cla = pnt.Classifier(path_list=['training_data/fore_rm_y.png',
                                'training_data/back.png'],
                     kind_list=[0, -1], core='dtc')

plot1 = pnt.Plot(r'D:\OneDrive\Documents\4_PhD\11_[Paper]AutoPhenoPaper\Data\sfm\S03.ply', cla)
plot1.auto_segmentation(denoise=True, ascending=True, img_folder='plot_out')
traits = plot1.get_traits(container_ht=0.057)    # size in meter
traits.to_csv('S03/plot1.csv')