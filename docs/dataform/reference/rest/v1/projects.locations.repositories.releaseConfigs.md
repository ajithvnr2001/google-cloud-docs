---
url: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs
title: REST Resource: projects.locations.repositories.releaseConfigs \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:05.438617+00:00
---

# REST Resource: projects.locations.repositories.releaseConfigs  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.repositories.releaseConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ReleaseConfig
    * JSON representation
  * ScheduledReleaseRecord
    * JSON representation
  * Methods



## Resource: ReleaseConfig

Represents a Dataform release configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "gitCommitish": string,
      "codeCompilationConfig": {
        object ([CodeCompilationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig))
      },
      "cronSchedule": string,
      "timeZone": string,
      "recentScheduledReleaseRecords": [
        {
          object ([ScheduledReleaseRecord](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs#ScheduledReleaseRecord))
        }
      ],
      "releaseCompilationResult": string,
      "disabled": boolean,
      "internalMetadata": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The release config's name.  
`gitCommitish` |  `string` Required. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` \- a tag: `tag1` \- a branch name: `branch1`  
`codeCompilationConfig` |  `object (`[CodeCompilationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig)`)` Optional. If set, fields of `codeCompilationConfig` override the default compilation settings that are specified in dataform.json.  
`cronSchedule` |  `string` Optional. Optional schedule (in cron format) for automatic creation of compilation results.  
`timeZone` |  `string` Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is `UTC`.  
`recentScheduledReleaseRecords[]` |  `object (`[ScheduledReleaseRecord](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs#ScheduledReleaseRecord)`)` Output only. Records of the 10 most recent scheduled release attempts, ordered in descending order of `releaseTime`. Updated whenever automatic creation of a compilation result is triggered by cronSchedule.  
`releaseCompilationResult` |  `string` Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is automatically created from this release config (using cronSchedule), or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.  
`disabled` |  `boolean` Optional. Disables automatic creation of compilation results.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
## ScheduledReleaseRecord

A record of an attempt to create a compilation result for this release config.

JSON representation  
---  
      
    
    {
      "releaseTime": string,
    
      // Union field result can be only one of the following:
      "compilationResult": string,
      "errorStatus": {
        object ([Status](https://docs.cloud.google.com/dataform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`releaseTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of this release attempt.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `result`. The result of this release attempt. `result` can be only one of the following:  
`compilationResult` |  `string` The name of the created compilation result, if one was successfully created. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.  
`errorStatus` |  `object (`[Status](https://docs.cloud.google.com/dataform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error status encountered upon this attempt to create the compilation result, if the attempt was unsuccessful.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/create)`

|  Creates a new ReleaseConfig in a given Repository.  
  
### `[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/delete)`

|  Deletes a single ReleaseConfig.  
  
### `[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/get)`

|  Fetches a single ReleaseConfig.  
  
### `[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/list)`

|  Lists ReleaseConfigs in a given Repository.  
  
### `[patch](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/patch)`

|  Updates a single ReleaseConfig.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
