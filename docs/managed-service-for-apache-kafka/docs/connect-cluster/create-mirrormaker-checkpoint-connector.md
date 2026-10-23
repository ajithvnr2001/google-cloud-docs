---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-checkpoint-connector/
title: Create a MirrorMaker 2.0 Checkpoint connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:22.572743+00:00
---

# Create a MirrorMaker 2.0 Checkpoint connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-checkpoint-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a MirrorMaker 2.0 Checkpoint connector Stay organized with collections  Save and categorize content based on your preferences. 

The MirrorMaker 2.0 Checkpoint connector copies consumer offsets from one Kafka cluster to another. Kafka consumers use consumer offsets to record the last successfully consumed message within a partition. Replicating the offsets lets consumers switch to the target cluster and resume processing from the same point.

You can use this connector to:

  * Help to ensure minimal downtime during a switch from the source cluster to the target cluster.

  * Enable seamless failover by providing a consistent consumer state across clusters.

  * Preserve consumer progress when you move data to the target cluster.




## How the Checkpoint connector works

The Checkpoint connector works with the [MirrorMaker 2.0 Source](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector) connector. The Checkpoint connector replicates offsets as follows:

  1. For each replicated partition, the MirrorMaker 2.0 Source connector writes replicated records to the target cluster.

  2. The records written to the target cluster typically have different offsets than the corresponding source records. To enable translation from source offsets to target offsets, the MirrorMaker 2.0 Source connector writes offset pairs to a topic named `mm2-offset-syncs.target.internal` on the source cluster. These offset pairs map source offsets to the corresponding target offsets.

  3. Consumers read records from the source cluster. To record progress, a consumer periodically _commits_ the latest processed message per partition. Kafka stores the committed offsets, also called _checkpoints_ , in a topic named `__consumer_offsets`. Checkpoint records include the consumer group ID of the consumer.

  4. The MirrorMaker 2.0 Checkpoint connector replicates the checkpoint records to a topic named `source.checkpoints.internal` in the target cluster.

  5. If `sync.group.offsets.enabled=true`, the Checkpoint connector periodically copies the checkpoints from `source.checkpoints.internal` to `__consumer_offsets` on the target cluster. This lets consumers restart from the latest committed offset after a failover. To resume processing, consumers use the same consumer group ID after failing over.

The `sync.group.offsets.interval.seconds` configuration setting controls how often the connector copies checkpoints to `__consumer_offsets`.




## Create a MirrorMaker 2.0 Checkpoint connector

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster where you want to create the connector.

The **Connect cluster details** page displays.

  3. Click **Create Connector**.

  4. In the **Connector name** field, enter a name for the connector.

  5. In the **Connector plugin** list, select "MirrorMaker 2.0 Checkpoint".

  6. For **Source cluster** , select an option:

     * **Managed Service for Apache Kafka Cluster** : In the **Kafka cluster** list, select the Managed Service for Apache Kafka cluster.
     * **Self-managed or External Kafka Cluster** : In the **Cluster bootstrap server** field, enter the bootstrap address of the Kafka cluster, in the format `HOSTNAME:PORT_NUMBER`.
  7. Optional: In the **Configurations** box, add configuration properties or edit the default properties. For more information, see Configure the connector.

  8. In the **Group names or Group regex** field, enter a comma-separated list of consumer groups to replicate. You can use regular expressions for the group names.

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




Here is an example of a configuration file for a MirrorMaker 2.0 Checkpoint connector:
    
    
    connector.class: "org.apache.kafka.connect.mirror.MirrorCheckpointConnector"
    emit.checkpoints.interval.seconds: "CHECKPOINT_INTERVAL"
    groups: ".*"
    groups.exclude: "console-consumer-.*,connect-.*,__.*"
    source.cluster.alias: "source"
    source.cluster.bootstrap.servers: "SOURCE_CLUSTER_BOOTSTRAP_ADDRESS"
    sync.group.offsets.enabled: "true"
    sync.group.offsets.interval.seconds: "OFFSETS_SYNC_INTERVAL"
    target.cluster.alias: "target"
    target.cluster.bootstrap.servers: "TARGET_CLUSTER_BOOTSTRAP_ADDRESS"
    tasks.max: "3"
    

Replace the following:

  * `CHECKPOINT_INTERVAL`: How often to write checkpoints, in seconds.

  * `SOURCE_CLUSTER_BOOTSTRAP_ADDRESS`: The bootstrap address of the source Kafka cluster.

  * `OFFSETS_SYNC_INTERVAL`: How often to copy checkpoints to the `__consumer_offsets` topic, in seconds. For more information, see Checkpoint synchronization.

  * `TARGET_CLUSTER_BOOTSTRAP_ADDRESS`: The bootstrap address of the target Kafka cluster.




## Configure the connector

This section describes some configuration properties that you can set on the connector.

For a complete list of the properties that are specific to this connector, see [MirrorMaker Checkpoint Configs](https://kafka.apache.org/37/configuration/mirrormaker-configs/#mirrormaker-checkpoint-configs) in the Apache Kafka documentation.

### Replicated consumer groups

To specify which consumer groups are replicated, set the `groups` configuration property. You can specify individual names or use regular expressions. Example: `"group1,group2,customer-*"`. The default value is `.*`.

To exclude consumer groups from replication, set the `groups.exclude` property.

### Checkpoint synchronization

The following settings control how the connector writes checkpoints to the target cluster.

  * `sync.group.offsets.enabled`: Whether to copy offsets from `source.checkpoints.internal` to `__consumer_offsets` on the target cluster. The default value is `false`. To enable consumers at the target cluster to restart seamlessly after a failover, set this property to `true`.

  * `emit.checkpoints.interval.seconds`: How often to write checkpoints to the internal checkpoint topic. Defaults to 60 seconds. When setting this property, consider the balance between tracking progress and minimizing the overhead of writing checkpoints. A value of 10 seconds is reasonable.

  * `sync.group.offsets.interval.seconds`: How often to copy checkpoints from the internal checkpoint topic to `__consumer_offsets`. Defaults to 60 seconds. This setting only applies if `sync.group.offsets.enabled` is `true`.




## What's next

  * [Create a MirrorMaker 2.0 Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector)
  * [Replicate Kafka topics with MirrorMaker 2.0](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/replicate-kafka-topics)
  * [Troubleshoot a MirrorMaker 2.0 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-mirrormaker-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
