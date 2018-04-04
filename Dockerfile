FROM kernsuite/base:3
RUN docker-apt-install python3-pyqt4 python3-astropy python-qt4 python-astropy python3-pytest python-pytest python3-pip python-pip
RUN pip install --upgrade pip
RUN pip3 install --upgrade pip
ADD . /code
WORKDIR /code
RUN pip install .
RUN pip3 install .
run python setup.py test
run python3 setup.py test
