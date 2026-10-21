---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-cloud-storage-connector/
title: Troubleshoot a Cloud Storage sink connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:19.914227+00:00
---

# Troubleshoot a Cloud Storage sink connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-cloud-storage-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Troubleshoot a Cloud Storage sink connector Stay organized with collections  Save and categorize content based on your preferences. 

This section provides troubleshooting guidance for common issues encountered when using a [Cloud Storage Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector).

## Deserialization is misconfigured

If the connector's converters don't match the data in Kafka, the connector fails with an error message similar to the following:
    
    
    org.apache.kafka.connect.errors.DataException: Converting byte[] to Kafka
    Connect data failed due to serialization error:
    

To resolve this issue, make sure the [key and value converters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#converters) for the connector match the data that the connector is reading from Kafka.

For example, if you set the format output type to `csv` and the value converter to `JsonConverter`, you might see the following error:
    
    
    org.apache.kafka.connect.errors.DataException: Converting byte[] to Kafka
    Connect data failed due to serialization error:
    **at org.apache.kafka.connect.json.JsonConverter.toConnectData(JsonConverter.java:333)**
    at org.apache.kafka.connect.storage.Converter.toConnectData(Converter.java:91)
    

This error occurs because CSV output requires `ByteArrayConverter` for the value converter, not `JsonConverter`. For more information, see [How a Cloud Storage Sink connector works](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector#storage-sink-connector).

The stack trace in the logs might help to locate the root cause. For example, the following log entry indicates a problem converting a UTF-32 character:
    
    
    Caused by: org.apache.kafka.common.errors.SerializationException:
    java.io.CharConversionException: Invalid UTF-32 character 0x31d086a
    (above 0x0010ffff) at char #1, byte #7
    

## Missing Cloud Storage bucket permissions

If the Managed Kafka service account doesn't have permission to write to the Cloud Storage bucket, the connector fails with an error message similar to the following:
    
    
    org.apache.kafka.connect.errors.ConnectException:
    com.google.cloud.storage.StorageException: 403 Forbidden
    

To resolve this issue, grant the **Storage Object Creator** role (`roles/storage.objectCreator`) to the Managed Kafka service account. For more information, see [Grant permissions to write to the Cloud Storage bucket](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector#grant-storage-permissions).

## Missing Cloud Storage credentials

If the connector configuration doesn't include `gcs.credentials.default=true`, the connector fails with an error message similar to the following:
    
    
    org.apache.kafka.connect.errors.ConnectException:
    com.google.cloud.storage.StorageException: 401 Unauthorized
    

To resolve this issue, add `gcs.credentials.default=true` to the connector's configuration settings.

## What's next

  * [Troubleshoot Connect clusters and connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-kafka-connect)
  * [Create a Cloud Storage sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
