FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye


# Install necessary tools and dependencies for TA-Lib
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    libtool \
    automake \
    autoconf \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download and build TA-Lib from source
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz \
    && tar -xzf ta-lib-0.4.0-src.tar.gz \
    && cd ta-lib \
    && ./configure --prefix=/usr \
    && make \
    && make install \
    && cd .. \
    && rm -rf ta-lib ta-lib-0.4.0-src.tar.gz