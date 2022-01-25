# Download the data
pip install kaggle

export KAGGLE_USERNAME=
export KAGGLE_KEY=

kaggle competitions download -c diabetic-retinopathy-detection

unzip diabetic-retinopathy-detection.zip

cat train.zip.* >train.zip
unzip train.zip

cat test.zip.* >test.zip
unzip test.zip

unzip trainLabels.csv.zip

rm -rf *.zip*
