---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/duplicate/
title: Method: projects.alerts.duplicate \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:38.319790+00:00
---

# Method: projects.alerts.duplicate  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/duplicate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  Method: projects.alerts.duplicate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Marks an alert as a duplicate of another alert. - DUPLICATE.

### HTTP request

`POST https://threatintelligence.googleapis.com/v1beta/{name=projects/*/alerts/*}:duplicate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the alert to mark as a duplicate. Format: projects/{project}/alerts/{alert}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "duplicateOf": string
    }  
  
Fields  
---  
`duplicateOf` |  `string` Optional. Name of the alert to mark as a duplicate of. Format: projects/{project}/alerts/{alert}  
  
### Response body

If successful, the response body contains an instance of `[Alert](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#Alert)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `threatintelligence.alerts.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
