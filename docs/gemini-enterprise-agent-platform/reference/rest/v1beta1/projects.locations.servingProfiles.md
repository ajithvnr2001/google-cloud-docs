---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles
title: REST Resource: projects.locations.servingProfiles \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:31:47.825296+00:00
---

# REST Resource: projects.locations.servingProfiles  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.servingProfiles Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: ServingProfile

Configures the serving behavior for a resource-less GenAI serving.

Fields  
  
`name` `string` Identifier. The resource name of the ServingProfile. | `displayName` `string` Required. The display name of the ServingProfile. The name can be up to 128 characters long and can consist of any UTF-8 characters. | `description` `string` Optional. The description of the ServingProfile. | `scope` `enum (`[ServingProfileScope](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles#ServingProfileScope)`)` Required. The specific API this ServingProfile applies to. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when the ServingProfile was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when the ServingProfile was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `profile_spec` `Union type`  
  
The profile spec for the ServingProfile. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`cmekConfig` `object (`[CmekConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles#CmekConfig)`)` CMEK configuration for the ServingProfile. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "scope": enum ([ServingProfileScope](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles#ServingProfileScope)),
      "createTime": string,
      "updateTime": string,
    
      // profile_spec
      "cmekConfig": {
        object ([CmekConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles#CmekConfig))
      }
      // Union type
    }  
  
## CmekConfig

Configuration for Customer-Managed Encryption Keys (CMEK).

Fields  
  
`encryptionSpec` `object (`[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/EncryptionSpec)`)` Required. The customer-managed encryption key spec for the Serving Profile. | JSON representation  
---  
      
    
    {
      "encryptionSpec": {
        object ([EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/EncryptionSpec))
      }
    }  
  
## ServingProfileScope

The specific API this ServingProfile applies to.

Enums  
---  
`SERVING_PROFILE_SCOPE_UNSPECIFIED` | Default value. This value is unused. When users create a ServingProfile, they must choose a scope.  
`GEMINI_LIVE` | The scope for Gemini Live.  
`INTERACTIONS_API` | The scope for Interactions API.  
`RESPONSE_API` | The scope for Response API.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles/create)`

|  Creates a ServingProfile.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles/delete)`

|  Deletes a ServingProfile.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles/get)`

|  Gets a ServingProfile.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles/list)`

|  Lists ServingProfiles in a Location.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.servingProfiles/patch)`

|  Updates a ServingProfile.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
