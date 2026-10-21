---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/centrify-sso-changelog/
title: Change log for CENTRIFY_SSO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:19.404273+00:00
---

# Change log for CENTRIFY_SSO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/centrify-sso-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CENTRIFY_SSO

Date | Changes  
---|---  
2022-08-10 |  Bug-fix - Modified mapping for the field `ComputerName` from `principal.asset.hostname` to `event.idm.read_only_udm.about.hostname` for logs with JSON format.   
2022-07-13 |  Enhancement:  
\- Mapped `msg` to `metadata.description`.  
\- Mapped `EventType` to `metadata.product_event_type`.  
\- Mapped `pid` to `principal.process.pid`.  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `SessionGuid` to `network.session_id`.  
\- Mapped `UserType` to `principal.user.attribute.roles`.  
\- Mapped `AzRoleName` to `target.user.attribute.roles`.  
\- Mapped `UserGuid` to `principal.user.userid`.  
\- Mapped `ComputerID` to `principal.asset.asset_id`.  
\- Mapped `ComputerName` to `principal.asset.hostname`.  
\- Mapped `ComputerFQDN` to `principal.asset.network_domain`.  
\- Mapped `AuthorityID` to `target.asset.asset_id`.  
\- Mapped `AuthorityFQDN` to `target.asset.network_domain`.  
\- Mapped `InternalTrackingID` to `metadata.product_log_id`.  
\- Mapped `EventMessage` to `security_result.summary`.  
\- Mapped `CredentialId` to `security_result.detection_fields`.  
\- Mapped `ProxyId` to `security_result.detection_fields`.  
\- Mapped `DirectoryServiceUuid` to `security_result.detection_fields`.  
\- Mapped `AzDeploymentId` to `security_result.detection_fields`.  
\- Mapped `ID` to `security_result.detection_fields`.  
\- Mapped `AccountID` to `security_result.detection_fields`.  
\- Mapped `DirectoryServiceName` to `security_result.detection_fields`.  
\- Mapped `Tenant` to `additional.fields`.  
\- Mapped `JumpType` to `additional.fields`.  
\- Mapped `OperationMode` to `additional.fields`.  
\- Mapped `ThreadType` to `additional.fields`.  
\- Mapped `AzRoleId` to `additional.fields`.  
\- Mapped `TokenType` to `additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
