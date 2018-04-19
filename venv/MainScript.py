from Signature import print_signature
from Engine import generate
import os

print_signature()

loop = True
while loop:
    targetDirectory = input('Enter target directory or hit enter if its your current directory: ')

    if targetDirectory == '':
        targetDirectory = os.getcwd()

    if os.path.isdir(targetDirectory):
        loop = False
    else:
        print("Target directory dosen't exists! Please provide a valid directory...\n")


outputFileName = input('Enter output filename: ')
outputDirectory = targetDirectory+'/output'


print('target directory = ', targetDirectory, '\noutput directory = ', outputDirectory)

try:
    generate(outputDirectory, outputFileName)
    print("\nThank you !!!")
except Exception as e:
    print("\nAn Error Occurred !\n", e.args)




