# Hello World With Flask And Docker

## Run

### Build docker
`docker build --no-cache -t python_flask:1.0 .`

### Run docker

`docker run -p 5000:5000 --name=flask python_flask:1.0`