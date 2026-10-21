---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations
title: REST Resource: projects.locations.validations \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:45.648579+00:00
---

# REST Resource: projects.locations.validations  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  REST Resource: projects.locations.validations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Validation
    * JSON representation
  * Methods



## Resource: Validation

Represents a `Validation` dry run of a fault injection.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "action": {
        object ([Action](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action))
      },
      "state": enum ([State](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State)),
      "createTime": string,
      "stopTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique identifier for the `Validation` dry run. Format: `projects/{projectId}/locations/{location}/validations/{validationId}`.  
`displayName` |  `string` Optional. A human-readable name of the `Validation` dry run.  
`description` |  `string` Optional. Notes or details about the `Validation` dry run. Minimum length is 0, maximum length is 2000.  
`action` |  `object (`[Action](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action)`)` Required. The fault injection action being checked.  
`state` |  `enum (`[State](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State)`)` Output only. The current state of the `Validation` dry run. Either `PREPARING` or `COMPLETED`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when this `Validation` dry run was started (RFC3339 UTC "Zulu" format).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`stopTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when this `Validation` dry run finished (RFC3339 UTC "Zulu" format).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/create)`

|  Creates a new `Validation` dry run.  
  
### `[delete](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/delete)`

|  Deletes a record of a dry run.  
  
### `[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/get)`

|  Retrieves the details of a specific `Validation` dry run.  
  
### `[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/list)`

|  Lists all dry runs in a specified project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
