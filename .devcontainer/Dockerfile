FROM python:3.10-slim

USER root
RUN apt update && apt install git --yes

RUN pip install polars==0.19.2
RUN pip install streamlit
RUN pip install pyyaml
RUN pip install streamlit-card