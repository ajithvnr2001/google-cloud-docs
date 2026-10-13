---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Feedback/
title: Feedback \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:04.082467+00:00
---

# Feedback  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Feedback/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  Feedback Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation

JSON representation  
---  
      
    
    {
      "idpUserId": string,
      "createdTime": string,
      "verdict": enum ([Verdict](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Verdict)),
      "reputation": enum ([Reputation](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Reputation)),
      "confidenceScore": integer,
      "riskScore": integer,
      "disregarded": boolean,
      "severity": integer,
      "comment": string,
      "status": enum ([Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Status)),
      "priority": enum ([Priority](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Priority)),
      "rootCause": string,
      "reason": enum ([Reason](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Reason)),
      "severityDisplay": string,
      "priorityDisplay": string,
      "triageAgentInvestigationId": string,
      "userType": enum ([UserType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/UserType))
    }  
  
Fields  
---  
`idpUserId` |  `string` Required.  
`createdTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`verdict` |  `enum (`[Verdict](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Verdict)`)`  
`reputation` |  `enum (`[Reputation](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Reputation)`)`  
`confidenceScore` |  `integer`  
`riskScore` |  `integer`  
`disregarded` |  `boolean`  
`severity` |  `integer`  
`comment` |  `string` Optional.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Status)`)` Optional.  
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Priority)`)` Optional.  
`rootCause` |  `string` Optional.  
`reason` |  `enum (`[Reason](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Reason)`)` Optional.  
`severityDisplay` |  `string` Optional.  
`priorityDisplay` |  `string` Optional.  
`triageAgentInvestigationId` |  `string` Optional.  
`userType` |  `enum (`[UserType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/UserType)`)`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-13 UTC."],[],[]] 
