---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/patch/
title: Method: projects.locations.instances.patch \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:42:02.071274+00:00
---

# Method: projects.locations.instances.patch  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.instances.patch Stay organized with collections  Save and categorize content based on your preferences. 

instances.patch updates an Instance.

### HTTP request

`PATCH https://notebooks.googleapis.com/v2/{instance.name}`

### Path parameters

Parameters  
---  
`instance.name` |  `string` Output only. Identifier. The name of this notebook instance. Format: `projects/{projectId}/locations/{location}/instances/{instanceId}`  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Mask used to update an instance. Updatable fields:

  * `labels`
  * `gceSetup.min_cpu_platform`
  * `gceSetup.metadata`
  * `gceSetup.machine_type`
  * `gceSetup.accelerator_configs`
  * `gceSetup.accelerator_configs.type`
  * `gceSetup.accelerator_configs.core_count`
  * `gceSetup.gpu_driver_config`
  * `gceSetup.gpu_driver_config.enable_gpu_driver`
  * `gceSetup.gpu_driver_config.custom_gpu_driver_path`
  * `gceSetup.shielded_instance_config`
  * `gceSetup.shielded_instance_config.enable_secure_boot`
  * `gceSetup.shielded_instance_config.enable_vtpm`
  * `gceSetup.shielded_instance_config.enable_integrity_monitoring`
  * `gceSetup.reservation_affinity`
  * `gceSetup.reservation_affinity.consume_reservation_type`
  * `gceSetup.reservation_affinity.key`
  * `gceSetup.reservation_affinity.values`
  * `gceSetup.tags`
  * `gceSetup.container_image`
  * `gceSetup.container_image.repository`
  * `gceSetup.container_image.tag`
  * `gceSetup.disable_public_ip`
  * `disableProxyAccess`

Note: `gceSetup.disable_public_ip` and `disableProxyAccess` are one-way on update -- they can only be used to _disable_ the feature (set the field to `true`). Requests that set either field back to `false` (re-enabling the external IP or proxy access) are rejected with `INVALID_ARGUMENT`.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`requestId` |  `string` Optional. Idempotent request UUID.  
  
### Request body

The request body contains an instance of `[Instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances#Instance)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/notebooks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
