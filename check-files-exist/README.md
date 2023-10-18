# Check files exist - Add metadata

This transformation job example will set the `ei_check_files_exist` metadata to your clinical dataset

![Run job](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/check-files-exist/run-check-files-exist.png?raw=true)

## Setup

**Operating mode**: Data item (`--in-indirectory`)

**Parameters**:

```
[
    {
        "name": "CSV files",
        "type": "string",
        "param": "files",
        "value": "",
        "help": "CSV files to merge, separated by coma"
    }
]
```

## Test the transformation block locally

The dataset used to test this transformation is accessible here: [https://www.kaggle.com/datasets/luisomoreau/activity-detection](https://www.kaggle.com/datasets/luisomoreau/activity-detection).

```
pip3 install -r requirement.txt
```

```
python3 transform.py --in-directory ../dataset/dir --out-directory output --files Accelerometer.csv, Gyroscope.csv
```

The output `ei-metadata.json` file will look like the following if the files are present:

```
{
    "version": 1,
    "action": "add",
    "metadata": {
        "ei_check_files_present": 1,
        "ei_check": 1
    }
}
```