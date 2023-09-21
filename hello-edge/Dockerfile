# Use a base image with Bash installed
FROM ubuntu:latest

# Do not use a WORKDIR under /home - it will be mounted in by Edge Impulse, making your files inaccessible.
WORKDIR /app

# Copy the bash script into the container
COPY hello.sh /hello.sh

# Make the bash script executable
RUN chmod +x /hello.sh

# Set the entrypoint command to run the script with the provided --name argument
ENTRYPOINT ["/hello.sh"]