---
url: https://docs.cloud.google.com/bigtable/docs/kafka-sink-connector/
title: Kafka Connect Bigtable sink connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:36.378998+00:00
---

# Kafka Connect Bigtable sink connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/kafka-sink-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Kafka Connect Bigtable sink connector

  
Sink connectors are plugins for the Kafka Connect framework that you can use to stream data from Kafka directly to other systems for storage and processing. The Kafka Connect Bigtable sink is a dedicated connector designed to stream data into Bigtable in real time with as little latency as possible. 

This page describes the connector's features and limitations. It also provides example usage for advanced scenarios with [Single Message Transforms (SMTs)](https://kafka.apache.org/documentation/#connect_transforms) and automated table creation. For installation instructions and full reference documentation, see the [Kafka Connect Bigtable Sink Connector repository](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/main/kafka-connect-bigtable-sink/README.md).

## Features

The Bigtable sink connector subscribes to your Kafka topics, reads messages received on these topics, and then writes the data to Bigtable tables. The following sections provide a high-level overview for each feature. For usage details, see Configuration section of this document.

#### Key mapping, SMTs, and converters

To write data to a Bigtable table, you need to provide a unique row key, column family, and column name for each operation. This information is inferred from the fields in Kafka messages. You can construct all the required identifiers with settings like `row.key.definition`, `row.key.delimiter`, or `default.column.family`. 

#### Automatic table creation

You can use the `auto.create.tables` and `auto.create.column.families` settings to automatically create destination tables and column families if they don't exist in your Bigtable destination. This flexibility comes at a certain performance cost, so we generally recommend that you first create the tables where you want to stream data. 

#### Write modes and deleting rows

When you write to a table, you can completely overwrite the data if a row already exists, or choose to abandon the operation with the `insert.mode` setting. You can leverage this setting in conjunction with DLQ error handling to achieve the _at least once delivery_ guarantee. 

To issue `DELETE` commands, configure the `value.null.mode` property. You can use it for deleting full rows, column families, or individual columns. 

#### Dead Letter Queue

Configure the `errors.deadletterqueue.topic.name` property and set `errors.tolerance=all` to post messages that fail to process to your DLQ topic. 

#### Compatibility with the Confluent Platform Bigtable Sink Connector

The Bigtable Kafka Connect sink connector from Google Cloud offers full parity with the [ self-managed Confluent Platform Bigtable Sink Connector](https://docs.confluent.io/kafka-connectors/gcp-bigtable/current/configuration_options.html). You can use your existing configuration file for the Confluent Platform connector by adjusting the `connector.class` setting to `connector.class=com.google.cloud.kafka.connect.bigtable.BigtableSinkConnector`. 

## Limitations

The following limitations apply:

  * The Kafka Connect Bigtable sink connector is currently only supported for Kafka clusters where you are able to independently install connectors (self-managed or on-premises Kafka clusters). This connector isn't currently supported for [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview).

  * This connector can create column families and columns from field names up to two nesting levels:

    * Structs nested deeper than two levels are converted to `JSON` and saved in their parent column.
    * Root-level structs are transformed into column families. Fields in those structs become column names.
    * Root-level primitive values are by default saved to a column family that uses the Kafka topic as its name. Columns in that family have names equal to the field names. You can modify this behavior by using the `default.column.family` and `default.column.qualifier` settings.



## Installation

To install this connector, you follow standard installation steps: build the project with Maven, copy the `.jar` files to your Kafka Connect plugin directory, and create the configuration file. For step-by-step instructions, see the [Running the connector](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/tree/main/kafka-connect-bigtable-sink#running-the-connector) section in the repository.

## Configuration

To configure Kafka Connect connectors, you need to write configuration files. The Bigtable Kafka Connect sink connector from Google Cloud supports all [basic Kafka connector properties](https://kafka.apache.org/documentation/#connect_configuring), as well as some extra fields tailored for working with Bigtable tables.

The following sections provide detailed examples for more advanced use cases, but they don't describe all available settings. For basic usage examples and the full properties reference, see the [Kafka Connect Bigtable Sink Connector repository](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/main/kafka-connect-bigtable-sink/README.md).

### Example: flexible row key and column family creation

Sample scenario
    

Your incoming Kafka messages contain details for shopping orders with user identifiers. You want to write each order to a row with two column families: one for user details, one for order details. 

Source Kafka message format
    

You format Kafka messages posted to the topic with the [`JsonConverter`](https://github.com/apache/kafka/blob/trunk/connect/json/src/main/java/org/apache/kafka/connect/json/JsonConverter.java) to achieve the following structure: 
    
    
    {
      "user": "user123",
      "phone": "800‑555‑0199",
      "email": "business@example.com",
      "order": {
        id: "order123",
        items: ["itemUUID1", "itemUUID2"],
        discount: 0.2
      }
    }

Expected Bigtable row
    

You want to write each message as a Bigtable row with the following structure: 

Row key | contact_details | order_details  
---|---|---  
name | phone | email | orderId | items | discount  
`user123#order123` | user123 | 800‑555‑0199 | business@example.com | order123 | ["itemUUID1", "itemUUID2"] | 0.2  
Connector configuration
     To achieve the expected result, you write the following configuration file: 
    
    
    # Settings such as latency configuration or DLQ identifiers omitted for brevity.
    # Refer to the GitHub repository for full settings reference.
    
    # Connector name, class, Bigtable and Google Cloud identifiers
    name=BigtableSinkConnector
    connector.class=com.google.cloud.kafka.connect.bigtable.BigtableSinkConnector
    gcp.bigtable.project.id=my_project_id
    gcp.bigtable.instance.id=my_bigtable_instance_id
    
    # Use JsonConverter to format Kafka messages as JSON
    key.converter=org.apache.kafka.connect.json.JsonConverter
    value.converter=org.apache.kafka.connect.json.JsonConverter
    
    # Name of the topic where shopping details are posted
    topics=shopping_topic
    
    # Settings for row key creation
    row.key.definition=user,order.id
    row.key.delimiter=#
    
    # All user identifiers are root level fields.
    # Use the default column family to aggregate them into a single family.
    default.column.family=contact_details
    
    # Use SMT to rename "orders" field into "order_details" for the new column family
    transforms=renameOrderField
    transforms.renameOrderField.type=org.apache.kafka.connect.transforms.ReplaceField$Key
    transforms.renameOrderField.renames=order:order_details

The results of using this file are as follows: 

  * `row.key.definition=user,order.id` is a comma-separated list of the fields you want to use to construct the row key. Each entry is concatenated with the character set in the `row.key.delimiter` setting. 

When you use `row.key.definition`, all your messages need to use the same schema. If you need to process messages with different structures into different columns or column families, we recommend that you create separate connector instances. For more information, see the  Example: write messages to multiple tables section of this document. 

  * Bigtable column family names are based on the names of non-null root-level structs. As such: 

    * Values for the contact details are root-level primitive data types, so you aggregate them into a default column family with the `default.column.family=contact_details` setting. 
    * Order details are already wrapped in the `order` object, but you want to use `order_details` as the column family name. To achieve that, you use the [ReplaceFields SMT](https://kafka.apache.org/documentation/#org.apache.kafka.connect.transforms.ReplaceField) and rename the field. 



### Example: automatic table creation and idempotent writes

Sample scenario
    

Your incoming Kafka messages contain details for shopping orders. Customers can edit their baskets before fulfillment, so you expect to receive follow-up messages with changed orders that you need to save as updates in the same row. You also can't guarantee that the destination table exists at write time, so you want the connector to automatically create the table if it doesn't exist. 

Connector configuration
     To achieve the expected result, you write the following configuration file: 
    
    
    # Settings such as latency configuration or DLQ identifiers omitted for brevity.
    # Refer to the GitHub repository for full settings reference.
    
    # Settings for row key creation also omitted.
    # Refer to the Example: flexible row key and column family creation section.
    
    # Connector name, class, Bigtable and Google Cloud identifiers
    name=BigtableSinkConnector
    connector.class=com.google.cloud.kafka.connect.bigtable.BigtableSinkConnector
    gcp.bigtable.project.id=my_project_id
    gcp.bigtable.instance.id=my_bigtable_instance_id
    
    # Use JsonConverter to format Kafka messages as JSON
    key.converter=org.apache.kafka.connect.json.JsonConverter
    value.converter=org.apache.kafka.connect.json.JsonConverter
    
    # Name of the topic where shopping details are posted
    topics=shopping_topic
    
    # Automatically create destination tables if they don't exist
    auto.create.tables=true
    
    # UPSERT causes subsequent writes to overwrite existing rows.
    # This way you can update the same order when customers change the contents
    # of their baskets.
    insert.mode=upsert

### Example: write messages to multiple tables

Sample scenario
    

Your incoming Kafka messages contain details for shopping orders from different fulfillment channels. These messages are posted to different topics, and you want to use the same configuration file to write them to separate tables. 

Connector configuration
    

You can write your messages to multiple tables, but if you use a single configuration file for your setup, then each message must use the same schema. If you need to process messages from different topics into distinct columns or families, we recommend that you create separate connector instances. 

To achieve the expected result, you write the following configuration file:
    
    
    # Settings such as latency configuration or DLQ identifiers omitted for brevity.
    # Refer to the GitHub repository for full settings reference.
    
    # Settings for row key creation are also omitted.
    # Refer to the Example: flexible row key and column family creation section.
    
    # Connector name, class, Bigtable and Google Cloud identifiers
    name=BigtableSinkConnector
    connector.class=com.google.cloud.kafka.connect.bigtable.BigtableSinkConnector
    gcp.bigtable.project.id=my_project_id
    gcp.bigtable.instance.id=my_bigtable_instance_id
    
    # Use JsonConverter to format Kafka messages as JSON
    key.converter=org.apache.kafka.connect.json.JsonConverter
    value.converter=org.apache.kafka.connect.json.JsonConverter
    
    # Name of the topics where shopping details are posted
    topics=shopping_topic_store1,shopping_topic_store2
    
    # Use a dynamic table name based on the Kafka topic name.
    table.name.format=orders_${topic}

In this approach, you use the `table.name.format=orders_${topic}` property to dynamically refer to each Kafka topic name. When you configure multiple topic names with the `topics=shopping_topic_store1,shopping_topic_store2` setting, each message is written to a separate table: 

  * Messages from the `shopping_topic_store1` topic are written to the `orders_shopping_topic_store1` table. 
  * Messages from the `shopping_topic_store2` topic are written to the `orders_shopping_topic_store2` table. 



## What's next

  * [Bigtable Beam connector](https://docs.cloud.google.com/bigtable/docs/beam-connector)
  * [Bigtable Flink connector](https://docs.cloud.google.com/bigtable/docs/flink-connector)
  * [Integrations with Bigtable](https://docs.cloud.google.com/bigtable/docs/integrations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
