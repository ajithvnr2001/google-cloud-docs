---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-CheckError/
title: Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::CheckError (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:50.275173+00:00
---

# Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::CheckError (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-CheckError/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::CheckError (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.0  0.5.0  0.4.6 

Reference documentation and code samples for the Service Control API V1 API class Google::Cloud::ServiceControl::V1::CheckError.

Defines the errors to be returned in [google.api.servicecontrol.v1.CheckResponse.check_errors](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-CheckResponse#Google__Cloud__ServiceControl__V1__CheckResponse_check_errors_instance_ "Google::Cloud::ServiceControl::V1::CheckResponse#check_errors \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #code
    
    
    def code() -> ::Google::Cloud::ServiceControl::V1::CheckError::Code

**Returns**

  * ([::Google::Cloud::ServiceControl::V1::CheckError::Code](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-CheckError-Code)) — The error code. 



### #code=
    
    
    def code=(value) -> ::Google::Cloud::ServiceControl::V1::CheckError::Code

**Parameter**

  * **value** ([::Google::Cloud::ServiceControl::V1::CheckError::Code](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-CheckError-Code)) — The error code. 



**Returns**

  * ([::Google::Cloud::ServiceControl::V1::CheckError::Code](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-CheckError-Code)) — The error code. 



### #detail
    
    
    def detail() -> ::String

**Returns**

  * (::String) — Free-form text providing details on the error cause of the error. 



### #detail=
    
    
    def detail=(value) -> ::String

**Parameter**

  * **value** (::String) — Free-form text providing details on the error cause of the error. 



**Returns**

  * (::String) — Free-form text providing details on the error cause of the error. 



### #status
    
    
    def status() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Rpc-Status)) — Contains public information about the check error. If available, `status.code` will be non zero and client can propagate it out as public error. 



### #status=
    
    
    def status=(value) -> ::Google::Rpc::Status

**Parameter**

  * **value** ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Rpc-Status)) — Contains public information about the check error. If available, `status.code` will be non zero and client can propagate it out as public error. 



**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Rpc-Status)) — Contains public information about the check error. If available, `status.code` will be non zero and client can propagate it out as public error. 



### #subject
    
    
    def subject() -> ::String

**Returns**

  * (::String) — 

Subject to whom this error applies. See the specific code enum for more details on this field. For example:

    * "project:
    * "folder:
    * "organization:



### #subject=
    
    
    def subject=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Subject to whom this error applies. See the specific code enum for more details on this field. For example:

    * "project:
    * "folder:
    * "organization:



**Returns**

  * (::String) — 

Subject to whom this error applies. See the specific code enum for more details on this field. For example:

    * "project:
    * "folder:
    * "organization:



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
