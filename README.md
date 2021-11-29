# face_rec

These python programs use dlib on Linux for facial feature recognition using the facial_recognition tool found here.
https://github.com/ageitgey/face_recognition

These programs were developed on Ubuntu with a virtual machine using VirtualBox. Some extra tools may need to be installed seperately if a different Linux distrobution is used.

VirtualBox: https://www.virtualbox.org/

Ubuntu: https://ubuntu.com/download/desktop

Here is a guide for setting up Ubuntu on VirtualBox: https://itsfoss.com/install-linux-in-virtualbox/

Once Ubuntu is setup on a virtual machine it is time to download the contents of this github. To do this, type this into the terminal.
```
git clone https://github.com/Andbram/face_rec.git
```

Next enter this into the terminal to download the tools needed to run the face_rec tool.
```
cd face_rec
chmod +x install
./install
```

Next we need to download the dataset that will be used by the face_rec tool. That is done by entering this into a browser search bar.
```
http://dlib.net/files/data/ibug_300W_large_face_landmark_dataset.tar.gz
```

Once it is downloaded, extract the contents and copy the contents of the "ibug_300W_large_face_landmark_dataset" file into the face_rec folder.

Now the face_rec tool is ready to use. To run the program, enter this into the terminal.
```
python3 face_rec.py
```

This will open a picture of President Obama with his facial features outlined in white lines. These white lines are made up of the 68 point representing a face that can be seen in the "68 Facial Points.jpg" file. 

image_rec using a model .dat  file for its facial recognition. Next we will use the ibug dataset to train a new .dat file. This is done by using these programs. These will take up alot of memory so if the virtual machine does not have atleast 30 GB of memory, it might freeze.
```
python3 parse_xml.py
python3 train_shape_predictor.py
```
This now created the "custom_predictor.dat" file. To use the new .dat file, enter this into terminal.
```
python3 image_rec_custom.py
```
This will again bring up an image of President Obama with lines outlining his facial features. This time less features will be outlined.

This will result in a faster facial recognition since it has less points to measure but with more error. 

To test the error rate of the new model go to the "parse_xml.py" file and edit lines 3 and 4 from
```
inpt = "labels_ibug_300W_train.xml"
outpt = "labels_ibug_300W_train_custom.xml"
```
to 
```
inpt = "labels_ibug_300W_test.xml"
outpt = "labels_ibug_300W_test_custom.xml"
```
Next run these in terminal to test the new .dat file error rate.
```
python3 parse_xml.py
python3 test_shape_predictor.py
```
This will output an error rate.

image_rec_custom.py

This file is used to perform image recognition on a image of your choice with the training date you chose. It will display the point data generated with connecting lines to outline each part of the face.

To change the training data, edit the ".dat" file on line 9 to your own training data.
```
predictor_custom_model = resource_filename(__name__, "YOUR FILE HERE .dat")
```

To change the image, edit the ".jpg" file on line 14 to your own image.
```
image = np.array(PIL.Image.open("YOUR IMAGE HERE.jpg"))
```




