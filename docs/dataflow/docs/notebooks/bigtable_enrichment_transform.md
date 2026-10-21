---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/bigtable_enrichment_transform/
title: Use Apache Beam and Bigtable to enrich data \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:44.212381+00:00
---

# Use Apache Beam and Bigtable to enrich data  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/bigtable_enrichment_transform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Apache Beam and Bigtable to enrich data Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/bigtable_enrichment_transform.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/bigtable_enrichment_transform.ipynb) This notebook shows how to enrich data by using the Apache Beam [enrichment transform](https://beam.apache.org/documentation/transforms/python/elementwise/enrichment/) with [Bigtable](https://cloud.google.com/bigtable/docs/overview). The enrichment transform is an Apache Beam turnkey transform that lets you enrich data by using a key-value lookup. This transform has the following features:

  * The transform has a built-in Apache Beam handler that interacts with Bigtable to get data to use in the enrichment.
  * The enrichment transform uses client-side throttling to manage rate limiting the requests. The requests are exponentially backed off with a default retry strategy. You can configure rate limiting to suit your use case.

This notebook demonstrates the following ecommerce use case: A stream of online transaction from [Pub/Sub](https://cloud.google.com/pubsub/docs/guides) contains the following fields: `sale_id`, `product_id`, `customer_id`, `quantity`, and `price`. Additional customer demographic data is stored in a separate Bigtable cluster. The demographic data is used to enrich the event stream from Pub/Sub. Then, the enriched data is used to predict the next product to recommended to a customer.

## Before you begin

Set up your environment and download dependencies.

### Install Apache Beam

To use the enrichment transform with the built-in Bigtable handler, install the Apache Beam SDK version 2.54.0 or later.
    
    
    pip install torch
    pip install apache_beam[interactive,gcp]==2.54.0 --quiet
    
    
    import datetime
    import json
    import math
    
    from typing import Any
    from typing import Dict
    
    import torch
    from google.cloud import pubsub_v1
    from google.cloud.bigtable import Client
    from google.cloud.bigtable import column_family
    
    import apache_beam as beam
    import apache_beam.runners.interactive.interactive_beam as ib
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.pytorch_inference import PytorchModelHandlerTensor
    from apache_beam.options import pipeline_options
    from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
    from apache_beam.transforms.enrichment import Enrichment
    from apache_beam.transforms.enrichment_handlers.bigtable import BigTableEnrichmentHandler
    

### Authenticate with Google Cloud

This notebook reads data from Pub/Sub and Bigtable. To use your Google Cloud account, authenticate this notebook. To prepare for this step, replace `<PROJECT_ID>`, `<INSTANCE_ID>`, and `<TABLE_ID>` with the appropriate values for your setup. These fields are used with Bigtable.
    
    
    PROJECT_ID = "<PROJECT_ID>"
    INSTANCE_ID = "<INSTANCE_ID>"
    TABLE_ID = "<TABLE_ID>"
    
    
    
    from google.colab import auth
    auth.authenticate_user(project_id=PROJECT_ID)
    

### Train the model

Create sample data by using the format `[product_id, quantity, price, customer_id, customer_location, recommend_product_id]`.
    
    
    data = [
        [3, 5, 127, 9, 'China', 7], [1, 6, 167, 5, 'Peru', 4], [5, 4, 91, 2, 'USA', 8], [7, 2, 52, 1, 'India', 4], [1, 8, 118, 3, 'UK', 8], [4, 6, 132, 8, 'Mexico', 2],
        [6, 3, 154, 6, 'Brazil', 3], [4, 7, 163, 1, 'India', 7], [5, 2, 80, 4, 'Egypt', 9], [9, 4, 107, 7, 'Bangladesh', 1], [2, 9, 192, 8, 'Mexico', 4], [4, 5, 116, 5, 'Peru', 8],
        [8, 1, 195, 1, 'India', 7], [8, 6, 153, 5, 'Peru', 1], [5, 3, 120, 6, 'Brazil', 2], [2, 7, 187, 7, 'Bangladesh', 4], [1, 8, 103, 6, 'Brazil', 8], [2, 9, 181, 1, 'India', 8],
        [6, 5, 166, 3, 'UK', 5], [3, 4, 115, 8, 'Mexico', 1], [4, 7, 170, 4, 'Egypt', 2], [9, 3, 141, 7, 'Bangladesh', 3], [9, 3, 157, 1, 'India', 2], [7, 6, 128, 9, 'China', 1],
        [1, 8, 102, 3, 'UK', 4], [5, 2, 107, 4, 'Egypt', 6], [6, 5, 164, 8, 'Mexico', 9], [4, 7, 188, 5, 'Peru', 1], [8, 1, 184, 1, 'India', 2], [8, 6, 198, 2, 'USA', 5],
        [5, 3, 105, 6, 'Brazil', 7], [2, 7, 162, 7, 'Bangladesh', 7], [1, 8, 133, 9, 'China', 3], [2, 9, 173, 1, 'India', 7], [6, 5, 183, 5, 'Peru', 8], [3, 4, 191, 3, 'UK', 6],
        [4, 7, 123, 2, 'USA', 5], [9, 3, 159, 8, 'Mexico', 2], [9, 3, 146, 4, 'Egypt', 8], [7, 6, 194, 1, 'India', 8], [3, 5, 112, 6, 'Brazil', 1], [4, 6, 101, 7, 'Bangladesh', 2],
        [8, 1, 192, 4, 'Egypt', 4], [7, 2, 196, 5, 'Peru', 6], [9, 4, 124, 9, 'China', 7], [3, 4, 129, 5, 'Peru', 6], [6, 3, 151, 8, 'Mexico', 9], [5, 7, 114, 7, 'Bangladesh', 4],
        [4, 7, 175, 6, 'Brazil', 5], [1, 8, 121, 1, 'India', 2], [4, 6, 187, 2, 'USA', 5], [6, 5, 144, 9, 'China', 9], [9, 4, 103, 5, 'Peru', 3], [5, 3, 84, 3, 'UK', 1],
        [3, 5, 193, 2, 'USA', 4], [4, 7, 135, 1, 'India', 1], [7, 6, 148, 8, 'Mexico', 8], [1, 6, 160, 5, 'Peru', 7], [8, 6, 155, 6, 'Brazil', 9], [5, 7, 183, 7, 'Bangladesh', 2],
        [2, 9, 125, 4, 'Egypt', 4], [6, 3, 111, 9, 'China', 9], [5, 2, 132, 3, 'UK', 3], [4, 5, 104, 7, 'Bangladesh', 7], [2, 7, 177, 8, 'Mexico', 7]]
    
    
    
    countries_to_id = {'India': 1, 'USA': 2, 'UK': 3, 'Egypt': 4, 'Peru': 5,
                       'Brazil': 6, 'Bangladesh': 7, 'Mexico': 8, 'China': 9}
    

Preprocess the data:

  1. Convert the lists to tensors.
  2. Separate the features from the expected prediction.


    
    
    X = [torch.tensor(item[:4]+[countries_to_id[item[4]]], dtype=torch.float) for item in data]
    Y = [torch.tensor(item[-1], dtype=torch.float) for item in data]
    

Define a simple model that has five input features and predicts a single value.
    
    
    def build_model(n_inputs, n_outputs):
      """build_model builds and returns a model that takes
      `n_inputs` features and predicts `n_outputs` value"""
      return torch.nn.Sequential(
          torch.nn.Linear(n_inputs, 8),
          torch.nn.ReLU(),
          torch.nn.Linear(8, 16),
          torch.nn.ReLU(),
          torch.nn.Linear(16, n_outputs))
    

Train the model.
    
    
    model = build_model(n_inputs=5, n_outputs=1)
    
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters())
    
    for epoch in range(1000):
      print(f'Epoch {epoch}: ---')
      optimizer.zero_grad()
      for i in range(len(X)):
        pred = model(X[i])
        loss = loss_fn(pred, Y[i])
        loss.backward()
      optimizer.step()
    

Save the model to the `STATE_DICT_PATH` variable.
    
    
    STATE_DICT_PATH = './model.pth'
    
    torch.save(model.state_dict(), STATE_DICT_PATH)
    

### Set up the Bigtable table

Create a sample Bigtable table for this notebook.
    
    
    # Connect to the Bigtable instance. If you don't have admin access, then drop `admin=True`.
    client = Client(project=PROJECT_ID, admin=True)
    instance = client.instance(INSTANCE_ID)
    
    # Create a column family.
    column_family_id = 'demograph'
    max_versions_rule = column_family.MaxVersionsGCRule(2)
    column_families = {column_family_id: max_versions_rule}
    
    # Create a table.
    table = instance.table(TABLE_ID)
    
    # You need admin access to use `.exists()`. If you don't have the admin access, then
    # comment out the if-else block.
    if not table.exists():
      table.create(column_families=column_families)
    else:
      print("Table %s already exists in %s:%s" % (TABLE_ID, PROJECT_ID, INSTANCE_ID))
    

Add rows to the table for the enrichment example.
    
    
    # Define column names for the table.
    customer_id = 'customer_id'
    customer_name = 'customer_name'
    customer_location = 'customer_location'
    
    # The following data is sample data to insert into Bigtable.
    customers = [
      {
        'customer_id': 1, 'customer_name': 'Sam', 'customer_location': 'India'
      },
      {
        'customer_id': 2, 'customer_name': 'John', 'customer_location': 'USA'
      },
      {
        'customer_id': 3, 'customer_name': 'Travis', 'customer_location': 'UK'
      },
    ]
    
    for customer in customers:
      row_key = str(customer[customer_id]).encode()
      row = table.direct_row(row_key)
      row.set_cell(
        column_family_id,
        customer_id.encode(),
        str(customer[customer_id]),
        timestamp=datetime.datetime.utcnow())
      row.set_cell(
        column_family_id,
        customer_name.encode(),
        customer[customer_name],
        timestamp=datetime.datetime.utcnow())
      row.set_cell(
        column_family_id,
        customer_location.encode(),
        customer[customer_location],
        timestamp=datetime.datetime.utcnow())
      row.commit()
      print('Inserted row for key: %s' % customer[customer_id])
    
    
    
    Inserted row for key: 1
    Inserted row for key: 2
    Inserted row for key: 3
    

### Publish messages to Pub/Sub

Use the Pub/Sub Python client to publish messages.
    
    
    # Replace <TOPIC_NAME> with the name of your Pub/Sub topic.
    TOPIC = "<TOPIC_NAME>"
    
    # Replace <SUBSCRIPTION_PATH> with the subscription for your topic.
    SUBSCRIPTION = "<SUBSCRIPTION_PATH>"
    
    
    
    messages = [
        {'sale_id': i, 'customer_id': i, 'product_id': i, 'quantity': i, 'price': i*100}
        for i in range(1,4)
      ]
    
    publisher = pubsub_v1.PublisherClient()
    topic_name = publisher.topic_path(PROJECT_ID, TOPIC)
    
    for message in messages:
      data = json.dumps(message).encode('utf-8')
      publish_future = publisher.publish(topic_name, data)
    

## Use the Bigtable enrichment handler

The [`BigTableEnrichmentHandler`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.bigtable.html#apache_beam.transforms.enrichment_handlers.bigtable.BigTableEnrichmentHandler) is a built-in handler included in the Apache Beam SDK versions 2.54.0 and later. Configure the `BigTableEnrichmentHandler` handler with the following required parameters:

  * `project_id`: the Google Cloud project ID for the Bigtable instance
  * `instance_id`: the instance name of the Bigtable cluster
  * `table_id`: the table ID of table containing relevant data
  * `row_key`: The field name from the input row that contains the row key to use when querying Bigtable.

Optionally, you can use parameters to further configure the `BigTableEnrichmentHandler` handler. For more information about the available parameters, see the [enrichment handler module documentation](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.bigtable.html#module-apache_beam.transforms.enrichment_handlers.bigtable). **Note:** When exceptions occur, by default, the logging severity is set to warning ([`ExceptionLevel.WARN`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.utils.html#apache_beam.transforms.enrichment_handlers.utils.ExceptionLevel.WARN)). To configure the severity to raise exceptions, set `exception_level` to [`ExceptionLevel.RAISE`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.utils.html#apache_beam.transforms.enrichment_handlers.utils.ExceptionLevel.RAISE). To ignore exceptions, set `exception_level` to [`ExceptionLevel.QUIET`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.utils.html#apache_beam.transforms.enrichment_handlers.utils.ExceptionLevel.QUIET).The following example demonstrates how to set the exception level in the `BigTableEnrichmentHandler` handler:
    
    
    bigtable_handler = BigTableEnrichmentHandler(project_id=PROJECT_ID,
                                                 instance_id=INSTANCE_ID,
                                                 table_id=TABLE_ID,
                                                 row_key=row_key,
                                                 exception_level=ExceptionLevel.RAISE)
    

The `row_key` parameter represents the field in input schema (`beam.Row`) that contains the row key for a row in the table. Starting with Apache Beam version 2.54.0, you can perform either of the following tasks when a table uses composite row keys:

  * Modify the input schema to contain the row key in the format required by Bigtable.
  * Use a custom enrichment handler. For more information, see the [example handler with composite row key support](https://www.toptal.com/developers/paste-gd/BYFGUL08).


    
    
    row_key = 'customer_id'
    
    
    
    bigtable_handler = BigTableEnrichmentHandler(project_id=PROJECT_ID,
                                                 instance_id=INSTANCE_ID,
                                                 table_id=TABLE_ID,
                                                 row_key=row_key)
    

## Use the enrichment transform

To use the [enrichment transform](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment.html#apache_beam.transforms.enrichment.Enrichment), the enrichment handler parameter is the only required parameter. The following example demonstrates the code needed to add this transform to your pipeline.
    
    
    with beam.Pipeline() as p:
      output = (p
                ...
                | "Enrich with BigTable" >> Enrichment(bigtable_handler)
                | "RunInference" >> RunInference(model_handler)
                ...
                )
    

By default, the enrichment transform performs a [`cross_join`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment.html#apache_beam.transforms.enrichment.cross_join). This join returns the enriched row with the following fields: `sale_id`, `customer_id`, `product_id`, `quantity`, `price`, and `customer_location`. To make a prediction when running the ecommerce example, however, the trained model needs the following fields: `product_id`, `quantity`, `price`, `customer_id`, and `customer_location`. Therefore, to get the required fields for the ecommerce example, design a custom join function that takes two dictionaries as input and returns an enriched row that include these fields.
    
    
    def custom_join(left: Dict[str, Any], right: Dict[str, Any]):
      enriched = {}
      enriched['product_id'] = left['product_id']
      enriched['quantity'] = left['quantity']
      enriched['price'] = left['price']
      enriched['customer_id'] = left['customer_id']
      enriched['customer_location'] = right['demograph']['customer_location']
      return beam.Row(**enriched)
    

To provide a `lambda` function for using a custom join with the enrichment transform, see the following example.
    
    
    with beam.Pipeline() as p:
      output = (p
                ...
                | "Enrich with BigTable" >> Enrichment(bigtable_handler, join_fn=custom_join)
                | "RunInference" >> RunInference(model_handler)
                ...
                )
    

Because the enrichment transform makes API calls to the remote service, use the `timeout` parameter to specify a timeout duration of 10 seconds:
    
    
    with beam.Pipeline() as p:
      output = (p
                ...
                | "Enrich with BigTable" >> Enrichment(bigtable_handler, join_fn=custom_join, timeout=10)
                | "RunInference" >> RunInference(model_handler)
                ...
                )
    

## Use the `PyTorchModelHandlerTensor` interface to run inference

Because the enrichment transform outputs data in the format `beam.Row`, to make it compatible with the [`PyTorchModelHandlerTensor`](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.pytorch_inference.html#apache_beam.ml.inference.pytorch_inference.PytorchModelHandlerTensor) interface, convert it to `torch.tensor`. Additionally, the enriched field `customer_location` is a `string` type, but the model requires a `float` type. Convert the `customer_location` field to a `float` type.
    
    
    def convert_row_to_tensor(element: beam.Row):
      row_dict = element._asdict()
      row_dict['customer_location'] = countries_to_id[row_dict['customer_location']]
      return torch.tensor(list(row_dict.values()), dtype=torch.float)
    

Initialize the model handler with the preprocessing function.
    
    
    model_handler = PytorchModelHandlerTensor(state_dict_path=STATE_DICT_PATH,
                                              model_class=build_model,
                                              model_params={'n_inputs':5, 'n_outputs':1}
                                              ).with_preprocess_fn(convert_row_to_tensor)
    

Define a `DoFn` to format the output.
    
    
    class PostProcessor(beam.DoFn):
      def process(self, element, *args, **kwargs):
        print('Customer %d who bought product %d is recommended to buy product %d' % (element.example[3], element.example[0], math.ceil(element.inference[0])))
    

## Run the pipeline

Configure the pipeline to run in streaming mode.
    
    
    options = pipeline_options.PipelineOptions()
    options.view_as(pipeline_options.StandardOptions).streaming = True # Streaming mode is set True
    

Pub/Sub sends the data in bytes. Convert the data to `beam.Row` objects by using a `DoFn`.
    
    
    class DecodeBytes(beam.DoFn):
      """
      The DecodeBytes `DoFn` converts the data read from Pub/Sub to `beam.Row`.
      First, decode the encoded string. Convert the output to
      a `dict` with `json.loads()`, which is used to create a `beam.Row`.
      """
      def process(self, element, *args, **kwargs):
        element_dict = json.loads(element.decode('utf-8'))
        yield beam.Row(**element_dict)
    

Use the following code to run the pipeline. **Note:** Because this pipeline is a streaming pipeline, you need to manually stop the cell. If you don't stop the cell, the pipeline continues to run.
    
    
    with beam.Pipeline(options=options) as p:
      _ = (p
           | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(subscription=SUBSCRIPTION)
           | "ConvertToRow" >> beam.ParDo(DecodeBytes())
           | "Enrichment" >> Enrichment(bigtable_handler, join_fn=custom_join, timeout=10)
           | "RunInference" >> RunInference(model_handler)
           | "Format Output" >> beam.ParDo(PostProcessor())
           )
    
    
    
    Customer 1 who bought product 1 is recommended to buy product 3
    Customer 2 who bought product 2 is recommended to buy product 5
    Customer 3 who bought product 3 is recommended to buy product 7
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
