---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun/
title: ConnectorRun \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:04.058415+00:00
---

# ConnectorRun  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  ConnectorRun Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * State
  * EntityRun
    * JSON representation
  * Progress
    * JSON representation
  * SyncType
  * Trigger



A data sync run of `[DataConnector](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections#DataConnector)`. After `[DataConnector](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections#DataConnector)` is successfully initialized, data syncs are scheduled at `[DataConnector.refresh_interval](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections#DataConnector.FIELDS.refresh_interval)`. A `[ConnectorRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun)` represents a data sync either in the past or onging that the moment. //

JSON representation  
---  
      
    
    {
      "name": string,
      "startTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#State)),
      "errors": [
        {
          object ([Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
        }
      ],
      "stateUpdateTime": string,
      "latestPauseTime": string,
      "entityRuns": [
        {
          object ([EntityRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#EntityRun))
        }
      ],
      "trigger": enum ([Trigger](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#Trigger))
    }  
  
Fields  
---  
`name` |  `string` Output only. The full resource name of the Connector Run. Format: `projects/*/locations/*/collections/*/dataConnector/connectorRuns/*`. The `connectorRunId` is system-generated.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the connector run started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the connector run ended.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#State)`)` Output only. The state of the sync run.  
`errors[]` |  `object (`[Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Contains info about errors incurred during the sync. Only exist if running into an error state. Contains error code and error message. Use with the `state` field.  
`stateUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` timestamp at which the connector run sync state was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`latestPauseTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the connector run was most recently paused.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`entityRuns[]` |  `object (`[EntityRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#EntityRun)`)` Output only. The details of the entities synced at the ConnectorRun. Each ConnectorRun consists of syncing one or more entities.  
`trigger` |  `enum (`[Trigger](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#Trigger)`)` Output only. The trigger for this `[ConnectorRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun)`.  
  
## State

The state of run.

Enums  
---  
`STATE_UNSPECIFIED` | Default value.  
`RUNNING` | The data sync is ongoing.  
`SUCCEEDED` | The data sync is finished.  
`FAILED` | The data sync is failed.  
`OVERRUN` | data sync has been running longer than expected and is still running at the time the next run is supposed to start.  
`CANCELLED` | data sync was scheduled but has been cancelled.  
`PENDING` | data sync is about to start.  
`WARNING` | The data sync completed with non-fatal errors.  
`SKIPPED` | An ongoing connector run has been running longer than expected, causing this run to be skipped.  
  
## EntityRun

Represents an entity that was synced in this `[ConnectorRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun)`.

JSON representation  
---  
      
    
    {
      "entityName": string,
      "state": enum ([State](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#State)),
      "errors": [
        {
          object ([Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
        }
      ],
      "stateUpdateTime": string,
      "progress": {
        object ([Progress](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#Progress))
      },
      "statsUpdateTime": string,
      "syncType": enum ([SyncType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#SyncType)),
      "scheduledRecordCount": string,
      "extractedRecordCount": string,
      "indexedRecordCount": string,
      "errorRecordCount": string,
      "sourceApiRequestCount": string,
      "deletedRecordCount": string
    }  
  
Fields  
---  
`entityName` |  `string` The name of the source entity.  
`state` |  `enum (`[State](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#State)`)` The state of the entity's sync run.  
`errors[]` |  `object (`[Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The errors from the entity's sync run. Only exist if running into an error state. Contains error code and error message.  
`stateUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` timestamp at which the entity sync state was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`progress` |  `object (`[Progress](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#Progress)`)` metadata to generate the progress bar.  
`statsUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp for either extracted_documents_count, indexed_documents_count and error_documents_count was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`syncType` |  `enum (`[SyncType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun#SyncType)`)` Sync type of this run.  
`scheduledRecordCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The number of documents scheduled to be crawled/extracted from connector source. This only applies to third party connectors.  
`extractedRecordCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The number of documents extracted from connector source, ready to be ingested to VAIS.  
`indexedRecordCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The number of documents indexed.  
`errorRecordCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The total number of documents failed at sync at indexing stage.  
`sourceApiRequestCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The number of requests sent to 3p API.  
`deletedRecordCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The number of documents deleted.  
  
## Progress

Represents the progress of a sync run.

JSON representation  
---  
      
    
    {
      "currentCount": string,
      "totalCount": string,
      "percentile": number
    }  
  
Fields  
---  
`currentCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The current progress.  
`totalCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total.  
`percentile` |  `number` Derived. The percentile of the progress.current_count / totalCount. The value is between [0, 1.0] inclusive.  
  
## SyncType

data synchronization type of the connector.

Enums  
---  
`SYNC_TYPE_UNSPECIFIED` | Sync type unspecified.  
`FULL` | Sync triggers full sync of all documents.  
`INCREMENTAL` | Incremental sync of updated documents.  
`REALTIME` | Realtime sync.  
`SCALA_SYNC` | Scala sync.  
  
## Trigger

Triggering reasons for `[ConnectorRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun)`.

Enums  
---  
`TRIGGER_UNSPECIFIED` | Default value.  
`SCHEDULER` | ConnectorRun triggered by scheduler if connector has PERIODIC sync mode.  
`INITIALIZATION` | ConnectorRun auto triggered by connector initialization.  
`RESUME` | ConnectorRun auto triggered by resuming connector.  
`MANUAL` | ConnectorRun triggered by user manually.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-26 UTC."],[],[]] 
