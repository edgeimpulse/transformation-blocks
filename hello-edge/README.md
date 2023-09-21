# Hello Edge - Edge Impulse transformation block example

This is an example of an Edge Impulse transformation blocks.
It will print "hello +name" on the transformation job logs.

## Setting up

To set this up in Edge Impulse Studio, head to your organization and navigate to Custom blocks -> Transformation blocks -> Create new.

Select a **Standalone** transformation block and use this Docker image: 
[luisomoreau/hello_edge:latest](https://hub.docker.com/r/luisomoreau/hello_edge)

Also, make sure to configure the [additional block parameters](https://docs.edgeimpulse.com/docs/tips-and-tricks/adding-parameters-to-custom-blocks) with this config:

```
[
    {
        "name": "Name",
        "type": "string",
        "param": "name",
        "value": "",
        "help": "Person to greet"
    }
]
```

![setup](/assets/hello-edge/studio-create-transformation-hello-edge.png)