---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ChangeQuorumMetadata/
title: ChangeQuorumMetadata \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:58.168556+00:00
---

# ChangeQuorumMetadata  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ChangeQuorumMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  ChangeQuorumMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ChangeQuorumRequest
    * JSON representation



Metadata type for the long-running operation returned by `[databases.changequorum](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/changequorum#google.spanner.admin.database.v1.DatabaseAdmin.ChangeQuorum)`.

JSON representation  
---  
      
    
    {
      "request": {
        object ([ChangeQuorumRequest](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ChangeQuorumMetadata#ChangeQuorumRequest))
      },
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`request` |  `object (`[ChangeQuorumRequest](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ChangeQuorumMetadata#ChangeQuorumRequest)`)` The request for `[databases.changequorum](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/changequorum#google.spanner.admin.database.v1.DatabaseAdmin.ChangeQuorum)`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the request was received.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` If set, the time at which this operation failed or was completed successfully.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ChangeQuorumRequest

The request for `[databases.changequorum](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/changequorum#google.spanner.admin.database.v1.DatabaseAdmin.ChangeQuorum)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "quorumType": {
        object ([QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#QuorumType))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the database in which to apply `databases.changequorum`. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`.  
`quorumType` |  `object (`[QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#QuorumType)`)` Required. The type of this quorum.  
`etag` |  `string` Optional. The etag is the hash of the `QuorumInfo`. The `databases.changequorum` operation is only performed if the etag matches that of the `QuorumInfo` in the current database resource. Otherwise the API returns an `ABORTED` error.The etag is used for optimistic concurrency control as a way to help prevent simultaneous change quorum requests that could create a race condition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
