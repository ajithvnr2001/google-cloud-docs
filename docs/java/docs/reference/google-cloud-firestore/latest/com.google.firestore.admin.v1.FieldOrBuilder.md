---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.FieldOrBuilder
title: Interface FieldOrBuilder (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:54.996081+00:00
---

# Interface FieldOrBuilder (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.FieldOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FieldOrBuilder (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public interface FieldOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIndexConfig()
    
    
    public abstract Field.IndexConfig getIndexConfig()

The index configuration for this field. If unset, field indexing will revert to the configuration defined by the `ancestor_field`. To explicitly remove all indexes for this field, specify an index config with an empty list of indexes.

`.google.firestore.admin.v1.Field.IndexConfig index_config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Field.IndexConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field.IndexConfig)` | The indexConfig.  
  
### getIndexConfigOrBuilder()
    
    
    public abstract Field.IndexConfigOrBuilder getIndexConfigOrBuilder()

The index configuration for this field. If unset, field indexing will revert to the configuration defined by the `ancestor_field`. To explicitly remove all indexes for this field, specify an index config with an empty list of indexes.

`.google.firestore.admin.v1.Field.IndexConfig index_config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Field.IndexConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field.IndexConfigOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Required. A field name of the form: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}`

A field path can be a simple field name, e.g. `address` or a path to fields within `map_value` , e.g. `address.city`, or a special field path. The only valid special field is `*`, which represents any field.

Field paths can be quoted using `` ` `` (backtick). The only character that must be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include: `*`, `.`, `` ` `` (backtick), `[`, `]`, as well as any ascii symbolic characters.``

`` ``

`` Examples: `` `address.city` `` represents a field named `address.city`, not the map key `city` in the field `address`. `` `_``` represents a field named `_`, not any field.``

`` ``

`` A special `Field` contains the default indexing settings for all fields. This field's resource name is: `projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/*` Indexes defined on this `Field` will be applied to all fields which do not have their own `Field` index configuration.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. A field name of the form: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}`

A field path can be a simple field name, e.g. `address` or a path to fields within `map_value` , e.g. `address.city`, or a special field path. The only valid special field is `*`, which represents any field.

Field paths can be quoted using `` ` `` (backtick). The only character that must be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include: `*`, `.`, `` ` `` (backtick), `[`, `]`, as well as any ascii symbolic characters.``

`` ``

`` Examples: `` `address.city` `` represents a field named `address.city`, not the map key `city` in the field `address`. `` `_``` represents a field named `_`, not any field.``

`` ``

`` A special `Field` contains the default indexing settings for all fields. This field's resource name is: `projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/*` Indexes defined on this `Field` will be applied to all fields which do not have their own `Field` index configuration.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getTtlConfig()
    
    
    public abstract Field.TtlConfig getTtlConfig()

The TTL configuration for this `Field`. Setting or unsetting this will enable or disable the TTL for documents that have this `Field`.

`.google.firestore.admin.v1.Field.TtlConfig ttl_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Field.TtlConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field.TtlConfig)` | The ttlConfig.  
  
### getTtlConfigOrBuilder()
    
    
    public abstract Field.TtlConfigOrBuilder getTtlConfigOrBuilder()

The TTL configuration for this `Field`. Setting or unsetting this will enable or disable the TTL for documents that have this `Field`.

`.google.firestore.admin.v1.Field.TtlConfig ttl_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Field.TtlConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field.TtlConfigOrBuilder)` |   
  
### hasIndexConfig()
    
    
    public abstract boolean hasIndexConfig()

The index configuration for this field. If unset, field indexing will revert to the configuration defined by the `ancestor_field`. To explicitly remove all indexes for this field, specify an index config with an empty list of indexes.

`.google.firestore.admin.v1.Field.IndexConfig index_config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the indexConfig field is set.  
  
### hasTtlConfig()
    
    
    public abstract boolean hasTtlConfig()

The TTL configuration for this `Field`. Setting or unsetting this will enable or disable the TTL for documents that have this `Field`.

`.google.firestore.admin.v1.Field.TtlConfig ttl_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ttlConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
