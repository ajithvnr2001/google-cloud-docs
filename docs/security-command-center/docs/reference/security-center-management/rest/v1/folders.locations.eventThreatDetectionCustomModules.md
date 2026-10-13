---
url: https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules
title: REST Resource: folders.locations.eventThreatDetectionCustomModules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:14.400529+00:00
---

# REST Resource: folders.locations.eventThreatDetectionCustomModules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  REST Resource: folders.locations.eventThreatDetectionCustomModules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EventThreatDetectionCustomModule
    * JSON representation
    * EnablementState
  * Methods



## Resource: EventThreatDetectionCustomModule

A Security Command Center resource that contains the configuration and enablement state of a custom module, which enables Event Threat Detection to write certain findings to Security Command Center.

JSON representation  
---  
      
    
    {
      "name": string,
      "config": {
        object
      },
      "ancestorModule": string,
      "enablementState": enum ([EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules#EventThreatDetectionCustomModule.EnablementState)),
      "type": string,
      "displayName": string,
      "description": string,
      "updateTime": string,
      "lastEditor": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the Event Threat Detection custom module, in one of the following formats:

  * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`

  
`config` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Configuration for the module. For the resident module, its configuration value is defined at this level. For the inherited module, its configuration value is inherited from the ancestor module.  
`ancestorModule` |  `string` Output only. The closest ancestor module that this module inherits the enablement state from. If empty, indicates that the custom module was created in the requesting parent organization, folder, or project. The format is the same as the custom module's resource name.  
`enablementState` |  `enum (`[EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules#EventThreatDetectionCustomModule.EnablementState)`)` Optional. The state of enablement for the module at the given level of the hierarchy.  
`type` |  `string` Optional. Type for the module. For example, `CONFIGURABLE_BAD_IP`.  
`displayName` |  `string` Optional. The human-readable name of the module.  
`description` |  `string` Optional. A description of the module.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the module was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastEditor` |  `string` Output only. The editor the module was last updated by.  
  
### EnablementState

The enablement state of the module.

Enums  
---  
`ENABLEMENT_STATE_UNSPECIFIED` | Unspecified enablement state.  
`ENABLED` | The module is enabled at the given level.  
`DISABLED` | The module is disabled at the given level.  
`INHERITED` | State is inherited from an ancestor module. The module will either be effectively `ENABLED` or `DISABLED` based on its closest non-inherited ancestor module in the CRM hierarchy. If you try to set a top-level module (a module with no parent) to the `INHERITED` state, you receive an `INVALID_ARGUMENT` error.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/create)`

|  Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent.  
  
### `[delete](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/delete)`

|  Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy.  
  
### `[get](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/get)`

|  Gets an Event Threat Detection custom module.  
  
### `[list](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/list)`

|  Lists all Event Threat Detection custom modules for the given organization, folder, or project.  
  
### `[listDescendant](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/listDescendant)`

|  Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.  
  
### `[patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/patch)`

|  Updates the Event Threat Detection custom module with the given name based on the given update mask.  
  
### `[validate](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.eventThreatDetectionCustomModules/validate)`

|  Validates the given Event Threat Detection custom module.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
