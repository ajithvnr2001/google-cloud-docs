---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/Trial/
title: Trial \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:10.487310+00:00
---

# Trial  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/Trial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  Trial Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * State
  * EndReason



Represents a Trial for a project.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/Trial#State)),
      "startTime": string,
      "endTime": string,
      "endReason": enum ([EndReason](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/Trial#EndReason))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the trial. Format: projects/{project}/locations/{location}/trial  
`state` |  `enum (`[State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/Trial#State)`)` Output only. The state of the trial.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the trial was subscribed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the trial will expire.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endReason` |  `enum (`[EndReason](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/Trial#EndReason)`)` Output only. The reason for ending the trial.  
  
## State

Trial state enum.

Enums  
---  
`STATE_UNSPECIFIED` | State not set.  
`SUBSCRIBED` | Trial is subscribed.  
`UNSUBSCRIBED` | Trial is unsubscribed before expiration.  
`EXPIRED` | Trial is expired post 30 days of subscription.  
`ELIGIBLE` | Trial is eligible for enablement.  
`NOT_ELIGIBLE` | Trial is not eligible for enablement.  
  
## EndReason

End reason enum.

Enums  
---  
`END_REASON_UNSPECIFIED` | End reason not set.  
`MOVE_TO_PAID` | Trial is deliberately ended by the user to transition to paid usage.  
`DISCONTINUED` | Trial is discontinued before expiration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-28 UTC."],[],[]] 
