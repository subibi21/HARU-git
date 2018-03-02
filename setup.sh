echo y | command


apt-get update
apt-get -y upgrade 

apt-get install -y python-dev python-setuptools swig
apt-get install -y ttf-unfonts-core
apt-get install -y python-pyaudio python3-pyaudio sox
apt-get install -y libatlas-base-dev libblas-dev liblapack-dev

pip install apiai

echo "Finish"
