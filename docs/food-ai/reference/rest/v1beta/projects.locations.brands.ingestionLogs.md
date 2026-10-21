---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs
title: REST Resource: projects.locations.brands.ingestionLogs \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:32:59.531589+00:00
---

# REST Resource: projects.locations.brands.ingestionLogs  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.ingestionLogs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: IngestionLog
    * JSON representation
  * State
  * IngestionPhase
    * JSON representation
  * Phase
  * State
  * Methods



## Resource: IngestionLog

A record of a menu ingestion run.

JSON representation  
---  
      
    
    {
      "name": string,
      "store": string,
      "state": enum ([State](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs#State)),
      "startTime": string,
      "endTime": string,
      "phases": [
        {
          object ([IngestionPhase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs#IngestionPhase))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the ingestion log. Format: projects/{project}/locations/{location}/brands/{brand}/ingestionLogs/{ingestionLog}  
`store` |  `string` Optional. The resource name of the store for the ingestion. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`state` |  `enum (`[State](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs#State)`)` Output only. Data about the current state of the ingestion.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when ingestion job started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when ingestion job finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`phases[]` |  `object (`[IngestionPhase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs#IngestionPhase)`)` Output only. List of phase runtimes.  
  
## State

The status of the ingestion run.

Enums  
---  
`STATE_UNSPECIFIED` | The status is unspecified.  
`SUCCEEDED` | The ingestion was successful.  
`FAILED` | The ingestion failed.  
`PROCESSING` | The ingestion is being processed.  
  
## IngestionPhase

A phase of the ingestion run.

JSON representation  
---  
      
    
    {
      "phase": enum ([Phase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs#Phase)),
      "startTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs#State_1)),
      "details": string
    }  
  
Fields  
---  
`phase` |  `enum (`[Phase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs#Phase)`)` Required. Name of the phase.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Start time of the phase.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. End time of the phase.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs#State_1)`)` Optional. State of the phase. Set by the caller on append, so it's an input, not a resource state.  
`details` |  `string` Optional. Details about the phase.  
  
## Phase

Enum for the name of the phase.

Enums  
---  
`PHASE_UNSPECIFIED` | The phase is unspecified.  
`READ_SOURCE_MENU` | Reading the source menu.  
`PARSE_SOURCE_MENU` | Parsing the source menu.  
`BRAND_SPECIFIC_VALIDATION` | Validating the brand specific configuration.  
`BRAND_AGNOSTIC_VALIDATION` | Validating the brand agnostic configuration.  
`CREATE_MENU` | Creating the menu.  
  
## State

The execution state of the phase.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unspecified.  
`SUCCEEDED` | The phase completed successfully.  
`FAILED` | The phase failed.  
  
## Methods  
  
---  
  
### `[appendIngestionPhase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/appendIngestionPhase)`

|  Appends an ingestion phase to an ingestion log.  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/create)`

|  Creates an ingestion log.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/delete)`

|  Deletes the specified ingestion log.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/get)`

|  Gets an ingestion log.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/list)`

|  Lists ingestion logs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-09 UTC."],[],[]] 
