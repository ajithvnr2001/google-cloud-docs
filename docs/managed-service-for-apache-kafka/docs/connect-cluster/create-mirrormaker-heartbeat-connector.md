---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-heartbeat-connector/
title: Create a MirrorMaker 2.0 Heartbeat connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:18.491715+00:00
---

# Create a MirrorMaker 2.0 Heartbeat connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-heartbeat-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a MirrorMaker 2.0 Heartbeat connector Stay organized with collections  Save and categorize content based on your preferences. 

The MirrorMaker 2.0 Heartbeat connector generates periodic heartbeat messages. It writes these messages to a dedicated topic named `heartbeats` in the target cluster.

After you configure a MirrorMaker 2.0 Heartbeat connector, you can use a [MirrorMaker 2.0 Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector) to replicate the `heartbeats` topic to a remote cluster. By observing the replicated heartbeats, you can implement the following use cases:

  * Monitor the status and performance of data replication between the clusters.

  * Verify the connection and data flow between clusters even when no other data is being produced.

  * Configure alerts in Cloud Monitoring to notify you if replication of the heartbeat stops.

  * Monitor lag (end-to-end replication latency) between two clusters.




Used by itself, the Heartbeat connector doesn't automatically monitor replication between clusters. You must replicate the `heartbeats` topic and observe the heartbeat messages arriving at the remote cluster.

## Create a MirrorMaker 2.0 Heartbeat connector

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster where you want to create the connector.

The **Connect cluster details** page displays.

  3. Click **Create Connector**.

  4. In the **Connector name** field, enter a name for the connector.

  5. In the **Connector plugin** list, select "MirrorMaker 2.0 Heartbeat".

  6. For **Primary Kafka cluster** , choose one of the following options:

     * **Use primary Kafka cluster as source cluster**.
     * **Use primary Kafka cluster as target cluster**.

The connector writes heartbeats to the _target_ cluster.

  7. For **Target cluster** or **Source cluster** , choose one of the following options:

     * **Managed Service for Apache Kafka Cluster**. If you select this option, select the Managed Service for Apache Kafka cluster in the **Kafka cluster** list.
     * **Self-managed or External Kafka Cluster** : If you select this option, enter the bootstrap address of the Kafka cluster, in the format `HOSTNAME:PORT_NUMBER`.
  8. Optional: In the **Configurations** box, add configuration properties or edit the default properties. For more information, see Configure the connector.

  9. Select the **Task restart policy**. For more information, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).

  10. Click **Create**.




###  gcloud 

  1. Run the [`gcloud managed-kafka connectors create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create) command:
         
         gcloud managed-kafka connectors create CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID \
             --config-file=CONFIG_FILE
         

Replace the following:

     * `CONNECTOR_ID`: The ID or name of the connector.

     * `LOCATION`: The location of the Connect cluster.

     * `CONNECT_CLUSTER_ID`: The ID of the Connect cluster.

     * `CONFIG_FILE`: The path to a YAML or JSON configuration file.




Here is an example of a configuration file for a MirrorMaker 2.0 Heartbeat connector:
    
    
    connector.class: "org.apache.kafka.connect.mirror.MirrorHeartbeatConnector"
    source.cluster.alias: "source"
    source.cluster.bootstrap.servers: "SOURCE_CLUSTER_BOOTSTRAP_ADDRESS"
    target.cluster.alias: "target"
    target.cluster.bootstrap.servers: "TARGET_CLUSTER_BOOTSTRAP_ADDRESS"
    tasks.max: "3"
    

Replace the following:

  * `SOURCE_CLUSTER_BOOTSTRAP_ADDRESS`: The bootstrap address of the source Kafka cluster.

  * `TARGET_CLUSTER_BOOTSTRAP_ADDRESS`: The bootstrap address of the target Kafka cluster.




## Configure the connector

Optionally, you can set the following configuration parameters:

  * `heartbeats.topic.replication.factor`: The replication factor for the `heartbeats` topic.

  * `emit.heartbeats.interval.seconds`: How often the connector emits a heartbeat, in seconds.




For more information, see [MirrorMaker HeartBeat Configs](https://kafka.apache.org/37/configuration/mirrormaker-configs/#mirrormaker-heartbeat-configs) in the Apache Kafka documentation.

## What's next

  * [Create a MirrorMaker 2.0 Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector)
  * [Replicate Kafka topics with MirrorMaker 2.0](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/replicate-kafka-topics)
  * [Troubleshoot a MirrorMaker 2.0 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-mirrormaker-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
