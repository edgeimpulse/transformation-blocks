#!/bin/bash

while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in
    --name)
      NAME="$2"
      shift # past argument
      shift # past value
      ;;
    *)
      # Unknown option
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

echo "Hello $NAME"