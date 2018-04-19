import os
import shutil

directories = ["drawable-mdpi", "drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi", "drawable-xxxhdpi"]


def generate(outDirectory, outFileName):
    if os.path.isdir(outDirectory):
        consent = input("\nOutput directory "+outDirectory + ' already exists! OVERRIDE? Type \'y\' to continue... ')
        if consent == 'y' or consent == 'Y':
            shutil.rmtree(outDirectory)
        else:
            print('\nRequest Cancelled! Aborting...')
            return

    os.mkdir(outDirectory)
    for i in range(5):

        child_directory = (outDirectory+"/"+directories[i]+"/")
        os.mkdir(child_directory)
        file = open(child_directory+"/"+outFileName, "w+")
        file.writelines("")
        file.close()

