---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-LookupEntryRequest/
title: Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::LookupEntryRequest (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:59.741308+00:00
---

# Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::LookupEntryRequest (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-LookupEntryRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::LookupEntryRequest (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.1  2.2.2  2.1.1  2.0.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.2  0.20.1  0.19.0  0.18.1  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1 

Reference documentation and code samples for the Data Catalog V1 API class Google::Cloud::DataCatalog::V1::LookupEntryRequest.

Request message for [LookupEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DataCatalog-Client#Google__Cloud__DataCatalog__V1__DataCatalog__Client_lookup_entry_instance_ "Google::Cloud::DataCatalog::V1::DataCatalog::Client#lookup_entry \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #fully_qualified_name
    
    
    def fully_qualified_name() -> ::String

**Returns**

  * (::String) — [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource.

FQNs take two forms:

    * For non-regionalized resources:

`{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}`

    * For regionalized resources:

`{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}`

Example for a DPMS table:

`dataproc_metastore:{PROJECT_ID}.{LOCATION_ID}.{INSTANCE_ID}.{DATABASE_ID}.{TABLE_ID}`

Note: The following fields are mutually exclusive: `fully_qualified_name`, `linked_resource`, `sql_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #fully_qualified_name=
    
    
    def fully_qualified_name=(value) -> ::String

**Parameter**

  * **value** (::String) — [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource.

FQNs take two forms:

    * For non-regionalized resources:

`{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}`

    * For regionalized resources:

`{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}`

Example for a DPMS table:

`dataproc_metastore:{PROJECT_ID}.{LOCATION_ID}.{INSTANCE_ID}.{DATABASE_ID}.{TABLE_ID}`

Note: The following fields are mutually exclusive: `fully_qualified_name`, `linked_resource`, `sql_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource.

FQNs take two forms:

    * For non-regionalized resources:

`{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}`

    * For regionalized resources:

`{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}`

Example for a DPMS table:

`dataproc_metastore:{PROJECT_ID}.{LOCATION_ID}.{INSTANCE_ID}.{DATABASE_ID}.{TABLE_ID}`

Note: The following fields are mutually exclusive: `fully_qualified_name`, `linked_resource`, `sql_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #linked_resource
    
    
    def linked_resource() -> ::String

**Returns**

  * (::String) — The full name of the Google Cloud Platform resource the Data Catalog entry represents. For more information, see [Full Resource Name](https://cloud.google.com/apis/design/resource_names#full_resource_name).

Full names are case-sensitive. For example:

    * `//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}`
    * `//pubsub.googleapis.com/projects/{PROJECT_ID}/topics/{TOPIC_ID}`

Note: The following fields are mutually exclusive: `linked_resource`, `sql_resource`, `fully_qualified_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #linked_resource=
    
    
    def linked_resource=(value) -> ::String

**Parameter**

  * **value** (::String) — The full name of the Google Cloud Platform resource the Data Catalog entry represents. For more information, see [Full Resource Name](https://cloud.google.com/apis/design/resource_names#full_resource_name).

Full names are case-sensitive. For example:

    * `//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}`
    * `//pubsub.googleapis.com/projects/{PROJECT_ID}/topics/{TOPIC_ID}`

Note: The following fields are mutually exclusive: `linked_resource`, `sql_resource`, `fully_qualified_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The full name of the Google Cloud Platform resource the Data Catalog entry represents. For more information, see [Full Resource Name](https://cloud.google.com/apis/design/resource_names#full_resource_name).

Full names are case-sensitive. For example:

    * `//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}`
    * `//pubsub.googleapis.com/projects/{PROJECT_ID}/topics/{TOPIC_ID}`

Note: The following fields are mutually exclusive: `linked_resource`, `sql_resource`, `fully_qualified_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — Location where the lookup should be performed. Required to lookup entry that is not a part of `DPMS` or `DATAPLEX` `integrated_system` using its `fully_qualified_name`. Ignored in other cases. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — Location where the lookup should be performed. Required to lookup entry that is not a part of `DPMS` or `DATAPLEX` `integrated_system` using its `fully_qualified_name`. Ignored in other cases. 



**Returns**

  * (::String) — Location where the lookup should be performed. Required to lookup entry that is not a part of `DPMS` or `DATAPLEX` `integrated_system` using its `fully_qualified_name`. Ignored in other cases. 



### #project
    
    
    def project() -> ::String

**Returns**

  * (::String) — Project where the lookup should be performed. Required to lookup entry that is not a part of `DPMS` or `DATAPLEX` `integrated_system` using its `fully_qualified_name`. Ignored in other cases. 



### #project=
    
    
    def project=(value) -> ::String

**Parameter**

  * **value** (::String) — Project where the lookup should be performed. Required to lookup entry that is not a part of `DPMS` or `DATAPLEX` `integrated_system` using its `fully_qualified_name`. Ignored in other cases. 



**Returns**

  * (::String) — Project where the lookup should be performed. Required to lookup entry that is not a part of `DPMS` or `DATAPLEX` `integrated_system` using its `fully_qualified_name`. Ignored in other cases. 



### #sql_resource
    
    
    def sql_resource() -> ::String

**Returns**

  * (::String) — The SQL name of the entry. SQL names are case-sensitive.

Examples:

    * `pubsub.topic.{PROJECT_ID}.{TOPIC_ID}`
    * `pubsub.topic.{PROJECT_ID}.```{TOPIC.ID.SEPARATED.WITH.DOTS}``
    * `bigquery.table.{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
    * `bigquery.dataset.{PROJECT_ID}.{DATASET_ID}`
    * `datacatalog.entry.{PROJECT_ID}.{LOCATION_ID}.{ENTRY_GROUP_ID}.{ENTRY_ID}`

Identifiers (`*_ID`) should comply with the [Lexical structure in GoogleSQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical).

Note: The following fields are mutually exclusive: `sql_resource`, `linked_resource`, `fully_qualified_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sql_resource=
    
    
    def sql_resource=(value) -> ::String

**Parameter**

  * **value** (::String) — The SQL name of the entry. SQL names are case-sensitive.

Examples:

    * `pubsub.topic.{PROJECT_ID}.{TOPIC_ID}`
    * `pubsub.topic.{PROJECT_ID}.```{TOPIC.ID.SEPARATED.WITH.DOTS}``
    * `bigquery.table.{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
    * `bigquery.dataset.{PROJECT_ID}.{DATASET_ID}`
    * `datacatalog.entry.{PROJECT_ID}.{LOCATION_ID}.{ENTRY_GROUP_ID}.{ENTRY_ID}`

Identifiers (`*_ID`) should comply with the [Lexical structure in GoogleSQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical).

Note: The following fields are mutually exclusive: `sql_resource`, `linked_resource`, `fully_qualified_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The SQL name of the entry. SQL names are case-sensitive.

Examples:

    * `pubsub.topic.{PROJECT_ID}.{TOPIC_ID}`
    * `pubsub.topic.{PROJECT_ID}.```{TOPIC.ID.SEPARATED.WITH.DOTS}``
    * `bigquery.table.{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
    * `bigquery.dataset.{PROJECT_ID}.{DATASET_ID}`
    * `datacatalog.entry.{PROJECT_ID}.{LOCATION_ID}.{ENTRY_GROUP_ID}.{ENTRY_ID}`

Identifiers (`*_ID`) should comply with the [Lexical structure in GoogleSQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical).

Note: The following fields are mutually exclusive: `sql_resource`, `linked_resource`, `fully_qualified_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
