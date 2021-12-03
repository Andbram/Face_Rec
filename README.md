# face_rec

These python programs use dlib on Linux for facial feature recognition using the facial_recognition tool found here.
https://github.com/ageitgey/face_recognition

These programs were developed on Ubuntu with a virtual machine using VirtualBox. Some extra tools may need to be installed seperately if a different Linux distrobution is used.

VirtualBox: https://www.virtualbox.org/

Ubuntu: https://ubuntu.com/download/desktop

Here is a guide for setting up Ubuntu on VirtualBox: https://itsfoss.com/install-linux-in-virtualbox/

Once Ubuntu is setup on a virtual machine, it is time to download the contents of this github. To do this, type this into the terminal.
```
sudo apt install git
git clone https://github.com/Andbram/face_rec.git
```

Next enter this into the terminal to download the tools needed to run the face_rec tool.
```
cd face_rec
chmod +x install.sh
./install.sh
```

Next we need to download the dataset that will be used by the face_rec tool. That is done by entering this into a browser search bar.
```
http://dlib.net/files/data/ibug_300W_large_face_landmark_dataset.tar.gz
```

Once it is downloaded, extract the contents and copy the contents of the "ibug_300W_large_face_landmark_dataset" file into the face_rec folder.

Now the face_rec tool is ready to use. To run the program, enter this into the terminal.
```
python3 image_rec.py
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

**parse_xml.py**

This file is used to edit the ibug ".xml" files that contain the point data for the ibug data set. This files reads through the ".xml" file and removes the point data that is outside of the range you specify.

To change which ".xml" file is being used as the input data, change line 3 to your desired ".xml" file. You really only need to change this between the "labels_ibug_300W_train.xml" and the "labels_ibug_300W_test.xml"
```
inpt = "YOUR FILE HERE.xml"
```

To change which ".xml" file is being used to store the output data, change line 4 to your desired ".xml" file name.
```
outpt = "YOUR FILE HERE.xml"
```

To change the desire points to be stored inside the ouput file, change line 6 to your desired points. Review the "68 Facial Points.jpg" file to see which points relate to each part of the face.
```
LANDMARKS = {YOUR POINTS HERE}
```

**train_shape_predictor.py**

This file is used to train the shape predictor based on the ".xml" file you provide it with. It will output the trained ".dat" file.

To change the input ".xml" file, edit line 4 to be the ".xml" file you want to be trained off.
```
xml = "YOUR FILE HERE.xml"
```

To change the output ".dat" file, edit line 5 to be the ".dat" file you want to store the trained data to.
```
dat = "YOUR FILE HERE.dat"
```

To change the options for training the shape predictor, edit lines 14, 21, 27, 34, 39, 45, 49, 53, 58. The changes each option has on the training are described above each of the options. 

**image_rec_custom.py**

This file is used to perform image recognition on a image of your choice with the training date you chose. It will display the point data generated with connecting lines to outline each part of the face.

To change the training data, edit the ".dat" file on line 9 to your own training data.
```
predictor_custom_model = resource_filename(__name__, "YOUR FILE HERE .dat")
```

To change the image, edit the ".jpg" file on line 14 to your own image.
```
image = np.array(PIL.Image.open("YOUR IMAGE HERE.jpg"))
```

If any point data is changed in the new ".dat" file then the point list one lines 22 - 27 need to be changed to match the new point data. For example, the first 9 points in the provided "custom_predictior.dat" file relate to the chin. So "chin: points[0:9]" is used to link those points together as the chin.
```
"chin": points[0:9], 
"nose_tip": points[9:13],
"left_eye": points[13:19], 
"right_eye": points[19:25],
"top_lip": points[25:32],
"bottom_lip": points[32:38]
```

**test_shape_predictor.py**

This file is used to test the error rate of a trained dataset to see how accurate it is.

To change which ".dat" file is being tested, edit line 3 to be your desired ".dat" file.
```
dat = "YOUR FILE HERE.dat"
```

To change which ".xml" file is being used to test the shape predictor on, edit line 4 to be your desired ".xml" file.
```
xml = "YOUR FILE HERE.xml"
```
