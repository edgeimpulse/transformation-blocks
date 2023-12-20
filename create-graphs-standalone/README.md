# Create graphs from sensors CSV file (Python)

This transformation block generates graphs from sensor CSV files.

![Create the job](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/create-graphs/create-transformation-job.png?raw=true)

## Setup

**Operating mode**: Standalone (`--standalone`)

**Parameters**:

`--bucket_name` Bucket where your dataset is hosted

`--bucket_directory` Directory in your bucket where your dataset is hosted

`--sensor_name` Sensor data to extract to create the graph, this should match the name of the file

```
[
    {
        "name": "Sensor",
        "type": "string",
        "param": "sensor_name",
        "value": "Accelerometer",
        "help": "Sensor data to extract to create the graph, this should match the name of the file"
    },
    {
        "name": "Bucket",
        "type": "bucket",
        "param": "bucket_name",
        "value": "",
        "help": "Bucket where your dataset is hosted"
    },
    {
        "name": "Path in bucket",
        "value": "",
        "type": "string",
        "param": "bucket_directory",
        "help": "Directory in your bucket where your dataset is hosted"
    }
]
```

## Test the transformation block locally

The dataset used to test this transformation is accessible here: [https://www.kaggle.com/datasets/luisomoreau/activity-detection](https://www.kaggle.com/datasets/luisomoreau/activity-detection).

In production, the MOUNT_PREFIX will be set to `/mnt/s3fs/`. Locally, you can overwrite this mount prefix using the following command:

```
export MOUNT_PREFIX=''
```

Run the script:
```
python3 transform.py --bucket_name ../dataset --sensor_name Accelerometer
```