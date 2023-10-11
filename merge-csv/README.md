# Merge CSV files

This transformation job example takes the CSV files as an input and merge them together.

![Run job](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/merge-csv/run-merge-csv.png?raw=true)

## Setup

**Operating mode**: Data item (`--in-directory`)

**Parameters**:

```
[
    {
        "name": "CSV files",
        "type": "string",
        "param": "files",
        "value": "",
        "help": "CSV files to merge, separated by coma"
    },
    {
        "name": "Merge key",
        "type": "string",
        "param": "key",
        "value": "",
        "help": "CSV files to merge, separated by coma"
    },
    {
        "name": "Join method",
        "type": "select",
        "valid": [
            "outer",
            "inner",
            "left",
            "right"
        ],
        "param": "join",
        "value": "outer",
        "help": "How to join the files"
    },
    {
        "name": "Define custom filename",
        "value": false,
        "type": "boolean",
        "param": "rename",
        "help": "By default, the first word of the folder will be used"
    },
    {
        "name": "filename",
        "value": "merged",
        "type": "string",
        "param": "filename",
        "help": "filename without extension",
        "showIf": {
            "parameter": "rename",
            "operator": "eq",
            "value": "true"
        }
    }
]
```

## Test the transformation block locally

The dataset used to test this transformation is accessible here: [https://www.kaggle.com/datasets/luisomoreau/activity-detection](https://www.kaggle.com/datasets/luisomoreau/activity-detection).

Install the dependencies:
```
pip3 install -r requirement.txt
```
Run the script:
```
python transform.py --in-directory ../dataset/Cycling-2023-09-14_06-33-47 --files Accelerometer.csv,Gyroscope.csv --out-directory output --key time --join outer --rename False
```