---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata/
title: Metadata \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:59.493495+00:00
---

# Metadata  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Metadata

Metadata is a key concept in Manufacturing Data Engine (MDE). It represents contextual data about facts. For example, sensor readings or events. Metadata helps answer questions such as the following:

  * What tag emitted a numeric reading?
  * What product was being processed at the time a numeric reading as taken?
  * What device does a sensor belong to?
  * What shift was in progress at the time an event happened?
  * What recipe was active at the time of a reading?



MDE distinguishes between two types of metadata based on their pace of change:

  1. Slowly changing [cloud metadata](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#cloud_metadata).
  2. Rapidly changing [embedded metadata](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#embedded_metadata).



## Cloud metadata

Slowly changing metadata represents contextual data that remains unchanged for an extended period of time, for example, asset context that describes the machine, cell, line, and plant of a given sensor. MDE lets you model, manage and explore your slowly changing metadata and link it to records. After metadata is linked to records, you can explore your records using the associated context.

Slowly changing metadata in MDE is called _cloud metadata_. Cloud metadata serves two functions in the solution:

  1. To contextualize and categorize records.
  2. To serve as a source of versioned master data about manufacturing entities, such as sensors, devices, and lines.



MDE allows cloud metadata to be sourced from the edge, be created manually using the MDE web interface, or be created programmatically using the API. The latter lets you to source metadata from existing Enterprise Asset Management (EAM) or Master Data Management (MDM) systems.

### Metadata buckets

Cloud metadata buckets (also called "buckets" or "metadata buckets") are configuration entities that model a related set of slowly changing contextual data. For example, a bucket can model the attributes of a tag or recipe. Buckets can be thought of as data dimensions in the data analytics domain.

The key attribute of a metadata bucket is its _schema_. The schema (expressed as a JSON schema object) defines and constrains the structure of _metadata instances_ contained within it. You can create a new metadata bucket version, but new versions must adhere to cloud metadata [bucket versioning rules](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#versioning_metadata_buckets).

Buckets are global, this means that they can be referenced by any type.

### Metadata instances

Metadata instances represent the "contents" of cloud metadata buckets. Each instance describes some entity, such as an asset, process or aspect of the records being captured. Instances have two types of identifiers:

  1. A system-generated _UUID_ (Universally Unique Identifier) that identifies the instance within MDE.
  2. A _natural key_ that identifies the entity outside of MDE (for example, a serial number of a sensor).



The metadata instances are versioned on the natural key. That means, MDE keeps track of the evolution of attributes for a given natural key. For example, a tag with a natural key "tag-123" might start off being in cell "X", but later moved to cell "Y". MDE stores and timestamps each instance and gives it a unique UUID. This unique UUID lets you retrieve the history of instances for a natural key, contextualize records with the right instance at ingestion, as well as retroactively apply an instance to past records at query time.

Starting in v1.5.0, metadata instances are versioned and processed based on the `event-time` and not the `processing time`. When you send metadata instances with historical records, MDE versions those metadata instances based on the `eventTimestamp` of the message, and that will enable both historical and recent metadata to co-exist without changing the latest instances. For more information, see [Versioning metadata buckets](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#versioning_metadata_buckets).

MDE only allows adding instances to a bucket that comply with the schema of a specific version of that bucket.

### Metadata bucket schema

Each metadata bucket version contains a schema, and metadata instances can only be added to a specific version of a bucket. Schemas further constrain the structure of metadata instances that can be added to a bucket version.

Metadata bucket schemas are expressed as JSON schema objects in accordance with the [2019-09 version](https://json-schema.org/draft/2019-09) of the JSON schema specification.

For example, if the schema later was added to a bucket version, it would state that the each instance object must have a property called `deviceName` with `string` value, and this property is required. See the following example:
    
    
    {
      "$schema": "https://json-schema.org/draft/2019-09/schema#",
      "type": "object",
      "properties": {
        "deviceName": {
          "type": "string"
        }
      },
      "required": ["deviceName"]
    }
    

**Important:** MDE automatically extends any user-created schema by adding the property `additionalProperties` and setting its value to `false`. This property enforces that buckets won't accept instances that contain properties beyond those explicitly defined by the schema.

#### Metadata instance validation

Metadata instances must comply with the schema defined for a specific metadata bucket version in order to be inserted.

### Types of buckets

MDE defines three types of buckets:

  1. _Tag_ buckets
  2. _Record_ buckets
  3. _Lookup_ buckets



The type of a bucket is defined when its created and can't be changed after.

#### Tag buckets

Tag buckets represent buckets that contextualize tags. This means that the natural key of the instances contained within the bucket must be the tag name.

#### Record buckets

Record buckets represent buckets that can contextualize any group of records that share a common natural key. The natural key of record bucket instances can be any value.

#### Lookup buckets

Lookup buckets represent buckets that don't contextualize records directly, but instead provide reference data that can be used in the parser. The natural key of lookup bucket instances can be any value.

Record bucket instances are never linked to records. Instead, instances can be retrieved from a lookup bucket by calling the [`mde::lookupByKey`](https://docs.cloud.google.com/manufacturing-data-engine/reference/Whistle/Whistle-mde-functions#lookupbykey) function in a Whistle script. The function takes the lookup `bucketName`, `bucketVersion`, and `naturalKey` as arguments, and returns the latest metadata instance for the provided natural key. You can use the instance to populate fields in a proto record in the parser.

### Versioning metadata buckets

The schema of metadata buckets can evolve, however, you must create a new version of a bucket to modify the schema. Existing bucket versions and any existing configuration entities that reference prior versions of a bucket are not impacted by this operation. To ensure data consistency across the lifetime of a metadata bucket, new metadata bucket schemas versions are subject to the following restrictions:

**New versions may:**

  * Add new optional fields.
  * Mark a required field optional.



**New versions may not:**

  * Remove fields.
  * Change data type of existing fields.
  * Mark an optional attribute required.



Starting in v1.5.0, the resolution of the metadata instances is based on event-timestamp as well. This means that MDE resolves the metadata instance that was latest compared to the event time of the record. This generalizes the concept of MDE linking metadata to work across different times which is controlled by the source message. To enhance the query readability of the metadata instances, MDE v1.5.0 introduces a new field called `validFrom` that designates the time when a particular metadata instance is effective. This field is used by MDE to check which metadata instance to pick based on the source message event time.

For example, for a natural-key `sensor-a`, suppose that you send to MDE one metadata instance today with the following value:
    
    
    {
        "naturalKey": "sensor-a",
        "instance": {
            "site": "ONE",
            "factory": "ONE",
            "floor": "ONE",
            "line": "ONE",
            "cell": "ONE"
        }
    }
    
    

MDE versions this instance based on the `eventTimestamp` value of the incoming message, where this metadata instance was sent, and because the timestamp was set to today, then MDE will treat this instance as the absolute latest received so far for that natural key. The value of the `validFrom` for this newly versioned metadata instance will be the value of the `eventTimestamp` value of the incoming message.

Now suppose that you send a historical metadata instance (for example, last year) for the same natural-key `sensor-a` with the following value:
    
    
    {
        "naturalKey": "sensor-a",
        "instance": {
            "site": "OLD",
            "factory": "OLD",
            "floor": "OLD",
            "line": "OLD",
            "cell": "OLD"
        }
    }
    
    

In this example, MDE versions this instance by comparing it to the latest metadata instances that were available at or before the received `eventTimestamp` (for example, last year), and it will insert it into the right place in the timelines, which is the fundamental difference between v.1.4.x and 1.5.0. When MDE receives historical records events, it will resolve the historical metadata entry that was the latest at the event time. The following diagram shows how the processing and linking logic works:

![Versioning metadata logic](https://docs.cloud.google.com/static/manufacturing-data-engine/images/versioning-metadata-buckets.png)

### Linking cloud metadata instances to records

**Note:** Only instances of `TAG` and `RECORD` buckets can be linked to records. `LOOKUP` bucket instances can't be linked to records.

Adding context to a record involves linking a record to a metadata instance. This is accomplished by storing a reference to the UUID of the metadata instance in the record. MDE provides two ways of creating this link in the parser:

  1. By providing an instance's natural key.
  2. By providing a proto metadata instance.



For example, the BigQuery data sink stores references to metadata instances per bucket in a field called `cloud_metadata_ref`. Here is an example of how a metadata instance reference appears in a BigQuery record:
    
    
    {
      "id": "e4b66cb9-7c60-4473-b1a1-1954eca92405",
      "tag_name": "primepaintingrobot-01-airpressure",
      "type_version": "1",
      "event_timestamp": "2023-06-20 07:11:59.757000 UTC",
      "value": "762.53",
      "embedded_metadata": {},
      "materialized_cloud_metadata": {
        "device-metadata": {
          "deviceName": "example-device"
        }
      },
      "cloud_metadata_ref": {
        "device-metadata": {
          "bucket_number": 143,
          "bucket_version": 1,
          "instance_id": "50e156a0-dbd9-4f9b-bdc8-1e77574bc4b1"
        }
      },
      "ingest_timestamp": "2023-06-20 07:12:06.335000 UTC",
      "source_message_id": "8434396321424812"
    }
    

#### Linking a record to a cloud metadata instance using natural key

You can link a record to a metadata instance by providing, in the parser, a reference to a cloud metadata bucket version and the natural key of the instance in the proto record. MDE automatically exchanges the natural key for the instance's UUID, if one exists, and stores the link in the record. If there are multiple instances for the provided natural key, MDE picks the most recent instance (instance with the most recent `created_timestamp`).

If the referenced bucket is a `TAG` bucket, providing a natural key is optional. If the natural key is omitted, MDE uses the value of the `tagName` field by default.

For information about how to link records to metadata instances using a natural key, see [Resolving a metadata `instance_id` by natural key](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-link-records-to-metadata-instances#resolving_a_metadata_instance_id_by_natural_key).

#### Linking a record to a cloud metadata instance using a proto metadata instance

You can link a record to a metadata instance by providing a reference to a cloud metadata bucket version and supplying a proto metadata instance and, optionally, a natural key in the proto record in the parser. This method of linking metadata instances is particularly useful if source messages already contain contextual information to construct a valid proto instance.

Consider the following when linking a record to a cloud metadata instance using a proto metadata instance:

  * If you omit the **natural key** , MDE automatically picks one for you depending on the bucket type.
  * If you omit the **natural key in a proto instance within the context of a`TAG` bucket**, MDE automatically picks the `tagName` as the natural key.
  * If you omit the **natural key in a proto instance within the context of a`RECORD` bucket**, MDE automatically generates a hash value of the message object and uses that as the natural key.
  * If the **supplied proto instance matches the most recent metadata instance for the provided natural key** , MDE exchanges the supplied proto instance for the UUID of the matched instance and stores the UUID in the record.
  * If the **supplied proto instance doesn´t match the most metadata instance for the provided natural key** , MDE creates a new metadata instance for the provided natural key and stores the UUID of the newly created instance in the record. This behavior of the system lets you dynamically populate metadata buckets with instances generated from source messages.



For information about how to link records to metadata instances using a proto metadata instance, see [Resolving a metadata instance ID by instance value](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-link-records-to-metadata-instances#resolving_a_metadata_instance_id_by_instance_value).

### Instance materialization

Instead of just storing the UUID of a metadata instance, records can optionally include the entire instance itself. This is called materialization. This behavior can be configured for each sink at the type level, by setting the value of the `materializeCloudMetadata` field for a sink to `true`.

For example, enabling metadata materialization for the BigQuery sink will produce a row like the following for a record that contains a metadata instance reference:
    
    
    {
      "id": "e4b66cb9-7c60-4473-b1a1-1954eca92405",
      "tag_name": "primepaintingrobot-01-airpressure",
      "type_version": "1",
      "event_timestamp": "2023-06-20 07:11:59.757000 UTC",
      "value": "762.53",
      "embedded_metadata": {},
      "materialized_cloud_metadata": {
         "tag":{
           "bucket_number":143,
           "bucket_version":1,
           "instance":{
             "datatype":"float",
             "deviceID":"ppr-01",
             "deviceName":"primepaintingrobot-01",
             "vendor":"KUKA"
           }
         }
      },
      "cloud_metadata_ref": {
        "device-metadata": {
          "bucket_number": 143,
          "bucket_version": 1,
          "instance_id": "50e156a0-dbd9-4f9b-bdc8-1e77574bc4b1"
        }
      },
      "ingest_timestamp": "2023-06-20 07:12:06.335000 UTC",
      "source_message_id": "8434396321424812"
    }
    

## Embedded metadata

Rapidly changing metadata represents contextual data that changes at a fast pace. Typical examples for rapidly changing metadata include counters and IDs that are auto-incremented, for example, serial numbers or transaction IDs.

MDE lets you to structure, harmonize, and transform rapidly changing metadata using Whistle, and embed it directly in the record by populating a field called `embeddedMetadata` in the proto record in the [parser](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/parser).

All the supported MDE data sinks make embedded metadata available. For example, populating the `embeddedMetadata` field in the proto record in the parser would produce a row like this one for the resulting record in BigQuery:
    
    
    {
      "id": "e4b66cb9-7c60-4473-b1a1-1954eca92405",
      "tag_name": "primepaintingrobot-01-airpressure",
      "type_version": "1",
      "event_timestamp": "2023-06-20 07:11:59.757000 UTC",
      "value": "762.53",
      "embedded_metadata": {
        "transactionNumber": "1234"
      },
      "materialized_cloud_metadata": {},
      "cloud_metadata_ref": {},
      "ingest_timestamp": "2023-06-20 07:12:06.335000 UTC",
      "source_message_id": "8434396321424812"
    }
    

## Metadata automatic deletion

For both, the record and tag metadata, MDE keeps track of the changes happening in each natural-key by comparing every new instance against the old instance. When there is a change in any of the instance attributes, MDE creates a new version and marks it as the _latest_ effective instance. By design, the tag and record metadata are expected to be in the granularity of thousands and less than hundred thousand. These restrictions allow MDE to index the metadata instances as they come from the edge or the API without impacting the processing throughput.

Sometimes due to a configuration errors, the parser will inject a high cardinality field like a timestamp in the metadata instance, which results in a quick proliferation of versions for each natural-key. After a certain threshold, this negatively impacts the performance of the ingestion. In some cases it might lead to a stop of the processing altogether until the underlying cloud infrastructure services are scaled by the solution administrator.

From v1.4.0 MDE enforces a maximum number of instances per natural-key to ensure a consistent performance. When the natural-keys number approach this threshold (default is 200), MDE will send warning to the new notifications API to inform the user of the natural-keys that a have high number of metadata instance versions. When the natural-keys instance size breaches the threshold, MDE will delete the old instances from the internal store automatically. It will also send another notification to the Notifications API informing the user of the natural-keys that have been deleted.

Both the warning and the deletion activities are also reported in the log which could be used to create an alert policy on the project Cloud Monitoring.

**Note:** The deletion is happening in the internal MDE stores and not in the target sinks such as BigQuery. MDE already sends a new record in the BigQuery sink whenever a new metadata instance is created so the user still has the option to query the historical changes of the metadata. The linked fact records in the type won't be impacted as they will refer to the historical metadata instances in the BigQuery sink.

### Naming restrictions for Metadata Buckets

A Metadata Bucket name can contain the following:

  * Letters (uppercase and lowercase), numbers and the special characters `-` and `_`.
  * Can be up to 255 characters long.



You can use the following regular expression for validation: `^[a-z][a-z0-9\\-_]{1,255}$`.

If you try to create an entity violating the naming restrictions you will get a `400 error`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
