# Split CSV File

This transformation job example takes an input CSV file and splits it into smaller CSV files based on a defined time interval.

![Run job](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/split-csv/run-split-csv.png?raw=true)

## Setup

**Operating mode**: File (`--in-file`)

**Parameters**:

```
[
    {
        "name": "Split Interval (s)",
        "type": "int",
        "param": "split-interval",
        "value": "",
        "help": "Time interval in seconds for splitting the CSV"
    },
    {
        "name": "Time column",
        "type": "string",
        "param": "time-column",
        "value": "time",
        "help": "Time column that will be used to split the CSV"
    }
]
```

## Test the transformation block locally

The dataset used to test this transformation is accessible here: [https://www.kaggle.com/datasets/luisomoreau/activity-detection](https://www.kaggle.com/datasets/luisomoreau/activity-detection).

```
pip3 install -r requirement.txt
```

```
python3 transform.py --in-file input/Accelerometer.csv --out-directory output --split-interval 10 --time-column time
```

In this transformation job, you specify the `--split_interval` parameter to define the time interval (in seconds) for splitting the input CSV file into smaller CSV files.