---
url: https://docs.cloud.google.com/pubsub/docs/schemas/
title: Schema overview \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:59.894800+00:00
---

# Schema overview  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Schema overview Stay organized with collections  Save and categorize content based on your preferences. 

A Pub/Sub schema is an optional feature that you can use to enforce the format of the [data](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage.FIELDS.bytes.google.pubsub.v1.PubsubMessage.data) field in a Pub/Sub message.

A schema creates a contract between the publisher and subscriber about the format of the messages. Pub/Sub enforces this format. Schemas facilitate inter-team consumption of data streams in your organization by creating a central authority for message types and permissions. A Pub/Sub message schema defines the names and data types for the fields in a message.

You can create a schema and associate it with a topic to enforce the schema for published messages. If a specific message does not conform to the schema, the message is not published. You can also create additional revisions for a schema.

## Types of schemas

You can create a schema in Pub/Sub by using one of the following frameworks:

  * [Apache Avro](https://avro.apache.org/docs/++version++/specification/#schema-declaration)
  * [Protocol Buffer](https://protobuf.dev/)



For example, the following schema defines the inventory of a warehouse, first in the Avro format and then in the Protocol Buffer format.

**Note:** Avro version 1.11 is supported. For Protocol Buffers, proto2 and proto3 are supported.

### Apache Avro format
    
    
    {
     "type" : "record",
     "name" : "Avro",
     "fields" : [
       {
         "name" : "ProductName",
         "type" : "string",
         "default": ""
       },
       {
         "name" : "SKU",
         "type" : "int",
         "default": 0
       },
       {
         "name" : "InStock",
         "type" : "boolean",
         "default": false
       }
     ]
    }
    

**Note:** Pub/Sub does not validate the default value of each field; follow the [Apache Avro specification](https://avro.apache.org/docs/1.11.1/specification/) for default value rules.

### Protocol Buffer format
    
    
    syntax = "proto3";
    message ProtocolBuffer {
      string product_name = 1;
      int32 SKU = 2;
      bool in_stock = 3;
    }
    

## Important information about schemas

The following is some important information regarding creating and managing Pub/Sub schemas.

  * For a schema to work with Pub/Sub, you must define only one top-level [type](https://docs.cloud.google.com/pubsub/docs/schemas#types-schema). Import statements that reference other types are not supported.

  * You can associate the same schema to multiple topics.

  * You can manually test whether a message validates against a schema.

  * Don't include sensitive information such as personally identifiable information (PII) or security data in your schema field names.




## Quotas and limits for schemas

Schemas have the following limits:

  * The schema definition field cannot exceed 300 KB in size.

  * A project can have a maximum of 10,000 schemas.

  * A single schema cannot have more than 20 revisions.

For information about schemas and limits related to Pub/Sub, see [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas).




## What's next

  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas)

  * [Associate a schema with a topic](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic)

  * [Commit a schema revision](https://docs.cloud.google.com/pubsub/docs/commit-schema-revision)

  * [Publish messages to a topic with a schema](https://docs.cloud.google.com/pubsub/docs/publish-topics-schema)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
