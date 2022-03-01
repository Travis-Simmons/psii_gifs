import glob
import subprocess
import shutil
import os
from PIL import Image

"""
This script takes in the output of 

https://github.com/phytooracle/rgb_flir_plot_clip_geojson.git

being run on many individual psii tiles.

The output of the above script looks like

psii_plotclip/date/plot/img.tif

This script then takes in the top level directory as the indir argument and first sorts the images like:

plot_sorting/plot/date1_plot1.tif date2_plot1.tif ...

It then goes in each plot directory and makes a tif out of all the images inside

Bug:

During the overlap phase of hte plotclip script wrong images are being brought in for visualization



"""

indir = 'psii_plotclip'

# Find all dates
all_dates = glob.glob(os.path.join(indir, '*'));all_dates

# Create output directory
if not os.path.exists('plot_sorting'):
    os.mkdir('plot_sorting')

# For each plot each day, sort them as described above
for i in all_dates:
    plots = glob.glob(os.path.join(i, '*'))
    date = os.path.basename(i)

    for x in plots:

        plot = os.path.basename(x)

        plot_folder = os.path.join('plot_sorting', plot)

        if not os.path.exists(plot_folder):
            os.mkdir(plot_folder)


        images = glob.glob(os.path.join(x, '*'))
        cnt = 0
        for z in images:
        

            new_filename = date+'_'+plot +'_'+ str(cnt)+'.tif'
            shutil.copyfile(z, os.path.join(plot_folder, new_filename))


# make gifs once sorted

# Make output directory
if not os.path.exists('gifs'):
    os.mkdir('gifs')

plots = glob.glob('plot_sorting/*')

for i in plots:

    imgs = glob.glob(os.path.join(i, '*'))

    frames = []
    for x in imgs:
        new_frame = Image.open(x)
        frames.append(new_frame)
    
    # Save into a GIF file that loops forever
    try:
        frames[0].save(os.path.join('gifs', os.path.basename(i)+'.gif'), format='GIF',
                    append_images=frames[1:],
                    save_all=True,
                    duration=800, loop=0)

    except:
        print(plot, 'didnt work')
