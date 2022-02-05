# Approach taken from https://github.com/SubtleMuffin/ns3-docker.git and tested here.

# Get Linux image.
FROM debian:buster-slim
# Non-interactive to prevent user input prompts.
ARG DEBIAN_FRONTEND=noninteractive

# Install essential binaries.
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git build-essential python3-dev gdb htop
# Get bridge utilities.
RUN apt-get install bridge-utils
# Install for ARM compatibility
# RUN apt-get install -y binfmt-support qemu qemu-user-static

# Clone, configure and build ns3
# COPY . .
# RUN git clone https://gitlab.com/nsnam/ns-3-dev.git
# RUN cd ns-3 && ./waf configure --enable-examples --enable-tests --enable-mpi && ./waf build

# Set working directory to guest directory that will bind to host ns-3.
WORKDIR /ns-3
# Set entry point.
ENTRYPOINT [ "/bin/bash", "-c"]