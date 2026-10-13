---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1
title: Package com.google.events.cloud.datastore.v1 (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:27.833842+00:00
---

# Package com.google.events.cloud.datastore.v1 (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.events.cloud.datastore.v1 (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.datastore.v1)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.datastore.v1)



## Classes 

### [ArrayValue](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.ArrayValue)

An array value.

Protobuf type `google.events.cloud.datastore.v1.ArrayValue`

### [ArrayValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.ArrayValue.Builder)

An array value.

Protobuf type `google.events.cloud.datastore.v1.ArrayValue`

### [Data](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Data)

### [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Entity)

A Datastore data object. Must not exceed 1 MiB - 4 bytes.

Protobuf type `google.events.cloud.datastore.v1.Entity`

### [Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Entity.Builder)

A Datastore data object. Must not exceed 1 MiB - 4 bytes.

Protobuf type `google.events.cloud.datastore.v1.Entity`

### [EntityEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.EntityEventData)

The data within all Firestore in Datastore Mode entity events.

Protobuf type `google.events.cloud.datastore.v1.EntityEventData`

### [EntityEventData.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.EntityEventData.Builder)

The data within all Firestore in Datastore Mode entity events.

Protobuf type `google.events.cloud.datastore.v1.EntityEventData`

### [EntityResult](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.EntityResult)

The result of fetching an entity from Datastore.

Protobuf type `google.events.cloud.datastore.v1.EntityResult`

### [EntityResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.EntityResult.Builder)

The result of fetching an entity from Datastore.

Protobuf type `google.events.cloud.datastore.v1.EntityResult`

### [Key](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Key)

A unique identifier for an entity. If a key's partition ID or any of its path kinds or names are reserved/read-only, the key is reserved/read-only. A reserved/read-only key is forbidden in certain documented contexts.

Protobuf type `google.events.cloud.datastore.v1.Key`

### [Key.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Key.Builder)

A unique identifier for an entity. If a key's partition ID or any of its path kinds or names are reserved/read-only, the key is reserved/read-only. A reserved/read-only key is forbidden in certain documented contexts.

Protobuf type `google.events.cloud.datastore.v1.Key`

### [Key.PathElement](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Key.PathElement)

A (kind, ID/name) pair used to construct a key path. If either name or ID is set, the element is complete. If neither is set, the element is incomplete.

Protobuf type `google.events.cloud.datastore.v1.Key.PathElement`

### [Key.PathElement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Key.PathElement.Builder)

A (kind, ID/name) pair used to construct a key path. If either name or ID is set, the element is complete. If neither is set, the element is incomplete.

Protobuf type `google.events.cloud.datastore.v1.Key.PathElement`

### [PartitionId](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.PartitionId)

A partition ID identifies a grouping of entities. The grouping is always by project and namespace, however the namespace ID may be empty. A partition ID contains several dimensions: project ID and namespace ID. Partition dimensions:

  * May be `""`.
  * Must be valid UTF-8 bytes.
  * Must have values that match regex `[A-Za-z\d\.\-_]{1,100}_` If the value of any dimension matches regex `_.*__`, the partition is reserved/read-only. A reserved/read-only partition ID is forbidden in certain documented contexts. Foreign partition IDs (in which the project ID does not match the context project ID ) are discouraged. Reads and writes of foreign partition IDs may fail if the project is not in an active state.



Protobuf type `google.events.cloud.datastore.v1.PartitionId`

### [PartitionId.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.PartitionId.Builder)

A partition ID identifies a grouping of entities. The grouping is always by project and namespace, however the namespace ID may be empty. A partition ID contains several dimensions: project ID and namespace ID. Partition dimensions:

  * May be `""`.
  * Must be valid UTF-8 bytes.
  * Must have values that match regex `[A-Za-z\d\.\-_]{1,100}_` If the value of any dimension matches regex `_.*__`, the partition is reserved/read-only. A reserved/read-only partition ID is forbidden in certain documented contexts. Foreign partition IDs (in which the project ID does not match the context project ID ) are discouraged. Reads and writes of foreign partition IDs may fail if the project is not in an active state.



Protobuf type `google.events.cloud.datastore.v1.PartitionId`

### [PropertyMask](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.PropertyMask)

A set of property paths on an entity.

Protobuf type `google.events.cloud.datastore.v1.PropertyMask`

### [PropertyMask.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.PropertyMask.Builder)

A set of property paths on an entity.

Protobuf type `google.events.cloud.datastore.v1.PropertyMask`

### [Value](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Value)

A message that can hold any of the supported value types and associated metadata.

Protobuf type `google.events.cloud.datastore.v1.Value`

### [Value.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Value.Builder)

A message that can hold any of the supported value types and associated metadata.

Protobuf type `google.events.cloud.datastore.v1.Value`

## Interfaces 

### [ArrayValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.ArrayValueOrBuilder)

### [EntityEventDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.EntityEventDataOrBuilder)

### [EntityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.EntityOrBuilder)

### [EntityResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.EntityResultOrBuilder)

### [Key.PathElementOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Key.PathElementOrBuilder)

### [KeyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.KeyOrBuilder)

### [PartitionIdOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.PartitionIdOrBuilder)

### [PropertyMaskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.PropertyMaskOrBuilder)

### [ValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.ValueOrBuilder)

## Enums 

### [EntityResult.ResultType](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.EntityResult.ResultType)

Specifies what data the 'entity' field contains. A `ResultType` is either implied (for example, in `LookupResponse.missing` from `datastore.proto`, it is always `KEY_ONLY`) or specified by context (for example, in message `QueryResultBatch`, field `entity_result_type` specifies a `ResultType` for all the values in field `entity_results`).

Protobuf enum `google.events.cloud.datastore.v1.EntityResult.ResultType`

### [Key.PathElement.IdTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Key.PathElement.IdTypeCase)

### [Value.ValueTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastore.v1.Value.ValueTypeCase)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
