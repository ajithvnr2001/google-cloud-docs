---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/StatsEvent/
title: StatsEvent \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:17.798642+00:00
---

# StatsEvent  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/StatsEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  StatsEvent Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ErrorInfo
    * JSON representation

JSON representation  
---  
      
    
    {
      "startTime": string,
      "windowStartTime": string,
      "lastSuccessfulUpload": string,
      "numBatchesDropped": integer,
      "numBatchesUploaded": integer,
      "bytesUploaded": string,
      "bytesBeforeCompression": string,
      "bytesAfterCompression": string,
      "numUploadRetries": integer,
      "collectorHostname": string,
      "collectorVersion": string,
      "bundleVersion": string,
      "containerVersion": string,
      "numBatchesResized": integer,
      "numInputDropped": integer,
      "compressionLevel": integer,
      "pcapStats": {
        object ([PcapStats](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/PcapStats))
      },
      "lastFailedUpload": string,
      "lastAttemptedUpload": string,
      "lastFailedStatusCode": integer,
      "errorInfo": [
        {
          object ([ErrorInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/StatsEvent#ErrorInfo))
        }
      ],
      "rusage": {
        object ([RUsage](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/RUsage))
      },
      "lastReceivedTimestamp": {
        string: string,
        ...
      },
      "localLoggingVerbosityLevel": integer,
      "remoteLoggingVerbosityLevel": integer,
      "logs": [
        string
      ],
      "numSplunkInputRestarts": integer,
      "maxSplunkLatencyMs": integer,
      "minSplunkLatencyMs": integer,
      "numSplunkQueryAttempts": integer,
      "numLogLinesDiscarded": integer,
      "lastSplunkInputRestart": string,
      "commandLineArgs": string,
      "batchBacklogSizeBytes": {
        string: string,
        ...
      },
      "aggregatedBatchStats": {
        object ([LogEntryBatchMetrics](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/LogEntryBatchMetrics))
      },
      "inputStats": [
        {
          object ([InputStatsEvent](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/InputStatsEvent))
        }
      ],
      "containerStats": {
        object ([ContainerStats](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/ContainerStats))
      },
      "os": string,
      "osVersion": string,
      "ingestionLatency": string,
      "uploadTryCount": integer,
      "configHash": string,
      "authConfigHash": string,
      "forwarderId": string,
      "semanticVersion": string,
      "forwarderIdPersisted": boolean,
      "autoUpdateEnabled": boolean
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`windowStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSuccessfulUpload` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`numBatchesDropped  
**(deprecated)**` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!  
`numBatchesUploaded  
**(deprecated)**` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!  
`bytesUploaded  
**(deprecated)**` |  `string` This item is deprecated!  
`bytesBeforeCompression` |  `string`  
`bytesAfterCompression` |  `string`  
`numUploadRetries` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`collectorHostname` |  `string`  
`collectorVersion` |  `string`  
`bundleVersion` |  `string`  
`containerVersion` |  `string`  
`numBatchesResized  
**(deprecated)**` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!  
`numInputDropped` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`compressionLevel` |  `integer`  
`pcapStats` |  `object (`[PcapStats](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/PcapStats)`)`  
`lastFailedUpload` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastAttemptedUpload` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastFailedStatusCode` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`errorInfo[]` |  `object (`[ErrorInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/StatsEvent#ErrorInfo)`)`  
`rusage` |  `object (`[RUsage](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/RUsage)`)`  
`lastReceivedTimestamp` |  `map (key: string, value: string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format))` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`localLoggingVerbosityLevel` |  `integer`  
`remoteLoggingVerbosityLevel` |  `integer`  
`logs[]` |  `string`  
`numSplunkInputRestarts` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`maxSplunkLatencyMs` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`minSplunkLatencyMs` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`numSplunkQueryAttempts` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`numLogLinesDiscarded` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`lastSplunkInputRestart` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commandLineArgs` |  `string`  
`batchBacklogSizeBytes  
**(deprecated)**` |  `map (key: string, value: string)` This item is deprecated!An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`aggregatedBatchStats` |  `object (`[LogEntryBatchMetrics](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/LogEntryBatchMetrics)`)`  
`inputStats[]` |  `object (`[InputStatsEvent](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/InputStatsEvent)`)`  
`containerStats` |  `object (`[ContainerStats](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/ContainerStats)`)`  
`os` |  `string`  
`osVersion` |  `string`  
`ingestionLatency` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)`  
`uploadTryCount` |  `integer`  
`configHash` |  `string`  
`authConfigHash` |  `string`  
`forwarderId` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A base64-encoded string.  
`semanticVersion` |  `string`  
`forwarderIdPersisted` |  `boolean`  
`autoUpdateEnabled` |  `boolean`  
  
## ErrorInfo

JSON representation  
---  
      
    
    {
      "statusCode": integer,
      "count": integer
    }  
  
Fields  
---  
`statusCode` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`count` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-19 UTC."],[],[]] 
