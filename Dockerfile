FROM python:3.7-slim-buster

RUN python3 -m pip install bpython
COPY scripts/bp_run.py /

ENTRYPOINT [ "./bp_run.py" ]
