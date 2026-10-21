---
url: https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/run/
title: Method: projects.locations.investigations.revisions.run \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:54.559049+00:00
---

# Method: projects.locations.investigations.revisions.run  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  Method: projects.locations.investigations.revisions.run Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * InvestigationRunParameters
    * JSON representation



This item is deprecated!

Deprecated: Investigations should only be run by the agent.

Run an existing revision of an investigation.

### HTTP request

`POST https://geminicloudassist.googleapis.com/v1alpha/{name=projects/*/locations/*/investigations/*/revisions/*}:run`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the investigation revision to run.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "runParameters": {
        object ([InvestigationRunParameters](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/run#InvestigationRunParameters))
      }
    }  
  
Fields  
---  
`runParameters` |  `object (`[InvestigationRunParameters](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/run#InvestigationRunParameters)`)` Optional. Parameters to pass through.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `geminicloudassist.investigationRevisions.run`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## InvestigationRunParameters

This item is deprecated!

Deprecated: This message is only used in the deprecated revisions.run method.

Represents user parameters for running an investigation.

JSON representation  
---  
      
    
    {
      "accessTokens": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`accessTokens` |  `map (key: string, value: string)` Optional. If populated, map of project to IAM token granting access to that project.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
