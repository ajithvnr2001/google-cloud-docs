---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workload_identity-v1/latest/Google-Cloud-WorkloadIdentity-V1-GenerateServiceAgentsRequest/
title: Workload Identity V1 API - Class Google::Cloud::WorkloadIdentity::V1::GenerateServiceAgentsRequest (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:02.654523+00:00
---

# Workload Identity V1 API - Class Google::Cloud::WorkloadIdentity::V1::GenerateServiceAgentsRequest (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workload_identity-v1/latest/Google-Cloud-WorkloadIdentity-V1-GenerateServiceAgentsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Workload Identity V1 API - Class Google::Cloud::WorkloadIdentity::V1::GenerateServiceAgentsRequest (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Workload Identity V1 API class Google::Cloud::WorkloadIdentity::V1::GenerateServiceAgentsRequest.

Message for creating all ServiceAgents for a ServiceProducer in a project and location.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — 

Required. The parent resource. The `location` for the parent resource must be `global`.

Examples:

    * projects/1234/locations/global/serviceProducers/bigquery.googleapis.com
    * folders/2344/locations/global/serviceProducers/vertexai.googleapis.com
    * organizations/3344/locations/global/serviceProducers/iam.googleapis.com



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The parent resource. The `location` for the parent resource must be `global`.

Examples:

    * projects/1234/locations/global/serviceProducers/bigquery.googleapis.com
    * folders/2344/locations/global/serviceProducers/vertexai.googleapis.com
    * organizations/3344/locations/global/serviceProducers/iam.googleapis.com



**Returns**

  * (::String) — 

Required. The parent resource. The `location` for the parent resource must be `global`.

Examples:

    * projects/1234/locations/global/serviceProducers/bigquery.googleapis.com
    * folders/2344/locations/global/serviceProducers/vertexai.googleapis.com
    * organizations/3344/locations/global/serviceProducers/iam.googleapis.com



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
