---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/view-brokers/
title: View brokers in a Google Cloud Managed Service for Apache Kafka cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:45.485870+00:00
---

# View brokers in a Google Cloud Managed Service for Apache Kafka cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/view-brokers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  View brokers in a Google Cloud Managed Service for Apache Kafka cluster Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Kafka automatically provisions the brokers for a cluster. A broker has the following properties:

  * `brokerIndex`: The zero-based index of the broker.
  * `nodeId`: The node ID for the broker.
  * `rack`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where the broker is provisioned, for example `us-central1-a`.



To view the brokers for a cluster, perform the following steps.

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. Select the **Configurations** tab. The cluster's brokers are listed under **Active Brokers**.




###  gcloud 

To get a list of the cluster's brokers, use the [`managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command with the `--full` flag.
    
    
    gcloud managed-kafka clusters describe CLUSTER_ID \
      --location=LOCATION \
      --full \
      --format="yaml(brokerDetails)"
    

Replace the following:

  * CLUSTER_ID: The ID or name of the cluster.
  * LOCATION: The location of the cluster.



The output looks similar to the following:
    
    
    brokerDetails:
    - brokerIndex: '0'
      nodeId: '10'
      rack: us-central1-c
    - brokerIndex: '1'
      nodeId: '11'
      rack: us-central1-f
    - brokerIndex: '2'
      nodeId: '12'
      rack: us-central1-b
    

###  Kafka CLI 

Before running this command, install the Kafka command-line tools on a Compute Engine VM. The VM must be able to reach a subnet that is connected to your Managed Service for Apache Kafka cluster. Follow the instructions in [ Produce and consume messages with the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart). 

To get a list of the cluster's brokers, use the `kafka-configs.sh --describe` command with the `--entity-type=brokers` flag.
    
    
    kafka-configs.sh --describe --entity-type brokers \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties
    

Replace BOOTSTRAP_ADDRESS with the cluster's [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).

This command returns a list of broker IDs, along with their dynamic configuration settings, if any. It does not return the `rack` property.

## What's next

  * [Overview of brokers in Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers)
  * [View a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
