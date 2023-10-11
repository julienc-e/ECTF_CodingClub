# CTFd Docker Deploy
Repository to deploy CTFd using docker-compose, nginx & TLS.

## How to use this repository to start a CTFd instance with TLS

1. Clone this repository by running `git clone https://github.com/julienc-e/ECTF_CodingClub.git`.
2. Go into the directory which the repository was cloned into (`ECTF_CodingClub` by default)
3. Install `docker` based on the instructions [here](https://docs.docker.com/install/).
4. Copy the contents of the https://github.com/CTFd/CTFd repository into the `infra` folder.
5. Setup your DNS records to point to the server where you are starting CTFd.
6. Get a TLS certificate and private key from a Certificate Authority and save them as `ctfd.crt` and `ctfd.key` respectively in the `ssl` directory.
7. Edit the `hostname` line in the `docker-compose-production.yml` file to match the hostname you have defined to point to this server.
8. Run `run.sh` or `docker-compose -f docker-compose.yml -f docker-compose-production.yml up -d`.

(Note: Taken from https://github.com/tghosth/CTFd-docker-deploy )
