---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-MutateRowsRequest-Entry/
title: Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::MutateRowsRequest::Entry (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:38.921156+00:00
---

# Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::MutateRowsRequest::Entry (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-MutateRowsRequest-Entry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::MutateRowsRequest::Entry (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Cloud Bigtable V2 API class Google::Cloud::Bigtable::V2::MutateRowsRequest::Entry.

A mutation for a given row.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #idempotency
    
    
    def idempotency() -> ::Google::Cloud::Bigtable::V2::Idempotency

**Returns**

  * ([::Google::Cloud::Bigtable::V2::Idempotency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Idempotency)) — If set consistently across retries, prevents this mutation from being double applied to aggregate column families within a 15m window. 



### #idempotency=
    
    
    def idempotency=(value) -> ::Google::Cloud::Bigtable::V2::Idempotency

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::V2::Idempotency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Idempotency)) — If set consistently across retries, prevents this mutation from being double applied to aggregate column families within a 15m window. 



**Returns**

  * ([::Google::Cloud::Bigtable::V2::Idempotency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Idempotency)) — If set consistently across retries, prevents this mutation from being double applied to aggregate column families within a 15m window. 



### #mutations
    
    
    def mutations() -> ::Array<::Google::Cloud::Bigtable::V2::Mutation>

**Returns**

  * ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-Array)<[::Google::Cloud::Bigtable::V2::Mutation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Mutation)>) — Required. Changes to be atomically applied to the specified row. Mutations are applied in order, meaning that earlier mutations can be masked by later ones. You must specify at least one mutation. 



### #mutations=
    
    
    def mutations=(value) -> ::Array<::Google::Cloud::Bigtable::V2::Mutation>

**Parameter**

  * **value** ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-Array)<[::Google::Cloud::Bigtable::V2::Mutation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Mutation)>) — Required. Changes to be atomically applied to the specified row. Mutations are applied in order, meaning that earlier mutations can be masked by later ones. You must specify at least one mutation. 



**Returns**

  * ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-Array)<[::Google::Cloud::Bigtable::V2::Mutation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Mutation)>) — Required. Changes to be atomically applied to the specified row. Mutations are applied in order, meaning that earlier mutations can be masked by later ones. You must specify at least one mutation. 



### #row_key
    
    
    def row_key() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The key of the row to which the `mutations` should be applied. 



### #row_key=
    
    
    def row_key=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The key of the row to which the `mutations` should be applied. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The key of the row to which the `mutations` should be applied. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
