---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.nativeDashboards/duplicate/
title: Method: nativeDashboards.duplicate \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:26.787079+00:00
---

# Method: nativeDashboards.duplicate  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.nativeDashboards/duplicate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: nativeDashboards.duplicate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.nativeDashboards.duplicate

Duplicate a dashboard.

### HTTP request

`POST https://{endpoint}/v1/{name}:duplicate`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The dashboard name to duplicate. Format: projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "nativeDashboard": {
        object ([NativeDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.nativeDashboards#NativeDashboard))
      }
    }  
  
Fields  
---  
`nativeDashboard` |  `object (`[NativeDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.nativeDashboards#NativeDashboard)`)` Required. Any fields that need modification can be passed through this like name, description etc.  
  
### Response body

If successful, the response body contains an instance of `[NativeDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.nativeDashboards#NativeDashboard)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.nativeDashboards.duplicate`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
