---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-pubsub-connector/
title: Troubleshoot a Pub/Sub connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:21.132220+00:00
---

# Troubleshoot a Pub/Sub connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-pubsub-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Troubleshoot a Pub/Sub connector Stay organized with collections  Save and categorize content based on your preferences. 

This section provides troubleshooting guidance for common issues encountered when using a [Pub/Sub source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector) or [Pub/Sub sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector).

## Missing Pub/Sub permissions

If the Managed Kafka service account doesn't have permission to access the Pub/Sub resources, the following error occurs:
    
    
    PERMISSION_DENIED: User not authorized to perform this action.
    

This error might occur for several reasons.

  * **Pub/Sub Source connector** : The Managed Kafka service account might not have permission to access the Pub/Sub subscription. To resolve this issue, grant the Managed Kafka service account both of the following Identity and Access Management (IAM) roles:

    * **Pub/Sub Subscriber** (`roles/pubsub.subscriber`)
    * **Pub/Sub Viewer** (`roles/pubsub.viewer`) 

For more information, see [Grant permissions to read from the Pub/Sub subscription](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector#grant-pubsub-permissions).

  * **Pub/Sub Sink connector** : The Managed Kafka service account might not have permission to publish to the Pub/Sub topic. To resolve this issue, grant the Managed Kafka service the **Pub/Sub Publisher** (`roles/pubsub.publisher`) IAM role.

For more information, see [Grant permissions to publish to the Pub/Sub topic](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector#grant-pubsub-permissions).




## Error verifying the subscription

If the Pub/Sub Source connector can't find the Pub/Sub subscription, the connector fails with an error similar to the following:
    
    
    org.apache.kafka.connect.errors.ConnectException: Error verifying the subscription SUBSCRIPTION for project PROJECT
    

To resolve this issue, verify that the connector's `cps.subscription` configuration specifies the correct subscription, and that the subscription exists in your project.

## Connector fails to convert records

If the connector's key converter or value converter is incompatible with the data type of records, a message similar to the following appears in the connector logs:
    
    
    org.apache.kafka.connect.errors.DataException: Invalid schema type for
    CONVERTER_NAME: DATA_FORMAT
    

To resolve this issue, change the key converter or value converter to the correct class to support the schema data type.

For example, if you the set the key converter to `ByteArrayConverter`, you might see the error `"Invalid schema type for ByteArrayConverter: STRING"`. This error occurs because the `ByteArrayConverter` doesn't support `STRING` types. Instead, use `org.apache.kafka.connect.storage.StringConverter`.

### Invalid schema type for `ByteArrayConverter`

The following issue occurs when a Pub/Sub Source connector outputs a Kafka record with a `struct` value, but the connector's value converter is a `ByteArrayConverter`.

The Pub/Sub messages are not written to the Kafka topic, and an error like the following appears in the connector logs:
    
    
    org.apache.kafka.connect.errors.DataException: Invalid schema type for ByteArrayConverter: STRUCT
    

To resolve this issue, make one of the following changes to the connector configuration:

  * Change `value.converter` to `org.apache.kafka.connect.json.JsonConverter`. With this setting, the connector converts the `struct` to JSON.

  * Don't change `value.converter`, but add `kafka.record.headers=true` to the configuration. With this setting, the connector writes the message data as a byte array instead of a `struct`. Any custom attributes in the Pub/Sub message are written as Kafka record headers.




For more information, see [Message conversion](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector#kafka-records).

## What's next

  * [Troubleshoot Connect clusters and connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-kafka-connect)
  * [Create a Pub/Sub source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector)
  * [Create a Pub/Sub sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
