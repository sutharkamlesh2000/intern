FROM oecinternal/odoo:18.0
USER root
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install imutils==0.5.4 numpy==1.23.5 pillow==9.2.0 matplotlib==3.6.2 opencv-python==4.6.0.66

