---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-bq-connector-config/
title: Troubleshoot the BigQuery sink connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:03.946375+00:00
---

# Troubleshoot the BigQuery sink connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-bq-connector-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Troubleshoot the BigQuery sink connector Stay organized with collections  Save and categorize content based on your preferences. 

In Managed Service for Apache Kafka, you can diagnose and resolve ingestion issues in the [BigQuery Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector) for Kafka Connect.

This page describes common errors that you might encounter when you stream records from Managed Service for Apache Kafka to BigQuery tables, and provides troubleshooting steps.

## Troubleshooting table-driven configuration

In table-driven configuration mode, Kafka messages must closely align with the table schema. Here are some common issues that might occur when you configure this method.

### Missing non-nullable column

If a Kafka message omits a field that exists as a non-nullable column in the BigQuery table, the write operation fails with an error message similar to the following:
    
    
    Failed to write rows after BQ table creation or schema update within 30
    attempts for: GenericData{classInfo=[datasetId, projectId, tableId], {datasetId=<datasetID>, tableId=<tableID>}}"
    

Replace `<datasetID>` and `<tableID>` with the actual dataset and table IDs.

To resolve the issue, change the BigQuery column to `NULLABLE` and restart the connector.

### Undefined fields

If any fields in the Kafka message are not defined in the BigQuery table schema, the write operation fails with an error message similar to the following:
    
    
    Insertion failed at table repairScenario for following rows:
    [row index 0] (Failure reason : The source object has fields unknown to BigQuery: root.<fieldName>.)
    

Replace `<fieldName>` with the name of the undefined field.

To resolve the issue, add the missing fields to the BigQuery table and restart the connector.

### Type mismatch

If a type mismatch occurs between a Kafka message field and the corresponding BigQuery table column (for example, a string in Kafka and an integer in BigQuery), the write operation fails with an error message similar to the following:
    
    
    [row index 0] (location <field>, reason: invalid): Cannot convert value to <type> (bad value): <val>
    

Replace `<field>`, `<type>`, and `<val>` with the relevant field name, data type, and value, respectively.

This is a known issue.

### AppendRows request too large

When using the `StorageWrite` mode of the connector, you might see an error similar to the following:
    
    
    INVALID_ARGUMENT: AppendRows request too large: 11053472 limit 10485760
    

The connector attempts to write all messages within a single poll from Kafka in a single batch to BigQuery. If the batch size exceeds the BigQuery limit (10485760 bytes), the write operation fails. To resolve this error, set the `consumer.override.max.poll.records` configuration property on the connector to a smaller number. The default value for this parameter is 500.

## What's next

  * [Troubleshoot Connect clusters and connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-kafka-connect)
  * [Create a BigQuery Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
