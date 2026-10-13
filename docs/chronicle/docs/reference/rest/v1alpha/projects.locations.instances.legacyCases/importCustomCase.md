---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyCases/importCustomCase/
title: Method: legacyCases.importCustomCase \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:00.001516+00:00
---

# Method: legacyCases.importCustomCase  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyCases/importCustomCase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacyCases.importCustomCase Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.legacyCases.importCustomCase

Imports a custom simulated case from a JSON package. This allows users to restore previously exported case simulation scenarios into their environment.

### HTTP request

`POST https://{endpoint}/v1alpha/{name}/legacyCases:importCustomCase`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the LegacyCase to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/LegacyCases  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "cases": [
        {
          object ([LegacyCaseInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo))
        }
      ],
      "type": enum ([CaseType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CaseType))
    }  
  
Fields  
---  
`cases[]` |  `object (`[LegacyCaseInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo)`)` Required. Cases is a list of case information items.  
`type` |  `enum (`[CaseType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CaseType)`)` Optional. Type is the case type.  
  
### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.legacyCases.importJson`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
