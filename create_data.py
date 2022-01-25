import pickle
import pandas as pd
import os
from glob import glob
import sys
from tqdm import tqdm
from pathlib import PurePath

trainPath = sys.argv[1]
testPath = sys.argv[2]
labelPath = sys.argv[3]

labels = pd.read_csv( str( labelPath ) )

image_to_labels = labels.set_index('image').T.to_dict('records')[0]

trainImages = glob( os.path.join( trainPath, "*.jpeg" ) )
testImages = glob( os.path.join( testPath, "*.jpeg" ) )

print("Training images : ", len(trainImages))
print("Test images : ", len(testImages))

final_dict = {}
final_dict['train'] = []
for img in tqdm( trainImages, desc="Making training dataset pickle" ):
	path = PurePath(img).parts[-1].replace(".jpeg", "")
	label = image_to_labels[ path ]
	final_dict['train'].append( (path, int(label) ) )

final_dict['test'] = []
for img in tqdm( trainImages, desc="Making test dataset pickle" ):
	path = PurePath(img).parts[-1].replace(".jpeg", "")
	label = image_to_labels[ path ]
	final_dict['test'].append( (path, int(label) ) )

with open("./dataset.pickle", "wb") as handle:
	pickle.dump( final_dict, handle, pickle.HIGHEST_PROTOCOL )