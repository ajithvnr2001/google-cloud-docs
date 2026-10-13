---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken/
title: MultiplexedSessionPrecommitToken \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:19.191468+00:00
---

# MultiplexedSessionPrecommitToken  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  MultiplexedSessionPrecommitToken Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



When a read-write transaction is executed on a multiplexed session, this precommit token is sent back to the client as a part of the `[Transaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction)` message in the `sessions.beginTransaction` response and also as a part of the `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` and `[PartialResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartialResultSet)` responses.

JSON representation  
---  
      
    
    {
      "precommitToken": string,
      "seqNum": integer
    }  
  
Fields  
---  
`precommitToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Opaque precommit token.A base64-encoded string.  
`seqNum` |  `integer` An incrementing seq number is generated on every precommit token that is returned. Clients should remember the precommit token with the highest sequence number from the current transaction attempt.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
