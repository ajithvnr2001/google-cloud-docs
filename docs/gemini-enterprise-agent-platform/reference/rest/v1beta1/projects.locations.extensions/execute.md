---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.extensions/execute/
title: Method: extensions.execute \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:59:43.212681+00:00
---

# Method: extensions.execute  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.extensions/execute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: extensions.execute Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.extensions.execute

Executes the request against a given extension.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{name}:execute`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Required. name (identifier) of the extension; Format: `projects/{project}/locations/{location}/extensions/{extension}`

### Request body

The request body contains data with the following structure: | Fields  
  
`operationId` `string` Required. The desired id of the operation to be executed in this extension as defined in `[ExtensionOperation.operation_id](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.extensions#ExtensionOperation.FIELDS.operation_id)`. | `operationParams` `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Request parameters that will be used for executing this operation.The struct should be in a form of map with param name as the key and actual param value as the value. E.g. If this operation requires a param "name" to be set to "abc". you can set this to something like {"name": "abc"}. | `runtimeAuthConfig` `object (`[AuthConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.extensions#AuthConfig)`)` Optional. Auth config provided at runtime to override the default value in [Extension.manifest.auth_config][]. The AuthConfig.auth_type should match the value in [Extension.manifest.auth_config][].

### Response body

Response message for `[ExtensionExecutionService.ExecuteExtension](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.extensions/execute#google.cloud.aiplatform.v1beta1.ExtensionExecutionService.ExecuteExtension)`. If successful, the response body contains data with the following structure: | Fields  
  
`content` `string` Response content from the extension. The content should be conformant to the response.content schema in the extension's manifest/OpenAPI spec. | JSON representation  
---  
      
    
    {
      "content": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.extensions.execute`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
