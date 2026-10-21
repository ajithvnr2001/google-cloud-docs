---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters
title: REST Resource: projects.configs.waiters \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:34.699305+00:00
---

# REST Resource: projects.configs.waiters  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  REST Resource: projects.configs.waiters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Waiter
    * JSON representation
  * EndCondition
    * JSON representation
  * Cardinality
    * JSON representation
  * Methods



## Resource: Waiter

A Waiter resource waits for some end condition within a RuntimeConfig resource to be met before it returns. For example, assume you have a distributed system where each node writes to a Variable resource indicating the node's readiness as part of the startup process.

You then configure a Waiter resource with the success condition set to wait until some number of nodes have checked in. Afterwards, your application runs some arbitrary code after the condition has been met and the waiter returns successfully.

Once created, a Waiter resource is immutable.

To learn more about using waiters, read the [Creating a Waiter](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter) documentation.

JSON representation  
---  
      
    
    {
      "name": string,
      "timeout": string,
      "failure": {
        object([EndCondition](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters#EndCondition))
      },
      "success": {
        object([EndCondition](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters#EndCondition))
      },
      "createTime": string,
      "done": boolean,
      "error": {
        object([Status](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/Shared.Types/Operation#Status))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the Waiter resource, in the format:
    
    
    projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]
    

The `[PROJECT_ID]` must be a valid Google Cloud project ID, the `[CONFIG_NAME]` must be a valid RuntimeConfig resource, the `[WAITER_NAME]` must match RFC 1035 segment specification, and the length of `[WAITER_NAME]` must be less than 64 bytes.After you create a Waiter resource, you cannot change the resource name.  
`timeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` [Required] Specifies the timeout of the waiter in seconds, beginning from the instant that `waiters().create` method is called. If this time elapses before the success or failure conditions are met, the waiter fails and sets the `error` code to `DEADLINE_EXCEEDED`.A duration in seconds with up to nine fractional digits, terminated by '`s`'. Example: `"3.5s"`.  
`failure` |  `object(`[EndCondition](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters#EndCondition)`)` [Optional] The failure condition of this waiter. If this condition is met, `done` will be set to `true` and the `error` code will be set to `ABORTED`. The failure condition takes precedence over the success condition. If both conditions are met, a failure will be indicated. This value is optional; if no failure condition is set, the only failure scenario will be a timeout.   
`success` |  `object(`[EndCondition](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters#EndCondition)`)` [Required] The success condition. If this condition is met, `done` will be set to `true` and the `error` value will remain unset. The failure condition takes precedence over the success condition. If both conditions are met, a failure will be indicated.   
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The instant at which this Waiter resource was created. Adding the value of `timeout` to this instant yields the timeout deadline for the waiter.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.  
`done` |  `boolean` Output only. If the value is `false`, it means the waiter is still waiting for one of its conditions to be met.If true, the waiter has finished. If the waiter finished due to a timeout or failure, `error` will be set.  
`error` |  `object(`[Status](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/Shared.Types/Operation#Status)`)` Output only. If the waiter ended due to a failure or timeout, this value will be set.   
  
## EndCondition

The condition that a Waiter resource is waiting for.

JSON representation  
---  
      
    
    {
      "cardinality": {
        object([Cardinality](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters#Cardinality))
      }
    }  
  
Fields  
---  
`cardinality` |  `object(`[Cardinality](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters#Cardinality)`)` The cardinality of the `EndCondition`.   
  
## Cardinality

A Cardinality condition for the Waiter resource. A cardinality condition is met when the number of variables under a specified path prefix reaches a predefined number. For example, if you set a Cardinality condition where the `path` is set to `/foo` and the number of paths is set to `2`, the following variables would meet the condition in a RuntimeConfig resource:

  * `/foo/variable1 = "value1"`
  * `/foo/variable2 = "value2"`
  * `/bar/variable3 = "value3"`



It would not satisfy the same condition with the `number` set to `3`, however, because there is only 2 paths that start with `/foo`. Cardinality conditions are recursive; all subtrees under the specific path prefix are counted.

JSON representation  
---  
      
    
    {
      "path": string,
      "number": number
    }  
  
Fields  
---  
`path` |  `string` The root of the variable subtree to monitor. For example, `/foo`.   
`number` |  `number` The number variables under the `path` that must exist to meet this condition. Defaults to 1 if not specified.   
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/create)`

|  Creates a Waiter resource.  
  
### `[delete](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/delete)`

|  Deletes the waiter with the specified name.  
  
### `[get](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/get)`

|  Gets information about a single waiter.  
  
### `[list](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/list)`

|  List waiters within the given configuration.  
  
### `[testIamPermissions](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
