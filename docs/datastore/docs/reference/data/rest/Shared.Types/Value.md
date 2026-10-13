---
url: https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value/
title: Value \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:31.711361+00:00
---

# Value  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Reference ](https://docs.cloud.google.com/datastore/docs/apis)



Send feedback 

#  Value Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Key
    * JSON representation
  * PartitionId
    * JSON representation
  * PathElement
    * JSON representation
  * Entity
    * JSON representation



A message that can hold any of the supported value types and associated metadata.

JSON representation  
---  
      
    
    {
      "meaning": integer,
      "excludeFromIndexes": boolean,
    
      // Union field value_type can be only one of the following:
      "nullValue": null,
      "booleanValue": boolean,
      "integerValue": string,
      "doubleValue": number,
      "timestampValue": string,
      "keyValue": {
        object ([Key](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#Key))
      },
      "stringValue": string,
      "blobValue": string,
      "geoPointValue": {
        object ([LatLng](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/LatLng))
      },
      "entityValue": {
        object ([Entity](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#Entity))
      },
      "arrayValue": {
        object ([ArrayValue](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/ArrayValue))
      }
      // End of list of possible types for union field value_type.
    }  
  
Fields  
---  
`meaning` |  `integer` The `meaning` field should only be populated for backwards compatibility.  
`excludeFromIndexes` |  `boolean` If the value should be excluded from all indexes including those defined explicitly.  
Union field `value_type`. Must have a value set. `value_type` can be only one of the following:  
`nullValue` |  `null` A null value.  
`booleanValue` |  `boolean` A boolean value.  
`integerValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` An integer value.  
`doubleValue` |  `number` A double value.  
`timestampValue` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` A timestamp value. When stored in the Datastore, precise only to microseconds; any additional precision is rounded down.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`keyValue` |  `object (`[Key](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#Key)`)` A key value.  
`stringValue` |  `string` A UTF-8 encoded string value. When `excludeFromIndexes` is false (it is indexed) , may have at most 1500 bytes. Otherwise, may be set to at most 1,000,000 bytes.  
`blobValue` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A blob value. May have at most 1,000,000 bytes. When `excludeFromIndexes` is false, may have at most 1500 bytes. In JSON requests, must be base64-encoded.A base64-encoded string.  
`geoPointValue` |  `object (`[LatLng](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/LatLng)`)` A geo point value representing a point on the surface of Earth.  
`entityValue` |  `object (`[Entity](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#Entity)`)` An entity value.

  * May have no key.
  * May have a key with an incomplete key path.
  * May have a reserved/read-only key.

  
`arrayValue` |  `object (`[ArrayValue](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/ArrayValue)`)` An array value. Cannot contain another array value. A `Value` instance that sets field `arrayValue` must not set fields `meaning` or `excludeFromIndexes`.  
  
## Key

A unique identifier for an entity. If a key's partition ID or any of its path kinds or names are reserved/read-only, the key is reserved/read-only. A reserved/read-only key is forbidden in certain documented contexts.

JSON representation  
---  
      
    
    {
      "partitionId": {
        object ([PartitionId](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#PartitionId))
      },
      "path": [
        {
          object ([PathElement](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#PathElement))
        }
      ]
    }  
  
Fields  
---  
`partitionId` |  `object (`[PartitionId](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#PartitionId)`)` Entities are partitioned into subsets, currently identified by a project ID and namespace ID. Queries are scoped to a single partition.  
`path[]` |  `object (`[PathElement](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#PathElement)`)` The entity path. An entity path consists of one or more elements composed of a kind and a string or numerical identifier, which identify entities. The first element identifies a _root entity_ , the second element identifies a _child_ of the root entity, the third element identifies a child of the second entity, and so forth. The entities identified by all prefixes of the path are called the element's _ancestors_.An entity path is always fully complete: _all_ of the entity's ancestors are required to be in the path along with the entity identifier itself. The only exception is that in some documented cases, the identifier in the last path element (for the entity) itself may be omitted. For example, the last path element of the key of `Mutation.insert` may have no identifier.A path can never be empty, and a path can have at most 100 elements.  
  
## PartitionId

A partition ID identifies a grouping of entities. The grouping is always by project and namespace, however the namespace ID may be empty.

A partition ID contains several dimensions: project ID and namespace ID.

Partition dimensions:

  * May be `""`.
  * Must be valid UTF-8 bytes.
  * Must have values that match regex `[A-Za-z\d\.\-_]{1,100}` If the value of any dimension matches regex `__.*__`, the partition is reserved/read-only. A reserved/read-only partition ID is forbidden in certain documented contexts.



Foreign partition IDs (in which the project ID does not match the context project ID ) are discouraged. Reads and writes of foreign partition IDs may fail if the project is not in an active state.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "databaseId": string,
      "namespaceId": string
    }  
  
Fields  
---  
`projectId` |  `string` The ID of the project to which the entities belong.  
`databaseId` |  `string` If not empty, the ID of the database to which the entities belong.  
`namespaceId` |  `string` If not empty, the ID of the namespace to which the entities belong.  
  
## PathElement

A (kind, ID/name) pair used to construct a key path.

If either name or ID is set, the element is complete. If neither is set, the element is incomplete.

JSON representation  
---  
      
    
    {
      "kind": string,
    
      // Union field id_type can be only one of the following:
      "id": string,
      "name": string
      // End of list of possible types for union field id_type.
    }  
  
Fields  
---  
`kind` |  `string` The kind of the entity.A kind matching regex `__.*__` is reserved/read-only. A kind must not contain more than 1500 bytes when UTF-8 encoded. Cannot be `""`.Must be valid UTF-8 bytes. Legacy values that are not valid UTF-8 are encoded as `__bytes<X>__` where `<X>` is the base-64 encoding of the bytes.  
Union field `id_type`. The type of ID. `id_type` can be only one of the following:  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The auto-allocated ID of the entity.Never equal to zero. Values less than zero are discouraged and may not be supported in the future.  
`name` |  `string` The name of the entity.A name matching regex `__.*__` is reserved/read-only. A name must not be more than 1500 bytes when UTF-8 encoded. Cannot be `""`.Must be valid UTF-8 bytes. Legacy values that are not valid UTF-8 are encoded as `__bytes<X>__` where `<X>` is the base-64 encoding of the bytes.  
  
## Entity

A Datastore data object.

Must not exceed 1 MiB - 4 bytes.

JSON representation  
---  
      
    
    {
      "key": {
        object ([Key](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#Key))
      },
      "properties": {
        string: {
          object ([Value](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value))
        },
        ...
      }
    }  
  
Fields  
---  
`key` |  `object (`[Key](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value#Key)`)` The entity's key.An entity must have a key, unless otherwise documented (for example, an entity in `Value.entity_value` may have no key). An entity's kind is its key path's last element's kind, or null if it has no key.  
`properties` |  `map (key: string, value: object (`[Value](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value)`))` The entity's properties. The map's keys are property names. A property name matching regex `__.*__` is reserved. A reserved property name is forbidden in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-08 UTC."],[],[]] 
