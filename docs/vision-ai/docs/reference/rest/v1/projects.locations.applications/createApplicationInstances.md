---
url: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications/createApplicationInstances/
title: Method: projects.locations.applications.createApplicationInstances \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:06.691504+00:00
---

# Method: projects.locations.applications.createApplicationInstances  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications/createApplicationInstances/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback 

#  Method: projects.locations.applications.createApplicationInstances Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * ApplicationInstance
    * JSON representation



Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

### HTTP request

`POST https://{endpoint}/v1/{name=projects/*/locations/*/applications/*}:createApplicationInstances`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/vision-ai/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "applicationInstances": [
        {
          object ([ApplicationInstance](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications/createApplicationInstances#ApplicationInstance))
        }
      ],
      "requestId": string
    }  
  
Fields  
---  
`applicationInstances[]` |  `object (`[ApplicationInstance](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications/createApplicationInstances#ApplicationInstance)`)` Required. The resources being created.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets.operations#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ApplicationInstance

Message for creating a Instance.

JSON representation  
---  
      
    
    {
      "instanceId": string,
      "instance": {
        object ([Instance](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications.instances#Instance))
      }
    }  
  
Fields  
---  
`instanceId` |  `string` Required. Id of the requesting object.  
`instance` |  `object (`[Instance](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications.instances#Instance)`)` Required. The resource being created.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
