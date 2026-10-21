---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/vertex_ai_feature_store_enrichment/
title: Use Apache Beam and Vertex AI Feature Store to enrich data \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:44.039832+00:00
---

# Use Apache Beam and Vertex AI Feature Store to enrich data  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/vertex_ai_feature_store_enrichment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Apache Beam and Vertex AI Feature Store to enrich data Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/vertex_ai_feature_store_enrichment.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/vertex_ai_feature_store_enrichment.ipynb) This notebook shows how to enrich data by using the Apache Beam [enrichment transform](https://beam.apache.org/documentation/transforms/python/elementwise/enrichment/) with [Vertex AI Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore/latest/overview). The enrichment transform is an Apache Beam turnkey transform that lets you enrich data by using a key-value lookup. This transform has the following features:

  * The transform has a built-in Apache Beam handler that interacts with Vertex AI to get precomputed feature values.
  * The transform uses client-side throttling to manage rate limiting the requests.
  * Optionally, you can configure a Redis cache to improve efficiency.

As of Apache Beam SDK version 2.55.0, [online feature serving](https://cloud.google.com/vertex-ai/docs/featurestore/latest/overview#online_serving) through Bigtable online serving and the Vertex AI Feature Store (legacy) method is supported. This notebook demonstrates how to use the Bigtable online serving approach with the enrichment transform in an Apache Beam pipeline. This notebook demonstrates the following ecommerce product recommendation use case based on the BigQuery public dataset [theLook eCommerce](https://pantheon.corp.google.com/marketplace/product/bigquery-public-data/thelook-ecommerce):

  * Use a stream of online transactions from [Pub/Sub](https://cloud.google.com/pubsub/docs/guides) that contains the following fields: `product_id`, `user_id`, and `sale_price`.
  * Deploy a pretrained model on Vertex AI based on the features `product_id`, `user_id`, `sale_price`, `age`, `gender`, `state`, and `country`.
  * Precompute the feature values for the pretrained model, and store the values in Vertex AI Feature Store.
  * Enrich the stream of transactions from Pub/Sub with feature values from Vertex AI Feature Store by using the enrichment transform.
  * Send the enriched data to the Vertex AI model for online prediction by using the `RunInference` transform, which predicts the product recommendation for the user.



## Before you begin

Set up your environment and download dependencies.

### Install Apache Beam

To use the enrichment transform with the built-in Vertex AI handler, install the Apache Beam SDK version 2.55.0 or later.
    
    
    pip install apache_beam[interactive,gcp]==2.55.0 --quiet
    pip install redis
    
    # Use TensorFlow 2.13.0, because it is the latest version that has the prebuilt
    # container image for Vertex AI model deployment.
    # See https://cloud.google.com/vertex-ai/docs/predictions/pre-built-containers#tensorflow
    pip install tensorflow==2.13
    
    
    import json
    import math
    import os
    import time
    
    from typing import Any
    from typing import Dict
    
    import pandas as pd
    from google.cloud import aiplatform
    from google.cloud import pubsub_v1
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.aiplatform_v1 import [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.feature_online_store_admin_service.FeatureOnlineStoreAdminServiceClient.html)
    from google.cloud.aiplatform_v1 import [FeatureRegistryServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.feature_registry_service.FeatureRegistryServiceClient.html)
    from google.cloud.aiplatform_v1.types import feature_view as feature_view_pb2
    from google.cloud.aiplatform_v1.types import \
        feature_online_store as feature_online_store_pb2
    from google.cloud.aiplatform_v1.types import \
        [feature_online_store_admin_service](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.feature_online_store_admin_service.html) as \
        feature_online_store_admin_service_pb2
    
    import apache_beam as beam
    import tensorflow as tf
    import apache_beam.runners.interactive.interactive_beam as ib
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.vertex_ai_inference import VertexAIModelHandlerJSON
    from apache_beam.options import pipeline_options
    from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
    from apache_beam.transforms.enrichment import Enrichment
    from apache_beam.transforms.enrichment_handlers.vertex_ai_feature_store import VertexAIFeatureStoreEnrichmentHandler
    from tensorflow import keras
    from tensorflow.keras import layers
    

### Authenticate with Google Cloud

This notebook reads data from Pub/Sub and Vertex AI. To use your Google Cloud account, authenticate this notebook.
    
    
    from google.colab import auth
    auth.authenticate_user()
    

Replace `<PROJECT_ID>` and `<LOCATION>` with the appropriate values for your Google Cloud account.
    
    
    PROJECT_ID = "<PROJECT_ID>" # @param {type:'string'}
    LOCATION = "<LOCATION>" # @param {type:'string'}
    

### Train and deploy the model to Vertex AI

Fetch the training data from the BigQuery public dataset [thelook-ecommerce](https://pantheon.corp.google.com/marketplace/product/bigquery-public-data/thelook-ecommerce).
    
    
    train_data_query = """
    WITH
     order_items AS (
       SELECT cast(user_id as string) AS user_id,
         product_id,
         sale_price,
       FROM `bigquery-public-data.thelook_ecommerce.order_items`),
      users AS (
       SELECT cast(id as string) AS user_id,
         age,
         lower(gender) as gender,
         lower(state) as state,
         lower(country) as country,
       FROM `bigquery-public-data.thelook_ecommerce.users`)
    SELECT *
    FROM order_items
    LEFT OUTER JOIN users
    USING (user_id)
    """
    
    client = bigquery.Client(project=PROJECT_ID)
    train_data = client.query(train_data_query).result().to_dataframe()
    train_data.head()
    

Create a prediction dataframe that contains the `product_id` to recommend to the user. Preprocess the data for columns that contain the categorical values.
    
    
    # Create a prediction dataframe.
    prediction_data = train_data['product_id'].sample(frac=1, replace=True)
    
    # Preprocess data to handle categorical values.
    train_data['gender'] = pd.factorize(train_data['gender'])[0]
    train_data['state'] = pd.factorize(train_data['state'])[0]
    train_data['country'] = pd.factorize(train_data['country'])[0]
    train_data.head()
    

Convert the dataframe to tensors.
    
    
    train_tensors = tf.convert_to_tensor(train_data.values, dtype=tf.float32)
    prediction_tensors = tf.convert_to_tensor(prediction_data.values, dtype=tf.float32)
    

Based on this data, build a basic neural network model by using TensorFlow.
    
    
    inputs = layers.Input(shape=(7,))
    x = layers.Dense(7, activation='relu')(inputs)
    x = layers.Dense(14, activation='relu')(x)
    outputs = layers.Dense(1)(x)
    
    model = keras.Model(inputs=inputs, outputs=outputs)
    

Train the model. This step takes about 90 seconds for one epoch.
    
    
    EPOCHS = 1
    
    
    
    model.compile(optimizer='adam', loss='mse')
    model.fit(train_tensors, prediction_tensors, epochs=EPOCHS)
    

Save the model to the `MODEL_PATH` variable.
    
    
    # Create a new directory to save the model.
    !mkdir model
    
    # Save the model.
    MODEL_PATH = './model/'
    tf.saved_model.save(model, MODEL_PATH)
    

Stage the locally saved model to a Google Cloud Storage bucket. Use this Cloud Storage bucket to deploy the model to Vertex AI. Replace `<BUCKET_NAME>` with the name of your Cloud Storage bucket. Replace `<BUCKET_DIRECTORY>` with the path to your Cloud Storage bucket.
    
    
    GCS_BUCKET = '<BUCKET_NAME>'
    GCS_BUCKET_DIRECTORY = '<BUCKET_DIRECTORY>'
    
    
    
    # Stage to the Cloud Storage bucket.
    import glob
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(project=PROJECT_ID)
    bucket = client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
    
    def upload_model_to_gcs(model_path, bucket, gcs_model_dir):
        for file in glob.glob(model_path + '/**', recursive=True):
          if os.path.isfile(file):
            path = os.path.join(gcs_model_dir, file[1 + len(model_path.rstrip("/")):])
            blob = bucket.blob(path)
            blob.[upload_from_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_filename)(file)
    
    
    upload_model_to_gcs(MODEL_PATH, bucket, GCS_BUCKET_DIRECTORY)
    

Upload the model saved in the Cloud Storage bucket to Vertex AI Model Registry.
    
    
    model_display_name = 'vertex-ai-enrichment'
    
    
    
    aiplatform.init(project=PROJECT_ID, location=LOCATION)
    model = aiplatform.Model.upload(
      display_name = model_display_name,
      description='Model used in the vertex ai enrichment notebook.',
      artifact_uri="gs://" + GCS_BUCKET + "/" + GCS_BUCKET_DIRECTORY,
      serving_container_image_uri='us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-13:latest',
    )
    

Create an endpoint on Vertex AI.
    
    
    endpoint = aiplatform.Endpoint.create(display_name = model_display_name,
                                          project = PROJECT_ID,
                                          location = LOCATION)
    

Deploy the model to the Vertex AI endpoint. **Note:** This step is a long running operation (LRO). Depending on the size of the model, it might take more than five minutes to complete.
    
    
    deployed_model_display_name = 'vertexai-enrichment-notebook'
    model.deploy(endpoint = endpoint,
                 deployed_model_display_name = deployed_model_display_name,
                 machine_type = 'n1-standard-2')
    
    
    
    model_endpoint_id = aiplatform.Endpoint.list(filter=f'display_name="{deployed_model_display_name}"')[0].name
    print(model_endpoint_id)
    
    
    
    8125472293125095424
    

### Set up Vertex AI Feature Store for online serving

Set up the feature data in BigQuery.
    
    
    feature_store_query = """
    SELECT cast(id as string) AS user_id,
      age,
      lower(gender) as gender,
      lower(state) as state,
      lower(country) as country,
    FROM `bigquery-public-data.thelook_ecommerce.users`
    """
    
    # Fetch feature values from BigQuery.
    client = bigquery.Client(project=PROJECT_ID)
    data = client.query(feature_store_query).result().to_dataframe()
    
    # Convert feature values to the string type. This step helps when creating tensors
    # of these values for inference that requires the same data type.
    data['gender'] = pd.factorize(data['gender'])[0]
    data['gender'] = data['gender'].astype(str)
    data['state'] = pd.factorize(data['state'])[0]
    data['state'] = data['state'].astype(str)
    data['country'] = pd.factorize(data['country'])[0]
    data['country'] = data['country'].astype(str)
    data.head()
    

Create a BigQuery dataset to use as the source for Vertex AI Feature Store.
    
    
    dataset_id = "vertexai_enrichment"
    dataset = bigquery.Dataset(f"{PROJECT_ID}.{dataset_id}")
    dataset.location = "US"
    dataset = client.create_dataset(
        dataset, exists_ok=True, timeout=30
    )
    
    print("Created dataset - %s.%s" % (dataset, dataset_id))
    

Create a BigQuery view with the precomputed feature values.
    
    
    view_id = "users_view"
    view_reference = "%s.%s.%s" % (PROJECT_ID, dataset_id, view_id)
    view = bigquery.Table(view_reference)
    view = client.load_table_from_dataframe(data, view_reference)
    

Initialize clients for Vertex AI to create and set up an online store.
    
    
    API_ENDPOINT = f"{LOCATION}-aiplatform.googleapis.com"
    
    admin_client = FeatureOnlineStoreAdminServiceClient(
        client_options={"api_endpoint": API_ENDPOINT}
    )
    registry_client = FeatureRegistryServiceClient(
        client_options={"api_endpoint": API_ENDPOINT}
    )
    

Create an online store instances on Vertex AI.
    
    
    feature_store_name = "vertexai_enrichment"
    
    online_store_config = feature_online_store_pb2.FeatureOnlineStore(
        bigtable=feature_online_store_pb2.FeatureOnlineStore.Bigtable(
            auto_scaling=feature_online_store_pb2.FeatureOnlineStore.Bigtable.AutoScaling(
                min_node_count=1, max_node_count=1, cpu_utilization_target=80
            )
        )
    )
    
    create_store_lro = admin_client.create_feature_online_store(
        feature_online_store_admin_service_pb2.CreateFeatureOnlineStoreRequest(
            parent=f"projects/{PROJECT_ID}/locations/{LOCATION}",
            feature_online_store_id=feature_store_name,
            feature_online_store=online_store_config,
        )
    )
    
    create_store_lro.result()
    

For the store instances created previously, use BigQuery as the data source to create feature views.
    
    
    feature_view_name = "users"
    
    bigquery_source = feature_view_pb2.FeatureView.BigQuerySource(
        uri=f"bq://{view_reference}", entity_id_columns=["user_id"]
    )
    
    create_view_lro = admin_client.create_feature_view(
        feature_online_store_admin_service_pb2.CreateFeatureViewRequest(
            parent=f"projects/{PROJECT_ID}/locations/{LOCATION}/featureOnlineStores/{feature_store_name}",
            feature_view_id=feature_view_name,
            feature_view=feature_view_pb2.FeatureView(
                big_query_source=bigquery_source,
            ),
        )
    )
    
    create_view_lro.result()
    

Pull feature values from BigQuery into the feature store.
    
    
    sync_response = admin_client.sync_feature_view(
        feature_view=f"projects/{PROJECT_ID}/locations/{LOCATION}/featureOnlineStores/{feature_store_name}/featureViews/{feature_view_name}"
    )
    
    
    
    while True:
        feature_view_sync = admin_client.get_feature_view_sync(
            name=sync_response.feature_view_sync
        )
        if feature_view_sync.run_time.end_time.seconds > 0:
            if feature_view_sync.final_status.code == 0
              print("feature view sync completed for %s" % feature_view_sync.name)
            else:
              print("feature view sync failed for %s" % feature_view_sync.name)
            break
        time.sleep(10)
    

Confirm the sync creation.
    
    
    admin_client.list_feature_view_syncs(
        parent=f"projects/{PROJECT_ID}/locations/{LOCATION}/featureOnlineStores/{feature_store_name}/featureViews/{feature_view_name}"
    )
    

### Publish messages to Pub/Sub

Use the Pub/Sub Python client to publish messages.
    
    
    # Replace <TOPIC_NAME> with the name of your Pub/Sub topic.
    TOPIC = "<TOPIC_NAME>" # @param {type:'string'}
    
    # Replace <SUBSCRIPTION_NAME> with the subscription path for your topic.
    SUBSCRIPTION = "<SUBSCRIPTION_NAME>" # @param {type:'string'}
    

Retrieve sample data from a public dataset in BigQuery. Convert it into Python dictionaries, and then send it to Pub/Sub.
    
    
    read_query = """
    SELECT cast(user_id as string) AS user_id,
      product_id,
      sale_price,
    FROM `bigquery-public-data.thelook_ecommerce.order_items`
    LIMIT 5;
    """
    
    client = bigquery.Client(project=PROJECT_ID)
    data = client.query(read_query).result().to_dataframe()
    data.head()
    
    
    
    messages = data.to_dict(orient='records')
    
    publisher = pubsub_v1.PublisherClient()
    topic_name = publisher.topic_path(PROJECT_ID, TOPIC)
    subscription_path = publisher.subscription_path(PROJECT_ID, SUBSCRIPTION)
    for message in messages:
      data = json.dumps(message).encode('utf-8')
      publish_future = publisher.publish(topic_name, data)
    

## Use the Vertex AI Feature Store enrichment handler

The [`VertexAIFeatureStoreEnrichmentHandler`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.vertex_ai_feature_store.html#apache_beam.transforms.enrichment_handlers.vertex_ai_feature_store.VertexAIFeatureStoreEnrichmentHandler) is a built-in handler in the Apache Beam SDK versions 2.55.0 and later. Configure the `VertexAIFeatureStoreEnrichmentHandler` handler with the following required parameters:

  * `project`: the Google Cloud project ID for the feature store
  * `location`: the region of the feature store, for example `us-central1`
  * `api_endpoint`: the public endpoint of the feature store
  * `feature_store_name`: the name of the Vertex AI feature store
  * `feature_view_name`: the name of the feature view within the Vertex AI feature store
  * `row_key`: The field name in the input row containing the entity ID for the feature store. This value is used to extract the entity ID from each element. The entity ID is used to fetch feature values for that specific element in the enrichment transform.

Optionally, to provide more configuration values to connect with the Vertex AI client, the `VertexAIFeatureStoreEnrichmentHandler` handler accepts a keyword argument (kwargs). For more information, see [`FeatureOnlineStoreServiceClient`](https://cloud.google.com/php/docs/reference/cloud-ai-platform/latest/V1.FeatureOnlineStoreServiceClient). **Note:** When exceptions occur, by default, the logging severity is set to warning ([`ExceptionLevel.WARN`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.utils.html#apache_beam.transforms.enrichment_handlers.utils.ExceptionLevel.WARN)). To configure the severity to raise exceptions, set `exception_level` to [`ExceptionLevel.RAISE`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.utils.html#apache_beam.transforms.enrichment_handlers.utils.ExceptionLevel.RAISE). To ignore exceptions, set `exception_level` to [`ExceptionLevel.QUIET`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment_handlers.utils.html#apache_beam.transforms.enrichment_handlers.utils.ExceptionLevel.QUIET).The `VertexAIFeatureStoreEnrichmentHandler` handler returns the latest feature values from the feature store.
    
    
    row_key = 'user_id'
    
    
    
    vertex_ai_handler = VertexAIFeatureStoreEnrichmentHandler(project=PROJECT_ID,
                                                 location=LOCATION,
                                                 api_endpoint = API_ENDPOINT,
                                                 feature_store_name=feature_store_name,
                                                 feature_view_name=feature_view_name,
                                                 row_key=row_key)
    

## Use the enrichment transform

To use the [enrichment transform](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment.html#apache_beam.transforms.enrichment.Enrichment), the [`EnrichmentHandler`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment.html#apache_beam.transforms.enrichment.EnrichmentSourceHandler) parameter is required. You can also use configuration parameters to specify a `lambda` for a join function, a timeout, a throttler, and a repeater (retry strategy). For more information, see [Parameters](https://cloud.google.com/dataflow/docs/guides/enrichment#parameters). To use the Redis cache, apply the `with_redis_cache` hook to the enrichment transform. The coders for encoding and decoding the input and output for the cache are optional and are internally inferred. The following example demonstrates the code needed to add this transform to your pipeline.
    
    
    with beam.Pipeline() as p:
      output = (p
                ...
                | "Enrich with Vertex AI" >> Enrichment(vertex_ai_handler)
                | "RunInference" >> RunInference(model_handler)
                ...
                )
    

To make a prediction, use the following fields: `product_id`, `quantity`, `price`, `customer_id`, and `customer_location`. Retrieve the value of the `customer_location` field from Bigtable. The enrichment transform performs a [`cross_join`](https://beam.apache.org/releases/pydoc/current/apache_beam.transforms.enrichment.html#apache_beam.transforms.enrichment.cross_join) by default.

## Use the `VertexAIModelHandlerJSON` interface to run inference

Because the enrichment transform outputs data in the format `beam.Row`, in order to align it with the [`VertexAIModelHandlerJSON`](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.vertex_ai_inference.html#apache_beam.ml.inference.vertex_ai_inference.VertexAIModelHandlerJSON) interface, convert the output into a list of `tensorflow.tensor`. Some enriched fields are of `string` type. For tensor creation, all values must be of the same type. Therefore, convert any `string` type fields to `int` type fields before creating a tensor.
    
    
    def convert_row_to_tensor(element: beam.Row):
      element_dict = element._asdict()
      row = list(element_dict.values())
      for i, r in enumerate(row):
        if isinstance(r, str):
          row[i] = int(r)
      return  tf.convert_to_tensor(row, dtype=tf.float32).numpy().tolist()
    

Initialize the model handler with the preprocessing function.
    
    
    model_handler = VertexAIModelHandlerJSON(endpoint_id=model_endpoint_id,
                                             project=PROJECT_ID,
                                             location=LOCATION,
                                            ).with_preprocess_fn(convert_row_to_tensor)
    

Define a `DoFn` to format the output.
    
    
    class PostProcessor(beam.DoFn):
      def process(self, element, *args, **kwargs):
        print('Customer %d who bought product %d is recommended to buy product %d' % (element.example[0], element.example[1], math.ceil(element.inference[0])))
    

## Run the pipeline

Configure the pipeline to run in streaming mode.
    
    
    options = pipeline_options.PipelineOptions()
    options.view_as(pipeline_options.StandardOptions).streaming = True  # Streaming mode is set to True
    

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
           | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(subscription=subscription_path)
           | "ConvertToRow" >> beam.ParDo(DecodeBytes())
           | "Enrichment" >> Enrichment(vertex_ai_handler)
           | "RunInference" >> RunInference(model_handler)
           | "Format Output" >> beam.ParDo(PostProcessor())
           )
    
    
    
    Customer 25005 who bought product 14235 is recommended to buy product 8944
    Customer 62544 who bought product 14235 is recommended to buy product 23313
    Customer 17228 who bought product 14235 is recommended to buy product 6600
    Customer 54015 who bought product 14235 is recommended to buy product 19682
    Customer 16569 who bought product 14235 is recommended to buy product 6441
    

## Clean up resources
    
    
    # Delete feature views.
    admin_client.delete_feature_view(
        name=f"projects/{PROJECT_ID}/locations/{LOCATION}/featureOnlineStores/{feature_store_name}/featureViews/{feature_view_name}"
    )
    
    # Delete online store instance.
    admin_client.delete_feature_online_store(
        name=f"projects/{PROJECT_ID}/locations/{LOCATION}/featureOnlineStores/{feature_store_name}",
        force=True,
    )
    
    
    
    <google.api_core.operation.Operation at 0x7b0e1a2843d0>
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
