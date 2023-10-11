#!/bin/bash

# Set your DockerHub username
DOCKERHUB_USER="edgeimpulse"

# Function to build and push Docker images for a given directory
build_and_push_image() {
    local dir="$1"
    local repo="$2"

    echo "Building Docker image for $dir..."
    docker build -t "${DOCKERHUB_USER}/ei-transform_${repo}" "$dir"
    docker push "${DOCKERHUB_USER}/ei-transform_${repo}"
    # Optional - use docker CLI plugin to push README.md files as a DockerHub repo description
    # docker pushrm "${DOCKERHUB_USER}/ei-transform_${repo}" -f "$dir/README.md"
}

# Iterate through your directory structure
for dir in */; do
    dir="${dir%/}"  # Remove trailing slash
    repo="${dir##*/}"  # Get the directory name as the repo name
    echo "Processing repository: $repo"

    # Check if there's a Dockerfile in the directory
    if [ -f "$dir/Dockerfile" ]; then
        build_and_push_image "$dir" "$repo"
    else
        echo "No Dockerfile found in $dir, skipping..."
    fi
done

echo "All Docker images have been built and pushed to DockerHub."