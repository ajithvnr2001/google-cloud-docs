---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.instances/diagnose/
title: Method: projects.locations.instances.diagnose \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:24.025353+00:00
---

# Method: projects.locations.instances.diagnose  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.instances/diagnose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.instances.diagnose Stay organized with collections  Save and categorize content based on your preferences. 

Creates a Diagnostic File and runs Diagnostic Tool given an Instance.

### HTTP request

`POST https://notebooks.googleapis.com/v1/{name}:diagnose`

### Path parameters

Parameters  
---  
`name` |  `string` Required. Format: `projects/{projectId}/locations/{location}/instances/{instanceId}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "diagnosticConfig": {
        object ([DiagnosticConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.instances/diagnose#DiagnosticConfig))
      },
      "timeoutMinutes": integer
    }  
  
Fields  
---  
`diagnosticConfig` |  `object (`[DiagnosticConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/projects.locations.instances/diagnose#DiagnosticConfig)`)` Required. Defines flags that are used to run the diagnostic tool  
`timeoutMinutes` |  `integer` Optional. Maximum amount of time in minutes before the operation times out.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/notebooks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## DiagnosticConfig

Defines flags that are used to run the diagnostic tool

JSON representation  
---  
      
    
    {
      "gcsBucket": string,
      "relativePath": string,
      "repairFlagEnabled": boolean,
      "packetCaptureFlagEnabled": boolean,
      "copyHomeFilesFlagEnabled": boolean
    }  
  
Fields  
---  
`gcsBucket` |  `string` Required. User Cloud Storage bucket location (REQUIRED). Must be formatted with path prefix (`gs://$GCS_BUCKET`).Permissions: User Managed Notebooks: - storage.buckets.writer: Must be given to the project's service account attached to VM. Google Managed Notebooks: - storage.buckets.writer: Must be given to the project's service account or user credentials attached to VM depending on authentication mode.Cloud Storage bucket Log file will be written to `gs://$GCS_BUCKET/$RELATIVE_PATH/$VM_DATE_$TIME.tar.gz`  
`relativePath` |  `string` Optional. Defines the relative storage path in the Cloud Storage bucket where the diagnostic logs will be written: Default path will be the root directory of the Cloud Storage bucket (`gs://$GCS_BUCKET/$DATE_$TIME.tar.gz`) Example of full path where Log file will be written: `gs://$GCS_BUCKET/$RELATIVE_PATH/`  
`repairFlagEnabled` |  `boolean` Optional. Enables flag to repair service for instance  
`packetCaptureFlagEnabled` |  `boolean` Optional. Enables flag to capture packets from the instance for 30 seconds  
`copyHomeFilesFlagEnabled` |  `boolean` Optional. Enables flag to copy all `/home/jupyter` folder contents  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
