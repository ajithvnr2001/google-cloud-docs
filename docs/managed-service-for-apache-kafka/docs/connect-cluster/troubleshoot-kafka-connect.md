---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-kafka-connect/
title: Troubleshoot Connect clusters and connectors \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:46.997701+00:00
---

# Troubleshoot Connect clusters and connectors  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-kafka-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Troubleshoot Connect clusters and connectors Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides troubleshooting guidance for Connect clusters and connectors.

## Detached state

A Connect Cluster can be in the state of `DETACHED`. This state means that the underlying Kafka cluster has been deleted or is in the process of being deleted. Because Kafka Connect stores all state on Kafka, the Connect Cluster is permanetly stopped. A Connect Cluster cannot be re-attached, and this cluster should be deleted.

## Per-cluster limits

A single Connect Cluster can become unresponsive if it tries to manage too many total Connect tasks. To prevent this issue, the following limits apply:

  * A Connect Cluster can have a maximum of 20 connectors.
  * A connector can have a maximum of 200 tasks.



If you need more connectors, you can attach a second Connect Cluster to the same same Kafka cluster.

## Troubleshoot a connector

If a connector fails to start up or fails while running, the [operational state](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connector) is `Failed`. A connector can also have errors while running; these appear in the connector logs.

To troubleshoot a connector, perform the following steps.

  1. View the connector logs to identify the error. For more information, see [View connector logs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/monitor-connect-cluster#view-connector-logs).

  2. Identify the root cause of the error. The following topics describe specific errors that might occur for each connector type:

     * [Troubleshoot a BigQuery sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-bq-connector-config)
     * [Troubleshoot a Cloud Storage sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-cloud-storage-connector)
     * [Troubleshoot a MirrorMaker 2.0 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-mirrormaker-connector)
     * [Troubleshoot a Pub/Sub connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-pubsub-connector)
  3. If the connector is mis-configured, [update](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connector) the connector's configuration and then [resume](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/pause-resume-stop-restart-connector#resume-connector) the connector. Transient failures might not require any changes to the configuration.




As a best practice, set the connector's [task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy) to restart with exponential backoff. This setting helps to avoid connector failures due to transient errors.

## Connect cluster errors

This section describes errors that might occur in a Connect cluster.

### Metadata topic has `'cleanup policy=delete'`

The Connect cluster logs show an error similar to the following:
    
    
    org.apache.kafka.common.config.ConfigException: Topic 'connect-offsets-
    PROJECT_ID-LOCATION-CONNECT_CLUSTER_NAME-UNIQUE_ID' supplied via the
    'offset.storage.topic' property is required to have 'cleanup policy=compact' to
    guarantee consistency and durability of source connector offsets, but found the
    topic currently has 'cleanup policy=delete'.
    

This error might occur for the following reasons:

  * The Connect cluster's primary Kafka cluster was deleted and then recreated with the same name.
  * The metadata topics created by the Connect cluster in the primary Kafka cluster were deleted.



To resolve this error, perform the following steps:

  1. Locate the metadata topics in the primary Kafka cluster. The metadata topics are named with the following format:

`connect-status-PROJECT_ID-LOCATION-CONNECT_CLUSTER_NAME-UNIQUE_ID`

For example:

`connect-status-project1-us-central1-connect1-3c563900-a4e4-4eDe-88f7-73b16d6344d2`

  2. For each metadata topic, edit the topic and add the key-value pair `cleanup.policy:compact` to the **Non-default parameters** field. For more information, see [Update a Kafka topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic).




## What's next

  * [Monitor a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/monitor-connect-cluster)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
