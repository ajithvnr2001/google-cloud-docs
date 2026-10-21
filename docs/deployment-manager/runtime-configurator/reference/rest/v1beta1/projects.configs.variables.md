---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables
title: REST Resource: projects.configs.variables \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:34.323512+00:00
---

# REST Resource: projects.configs.variables  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  REST Resource: projects.configs.variables Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Variable
    * JSON representation
  * VariableState
  * Methods



## Resource: Variable

Describes a single variable within a RuntimeConfig resource. The name denotes the hierarchical variable name. For example, `ports/serving_port` is a valid variable name. The variable value is an opaque string and only leaf variables can have values (that is, variables that do not have any child variables).

JSON representation  
---  
      
    
    {
      "name": string,
      "updateTime": string,
      "state": enum([VariableState](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#VariableState)),
    
      // Union field contents can be only one of the following:
      "value": string,
      "text": string
      // End of list of possible types for union field contents.
    }  
  
Fields  
---  
`name` |  `string` The name of the variable resource, in the format:
    
    
    projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_NAME]
    

The `[PROJECT_ID]` must be a valid project ID, `[CONFIG_NAME]` must be a valid RuntimeConfig resource and `[VARIABLE_NAME]` follows Unix file system file path naming.The `[VARIABLE_NAME]` can contain ASCII letters, numbers, slashes and dashes. Slashes are used as path element separators and are not part of the `[VARIABLE_NAME]` itself, so `[VARIABLE_NAME]` must contain at least one non-slash character. Multiple slashes are coalesced into single slash character. Each path segment should match [0-9A-Za-z](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables?:\[_.A-Za-z0-9-\]{0,62}\[_.A-Za-z0-9\])? regular expression. The length of a `[VARIABLE_NAME]` must be less than 256 characters.Once you create a variable, you cannot change the variable name.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time of the last variable update. Timestamp will be UTC timestamp.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.  
`state` |  `enum(`[VariableState](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#VariableState)`)` Output only. The current state of the variable. The variable state indicates the outcome of the `variables().watch` call and is visible through the `get` and `list` calls.   
Union field `contents`. The value of the variable. It can be either a binary or a string value. You must specify one of either `value` or `text`. Specifying both will cause the server to return an error. `contents` can be only one of the following:  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The binary value of the variable. The length of the value must be less than 4096 bytes. Empty values are also accepted. The value must be base64 encoded, and must comply with IETF RFC4648 (<https://www.ietf.org/rfc/rfc4648.txt>). Only one of `value` or `text` can be set.A base64-encoded string.  
`text` |  `string` The string value of the variable. The length of the value must be less than 4096 bytes. Empty values are also accepted. For example, `text: "my text value"`. The string must be valid UTF-8.   
  
## VariableState

The `VariableState` describes the last known state of the variable and is used during a `variables().watch` call to distinguish the state of the variable.

Enums  
---  
`VARIABLE_STATE_UNSPECIFIED` | Default variable state.  
`UPDATED` | The variable was updated, while `variables().watch` was executing.  
`DELETED` | The variable was deleted, while `variables().watch` was executing.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/create)`

|  Creates a variable within the given configuration.  
  
### `[delete](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/delete)`

|  Deletes a variable or multiple variables.  
  
### `[get](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/get)`

|  Gets information about a single variable.  
  
### `[list](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list)`

|  Lists variables within given a configuration, matching any provided filters.  
  
### `[testIamPermissions](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[update](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/update)`

|  Updates an existing variable with a new value.  
  
### `[watch](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/watch)`

|  Watches a specific variable and waits for a change in the variable's value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
