---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CommitLogEntry/
title: CommitLogEntry \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:48:56.493111+00:00
---

# CommitLogEntry  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CommitLogEntry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  CommitLogEntry Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Represents a single commit log.

JSON representation  
---  
      
    
    {
      "commitTime": string,
      "commitSha": string,
      "author": {
        object ([CommitAuthor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CommitAuthor))
      },
      "commitMessage": string
    }  
  
Fields  
---  
`commitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Commit timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commitSha` |  `string` The commit SHA for this commit log entry.  
`author` |  `object (`[CommitAuthor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CommitAuthor)`)` The commit author for this commit log entry.  
`commitMessage` |  `string` The commit message for this commit log entry.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
