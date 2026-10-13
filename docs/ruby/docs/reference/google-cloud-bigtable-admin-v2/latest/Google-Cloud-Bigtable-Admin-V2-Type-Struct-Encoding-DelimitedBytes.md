---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-Struct-Encoding-DelimitedBytes/
title: Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Type::Struct::Encoding::DelimitedBytes (v1.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:12.628258+00:00
---

# Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Type::Struct::Encoding::DelimitedBytes (v1.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-Struct-Encoding-DelimitedBytes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Type::Struct::Encoding::DelimitedBytes (v1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.3  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.1 

Reference documentation and code samples for the Cloud Bigtable Admin V2 API class Google::Cloud::Bigtable::Admin::V2::Type::Struct::Encoding::DelimitedBytes.

Fields are encoded independently and concatenated with a configurable `delimiter` in between.

A struct with no fields defined is encoded as a single `delimiter`.

Sorted mode:

  * Fields are encoded in sorted mode.
  * Encoded field values must not contain any bytes <= `delimiter[0]`
  * Element-wise order is preserved: `A < B` if `A[0] < B[0]`, or if `A[0] == B[0] && A[1] < B[1]`, etc. Strict prefixes sort first.



Distinct mode:

  * Fields are encoded in distinct mode.
  * Encoded field values must not contain `delimiter[0]`.



## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #delimiter
    
    
    def delimiter() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — Byte sequence used to delimit concatenated fields. The delimiter must contain at least 1 character and at most 50 characters. 



### #delimiter=
    
    
    def delimiter=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — Byte sequence used to delimit concatenated fields. The delimiter must contain at least 1 character and at most 50 characters. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — Byte sequence used to delimit concatenated fields. The delimiter must contain at least 1 character and at most 50 characters. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
