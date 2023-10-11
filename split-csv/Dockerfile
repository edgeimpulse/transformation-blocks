FROM public.ecr.aws/docker/library/python:3.10

WORKDIR /app

# Python dependencies
COPY requirements.txt ./
RUN pip3 --no-cache-dir install -r requirements.txt

COPY . ./

ENTRYPOINT [ "python3",  "-u", "transform.py" ]