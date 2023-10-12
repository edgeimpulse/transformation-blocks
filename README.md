# Transformation block examples

This repository contains examples of Edge Impulse transformation blocks.

For more information on how to set up a transformation block, please head to Edge Impulse documentation, [Custom blocks -> Transformation blocks](https://docs.edgeimpulse.com/docs/edge-impulse-studio/organizations/custom-blocks/transformation-blocks)

## Examples

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Mode</th>
      <th>Programming language</th>
      <th>Public docker image (optional)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="/hello-edge/">Hello Edge</a></td>
      <td>print <code>hello +name</code> on the transformation job logs</td>
      <td>Standalone</td>
      <td>Bash</td>
      <td><a href="https://hub.docker.com/r/edgeimpulse/ei-transform_hello-edge" target="_blank">edgeimpulse/ei-transform_hello-edge:latest</a></td>
    </tr>
     <tr>
      <td><a href="/utils-access-data/">Utils - Access data</a></td>
      <td>Utility example to explain how to access data</td>
      <td>Standalone | Data item | File</td>
      <td>Python</td>
      <td><a href="https://hub.docker.com/r/edgeimpulse/ei-transform_utils-access-data" target="_blank">edgeimpulse/ei-transform_utils-access-data:latest</a></td>
    </tr>
    <tr>
      <td><a href="/fetch-kaggle-dataset/">Fetch Kaggle Dataset</a></td>
      <td>Import a dataset hosted on Kaggle to your bucket</td>
      <td>Standalone</td>
      <td>Python</td>
      <td><a href="https://hub.docker.com/r/edgeimpulse/ei_transform_fetch-kaggle-dataset" target="_blank">edgeimpulse/ei_transform_fetch-kaggle-dataset:latest</a></td>
    </tr>
    <tr>
      <td><a href="/create-graphs-standalone/">Create graphs (Standalone)</a></td>
      <td>Generate a helper graph from sensor CSV</td>
      <td>Standalone</td>
      <td>Python</td>
      <td><a href="https://hub.docker.com/r/edgeimpulse/ei-transform_create-graphs-standalone" target="_blank">edgeimpulse/ei-transform_create-graphs-standalone</td>
    </tr>
    <tr>
      <td><a href="/create-graphs-in-file/">Create graphs (in-file)</a></td>
      <td>Generate a helper graph from sensor CSV</td>
      <td>File</td>
      <td>Python</td>
      <td><a href="https://hub.docker.com/r/edgeimpulse/ei-transform_create-graphs-in-file" target="_blank">edgeimpulse/ei-transform_create-graphs-standalone-in-file</td>
    </tr>
    <tr>
      <td><a href="/merge-csv/">Merge CSV</a></td>
      <td>Merge CSV files on a given key</td>
      <td>Data item</td>
      <td>Python</td>
      <td><a href="https://hub.docker.com/r/edgeimpulse/ei-transform_merge-csv" target="_blank">edgeimpulse/ei-transform_merge-csv</td>
    </tr>
    <tr>
      <td><a href="/resample-csv/">Resample CSV</a></td>
      <td>Upsample or downsample CSV files with a constant frequency</td>
      <td>File</td>
      <td>Python</td>
      <td><a href="https://hub.docker.com/r/edgeimpulse/ei-transform_resample-csv" target="_blank">edgeimpulse/ei-transform_resample-csv</td>
    </tr>
    <tr>
      <td><a href="/split-csv/">Split CSV</a></td>
      <td>Split CSV files into smaller CSV files defined by a split interval</td>
      <td>File</td>
      <td>Python</td>
      <td><a href="https://hub.docker.com/r/edgeimpulse/ei-transform_split-csv" target="_blank">edgeimpulse/ei-transform_split-csv</td>
    </tr>
    
  </tbody>
</table>

To use the examples, a README.md instruction file will be provided inside the example repositories. Sometimes, a public docker image will also be provided to quickly test so you don't need to import it and clone the entire repository.

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
