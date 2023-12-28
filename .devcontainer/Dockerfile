FROM nvcr.io/nvidia/pytorch:22.12-py3

USER root
RUN apt update && apt install git --yes

RUN pip uninstall polars --yes
RUN pip install polars==0.19.2
RUN pip install streamlit