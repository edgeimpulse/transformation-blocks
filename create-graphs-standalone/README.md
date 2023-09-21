# Create graphs from sensors CSV file (Python)

This transformation block generate graphs from sensor CSV files.

The dataset used to test this transformation is accessible here: [https://www.kaggle.com/datasets/luisomoreau/activity-detection](https://www.kaggle.com/datasets/luisomoreau/activity-detection).

Input parameters:

`--bucket_name` Bucket where your dataset is hosted

`--bucket_directory` Directory in your bucket where your dataset is hosted

`--sensor_name` Sensor data to extract to create the graph, this should match the name of the file

## Test the transformation block locally

In production, the MOUNT_PREFIX will be set to `/mnt/s3fs/`. Locally, you can overwrite this mount prefix using the following command:

```
export MOUNT_PREFIX=''
```

Run the script:
```
python3 transform.py --bucket_name ../dataset --sensor_name Accelerometer
```

## How to run (Edge Impulse)

1. Clone this repository:

    ```
    git clone 
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

## Run job

![Create the job](create-graphs-standalone/create-transformation-job.png)