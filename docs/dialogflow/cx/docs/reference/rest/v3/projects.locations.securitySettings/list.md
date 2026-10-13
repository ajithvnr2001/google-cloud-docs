---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/list/
title: Method: projects.locations.securitySettings.list \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:27.214970+00:00
---

# Method: projects.locations.securitySettings.list  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/list/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.securitySettings.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Returns the list of all security settings in the specified location.

### HTTP request

`GET https://{endpoint}/v3/{parent=projects/*/locations/*}/securitySettings`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The location to list all security settings for. Format: `projects/<ProjectID>/locations/<LocationID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.securitySettings.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return in a single page. By default 20 and at most 100.  
`pageToken` |  `string` The nextPageToken value returned from a previous list request.  
  
### Request body

The request body must be empty.

### Response body

The response message for [SecuritySettings.ListSecuritySettings][].

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "securitySettings": [
        {
          object ([SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`securitySettings[]` |  `object (`[SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings)`)` The list of security settings.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
