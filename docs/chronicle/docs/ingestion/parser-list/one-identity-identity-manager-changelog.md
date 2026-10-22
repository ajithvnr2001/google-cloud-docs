---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/one-identity-identity-manager-changelog/
title: Change log for ONE_IDENTITY_IDENTITY_MANAGER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:29.316763+00:00
---

# Change log for ONE_IDENTITY_IDENTITY_MANAGER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/one-identity-identity-manager-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ONE_IDENTITY_IDENTITY_MANAGER

Date | Changes  
---|---  
2025-07-08 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` log fields with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `time` log fields with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `hostname` fields with a grok pattern to identify IP addresses. When an IP is found, it is mapped to `event.idm.read_only_udm.intermediary.ip`. Otherwise, the existing mapping to `event.idm.read_only_udm.intermediary.hostname` is used.  
\- event.idm.read_only_udm.principal.application: Newly mapped `app_name` log fields with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `process_id` log fields with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `EventTimestamp` log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `EventUserDisplayName` log fields with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped `EventUserId` log fields with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `AssetPartitionId`, `DurationInMinutes`, `OfflineWorkflowMode`, `RequiredDate`, `WasCheckedOut`, `ApproverAccessRequestUri` and `ReviewerAccessRequestUri` log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `AccessRequestType` log fields with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.roles: Newly mapped `AccountDistinguishedName` log fields with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `AccountDomainName` log fields with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- event.idm.read_only_udm.target.asset.platform_software.platform: Newly mapped `AssetPlatformType` log fields with `event.idm.read_only_udm.target.asset.platform_software.platform` UDM field.   
2025-02-19 |  \- Added support for the new SYSLOG+JSON log format.   
2024-10-03 |  \- Added support for the new log format.   
2024-09-03 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
