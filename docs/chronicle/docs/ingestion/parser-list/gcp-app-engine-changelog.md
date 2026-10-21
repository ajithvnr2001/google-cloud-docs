---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-app-engine-changelog/
title: Change log for GCP_APP_ENGINE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:02:08.760331+00:00
---

# Change log for GCP_APP_ENGINE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-app-engine-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_APP_ENGINE

Date | Changes  
---|---  
2025-12-29 |  \- event.idm.read_only_udm.principal.ip: Newly mapped `protoPayload.requestMetadata.callerIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `protoPayload.requestMetadata.callerIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `protoPayload.authenticationInfo.principalEmail` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `protoPayload.methodName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `protoPayload.resourceName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `protoPayload.serviceName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `protoPayload.resourceLocation.currentLocations` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `protoPayload.authenticationInfo.oauthInfo.oauthClientId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `protoPayload.requestMetadata.requestAttributes.time`, `operation.first`, `protoPayload.serviceData.updateService.request.updateMask`, `operation.id`, `protoPayload.authenticationInfo.serviceAccountKeyName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `protoPayload.authorizationInfo.permission` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `protoPayload.authorizationInfo.permissionType` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `protoPayload.authorizationInfo.granted` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- The conditional logic for security_result.severity was updated to include `NOTICE` in addition to `INFO` for setting the severity to `INFORMATIONAL`.   
2024-08-01 |  \- If principal machine data is present, then set `metadata.event_type` to `STATUS_UPDATE`.  
\- Mapped `protoPayload.ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `protoPayload.appId` to `principal.resource.attribute.labels`.  
\- Mapped `protoPayload.host` to `principal.hostname`.  
\- Mapped `protoPayload.method` to `network.http.method`.  
\- Mapped `protoPayload.@type` , `labels.clone_id` and `operation.producer` to `additional.labels`.   
2024-06-03 |  \- Added support for a new type of JSON logs.   
2024-03-05 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
