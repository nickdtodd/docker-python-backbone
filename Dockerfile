FROM fspot/flask-sockets

ADD requirements.txt /code/work/requirements.txt
WORKDIR /code/work
RUN $VENV_DIR/bin/pip install -r requirements.txt
