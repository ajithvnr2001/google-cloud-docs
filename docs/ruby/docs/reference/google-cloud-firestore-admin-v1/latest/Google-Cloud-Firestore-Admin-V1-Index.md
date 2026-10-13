---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index/
title: Cloud Firestore Admin V1 API - Class Google::Cloud::Firestore::Admin::V1::Index (v1.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:10.545536+00:00
---

# Cloud Firestore Admin V1 API - Class Google::Cloud::Firestore::Admin::V1::Index (v1.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore Admin V1 API - Class Google::Cloud::Firestore::Admin::V1::Index (v1.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.2 (latest)  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.18.0  0.17.1  0.16.0  0.15.0  0.14.3  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Cloud Firestore Admin V1 API class Google::Cloud::Firestore::Admin::V1::Index.

Cloud Firestore indexes enable simple and complex queries against documents in a database.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #api_scope
    
    
    def api_scope() -> ::Google::Cloud::Firestore::Admin::V1::Index::ApiScope

**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::ApiScope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-ApiScope)) — The API scope supported by this index. 



### #api_scope=
    
    
    def api_scope=(value) -> ::Google::Cloud::Firestore::Admin::V1::Index::ApiScope

**Parameter**

  * **value** ([::Google::Cloud::Firestore::Admin::V1::Index::ApiScope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-ApiScope)) — The API scope supported by this index. 



**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::ApiScope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-ApiScope)) — The API scope supported by this index. 



### #density
    
    
    def density() -> ::Google::Cloud::Firestore::Admin::V1::Index::Density

**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::Density](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-Density)) — Immutable. The density configuration of the index. 



### #density=
    
    
    def density=(value) -> ::Google::Cloud::Firestore::Admin::V1::Index::Density

**Parameter**

  * **value** ([::Google::Cloud::Firestore::Admin::V1::Index::Density](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-Density)) — Immutable. The density configuration of the index. 



**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::Density](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-Density)) — Immutable. The density configuration of the index. 



### #fields
    
    
    def fields() -> ::Array<::Google::Cloud::Firestore::Admin::V1::Index::IndexField>

**Returns**

  * (::Array<[::Google::Cloud::Firestore::Admin::V1::Index::IndexField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-IndexField)>) — The fields supported by this index.

For composite indexes, this requires a minimum of 2 and a maximum of 100 fields. The last field entry is always for the field path `__name__`. If, on creation, `__name__` was not specified as the last field, it will be added automatically with the same direction as that of the last field defined. If the final field in a composite index is not directional, the `__name__` will be ordered ASCENDING (unless explicitly specified).

For single field indexes, this will always be exactly one entry with a field path equal to the field path of the associated field. 




### #fields=
    
    
    def fields=(value) -> ::Array<::Google::Cloud::Firestore::Admin::V1::Index::IndexField>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Firestore::Admin::V1::Index::IndexField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-IndexField)>) — The fields supported by this index.

For composite indexes, this requires a minimum of 2 and a maximum of 100 fields. The last field entry is always for the field path `__name__`. If, on creation, `__name__` was not specified as the last field, it will be added automatically with the same direction as that of the last field defined. If the final field in a composite index is not directional, the `__name__` will be ordered ASCENDING (unless explicitly specified).

For single field indexes, this will always be exactly one entry with a field path equal to the field path of the associated field. 




**Returns**

  * (::Array<[::Google::Cloud::Firestore::Admin::V1::Index::IndexField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-IndexField)>) — The fields supported by this index.

For composite indexes, this requires a minimum of 2 and a maximum of 100 fields. The last field entry is always for the field path `__name__`. If, on creation, `__name__` was not specified as the last field, it will be added automatically with the same direction as that of the last field defined. If the final field in a composite index is not directional, the `__name__` will be ordered ASCENDING (unless explicitly specified).

For single field indexes, this will always be exactly one entry with a field path equal to the field path of the associated field. 




### #multikey
    
    
    def multikey() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether the index is multikey. By default, the index is not multikey. For non-multikey indexes, none of the paths in the index definition reach or traverse an array, except via an explicit array index. For multikey indexes, at most one of the paths in the index definition reach or traverse an array, except via an explicit array index. Violations will result in errors.

Note this field only applies to index with MONGODB_COMPATIBLE_API ApiScope. 




### #multikey=
    
    
    def multikey=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether the index is multikey. By default, the index is not multikey. For non-multikey indexes, none of the paths in the index definition reach or traverse an array, except via an explicit array index. For multikey indexes, at most one of the paths in the index definition reach or traverse an array, except via an explicit array index. Violations will result in errors.

Note this field only applies to index with MONGODB_COMPATIBLE_API ApiScope. 




**Returns**

  * (::Boolean) — Optional. Whether the index is multikey. By default, the index is not multikey. For non-multikey indexes, none of the paths in the index definition reach or traverse an array, except via an explicit array index. For multikey indexes, at most one of the paths in the index definition reach or traverse an array, except via an explicit array index. Violations will result in errors.

Note this field only applies to index with MONGODB_COMPATIBLE_API ApiScope. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. A server defined name for this index. The form of this name for composite indexes will be: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{composite_index_id}` For single field indexes, this field will be empty. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. A server defined name for this index. The form of this name for composite indexes will be: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{composite_index_id}` For single field indexes, this field will be empty. 



**Returns**

  * (::String) — Output only. A server defined name for this index. The form of this name for composite indexes will be: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{composite_index_id}` For single field indexes, this field will be empty. 



### #query_scope
    
    
    def query_scope() -> ::Google::Cloud::Firestore::Admin::V1::Index::QueryScope

**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::QueryScope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-QueryScope)) — Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection ID.

Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection ID as this index. 




### #query_scope=
    
    
    def query_scope=(value) -> ::Google::Cloud::Firestore::Admin::V1::Index::QueryScope

**Parameter**

  * **value** ([::Google::Cloud::Firestore::Admin::V1::Index::QueryScope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-QueryScope)) — Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection ID.

Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection ID as this index. 




**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::QueryScope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-QueryScope)) — Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection ID.

Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection ID as this index. 




### #search_index_options
    
    
    def search_index_options() -> ::Google::Cloud::Firestore::Admin::V1::Index::SearchIndexOptions

**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::SearchIndexOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-SearchIndexOptions)) — Optional. Options for search indexes that are at the index definition level. This field is only currently supported for indexes with MONGODB_COMPATIBLE_API ApiScope. 



### #search_index_options=
    
    
    def search_index_options=(value) -> ::Google::Cloud::Firestore::Admin::V1::Index::SearchIndexOptions

**Parameter**

  * **value** ([::Google::Cloud::Firestore::Admin::V1::Index::SearchIndexOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-SearchIndexOptions)) — Optional. Options for search indexes that are at the index definition level. This field is only currently supported for indexes with MONGODB_COMPATIBLE_API ApiScope. 



**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::SearchIndexOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-SearchIndexOptions)) — Optional. Options for search indexes that are at the index definition level. This field is only currently supported for indexes with MONGODB_COMPATIBLE_API ApiScope. 



### #shard_count
    
    
    def shard_count() -> ::Integer

**Returns**

  * (::Integer) — Optional. The number of shards for the index. 



### #shard_count=
    
    
    def shard_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The number of shards for the index. 



**Returns**

  * (::Integer) — Optional. The number of shards for the index. 



### #state
    
    
    def state() -> ::Google::Cloud::Firestore::Admin::V1::Index::State

**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-State)) — Output only. The serving state of the index. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::Firestore::Admin::V1::Index::State

**Parameter**

  * **value** ([::Google::Cloud::Firestore::Admin::V1::Index::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-State)) — Output only. The serving state of the index. 



**Returns**

  * ([::Google::Cloud::Firestore::Admin::V1::Index::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin-v1/latest/Google-Cloud-Firestore-Admin-V1-Index-State)) — Output only. The serving state of the index. 



### #unique
    
    
    def unique() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether it is an unique index. Unique index ensures all values for the indexed field(s) are unique across documents. 



### #unique=
    
    
    def unique=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether it is an unique index. Unique index ensures all values for the indexed field(s) are unique across documents. 



**Returns**

  * (::Boolean) — Optional. Whether it is an unique index. Unique index ensures all values for the indexed field(s) are unique across documents. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
