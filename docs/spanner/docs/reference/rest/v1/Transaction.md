---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction/
title: Transaction \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:22.665918+00:00
---

# Transaction  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Transaction Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A transaction.

JSON representation  
---  
      
    
    {
      "id": string,
      "readTimestamp": string,
      "precommitToken": {
        object ([MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken))
      }
    }  
  
Fields  
---  
`id` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` `id` may be used to identify the transaction in subsequent `[sessions.read](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#google.spanner.v1.Spanner.Read)`, `[ExecuteSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#google.spanner.v1.Spanner.ExecuteSql)`, `[Commit](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#google.spanner.v1.Spanner.Commit)`, or `[sessions.rollback](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/rollback#google.spanner.v1.Spanner.Rollback)` calls.Single-use read-only transactions do not have IDs, because single-use transactions do not support multiple requests.A base64-encoded string.  
`readTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` For snapshot read-only transactions, the read timestamp chosen for the transaction. Not returned by default: see `[TransactionOptions.ReadOnly.return_read_timestamp](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#ReadOnly.FIELDS.return_read_timestamp)`.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`precommitToken` |  `object (`[MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken)`)` A precommit token is included in the response of a sessions.beginTransaction request if the read-write transaction is on a multiplexed session and a mutationKey was specified in the `sessions.beginTransaction`. The precommit token with the highest sequence number from this transaction attempt should be passed to the `[Commit](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#google.spanner.v1.Spanner.Commit)` request for this transaction.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
