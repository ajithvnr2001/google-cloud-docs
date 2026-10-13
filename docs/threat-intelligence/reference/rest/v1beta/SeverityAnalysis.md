---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/SeverityAnalysis/
title: SeverityAnalysis \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:41.793047+00:00
---

# SeverityAnalysis  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/SeverityAnalysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  SeverityAnalysis Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SeverityLevel



Structured severity analysis for a threat.

JSON representation  
---  
      
    
    {
      "severityLevel": enum ([SeverityLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/SeverityAnalysis#SeverityLevel)),
      "confidence": enum ([ConfidenceLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/ConfidenceLevel)),
      "reasoning": string
    }  
  
Fields  
---  
`severityLevel` |  `enum (`[SeverityLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/SeverityAnalysis#SeverityLevel)`)` The level of severity.  
`confidence` |  `enum (`[ConfidenceLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/ConfidenceLevel)`)` The level of confidence in the given verdict.  
`reasoning` |  `string` Human-readable explanation from the model, detailing why a particular result is considered to have a certain severity.  
  
## SeverityLevel

Severity Level of an issue.

Enums  
---  
`SEVERITY_LEVEL_UNSPECIFIED` | Default value, should never be set.  
`SEVERITY_LEVEL_LOW` | Low Severity.  
`SEVERITY_LEVEL_MEDIUM` | Medium Severity.  
`SEVERITY_LEVEL_HIGH` | High Severity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
