---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SpannerDatabaseReference/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:52.527912+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SpannerDatabaseReference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference.

Message representing a reference to a single Spanner database.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #database_id
    
    
    def database_id() -> ::String

**Returns**

  * (::String) — Required. The database id. 



### #database_id=
    
    
    def database_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The database id. 



**Returns**

  * (::String) — Required. The database id. 



### #database_table_references
    
    
    def database_table_references() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::DatabaseTableReference>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::DatabaseTableReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DatabaseTableReference)>) — Optional. References to tables within the database. Each reference specifies a table and can optionally include the table's schema to provide context for the query. 



### #database_table_references=
    
    
    def database_table_references=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::DatabaseTableReference>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::DatabaseTableReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DatabaseTableReference)>) — Optional. References to tables within the database. Each reference specifies a table and can optionally include the table's schema to provide context for the query. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::DatabaseTableReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DatabaseTableReference)>) — Optional. References to tables within the database. Each reference specifies a table and can optionally include the table's schema to provide context for the query. 



### #engine
    
    
    def engine() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference::Engine

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference::Engine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SpannerDatabaseReference-Engine)) — Required. The engine of the Spanner instance. 



### #engine=
    
    
    def engine=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference::Engine

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference::Engine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SpannerDatabaseReference-Engine)) — Required. The engine of the Spanner instance. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::SpannerDatabaseReference::Engine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SpannerDatabaseReference-Engine)) — Required. The engine of the Spanner instance. 



### #instance_id
    
    
    def instance_id() -> ::String

**Returns**

  * (::String) — Required. The instance id. 



### #instance_id=
    
    
    def instance_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The instance id. 



**Returns**

  * (::String) — Required. The instance id. 



### #priority
    
    
    def priority() -> ::String

**Returns**

  * (::String) — Optional. Priority for the queries to Spanner. Should be a value supported by Cloud Spanner e.g.: LOW, MEDIUM, HIGH. Unsupported values will be ignored. See https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#Priority for complete list. 



### #priority=
    
    
    def priority=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Priority for the queries to Spanner. Should be a value supported by Cloud Spanner e.g.: LOW, MEDIUM, HIGH. Unsupported values will be ignored. See https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#Priority for complete list. 



**Returns**

  * (::String) — Optional. Priority for the queries to Spanner. Should be a value supported by Cloud Spanner e.g.: LOW, MEDIUM, HIGH. Unsupported values will be ignored. See https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#Priority for complete list. 



### #project_id
    
    
    def project_id() -> ::String

**Returns**

  * (::String) — Required. The project the instance belongs to. 



### #project_id=
    
    
    def project_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The project the instance belongs to. 



**Returns**

  * (::String) — Required. The project the instance belongs to. 



### #request_tag
    
    
    def request_tag() -> ::String

**Returns**

  * (::String) — Tag to be attached to all queries to Spanner. Allows to identify and monitor queries sent to Spanner by the GDA service. 



### #request_tag=
    
    
    def request_tag=(value) -> ::String

**Parameter**

  * **value** (::String) — Tag to be attached to all queries to Spanner. Allows to identify and monitor queries sent to Spanner by the GDA service. 



**Returns**

  * (::String) — Tag to be attached to all queries to Spanner. Allows to identify and monitor queries sent to Spanner by the GDA service. 



### #table_ids
    
    
    def table_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The table ids. Denotes all tables if unset. 



### #table_ids=
    
    
    def table_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The table ids. Denotes all tables if unset. 



**Returns**

  * (::Array<::String>) — Optional. The table ids. Denotes all tables if unset. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
