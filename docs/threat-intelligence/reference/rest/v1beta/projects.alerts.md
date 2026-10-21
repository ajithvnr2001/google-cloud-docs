---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts
title: REST Resource: projects.alerts \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:37.966758+00:00
---

# REST Resource: projects.alerts  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  REST Resource: projects.alerts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Alert
    * JSON representation
  * State
  * AlertDetail
    * JSON representation
  * InitialAccessBrokerAlertDetail
    * JSON representation
  * DataLeakAlertDetail
    * JSON representation
  * InsiderThreatAlertDetail
    * JSON representation
  * TargetTechnologyAlertDetail
    * JSON representation
  * PriorityAnalysis
    * JSON representation
  * PriorityLevel
  * Methods



## Resource: Alert

Stateful object representing a group of Findings. Key feature to an Alert is that it expresses the user's intent towards the findings of that group, even those that haven't occurred yet.

JSON representation  
---  
      
    
    {
      "name": string,
      "findings": [
        string
      ],
      "state": enum ([State](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#State)),
      "audit": {
        object ([Audit](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/Audit))
      },
      "displayName": string,
      "detail": {
        object ([AlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#AlertDetail))
      },
      "duplicateOf": string,
      "duplicatedBy": [
        string
      ],
      "etag": string,
      "externalId": string,
      "aiSummary": string,
      "relevanceAnalysis": {
        object ([RelevanceAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis))
      },
      "severityAnalysis": {
        object ([SeverityAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/SeverityAnalysis))
      },
      "priorityAnalysis": {
        object ([PriorityAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#PriorityAnalysis))
      },
      "findingCount": string,
      "configurations": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. Server generated name for the alert. format is projects/{project}/alerts/{alert}  
`findings[]` |  `string` Output only. Findings that are covered by this alert.  
`state` |  `enum (`[State](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#State)`)` Output only. State of the alert.  
`audit` |  `object (`[Audit](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/Audit)`)` Output only. Audit information for the alert.  
`displayName` |  `string` Output only. A short title for the alert.  
`detail` |  `object (`[AlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#AlertDetail)`)` Output only. Details object for the alert, not all alerts will have a details object.  
`duplicateOf` |  `string` Output only. alert name of the alert this alert is a duplicate of. Format: projects/{project}/alerts/{alert}  
`duplicatedBy[]` |  `string` Output only. alert names of the alerts that are duplicates of this alert. Format: projects/{project}/alerts/{alert}  
`etag` |  `string` Optional. If included when updating an alert, this should be set to the current etag of the alert. If the etags do not match, the update will be rejected and an ABORTED error will be returned.  
`externalId` |  `string` Output only. External ID for the alert. This is used internally to provide protection against out of order updates.  
`aiSummary` |  `string` Optional. AI summary of the alert.  
`relevanceAnalysis` |  `object (`[RelevanceAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis)`)` Output only. High-Precision Relevance Analysis verdict for the alert.  
`severityAnalysis` |  `object (`[SeverityAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/SeverityAnalysis)`)` Output only. High-Precision Severity Analysis for the alert.  
`priorityAnalysis` |  `object (`[PriorityAnalysis](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#PriorityAnalysis)`)` Output only. High-Precision Priority Analysis for the alert.  
`findingCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of findings associated with this alert.  
`configurations[]` |  `string` Output only. The resource names of the Configurations bound to this alert. Format: projects/{project}/configurations/{configuration}  
  
## State

alert state is used to track the lifecycle of an alert. More state values may be added in the future.

Enums  
---  
`STATE_UNSPECIFIED` | Default value, should never be set.  
`NEW` | alert is new.  
`READ` | alert was read by a human.  
`TRIAGED` | alert has been triaged.  
`ESCALATED` | alert has been escalated.  
`RESOLVED` | alert has been resolved.  
`DUPLICATE` | alert is a duplicate of another alert.  
`FALSE_POSITIVE` | alert is a false positive and should be ignored.  
`NOT_ACTIONABLE` | alert is not actionable.  
`BENIGN` | alert is benign.  
`TRACKED_EXTERNALLY` | alert is tracked externally.  
  
## AlertDetail

Container for different types of alert details.

JSON representation  
---  
      
    
    {
      "detailType": string,
    
      // Union field detail can be only one of the following:
      "initialAccessBroker": {
        object ([InitialAccessBrokerAlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#InitialAccessBrokerAlertDetail))
      },
      "dataLeak": {
        object ([DataLeakAlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#DataLeakAlertDetail))
      },
      "insiderThreat": {
        object ([InsiderThreatAlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#InsiderThreatAlertDetail))
      },
      "targetTechnology": {
        object ([TargetTechnologyAlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#TargetTechnologyAlertDetail))
      }
      // End of list of possible types for union field detail.
    }  
  
Fields  
---  
`detailType` |  `string` Output only. Name of the detail type. Will be set by the server during creation to the name of the field that is set in the detail union.  
Union field `detail`. Domain specific details object which includes a high level summary of the finding for use in ATD contexts. `detail` can be only one of the following:  
`initialAccessBroker` |  `object (`[InitialAccessBrokerAlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#InitialAccessBrokerAlertDetail)`)` Initial Access Broker alert detail type.  
`dataLeak` |  `object (`[DataLeakAlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#DataLeakAlertDetail)`)` Data Leak alert detail type.  
`insiderThreat` |  `object (`[InsiderThreatAlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#InsiderThreatAlertDetail)`)` Insider Threat alert detail type.  
`targetTechnology` |  `object (`[TargetTechnologyAlertDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#TargetTechnologyAlertDetail)`)` Technology Watchlist alert detail type.  
  
## InitialAccessBrokerAlertDetail

Captures the specific details of InitialAccessBroker (IAB) alert.

JSON representation  
---  
      
    
    {
      "severity": string,
      "discoveryDocumentIds": [
        string
      ]
    }  
  
Fields  
---  
`severity` |  `string` Required. The severity of the Initial Access Broker (IAB) alert. Allowed values are: * `LOW` * `MEDIUM` * `HIGH` * `CRITICAL`  
`discoveryDocumentIds[]` |  `string` Required. Array of ids to accommodate multiple discovery documents  
  
## DataLeakAlertDetail

Captures the specific details of Data Leak alert.

JSON representation  
---  
      
    
    {
      "severity": string,
      "discoveryDocumentIds": [
        string
      ]
    }  
  
Fields  
---  
`severity` |  `string` Required. The severity of the Data Leak alert. Allowed values are: * `LOW` * `MEDIUM` * `HIGH` * `CRITICAL`  
`discoveryDocumentIds[]` |  `string` Required. Array of ids to accommodate multiple discovery documents  
  
## InsiderThreatAlertDetail

Captures the specific details of InsiderThreat alert.

JSON representation  
---  
      
    
    {
      "severity": string,
      "discoveryDocumentIds": [
        string
      ]
    }  
  
Fields  
---  
`severity` |  `string` Required. The severity of the Insider Threat alert. Allowed values are: * `LOW` * `MEDIUM` * `HIGH` * `CRITICAL`  
`discoveryDocumentIds[]` |  `string` Required. Array of ids to accommodate multiple discovery documents  
  
## TargetTechnologyAlertDetail

Contains details for a technology watchlist alert.

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
  
## PriorityAnalysis

Structured priority analysis for a threat.

JSON representation  
---  
      
    
    {
      "priorityLevel": enum ([PriorityLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#PriorityLevel)),
      "confidence": enum ([ConfidenceLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/ConfidenceLevel)),
      "reasoning": string
    }  
  
Fields  
---  
`priorityLevel` |  `enum (`[PriorityLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts#PriorityLevel)`)` The level of Priority.  
`confidence` |  `enum (`[ConfidenceLevel](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/ConfidenceLevel)`)` The level of confidence in the given verdict.  
`reasoning` |  `string` Human-readable explanation from the model, detailing why a particular result is considered to have a certain priority.  
  
## PriorityLevel

Priority Level of an issue.

Enums  
---  
`PRIORITY_LEVEL_UNSPECIFIED` | Default value, should never be set.  
`PRIORITY_LEVEL_LOW` | Low Priority.  
`PRIORITY_LEVEL_MEDIUM` | Medium Priority.  
`PRIORITY_LEVEL_HIGH` | High Priority.  
`PRIORITY_LEVEL_CRITICAL` | Critical Priority.  
  
## Methods  
  
---  
  
### `[benign](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/benign)`

|  Marks an alert as benign - BENIGN.  
  
### `[duplicate](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/duplicate)`

|  Marks an alert as a duplicate of another alert.  
  
### `[enumerateFacets](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/enumerateFacets)`

|  EnumerateAlertFacets returns the facets and the number of alerts that meet the filter criteria and have that value for each facet.  
  
### `[escalate](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/escalate)`

|  Marks an alert as escalated - ESCALATED.  
  
### `[falsePositive](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/falsePositive)`

|  Marks an alert as a false positive - FALSE_POSITIVE.  
  
### `[get](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/get)`

|  Get an alert by name.  
  
### `[list](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/list)`

|  Get a list of alerts that meet the filter criteria.  
  
### `[notActionable](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/notActionable)`

|  Marks an alert as not actionable - NOT_ACTIONABLE.  
  
### `[read](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/read)`

|  Marks an alert as read - READ.  
  
### `[resolve](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/resolve)`

|  Marks an alert to closed state - RESOLVED.  
  
### `[trackExternally](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/trackExternally)`

|  Marks an alert as tracked externally - TRACKED_EXTERNALLY.  
  
### `[triage](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/triage)`

|  Marks an alert as triaged - TRIAGED.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
