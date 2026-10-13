---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce-consumer-procurement-v1/latest/Google-Cloud-Commerce-Consumer-Procurement-V1-AssignmentProtocol-AutoAssignmentType/
title: Cloud Commerce Consumer Procurement V1 API - Class Google::Cloud::Commerce::Consumer::Procurement::V1::AssignmentProtocol::AutoAssignmentType (v1.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:44.005554+00:00
---

# Cloud Commerce Consumer Procurement V1 API - Class Google::Cloud::Commerce::Consumer::Procurement::V1::AssignmentProtocol::AutoAssignmentType (v1.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce-consumer-procurement-v1/latest/Google-Cloud-Commerce-Consumer-Procurement-V1-AssignmentProtocol-AutoAssignmentType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Commerce Consumer Procurement V1 API - Class Google::Cloud::Commerce::Consumer::Procurement::V1::AssignmentProtocol::AutoAssignmentType (v1.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.0 (latest)  1.9.1  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.2  0.4.0  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Commerce Consumer Procurement V1 API class Google::Cloud::Commerce::Consumer::Procurement::V1::AssignmentProtocol::AutoAssignmentType.

Configuration for automatic assignments handled by data plane operations.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #inactive_license_ttl
    
    
    def inactive_license_ttl() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce-consumer-procurement-v1/latest/Google-Protobuf-Duration)) — Optional. The time to live for an inactive license. After this time has passed, the license will be automatically unassigned from the user. Must be at least 7 days, if set. If unset, the license will never expire. 



### #inactive_license_ttl=
    
    
    def inactive_license_ttl=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce-consumer-procurement-v1/latest/Google-Protobuf-Duration)) — Optional. The time to live for an inactive license. After this time has passed, the license will be automatically unassigned from the user. Must be at least 7 days, if set. If unset, the license will never expire. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce-consumer-procurement-v1/latest/Google-Protobuf-Duration)) — Optional. The time to live for an inactive license. After this time has passed, the license will be automatically unassigned from the user. Must be at least 7 days, if set. If unset, the license will never expire. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
