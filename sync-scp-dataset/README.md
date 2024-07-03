# Fetch files using scp and sync with organization dataset

This transformation block fetch files using scp and store it in your [organizational datasets](https://docs.edgeimpulse.com/docs/edge-impulse-studio/organizations/data).

### Input parameters:

`--remote-host` Remote host to copy files from

`--remote-port` Remote port to use

`--remote-directory` Remote directory to fetch

`--bucket-name` Bucket to store the files

`--bucket-prefix` Output bucket prefix to store the files

### SSH credentials

This block uses username and password authentication method. Both secrets are passed as environment variables when the container starts.
To use within an Edge Impulse Transformation Block, add `SCP_USERNAME` and `SCP_PASSWORD` as Secrets in the Transformation Blocks section.

## Test the transformation block locally

1. Clone this repository:

    ```
    git clone https://github.com/edgeimpulse/transformation-blocks.git
    cd transformation-blocks/sync-scp-dataset
    ```

2. Build the container:

```
docker build -t sync-scp-dataset .
```

3. Run it locally by passing the different parameters, ie:

```
docker run --env SCP_USERNAME=xxxxx --env SCP_PASSWORD=xxxxx -v $PWD:/home sync-scp-dataset --remote-host scpserver.com --remote-port 22 --remote-directory /tmp/scp_files/
```

As the `--bucket-name` parameter is not present, files will be written to the `./output` directory.

## Transformation Block setup

1. Clone this repository:

    ```
    git clone https://github.com/edgeimpulse/transformation-blocks.git
    cd transformation-blocks/sync-scp-dataset
    ```

2. Create a new transformation block:

    ```
    $ edge-impulse-blocks init

    ? Choose a type of block Transformation block
    ? Choose an option Create a new block
    ? Enter the name of your block Sync data from SCP server
    ? Enter the description of your block Fetch files from a SCP server and store in a dataset
    ? What type of data does this block operate on? Standalone (runs the container, but no files / data items passed in)
    ? Which buckets do you want to mount into this block (will be mounted under /mnt/s3fs/BUCKET_NAME, you can change these mount points in the Studio)? (Select your bucket)
    ```

3. Push the block:

    ```
    $ edge-impulse-blocks push
    ```

4. Environment variables/Secrets

    In the Organization -> Custom blocks -> Transformation section, click on _Add new secret_ and set both `SCP_USERNAME` and `SCP_PASSWORD` secrets.

5. Create dataset

    In the Organization -> Data -> Datasets section, click on _Add new dataset_:

    ![Create dataset](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/sync-scp-dataset/create-dataset.png?raw=true)

    Data from the SCP server will be stored in this dataset.

## Run transformation job

In the Organization -> Data transformation section, click on _Create job_.

Fill in the different parameters, and start the transformation job. Make sure the _output bucket path_ matches the _bucket path_ from the previous dataset section (ie: `scp-files/`)

![Create dataset](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/sync-scp-dataset/create-job.png?raw=true)

Once the job is finished, your files will appear in the dataset created in the previous section.
