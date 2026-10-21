---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis/
title: RelevanceAnalysis \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:41.920026+00:00
---

# RelevanceAnalysis  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  RelevanceAnalysis Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Evidence
    * JSON representation
  * RelevanceLevel



Structured relevance analysis for a threat.

JSON representation  
---  
      
    
    {
      "relevant": boolean,
      "confidence": enum ([ConfidenceLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/ConfidenceLevel)),
      "reasoning": string,
      "evidence": {
        object ([Evidence](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis#Evidence))
      },
      "relevanceLevel": enum ([RelevanceLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis#RelevanceLevel))
    }  
  
Fields  
---  
`relevant` |  `boolean` Indicates whether the threat is considered relevant.  
`confidence` |  `enum (`[ConfidenceLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/ConfidenceLevel)`)` The level of confidence in the given verdict.  
`reasoning` |  `string` Human-readable explanation from the matcher, detailing why a particular result is considered relevant or not relevant.  
`evidence` |  `object (`[Evidence](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis#Evidence)`)` Evidence supporting the verdict, including matched and unmatched items.  
`relevanceLevel` |  `enum (`[RelevanceLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis#RelevanceLevel)`)` The level of relevance.  
  
## Evidence

Details the evidence used to determine the relevance verdict.

JSON representation  
---  
      
    
    {
      "commonThemes": [
        string
      ],
      "distinctThemes": [
        string
      ]
    }  
  
Fields  
---  
`commonThemes[]` |  `string` A list of semantic themes or concepts found to be common, related, or aligned between the sources, supporting the verdict.  
`distinctThemes[]` |  `string` A list of semantic themes or descriptions unique to one source or semantically distant.  
  
## RelevanceLevel

Relevance Level of an issue.

Enums  
---  
`RELEVANCE_LEVEL_UNSPECIFIED` | Default value, should never be set.  
`RELEVANCE_LEVEL_LOW` | Low Relevance.  
`RELEVANCE_LEVEL_MEDIUM` | Medium Relevance.  
`RELEVANCE_LEVEL_HIGH` | High Relevance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
