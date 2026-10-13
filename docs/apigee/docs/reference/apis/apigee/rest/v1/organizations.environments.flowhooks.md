---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks
title: REST Resource: organizations.environments.flowhooks \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:53.611714+00:00
---

# REST Resource: organizations.environments.flowhooks  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.environments.flowhooks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: FlowHook
    * JSON representation
  * Methods



## Resource: FlowHook

JSON representation  
---  
      
    
    {
      "flowHookPoint": string,
      "description": string,
      "sharedFlow": string,
      "continueOnError": boolean
    }  
  
Fields  
---  
`flowHookPoint` |  `string` Output only. Where in the API call flow the flow hook is invoked. Must be one of `PreProxyFlowHook`, `PostProxyFlowHook`, `PreTargetFlowHook`, or `PostTargetFlowHook`.  
`description` |  `string` Description of the flow hook.  
`sharedFlow` |  `string` Shared flow attached to this flow hook, or empty if there is none attached.  
`continueOnError` |  `boolean` Optional. Flag that specifies whether execution should continue if the flow hook throws an exception. Set to `true` to continue execution. Set to `false` to stop execution if the flow hook throws an exception. Defaults to `true`.  
  
## Methods  
  
---  
  
### `[attachSharedFlowToFlowHook](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks/attachSharedFlowToFlowHook)`

|  Attaches a shared flow to a flow hook.  
  
### `[detachSharedFlowFromFlowHook](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks/detachSharedFlowFromFlowHook)`

|  Detaches a shared flow from a flow hook.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks/get)`

|  Returns the name of the shared flow attached to the specified flow hook.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.flowhooks/list)`

|  Lists the flow hooks attached to an environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
