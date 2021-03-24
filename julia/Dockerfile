FROM nvcr.io/nvidia/nvhpc:21.2-devel-cuda_multi-ubuntu20.04

LABEL maintainer "Nischay Mamidi <nischaypro@gmail.com>"

SHELL ["/bin/bash", "-c", "-l"] 
RUN apt-get update
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y --no-install-recommends install git wget build-essential curl ca-certificates
RUN wget https://julialang-s3.julialang.org/bin/linux/x64/1.5/julia-1.5.4-linux-x86_64.tar.gz
RUN tar -xvzf julia-1.5.4-linux-x86_64.tar.gz
RUN rm -rf julia-1.5.4-linux-x86_64.tar.gz
RUN mv julia-1.5.4 /opt/julia
RUN ln -sf /opt/julia/bin/julia /usr/local/bin/julia
RUN julia --version
RUN mkdir /julia
WORKDIR /julia
COPY install.jl /julia/install.jl
RUN julia install.jl
RUN rm -rf /julia/install.jl
RUN mkdir /data
WORKDIR /data
RUN git clone https://github.com/Nischay-Pro/meshfree-solver.git --branch=julia_cuda julia