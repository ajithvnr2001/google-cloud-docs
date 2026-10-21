---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-synthetic-data/
title: Quickstart: Generate synthetic data for Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:08.900753+00:00
---

# Quickstart: Generate synthetic data for Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-synthetic-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Generate synthetic data for a Managed Service for Apache Kafka cluster

Learn how to generate synthetic test data for a Google Cloud Managed Service for Apache Kafka cluster using the Google Cloud console.

This guide uses the Dataflow Streaming Data Generator template to automatically publish sample game telemetry data to a Managed Service for Apache Kafka topic. The Streaming Data Generator is a Dataflow template that generates synthetic test records based on a specified schema at a configurable rate. Generating synthetic data lets you observe cluster activity, test load handling, and verify monitoring metrics without installing a local Kafka client or writing custom producer code. For more information about the template, see [Dataflow Streaming Data Generator template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/streaming-data-generator).

## Before you begin

Before you start this tutorial, create a new Managed Service for Apache Kafka cluster. If you already have a cluster, you can skip this step. For information about the required roles and permissions to create a cluster, see [Create and view a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-cluster). If you follow that guide, complete only the **Create a cluster** section before returning to this guide.

### How to create a cluster

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click add_box **Create**.
  3. In the **Cluster name** box, enter a name for the cluster.
  4. In the **Region** list, select a location for the cluster.
  5. For **Network configuration** , configure the subnet where the cluster is accessible: 
     1. For **Project** , select your project.
     2. For **Network** , select the VPC network.
     3. For **Subnet** , select the subnet.
     4. Click **Done**.
  6. Click **Create**.



After you click **Create** , the cluster state is `Creating`. When the cluster is ready, the state is `Active`. 

### gcloud

To create a Kafka cluster, run the [`managed-kafka clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create) command. 
    
    
    gcloud managed-kafka clusters create KAFKA_CLUSTER \
    --location=REGION \
    --cpu=3 \
    --memory=3GiB \
    --subnets=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
    --async

Replace the following:

  * `KAFKA_CLUSTER`: a name for the Kafka cluster
  * `REGION`: the location of the cluster
  * `PROJECT_ID`: your project ID
  * `SUBNET_NAME`: the subnet where you want to create the cluster, for example `default`



For information about supported locations, see [ Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations). 

The command runs asynchronously and returns an operation ID:
    
    
    Check operation [projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID] for status.

To track the progress of the create operation, use the [`gcloud managed-kafka operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/operations/describe) command: 
    
    
    gcloud managed-kafka operations describe OPERATION_ID \
      --location=REGION

When the cluster is ready, the output from this command includes the entry `state: ACTIVE`. For more information, see [ Monitor the cluster creation operation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#monitor_cluster). 

### Required roles

To get the permissions that you need to generate synthetic data for a cluster, ask your administrator to grant you the following IAM roles on the project: 

  * [Dataflow Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.developer) (`roles/dataflow.developer`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to generate synthetic data for a cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to generate synthetic data for a cluster:

  * `dataflow.jobs.create`
  * `dataflow.jobs.get`
  * `managedkafka.clusters.get`
  * `managedkafka.topics.get`
  * `managedkafka.topics.create`
  * `managedkafka.topics.publish`
  * `resourcemanager.projects.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To ensure that the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) has the necessary permissions to run the Dataflow job, ask your administrator to grant the following IAM roles to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) on the project: 

**Important:** You must grant these roles to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Dataflow Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker) (`roles/dataflow.worker`)
  * [Managed Kafka Client ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you have the permissions to grant IAM roles, the Google Cloud console prompts you to grant the required roles during the synthetic data generation process. If you don't have permission to grant roles, the console displays a message asking you to request that an administrator grant the required permissions.

## Generate synthetic data

To create and launch the Dataflow job that generates synthetic data for your Kafka topic:

  1. In the Google Cloud console, go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of your cluster, such as `test-cluster`.

  3. Select the **Sources** tab.

  4. On the **Sources** page, in the **Generate Synthetic Data** card, click **Create a Dataflow job**. The **Produce Data** pane opens.

  5. In the **Produce Data** pane, select a topic from the **Kafka topic** drop-down list, such as `test-topic`. If you don't have a topic, create one:

     1. In the **Kafka topic** drop-down list, click **Create topic**. The **Create topic** pane opens.
     2. In the **Topic name** field, enter `test-topic`.
     3. Retain the default values for **Partition count** (`3`) and **Replication factor** (`3`).
     4. Click **Create**.
  6. In the **Output rate (QPS)** field, enter the queries-per-second rate you want the generator to produce, such as `100`. This lets you test how your cluster handles different loads.

  7. If a warning appears stating that your Dataflow service account lacks necessary permissions, click **Grant** to assign the following roles:

     * **Dataflow Worker** (`roles/dataflow.worker`)
     * **Managed Kafka Client** (`roles/managedkafka.client`)
  8. In the **Produce Data** pane, click **Create** to launch the Dataflow job.

A notification appears stating that the Dataflow job was created.

  9. In the notification, click **View job** to open the **Dataflow Job details** page, where you can observe the job graph, status, and execution metrics.




## View cluster metrics

After the Dataflow job starts, observe the synthetic data flowing into your cluster:

  1. On the **Cluster details** page for `test-cluster`, click the **Monitoring** tab.

  2. Review the **Byte rates** and **Top 5 topics by produce throughput** charts to verify that data is actively being produced to your topic.




## View the messages

Verify that synthetic messages are being published to your topic using one of the following methods.

### View in Kafka command-line tools

To consume messages directly from your cluster using Kafka CLI tools on a client VM:

  1. Connect to your client VM using SSH. If you haven't set up a client VM, see [Create a client VM](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart#set_up_a_client_machine).

  2. Obtain your cluster's bootstrap server address from the Google Cloud console and set it as an environment variable on your client VM:

     1. In the Google Cloud console, go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

     2. Click the name of your cluster, such as `test-cluster`.

     3. On the **Cluster details** page, click **Configurations**.

     4. Copy the value listed under **Bootstrap URL**.

  3. On your client VM, set the environment variable:
         
         ```sh
         export BOOTSTRAP="BOOTSTRAP_URL"
         ```
         

Replace `BOOTSTRAP_URL` with your copied bootstrap address.

  4. Run the `kafka-console-consumer.sh` command to read messages:
         
         kafka-console-consumer.sh \
          --bootstrap-server $BOOTSTRAP \
          --topic TOPIC_ID \
          --from-beginning \
          --consumer.config client.properties
         

Replace TOPIC_ID with the topic name, such as `test-topic`.

The console displays the streaming synthetic game data records as they are consumed.

  5. Press `Ctrl`+`C` to stop consuming messages.




### View in BigQuery

To stream data from your Kafka topic into BigQuery and view the records:

  1. Since the synthetic data is raw JSON, you must manually create the destination table in BigQuery before creating your connector. For information on how to create a table, see [Create an empty table with a schema definition](https://docs.cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition). Create a table named `test-topic` in your dataset with the following schema:
         
         [
           {"name": "eventId", "type": "STRING"},
           {"name": "eventTimestamp", "type": "INTEGER"},
           {"name": "ipv4", "type": "STRING"},
           {"name": "ipv6", "type": "STRING"},
           {"name": "country", "type": "STRING"},
           {"name": "username", "type": "STRING"},
           {"name": "quest", "type": "STRING"},
           {"name": "score", "type": "INTEGER"},
           {"name": "completed", "type": "BOOLEAN"}
         ]
         

  2. Create a [BigQuery Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector) in a Connect cluster to stream messages from your topic to your BigQuery table. When configuring the connector, use the following sample properties, replacing `PROJECT_ID` with your project ID:
         
         bigQueryPartitionDecorator=false
         connector.class=com.wepay.kafka.connect.bigquery.BigQuerySinkConnector
         defaultDataset=test_dataset
         key.converter=org.apache.kafka.connect.storage.StringConverter
         project=PROJECT_ID
         tasks.max=3
         topics=test-topic
         value.converter=org.apache.kafka.connect.json.JsonConverter
         value.converter.schemas.enable=false
         

  3. After the connector starts streaming data, go to the **BigQuery** page in the Google Cloud console.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  4. In the **Explorer** panel, expand your project ID and select your dataset, `test_dataset`.

  5. Click the table name, `test-topic`.

  6. Click the **Preview** tab to view the streamed synthetic records. Alternatively, click **Compose new query** and run the following SQL query:
         
         SELECT * FROM `PROJECT_ID.DATASET_ID.TABLE_ID` LIMIT 10;
         

Replace the following:

     * PROJECT_ID: your project ID
     * DATASET_ID: your dataset ID, such as `test_dataset`
     * TABLE_ID: your table ID, such as `test-topic`
  7. Click **Run** to view the sample records in the **Query results** pane.

**Note:** Do not use a `SELECT COUNT(*)` query to verify your records. Because the connector uses the BigQuery Streaming API, data is initially written to a streaming buffer. While the data is immediately visible using `SELECT *`, it can take several minutes for row counts to update.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Dataflow Jobs** page.

[Go to Dataflow Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click the name of the job created for your topic.

  3. Click **Stop**.

  4. Select **Cancel** , and then click **Stop Job**.

  5. Optional: If you no longer need the Kafka cluster, go to the **Managed Service for Apache Kafka Clusters** page, select `test-cluster`, and click **Delete**.




## What's next

  * [Overview of Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)
  * [Monitoring Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster)
  * [Dataflow Streaming Data Generator template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/streaming-data-generator)
  * [Create a BigQuery Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
