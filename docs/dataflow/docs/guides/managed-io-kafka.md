---
url: https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka/
title: Dataflow managed I/O for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:40.544245+00:00
---

# Dataflow managed I/O for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow managed I/O for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

[Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io) supports reading and writing to Apache Kafka.

## Requirements

The following SDKs support managed I/O for Apache Kafka:

  * Apache Beam SDK for Java version 2.58.0 or later
  * Apache Beam SDK for Python version 2.61.0 or later



## Configuration

Managed I/O for BigQuery supports the following configuration parameters:

### `KAFKA` Read

Configuration | Type | Description  
---|---|---  
**bootstrap_servers** |  `str` |  A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. The client will make use of all servers irrespective of which servers are specified here for bootstrapping—this list only impacts the initial hosts used to discover the full set of servers. This list should be in the form `host1:port1,host2:port2,...`   
**topic** |  `str` |  n/a   
allow_duplicates  |  `boolean` |  If the Kafka read allows duplicates.   
confluent_schema_registry_subject  |  `str` |  n/a   
confluent_schema_registry_url  |  `str` |  n/a   
consumer_config_updates  |  `map[str, str]` |  A list of key-value pairs that act as configuration parameters for Kafka consumers. Most of these configurations will not be needed, but if you need to customize your Kafka consumer, you may use this. See a detailed list: https://docs.confluent.io/platform/current/installation/configuration/consumer-configs.html   
file_descriptor_path  |  `str` |  The path to the Protocol Buffer File Descriptor Set file. This file is used for schema definition and message serialization.   
format  |  `str` |  The encoding format for the data stored in Kafka. Valid options are: RAW,STRING,AVRO,JSON,PROTO   
message_name  |  `str` |  The name of the Protocol Buffer message to be used for schema extraction and data conversion.   
offset_deduplication  |  `boolean` |  If the redistribute is using offset deduplication mode.   
redistribute_by_record_key  |  `boolean` |  If the redistribute keys by the Kafka record key.   
redistribute_num_keys  |  `int32` |  The number of keys for redistributing Kafka inputs.   
redistributed  |  `boolean` |  If the Kafka read should be redistributed.   
schema  |  `str` |  The schema in which the data is encoded in the Kafka topic. For AVRO data, this is a schema defined with AVRO schema syntax (https://avro.apache.org/docs/1.10.2/spec.html#schemas). For JSON data, this is a schema defined with JSON-schema syntax (https://json-schema.org/). If a URL to Confluent Schema Registry is provided, then this field is ignored, and the schema is fetched from Confluent Schema Registry.   
  
### `KAFKA` Write

Configuration | Type | Description  
---|---|---  
**bootstrap_servers** |  `str` |  A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. The client will make use of all servers irrespective of which servers are specified here for bootstrapping—this list only impacts the initial hosts used to discover the full set of servers. | Format: host1:port1,host2:port2,...   
**format** |  `str` |  The encoding format for the data stored in Kafka. Valid options are: RAW,JSON,AVRO,PROTO   
**topic** |  `str` |  n/a   
file_descriptor_path  |  `str` |  The path to the Protocol Buffer File Descriptor Set file. This file is used for schema definition and message serialization.   
message_name  |  `str` |  The name of the Protocol Buffer message to be used for schema extraction and data conversion.   
producer_config_updates  |  `map[str, str]` |  A list of key-value pairs that act as configuration parameters for Kafka producers. Most of these configurations will not be needed, but if you need to customize your Kafka producer, you may use this. See a detailed list: https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html   
schema  |  `str` |  n/a   
  
## What's next

For more information and code examples, see the following topics:

  * [Read from Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka)
  * [Write to Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/write-to-kafka)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
