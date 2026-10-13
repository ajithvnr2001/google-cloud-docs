---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs
title: REST Resource: projects.locations.hyperparameterTuningJobs \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:48.237813+00:00
---

# REST Resource: projects.locations.hyperparameterTuningJobs  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.hyperparameterTuningJobs Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: HyperparameterTuningJob

Represents a HyperparameterTuningJob. A HyperparameterTuningJob has a Study specification and multiple CustomJobs with identical CustomJob specification.

Fields  
  
`name` `string` Output only. Resource name of the HyperparameterTuningJob. | `displayName` `string` Required. The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. | `studySpec` `object (`[StudySpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/StudySpec)`)` Required. Study configuration of the HyperparameterTuningJob. | `maxTrialCount` `integer` Required. The desired total number of Trials. | `parallelTrialCount` `integer` Required. The desired number of Trials to run in parallel. | `maxFailedTrialCount` `integer` The number of failed Trials that need to be seen before failing the HyperparameterTuningJob.If set to 0, Agent Platform decides how many Trials must fail before the whole job fails. | `trialJobSpec` `object (`[CustomJobSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec)`)` Required. The spec of a trial job. The same spec applies to the CustomJobs created in all the trials. | `trials[]` `object (`[Trial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials#Trial)`)` Output only. Trials of the HyperparameterTuningJob. | `state` `enum (`[JobState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/JobState)`)` Output only. The detailed state of the job. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. time when the HyperparameterTuningJob was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `startTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `endTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. time when the HyperparameterTuningJob was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `error` `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED. | `labels` `map (key: string, value: string)` The labels with user-defined metadata to organize HyperparameterTuningJobs.label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.See <https://goo.gl/xmQnxf> for more information and examples of labels. | `encryptionSpec` `object (`[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/EncryptionSpec)`)` Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key. | `satisfiesPzs` `boolean` Output only. reserved for future use. | `satisfiesPzi` `boolean` Output only. reserved for future use. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "studySpec": {
        object ([StudySpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/StudySpec))
      },
      "maxTrialCount": integer,
      "parallelTrialCount": integer,
      "maxFailedTrialCount": integer,
      "trialJobSpec": {
        object ([CustomJobSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec))
      },
      "trials": [
        {
          object ([Trial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.studies.trials#Trial))
        }
      ],
      "state": enum ([JobState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/JobState)),
      "createTime": string,
      "startTime": string,
      "endTime": string,
      "updateTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "labels": {
        string: string,
        ...
      },
      "encryptionSpec": {
        object ([EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/EncryptionSpec))
      },
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/cancel)`

|  Cancels a HyperparameterTuningJob.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/create)`

|  Creates a HyperparameterTuningJob  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/delete)`

|  Deletes a HyperparameterTuningJob.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/get)`

|  Gets a HyperparameterTuningJob  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.hyperparameterTuningJobs/list)`

|  Lists HyperparameterTuningJobs in a Location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
