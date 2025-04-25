### Building and running your application

Build the image using:
`docker build -t passwordgenerator .`.

Then, run the container in interactive mode with a pseudo-TTY:
`docker run -it --name pwdcontainer passwordgenerator`
