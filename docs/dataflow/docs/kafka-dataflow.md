---
url: https://docs.cloud.google.com/dataflow/docs/kafka-dataflow/
title: Write data from Kafka to BigQuery by using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:18.407392+00:00
---

# Write data from Kafka to BigQuery by using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/kafka-dataflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Write data from Kafka to BigQuery by using Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to use Dataflow to read data from [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview) and write the records to a BigQuery table. This tutorial uses the [Apache Kafka to BigQuery template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-bigquery) to create the Dataflow job.

## Overview

[Apache Kafka](https://kafka.apache.org/) is an open source platform for streaming events. Kafka is commonly used in distributed architectures to enable communication between loosely coupled components. You can use Dataflow to read events from Kafka, process them, and write the results to a BigQuery table for further analysis.

Managed Service for Apache Kafka is a Google Cloud service that helps you run secure and scalable Kafka clusters.

![Reading Kafka events into BigQuery](https://docs.cloud.google.com/static/dataflow/images/kafka-dataflow.png)Event-driven architecture using Apache Kafka

## Required permissions

The Dataflow [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) must have the following Identity and Access Management (IAM) roles:

  * Managed Kafka Client (`roles/managedkafka.client`)
  * BigQuery Data Editor (`roles/bigquery.dataEditor`)



For more information, see [Dataflow security and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions).

## Create a Kafka cluster

In this step, you create a Managed Service for Apache Kafka cluster. For more information, see [Create a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click **Create**.

  3. In the **Cluster name** box, enter a name for the cluster.

  4. In the **Region** list, select a location for the cluster.

  5. Click **Create**.




### gcloud

Use the [`managed-kafka clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create) command.
    
    
    gcloud managed-kafka clusters create CLUSTER \
    --location=REGION \
    --cpu=3 \
    --memory=3GiB \
    --subnets=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
    

Replace the following:

  * `CLUSTER`: a name for the cluster
  * `REGION`: the region where you created the subnet
  * `PROJECT_ID`: your project ID
  * `SUBNET_NAME`: the subnet where you want to deploy the cluster



Creating a cluster usually takes 20-30 minutes.

## Create a Kafka topic

After the Managed Service for Apache Kafka cluster is created, create a topic.

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. In the cluster details page, click **Create Topic**.

  4. In the **Topic name** box, enter a name for the topic.

  5. Click **Create**.




### gcloud

Use the [`managed-kafka topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create) command.
    
    
    gcloud managed-kafka topics create TOPIC_NAME \
    --cluster=CLUSTER \
    --location=REGION \
    --partitions=10 \
    --replication-factor=3
    

Replace the following:

  * `TOPIC_NAME`: the name of the topic to create



## Create a BigQuery table

In this step, you create a BigQuery table with the following schema:

Column name | Data type  
---|---  
`name` | `STRING`  
`customer_id` | `INTEGER`  
  
If you don't already have a BigQuery dataset, first create one. For more information, see [Create datasets](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset). Then create a new empty table:

###  Console 

  1. Go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, expand your project, and then select a dataset.

  3. In the **Dataset** info section, click add_box **Create table**.

  4. In the **Create table from** list, select **Empty table**.

  5. In the **Table** box, enter the name of the table.

  6. In the **Schema** section, click **Edit as text**.

  7. Paste in the following schema definition:
         
         name:STRING,
         customer_id:INTEGER
         

  8. Click **Create table**.




###  gcloud 

Use the [`bq mk`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_mk) command.
    
    
    bq mk --table \
      PROJECT_ID:DATASET_NAME.TABLE_NAME \
      name:STRING,customer_id:INTEGER
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `DATASET_NAME`: the name of the dataset
  * `TABLE_NAME`: the name of the table to create



## Run the Dataflow job

After you create the Kafka cluster and the BigQuery table, run the Dataflow template.

**Note:** You can also use this template to read from an external Kafka cluster. You might need to configure networking so that the Dataflow worker VMs can reach the brokers in your cluster. For more information, see [Configure networking](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka#networking).

###  Console 

First, get the cluster's bootstrap server address:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the cluster name.

  3. Click the **Configurations** tab.

  4. Copy the bootstrap server address from **Bootstrap URL**.




Next, run the template to create the Dataflow job:

  1. Go to the **Dataflow** > **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click **Create job from template**.

  3. In the **Job Name** field, enter `kafka-to-bq`.

  4. For **Regional endpoint** , select the region where your Managed Service for Apache Kafka cluster is located.

  5. Select the "Kafka to BigQuery" template.

  6. Enter the following template parameters:

     * **Kafka bootstrap server** : the bootstrap server address
     * **Source Kafka topic** : the name of the topic to read
     * **Kafka source authentication mode** : `APPLICATION_DEFAULT_CREDENTIALS`
     * **Kafka message format** : `JSON`
     * **Table name strategy** : `SINGLE_TABLE_NAME`
     * **BigQuery output table** : The BigQuery table, formatted as follows: `PROJECT_ID`:`DATASET_NAME`.`TABLE_NAME`
  7. Under **Dead letter queue** , check **Write errors to BigQuery**.

  8. Enter a BigQuery table name for the dead-letter queue, formatted as follows: `PROJECT_ID`:`DATASET_NAME`.`ERROR_TABLE_NAME`

Don't create this table ahead of time. The pipeline creates it.

  9. Click **Run job**.




###  gcloud 

Use the [`dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command.
    
    
    gcloud dataflow flex-template run kafka-to-bq \
    --template-file-gcs-location gs://dataflow-templates/latest/flex/Kafka_to_BigQuery \
    --region LOCATION \
    --parameters \
    readBootstrapServerAndTopic=projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_ID/topics/TOPIC,\
    persistKafkaKey=false,\
    writeMode=SINGLE_TABLE_NAME,\
    kafkaReadOffset=earliest,\
    kafkaReadAuthenticationMode=APPLICATION_DEFAULT_CREDENTIALS,\
    messageFormat=JSON,\
    outputTableSpec=PROJECT_ID:DATASET_NAME.TABLE_NAME\
    useBigQueryDLQ=true,\
    outputDeadletterTable=PROJECT_ID:DATASET_NAME.ERROR_TABLE_NAME

Replace the following variables:

  * `LOCATION`: the region where your Managed Service for Apache Kafka is located
  * `PROJECT_ID`: the name of your Google Cloud project
  * `CLUSTER_ID`: the name of the cluster
  * `TOPIC`: the name of the Kafka topic
  * `DATASET_NAME`: the name of the dataset
  * `TABLE_NAME`: the name of the table
  * `ERROR_TABLE_NAME`: a BigQuery table name for the dead-letter queue



Don't create the table for the dead-letter queue ahead of time. The pipeline creates it.

## Send messages to Kafka

After the Dataflow job starts, you can send messages to Kafka, and the pipeline writes them to BigQuery.

  1. Create a VM in the same subnet as the Kafka cluster and install Kafka command line tools. For detailed instructions, see [Set up a client machine](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart#set_up_a_client_machine) in [Publish and consume messages with the CLI](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart).

  2. Run the following command to write messages to the Kafka topic:
         
         kafka-console-producer.sh \
          --topic TOPIC \
          --bootstrap-server bootstrap.CLUSTER_ID.LOCATION.managedkafka.PROJECT_ID.cloud.goog:9092 \
          --producer.config client.properties

Replace the following variables:

     * `TOPIC`: the name of the Kafka topic
     * `CLUSTER_ID`: the name of the cluster
     * `LOCATION`: the region where your cluster is located
     * `PROJECT_ID`: the name of your Google Cloud project
  3. At the prompt, enter the following lines of text to send messages to Kafka:
         
         {"name": "Alice", "customer_id": 1}
         {"name": "Bob", "customer_id": 2}
         {"name": "Charles", "customer_id": 3}
         




## Use a dead-letter queue

While the job is running, the pipeline might fail to write individual messages to BigQuery. Possible errors include:

  * Serialization errors, including badly-formatted JSON.
  * Type conversion errors, caused by a mismatch in the table schema and the JSON data.
  * Extra fields in the JSON data that are not present in the table schema.



These errors don't cause the job to fail, and they don't appear as errors in the Dataflow job log. Instead, the pipeline uses a _dead letter queue_ to handle these types of errors.

To enable the dead-letter queue when you run the template, set the following template parameters:

  * `useBigQueryDLQ`: `true`
  * `outputDeadletterTable`: a fully-qualified BigQuery table name; for example, `my-project:dataset1.errors`



The pipeline automatically creates the table. If an error occurs when processing a Kafka message, the pipeline writes an error entry to the table.

Example error messages:

Type of error | Event data | errorMessage  
---|---|---  
Serialization error | "Hello world" | Failed to serialize json to table row: "Hello world"  
Type conversion error | {"name":"Emily","customer_id":"abc"} | { "errors" : [ { "debugInfo" : "", "location" : "age", "message" : "Cannot convert value to integer (bad value): abc", "reason" : "invalid" } ], "index" : 0 }  
Unknown field | {"name":"Zoe","age":34} | { "errors" : [ { "debugInfo" : "", "location" : "age", "message" : "no such field: customer_id.", "reason" : "invalid" } ], "index" : 0 }  
  
## Work with BigQuery data types

Internally, the Kafka I/O connector converts JSON message payloads to Apache Beam [`TableRow`](https://www.javadoc.io/doc/com.google.apis/google-api-services-bigquery/latest/com/google/api/services/bigquery/model/TableRow.html) objects, and translates the `TableRow` field values into BigQuery types.

The following table shows JSON representations of BigQuery [data types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types).

BigQuery type | JSON representation  
---|---  
`ARRAY` | `[1.2,3]`  
`BOOL` | `true`  
`DATE` | `"2022-07-01"`  
`DATETIME` | `"2022-07-01 12:00:00.00"`  
`DECIMAL` | `5.2E11`  
`FLOAT64` | `3.142`  
`GEOGRAPHY` | `"POINT(1 2)"`  
Specify the geography using either well-known text (WKT) or GeoJSON, formatted as a string. For more information, see [Loading geospatial data](https://docs.cloud.google.com/bigquery/docs/geospatial-data#loading_geospatial_data).  
`INT64` | `10`  
`INTERVAL` | `"0-13 370 48:61:61"`  
`STRING` | `"string_val"`  
`TIMESTAMP` | `"2022-07-01T12:00:00.00Z"`  
Use the JavaScript `Date.toJSON` method to format the value.  
  
### Structured data

If your JSON messages follow a consistent schema, you can represent JSON objects by using the [`STRUCT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type) data type in BigQuery.

In the following example, the `answers` field is a JSON object with two subfields, `a` and `b`:
    
    
    {"name":"Emily","answers":{"a":"yes","b":"no"}}
    

The following SQL statement creates a BigQuery table with a compatible schema:
    
    
    CREATE TABLE my_dataset.kafka_events (name STRING, answers STRUCT<a STRING, b STRING>);
    

The resulting table looks like the following:
    
    
    +-------+----------------------+
    | name  |       answers        |
    +-------+----------------------+
    | Emily | {"a":"yes","b":"no"} |
    +-------+----------------------+
    

### Semi-structured data

If your JSON messages don't follow a strict schema, consider storing them in BigQuery as a [`JSON`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#json_type) data type. By storing JSON data as a `JSON` type, you don't need to define the schema upfront. After data ingestion, you can query the data by using the field access (dot notation) and array access operators in GoogleSQL. For more information, see [Working with JSON data in GoogleSQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json-data).

## Use a UDF to transform the data

This tutorial assumes that the Kafka messages are formatted as JSON, and that the BigQuery table schema matches the JSON data, with no transformations applied to the data.

Optionally, you can provide a JavaScript user-defined function (UDF) that transforms the data before it is written to BigQuery. The UDF can also perform additional processing, such as filtering, removing personal identifiable information (PII), or enriching the data with additional fields.

For more information, see [Create user-defined functions for Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf).

## What's next

  * [Use Dataflow with Managed Service for Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/managed-service-for-apache-kafka)
  * [Learn about BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
