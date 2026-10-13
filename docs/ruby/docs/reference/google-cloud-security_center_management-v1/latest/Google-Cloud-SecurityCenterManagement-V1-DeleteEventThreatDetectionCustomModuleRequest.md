---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-DeleteEventThreatDetectionCustomModuleRequest/
title: Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::DeleteEventThreatDetectionCustomModuleRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:10.372742+00:00
---

# Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::DeleteEventThreatDetectionCustomModuleRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-DeleteEventThreatDetectionCustomModuleRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::DeleteEventThreatDetectionCustomModuleRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Security Command Center Management V1 API class Google::Cloud::SecurityCenterManagement::V1::DeleteEventThreatDetectionCustomModuleRequest.

Request message for [SecurityCenterManagement.DeleteEventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Client#Google__Cloud__SecurityCenterManagement__V1__SecurityCenterManagement__Client_delete_event_threat_detection_custom_module_instance_ "Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Client#delete_event_threat_detection_custom_module \(method\)").

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

  * (::String) — 

Required. The resource name of the Event Threat Detection custom module, in one of the following formats:

    * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The resource name of the Event Threat Detection custom module, in one of the following formats:

    * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`



**Returns**

  * (::String) — 

Required. The resource name of the Event Threat Detection custom module, in one of the following formats:

    * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be deleted. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to delete the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during creation of the module

Defaults to `false`. 




### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be deleted. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to delete the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during creation of the module

Defaults to `false`. 




**Returns**

  * (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be deleted. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to delete the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during creation of the module

Defaults to `false`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
