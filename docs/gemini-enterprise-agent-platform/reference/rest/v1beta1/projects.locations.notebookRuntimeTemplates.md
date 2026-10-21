---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates
title: REST Resource: projects.locations.notebookRuntimeTemplates \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:42:23.329611+00:00
---

# REST Resource: projects.locations.notebookRuntimeTemplates  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.notebookRuntimeTemplates Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: NotebookRuntimeTemplate

A template that specifies runtime configurations such as machine type, runtime version, network configurations, etc. Multiple runtimes can be created from a runtime template.

Fields  
  
`name` `string` The resource name of the NotebookRuntimeTemplate. | `displayName` `string` Required. The display name of the NotebookRuntimeTemplate. The name can be up to 128 characters long and can consist of any UTF-8 characters. | `description` `string` The description of the NotebookRuntimeTemplate. | `isDefault  
**(deprecated)**` `boolean` This item is deprecated!Output only. Deprecated: This field has no behavior. Use notebookRuntimeType = 'ONE_CLICK' instead.The default template to use if not specified. | `machineSpec` `object (`MachineSpec`)` Optional. Immutable. The specification of a single machine for the template. | `dataPersistentDiskSpec` `object (`[PersistentDiskSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PersistentDiskSpec)`)` Optional. The specification of [persistent disk][https://cloud.google.com/compute/docs/disks/persistent-disks] attached to the runtime as data disk storage. | `networkSpec` `object (`[NetworkSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NetworkSpec)`)` Optional. Network spec. | `serviceAccount  
**(deprecated)**` `string` This item is deprecated!Deprecated: This field is ignored and the "Agent Platform Notebook service Account" ([service-PROJECT_NUMBER@gcp-sa-aiplatform-vm.iam.gserviceaccount.com](mailto:service-PROJECT_NUMBER@gcp-sa-aiplatform-vm.iam.gserviceaccount.com)) is used for the runtime workload identity. See <https://cloud.google.com/iam/docs/service-agents#vertex-ai-notebook-service-account> for more details. For NotebookExecutionJob, use NotebookExecutionJob.service_account instead.The service account that the runtime workload runs as. You can use any service account within the same project, but you must have the service account user permission to use the instance.If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. | `etag` `string` Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. | `labels` `map (key: string, value: string)` The labels with user-defined metadata to organize the NotebookRuntimeTemplates.label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.See <https://goo.gl/xmQnxf> for more information and examples of labels. | `idleShutdownConfig` `object (`[NotebookIdleShutdownConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NotebookIdleShutdownConfig)`)` The idle shutdown configuration of NotebookRuntimeTemplate. This config will only be set when idle shutdown is enabled. | `eucConfig` `object (`[NotebookEucConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NotebookEucConfig)`)` EUC configuration of the NotebookRuntimeTemplate. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this NotebookRuntimeTemplate was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this NotebookRuntimeTemplate was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `notebookRuntimeType` `enum (`[NotebookRuntimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NotebookRuntimeType)`)` Optional. Immutable. The type of the notebook runtime template. | `shieldedVmConfig` `object (`[ShieldedVmConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ShieldedVmConfig)`)` Optional. Immutable. Runtime Shielded VM spec. | `networkTags[]` `string` Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/vpc/docs/add-remove-network-tags)). | `encryptionSpec` `object (`[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/EncryptionSpec)`)` Customer-managed encryption key spec for the notebook runtime. | `softwareConfig` `object (`[NotebookSoftwareConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NotebookSoftwareConfig)`)` Optional. The notebook software configuration of the notebook runtime. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "isDefault": boolean,
      "machineSpec": {
        object (MachineSpec)
      },
      "dataPersistentDiskSpec": {
        object ([PersistentDiskSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PersistentDiskSpec))
      },
      "networkSpec": {
        object ([NetworkSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NetworkSpec))
      },
      "serviceAccount": string,
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "idleShutdownConfig": {
        object ([NotebookIdleShutdownConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NotebookIdleShutdownConfig))
      },
      "eucConfig": {
        object ([NotebookEucConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NotebookEucConfig))
      },
      "createTime": string,
      "updateTime": string,
      "notebookRuntimeType": enum ([NotebookRuntimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NotebookRuntimeType)),
      "shieldedVmConfig": {
        object ([ShieldedVmConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ShieldedVmConfig))
      },
      "networkTags": [
        string
      ],
      "encryptionSpec": {
        object ([EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/EncryptionSpec))
      },
      "softwareConfig": {
        object ([NotebookSoftwareConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/NotebookSoftwareConfig))
      }
    }  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/create)`

|  Creates a NotebookRuntimeTemplate.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/delete)`

|  Deletes a NotebookRuntimeTemplate.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/get)`

|  Gets a NotebookRuntimeTemplate.  
  
### `[getIamPolicy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/list)`

|  Lists NotebookRuntimeTemplates in a Location.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/patch)`

|  Updates a NotebookRuntimeTemplate.  
  
### `[setIamPolicy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
