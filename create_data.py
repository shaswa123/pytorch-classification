import pickle
import pandas as pd
import os
from glob import glob
import sys
from tqdm import tqdm
from pathlib import PurePath
import random

random.seed(1)

trainPath = sys.argv[1]
testPath = sys.argv[2]
trainLabelPath = sys.argv[3]
testLabelPath = sys.argv[4]

trainLabels = pd.read_csv( str( trainLabelPath ) )

image_to_labels = trainLabels.set_index('image').T.to_dict('records')[0]

trainImages = glob( os.path.join( trainPath, "*.jpeg" ) )
testImages = glob( os.path.join( testPath, "*.jpeg" ) )

print("Training images : ", len(trainImages))
print("Test images : ", len(testImages))

final_dict = {}
final_dict['train'] = []
for img in tqdm( trainImages, desc="Making training dataset pickle" ):
	path = PurePath(img).parts[-1].replace(".jpeg", "")
	label = image_to_labels[ path ]
	final_dict['train'].append( (img, int(label) ) )

assert len( trainImages ) == len( final_dict['train'] )

random.shuffle( final_dict['train'] )
val = final_dict['train'][ int( len(final_dict['train']) * 0.8 ) :  ]
final_dict['train'] = final_dict['train'][  : int( len(final_dict['train']) *0.8 ) ]
final_dict['val'] = val

testLabels = pd.read_csv( str( testLabelPath ) )[["image", "level"]]
image_to_labels = testLabels.set_index('image').T.to_dict('records')[0]

final_dict['test'] = []
for img in tqdm( testImages, desc="Making test dataset pickle" ):
	path = PurePath(img).parts[-1].replace(".jpeg", "")
	label = image_to_labels[ path ]
	final_dict['test'].append( (img, int(label) ) )

with open("./dataset.pickle", "wb") as handle:
	pickle.dump( final_dict, handle, pickle.HIGHEST_PROTOCOL )
