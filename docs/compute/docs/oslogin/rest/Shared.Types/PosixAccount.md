---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/PosixAccount/
title: PosixAccount \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:22:36.131075+00:00
---

# PosixAccount  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/PosixAccount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  PosixAccount Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The POSIX account information associated with a Google account.

JSON representation  
---  
      
    
    {
      "primary": boolean,
      "username": string,
      "uid": string,
      "gid": string,
      "homeDirectory": string,
      "shell": string,
      "gecos": string,
      "systemId": string,
      "accountId": string,
      "operatingSystemType": enum ([OperatingSystemType](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/OperatingSystemType)),
      "name": string
    }  
  
Fields  
---  
`primary` |  `boolean` Only one POSIX account can be marked as primary.  
`username` |  `string` The username of the POSIX account.  
`uid` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The user ID.  
`gid` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The default group ID.  
`homeDirectory` |  `string` The path to the home directory for this account.  
`shell` |  `string` The path to the logic shell for this account.  
`gecos` |  `string` The GECOS (user information) entry for this account.  
`systemId` |  `string` System identifier for which account the username or uid applies to. By default, the empty value is used.  
`accountId` |  `string` Output only. A POSIX account identifier.  
`operatingSystemType` |  `enum (`[OperatingSystemType](https://docs.cloud.google.com/compute/docs/oslogin/rest/Shared.Types/OperatingSystemType)`)` The operating system type where this account applies.  
`name` |  `string` Output only. The canonical resource name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
