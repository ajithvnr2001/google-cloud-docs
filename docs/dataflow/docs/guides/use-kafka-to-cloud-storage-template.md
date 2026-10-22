---
url: https://docs.cloud.google.com/dataflow/docs/guides/use-kafka-to-cloud-storage-template/
title: Write Managed Service for Apache Kafka data to Cloud Storage \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:38.706279+00:00
---

# Write Managed Service for Apache Kafka data to Cloud Storage  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/use-kafka-to-cloud-storage-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Write Managed Service for Apache Kafka data to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

If you need to load data from a Managed Service for Apache Kafka topic to a Cloud Storage bucket, you can do so with a Dataflow template. You can use the Google Cloud console, the REST API, or the Google Cloud CLI.

This document helps you configure the **Kafka to Cloud Storage Dataflow** template using the Google Cloud console.

## Google Cloud products used

The **Kafka to Cloud Storage Dataflow** template uses the following billable Google Cloud products. Use the [Pricing calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

  * **Dataflow** : Dataflow is a fully managed data processing service. The **Kafka to Cloud Storage Dataflow** template utilizes Dataflow to create a pipeline that reads data from your Kafka topic, performs any necessary transformations, and writes it to Cloud Storage. Dataflow's autoscaling and self-healing capabilities ensure your pipeline runs reliably and efficiently.
  * **Cloud Storage** : Serves as the destination for your Kafka data. You'll need a Cloud Storage bucket to store the data transferred by the Dataflow pipeline.



Additionally, the solution also uses Managed Service for Apache Kafka.

  * **Managed Service for Apache Kafka** : A Google Cloud service that helps you run Apache Kafka. Provides the source data for the pipeline. You'll need an existing Managed Service for Apache Kafka cluster and topic with data you want to transfer to Cloud Storage. For more information about Managed Service for Apache Kafka pricing, see [the pricing guide](https://docs.cloud.google.com/managed-service-for-apache-kafka/pricing).



## Before you begin

Before launching your **Kafka to Cloud Storage Dataflow** template, ensure you have completed the following:

  1. Create a Managed Service for Apache Kafka cluster and topic.

One way of creating a cluster and a topic is to follow the [Managed Service for Apache Kafka quickstart](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart).

If your topic contains Avro records, for additional resource requirements, see [Configure the Kafka message format](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-bq#configure-message-format).

  2. Enable the following Google Cloud APIs:

     * Dataflow

     * Cloud Storage
    
    gcloud services enable dataflow.googleapis.com storage-api.googleapis.com \
    

  3. Create a Cloud Storage bucket.

For more information about how to create a Cloud Storage bucket, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).




### Grant the Managed Kafka client role to the Dataflow worker service account

To connect your Dataflow job to Managed Service for Apache Kafka, you'll need to grant specific permissions to the Dataflow worker service account. This service account is the identity used for all worker VMs in your Dataflow job, and any requests made from these VMs utilize this account.

To allow access to your Kafka resources, you must grant the `roles/managedkafka.client` role to the Dataflow worker service account. This role includes the necessary `managedkafka.clusters.connect` permission for establishing connections.

For more information about the worker service account, see [Security and permissions for pipelines on Google Cloud](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#permissions).

To grant the Managed Kafka client role to the Dataflow service account, follow these steps:

### Console

  1. In the Google Cloud console, go to the **IAM** page.  
[Go to IAM](https://console.cloud.google.com/iam-admin/iam)
  2. Check that the project is set to the consumer project that the Managed Service for Apache Kafka client would be accessing.
  3. Click **Grant access**.
  4. In the new page, for **Add Principals** , enter the email address of the Dataflow worker service account that you are using.
  5. For **Assign roles** , select the **Managed Kafka client** role.
  6. Click **Save**.



### gcloud CLI

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member serviceAccount:SERVICE_ACCOUNT_EMAIL \
           --role roles/managedkafka.client

Replace the following:

     * PROJECT_ID is the project ID.

     * SERVICE_ACCOUNT_EMAIL is the email address of the Dataflow worker service account.




## Launch the Kafka to Cloud Storage Dataflow template

You can launch the **Kafka to Cloud Storage Dataflow** template from the cluster details page in the console.

  1. In the Google Cloud console, go to the **Cluster** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

The clusters you created in a project are listed.

  2. To view the cluster details page, click a cluster name. 
  3. In the cluster details page, click **Import data**. 

The **Create a Dataflow job using template "Kafka to Kafka"** page opens.

  4. In the template, for **Dataflow template** , update the template to **Kafka to Cloud Storage**. 



Configure the fields in the template according to the information included in the following sections.

## Enter a job name

For the **Job name** field, enter a name for your Dataflow job.

The name must be unique among all the current running jobs in the project.

## Choose a regional endpoint for your pipeline

For the **Regional endpoint** field, set the regional endpoint to the location of your Kafka cluster to minimize cross-region data transfer fees.

The Dataflow workers can run independent of the region of your Kafka cluster. However, you incur inter-regional egress costs if you launch workers outside the region of your Kafka cluster.

To view the location of the cluster, follow the steps in [List your Managed Service for Apache Kafka clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-clusters#list).

## Configure source

  1. For **Source** , retain the default value of **Managed Service for Apache Kafka**.

  2. For **Kafka cluster** and **Kafka source authentication mode** , retain the default values.

  3. For **Kafka topic** , select a topic from the list of available topics.


**Note:** We recommend that you use **Application Default Credentials** as the Kafka source authentication mode in the template. The authentication options **TLS** and **None** are not supported by Managed Service for Apache Kafka. Use **SASL_PLAIN** authentication only for testing purposes.

### Configure the Kafka message format

The Dataflow template supports the following message formats:

  * **Avro Confluent wire format** : Each Kafka message includes a magic byte, a schema ID, and the Avro binary-encoded record.

For Avro (Confluent wire format) formats, you can utilize either a single schema or multiple schemas:

    * **Single schema** : All messages adhere to a single predefined Avro schema.

    * **Multiple schemas** : Messages can utilize different schemas. This is only supported for the Avro (Confluent wire format).

  * **Avro (binary-encoded):** Messages contain only the payload of the record without any metadata. You must provide an Avro schema file (.avsc) uploaded to Cloud Storage. All messages must adhere to this single schema.

  * **JSON** : Records don't require a predefined schema. Records that don't conform to the schema are sent to the dead-letter queue (if configured) or an error message is logged. The supported format is `{"field": "value"}` format. The format `[{"name": "field", "value": "value"}]`is not supported.




Managed Service for Apache Kafka does not offer a schema registry. The template only supports passing authentication credentials to schema registries that are Confluent-wire format compatible.

#### Avro Confluent wire format

If you choose this option as the **Kafka message format** , configure the following additional settings:

**Schema source** : This field tells the pipeline where to find the schema. Choose one of the following options:

  * **Schema registry** : Your schemas are stored in a Confluent Schema Registry. This is useful for evolving schemas and managing multiple versions. Ensure that the scehma registry is accessible to the Managed Service for Apache Kafka cluster network and is hosted in the same region as your Dataflow workers. You can use a schema registry with both single and multiple schema scenarios. Configure the following additional settings:

    * **Schema registry connection URL** : Provide the URL to connect to your schema registry.

    * **Authentication Mode** : If your registry requires authentication, select **OAuth** or **TLS**. Else, select **None**.

  * **Single schema file** : Choose this option if all your messages follow a single, fixed schema defined in a file.

    * **Cloud storage file to the Avro schema file** : The path to the Avro schema file used to decode all of the messages in a topic.



#### Avro binary encoding

If you choose this option as the **Kafka message format** , configure the following additional settings:

  * **Cloud storage file to the Avro schema file** : The path to the Avro schema file used to decode all of the messages in a topic.



#### JSON

If you choose this option as the **Kafka message format** , no other configurations are required.

### Specify the Kafka offset

  1. To avoid reprocessing messages when individual workers or the entire pipeline need to be restarted, select the **Commit offsets to Kafka** option. This ensures that your pipeline resumes processing from where it left off, preventing duplicate processing and potential data inconsistencies.

  2. For the **Enter Consumer Group ID** field, enter a unique name for this pipeline's group. In most circumstances, you want the pipeline to read each message once and be restartable.

  3. For the **Default Kafka start offset** field, the Dataflow pipeline offers two starting offset options. Select one of the following:

     * **Earliest** : Processes messages from the beginning of the Kafka topic.

     * **Latest** : Processes messages starting from the latest available offset.




## Configure destination

These options control how your data pipeline writes data to Cloud Storage.

  1. For **Destination** , enter the bucket path and include the filename prefix for your output files. The file prefix must end with a slash. For example, `gs://test-bucket/test-prefix/`

  2. For **Window duration** , enter the time window for writing data to Cloud Storage. Choose the appropriate format (`Ns` for seconds, `Nm` for minutes, `Nh` for hours) based on your data processing requirements.

  3. For **Output filename prefix of the files to write** , you can provide a prefix to be added to each output file for better organization and identification.

  4. For **Maximum output shards** , set the number to zero. You can specify the number of shards to be produced when writing files. Increasing the number can achieve higher throughput, but it also leads to increased costs due to higher shuffle costs. The service selects an optimal number when you set the number to zero.




## Configure dead letter queue

Sometimes messages can't be processed due to corruption, incompatible data types, or schema mismatches.

To handle these cases, enable the dead-letter queue in the template and provide a table name. The template creates the table using a standardized schema.

## Configure encryption

By default, all data at rest and in-transit are encrypted by a Google-owned and Google-managed encryption key. If you have customer-managed encryption keys (CMEK), you can select your own keys. For more information about how to configure a CMEK, see [Configure message encryption](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption).

## Configure networking

You must specify the cluster's network and subnetwork in the Dataflow template. The template's **Optional parameters** section lets you define the network for your Dataflow workers.

The **Kafka to Cloud Storage Dataflow** template provisions Dataflow workers in your project's default network, by default. To let your Managed Service for Apache Kafka cluster send data to Cloud Storage through Dataflow, ensure that your Dataflow workers can access your cluster's network.

We recommend that if your Kafka cluster is not connected to a subnet in the project's default network, use your project's default network for your Kafka cluster.

For more information on setting up networking with your Dataflow pipeline, see the following:

  * [Guidelines for specifying a network parameter](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks#network_parameter).

  * [Read from Kafka](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka#networking).




If you encounter challenges configuring your Dataflow networking, see the [Dataflow networking troubleshooting guide](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-networking).

## Configure optional Dataflow parameters

Configure the optional parameters only if you know the impact of the configuration on the Dataflow workers. Incorrect settings can affect performance or cost. For detailed explanations of each option, see [Optional parameters](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-gcs#optional-parameters).

## Monitoring

The Dataflow template for **Kafka to Cloud Storage** provides a monitoring experience that lets you explore logs, metrics, and errors within the console. This monitoring suite of tools is available as part of the Dataflow user interface.

The **Job Metrics** tab lets you create custom dashboards. For the **Kafka to Cloud Storage** Dataflow template, we recommend setting up a **Job Metrics** dashboard that monitors the following:

  * **Throughput** : The volume of data processed at any point in time. This is useful for monitoring data flow through your job and identifying potential performance issues.

For more information, see [Dataflow throughput monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#throughput).

  * **Data freshness** : The difference in seconds between the timestamp on the data element and the time the event is processed in your pipeline. This helps identify performance and data source bottlenecks or frequent retries.

For more information, see [Dataflow data freshness monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#data_freshness_streaming).

  * **Backlog** : The amount of bytes waiting to be processed. This information informs [autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#heuristics) decisions.




For more information about Dataflow monitoring, see the [Dataflow monitoring documentation](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview).

## Troubleshooting

If you encounter performance issues with your Dataflow pipeline, Dataflow provides a comprehensive set of troubleshooting and diagnostic tools.

Here are two common scenarios and their respective troubleshooting guides:

  * [Troubleshoot slow or stuck streaming pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs).

  * [Troubleshooting stragglers in pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-streaming-stragglers).




For a general overview of debugging Dataflow pipelines, see [Troubleshoot and debug Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline).

## Known limitations

  * The template does not support passing credentials for authentication to your Schema Registry.

  * When you create the **Kafka to Cloud Storage** Dataflow job, ensure that the Google Cloud project is set to the same project that contains the Managed Service for Apache Kafka cluster.




## What's next

  * [Apache Kafka to Cloud Storage template parameters](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-gcs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
