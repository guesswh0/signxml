# signxml

# Docker
```shell
git clone https://github.com/guesswh0/signxml.git
cd signxml
docker build -t signxml . 
docker run --rm -it signxml
```

# Ubuntu(Debian)
```shell
sudo apt-get update && install python3-dev libpcsclite1 libltdl7 
git clone https://github.com/guesswh0/signxml.git
cd signxml
export TZ="Asia/Almaty"
export LD_LIBRARY_PATH=signxml/lib:$LD_LIBRARY_PATH
python3 main.py
```