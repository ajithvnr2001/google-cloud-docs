---
url: https://docs.cloud.google.com/dataflow/docs/guides/use-kafka-to-kafka-template/
title: Replicate Kafka data to Managed Service for Apache Kafka \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:13.022180+00:00
---

# Replicate Kafka data to Managed Service for Apache Kafka  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/use-kafka-to-kafka-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Replicate Kafka data to Managed Service for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

If you need to move data from an open source Apache Kafka topic to Managed Service for Apache Kafka, you can do so with a Dataflow template. You can use the Google Cloud console, the REST API, or the Google Cloud CLI. The messages in the Kafka topic must be published using AVRO or JSON schema and encoding.

This document helps you configure the **Kafka to Kafka Dataflow** template using the Google Cloud console.

## Google Cloud products used

The **Kafka to Kafka Dataflow template** uses the following billable Google Cloud products. Use the [Pricing calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

  * **Dataflow** : Dataflow is a fully managed data processing service. The **Kafka to Kafka Dataflow** template utilizes Dataflow to create a pipeline that reads data from your external Kafka topic and writes it to a Managed Service for Apache Kafka topic. Dataflow's autoscaling and self-healing capabilities ensure your pipeline runs reliably and efficiently.
  * **Cloud Storage** : Cloud Storage provides object storage. It is used only if you use TLS authentication for your external Kafka source. You store your Keystore and Truststore files containing TLS certificates in Cloud Storage, and the Dataflow pipeline accesses them from Cloud Storage.
  * **Secret Manager** : Secret Manager is a secrets and credential management service.The product is used only if you choose TLS or SASL_PLAIN authentication for your external Kafka source. It stores your authentication credentials such as usernames, passwords, and certificates. These credentials are used to connect to the external Kafka cluster securely.



Additionally, the solution also uses Managed Service for Apache Kafka.

  * **Managed Service for Apache Kafka** : A Google Cloud service that helps you run Apache Kafka. In this solution, Managed Service for Apache Kafka is used as the destination for your data. You stream data from an external Kafka topic into a topic within your Managed Service for Apache Kafka cluster. For more information about Managed Service for Apache Kafka pricing, see [the pricing guide](https://docs.cloud.google.com/managed-service-for-apache-kafka/pricing).



## Before you begin

Before launching your **Kafka to Kafka Dataflow** template, ensure you have completed the following:

  1. Create a Managed Service for Apache Kafka cluster and topic.

One way of creating a cluster and a topic is to follow the [Managed Service for Apache Kafka quickstart](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart).

If your topic contains Avro records, for additional resource requirements, see [Configure the Kafka message format](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-bq#configure-message-format).

  2. Enable the following Google Cloud APIs:

     * Dataflow

     * Secret Manager (Only if you use SASL_PLAIN or TLS authentication for your external Kafka source)

     * Cloud Storage (Only if you use TLS authentication for your external Kafka source)
    
    gcloud services enable dataflow.googleapis.com \
    secretmanager.googleapis.com storage.googleapis.com
    




### Prepare the SASL_PLAIN authentication resources

Follow the instructions in this section if you are planning to use your SASL_PLAIN authentication credentials for your external Kafka source.

  1. In the Google Cloud console, navigate to Secret Manager.

[Go to Secret Manager ](https://console.cloud.google.com/security/secret-manager)

  2. Create two secrets: one for your Kafka username and one for your Kafka password.

For each secret, provide a descriptive name such as "kafka-username" and "kafka-password".




For more information about how to create a secret, including the required roles and permissions, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

### Prepare the TLS authentication resources

Follow the instructions in this section if you are planning to use your TLS authentication credentials for your external Kafka source.

  1. In the Google Cloud console, navigate to Secret Manager.

[Go to Secret Manager ](https://console.cloud.google.com/security/secret-manager)

  2. Ensure your Keystore file (JKS format) contains the TLS certificate and private key required to authenticate your client with the Kafka cluster.

  3. Ensure your Truststore file (JKS format) contains the trusted certificates required to verify the identity of the Kafka broker.

  4. Upload your Keystore and Truststore files to Cloud Storage.

For more information about how to upload files to Cloud Storage, see [Upload objects from a file system](https://docs.cloud.google.com/storage/docs/uploading-objects).

  5. Create three secrets for your TLS configuration:

     * Truststore password: Stores the password used to access your Truststore file.

     * Keystore password: Stores the password used to access your Keystore file.

     * Private key password: Stores the password used to access the private key within your Keystore file.

For each secret, provide a descriptive name.




For more information about how to create a secret, including the required roles and permissions, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

### Grant the Managed Kafka client role to the Dataflow worker service account

To connect your Dataflow job to Managed Service for Apache Kafka, you'll need to grant specific permissions to the Dataflow worker service account. This service account is the identity used for all worker VMs in your Dataflow job, and any requests made from these VMs utilize this account.

To allow access to your Kafka resources, you must grant the `roles/managedkafka.client` role on the Dataflow worker service account. This role includes the necessary `managedkafka.clusters.connect` permission for establishing connections.

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




## Launch the Kafka to Kafka Dataflow template

You can launch the **Kafka to Kafka Dataflow** template from the cluster details page in the console.

  1. In the Google Cloud console, go to the **Cluster** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

The clusters you created in a project are listed.

  2. To view the cluster details page, click a cluster name. 
  3. In the cluster details page, click **Import data**. 

The **Create a Dataflow job using template "Kafka to Kafka"** page opens.




Configure the fields in the template according to the information included in the following sections.

## Enter a job name

For the **Job name** field, enter a name for your Dataflow job.

The name must be unique among all the current running jobs in the project.

## Choose a regional endpoint for your pipeline

For the **Regional endpoint** field, set the regional endpoint to the location of your Kafka cluster to minimize cross-region data transfer fees.

The Dataflow workers can run independent of the region of your Kafka cluster. However, you incur inter-regional egress costs if you launch workers outside the region of your Kafka cluster.

To view the location of the cluster, follow the steps in [List your Managed Service for Apache Kafka clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-clusters#list).

## Configure source

  1. For **Source** , select **Self-managed or External Kafka**.

  2. For **Kafka bootstrap server** , enter the address of the external Kafka cluster bootstrap server.

  3. For **Source Kafka Bootstrap server and topic** , enter the external Kafka bootstrap server and topic address.

  4. For **Kafka source authentication mode** , select your authentication mode from the provided choices. For external Kafka, you have three options:

     * **SASL_PLAIN**

     * **TLS**

     * **None**




### For SASL_PLAIN Kafka source authentication

Before proceeding with this section, see Prepare the SASL_PLAIN authentication resources.

If you select SASL_PLAIN as the Kafka source authentication, fill in the following additional fields.

  1. For **Secret version ID for Kafka SASL/PLAIN username** , enter the version ID for the username.

  2. For **Secret version ID for Kafka SASL/PLAIN password** , enter the version ID for the password.




### For TLS Kafka source authentication

Before proceeding with this section, see Prepare the TLS authentication resources.

If you select TLS as the Kafka source authentication, fill in the following additional fields.

  1. For **Location of keystore** , enter the Cloud Storage path to your Java Keystore (JKS) file. This file contains the TLS certificate and private key needed to authenticate your pipeline with the Kafka cluster. For example: gs://your-bucket/keystore.jks

  2. For **Truststore file location** field, enter the Cloud Storage path to your Java Truststore (JKS) file. This file contains the trusted certificates used to verify the identity of the Kafka broker.

  3. For **Secret Version ID for Truststore password** , provide the Secret Manager secret ID that stores the password to access your Truststore JKS file.

  4. For **Secret Version ID of Keystore password** , provide the Secret Manager secret ID that stores the password to access your JKS file.

  5. For the **Secret Version ID of private key password** field, if your private key within the Keystore has a separate password, enter the Secret Manager secret ID containing that password.




### Commit offsets to Kafka

This setting controls how the pipeline keeps track of which messages from the external Kafka source is processed. Enabling this setting helps ensure that your pipeline processes messages reliably and avoids errors when restarting.

Kafka keeps track of messages using offsets. Think of these as bookmarks, remembering the pipeline's place in each message stream. When you enable the setting, the pipeline regularly saves its bookmarks in Kafka. If the pipeline restarts due to an error, update, or planned maintenance, it can use the saved bookmarks to pick up right where it left off. This prevents it from missing messages or accidentally processing the same message twice.

  1. Enable **Commit offsets to Kafka**.

  2. Provide a **Consumer group ID**. This is a name that identifies your pipeline to Kafka.

  3. For **Default Kafka start offset** , choose one of the following:

     * **Earliest** : Processes messages from the beginning of the Kafka topic.

     * **Latest** : Processes messages starting from the newest message.




## Configure destination

  1. For destination, choose **Managed Service for Apache Kafka**.

  2. For **Kafka cluster** , choose a cluster that you already created.

  3. You can choose an existing topic or create a new one.

  4. For **Kafka destination autheticaton method** , select **Application Default Credentials**.




## Configure encryption

By default, all data at rest and in-transit are encrypted by a Google-owned and Google-managed encryption key. If you have customer-managed encryption keys (CMEK), you can select your own keys. For more information about how to configure a CMEK, see [Configure message encryption](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption).

## Configure networking

You must specify the cluster's network and subnetwork in the Dataflow template. The template's **Optional parameters** section lets you define the network for your Dataflow workers.

The **Kafka to Kafka Dataflow** template provisions Dataflow workers in your project's default network, by default. To let your external Kafka cluster send data to Managed Service for Apache Kafka through Dataflow, ensure that your Dataflow workers can access your cluster's network.

We recommend that if your Kafka cluster is not connected to a subnet in the project's default network, use your project's default network for your Kafka cluster.

For more information on setting up networking with your Dataflow pipeline, see the following:

  * [Guidelines for specifying a network parameter](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks#network_parameter).

  * [Read from Kafka](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka#networking).




If you encounter challenges configuring your Dataflow networking, see the [Dataflow networking troubleshooting guide](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-networking).

## Configure optional Dataflow parameters

Configure the optional Dataflow parameters only if you know the impact of the configuration on the Dataflow workers. Incorrect settings can affect performance or cost. For detailed explanations of each option, see [Optional parameters](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-kafka#optional-parameters).

## Monitoring

The Dataflow template for Kafka to Managed Service for Apache Kafka provides a monitoring experience that lets you explore logs, metrics, and errors within the console. This monitoring suite of tools is available as part of the Dataflow user interface.

The **Job Metrics** tab lets you create custom dashboards. For the Kafka to Managed Service for Apache Kafka template, we recommend setting up a Job Metrics dashboard that monitors the following:

  * **Throughput** : The volume of data processed at any point in time. This is useful for monitoring data flow through your job and identifying potential performance issues.

For more information, see [Dataflow throughput monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#throughput).

  * **Data freshness** : The difference in seconds between the timestamp on the data element and the time the event is processed in your pipeline. This helps identify performance and data source bottlenecks or frequent retries.

For more information, see the following: [Dataflow freshness monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#data_freshness_streaming).

  * **Backlog** : The amount of bytes waiting to be processed. This information informs [autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#heuristics) decisions.




For more information about Dataflow monitoring, see the [Dataflow monitoring documentation](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview).

## Troubleshooting

If you encounter performance issues with your Dataflow pipeline, Dataflow provides a comprehensive set of troubleshooting and diagnostic tools.

Here are two common scenarios and their respective troubleshooting guides:

  * [Troubleshoot slow or stuck streaming pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs).

  * [Troubleshooting stragglers in pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-streaming-stragglers).




For a general overview of debugging Dataflow pipelines, see [Troubleshoot and debug Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline).

## What's next

  * [Apache Kafka to Kafka template parameters](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/kafka-to-kafka)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
