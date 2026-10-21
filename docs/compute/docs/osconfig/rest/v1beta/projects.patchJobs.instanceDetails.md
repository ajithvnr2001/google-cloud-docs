---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs.instanceDetails
title: REST Resource: projects.patchJobs.instanceDetails \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:26:46.394998+00:00
---

# REST Resource: projects.patchJobs.instanceDetails  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs.instanceDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.patchJobs.instanceDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PatchJobInstanceDetails
    * JSON representation
  * PatchState
  * Methods



## Resource: PatchJobInstanceDetails

Patch details for a VM instance. For more information about reviewing VM instance details, see [Listing all VM instance details for a specific patch job](https://cloud.google.com/compute/docs/os-patch-management/manage-patch-jobs#list-instance-details).

JSON representation  
---  
      
    
    {
      "name": string,
      "instanceSystemId": string,
      "state": enum ([PatchState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs.instanceDetails#PatchState)),
      "failureReason": string,
      "attemptCount": string
    }  
  
Fields  
---  
`name` |  `string` The instance name in the form `projects/*/zones/*/instances/*`  
`instanceSystemId` |  `string` The unique identifier for the instance. This identifier is defined by the server.  
`state` |  `enum (`[PatchState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs.instanceDetails#PatchState)`)` Current state of instance patch.  
`failureReason` |  `string` If the patch fails, this field provides the reason.  
`attemptCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of times the agent that the agent attempts to apply the patch.  
  
## PatchState

Patch state of an instance.

Enums  
---  
`PATCH_STATE_UNSPECIFIED` | Unspecified.  
`PENDING` | The instance is not yet notified.  
`INACTIVE` | Instance is inactive and cannot be patched.  
`NOTIFIED` | The instance is notified that it should be patched.  
`STARTED` | The instance has started the patching process.  
`DOWNLOADING_PATCHES` | The instance is downloading patches.  
`APPLYING_PATCHES` | The instance is applying patches.  
`REBOOTING` | The instance is rebooting.  
`SUCCEEDED` | The instance has completed applying patches.  
`SUCCEEDED_REBOOT_REQUIRED` | The instance has completed applying patches but a reboot is required.  
`FAILED` | The instance has failed to apply the patch.  
`ACKED` | The instance acked the notification and will start shortly.  
`TIMED_OUT` | The instance exceeded the time out while applying the patch.  
`RUNNING_PRE_PATCH_STEP` | The instance is running the pre-patch step.  
`RUNNING_POST_PATCH_STEP` | The instance is running the post-patch step.  
`NO_AGENT_DETECTED` | The service could not detect the presence of the agent. Check to ensure that the agent is installed, running, and able to communicate with the service.  
`SKIPPED` | The instance was skipped during patching due to one of two reasons:

  1. The instance runs Container-Optimized OS (COS), which cannot be patched.
  2. The patch job's configuration prohibits patching on Managed Instance Groups (MIGs), and the instance is part of one.

  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs.instanceDetails/list)`

|  Get a list of instance details for a given patch job.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
