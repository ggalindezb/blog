FROM python:3.13-bookworm
COPY . /home/blog
WORKDIR /home/blog
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt

ENV KEY=2a1e0fc0-7bab-4aa0-9e2f-23d7ddd81241
ENV JWT_TOKEN=fe842f32bf823682b7f25cc0dbd81e1fd84801563d09a0cab7cbf150ac7ef38d

CMD ["flask", "--app", "blog", "run", "--debug", "--host=0.0.0.0"]
