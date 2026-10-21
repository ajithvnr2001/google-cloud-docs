---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/bigquery_enrichment_transform/
title: Use Apache Beam and BigQuery to enrich data \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:44.457266+00:00
---

# Use Apache Beam and BigQuery to enrich data  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/bigquery_enrichment_transform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Apache Beam and BigQuery to enrich data Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/bigquery_enrichment_transform.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/bigquery_enrichment_transform.ipynb) This notebook shows how to enrich data by using the Apache Beam [enrichment transform](https://beam.apache.org/documentation/transforms/python/elementwise/enrichment/) with [BigQuery](https://cloud.google.com/bigquery/docs/overview). The enrichment transform is an Apache Beam turnkey transform that lets you enrich data by using a key-value lookup. This transform has the following features:

  * The transform has a built-in Apache Beam handler that interacts with BigQuery data during enrichment.
  * The enrichment transform uses client-side throttling to rate limit the requests. The default retry strategy uses exponential backoff. You can configure rate limiting to suit your use case.

This notebook demonstrates the following telecommunications company use case: A telecom company wants to predict which customers are likely to cancel their subscriptions so that the company can proactively offer these customers incentives to stay. The example uses customer demographic data and usage data stored in BigQuery to enrich a stream of customer IDs. The enriched data is then used to predict the likelihood of customer churn.

## Before you begin

Set up your environment and download dependencies.

### Install Apache Beam

To use the enrichment transform with the built-in BigQuery handler, install the Apache Beam SDK version 2.57.0 or later.
    
    
    pip install torch
    pip install apache_beam[interactive,gcp]==2.57.0 --quiet

Import the following modules:

  * Pub/Sub for streaming data
  * BigQuery for enrichment
  * Apache Beam for running the streaming pipeline
  * PyTorch to predict customer churn


    
    
    import datetime
    import json
    import math
    
    from typing import Any
    from typing import Dict
    
    import torch
    from google.cloud import pubsub_v1
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    from google.api_core.exceptions import Conflict
    
    import apache_beam as beam
    import apache_beam.runners.interactive.interactive_beam as ib
    from apache_beam.ml.inference.base import KeyedModelHandler
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.pytorch_inference import PytorchModelHandlerTensor
    from apache_beam.options import pipeline_options
    from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
    from apache_beam.transforms.enrichment import Enrichment
    from apache_beam.transforms.enrichment_handlers.bigquery import BigQueryEnrichmentHandler
    
    import pandas as pd
    
    from sklearn.preprocessing import LabelEncoder
    
    
    
    
    

### Authenticate with Google Cloud

This notebook reads data from Pub/Sub and BigQuery. To use your Google Cloud account, authenticate this notebook. To prepare for this step, replace `<PROJECT_ID>` with your Google Cloud project ID.
    
    
    PROJECT_ID = "<PROJECT_ID>" # @param {type:'string'}
    
    
    
    
    
    
    
    from google.colab import auth
    auth.authenticate_user(project_id=PROJECT_ID)
    
    
    
    
    

### Set up the BigQuery tables

Create sample BigQuery tables for this notebook.

  * Replace `<DATASET_ID>` with the name of your BigQuery dataset. Only letters (uppercase or lowercase), numbers, and underscores are allowed.
  * If the dataset does not exist, a new dataset with this ID is created.


    
    
    DATASET_ID = "<DATASET_ID>" # @param {type:'string'}
    
    CUSTOMERS_TABLE_ID = f'{PROJECT_ID}.{DATASET_ID}.customers'
    USAGE_TABLE_ID = f'{PROJECT_ID}.{DATASET_ID}.usage'
    
    
    
    
    

Create customer and usage tables, and insert fake data.
    
    
    client = bigquery.Client(project=PROJECT_ID)
    
    # Create dataset if it does not exist.
    client.create_dataset(bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}"), exists_ok=True)
    print(f"Created dataset {DATASET_ID}")
    
    # Prepare the fake customer data.
    customer_data = {
        'customer_id': [1, 2, 3, 4, 5],
        'age': [35, 28, 45, 62, 22],
        'plan': ['Gold', 'Silver', 'Bronze', 'Gold', 'Silver'],
        'contract_length': [12, 24, 6, 36, 12]
    }
    
    customers_df = pd.DataFrame(customer_data)
    
    # Insert customer data.
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("customer_id", "INTEGER"),
            bigquery.SchemaField("age", "INTEGER"),
            bigquery.SchemaField("plan", "STRING"),
            bigquery.SchemaField("contract_length", "INTEGER"),
        ],
        write_disposition="WRITE_TRUNCATE",
    )
    
    job = client.load_table_from_dataframe(
        customers_df, CUSTOMERS_TABLE_ID, job_config=job_config
    )
    job.result()  # Wait for the job to complete.
    print(f"Customers table created and populated: {CUSTOMERS_TABLE_ID}")
    
    # Prepare the fake usage data.
    usage_data = {
        'customer_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        'date': pd.to_datetime(['2024-09-01', '2024-10-01', '2024-09-01', '2024-10-01', '2024-09-01', '2024-10-01', '2024-09-01', '2024-10-01', '2024-09-01', '2024-10-01']),
        'calls_made': [50, 65, 20, 18, 100, 110, 30, 28, 60, 70],
        'data_usage_gb': [10, 12, 5, 4, 20, 22, 8, 7, 15, 18]
    }
    usage_df = pd.DataFrame(usage_data)
    
    # Insert usage data.
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("customer_id", "INTEGER"),
            bigquery.SchemaField("date", "DATE"),
            bigquery.SchemaField("calls_made", "INTEGER"),
            bigquery.SchemaField("data_usage_gb", "FLOAT"),
        ],
        write_disposition="WRITE_TRUNCATE",
    )
    job = client.load_table_from_dataframe(
        usage_df, USAGE_TABLE_ID, job_config=job_config
    )
    job.result()  # Wait for the job to complete.
    
    print(f"Usage table created and populated: {USAGE_TABLE_ID}")
    
    
    
    
    

### Train the model

Create sample data and train a simple model for churn prediction.
    
    
    # Create fake training data
    data = {
        'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'age': [35, 28, 45, 62, 22, 38, 55, 25, 40, 30],
        'plan': ['Gold', 'Silver', 'Bronze', 'Gold', 'Silver', 'Bronze', 'Gold', 'Silver', 'Bronze', 'Silver'],
        'contract_length': [12, 24, 6, 36, 12, 18, 30, 12, 24, 18],
        'avg_monthly_calls': [57.5, 19, 100, 30, 60, 45, 25, 70, 50, 35],
        'avg_monthly_data_usage_gb': [11, 4.5, 20, 8, 15, 10, 7, 18, 12, 8],
        'churned': [0, 0, 1, 0, 1, 0, 0, 1, 0, 1]  # Target variable
    }
    plan_encoder = LabelEncoder()
    plan_encoder.fit(data['plan'])
    df = pd.DataFrame(data)
    df['plan'] = plan_encoder.transform(data['plan'])
    
    
    
    
    

Preprocess the data:

  1. Convert the lists to tensors.
  2. Separate the features from the expected prediction.


    
    
    features = ['age', 'plan', 'contract_length', 'avg_monthly_calls', 'avg_monthly_data_usage_gb']
    target = 'churned'
    
    X = torch.tensor(df[features].values, dtype=torch.float)
    Y = torch.tensor(df[target], dtype=torch.float)
    
    
    
    
    

Define a model that has five input features and predicts a single value.
    
    
    def build_model(n_inputs, n_outputs):
      """build_model builds and returns a model that takes
      `n_inputs` features and predicts `n_outputs` value"""
      return torch.nn.Sequential(
          torch.nn.Linear(n_inputs, 8),
          torch.nn.ReLU(),
          torch.nn.Linear(8, 16),
          torch.nn.ReLU(),
          torch.nn.Linear(16, n_outputs),
          torch.nn.Sigmoid())
    
    
    
    
    

Train the model.
    
    
    model = build_model(n_inputs=5, n_outputs=1)
    
    loss_fn = torch.nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters())
    
    for epoch in range(1000):
      print(f'Epoch {epoch}: ---')
      optimizer.zero_grad()
      for i in range(len(X)):
        pred = model(X[i])
        loss = loss_fn(pred, Y[i].unsqueeze(0))
        loss.backward()
      optimizer.step()
    
    
    
    
    

Save the model to the `STATE_DICT_PATH` variable.
    
    
    STATE_DICT_PATH = './model.pth'
    torch.save(model.state_dict(), STATE_DICT_PATH)
    
    
    
    
    

### Publish messages to Pub/Sub

Create the Pub/Sub topic and subscription to use for data streaming.
    
    
    # Replace <TOPIC_NAME> with the name of your Pub/Sub topic.
    TOPIC = "<TOPIC_NAME>" # @param {type:'string'}
    
    # Replace <SUBSCRIPTION_PATH> with the subscription for your topic.
    SUBSCRIPTION = "<SUBSCRIPTION_PATH>" # @param {type:'string'}
    
    
    
    
    
    
    
    from google.api_core.exceptions import AlreadyExists
    
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC)
    try:
      topic = publisher.create_topic(request={"name": topic_path})
      print(f"Created topic: {topic.name}")
    except AlreadyExists:
      print(f"Topic {topic_path} already exists.")
    
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION)
    try:
        subscription = subscriber.create_subscription(
            request={"name": subscription_path, "topic": topic_path}
        )
        print(f"Created subscription: {subscription.name}")
    except AlreadyExists:
      print(f"Subscription {subscription_path} already exists.")
    
    
    
    
    

Use the Pub/Sub Python client to publish messages.
    
    
    messages = [
        {'customer_id': i}
        for i in range(1, 6)
    ]
    
    for message in messages:
      data = json.dumps(message).encode('utf-8')
      publish_future = publisher.publish(topic_path, data)
    
    
    
    
    

## Use the BigQuery enrichment handler

The [`BigQueryEnrichmentHandler`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.bigquery.html#apache_beam.transforms.enrichment_handlers.bigquery.BigQueryEnrichmentHandler) is a built-in handler included in the Apache Beam SDK versions 2.57.0 and later. Configure the `BigQueryEnrichmentHandler` handler with the following parameters.

### Required parameters

The following parameters are required.

  * `project` (str): The Google Cloud project ID for the BigQuery table

You must also provide one of the following combinations:

  * `table_name`, `row_restriction_template`, and `fields`
  * `table_name`, `row_restriction_template`, and `condition_value_fn`
  * `query_fn`



### Optional parameters

The following parameters are optional.

  * `table_name` (str): The fully qualified BigQuery table name in the format `project.dataset.table`
  * `row_restriction_template` (str): A template string for the `WHERE` clause in the BigQuery query with placeholders (`{}`) to dynamically filter rows based on input data
  * `fields` (Optional[List[str]]): A list of field names present in the input `beam.Row`. These fields names are used to construct the `WHERE` clause if `condition_value_fn` is not provided.
  * `column_names` (Optional[List[str]]): The names of columns to select from the BigQuery table. If not provided, all columns (`*`) are selected.
  * `condition_value_fn` (Optional[Callable[[beam.Row], List[Any]]]): A function that takes a `beam.Row` and returns a list of values to populate in the placeholder `{}` of the `WHERE` clause in the query
  * `query_fn` (Optional[Callable[[beam.Row], str]]): A function that takes a `beam.Row` and returns a complete BigQuery SQL query string
  * `min_batch_size` (int): The minimum number of rows to batch together when querying BigQuery. Defaults to `1` if `query_fn` is not specified.
  * `max_batch_size` (int): The maximum number of rows to batch together. Defaults to `10,000` if `query_fn` is not specified.



### Parameter requirements

When you use parameters, consider the following requirements.

  * You can't define the `min_batch_size` and `max_batch_size` parameters if you provide the `query_fn` parameter.
  * You must provide either the `fields` parameter or the `condition_value_fn` parameter for query construction if you don't provide the `query_fn` parameter.
  * You must grant the appropriate permissions to access BigQuery.



### Create handlers

In this example, you create two handlers:

  * One for customer data that specifies `table_name` and `row_restriction_template`
  * One for usage data that uses a custom aggregation query by using the `query_fn` function

These handlers are used in the Enrichment transforms in this pipeline to fetch and join data from BigQuery with the streaming data.
    
    
    user_data_handler = BigQueryEnrichmentHandler(
        project=PROJECT_ID,
        table_name=f"`{CUSTOMERS_TABLE_ID}`",
        row_restriction_template='customer_id = {}',
        fields=['customer_id']
    )
    
    # Define the SQL query for usage data aggregation.
    usage_data_query_template = f"""
    WITH monthly_aggregates AS (
      SELECT
        customer_id,
        DATE_TRUNC(date, MONTH) as month,
        SUM(calls_made) as total_calls,
        SUM(data_usage_gb) as total_data_usage_gb
      FROM
        `{USAGE_TABLE_ID}`
      WHERE
        customer_id = @customer_id
      GROUP BY
        customer_id, month
    )
    SELECT
      customer_id,
      AVG(total_calls) as avg_monthly_calls,
      AVG(total_data_usage_gb) as avg_monthly_data_usage_gb
    FROM
      monthly_aggregates
    GROUP BY
      customer_id
    """
    
    def usage_data_query_fn(row: beam.Row) -> str:
        return usage_data_query_template.replace('@customer_id', str(row.customer_id))
    
    usage_data_handler = BigQueryEnrichmentHandler(
        project=PROJECT_ID,
        query_fn=usage_data_query_fn
    )
    
    
    
    
    

In this example:

  1. The `user_data_handler` handler uses the `table_name`, `row_restriction_template`, and `fields` parameter combination to fetch customer data.
  2. The `usage_data_handler` handler uses the `query_fn` parameter to execute a more complex query that aggregates usage data.



## Use the `PytorchModelHandlerTensor` interface to run inference

Define functions to convert enriched data to the tensor format for the model.
    
    
    def convert_row_to_tensor(customer_data):
        import pandas as pd
        customer_df = pd.DataFrame([customer_data[1].as_dict()])
        customer_df['plan'] = plan_encoder.transform(customer_df['plan'])
        return (customer_data[0], torch.tensor(customer_df[features].values, dtype=torch.float))
    
    keyed_model_handler = KeyedModelHandler(PytorchModelHandlerTensor(
        state_dict_path=STATE_DICT_PATH,
        model_class=build_model,
        model_params={'n_inputs':5, 'n_outputs':1}
    )).with_preprocess_fn(convert_row_to_tensor)
    
    
    
    
    

Define a `DoFn` to format the output.
    
    
    class PostProcessor(beam.DoFn):
      def process(self, element, *args, **kwargs):
        print('Customer %d churn risk: %s' % (element[0], "High" if element[1].inference[0].item() > 0.5 else "Low"))
    
    
    
    
    

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
           | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(subscription=f"projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION}")
           | "ConvertToRow" >> beam.ParDo(DecodeBytes())
           | "Enrich with customer data" >> Enrichment(user_data_handler)
           | "Enrich with usage data" >> Enrichment(usage_data_handler)
           | "Key data" >> beam.Map(lambda x: (x.customer_id, x))
           | "RunInference" >> RunInference(keyed_model_handler)
           | "Format Output" >> beam.ParDo(PostProcessor())
           )
    
    
    
    
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
