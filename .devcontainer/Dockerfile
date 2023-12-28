# TODO: baseのイメージはもっと最低限で軽量なものを探す
FROM gcr.io/kaggle-gpu-images/python@sha256:2e7e3f1b87810248aa8129ce5d7e1d38bd89ae202cc59d29763625abc5bbaba8

USER root
RUN apt install git --yes

RUN pip uninstall polars --yes
RUN pip install polars==0.19.2
RUN pip install streamlit