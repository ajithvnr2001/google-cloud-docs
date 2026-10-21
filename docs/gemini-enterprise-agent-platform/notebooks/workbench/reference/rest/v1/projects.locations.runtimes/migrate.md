---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.runtimes/migrate/
title: Method: projects.locations.runtimes.migrate \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:31:26.208646+00:00
---

# Method: projects.locations.runtimes.migrate  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.runtimes/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.runtimes.migrate Stay organized with collections  Save and categorize content based on your preferences. 

Migrate an existing Runtime to a new Workbench Instance.

### HTTP request

`POST https://notebooks.googleapis.com/v1/{name}:migrate`

### Path parameters

Parameters  
---  
`name` |  `string` Required. Format: `projects/{projectId}/locations/{location}/runtimes/{runtimeId}` Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `name`:

  * `notebooks.runtimes.get`
  * `notebooks.instances.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "network": string,
      "subnet": string,
      "serviceAccount": string,
      "requestId": string,
      "postStartupScriptOption": enum ([PostStartupScriptOption](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.runtimes/migrate#PostStartupScriptOption))
    }  
  
Fields  
---  
`network` |  `string` Optional. Name of the VPC that the new Instance is in. This is required if the Runtime uses google-managed network. If the Runtime uses customer-owned network, it will reuse the same VPC, and this field must be empty. Format: `projects/{projectId}/global/networks/{network_id}`  
`subnet` |  `string` Optional. Name of the subnet that the new Instance is in. This is required if the Runtime uses google-managed network. If the Runtime uses customer-owned network, it will reuse the same subnet, and this field must be empty. Format: `projects/{projectId}/regions/{region}/subnetworks/{subnetwork_id}`  
`serviceAccount` |  `string` Optional. The service account to be included in the Compute Engine instance of the new Workbench Instance when the Runtime uses "single user only" mode for permission. If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. When the Runtime uses service account mode for permission, it will reuse the same service account, and this field must be empty.  
`requestId` |  `string` Optional. Idempotent request UUID.  
`postStartupScriptOption` |  `enum (`[PostStartupScriptOption](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.runtimes/migrate#PostStartupScriptOption)`)` Optional. Specifies the behavior of post startup script during migration.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/notebooks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## PostStartupScriptOption

Specifies the behavior of post startup script during migration.

Enums  
---  
`POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED` | Post startup script option is not specified. Default is POST_STARTUP_SCRIPT_OPTION_SKIP.  
`POST_STARTUP_SCRIPT_OPTION_SKIP` | Not migrate the post startup script to the new Workbench Instance.  
`POST_STARTUP_SCRIPT_OPTION_RERUN` | Redownload and rerun the same post startup script as the Google-Managed Notebook.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
