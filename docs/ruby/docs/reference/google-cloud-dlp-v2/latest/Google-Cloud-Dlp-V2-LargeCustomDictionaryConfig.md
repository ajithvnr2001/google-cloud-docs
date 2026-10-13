---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-LargeCustomDictionaryConfig/
title: Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::LargeCustomDictionaryConfig (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:50.179055+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::LargeCustomDictionaryConfig (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-LargeCustomDictionaryConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::LargeCustomDictionaryConfig (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API class Google::Cloud::Dlp::V2::LargeCustomDictionaryConfig.

Configuration for a custom dictionary created from a data source of any size up to the maximum size defined in the [limits](https://docs.cloud.google.com/sensitive-data-protection/limits) page. The artifacts of dictionary creation are stored in the specified Cloud Storage location. Consider using `CustomInfoType.Dictionary` for smaller dictionaries that satisfy the size requirements.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #big_query_field
    
    
    def big_query_field() -> ::Google::Cloud::Dlp::V2::BigQueryField

**Returns**

  * ([::Google::Cloud::Dlp::V2::BigQueryField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-BigQueryField)) — Field in a BigQuery table where each cell represents a dictionary phrase.

Note: The following fields are mutually exclusive: `big_query_field`, `cloud_storage_file_set`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #big_query_field=
    
    
    def big_query_field=(value) -> ::Google::Cloud::Dlp::V2::BigQueryField

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::BigQueryField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-BigQueryField)) — Field in a BigQuery table where each cell represents a dictionary phrase.

Note: The following fields are mutually exclusive: `big_query_field`, `cloud_storage_file_set`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::BigQueryField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-BigQueryField)) — Field in a BigQuery table where each cell represents a dictionary phrase.

Note: The following fields are mutually exclusive: `big_query_field`, `cloud_storage_file_set`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloud_storage_file_set
    
    
    def cloud_storage_file_set() -> ::Google::Cloud::Dlp::V2::CloudStorageFileSet

**Returns**

  * ([::Google::Cloud::Dlp::V2::CloudStorageFileSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudStorageFileSet)) — Set of files containing newline-delimited lists of dictionary phrases.

Note: The following fields are mutually exclusive: `cloud_storage_file_set`, `big_query_field`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloud_storage_file_set=
    
    
    def cloud_storage_file_set=(value) -> ::Google::Cloud::Dlp::V2::CloudStorageFileSet

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::CloudStorageFileSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudStorageFileSet)) — Set of files containing newline-delimited lists of dictionary phrases.

Note: The following fields are mutually exclusive: `cloud_storage_file_set`, `big_query_field`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::CloudStorageFileSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudStorageFileSet)) — Set of files containing newline-delimited lists of dictionary phrases.

Note: The following fields are mutually exclusive: `cloud_storage_file_set`, `big_query_field`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #output_path
    
    
    def output_path() -> ::Google::Cloud::Dlp::V2::CloudStoragePath

**Returns**

  * ([::Google::Cloud::Dlp::V2::CloudStoragePath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudStoragePath)) — Location to store dictionary artifacts in Cloud Storage. These files will only be accessible by project owners and the DLP API. If any of these artifacts are modified, the dictionary is considered invalid and can no longer be used. 



### #output_path=
    
    
    def output_path=(value) -> ::Google::Cloud::Dlp::V2::CloudStoragePath

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::CloudStoragePath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudStoragePath)) — Location to store dictionary artifacts in Cloud Storage. These files will only be accessible by project owners and the DLP API. If any of these artifacts are modified, the dictionary is considered invalid and can no longer be used. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::CloudStoragePath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudStoragePath)) — Location to store dictionary artifacts in Cloud Storage. These files will only be accessible by project owners and the DLP API. If any of these artifacts are modified, the dictionary is considered invalid and can no longer be used. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
