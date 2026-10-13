---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations/provision/
title: Method: projects.locations.provision \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:59.138518+00:00
---

# Method: projects.locations.provision  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations/provision/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.provision Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Provisions the project resource. During the process, related systems will get prepared and initialized.

Caller must read the [Terms for data use](https://cloud.google.com/retail/data-use-terms), and optionally specify in request to provide consent to that service terms.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1beta/{name=projects/*/locations/*}:provision`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Full resource name of a `Project`, such as `projects/{project_id_or_number}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "acceptDataUseTerms": boolean,
      "dataUseTermsVersion": string,
      "saasParams": {
        object ([SaasParams](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SaasParams))
      }
    }  
  
Fields  
---  
`acceptDataUseTerms` |  `boolean` Required. Set to `true` to specify that caller has read and would like to give consent to the [Terms for data use](https://cloud.google.com/retail/data-use-terms).  
`dataUseTermsVersion` |  `string` Required. The version of the [Terms for data use](https://cloud.google.com/retail/data-use-terms) that caller has read and would like to give consent to.Acceptable version is `2022-11-23`, and this may change over time.  
`saasParams` |  `object (`[SaasParams](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SaasParams)`)` Optional. Parameters for Agentspace.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `discoveryengine.projects.provision`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
