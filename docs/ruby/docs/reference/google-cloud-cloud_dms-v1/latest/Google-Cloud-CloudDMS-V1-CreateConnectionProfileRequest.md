---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateConnectionProfileRequest/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CreateConnectionProfileRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:22.920595+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CreateConnectionProfileRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateConnectionProfileRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CreateConnectionProfileRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::CreateConnectionProfileRequest.

Request message for 'CreateConnectionProfile' request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #connection_profile
    
    
    def connection_profile() -> ::Google::Cloud::CloudDMS::V1::ConnectionProfile

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile)) — Required. The create request body including the connection profile data 



### #connection_profile=
    
    
    def connection_profile=(value) -> ::Google::Cloud::CloudDMS::V1::ConnectionProfile

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile)) — Required. The create request body including the connection profile data 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile)) — Required. The create request body including the connection profile data 



### #connection_profile_id
    
    
    def connection_profile_id() -> ::String

**Returns**

  * (::String) — Required. The connection profile identifier. 



### #connection_profile_id=
    
    
    def connection_profile_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The connection profile identifier. 



**Returns**

  * (::String) — Required. The connection profile identifier. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent which owns this collection of connection profiles. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent which owns this collection of connection profiles. 



**Returns**

  * (::String) — Required. The parent which owns this collection of connection profiles. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Returns**

  * (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




### #skip_validation
    
    
    def skip_validation() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Create the connection profile without validating it. The default is false. Only supported for Oracle connection profiles. 



### #skip_validation=
    
    
    def skip_validation=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Create the connection profile without validating it. The default is false. Only supported for Oracle connection profiles. 



**Returns**

  * (::Boolean) — Optional. Create the connection profile without validating it. The default is false. Only supported for Oracle connection profiles. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Only validate the connection profile, but don't create any resources. The default is false. Only supported for Oracle connection profiles. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Only validate the connection profile, but don't create any resources. The default is false. Only supported for Oracle connection profiles. 



**Returns**

  * (::Boolean) — Optional. Only validate the connection profile, but don't create any resources. The default is false. Only supported for Oracle connection profiles. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
