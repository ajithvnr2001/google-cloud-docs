---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-cloud-storage/
title: Back up Kafka messages to Cloud Storage \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:42.143794+00:00
---

# Back up Kafka messages to Cloud Storage  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Back up Kafka messages to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to write messages from your Managed Service for Apache Kafka cluster to Cloud Storage using Kafka Connect.

Kafka Connect manages data movement between your Kafka cluster and other systems. In this tutorial, you create a [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) and a [Cloud Storage Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector). The Cloud Storage Sink connector reads messages from Kafka and writes them to a Cloud Storage bucket.

## Before you begin

###  Console 

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

  8. Make sure that you have the following role or roles on the project: **Managed Kafka Cluster Editor** , **Managed Kafka Connect Cluster Editor** , **Managed Kafka Connector Editor** , **Managed Kafka Topic Editor** , **Storage Admin**

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



###  gcloud 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Managed Kafka API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable managedkafka.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Managed Kafka API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable managedkafka.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: ` roles/managedkafka.clusterEditor, roles/managedkafka.connectClusterEditor, roles/managedkafka.connectorEditor, roles/managedkafka.topicEditor, roles/storage.admin `
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Create a Cloud Storage bucket

In this step, you create a Cloud Storage bucket. This bucket stores the data that the Cloud Storage Sink connector reads from Kafka.

### Console

  1. Go to the **Cloud Storage** > **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.

  3. On the **Create a bucket** page, enter a name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). Cloud Storage bucket names must be globally unique.

  4. Click **Create**.




###  gcloud 

To create a Cloud Storage bucket, run the [`gcloud storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) command.
    
    
    gcloud storage buckets create gs://BUCKET_NAME --location=BUCKET_LOCATION
    

Replace the following:

  * BUCKET_NAME: a name for your Cloud Storage bucket that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). Cloud Storage bucket names must be globally unique.

  * BUCKET_LOCATION: the [location](https://docs.cloud.google.com/storage/docs/locations#available-locations) for the bucket. For example, `US`.




## Create Managed Service for Apache Kafka resources

In this section, you create the following Managed Service for Apache Kafka resources:

  * A Kafka cluster with a topic.
  * A Connect cluster with connectors a Cloud Storage Sink connector.



### Create a Kafka cluster

In this step, you create a [Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster). Creating a cluster can take up to 30 minutes.

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

### Create a Kafka topic

After the Managed Service for Apache Kafka cluster is created, create a Kafka topic.

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. In the cluster details page, click add_box **Create Topic**.

  4. In the **Topic name** box, enter a name for the topic.

  5. Click **Create**.




###  gcloud 

To create a Kafka topic, run the [`managed-kafka topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create) command.
    
    
    gcloud managed-kafka topics create KAFKA_TOPIC_NAME \
    --cluster=KAFKA_CLUSTER \
    --location=REGION \
    --partitions=10 \
    --replication-factor=3
    

Replace the following:

  * `KAFKA_TOPIC_NAME`: the name of the Kafka topic to create
  * `KAFKA_CLUSTER`: the name of the Kafka cluster
  * `REGION`: the region where you created the Kafka cluster



### Create a Connect cluster

In this step, you create a Connect cluster. Creating a Connect cluster can take up to 30 minutes.

Before you start this step, make sure the Managed Service for Apache Kafka cluster is fully created.

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click add_box **Create**.

  3. For the **Connect cluster name** , enter a string. Example: `my-connect-cluster`.

  4. For **Primary Kafka cluster** , select the Kafka that you created earlier.

  5. Click **Create**.




While the cluster is being created, the cluster state is `Creating`. When the cluster has finished being created, the state is `Active`.

###  gcloud 

To create a Connect cluster, run the [`gcloud managed-kafka connect-clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/connect-clusters/create) command.
    
    
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

### Grant IAM roles

Grant the **Storage Object Creator** Identity and Access Management (IAM) role to the Managed Kafka service account. This role allows the connector to write files to Cloud Storage.

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select **Include Google-provided role grants**.

  3. Find the row for **Managed Kafka Service Account** and click mode_edit  **Edit principal**.

  4. Click **Add another role** and select the **Storage Object Creator** role.

  5. Click **Save**.




For more information about granting roles, see [Grant an IAM role by using the console](https://docs.cloud.google.com/iam/docs/grant-role-console).

###  gcloud 

To grant an IAM role to the service account, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com \
        --role=roles/storage.objectCreator
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `PROJECT_NUMBER`: your project number



To find your project number, use the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command.

### Create a Cloud Storage Sink connector

In this step, you create a [Cloud Storage Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector). This connector reads messages from one or more Kafka topics and writes them to Cloud Storage.

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the name of the Connect cluster.

  3. Click add_box **Create connector**.

  4. For the **Connector name** , enter a string. Example: `pubsub-source`.

  5. In the **Connector plugin** list, select `Cloud Storage Source`.

  6. For **Topics** , select Kafka topic that you created previously and click **OK**.

  7. For **GCS Bucket** , click **Browse**.

  8. Select the Cloud Storage bucket that you created previously and click **Select**.

  9. Click **Create**.




###  gcloud 

To create a Cloud Storage Sink connector, run the [`gcloud managed-kafka connectors create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create) command.
    
    
    gcloud managed-kafka connectors create STORAGE_CONNECTOR_NAME \
      --location=REGION \
      --connect-cluster=CONNECT_CLUSTER \
      --configs=connector.class=io.aiven.kafka.connect.gcs.GcsSinkConnector,\
    file.name.prefix=,\
    format.output.type=json,\
    gcs.bucket.name=BUCKET_NAME,\
    gcs.credentials.default=true,\
    key.converter=org.apache.kafka.connect.storage.StringConverter,\
    tasks.max=3,\
    topics=KAFKA_TOPIC_NAME,\
    value.converter=org.apache.kafka.connect.json.JsonConverter,\
    value.converter.schemas.enable=false
    

Replace the following:

  * `STORAGE_CONNECTOR_NAME`: a name for the connector, such as `storage-sink-connector`
  * `CONNECT_CLUSTER`: the name of your Connect cluster
  * `REGION`: the region where you created the Connect cluster
  * `PROJECT_ID`: your project ID
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `KAFKA_TOPIC_NAME`: the name of your Kafka topic



## View results

To view the results, send messages to the Kafka topic. There are various ways to send messages to Managed Service for Apache Kafka, including:

  * [Use the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart).
  * [Use a Java producer](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-java).
  * [Use a Python producer](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-python)
  * [Stream messages from Pub/Sub by using Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-pubsub-to-gcs)



The Cloud Storage Sink connector reads the Kafka messages and writes them to files in Cloud Storage. It might take a few minutes for the first file to be written.

To view the output files, perform the following steps.

### Console

  1. Go to the **Cloud Storage** > **Buckets** page.



[Go to Buckets](https://console.cloud.google.com/storage/browser)

  1. In the list of buckets, click the name of the bucket that you created earlier.

  2. If the Cloud Storage Sink connector successfully wrote files, they are listed in the **Bucket details** page. Select one of more files.

  3. Click **Download** to download the selected files.




###  gcloud 

To list the output files, run the [`gcloud storage ls`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls) command:
    
    
    gcloud storage ls gs://BUCKET_NAME
    

To download the files, run the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command.
    
    
    gcloud storage cp --recursive gs://BUCKET_NAME .
    

Replace BUCKET_NAME with the name of your Cloud Storage bucket.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Console

  1. Delete the Cloud Storage bucket.

     1. Go to the **Cloud Storage** > **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage)

     2. Select the bucket and click **Delete**.

  2. Delete the Connect cluster.

     1. Go to the **Managed Service for Apache Kafka** > **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

     2. Select the Connect cluster and click **Delete**.

  3. Delete the Kafka cluster.

     1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

     2. Select the Kafka cluster and click **Delete**.




###  gcloud 

  1. To delete the Cloud Storage bucket and its objects, use the [`gcloud storage rm`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) command.
         
         gcloud storage rm gs://BUCKET_NAME --recursive
         

  2. To delete the Connect cluster, use the [`gcloud managed-kafka connect-clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/delete) command.
         
         gcloud managed-kafka connect-clusters delete CONNECT_CLUSTER \
           --location=REGION --async
         

  3. To delete the Kafka cluster, use the [`gcloud managed-kafka clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/delete) command.
         
         gcloud managed-kafka clusters delete KAFKA_CLUSTER \
           --location=REGION --async
         




## What's next

  * [Troubleshoot a Cloud Storage Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-cloud-storage-connector).
  * Learn more about the [Cloud Storage Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector).
  * Learn more about [Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
