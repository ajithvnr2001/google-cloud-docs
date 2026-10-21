---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-cloud-activity-tracker-changelog/
title: Change log for IBM_CLOUD_ACTIVITY_TRACKER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:25:54.965620+00:00
---

# Change log for IBM_CLOUD_ACTIVITY_TRACKER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-cloud-activity-tracker-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_CLOUD_ACTIVITY_TRACKER

Date | Changes  
---|---  
2025-05-29 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data_requestData_repository` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `data_serviceName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data_correlationId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `data_logSourceCRN` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `data_action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `data_initiator_authnId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data_initiator_authnName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `data_credential_type` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `data_initiator_host_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data_initiator_host_addressType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event.idm.read_only_udm.network.http.user_agent and event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `data_initiator_host_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM fields  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `data_initiator_id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `data_initiator_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field  
\- event.idm.read_only_udm.principal.url: Newly mapped `data_initiator_typeURI` raw log field with `event.idm.read_only_udm.principal.url` UDM field  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `data_typeURI` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data_dataEvent` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event.idm.read_only_udm.observer.resource.name: Newly mapped `data_observer_name` raw log field with `event.idm.read_only_udm.observer.resource.name` UDM field  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `data_outcome` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data_saveServiceCopy` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `data_reason_reasonCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field  
\- event.idm.read_only_udm.security_result.description: Newly mapped `data_reason_reasonType` raw log field with `event.idm.read_only_udm.security_result.description` UDM field  
\- event.idm.read_only_udm.metadata.description: Newly mapped `data_message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `data_target_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `data_target_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field  
\- Added a `has_target_resource` flag before mapping `data_target_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `data_target_typeURI` raw log field with `event.idm.read_only_udm.target.url` UDM field  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `data_severity` raw log field to `event.idm.read_only_udm.security_result.severity` if `severity` is equals to `normal` else mapped to `event.idm.read_only_udm.security_result.severity` UDM field  
\- event.idm.read_only_udm.principal.application: Newly mapped `labels_applicationname` raw log field with `event.idm.read_only_udm.principal.application` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `labels_subsystemname` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `labels_computername` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `labels_threadid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `labels_ipaddress` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `data_eventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `meta_data_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `meta_data_severity` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `meta_data_logid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- event.idm.read_only_udm.security_result.priority: Newly mapped `HIGH_PRIORITY` to `event.idm.read_only_udm.security_result.priority` UDM field if `meta_data_priorityclass` is equals to `high`  
\- event.idm.read_only_udm.additional.fields: Newly mapped `meta_data_branchid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `meta_data_ingressTimestamp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.target.group.product_object_id: Newly mapped `data_target_resourceGroupId` raw log field with `event.idm.read_only_udm.target.group.product_object_id` UDM field  
\- Added a conditional check before mapping `USER_RESOURCE_ACCESS` and `USER_RESOURCE_CREATION` to `event.idm.read_only_udm.metadata.event_type` UDM field.  
\- Added a gsub to replace `metadata` with `meta_data` on message field.   
2024-09-12 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
