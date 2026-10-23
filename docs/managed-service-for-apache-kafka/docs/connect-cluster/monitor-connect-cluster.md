---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/monitor-connect-cluster/
title: Monitor a Connect cluster \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:22.135383+00:00
---

# Monitor a Connect cluster  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/monitor-connect-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Monitor a Connect cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to monitor a [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) by viewing metrics and logs for the Connect cluster and its connectors.

## View Connect cluster metrics

To view metrics for a Connect cluster and its connectors, perform the following steps.

  1. Go to the **Managed Service for Apache Kafka** > **Connect clusters** page.

[Go to Connect clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the name of the Connect cluster.

  3. Click the **Monitoring** tab. The **Monitoring** tab displays charts for the following metrics:

     * **Worker CPU usage**. The CPU usage of the Connect cluster workers.

     * **Worker memory usage**. The memory usage of the Connect cluster workers.

     * **Connector incoming byte rate**. The average number of bytes read from sources, per second.

     * **Connector outgoing byte rate**. The average number of bytes written or sent to sinks, per second.

  4. Optional: To view one of these metrics in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), select more_vert**More chart options** in the graph and click **View in Metrics Explorer**.




Worker CPU and worker memory are useful for tracking overall resource utilization in a Connect cluster. Creating new connectors increases CPU and memory utilization.

The connector metrics shown on this tab are aggregated across all of the connectors running in the cluster. Use these metrics to monitor the amount of data that is read or sent per second.

### View additional metrics in Metrics Explorer

To view additional metrics for a Connect cluster, use [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), as follows:

  1. Go to the **Cloud Monitoring** > **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Click **Select a metric**.

  3. In the **Active resources** section, select one or more metrics from the `Apache Kafka Connect Cluster` and `Apache Kafka Connect Connector` categories.




## View Connect cluster logs

You can view logs for a Connect cluster and its connectors in the **Connect clusters** page or by using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### View cluster logs

To view the logs for a Connect cluster, perform the following steps:

  1. Go to the **Managed Service for Apache Kafka** > **Connect clusters** page.

[Go to Connect clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the name of the Connect cluster.

  3. Click **Logs**. The **Logs** tab displays logs for the selected Connect cluster. These logs are updated in real time.

  4. Optional: To view historical logs, use the Logs Explorer. From the **Logs** tab, click open_in_new **View in Logs Explorer**. The Logs Explorer opens with a pre-populated query.




### View connector logs

To view logs for a connector, perform the following steps:

  1. Go to the **Managed Service for Apache Kafka** > **Connect clusters** page.

[Go to Connect clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the name of the Connect cluster.

  3. Click **Resources**.

  4. Click the name of the connector.

  5. Click **Logs**. The **Logs** tab displays logs for the connector. These logs are updated in real time.

This view filters log entries that contain the connector's name. It might not contain all logs that relate to the connector. For the complete set of logs, view the Connect cluster logs.

  6. Optional: To view historical logs, use the Logs Explorer. From the **Logs** tab, click open_in_new **View in Logs Explorer**. The Logs Explorer opens with a pre-populated query.




### View logs by using the Logs Explorer

In the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), you can query for Connect cluster logs by using the following query:
    
    
    resource.type="managedkafka.googleapis.com/ConnectCluster"
    resource.labels.cluster_id="CONNECT_CLUSTER_NAME"
    resource.labels.location="LOCATION"
    

Replace the following:

  * `CONNECT_CLUSTER_NAME`: the name of the Connect cluster
  * `LOCATION`: the location of the Connect cluster



Connect cluster logs contain all of the logs emitted by the cluster, including log entries for the connectors.

For more information about writing queries in the Logs Explorer, see [Build and save queries by using the Logging query language](https://docs.cloud.google.com/logging/docs/view/building-queries).

## What's next

  * [Monitor a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster).
  * [Learn more about Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview).



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
