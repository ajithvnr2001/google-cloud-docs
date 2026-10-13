---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/merge/
title: Method: cases.merge \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:03.680483+00:00
---

# Method: cases.merge  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/merge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: cases.merge Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.merge

Merges one or more cases into a single destination case. This is useful when multiple cases are determined to be part of the same security investigation.

### HTTP request

`POST https://{endpoint}/v1/{parent}/cases:merge`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to merge cases on. Format: projects/{project}/locations/{location}/instances/{instance}/cases  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "casesIds": [
        integer
      ],
      "caseToMergeWith": integer
    }  
  
Fields  
---  
`casesIds[]` |  `integer` Required. Cases to merge.  
`caseToMergeWith` |  `integer` Required. Case to merge with.  
  
### Response body

Response message for cases.merge.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "newCaseId": integer,
      "isRequestValid": boolean,
      "errors": [
        string
      ]
    }  
  
Fields  
---  
`newCaseId` |  `integer` Output only. New caseId if request is successful, null otherwise.  
`isRequestValid` |  `boolean` Output only. Flag that indicates whether the request is valid or not.  
`errors[]` |  `string` Output only. Error list if request is invalid.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.cases.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
