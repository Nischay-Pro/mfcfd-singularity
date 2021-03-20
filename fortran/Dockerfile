FROM nvcr.io/nvidia/nvhpc:21.2-devel-cuda_multi-ubuntu20.04

LABEL maintainer "Nischay Mamidi <nischaypro@gmail.com>"

SHELL ["/bin/bash", "-c", "-l"] 
RUN apt-get update
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y --no-install-recommends install git make python3 wget build-essential cmake curl ca-certificates
RUN git clone https://github.com/spack/spack.git --depth=1 /opt/spack
RUN source /opt/spack/share/spack/setup-env.sh && spack compiler add
RUN source /opt/spack/share/spack/setup-env.sh && spack install hdf5 +cxx +fortran +hl -mpi target=x86_64 %nvhpc && spack clean -a
RUN apt-get -y autoremove
RUN apt-get -y clean
RUN mkdir /data
WORKDIR /data
RUN git clone https://github.com/Nischay-Pro/mfcfd.git --branch=hdf5-sec-order --depth=1 fortran
WORKDIR /data/fortran/install
RUN source /opt/spack/share/spack/setup-env.sh && spack load hdf5 && CC=nvc CXX=nvc++ python3 install.py --mfcfd cuda
RUN mkdir /fortran
RUN cp /data/fortran/install/execname /fortran
