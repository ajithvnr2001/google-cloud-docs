---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents/list/
title: Method: projects.locations.insightsConfigs.deploymentEvents.list \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:01.249891+00:00
---

# Method: projects.locations.insightsConfigs.deploymentEvents.list  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.insightsConfigs.deploymentEvents.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists Deployment Events in a given insights config.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{parent=projects/*/locations/*/insightsConfigs/*}/deploymentEvents`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent insights config that owns this collection of deployment events. Format: projects/{project}/locations/{location}/insightsConfigs/{insightsConfig}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of deployment events to return. The service may return fewer than this value. If unspecified, at most 50 deployment events will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `deploymentEvents.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `deploymentEvents.list` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter expression that matches a subset of the DeploymentEvents. <https://google.aip.dev/160>.  
  
### Request body

The request body must be empty.

### Response body

Response to listing DeploymentEvents.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "deploymentEvents": [
        {
          object ([DeploymentEvent](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents#DeploymentEvent))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`deploymentEvents[]` |  `object (`[DeploymentEvent](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents#DeploymentEvent)`)` The list of DeploymentEvents.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `developerconnect.deploymentEvents.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-18 UTC."],[],[]] 
