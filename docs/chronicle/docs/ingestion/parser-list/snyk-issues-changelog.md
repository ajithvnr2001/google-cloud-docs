---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snyk-issues-changelog/
title: Change log for SNYK_ISSUES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:56.070615+00:00
---

# Change log for SNYK_ISSUES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snyk-issues-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SNYK_ISSUES

Date | Changes  
---|---  
2025-12-22 |  New Field Mapping:  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `project.id` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `project.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.group.creation_time`: Newly mapped `project.created` raw log field with `event.idm.read_only_udm.target.group.creation_time` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `project.origin`, `project.readOnly`, `project.isMonitored`, `project.testFrequency`, `project.totalDependencies`, `project.imageTag`, `project.branch` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `project.type` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.about.labels`: Newly mapped `project.issueCountsBySeverity.low`, `project.issueCountsBySeverity.high`, `project.issueCountsBySeverity.medium`, `project.issueCountsBySeverity.critical` raw log field(s) with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `project.lastTestedDate` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `project.browseUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `org.id`, `org.slug`, `org.group.id`, `group.name`, `group.url`, `group.created` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `org.name` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `org.url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.groupid`: Newly mapped `org.group.name` raw log field with `event.idm.read_only_udm.principal.user.groupid` UDM field.  
\- `event.idm.read_only_udm.principal.group.creation_time`: Newly mapped `org.created` raw log field with `event.idm.read_only_udm.principal.group.creation_time` UDM field.   
2025-02-20 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
