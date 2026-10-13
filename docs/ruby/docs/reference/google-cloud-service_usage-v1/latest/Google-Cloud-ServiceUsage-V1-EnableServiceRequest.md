---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_usage-v1/latest/Google-Cloud-ServiceUsage-V1-EnableServiceRequest/
title: Service Usage V1 API - Class Google::Cloud::ServiceUsage::V1::EnableServiceRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:24.881306+00:00
---

# Service Usage V1 API - Class Google::Cloud::ServiceUsage::V1::EnableServiceRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_usage-v1/latest/Google-Cloud-ServiceUsage-V1-EnableServiceRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Usage V1 API - Class Google::Cloud::ServiceUsage::V1::EnableServiceRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.1  0.2.1  0.1.4 

Reference documentation and code samples for the Service Usage V1 API class Google::Cloud::ServiceUsage::V1::EnableServiceRequest.

Request message for the `EnableService` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name of the consumer and service to enable the service on.

The `EnableService` and `DisableService` methods currently only support projects.

Enabling a service requires that the service is public or is shared with the user enabling the service.

An example name would be: `projects/123/services/serviceusage.googleapis.com` where `123` is the project number. 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the consumer and service to enable the service on.

The `EnableService` and `DisableService` methods currently only support projects.

Enabling a service requires that the service is public or is shared with the user enabling the service.

An example name would be: `projects/123/services/serviceusage.googleapis.com` where `123` is the project number. 




**Returns**

  * (::String) — Name of the consumer and service to enable the service on.

The `EnableService` and `DisableService` methods currently only support projects.

Enabling a service requires that the service is public or is shared with the user enabling the service.

An example name would be: `projects/123/services/serviceusage.googleapis.com` where `123` is the project number. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
