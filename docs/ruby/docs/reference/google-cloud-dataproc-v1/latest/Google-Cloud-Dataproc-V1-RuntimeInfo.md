---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-RuntimeInfo/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::RuntimeInfo (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:14.200697+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::RuntimeInfo (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-RuntimeInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::RuntimeInfo (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::RuntimeInfo.

Runtime information about workload execution.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #approximate_usage
    
    
    def approximate_usage() -> ::Google::Cloud::Dataproc::V1::UsageMetrics

**Returns**

  * ([::Google::Cloud::Dataproc::V1::UsageMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-UsageMetrics)) — Output only. Approximate workload resource usage, calculated when the workload completes (see [Dataproc Serverless pricing](https://cloud.google.com/dataproc-serverless/pricing)).

**Note:** This metric calculation may change in the future, for example, to capture cumulative workload resource consumption during workload execution (see the [Dataproc Serverless release notes](https://cloud.google.com/dataproc-serverless/docs/release-notes) for announcements, changes, fixes and other Dataproc developments). 




### #current_usage
    
    
    def current_usage() -> ::Google::Cloud::Dataproc::V1::UsageSnapshot

**Returns**

  * ([::Google::Cloud::Dataproc::V1::UsageSnapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-UsageSnapshot)) — Output only. Snapshot of current workload resource usage. 



### #diagnostic_output_uri
    
    
    def diagnostic_output_uri() -> ::String

**Returns**

  * (::String) — Output only. A URI pointing to the location of the diagnostics tarball. 



### #endpoints
    
    
    def endpoints() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Output only. Map of remote access endpoints (such as web interfaces and APIs) to their URIs. 



### #output_uri
    
    
    def output_uri() -> ::String

**Returns**

  * (::String) — Output only. A URI pointing to the location of the stdout and stderr of the workload. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
