---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-schema-registry/
title: Use Kafka Connect with schema registry \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:26.767174+00:00
---

# Use Kafka Connect with schema registry  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-schema-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Use Kafka Connect with schema registry Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to integrate [Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview) with [schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview), so that connectors can use registered schemas to serialize and deserialize messages.

Before you start this tutorial, complete the steps in [Produce Avro messages with the schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/bigquery-sink-schema-registry). After you complete them, you have the following components that are needed for this tutorial:

  * A schema registry with a registered Avro schema.
  * A Kafka cluster with a topic that contains Avro messages.



## Overview

A _schema_ defines the structure of a message or data payload. A [schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview) provides a centralized location to store schemas. By using a schema registry, you can ensure consistent encoding and decoding of your data as it moves from producers to consumers.

This tutorial demonstrates the following scenario:

  1. A Java producer client writes Apache Avro messages to a Managed Service for Apache Kafka cluster. The Avro message schema is stored in a schema registry.

  2. A [BigQuery Sink](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector) connector reads the incoming messages from Kafka and writes them to BigQuery. The connector automatically creates a BigQuery table that is compatible with the Avro schema.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Managed Kafka API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=managedkafka.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Managed Kafka API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=managedkafka.googleapis.com)

  8. Make sure that you have the following role or roles on the project: **Managed Kafka Cluster Editor** , **Managed Kafka Connect Cluster Editor** , **Managed Kafka Connector Editor** , and **BigQuery Data Owner**

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  9. Complete the steps in [ Produce Avro messages with the schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/bigquery-sink-schema-registry).



## Create a Connect cluster

Perform the following steps to create a Connect cluster. Creating a Connect cluster can take up to 30 minutes.

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click add_box **Create**.

  3. For the **Connect cluster name** , enter a string. Example: `my-connect-cluster`.

  4. For **Primary Kafka cluster** , select the Kafka cluster.

  5. Click **Create**.




While the Connect cluster is being created, the cluster state is `Creating`. When the cluster has finished being created, the state is `Active`.

###  gcloud 

To create a Connect cluster, run the [`gcloud managed-kafka connect-clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/create) command.
    
    
    gcloud managed-kafka connect-clusters create CONNECT_CLUSTER \
      --location=REGION \
      --cpu=12 \
      --memory=12GiB \
      --primary-subnet=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
      --kafka-cluster=KAFKA_CLUSTER \
      --async
    

Replace the following:

  * `CONNECT_CLUSTER`: a name for the Connect cluster
  * `REGION`: the region where you created the Kafka cluster
  * `PROJECT_ID`: your project ID
  * `SUBNET_NAME`: the subnet where you created the Kafka cluster
  * `KAFKA_CLUSTER`: the name of your Kafka cluster



The command runs asynchronously and returns an operation ID:
    
    
    Check operation [projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID] for status.
    

To track the progress of the create operation, use the [`gcloud managed-kafka operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/operations/describe) command:
    
    
    gcloud managed-kafka operations describe OPERATION_ID \
      --location=REGION
    

For more information, see [Monitor the cluster creation operation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#monitor_cluster).

## Grant IAM roles

Grant the **BigQuery Data Editor** Identity and Access Management (IAM) role to the [Managed Kafka service agent](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control#service-agent). This role allows the connector to write to BigQuery.

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select **Include Google-provided role grants**.

  3. Find the row for **Managed Kafka Service Account** and click mode_edit  **Edit principal**.

  4. Click **Add another role** and select the role **BigQuery Data Editor**.

  5. Click **Save**.




For more information about granting roles, see [Grant an IAM role by using the console](https://docs.cloud.google.com/iam/docs/grant-role-console).

###  gcloud 

To grant IAM roles to the service account, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com \
        --role=roles/bigquery.dataEditor
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `PROJECT_NUMBER`: your project number



To find your project number, use the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command.

By default, a Connect cluster has permission to access schema registries in the same project. If you create the Connect cluster in a different project from the schema registry, you must grant the **Managed Kafka Client** (`roles/managedkafka.client`) role on the schema registry's project to the Managed Kafka service agent. For more information, see [Create a Connect cluster in a different project](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#create-a-connect-cluster-in-a-different-project).

## Create a BigQuery dataset

In this step, you create a [dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) to hold the BigQuery table. The BigQuery Sink connector automatically creates the table.

To create a dataset, perform the following steps.

###  Console 

  1. Open the **BigQuery** page.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, select the project where you want to create the dataset.

  3. Expand the more_vert **View actions** option and click **Create dataset**.

  4. On the **Create dataset** page:

     * For **Dataset ID** , enter a name for the dataset.

     * For **Location type** , choose a geographic location for the dataset.




###  gcloud 

To create a new dataset, use the [`bq mk`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#mk-dataset) command with the `--dataset` flag.
    
    
    bq mk --location REGION \
      --dataset PROJECT_ID:DATASET_NAME
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `DATASET_NAME`: the name of the dataset
  * `REGION`: the dataset's [location](https://docs.cloud.google.com/bigquery/docs/locations)



## Create a BigQuery Sink connector

In this step, you create a [BigQuery Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector), which reads from Kafka and writes to BigQuery. You configure the connector to deserialize the Kafka messages by using the Avro schema stored in your schema registry.

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the name of the Connect cluster.

  3. Click add_box **Create connector**.

  4. For the **Connector name** , enter a string. Example: `bigquery-connector`.

  5. In the **Connector plugin** list, select `BigQuery Sink`.

  6. For **Topics** , select the Kafka topic named `newUsers`. This topic is created by the [Java producer client](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-avro#create_a_producer_client).

  7. For **Dataset** , enter the name of the BigQuery dataset, in the following format: `PROJECT_ID.DATASET_NAME`. Example: `my-project.dataset1`.

  8. In the **Configurations** edit box, replace the existing configuration with the following:
         
         tasks.max=3
         key.converter=org.apache.kafka.connect.storage.StringConverter
         value.converter=io.confluent.connect.avro.AvroConverter
         value.converter.bearer.auth.credentials.source=GCP
         value.converter.schema.registry.url=https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/REGISTRY_REGION/schemaRegistries/REGISTRY_NAME
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `REGISTRY_REGION`: the region where you created your schema registry
     * `REGISTRY_NAME`: the name of your schema registry
  9. Click **Create**.




###  gcloud 

To create a BigQuery Sink connector, run the [`gcloud managed-kafka connectors create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create) command.
    
    
    export REGISTRY_PATH=projects/PROJECT_ID/locations/REGISTRY_REGION/schemaRegistries/REGISTRY_NAME
    
    gcloud managed-kafka connectors create CONNECTOR_NAME \
      --location=REGION \
      --connect-cluster=CONNECT_CLUSTER \
      --configs=connector.class=com.wepay.kafka.connect.bigquery.BigQuerySinkConnector,\
    key.converter=org.apache.kafka.connect.storage.StringConverter,\
    value.converter=io.confluent.connect.avro.AvroConverter,\
    value.converter.bearer.auth.credentials.source=GCP,\
    value.converter.schema.registry.url=https://managedkafka.googleapis.com/v1/$REGISTRY_PATH,\
    tasks.max=3,\
    project=PROJECT_ID,\
    defaultDataset=DATASET_NAME,\
    topics=newUsers
    

Replace the following:

  * `REGISTRY_REGION`: the region where you created your schema registry
  * `REGISTRY_NAME`: the name of your schema registry
  * `CONNECTOR_NAME`: a name for the connector, such as `bigquery-connector`
  * `CONNECT_CLUSTER`: the name of your Connect cluster
  * `REGION`: the region where you created the Connect cluster
  * `PROJECT_ID`: your project ID
  * `DATASET_NAME`: the name of your BigQuery dataset



## View results

To view the results in BigQuery, run a query on the table as follows. It might take a few minutes for the first messages to be written to the table.

### Console

  1. Open the **BigQuery** page.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  2. In the query editor, run the following query:
         
         SELECT * FROM `PROJECT_ID.DATASET_NAME.newUsers`
         

Replace the following variables:

     * `PROJECT_ID`: the name of your Google Cloud project
     * `DATASET_NAME`: the name of your BigQuery dataset



###  gcloud 

Use the [`bq query`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_query) command to run a query on the table:
    
    
    bq query --use_legacy_sql=false 'SELECT * FROM `PROJECT_ID.DATASET_NAME.newUsers`'
    

Replace the following variables:

  * `PROJECT_ID`: the name of your Google Cloud project
  * `DATASET_NAME`: the name of your BigQuery dataset



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Console

  1. Delete the Connect cluster.

     1. Go to the **Managed Service for Apache Kafka** > **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

     2. Select the Connect cluster and click **Delete**.

  2. Delete the Kafka cluster.

     1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

     2. Select the Kafka cluster and click **Delete**.

  3. Delete the BigQuery table and dataset.

     1. Go to the **BigQuery** page.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

     2. In the **Explorer** pane, expand your project and select a dataset.

     3. Expand the more_vert **Actions** option and click **Delete**.

     4. In the **Delete dataset** dialog, type `delete` into the field, and then click **Delete**.




###  gcloud 

  1. To delete the Connect cluster, use the [`gcloud managed-kafka connect-clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/delete) command.
         
         gcloud managed-kafka connect-clusters delete CONNECT_CLUSTER \
           --location=REGION --async
         

  2. To delete the Kafka cluster, use the [`gcloud managed-kafka clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/delete) command.
         
         gcloud managed-kafka clusters delete KAFKA_CLUSTER \
           --location=REGION --async
         

  3. To delete both the BigQuery dataset and the BigQuery table, use the [`bq rm`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_rm) command.
         
         bq rm --recursive --dataset PROJECT_ID:DATASET_NAME
         




## What's next

  * [Troubleshoot a BigQuery sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-bq-connector-config).
  * Learn more about [BigQuery sink connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector).
  * Learn more about [Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
