---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-AllocateQuotaRequest/
title: Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::AllocateQuotaRequest (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:57.768377+00:00
---

# Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::AllocateQuotaRequest (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-AllocateQuotaRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::AllocateQuotaRequest (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.0  0.5.0  0.4.6 

Reference documentation and code samples for the Service Control API V1 API class Google::Cloud::ServiceControl::V1::AllocateQuotaRequest.

Request message for the AllocateQuota method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allocate_operation
    
    
    def allocate_operation() -> ::Google::Cloud::ServiceControl::V1::QuotaOperation

**Returns**

  * ([::Google::Cloud::ServiceControl::V1::QuotaOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-QuotaOperation)) — Operation that describes the quota allocation. 



### #allocate_operation=
    
    
    def allocate_operation=(value) -> ::Google::Cloud::ServiceControl::V1::QuotaOperation

**Parameter**

  * **value** ([::Google::Cloud::ServiceControl::V1::QuotaOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-QuotaOperation)) — Operation that describes the quota allocation. 



**Returns**

  * ([::Google::Cloud::ServiceControl::V1::QuotaOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-QuotaOperation)) — Operation that describes the quota allocation. 



### #service_config_id
    
    
    def service_config_id() -> ::String

**Returns**

  * (::String) — Specifies which version of service configuration should be used to process the request. If unspecified or no matching version can be found, the latest one will be used. 



### #service_config_id=
    
    
    def service_config_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies which version of service configuration should be used to process the request. If unspecified or no matching version can be found, the latest one will be used. 



**Returns**

  * (::String) — Specifies which version of service configuration should be used to process the request. If unspecified or no matching version can be found, the latest one will be used. 



### #service_name
    
    
    def service_name() -> ::String

**Returns**

  * (::String) — Name of the service as specified in the service configuration. For example, `"pubsub.googleapis.com"`.

See [google.api.Service][google.api.Service] for the definition of a service name. 




### #service_name=
    
    
    def service_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the service as specified in the service configuration. For example, `"pubsub.googleapis.com"`.

See [google.api.Service][google.api.Service] for the definition of a service name. 




**Returns**

  * (::String) — Name of the service as specified in the service configuration. For example, `"pubsub.googleapis.com"`.

See [google.api.Service][google.api.Service] for the definition of a service name. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
