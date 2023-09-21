# Transformation block examples

This repository contains example of transformation blocks.

For more information on how to set up a transformation block, please head to Edge Impulse documentation, [Custom blocks -> Transformation blocks](https://docs.edgeimpulse.com/docs/edge-impulse-studio/organizations/custom-blocks/transformation-blocks)

## Examples

To use the following examples, a README.md instruction file will be provided inside the example repositories. Sometimes, a public docker image will also be provided to quickly test so you don't need to import it and clone the entire repository.

To modify the code and push the blocks to your organization, you will need to use [Edge Impulse CLI](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli).

1. Clone this repository:

```
git clone https://github.com/edgeimpulse/transformation-blocks.git
```

2. Navigate to the desired example:

```
cd transformation-blocks/hello-edge
```

3. Create the transformation block:

```
edge-impulse-block init
```

4. Push the transformation block to your organization:

```
edge-impulse-block push
```

## Contributing to this repository

We welcome contributions to this repository. Both improvements to our own transformation blocks, as well as new and well-tested transformation blocks for other use cases. Make sure to provide a public dataset - or subset of this dataset - so everyone can reproduce your workflow seamlessly.
