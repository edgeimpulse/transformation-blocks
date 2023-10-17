# Resample CSV file

This transformation job example takes an input csv file and resample it to a defined frequency.

![Run job](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/resample-csv/run-resample-csv.png?raw=true)

## Setup

**Operating mode**: File (`--in-files`)

**Parameters**:

```
[
    {
        "name": "Time column",
        "type": "string",
        "param": "time-column",
        "value": "time",
        "help": "Time column that will be used as for the x-axis"
    }
]
```

## Test the transformation block locally

The dataset used to test this transformation is accessible here: [https://www.kaggle.com/datasets/luisomoreau/activity-detection](https://www.kaggle.com/datasets/luisomoreau/activity-detection).

```
pip3 install -r requirement.txt
```

```
python3 transform.py --in-file input/Accelerometer.csv --out-directory output
```

The output graph will look like the following:

* Accelerometer.csv:

![Accelerometer graph](/assets/create-graphs/Accelerometer.graph.png)

* Location.csv:

![Location graph](assets/../../assets/create-graphs/Location.graph.png)