FROM marcopalena/polito-os161:latest

USER root

RUN apt-get update && apt-get install -y \
  neovim \
  && rm -rf /var/lib/apt/lists/*

USER os161user
