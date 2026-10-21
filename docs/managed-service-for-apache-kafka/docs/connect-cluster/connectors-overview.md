---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview/
title: Connectors overview \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:16.269131+00:00
---

# Connectors overview  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Connectors overview Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists the Kafka Connect connector types that Managed Service for Apache Kafka supports. You can use these connectors to integrate Apache Kafka with your applications and with other Google Cloud services.

Connector | Description | Use cases  
---|---|---  
[ BigQuery Sink](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-bq-connector) |  Streams data from Kafka topics to a BigQuery table.  | Data warehousing, analytics  
[ Cloud SQL for PostgreSQL Source](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-sql-postgres-source-connector) |  Reads row-level changes from a Cloud SQL for PostgreSQL database and writes them to Kafka.  | Database integration, monitor and respond to database events  
[ Cloud Storage Sink](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector) |  Streams data from Kafka topics to a Cloud Storage bucket.  | Data lake ingestion, data archiving  
[ MirrorMaker 2.0](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector) |  Replicates topics and data from one Kafka cluster to another Kafka cluster.  | Data replication, disaster recovery, data migration  
[ Pub/Sub Sink](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-sink-connector) |  Streams data from Kafka topics to a Pub/Sub topic.  | Service integration, real-time notifications  
[ Pub/Sub Source](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-pubsub-source-connector) |  Streams messages from a Pub/Sub subscription to a Kafka topic.  | Real-time data ingestion, event-driven architectures  
[ Generic PostgreSQL Source](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-generic-postgres-source-connector) |  Reads row-level changes from a PostgreSQL database and writes them to Kafka.  | Database integration, monitor and respond to database events  
  
## Converters

Converters are responsible for serialization and deserialization of Kafka record data. They translate between the raw byte format found on Kafka topics and the internal, structured data representation used by Kafka Connect.

  * For sink connectors, converters deserialize data from the topic's wire format to the Kafka Connect internal data format, which the connector uses to write to the target system.

  * For source connectors, converters serialize the data from the Kafka Connect internal data format to the specified wire format for the Kafka topic.




Converters ensure that the connector reads or writes the Kafka records in a format that is compatible with the external system.

When you configure a connector, set the following properties:

  * Key converter (`key.converter`): The converter to use when serializing and deserializing Kafka record keys.

  * Value converter (`value.converter`): The converter to use when serializing and deserializing Kafka record values.




If you don't specify a converter, the default converter type is `org.apache.kafka.connect.converters.ByteArrayConverter`, which passes the data through in its raw byte format.

### Supported converters

Managed Service for Apache Kafka supports the following built-in converters:

Converter| Format  
---|---  
`io.confluent.connect.avro.AvroConverter` | Apache Avro  
`org.apache.kafka.connect.converters.BooleanConverter` | Boolean  
`org.apache.kafka.connect.converters.ByteArrayConverter` |  Byte array The default converter type. Preserves the exact content of messages across two systems.  
`org.apache.kafka.connect.converters.DoubleConverter` | Double  
`org.apache.kafka.connect.converters.FloatConverter` | Float  
`org.apache.kafka.connect.converters.IntegerConverter` | Integer  
`org.apache.kafka.connect.json.JsonConverter` |  JSON For JSON data without a schema, also set `value.converter.schemas.enable=false`.  
`org.apache.kafka.connect.converters.LongConverter` | Long  
`org.apache.kafka.connect.converters.ShortConverter` | Short  
`org.apache.kafka.connect.storage.StringConverter` | String  
  
The choice of converter depends on the connector type and the data that you are storing in Kafka. For more information, see the documentation for the specific connector.

## Tasks

A connector transfers data by creating one or more _tasks_ that operate in parallel. To set an upper limit on how many tasks a connector creates, set the connector's `tasks.max` configuration property. The connector might create fewer tasks than this value.

Increasing the value of `tasks.max` can improve throughput, but also increase resource consumption (CPU and memory). The optimal value depends on the workload and the resources allocated to your Connect cluster workers. For sink connectors, the number of Kafka topic partitions can also affect parallelism.

### Task restart policy

You can set a connector's _task restart policy_ , which determines the behavior when a failure occurs. Connectors support the following policies:

  * **Never restart.** The connector does not restart failed tasks. This policy is the default behavior. It's useful for debugging, or in situations where manual intervention is required after an error.

  * **Restart with exponential backoff.** The connector restarts a failed task after a delay (called the _backoff_ period). The delay increases exponentially with each subsequent failure. This policy is recommended for most production workloads.

If you use the exponential backoff policy, also set values for the minimum and maximum backoff. The minimum backoff should be greater than 60 seconds, and the maximum backoff should be less than 7200 seconds.




## Transformations and predicates

Managed Service for Apache Kafka supports the default Kafka Connect [transformations](https://kafka.apache.org/37/kafka-connect/user-guide/#transformations) and [predicates](https://kafka.apache.org/37/kafka-connect/user-guide/#predicates).

**Transformations** let you modify individual messages before they are sent to Managed Service for Apache Kafka (for source connectors) or to the external system (for sink connectors). You might use a transformation to mask sensitive data, add timestamps, or rename fields.

**Predicates** let you filter data based on specific conditions, determining which messages a transform applies to based on message properties.

For example, to configure a sink connector to disregard messages that contain a `DoNotProcess` header key, add the following configuration:
    
    
    transforms=dropMessage
    transforms.dropMessage.type=org.apache.kafka.connect.transforms.Filter
    transforms.dropMessage.predicate=hasKey
    predicates=hasKey
    predicates.hasKey.type=org.apache.kafka.connect.transforms.predicates.HasHeaderKey
    predicates.hasKey.name=DoNotProcess
    

This configuration does the following:

  1. Configures a predicate named `hasKey` of type [`org.apache.kafka.connect.transforms.predicates.HasHeaderKey`](https://kafka.apache.org/37/kafka-connect/user-guide/#org.apache.kafka.connect.transforms.predicates.HasHeaderKey). This predicate matches all messages that contain a header with the key `DoNotProcess`.

  2. Configures a transformation named `dropMessage` of type [`org.apache.kafka.connect.transforms.Filter`](https://kafka.apache.org/37/kafka-connect/user-guide/#org.apache.kafka.connect.transforms.Filter). This transformation drops all messages that match the configured predicate.

  3. Links the transformation to the predicate `hasKey`. This ensures that only messages with the `DoNotProcess` header key present are dropped by the transformation.




## What's next?

  * [Kafka Connect overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview)

  * [Create a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
