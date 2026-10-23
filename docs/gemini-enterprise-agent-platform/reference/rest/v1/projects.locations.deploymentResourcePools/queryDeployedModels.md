---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.deploymentResourcePools/queryDeployedModels/
title: Method: deploymentResourcePools.queryDeployedModels \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:22.519516+00:00
---

# Method: deploymentResourcePools.queryDeployedModels  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.deploymentResourcePools/queryDeployedModels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: deploymentResourcePools.queryDeployedModels Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.deploymentResourcePools.queryDeployedModels

List DeployedModels that have been deployed on this DeploymentResourcePool.

### Endpoint

get  `https://{service-endpoint}/v1/{deploymentResourcePool}:queryDeployedModels`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`deploymentResourcePool` `string` Required. The name of the target DeploymentResourcePool to query. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deploymentResourcePool}`

### Query parameters

| `pageSize` `integer` The maximum number of DeployedModels to return. The service may return fewer than this value. | `pageToken` `string` A page token, received from a previous `deploymentResourcePools.queryDeployedModels` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `deploymentResourcePools.queryDeployedModels` must match the call that provided the page token.

### Request body

The request body must be empty.

### Response body

Response message for deploymentResourcePools.queryDeployedModels method. If successful, the response body contains data with the following structure: | Fields  
  
`deployedModels[]  
**(deprecated)**` `object (`[DeployedModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints#DeployedModel)`)` This item is deprecated!DEPRECATED Use deployedModelRefs instead. | `nextPageToken` `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. | `deployedModelRefs[]` `object (`[DeployedModelRef](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models#Model.DeployedModelRef)`)` References to the DeployedModels that share the specified deploymentResourcePool. | `totalDeployedModelCount` `integer` The total number of DeployedModels on this DeploymentResourcePool. | `totalEndpointCount` `integer` The total number of endpoints that have DeployedModels on this DeploymentResourcePool. | JSON representation  
---  
      
    
    {
      "deployedModels": [
        {
          object ([DeployedModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints#DeployedModel))
        }
      ],
      "nextPageToken": string,
      "deployedModelRefs": [
        {
          object ([DeployedModelRef](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models#Model.DeployedModelRef))
        }
      ],
      "totalDeployedModelCount": integer,
      "totalEndpointCount": integer
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `deploymentResourcePool` resource:

  * `aiplatform.deploymentResourcePools.queryDeployedModels`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
