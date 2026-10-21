---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/execute/
title: Method: projects.patchJobs.execute \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:51.035773+00:00
---

# Method: projects.patchJobs.execute  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/execute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.patchJobs.execute Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Patch VM instances by creating and running a patch job.

### HTTP request

`POST https://osconfig.googleapis.com/v1/{parent=projects/*}/patchJobs:execute`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project in which to run this patch in the form `projects/*`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "description": string,
      "instanceFilter": {
        object ([PatchInstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter))
      },
      "patchConfig": {
        object ([PatchConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig))
      },
      "duration": string,
      "dryRun": boolean,
      "displayName": string,
      "rollout": {
        object ([PatchRollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchRollout))
      }
    }  
  
Fields  
---  
`description` |  `string` Description of the patch job. Length of the description is limited to 1024 characters.  
`instanceFilter` |  `object (`[PatchInstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter)`)` Required. Instances to patch, either explicitly or filtered by some criteria such as zone or labels.  
`patchConfig` |  `object (`[PatchConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig)`)` Patch configuration being applied. If omitted, instances are patched using the default configurations.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration of the patch job. After the duration ends, the patch job times out.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`dryRun` |  `boolean` If this patch is a dry-run only, instances are contacted but will do nothing.  
`displayName` |  `string` Display name for this patch job. This does not have to be unique.  
`rollout` |  `object (`[PatchRollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchRollout)`)` Rollout strategy of the patch job.  
  
### Response body

If successful, the response body contains an instance of `[PatchJob](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs#PatchJob)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `osconfig.patchJobs.exec`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
