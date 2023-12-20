# Create graphs from CSV

This transformation block generates graphs from sensor CSV files.

![Run job](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/create-graphs/run-job.png?raw=true)

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
python3 transform.py --in-file input/Accelerometer.csv --out-directory output --time-column time
```

The output graph will look like the following:

* Accelerometer.csv:

![Accelerometer graph](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/create-graphs/Accelerometer.graph.png?raw=true)

* Location.csv:

![Location graph](https://github.com/edgeimpulse/transformation-blocks/blob/main/assets/create-graphs/Location.graph.png?raw=true)