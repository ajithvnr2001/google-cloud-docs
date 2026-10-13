---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyReferenceList/
title: Method: instances.verifyReferenceList \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:30.626722+00:00
---

# Method: instances.verifyReferenceList  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyReferenceList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.verifyReferenceList Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * ReferenceListError
    * JSON representation



**Full name** : projects.locations.instances.verifyReferenceList

instances.verifyReferenceList validates list content and returns line errors, if any.

### HTTP request

`POST https://{endpoint}/v1/{instance}:verifyReferenceList`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The name of the parent resource, which is the SecOps instance associated with the request. Format: `projects/{project}/locations/{location}/instances/{instance}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "syntaxType": enum ([ReferenceListSyntaxType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.referenceLists#ReferenceListSyntaxType)),
      "entries": [
        {
          object ([ReferenceListEntry](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.referenceLists#ReferenceListEntry))
        }
      ]
    }  
  
Fields  
---  
`syntaxType` |  `enum (`[ReferenceListSyntaxType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.referenceLists#ReferenceListSyntaxType)`)` Required. Type (format) of list lines.  
`entries[]` |  `object (`[ReferenceListEntry](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.referenceLists#ReferenceListEntry)`)` Required. The entries of the reference list. Each line may be either an item in the list or a comment.  
  
### Response body

VerifyListResponse response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "success": boolean,
      "errors": [
        {
          object ([ReferenceListError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyReferenceList#ReferenceListError))
        }
      ]
    }  
  
Fields  
---  
`success` |  `boolean` Validity of list - true if no errors found.  
`errors[]` |  `object (`[ReferenceListError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyReferenceList#ReferenceListError)`)` Line-level errors causing the list to be invalid.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.referenceLists.verifyReferenceList`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ReferenceListError

The error generated when verifying the reference list.

JSON representation  
---  
      
    
    {
      "lineNumber": integer,
      "errorMessage": string
    }  
  
Fields  
---  
`lineNumber` |  `integer` 1-indexed line number where the error occurs. General list errors are indexed at -1.  
`errorMessage` |  `string` Message explaining why the line is invalid.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
