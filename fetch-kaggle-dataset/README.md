# Fetch a dataset hosted in Kaggle using a transformation block (Python)

This transformation block takes Kaggle owner/dataset arguments to fetch it and store it in your [organizational datasets](https://docs.edgeimpulse.com/docs/edge-impulse-studio/organizations/data).

Input parameters:

`--kaggle_dataset owner/dataset-slug` The Kaggle dataset

`--bucket_name output` The bucket in which you want to store the fetched dataset

`--bucket_directory` The directory in the bucket to store the fetched dataset (optional)

## Test the transformation block locally

In production, the MOUNT_PREFIX will be set to `/mnt/s3fs/`, locally you can overwrite this mount prefix using the following command:

```
export MOUNT_PREFIX=''
```

Run the script:
```
python3 fetch.py --kaggle_dataset owner/dataset-slug --bucket_name output
```

## How to setup

1. Clone this repository:

    ```
    git clone https://github.com/edgeimpulse/transformation-blocks.git
    cd transformation-blocks/fetch-kaggle-dataset
    ```

2. Create a new transformation block:

    ```
    $ edge-impulse-blocks init

    ? Choose a type of block Transformation block
    ? Choose an option Create a new block
    ? Enter the name of your block Fetch Kaggle Dataset
    ? Enter the description of your block Fetch a dataset hosted on Kaggle
    ? What type of data does this block operate on? Standalone (runs the container, but no files / data items passed in)
    ? Which buckets do you want to mount into this block (will be mounted under /mnt/s3fs/BUCKET_NAME, you can change these mount points in the St
    udio)?
    ? Would you like to download and load the example repository? no
    ```

3. Push the block:

    ```
    $ edge-impulse-blocks push
    ```

4. Environment variables/Secrets

    You will need to set your `KAGGLE_USERNAME` and `KAGGLE_KEY` in your Transformation blocks' secrets:

    ![Transformation block overview](/assets/fetch-kaggle-dataset/transformation-blocks-overview.png)

5. Parameters - These should be set by `edge-impulse-block` CLI:

    ```
    [
        {
            "name": "Kaggle dataset",
            "type": "string",
            "param": "kaggle_dataset",
            "value": "",
            "help": "owner/dataset-slug"
        },
        {
            "name": "Output bucket",
            "type": "bucket",
            "param": "bucket_name",
            "value": "",
            "help": "The bucket where you will store the fetched dataset"
        },
        {
            "name": "Output bucket path",
            "value": "kaggle-original-dataset/",
            "type": "string",
            "param": "bucket_directory",
            "help": "The prefix in the output bucket"
        }
    ]
    ```

6. Overview

    ![Block overview](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/fetch-kaggle-dataset/fetch-kaggle-dataset-transformation-overview.png?raw=true)

## Run job

![Create the job](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/fetch-kaggle-dataset/create-transformation-job-2.png?raw=true)

## Additional info

There is also a public image of this block: [edgeimpulse/ei-transform_fetch-kaggle-dataset:latest](https://hub.docker.com/r/edgeimpulse/ei-transform_fetch-kaggle-dataset)