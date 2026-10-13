---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_insights-v1/latest/Google-Cloud-StorageInsights-V1-DatasetConfig-CloudStorageBuckets-CloudStorageBucket/
title: Storage Insights V1 API - Class Google::Cloud::StorageInsights::V1::DatasetConfig::CloudStorageBuckets::CloudStorageBucket (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:58.741724+00:00
---

# Storage Insights V1 API - Class Google::Cloud::StorageInsights::V1::DatasetConfig::CloudStorageBuckets::CloudStorageBucket (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_insights-v1/latest/Google-Cloud-StorageInsights-V1-DatasetConfig-CloudStorageBuckets-CloudStorageBucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Insights V1 API - Class Google::Cloud::StorageInsights::V1::DatasetConfig::CloudStorageBuckets::CloudStorageBucket (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.7.0  0.6.0  0.5.1  0.4.2  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Storage Insights V1 API class Google::Cloud::StorageInsights::V1::DatasetConfig::CloudStorageBuckets::CloudStorageBucket.

Defines the bucket by its name or a regex pattern to match buckets.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bucket_name
    
    
    def bucket_name() -> ::String

**Returns**

  * (::String) — Cloud Storage bucket name.

Note: The following fields are mutually exclusive: `bucket_name`, `bucket_prefix_regex`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bucket_name=
    
    
    def bucket_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Cloud Storage bucket name.

Note: The following fields are mutually exclusive: `bucket_name`, `bucket_prefix_regex`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Cloud Storage bucket name.

Note: The following fields are mutually exclusive: `bucket_name`, `bucket_prefix_regex`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bucket_prefix_regex
    
    
    def bucket_prefix_regex() -> ::String

**Returns**

  * (::String) — A regex pattern for bucket names matching the regex. Regex should follow the syntax specified in `google/re2` on GitHub.

Note: The following fields are mutually exclusive: `bucket_prefix_regex`, `bucket_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bucket_prefix_regex=
    
    
    def bucket_prefix_regex=(value) -> ::String

**Parameter**

  * **value** (::String) — A regex pattern for bucket names matching the regex. Regex should follow the syntax specified in `google/re2` on GitHub.

Note: The following fields are mutually exclusive: `bucket_prefix_regex`, `bucket_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — A regex pattern for bucket names matching the regex. Regex should follow the syntax specified in `google/re2` on GitHub.

Note: The following fields are mutually exclusive: `bucket_prefix_regex`, `bucket_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
