FROM python:3.13-bookworm
COPY . /home/blog
WORKDIR /home/blog
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "--app", "blog", "run", "--debug", "--host=0.0.0.0"]
