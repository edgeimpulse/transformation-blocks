# Resample CSV file

This transformation job example takes an input csv file and resample it to a defined frequency.

![Run job](/assets/resample-csv/run-resample-csv.png)

## Setup

**Operating mode**: File (`--in-files`)

**Parameters**:

```
[
    {
        "name": "Sampling rate (ms)",
        "type": "int",
        "param": "sampling_rate",
        "value": "",
        "help": "Sampling rate in milliseconds"
    },
    {
        "name": "Resampling mode",
        "type": "select",
        "valid": [
            "mean",
            "median"
        ],
        "param": "resampling_mode",
        "value": "",
        "help": "Resampling mode"
    }
]
```

## Test the transformation block locally

The dataset used to test this transformation is accessible here: [https://www.kaggle.com/datasets/luisomoreau/activity-detection](https://www.kaggle.com/datasets/luisomoreau/activity-detection).

```
pip3 install -r requirement.txt
```

```
python3 transform.py --in-file input/Accelerometer.csv --out-directory output --sampling_rate 16 --resampling_mode median
```