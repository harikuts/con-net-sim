# Approach taken from https://github.com/SubtleMuffin/ns3-docker.git and tested here.

# Get Linux image.
FROM debian:buster-slim
# Non-interactive to prevent user input prompts.
ARG DEBIAN_FRONTEND=noninteractive

# Install essential binaries.
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git build-essential python3-dev gdb htop
# Install for ARM compatibility
# RUN apt-get install -y binfmt-support qemu qemu-user-static

# Clone, configure and build ns3
# COPY . .
# RUN git clone https://gitlab.com/nsnam/ns-3-dev.git
# RUN cd ns-3-dev && ./waf configure --enable-examples --enable-tests --enable-mpi && ./waf build

WORKDIR /ns-3-dev
ENTRYPOINT [ "/bin/bash" ]