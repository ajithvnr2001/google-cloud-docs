---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-RecordKey/
title: Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::RecordKey (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:19.255084+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::RecordKey (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-RecordKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::RecordKey (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API class Google::Cloud::Dlp::V2::RecordKey.

Message for a unique key indicating a record that contains a finding.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #big_query_key
    
    
    def big_query_key() -> ::Google::Cloud::Dlp::V2::BigQueryKey

**Returns**

  * ([::Google::Cloud::Dlp::V2::BigQueryKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-BigQueryKey)) — Datastore key

Note: The following fields are mutually exclusive: `big_query_key`, `datastore_key`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #big_query_key=
    
    
    def big_query_key=(value) -> ::Google::Cloud::Dlp::V2::BigQueryKey

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::BigQueryKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-BigQueryKey)) — Datastore key

Note: The following fields are mutually exclusive: `big_query_key`, `datastore_key`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::BigQueryKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-BigQueryKey)) — Datastore key

Note: The following fields are mutually exclusive: `big_query_key`, `datastore_key`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #datastore_key
    
    
    def datastore_key() -> ::Google::Cloud::Dlp::V2::DatastoreKey

**Returns**

  * ([::Google::Cloud::Dlp::V2::DatastoreKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DatastoreKey)) — BigQuery key

Note: The following fields are mutually exclusive: `datastore_key`, `big_query_key`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #datastore_key=
    
    
    def datastore_key=(value) -> ::Google::Cloud::Dlp::V2::DatastoreKey

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::DatastoreKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DatastoreKey)) — BigQuery key

Note: The following fields are mutually exclusive: `datastore_key`, `big_query_key`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::DatastoreKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DatastoreKey)) — BigQuery key

Note: The following fields are mutually exclusive: `datastore_key`, `big_query_key`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #id_values
    
    
    def id_values() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Values of identifying columns in the given row. Order of values matches the order of `identifying_fields` specified in the scanning request. 



### #id_values=
    
    
    def id_values=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Values of identifying columns in the given row. Order of values matches the order of `identifying_fields` specified in the scanning request. 



**Returns**

  * (::Array<::String>) — Values of identifying columns in the given row. Order of values matches the order of `identifying_fields` specified in the scanning request. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
