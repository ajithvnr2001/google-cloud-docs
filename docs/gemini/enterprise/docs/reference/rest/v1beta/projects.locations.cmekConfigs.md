---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs
title: REST Resource: projects.locations.cmekConfigs \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:48.397122+00:00
---

# REST Resource: projects.locations.cmekConfigs  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.cmekConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CmekConfig
    * JSON representation
    * State
    * SingleRegionKey
      * JSON representation
    * NotebookLMState
  * Methods



## Resource: CmekConfig

Configurations used to enable CMEK data encryption with Cloud KMS keys.

JSON representation  
---  
      
    
    {
      "name": string,
      "kmsKey": string,
      "kmsKeyVersion": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs#CmekConfig.State)),
      "isDefault": boolean,
      "lastRotationTimestampMicros": string,
      "singleRegionKeys": [
        {
          object ([SingleRegionKey](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs#CmekConfig.SingleRegionKey))
        }
      ],
      "notebooklmState": enum ([NotebookLMState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs#CmekConfig.NotebookLMState))
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the CmekConfig of the form `projects/{project}/locations/{location}/cmekConfig` or `projects/{project}/locations/{location}/cmekConfigs/{cmekConfig}`.  
`kmsKey` |  `string` Required. KMS key resource name which will be used to encrypt resources `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{keyId}`.  
`kmsKeyVersion` |  `string` Output only. KMS key version resource name which will be used to encrypt resources `<kmsKey>/cryptoKeyVersions/{keyVersion}`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs#CmekConfig.State)`)` Output only. The states of the CmekConfig.  
`isDefault` |  `boolean` Output only. The default CmekConfig for the Customer.  
`lastRotationTimestampMicros` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The timestamp of the last key rotation.  
`singleRegionKeys[]` |  `object (`[SingleRegionKey](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs#CmekConfig.SingleRegionKey)`)` Optional. Single-regional CMEKs that are required for some VAIS features.  
`notebooklmState` |  `enum (`[NotebookLMState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs#CmekConfig.NotebookLMState)`)` Output only. Whether the NotebookLM Corpus is ready to be used.  
  
### State

States of the CmekConfig.

Enums  
---  
`STATE_UNSPECIFIED` | The CmekConfig state is unknown.  
`CREATING` | The CmekConfig is creating.  
`ACTIVE` | The CmekConfig can be used with DataStores.  
`KEY_ISSUE` | The CmekConfig is unavailable, most likely due to the KMS Key being revoked.  
`DELETING` | The CmekConfig is deleting.  
`DELETE_FAILED` | The CmekConfig deletion process failed.  
`UNUSABLE` | The CmekConfig is not usable, most likely due to some internal issue.  
`ACTIVE_ROTATING` | The KMS key version is being rotated.  
`DELETED` | The KMS key is soft deleted. Some cleanup policy will eventually be applied.  
`EXPIRED` | The KMS key is expired, meaning the key has been disabled for 30+ days. The customer can call cmekConfigs.delete to change the state to DELETED.  
  
### SingleRegionKey

Metadata for single-regional CMEKs.

JSON representation  
---  
      
    
    {
      "kmsKey": string
    }  
  
Fields  
---  
`kmsKey` |  `string` Required. Single-regional kms key resource name which will be used to encrypt resources `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{keyId}`.  
  
### NotebookLMState

States of NotebookLM.

Enums  
---  
`NOTEBOOK_LM_STATE_UNSPECIFIED` | The NotebookLM state is unknown.  
`NOTEBOOK_LM_NOT_READY` | The NotebookLM is not ready.  
`NOTEBOOK_LM_READY` | The NotebookLM is ready to be used.  
`NOTEBOOK_LM_NOT_ENABLED` | The NotebookLM is not enabled.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs/delete)`

|  De-provisions a CmekConfig.  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs/get)`

|  Gets the `[CmekConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs#CmekConfig)`.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs/list)`

|  Lists all the `[CmekConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs#CmekConfig)`s with the project.  
  
### `[patch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.cmekConfigs/patch)`

|  Provisions a CMEK key for use in a location of a customer's project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
