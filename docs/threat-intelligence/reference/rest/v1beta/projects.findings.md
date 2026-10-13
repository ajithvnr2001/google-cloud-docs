---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings
title: REST Resource: projects.findings \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:40.624097+00:00
---

# REST Resource: projects.findings  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  REST Resource: projects.findings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Finding
    * JSON representation
  * FindingDetail
    * JSON representation
  * InitialAccessBrokerFindingDetail
    * JSON representation
  * Severity
  * DataLeakFindingDetail
    * JSON representation
  * Severity
  * InsiderThreatFindingDetail
    * JSON representation
  * Severity
  * TargetTechnologyFindingDetail
    * JSON representation
  * Methods



## Resource: Finding

A ‘stateless’ and a point in time event that a check produced a result of interest.

JSON representation  
---  
      
    
    {
      "name": string,
      "provider": string,
      "displayName": string,
      "detail": {
        object ([FindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#FindingDetail))
      },
      "severity": number,
      "reoccurrenceTimes": [
        string
      ],
      "relevanceAnalysis": {
        object ([RelevanceAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis))
      },
      "severityAnalysis": {
        object ([SeverityAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/SeverityAnalysis))
      },
      "aiSummary": string,
      "audit": {
        object ([Audit](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/Audit))
      },
      "alert": string,
      "configurations": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. Server generated name for the finding (leave clear during creation). Format: projects/{project}/findings/{finding}  
`provider` |  `string` Required. Logical source of this finding (name of the sub-engine).  
`displayName` |  `string` Required. A short descriptive title for the finding <= 250 chars. EX: "Actor 'baddy' offering $1000 for credentials of 'goodguy'".  
`detail` |  `object (`[FindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#FindingDetail)`)` Required. Holder of the domain specific details of the finding.  
`severity  
**(deprecated)**` |  `number` This item is deprecated!Optional. Deprecated: Use the `severityAnalysis` field instead. Base severity score from the finding source.  
`reoccurrenceTimes[]` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When identical finding (same labels and same details) has re-occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`relevanceAnalysis` |  `object (`[RelevanceAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis)`)` Output only. High-Precision Relevance Analysis verdict for the finding.  
`severityAnalysis` |  `object (`[SeverityAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/SeverityAnalysis)`)` Output only. High-Precision Severity Analysis verdict for the finding.  
`aiSummary` |  `string` Optional. AI summary of the finding.  
`audit` |  `object (`[Audit](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/Audit)`)` Output only. Audit data about the finding.  
`alert` |  `string` Optional. Name of the alert that this finding is bound to.  
`configurations[]` |  `string` Optional. Configuration names that are bound to this finding.  
  
## FindingDetail

Wrapper class that contains the union struct for all the various findings detail specific classes.

JSON representation  
---  
      
    
    {
      "detailType": string,
    
      // Union field detail can be only one of the following:
      "initialAccessBroker": {
        object ([InitialAccessBrokerFindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#InitialAccessBrokerFindingDetail))
      },
      "dataLeak": {
        object ([DataLeakFindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#DataLeakFindingDetail))
      },
      "insiderThreat": {
        object ([InsiderThreatFindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#InsiderThreatFindingDetail))
      },
      "targetTechnology": {
        object ([TargetTechnologyFindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#TargetTechnologyFindingDetail))
      }
      // End of list of possible types for union field detail.
    }  
  
Fields  
---  
`detailType` |  `string` Output only. Name of the detail type. Will be set by the server during creation to the name of the field that is set in the detail union.  
Union field `detail`. Domain specific details object which includes a high level summary of the finding for use in ATD contexts. `detail` can be only one of the following:  
`initialAccessBroker` |  `object (`[InitialAccessBrokerFindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#InitialAccessBrokerFindingDetail)`)` Initial Access Broker finding detail type.  
`dataLeak` |  `object (`[DataLeakFindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#DataLeakFindingDetail)`)` Data Leak finding detail type.  
`insiderThreat` |  `object (`[InsiderThreatFindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#InsiderThreatFindingDetail)`)` Insider Threat finding detail type.  
`targetTechnology` |  `object (`[TargetTechnologyFindingDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#TargetTechnologyFindingDetail)`)` Technology Watchlist finding detail type.  
  
## InitialAccessBrokerFindingDetail

A detail object for an Initial Access Broker (IAB) finding.

JSON representation  
---  
      
    
    {
      "matchScore": number,
      "severity": enum ([Severity](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#Severity)),
      "documentId": string
    }  
  
Fields  
---  
`matchScore` |  `number` Required. Reference to the match score of the IAB finding. This is a float value between 0 and 1 calculated by the matching engine based on the similarity of the document and the user provided configurations.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#Severity)`)` Required. The severity of the IAB finding. This indicates the potential impact of the threat.  
`documentId` |  `string` Required. The unique identifier of the document that triggered the IAB finding. This ID can be used to retrieve the content of the document for further analysis.  
  
## Severity

Severity of the threat finding

Enums  
---  
`SEVERITY_UNSPECIFIED` |   
`LOW` |   
`MEDIUM` |   
`HIGH` |   
`CRITICAL` |   
  
## DataLeakFindingDetail

A detail object for a Data Leak finding.

JSON representation  
---  
      
    
    {
      "matchScore": number,
      "severity": enum ([Severity](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#Severity_1)),
      "documentId": string
    }  
  
Fields  
---  
`matchScore` |  `number` Required. Reference to the match score of the Data Leak finding. This is a float value greater than 0 and less than or equal to 1 calculated by the matching engine based on the similarity of the document and the user provided configurations.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#Severity_1)`)` Required. The severity of the Data Leak finding. This indicates the potential impact of the threat.  
`documentId` |  `string` Required. The unique identifier of the document that triggered the Data Leak finding. This ID can be used to retrieve the content of the document for further analysis.  
  
## Severity

Severity of the threat finding.

Enums  
---  
`SEVERITY_UNSPECIFIED` | Default value, should never be set.  
`LOW` | Low severity.  
`MEDIUM` | Medium severity.  
`HIGH` | High severity.  
`CRITICAL` | Critical severity.  
  
## InsiderThreatFindingDetail

A detail object for a InsiderThreat finding.

JSON representation  
---  
      
    
    {
      "matchScore": number,
      "severity": enum ([Severity](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#Severity_2)),
      "documentId": string
    }  
  
Fields  
---  
`matchScore` |  `number` Required. Reference to the match score of the InsiderThreat finding. This is a float value greater than 0 and less than or equal to 1 calculated by the matching engine based on the similarity of the document and the user provided configurations.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings#Severity_2)`)` Required. The severity of the InsiderThreat finding. This indicates the potential impact of the threat.  
`documentId` |  `string` Required. The unique identifier of the document that triggered the InsiderThreat finding. This ID can be used to retrieve the content of the document for further analysis.  
  
## Severity

Severity of the threat finding.

Enums  
---  
`SEVERITY_UNSPECIFIED` | Default value, should never be set.  
`LOW` | Low severity.  
`MEDIUM` | Medium severity.  
`HIGH` | High severity.  
`CRITICAL` | Critical severity.  
  
## TargetTechnologyFindingDetail

Contains details for a technology watchlist finding.

JSON representation  
---  
      
    
    {
      "vulnerabilityMatch": {
        object ([VulnerabilityMatch](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/VulnerabilityMatch))
      }
    }  
  
Fields  
---  
`vulnerabilityMatch` |  `object (`[VulnerabilityMatch](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/VulnerabilityMatch)`)` Optional. The vulnerability match details.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings/get)`

|  Get a finding by name.  
  
### `[list](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings/list)`

|  Get a list of findings that meet the filter criteria.  
  
### `[search](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings/search)`

|  SearchFindings is a more powerful version of ListFindings that supports complex queries like "findings for alerts" using functions such as `has_alert` in the query string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
