---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.deploymentResourcePools/create/
title: Method: deploymentResourcePools.create \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:40.974178+00:00
---

# Method: deploymentResourcePools.create  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.deploymentResourcePools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: deploymentResourcePools.create Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.deploymentResourcePools.create

Create a DeploymentResourcePool.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}/deploymentResourcePools`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The parent location resource where this DeploymentResourcePool will be created. Format: `projects/{project}/locations/{location}`

### Request body

The request body contains data with the following structure: | Fields  
  
`deploymentResourcePool` `object (`[DeploymentResourcePool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.deploymentResourcePools#DeploymentResourcePool)`)` Required. The DeploymentResourcePool to create. | `deploymentResourcePoolId` `string` Required. The id to use for the DeploymentResourcePool, which will become the final component of the DeploymentResourcePool's resource name.The maximum length is 63 characters, and valid characters are `/^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$/`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-05-04 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
