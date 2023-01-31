# first step
docker build -t test .

# second step
docker run -d -p 8000:8000 test