---
url: https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations/generateServiceIdentity/
title: Method: projects.locations.generateServiceIdentity \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:41.481168+00:00
---

# Method: projects.locations.generateServiceIdentity  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations/generateServiceIdentity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Reference ](https://docs.cloud.google.com/tpu/docs/reference)



Send feedback 

#  Method: projects.locations.generateServiceIdentity Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * ServiceIdentity
    * JSON representation
  * Try it!



Generates the Cloud TPU service identity for the project.

### HTTP request

`POST https://tpu.googleapis.com/v2alpha1/{parent=projects/*/locations/*}:generateServiceIdentity`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name.  
  
### Request body

The request body must be empty.

### Response body

Response for `[locations.generateServiceIdentity](https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations/generateServiceIdentity#google.cloud.tpu.v2alpha1.Tpu.GenerateServiceIdentity)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "identity": {
        object ([ServiceIdentity](https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations/generateServiceIdentity#ServiceIdentity))
      }
    }  
  
Fields  
---  
`identity` |  `object (`[ServiceIdentity](https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations/generateServiceIdentity#ServiceIdentity)`)` ServiceIdentity that was created or retrieved.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud.tpu`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ServiceIdentity

The per-product per-project service identity for Cloud TPU service.

JSON representation  
---  
      
    
    {
      "email": string
    }  
  
Fields  
---  
`email` |  `string` The email address of the service identity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-15 UTC."],[],[]] 
