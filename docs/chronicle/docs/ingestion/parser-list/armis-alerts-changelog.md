---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-alerts-changelog/
title: Change log for ARMIS_ALERTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:39.907223+00:00
---

# Change log for ARMIS_ALERTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-alerts-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARMIS_ALERTS

Date | Changes  
---|---  
2026-07-21 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Removed mapping of `deviceId` from `event.idm.read_only_udm.principal.asset.asset_id` since `event.idm.read_only_udm.principal.asset.product_object_id` is more appropriate for holding product-specific identifiers like Armis Device IDs.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Mapped `deviceId` raw log field to `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Removed mapping of `title` from `event.idm.read_only_udm.metadata.product_event_type` since `event.idm.read_only_udm.security_result.summary` is more appropriate for holding alert descriptions/summaries.  
\- `event.idm.read_only_udm.security_result.summary`: Mapped `title` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Removed mapping of `type` from `event.idm.read_only_udm.security_result.category_details` since `event.idm.read_only_udm.security_result.rule_type` is more appropriate for policy violation types.  
\- `event.idm.read_only_udm.security_result.rule_type`: Mapped `type` raw log field to `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Mapped `classification` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `mitreAttackLabels.matrix`, `mitreAttackLabels.technique`, `mitreAttackLabels.tactic`, `lastAlertUpdateTime`, `statusChangeTime`, and `sourceEndpoints.businessImpact` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `policyLabels`, `sourceEndpoints.boundaries`, and `sourceEndpoints.dataSources` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `affectedDevicesCount` raw log field to `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `sourceEndpoints.name` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.asset_id`, `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `sourceEndpoints.id` raw log field to `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` UDM fields.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `sourceEndpoints.sites` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `sourceEndpoints.riskLevel` raw log field to `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sourceEndpoints.ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.mac`, `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `sourceEndpoints.macAddress` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destinationEndpoints.ip` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `destinationEndpoints.name` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.asset_id`, `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `destinationEndpoints.id` raw log field to `event.idm.read_only_udm.target.asset_id` and `event.idm.read_only_udm.target.asset.asset_id` UDM fields.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `policyId` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `policyTitle` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Removed static assignment of `GENERIC_EVENT`. Added logic to dynamically set event type to `NETWORK_CONNECTION`, `STATUS_UPDATE`, or `GENERIC_EVENT` based on the presence of principal and target devices.  
\- Updated the logic to set alert state to `ALERTING` for both `Unhandled` and `Open` statuses (previously only `Unhandled`).   
2023-02-07 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
