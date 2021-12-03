sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install cmake
sudo apt install python3-pip
git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake ..; cmake --build .
cd ..
pip3 install face_recognition
pip install multiprocess
git clone https://github.com/ageitgey/face_recognition.git
