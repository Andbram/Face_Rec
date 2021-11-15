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


