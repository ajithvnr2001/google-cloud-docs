---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource/
title: Guidelines to name a Google Cloud Managed Service for Apache Kafka resource \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:44.234730+00:00
---

# Guidelines to name a Google Cloud Managed Service for Apache Kafka resource  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/apis)



Send feedback 

#  Guidelines to name a Google Cloud Managed Service for Apache Kafka resource Stay organized with collections  Save and categorize content based on your preferences. 

A Google Cloud resource is any component that you create or use within the Google Cloud. These resources form the building blocks of your applications and systems running on the platform.

Resources in Managed Service for Apache Kafka include the following:

  * Cluster

  * Topic

  * Consumer group

  * ACL

  * Schema registry

  * Context (within a schema registry)

  * Subject (within a schema registry or context)

  * Version (versions of a schema under a subject)

  * Schema (identified by ID, associated with a single or multiple subjects and versions)




For more information on general Google Cloud resource naming, see [Resource names](https://google.aip.dev/122). The schema registry API for Managed Service for Apache Kafka was designed for compatibility with an existing open source API, so some naming conventions might differ from typical API standards.

## Resource naming format

Here are the formats for the different resources:

  * Cluster: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/clusters/{CLUSTER_ID}`

  * Topic: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/clusters/{CLUSTER_ID}/topics/{TOPIC_ID}`

  * Consumer group: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/clusters/{CLUSTER_ID}/consumerGroup/{CONSUMER_GROUP_ID}`

  * ACL: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/clusters/{CLUSTER_ID}/acl/{ACL_ID}`

  * Schema registry: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/schemaRegistries/{SCHEMA_REGISTRY_ID}`

  * Context: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/schemaRegistries/{SCHEMA_REGISTRY_ID}/contexts/{CONTEXT_ID}`

  * Subject:

    * Within default context: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/schemaRegistries/{SCHEMA_REGISTRY_ID}/subjects/{SUBJECT_ID}`
    * Within a specific context: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/schemaRegistries/{SCHEMA_REGISTRY_ID}/contexts/{CONTEXT_ID}/subjects/{SUBJECT_ID}`
  * Schema (identified by ID):

    * Within default context: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/schemaRegistries/{SCHEMA_REGISTRY_ID}/schemas/ids/{SCHEMA_ID}`
    * Within a specific context: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/schemaRegistries/{SCHEMA_REGISTRY_ID}/contexts/{CONTEXT_ID}/schemas/ids/{SCHEMA_ID}`
  * Version (identified by version number under a subject):

    * Within default context: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/schemaRegistries/{SCHEMA_REGISTRY_ID}/subjects/{SUBJECT_ID}/versions/{VERSION_ID}`
    * Within a specific context: `projects/{PROJECT_ID}/locations/{LOCATION_NAME}/schemaRegistries/{SCHEMA_REGISTRY_ID}/contexts/{CONTEXT_ID}/subjects/{SUBJECT_ID}/versions/{VERSION_ID}`



Here's a breakdown of each component in the next sections.

### Project ID

The value must be the project ID or project number, available from the Google Cloud console. For example, `my-cool-project` is a project ID, while `123456789123` is a project number.

### Location

The value must be one of the supported Managed Service for Apache Kafka locations. For a list of available locations, see [Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations).

### ID

`ID` is the final segment in the resource path. Variables such as {CLUSTER_ID}, {TOPIC_ID}, {CONSUMER_GROUP_ID}, {SCHEMA_REGISTRY_ID}, {CONTEXT_ID}, and {SUBJECT_ID} must conform to the following guidelines:

  * Not begin with the string `goog`

  * Start with a letter

  * Length constraints:

    * Cluster IDs: contain between 3 and 53 characters.

    * Topic, Consumer Group IDs: Any length allowed by Apache Kafka. Apache Kafka topic names are limited to 249 characters.

    * Schema registry ID: contains up to 255 characters.

    * Context ID: contains up to 255 characters.

    * Subject ID: contains up to 255 UTF-8 bytes.

  * Character constraints:

    * Cluster IDs: Must match the regex `^[a-z]([-a-z0-9]*[a-z0-9])?`. This means lowercase letters, numbers, and hyphens. It must start with a letter and cannot end with a hyphen.

    * Topic, Consumer Group IDs: Validation is performed by Kafka. The allowed characters are `[a-zA-Z0-9._-], which includes ASCII alphanumerics, periods (.), underscores (_), and dashes (-).

    * Schema registry ID: letters (uppercase or lowercase), numbers, and underscores `_`.

    * Context ID: letters (uppercase or lowercase), numbers, and the following special characters: dashes `-`, periods `.`, underscores `_`, tildes `~`, percents `%`, or plus signs `+`.

    * Subject ID: letters (uppercase or lowercase), numbers, and the following special characters: dashes `-`, periods `.`, underscores `_`, tildes `~`, percents `%`, or plus signs `+`.




## Special characters

You can use the special characters listed in the previous section in resource IDs without URL-encoding. However, you must ensure that any other special character is properly encoded or decoded when used in URLs.

For example, `mi-tópico` is an invalid ID if `ó` is not an allowed character for that specific resource ID type. However, `mi-topico` would be valid if only basic Latin letters are allowed. This format is important when making REST calls.

If you're referencing a topic from the Kafka client libraries, the full resource path is not used. Only the topic name itself is used. Similarly, when interacting with schemas using Kafka client integrations like serializers or deserializers, you typically use the subject name rather than the full resource path.

## Subject naming strategies

When working with schema registry, especially with Kafka client integrations like serializers and deserializers, the subject name is crucial. The subject naming strategy determines how a schema is registered and retrieved from the schema registry. Different strategies offer varying levels of flexibility and control over schema evolution.

You can configure the subject naming strategy by setting the `key.subject.name.strategy` or `value.subject.name.strategy` property in your Kafka client configuration.

### TopicNameStrategy

This is the default strategy for open-source Kafka client libraries.

The subject name is derived directly from the Kafka topic name, appended with `key` for message keys or `value` for message values. If `auto.register.schema` is set to `true`, producer clients use `topicName-value` or `topicName-key` for a topic named `topicName`.

Here are some examples:

  * Topic name: `orders`
  * Subject for message values: `orders-value`
  * Subject for message keys: `orders-key`



The following is a list of advantages for using `TopicNameStrategy`:

  * It's a straightforward strategy, making it a good fit for many use cases.

  * Schemas are tied directly to a topic, allowing you to evolve the record types within a single topic independently.




The following is a list of disadvantages for using `TopicNameStrategy`:

  * Each topic can effectively only handle one type of message that is based on the value schema. This is because the subject name is fixed to the topic name. If you need to send different types of records to the same topic, this strategy won't work.



### RecordNameStrategy

This strategy uses the fully qualified class name of the Avro or Protobuf record as the subject name.

Here are some examples:

  * Avro schema name: `com.example.data.Customer`
  * Protobuf message name: `com.example.data.Order`
  * Subject for `customer` schema: `com.example.data.Customer`
  * Subject for `order` schema: `com.example.data.Order`



The following is a list of advantages for using `RecordNameStrategy`:

  * Since the subject name isn't tied to the topic, you can send different types of records to the same Kafka topic. This is possible as long as each record type has its own unique fully qualified name and corresponding schema registered.

  * A schema for a specific record type such as `com.example.common.Address` can be used across multiple topics, and its evolution is managed centrally under a single subject.




The following is a list of disadvantages for using `RecordNameStrategy`:

  * You must use the same subject and version for all topics that use a particular record type. This can be restrictive if you need different versions of the same record type in different topics.



### TopicRecordNameStrategy

This strategy combines aspects of both `TopicNameStrategy` and `RecordNameStrategy`.

The subject name is a combination of the Kafka topic name and the fully qualified class name of the record, formatted as `TOPIC_NAME-FULLY_QUALIFIED_CLASS_NAME`.

Here are some examples:

  * Topic: `user-events`

  * Fully qualified name: `com.example.events.PageView`

  * Subject name for this combination: `user-events-com.example.events.PageView`

  * Another topic: `product-interactions`

  * Fully qualified name: `com.example.events.PageView`

  * Subject name for this combination: `product-interactions-com.example.events.PageView`


**Note:** `com.example.events.PageView` can evolve differently in `user-events` than in `product-interactions`.

The following is a list of advantages for using `TopicRecordNameStrategy`:

  * Similar to `RecordNameStrategy`, you can send different types of records to the same topic.

  * Unlike `RecordNameStrategy`, this strategy lets you evolve the schema for a specific record type independently within each topic. This means `my-topic-com.example.project.MyRecord` can evolve differently than `another-topic-com.example.project.MyRecord`.




The following is a list of disadvantages for using `TopicRecordNameStrategy`:

  * Subject names can become quite long due to the combination of topic name and fully qualified record name.



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
