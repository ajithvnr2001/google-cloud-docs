---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments
title: REST Resource: projects.locations.experiments \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:42.741960+00:00
---

# REST Resource: projects.locations.experiments  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  REST Resource: projects.locations.experiments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Experiment
    * JSON representation
  * EndReason
  * Methods



## Resource: Experiment

Represents a single fault injection experiment where faults are deliberately introduced to your cloud resources to see how your application responds.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "experimentTemplate": string,
      "templateDisplayName": string,
      "templateDescription": string,
      "templateDuration": string,
      "effectiveAction": {
        object ([Action](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action))
      },
      "state": enum ([State](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State)),
      "endReason": enum ([EndReason](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments#EndReason)),
      "endNotes": string,
      "createTime": string,
      "startTime": string,
      "stateUpdateTime": string,
      "stopTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique identifier for the experiment. Format: `projects/{projectId}/locations/{location}/experiments/{experimentId}`.  
`displayName` |  `string` Optional. A human-readable name of the experiment.  
`description` |  `string` Optional. Notes or details to describe the purpose or context of the experiment. Minimum length is 0, maximum length is 2000.  
`experimentTemplate` |  `string` Required. The unique identifier of the reusable experiment template used to configure the experiment. This field determines the type of fault, target, and duration. Format: `projects/{projectId}/locations/{location}/experimentTemplates/{experimentTemplateId}`.  
`templateDisplayName` |  `string` Output only. The human-readable name of the experiment template used for the experiment. Minimum length is 0, maximum length is 1000.  
`templateDescription` |  `string` Output only. The description from the experiment template used for the experiment. Minimum length is 0, maximum length is 2000.  
`templateDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The planned duration of the experiment, as defined in the experiment template. Minimum duration is 1 minute, maximum is 10 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`effectiveAction` |  `object (`[Action](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action)`)` Output only. The specific fault that was introduced during the experiment. Examples: Triggering a database failover, adding delays to web requests. This field comes from the experiment template.  
`state` |  `enum (`[State](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State)`)` Output only. The current state of the experiment. Example: `PREPARING`, `INJECTED`, `COMPLETED`.  
`endReason` |  `enum (`[EndReason](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments#EndReason)`)` Output only. Why the experiment stopped. Example: It finished normally, or was cancelled by a user.  
`endNotes` |  `string` Output only. Optional user-added notes explaining why the experiment was stopped, particularly if it was manually cancelled.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when the experiment record was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when the fault injection actually began.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`stateUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when the experiment's state was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`stopTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when the experiment entered the REVERTING state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## EndReason

The reason why an experiment concluded. String values are used in JSON.

Enums  
---  
`END_REASON_UNSPECIFIED` | The reason for stopping is not specified.  
`CANCELLED` | A user manually stopped the experiment.  
`COMPLETED` | The experiment finished normally after its duration.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/create)`

|  Creates an `Experiment` and prepares it to run by identifying all cloud resources that will be affected.  
  
### `[delete](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/delete)`

|  Deletes an `Experiment` record.  
  
### `[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/get)`

|  Returns a single `Experiment` resource, including its current state and configuration.  
  
### `[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/list)`

|  Lists all experiments in a specified project and location.  
  
### `[start](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/start)`

|  Starts an existing `Experiment`.  
  
### `[stop](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/stop)`

|  Stops a running `Experiment`.  
  
### `[stopAll](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/stopAll)`

|  Stops all running experiments in a given location for a given project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-15 UTC."],[],[]] 
