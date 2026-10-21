---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-audit-changelog/
title: Change log for TRENDMICRO_VISION_ONE_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:33:09.863049+00:00
---

# Change log for TRENDMICRO_VISION_ONE_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_VISION_ONE_AUDIT

Date | Changes  
---|---  
2026-09-25 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `loggedUserId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `loggedUserMailAddress` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `udso.ipAddr` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `details.policyName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `details.priorityAction` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `details.currentPriorityOrder`, `changed_item.field`, `changed_item.from`, `changed_item.to` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Modified mapping for `event.idm.read_only_udm.metadata.event_type` when `has_principal_user` is `true` and `has_target` is `true`, and `result` is `Successful`, `activity` is `Log on`, `category` is `Logon and Logoff`, or `loggedUser` is not empty, set to `USER_LOGIN`.  
\- Modified mapping for `event.idm.read_only_udm.metadata.event_type` when `has_target_resource` is `true`, set to `USER_RESOURCE_UPDATE_CONTENT`.  
\- Modified mapping for `event.idm.read_only_udm.metadata.event_type` when `has_principal_user` is `true`, set to `USER_UNCATEGORIZED`.   
2025-09-29 |  Enhancement:  
\- Modified principal.user.user_role mapping logic to include `Senior Analyst` as `ADMINISTRATOR`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `details.description` raw log field to event.idm.read_only_udm.metadata.description.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `details.status` and `details.assMitigateStatus` raw log field to event.idm.read_only_udm.security_result.summary.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `details.feedback.description` raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `details.workbenchId` raw log field to event.idm.read_only_udm.target.resource.id.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `details.ipAddr` raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `details.identifier.id` raw log field to event.idm.read_only_udm.principal.user.product_object_id.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `details.identifier.type` raw log field to event.idm.read_only_udm.metadata.product_event_type.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `details.identifier.name` and `details.user` raw log field to event.idm.read_only_udm.principal.user.user_display_name.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `details.identifier.email` raw log field to event.idm.read_only_udm.principal.user.email_addresses.  
\- event.idm.read_only_udm.principal.resource.resource_subtype: Newly mapped `details.identifier.subType` raw log field to event.idm.read_only_udm.principal.resource.resource_subtype.  
\- event.idm.read_only_udm.metadata.product_deployment_id: Newly mapped `details.traceId` raw log field to event.idm.read_only_udm.metadata.product_deployment_id.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `details.action` raw log field to event.idm.read_only_udm.security_result.action_details.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `removedAgent.hostname` raw log field to event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `removedAgent.xdrDeviceId` raw log field to event.idm.read_only_udm.principal.asset.product_object_id.  
\- event.idm.read_only_udm.principal.resource.type: Newly mapped `details.type` raw log field to event.idm.read_only_udm.principal.resource.type.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `details.instanceId` raw log field to event.idm.read_only_udm.principal.resource.product_object_id.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `details.serverId` raw log field to event.idm.read_only_udm.principal.asset.product_object_id.  
\- event.idm.read_only_udm.principal.group.product_object_id: Newly mapped `details.groupId` raw log field to event.idm.read_only_udm.principal.group.product_object_id.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `endpoint.wsDeviceId` raw log field to event.idm.read_only_udm.target.resource.product_object_id.  
\- event.idm.read_only_udm.target.resource.type: Newly mapped `endpoint.xdrDeviceId` raw log field to event.idm.read_only_udm.target.resource.type.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `details.source`, `details.investigationResult`, `details.feedback.reason.id`, `details.feedback.reason.value`, `details.reason`, `details.assTotalAssetsInvolved`, `ass_EventList.Risk event`, `ass_EventList.Asset name`, `ass_EventList.Asset type` and `details.role` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `details.requestId` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels.   
2025-04-07 |  \- Newly created parser.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `loggedDateTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `ingestedDateTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `loggedUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_role`: Newly mapped `loggedRole` raw log field with `event.idm.read_only_udm.principal.user.user_role` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `category`, `activity`, `accessType`, `result` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `uuid` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
