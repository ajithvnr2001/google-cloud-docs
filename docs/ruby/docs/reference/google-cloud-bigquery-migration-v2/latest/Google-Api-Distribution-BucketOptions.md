---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions/
title: BigQuery Migration V2 API - Class Google::Api::Distribution::BucketOptions (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:53.073722+00:00
---

# BigQuery Migration V2 API - Class Google::Api::Distribution::BucketOptions (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Api::Distribution::BucketOptions (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Api::Distribution::BucketOptions.

`BucketOptions` describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. `BucketOptions` does not include the number of values in each bucket.

A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #explicit_buckets
    
    
    def explicit_buckets() -> ::Google::Api::Distribution::BucketOptions::Explicit

**Returns**

  * ([::Google::Api::Distribution::BucketOptions::Explicit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Explicit)) — The explicit buckets.

Note: The following fields are mutually exclusive: `explicit_buckets`, `linear_buckets`, `exponential_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #explicit_buckets=
    
    
    def explicit_buckets=(value) -> ::Google::Api::Distribution::BucketOptions::Explicit

**Parameter**

  * **value** ([::Google::Api::Distribution::BucketOptions::Explicit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Explicit)) — The explicit buckets.

Note: The following fields are mutually exclusive: `explicit_buckets`, `linear_buckets`, `exponential_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Api::Distribution::BucketOptions::Explicit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Explicit)) — The explicit buckets.

Note: The following fields are mutually exclusive: `explicit_buckets`, `linear_buckets`, `exponential_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #exponential_buckets
    
    
    def exponential_buckets() -> ::Google::Api::Distribution::BucketOptions::Exponential

**Returns**

  * ([::Google::Api::Distribution::BucketOptions::Exponential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Exponential)) — The exponential buckets.

Note: The following fields are mutually exclusive: `exponential_buckets`, `linear_buckets`, `explicit_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #exponential_buckets=
    
    
    def exponential_buckets=(value) -> ::Google::Api::Distribution::BucketOptions::Exponential

**Parameter**

  * **value** ([::Google::Api::Distribution::BucketOptions::Exponential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Exponential)) — The exponential buckets.

Note: The following fields are mutually exclusive: `exponential_buckets`, `linear_buckets`, `explicit_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Api::Distribution::BucketOptions::Exponential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Exponential)) — The exponential buckets.

Note: The following fields are mutually exclusive: `exponential_buckets`, `linear_buckets`, `explicit_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #linear_buckets
    
    
    def linear_buckets() -> ::Google::Api::Distribution::BucketOptions::Linear

**Returns**

  * ([::Google::Api::Distribution::BucketOptions::Linear](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Linear)) — The linear bucket.

Note: The following fields are mutually exclusive: `linear_buckets`, `exponential_buckets`, `explicit_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #linear_buckets=
    
    
    def linear_buckets=(value) -> ::Google::Api::Distribution::BucketOptions::Linear

**Parameter**

  * **value** ([::Google::Api::Distribution::BucketOptions::Linear](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Linear)) — The linear bucket.

Note: The following fields are mutually exclusive: `linear_buckets`, `exponential_buckets`, `explicit_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Api::Distribution::BucketOptions::Linear](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-BucketOptions-Linear)) — The linear bucket.

Note: The following fields are mutually exclusive: `linear_buckets`, `exponential_buckets`, `explicit_buckets`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
