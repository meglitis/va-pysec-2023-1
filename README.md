# va-pysec-2023-1

## 1. Instalācija

Izmantoju Ubuntu 23.04

Python 3.11 pieejams pēc noklusējuma.

Python 2.7.16 instalācija 

```shell
wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz
tar xzf Python-2.7.16.tgz
cd Python-2.7.16
./configure --enable-optimizations
sudo make altinstall

$ python
python2.7         python2.7-config  python3           python3.11
```

## 2. Pārslēgšanās starp virtuālajām vidēm

```shell
python3.11 -m venv venv3.11
source venv3.11/bin/activate
pip freeze > requirements.txt
deactivate

python2.7 -m venv venv2.7
source venv2.7/bin/activate
python2.7 -m pip install -r requirements.txt
deactivate
```
