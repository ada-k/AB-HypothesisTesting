# import glob

# read_files = glob.glob("/home/ada/10academy/training /week4/*.txt")

# with open("requirements.txt", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())

import glob
files = glob.glob('/home/ada/10academy/training /week4/*.txt' )

with open( '/home/ada/10academy/training /week4/requirements.txt', 'w' ) as result:
    for file_ in files:
        for line in open( file_, 'r' ):
            result.write( line )