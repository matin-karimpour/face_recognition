FROM python

# OpenCV Version 
ARG OPENCV_VERSION

# Install dependencies
RUN apt-get update || true && apt-get upgrade -y &&\
    # Install build tools, build dependencies and python
    apt-get install --no-install-recommends -y \
	build-essential gcc g++ \
	cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
    libtbb-dev libjpeg-dev libpng-dev libtiff-dev \
    yasm libatlas-base-dev gfortran libpq-dev \
    libxine2-dev libglew-dev libtiff5-dev zlib1g-dev libavutil-dev libpostproc-dev \ 
    libeigen3-dev python3-dev python3-pip python3-numpy libx11-dev tzdata \
&& rm -rf /var/lib/apt/lists/*


RUN mkdir /service
COPY . /service/video_input_service/


WORKDIR /service/video_input_service
RUN pip install -r requirements.txt


EXPOSE 50051
ENTRYPOINT [ "python", "main.py" ]