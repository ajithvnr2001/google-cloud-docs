---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Cloud-BeyondCorp-AppConnectors-V1-ResourceInfo/
title: BeyondCorp AppConnectors V1 API - Class Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo (v0.13.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:47.884596+00:00
---

# BeyondCorp AppConnectors V1 API - Class Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo (v0.13.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Cloud-BeyondCorp-AppConnectors-V1-ResourceInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BeyondCorp AppConnectors V1 API - Class Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo (v0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.2  0.4.2  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the BeyondCorp AppConnectors V1 API class Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo.

ResourceInfo represents the information/status of an app connector resource. Such as:

  * remote_agent 
    * container
    * runtime
    * appgateway 
      * appconnector
      * appconnection 
        * tunnel
      * logagent



## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Required. Unique Id for the resource. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Unique Id for the resource. 



**Returns**

  * (::String) — Required. Unique Id for the resource. 



### #resource
    
    
    def resource() -> ::Google::Protobuf::Any

**Returns**

  * ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Protobuf-Any)) — Specific details for the resource. This is for internal use only. 



### #resource=
    
    
    def resource=(value) -> ::Google::Protobuf::Any

**Parameter**

  * **value** ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Protobuf-Any)) — Specific details for the resource. This is for internal use only. 



**Returns**

  * ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Protobuf-Any)) — Specific details for the resource. This is for internal use only. 



### #status
    
    
    def status() -> ::Google::Cloud::BeyondCorp::AppConnectors::V1::HealthStatus

**Returns**

  * ([::Google::Cloud::BeyondCorp::AppConnectors::V1::HealthStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Cloud-BeyondCorp-AppConnectors-V1-HealthStatus)) — Overall health status. Overall status is derived based on the status of each sub level resources. 



### #status=
    
    
    def status=(value) -> ::Google::Cloud::BeyondCorp::AppConnectors::V1::HealthStatus

**Parameter**

  * **value** ([::Google::Cloud::BeyondCorp::AppConnectors::V1::HealthStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Cloud-BeyondCorp-AppConnectors-V1-HealthStatus)) — Overall health status. Overall status is derived based on the status of each sub level resources. 



**Returns**

  * ([::Google::Cloud::BeyondCorp::AppConnectors::V1::HealthStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Cloud-BeyondCorp-AppConnectors-V1-HealthStatus)) — Overall health status. Overall status is derived based on the status of each sub level resources. 



### #sub
    
    
    def sub() -> ::Array<::Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo>

**Returns**

  * (::Array<[::Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Cloud-BeyondCorp-AppConnectors-V1-ResourceInfo)>) — List of Info for the sub level resources. 



### #sub=
    
    
    def sub=(value) -> ::Array<::Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Cloud-BeyondCorp-AppConnectors-V1-ResourceInfo)>) — List of Info for the sub level resources. 



**Returns**

  * (::Array<[::Google::Cloud::BeyondCorp::AppConnectors::V1::ResourceInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Cloud-BeyondCorp-AppConnectors-V1-ResourceInfo)>) — List of Info for the sub level resources. 



### #time
    
    
    def time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Protobuf-Timestamp)) — The timestamp to collect the info. It is suggested to be set by the topmost level resource only. 



### #time=
    
    
    def time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Protobuf-Timestamp)) — The timestamp to collect the info. It is suggested to be set by the topmost level resource only. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connectors-v1/latest/Google-Protobuf-Timestamp)) — The timestamp to collect the info. It is suggested to be set by the topmost level resource only. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
