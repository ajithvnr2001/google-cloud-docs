---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/mysql-change-data-capture-to-bigquery/
title: Change Data Capture from MySQL to BigQuery using Debezium and Pub/Sub (Stream) template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:20.655831+00:00
---

# Change Data Capture from MySQL to BigQuery using Debezium and Pub/Sub (Stream) template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/mysql-change-data-capture-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Change Data Capture from MySQL to BigQuery using Debezium and Pub/Sub (Stream) template Stay organized with collections  Save and categorize content based on your preferences. 

The Change Data Capture from MySQL to BigQuery using Debezium and Pub/Sub template is a streaming pipeline that reads Pub/Sub messages with change data from a MySQL database and writes the records to BigQuery. A Debezium connector captures changes to the MySQL database and publishes the changed data to Pub/Sub. The template then reads the Pub/Sub messages and writes them to BigQuery.

You can use this template to sync MySQL databases and BigQuery tables. The pipeline writes the changed data to a BigQuery staging table and intermittently updates a BigQuery table replicating the MySQL database.

## Pipeline requirements

  * The Debezium connector must be [deployed](https://github.com/GoogleCloudPlatform/DataflowTemplates/tree/master/v2/cdc-parent#deploying-the-connector).
  * The Pub/Sub messages must be serialized in a [Beam Row](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/values/Row.html).



## Template parameters

### Required parameters

  * **inputSubscriptions** : The comma-separated list of Pub/Sub input subscriptions to read from, in the format `<SUBSCRIPTION_NAME>,<SUBSCRIPTION_NAME>, ...`.
  * **changeLogDataset** : The BigQuery dataset to store the staging tables in, in the format <DATASET_NAME>.
  * **replicaDataset** : The location of the BigQuery dataset to store the replica tables in, in the format <DATASET_NAME>.



### Optional parameters

  * **inputTopics** : Comma-separated list of PubSub topics to where CDC data is being pushed.
  * **updateFrequencySecs** : The interval at which the pipeline updates the BigQuery table replicating the MySQL database.
  * **useSingleTopic** : Set this to `true` if you configure your Debezium connector to publish all table updates to a single topic. Defaults to: false.
  * **useStorageWriteApi** : If true, the pipeline uses the BigQuery Storage Write API (<https://cloud.google.com/bigquery/docs/write-api>). The default value is `false`. For more information, see Using the Storage Write API (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#storage-write-api>).
  * **useStorageWriteApiAtLeastOnce** : When using the Storage Write API, specifies the write semantics. To use at-least once semantics (<https://beam.apache.org/documentation/io/built-in/google-bigquery/#at-least-once-semantics>), set this parameter to `true`. To use exactly-once semantics, set the parameter to `false`. This parameter applies only when `useStorageWriteApi` is `true`. The default value is `false`.
  * **numStorageWriteApiStreams** : When using the Storage Write API, specifies the number of write streams. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter. Defaults to: 0.
  * **storageWriteApiTriggeringFrequencySec** : When using the Storage Write API, specifies the triggering frequency, in seconds. If `useStorageWriteApi` is `true` and `useStorageWriteApiAtLeastOnce` is `false`, then you must set this parameter.



## Run the template

To run this template, perform the following steps:

  1. On your local machine, clone the [DataflowTemplates repository](https://github.com/GoogleCloudPlatform/DataflowTemplates).
  2. Change to the `v2/cdc-parent` directory.
  3. Ensure that the Debezium connector is [deployed](https://github.com/GoogleCloudPlatform/DataflowTemplates/tree/master/v2/cdc-parent#deploying-the-connector). 
  4. Using Maven, run the Dataflow template: 
         
         mvn exec:java -pl cdc-change-applier -Dexec.args="--runner=DataflowRunner \
             --inputSubscriptions=SUBSCRIPTIONS \
             --updateFrequencySecs=300 \
             --changeLogDataset=CHANGELOG_DATASET \
             --replicaDataset=REPLICA_DATASET \
             --project=PROJECT_ID \
             --region=REGION_NAME"
           

Replace the following:

     * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
     * `SUBSCRIPTIONS`: your comma-separated list of Pub/Sub subscription names
     * `CHANGELOG_DATASET`: your BigQuery dataset for changelog data
     * `REPLICA_DATASET`: your BigQuery dataset for replica tables



## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
