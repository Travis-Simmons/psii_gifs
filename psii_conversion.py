# sorting
import glob
import subprocess
import shutil


all_dates = glob.glob('psii_plotclip/*');all_dates

if not os.path.exists('plot_sorting'):
    os.mkdir('plot_sorting')


for i in all_dates:
    plots = glob.glob(os.path.join(i, '*'))
    date = os.path.basename(i)
    print(date)
    
    
    for x in plots:
        

        plot = os.path.basename(x)

        plot_folder = os.path.join('plot_sorting', plot)

        if not os.path.exists(plot_folder):
            os.mkdir(plot_folder)


        images = glob.glob(os.path.join(x, '*'))
        cnt = 0
        for z in images:
        

            new_filename = date+'_'+plot +'_'+ str(cnt)+'.tif'
            # print(new_filename)
            shutil.copyfile(z, os.path.join(plot_folder, new_filename))


# make gifs once sorted


from PIL import Image
import glob
 
# Create the frames

# imgs = glob.glob("2000_psii_set_png/*.png")

# plot level 

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
