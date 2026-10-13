---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/addSplitPoints/
title: Method: projects.instances.databases.addSplitPoints \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:05.421387+00:00
---

# Method: projects.instances.databases.addSplitPoints  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/addSplitPoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.addSplitPoints Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * SplitPoints
    * JSON representation
  * Key
    * JSON representation
  * Try it!



Adds split points to specified tables and indexes of a database.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{database=projects/*/instances/*/databases/*}:addSplitPoints`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`database` |  `string` Required. The database on whose tables or indexes the split points are to be added. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.databases.addSplitPoints`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "splitPoints": [
        {
          object ([SplitPoints](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/addSplitPoints#SplitPoints))
        }
      ],
      "initiator": string
    }  
  
Fields  
---  
`splitPoints[]` |  `object (`[SplitPoints](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/addSplitPoints#SplitPoints)`)` Required. The split points to add.  
`initiator` |  `string` Optional. A user-supplied tag associated with the split points. For example, "initial_data_load", "special_event_1". Defaults to "CloudAddSplitPointsAPI" if not specified. The length of the tag must not exceed 50 characters, or else it is trimmed. Only valid UTF8 characters are allowed.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## SplitPoints

The split points of a table or an index.

JSON representation  
---  
      
    
    {
      "table": string,
      "index": string,
      "keys": [
        {
          object ([Key](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/addSplitPoints#Key))
        }
      ],
      "expireTime": string
    }  
  
Fields  
---  
`table` |  `string` The table to split.  
`index` |  `string` The index to split. If specified, the `table` field must refer to the index's base table.  
`keys[]` |  `object (`[Key](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/addSplitPoints#Key)`)` Required. The list of split keys. In essence, the split boundaries.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The expiration timestamp of the split points. A timestamp in the past means immediate expiration. The maximum value can be 30 days in the future. Defaults to 10 days in the future if not specified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Key

A split key.

JSON representation  
---  
      
    
    {
      "keyParts": array
    }  
  
Fields  
---  
`keyParts` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Required. The column values making up the split key.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
