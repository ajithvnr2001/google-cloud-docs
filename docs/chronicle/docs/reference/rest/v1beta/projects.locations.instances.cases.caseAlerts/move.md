---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.caseAlerts/move/
title: Method: caseAlerts.move \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:10.810881+00:00
---

# Method: caseAlerts.move  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.caseAlerts/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: caseAlerts.move Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.caseAlerts.move

Moves a CaseAlert to a different Case. Use this method to reassign an alert to a more appropriate case. The alert must be open, and both the source and destination cases must also be open.

### HTTP request

`POST https://{endpoint}/v1beta/{name}:move`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The CaseAlert to move. The CaseAlert's `name` field is used to identify the CaseAlert. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts/{caseAlert}:move  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "destinationCaseId": integer
    }  
  
Fields  
---  
`destinationCaseId` |  `integer` Optional. The case to which the alert will be moved to.  
  
### Response body

Response message for caseAlerts.move.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "newCaseId": integer,
      "valid": boolean,
      "errors": [
        string
      ]
    }  
  
Fields  
---  
`newCaseId` |  `integer` Output only. The new case to which the alert was moved to, or null if the move failed.  
`valid` |  `boolean` Output only. Was the operation valid.  
`errors[]` |  `string` Output only. Errors raised when moving the alert  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.caseAlerts.move`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
