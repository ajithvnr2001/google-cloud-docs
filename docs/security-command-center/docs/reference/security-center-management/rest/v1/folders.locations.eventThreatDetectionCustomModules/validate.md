---
url: https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/validate/
title: Method: folders.locations.eventThreatDetectionCustomModules.validate \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:47.986257+00:00
---

# Method: folders.locations.eventThreatDetectionCustomModules.validate  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/validate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: folders.locations.eventThreatDetectionCustomModules.validate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Validates the given Event Threat Detection custom module.

### HTTP request

`POST https://securitycentermanagement.googleapis.com/v1/{parent=folders/*/locations/*}/eventThreatDetectionCustomModules:validate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name of the parent to validate the custom modules under, in one of the following formats:

  * `organizations/{organization}/locations/{location}`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rawText": string,
      "type": string
    }  
  
Fields  
---  
`rawText` |  `string` Required. The raw text of the module's contents. Used to generate error messages.  
`type` |  `string` Required. The type of the module. For example, `CONFIGURABLE_BAD_IP`.  
  
### Response body

If successful, the response body contains an instance of `[ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/ValidateEventThreatDetectionCustomModuleResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `securitycentermanagement.eventThreatDetectionCustomModules.validate`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-01 UTC."],[],[]] 
