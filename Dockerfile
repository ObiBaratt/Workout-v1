FROM python:3.10

# Create app directory
WORKDIR /app

# Pre dep installs
RUN apt-get update && apt-get install -y \
  libpq-dev \
  python3-dev

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
