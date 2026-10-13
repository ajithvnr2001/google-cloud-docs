---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/
title: Google Threat Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:29.177752+00:00
---

# Google Threat Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  Google Threat Intelligence API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1beta.projects.alerts
  * REST Resource: v1beta.projects.alerts.documents
  * REST Resource: v1beta.projects.configurations
  * REST Resource: v1beta.projects.configurations.revisions
  * REST Resource: v1beta.projects.findings

**Note:** For the full Google Threat Intelligence API Reference and Guides, please go to the [GTI Docs Portal](https://gtidocs.virustotal.com/). 

## Service: threatintelligence.googleapis.com

### Quick Start

To start calling the API with simple examples immediately, see [Get Started](https://docs.cloud.google.com/threat-intelligence/guides/get-started) page.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming APIs. We have the following discovery documents:

  * REST: <https://threatintelligence.googleapis.com/$discovery/rest?version=v1beta>
  * OpenAPI: <https://threatintelligence.googleapis.com/$discovery/OPENAPI3_0?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. We have the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://threatintelligence.googleapis.com`



## REST Resource: [v1beta.projects.alerts](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts)

Methods  
---  
`[benign](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/benign)` |  `POST /v1beta/{name=projects/*/alerts/*}:benign`   
Marks an alert as benign - BENIGN.  
`[duplicate](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/duplicate)` |  `POST /v1beta/{name=projects/*/alerts/*}:duplicate`   
Marks an alert as a duplicate of another alert.  
`[enumerateFacets](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/enumerateFacets)` |  `GET /v1beta/{parent=projects/*}/alerts:enumerateFacets`   
EnumerateAlertFacets returns the facets and the number of alerts that meet the filter criteria and have that value for each facet.  
`[escalate](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/escalate)` |  `POST /v1beta/{name=projects/*/alerts/*}:escalate`   
Marks an alert as escalated - ESCALATED.  
`[falsePositive](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/falsePositive)` |  `POST /v1beta/{name=projects/*/alerts/*}:falsePositive`   
Marks an alert as a false positive - FALSE_POSITIVE.  
`[get](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/get)` |  `GET /v1beta/{name=projects/*/alerts/*}`   
Get an alert by name.  
`[list](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/list)` |  `GET /v1beta/{parent=projects/*}/alerts`   
Get a list of alerts that meet the filter criteria.  
`[notActionable](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/notActionable)` |  `POST /v1beta/{name=projects/*/alerts/*}:notActionable`   
Marks an alert as not actionable - NOT_ACTIONABLE.  
`[read](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/read)` |  `POST /v1beta/{name=projects/*/alerts/*}:read`   
Marks an alert as read - READ.  
`[resolve](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/resolve)` |  `POST /v1beta/{name=projects/*/alerts/*}:resolve`   
Marks an alert to closed state - RESOLVED.  
`[trackExternally](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/trackExternally)` |  `POST /v1beta/{name=projects/*/alerts/*}:trackExternally`   
Marks an alert as tracked externally - TRACKED_EXTERNALLY.  
`[triage](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts/triage)` |  `POST /v1beta/{name=projects/*/alerts/*}:triage`   
Marks an alert as triaged - TRIAGED.  
  
## REST Resource: [v1beta.projects.alerts.documents](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts.documents)

Methods  
---  
`[get](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts.documents/get)` |  `GET /v1beta/{name=projects/*/alerts/*/documents/*}`   
Gets a specific document associated with an alert.  
  
## REST Resource: [v1beta.projects.configurations](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations)

Methods  
---  
`[get](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations/get)` |  `GET /v1beta/{name=projects/*/configurations/*}`   
Get a configuration by name.  
`[list](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations/list)` |  `GET /v1beta/{parent=projects/*}/configurations`   
Get a list of configurations that meet the filter criteria.  
`[upsert](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations/upsert)` |  `POST /v1beta/{parent=projects/*}/configurations:upsert`   
Creates or updates a configuration.  
  
## REST Resource: [v1beta.projects.configurations.revisions](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations.revisions)

Methods  
---  
`[list](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations.revisions/list)` |  `GET /v1beta/{parent=projects/*/configurations/*}/revisions`   
List configuration revisions that meet the filter criteria.  
  
## REST Resource: [v1beta.projects.findings](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings)

Methods  
---  
`[get](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings/get)` |  `GET /v1beta/{name=projects/*/findings/*}`   
Get a finding by name.  
`[list](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings/list)` |  `GET /v1beta/{parent=projects/*}/findings`   
Get a list of findings that meet the filter criteria.  
`[search](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings/search)` |  `GET /v1beta/{parent=projects/*}/findings:search`   
SearchFindings is a more powerful version of ListFindings that supports complex queries like "findings for alerts" using functions such as `has_alert` in the query string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
