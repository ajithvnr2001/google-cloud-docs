---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/acalvio-changelog/
title: Change log for ACALVIO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:44.339816+00:00
---

# Change log for ACALVIO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/acalvio-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ACALVIO

Date | Changes  
---|---  
2026-02-13 |  Enhancement:  
\- Added support for CEF format.  
\- Renamed internal variable `msg` to `msg1` to prevent potential conflicts.  
\- Enhanced Grok patterns to support `ISO8601` timestamps and hostnames in the syslog header.  
\- `event.idm.read_only_udm.intermediary.ip` or `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field to `event.idm.read_only_udm.intermediary.ip` if `inter_host` is an IP address, otherwise to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when user information is available.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `endTime` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user_name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dstEndpointName`, `dstEntityType`, `dstSubnet`, `dstSubnetCat` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `callbackURL` raw log field to `event.idm.read_only_udm.security_result.url_back_to_product`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `srcSubnetCat` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field to `event.idm.read_only_udm.network.session_id`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `operation`, `incidentStatus`, `scanType`, `responseStatus`, `srcSiteType`, `srcSubnet`, `dstOSFamily`, `playbookPurpose`, `credentialAnalytics`, `tenantName`, `MITREVersion`, `MITREMatrixType`, `MITREFrameworkType`, `observationCount`, `tenantID`, `messageVersion`, `notificationSource` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `techniqueID` raw log field to `event.idm.read_only_udm.security_result.attack_details.techniques`.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `techniqueID` raw log field to `event.idm.read_only_udm.security_result.attack_details.tactics`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field to event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `sev` raw log field to `event.idm.read_only_udm.security_result.severity`.  
\- Added support for failed logs due to which the following UDM fields are now being parsed correctly:  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.resource.type`  
\- `event.idm.read_only_udm.security_result[].category_details[]`  
\- `event.idm.read_only_udm.security_result[].summary`  
\- `event.idm.read_only_udm.target.port`  
2025-03-28 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_type` raw log field with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `message` raw log field with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `application.id` raw log field with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.extensions.vulns.vulnerabilities.vendor_vulnerability_id: Newly mapped `vulnerability.id` raw log field with event.idm.read_only_udm.extensions.vulns.vulnerabilities.vendor_vulnerability_id UDM field.  
\- event.idm.read_only_udm.extensions.vulns.vulnerabilities.description: Newly mapped `vulnerability.title` raw log field with event.idm.read_only_udm.extensions.vulns.vulnerabilities.description UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.uuid` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.severity` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.status` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.category` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.confidence` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.impact` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.likelihood` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.first_time_seen` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.last_time_seen` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.sub_status` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.tags` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.rule` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.rule_name` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.rule_title` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.bug_tracker_tickets` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.auto_remediated_expiration` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.name` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.language` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.importance` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.importance_description` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.first_seen` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.last_seen` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.tags` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.context_path` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.child` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `application.parent_app_id` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `server.id` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `server.name` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `server.environment` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
