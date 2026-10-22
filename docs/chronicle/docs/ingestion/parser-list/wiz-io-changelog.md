---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wiz-io-changelog/
title: Change log for WIZ_IO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:47:06.244556+00:00
---

# Change log for WIZ_IO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wiz-io-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WIZ_IO

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `resource.type` from `event.idm.read_only_udm.target.resource.resource_type` UDM field when its value is `compute#firewall` as it represents target resource type data.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Mapped `resource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field when its value is `compute#firewall`.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Removed mapping of `trigger.changedBy` raw log field from `event.idm.read_only_udm.principal.user.product_object_id` UDM field when its value is `WIZ` as it represents security-relevant information.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `trigger.changedBy` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field when its value is `WIZ`.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when target resource data is present.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `cloud_external_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.   
2026-09-15 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Removed mapping of `detection.detectionURL` from `event.idm.read_only_udm.security_result.url_back_to_product` UDM field as it represents metadata related data.  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Mapped `detection.detectionURL` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `detection.threatURL` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it represents URL related data.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Mapped `detection.threatURL` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `issue.issueURL` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `control.sourceCloudConfigurationRuleId`, `control.sourceCloudConfigurationRuleName` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `trigger.triggeredBy`, `issue.created`, `issue.updated`, `issue.type`, `evidence.data`, `detection.timeframe.start`, `detection.timeframe.end`, `detection.primaryResource.hasSensitiveData`, `detection.primaryResource.openToAllInternet`, `detection.primaryResource.nativeType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-08-27 |  Enhancement:  
\- Refactored code to map `security_result` fields accurately.  
\- Added a `gsub` pattern on `message` to handle malformed empty array formatting.  
\- Added initialization for the `subcategories_category_name` variable.  
\- Modified the `on_error` logic for `mutate` `split` operations on `threat.tdrNames` and `threat.detectionIds` fields to be at the `mutate` block level.   
2026-07-08 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `detection.projects` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.asset.location.country_or_region`: Newly mapped `detection.primaryResource.region` raw log field with `event.idm.read_only_udm.target.asset.location.country_or_region` UDM field.   
2026-06-26 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Removed mapping of `threat.id` from `event.idm.read_only_udm.metadata.product_log_id` since the field represents security threat related data.  
\- `event.idm.read_only_udm.security_result.threat_id`: Mapped `threat.id` raw log field to `event.idm.read_only_udm.security_result.threat_id`.  
\- `event.idm.read_only_udm.metadata.description`: Removed mapping of `threat.title` from `event.idm.read_only_udm.metadata.description` since the field represents security threat related data.  
\- `event.idm.read_only_udm.security_result.threat_name`: Mapped `threat.title` raw log field to `event.idm.read_only_udm.security_result.threat_name`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `threat.resolutionNote` from `event.idm.read_only_udm.additional.fields` since the field represents security related data.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `threat.resolutionNote` raw log field to `event.idm.read_only_udm.security_result.detection_fields` with key `threat_resolutionNote`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `threat.mitreTactics` from `event.idm.read_only_udm.additional.fields` since the field represents tactic id's and `security_result.attack_details.tactics` is more appropriate UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Mapped `threat.mitreTactics` raw log field to `event.idm.read_only_udm.security_result.attack_details.tactics`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `threat.mitreTechniques` from `event.idm.read_only_udm.additional.fields` since the field represents technique id's and `security_result.attack_details.techniques` is more appropriate UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Mapped `threat.mitreTechniques` raw log field to `event.idm.read_only_udm.security_result.attack_details.techniques`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `actor.id` from `event.idm.read_only_udm.principal.resource.attribute.labels` when index is not `0`. Actor ID should be under user attributes since it is more appropriate.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Mapped `actor.id` raw log field to `event.idm.read_only_udm.principal.user.attribute.labels` when index is not `0`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `actor.email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` when index is `0`.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `actor.name` (when not an email), `actor.email` raw log fields to `event.idm.read_only_udm.principal.user.attribute.labels` when index is not `0`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `threat.cloudAccount.cloudProvider`, `threat.cloudAccount.externalId`, `threat.cloudAccount.id`, `threat.cloudAccount.name` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `threat.aiAnalysisVerdict`, `threat.aiAnalysisConfidenceLevel`, `threat.aiAnalysisConclusion`, `threat.resolutionReason` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `threat.assignee.email`, `threat.assignee.id`, `threat.assignee.name` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `threat.eventOrigin` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.   
2026-06-17 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `aiAnalysis.verdict`, `aiAnalysis.analyzedAt` , `aiAnalysis.severity` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `aiAnalysis.conclusion` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.confidence: When `aiAnalysis.confidenceLevel` is `Unknown`, updated the value of `event.idm.read_only_udm.security_result.confidence` to `UNKNOWN_CONFIDENCE`, when `aiAnalysis.confidenceLevel` is `Low`, updated the value of `event.idm.read_only_udm.security_result.confidence` to `LOW_CONFIDENCE`, when `aiAnalysis.confidenceLevel` is `Medium`, updated the value of `event.idm.read_only_udm.security_result.confidence` to `MEDIUM_CONFIDENCE` and when `aiAnalysis.confidenceLevel` is `High`, updated the value of `event.idm.read_only_udm.security_result.confidence` to `HIGH_CONFIDENCE`.   
2026-05-18 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.primaryActor.id` from `event.idm.read_only_udm.additional.fields` UDM field as it represents an internal id of a primary actor.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Mapped `detection.primaryActor.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `detection.primaryActor.externalId` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field as it represents a unique identifier for the actor from the source system.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `detection.primaryActor.externalId` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `detection.primaryActor.name` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field as it is not a target resource field instead it represents the name of the actor.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Mapped `detection.primaryActor.name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `detection.actors.type` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it is not a security related field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Mapped `detection.actors.type` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `detection.actors.externalId` from `event.idm.read_only_udm.principal.user.userid` UDM field as `detection.actors` is an array and the log contains dedicated `detection.primaryActor` object as a principal.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Mapped `detection.actors.externalId` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Removed mapping of `detection.actors.id` from `event.idm.read_only_udm.principal.user.product_object_id` UDM field as `detection.actors` is an array and the log contains dedicated `detection.primaryActor` object as a principal.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Mapped `detection.actors.id` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `detection.actors.name` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field as `detection.actors` is an array and the log contains dedicated `detection.primaryActor` object as a principal.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Mapped `detection.actors.name` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` based on necessary data in raw log.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detection.cloudAccounts.cloudProvider`, `trigger.workflowId`, `trigger.workflowName` raw log field with `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `detection.primaryActor.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `detection.primaryActor.friendlyName`, `detection.primaryActor.nativeType`, `detection.primaryActor.providerUniqueId` and `detection.actors` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.   
2026-05-11 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.tdrId` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents security related data.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `detection.tdrId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.tdrSource` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents security related data.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `detection.tdrSource` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.cloudAccounts.externalId` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents target resource related data.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `detection.cloudAccounts.externalId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.cloudAccounts.id` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents target resource related data.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `detection.cloudAccounts.id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.cloudAccounts.name` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents target resource related data.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `detection.cloudAccounts.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `detection.actors.externalId` raw log field from `event.idm.read_only_udm.target.user.userid` UDM field since the field is redundant.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Removed mapping of `detection.actors.id` raw log field from `event.idm.read_only_udm.target.user.product_object_id` UDM field since the field is redundant.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Removed mapping of `detection.actors.name` raw log field from `event.idm.read_only_udm.target.user.user_display_name` UDM field since the field is redundant.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.primaryResource.type` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents target resource related data.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Mapped `detection.primaryResource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field when valid resource_type enum value is present.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `detection.primaryResource.type` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when valid resource_type enum value is not present.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `detection.triggeringEvents.actor.id` raw log field from `event.idm.read_only_udm.security_result.detection_fields` UDM field since the field represents principal resource related data.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `detection.triggeringEvents.actor.id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.triggeringEvents.actorIPMeta.country` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents principal location data.  
\- `event.idm.read_only_udm.principal.asset.location.country_or_region`: Mapped `detection.triggeringEvents.actorIPMeta.country` raw log field with `event.idm.read_only_udm.principal.asset.location.country_or_region` UDM field at index `0`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `detection.triggeringEvents.actorIPMeta.country` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field when the index is not `0`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.triggeringEvents.cloudPlatform` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents security result related data.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `detection.triggeringEvents.cloudPlatform` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.url`: Mapped `detection.triggeringEvents.cloudProviderUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field when index is `0`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `detection.triggeringEvents.cloudProviderUrl` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when the index is not `0`.  
\- `event.idm.read_only_udm.metadata.description`: Mapped `detection.triggeringEvents.description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field when the index is `0`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detection.triggeringEvents.description` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when the index is not `0`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.triggeringEvents.externalId` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents principal resource related data.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `detection.triggeringEvents.externalId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field when the index is `0`.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `detection.triggeringEvents.externalId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when the index is not `0`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.triggeringEvents.name` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents security result related data.  
\- `event.idm.read_only_udm.security_result.summary`: Mapped `detection.triggeringEvents.name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field when the index is `0`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `detection.triggeringEvents.name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field when the index is not `0`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.triggeringEvents.status` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents security result related data.  
\- `event.idm.read_only_udm.security_result.action_details`: Mapped `detection.triggeringEvents.status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field when the index is `0`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `detection.triggeringEvents.status` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field when the index is not `0`.  
\- `event.idm.read_only_udm.security_result.summary`: Removed mapping of `title` raw log field from `event.idm.read_only_udm.security_result.summary` UDM field since the field represents security rule name.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `title` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed mapping of `createdAt` raw log field from `event.idm.read_only_udm.metadata.event_timestamp` UDM field since the field does not represent the event timestamp.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `createdAt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Removed mapping of `timeframe.start` raw log field from `event.idm.read_only_udm.metadata.collected_timestamp` UDM field since the field represents the event timestamp.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Mapped `timeframe.start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `timeframe.end` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents collected timestamp.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Mapped `timeframe.end` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Removed mapping of `actors.externalId` raw log field from `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields since the field represents the principal IP details.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `actors.externalId` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when the value contains a valid IP address.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `actors.externalId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when the value does not contain a valid IP address.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `actors.id` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents principal userid details.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Mapped `actors.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `actors.name` raw log field from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields since the field represents the principal IP details.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `actors.name` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when the value contains a valid IP address.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Mapped `actors.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field when the value does not contain a valid IP address.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `actors.type` raw log field from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field to introduce accurate UDM mapping.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `actors.type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `primaryActor.externalId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field when the value does not contain a valid IP address.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `primaryResource.externalId` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents target resource related data.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `primaryResource.externalId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Removed mapping of `primaryResource.id` raw log field from `event.idm.read_only_udm.target.resource.product_object_id` UDM field to introduce accurate UDM mapping.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `primaryResource.id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Removed mapping of `primaryResource.name` raw log field from `event.idm.read_only_udm.target.resource.name` UDM field since the field represents the target hostname details.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `primaryResource.name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `triggeringEvents.actor.id` raw log field from `event.idm.read_only_udm.principal.user.userid` UDM field when the index is `0` since the mapping is redundant.  
\- `event.idm.read_only_udm.about.user.user_display_name`: Removed mapping of `triggeringEvents.actor.name` raw log field from `event.idm.read_only_udm.about.user.user_display_name` UDM field to introduce accurate UDM mapping.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `triggeringEvents.actor.name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.about.resource.resource_type`: Removed mapping of `triggeringEvents.actor.type` raw log field from `event.idm.read_only_udm.about.resource.resource_type` UDM field to introduce accurate UDM mapping.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Removed mapping of `triggeringEvents.actor.type` raw log field from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field to introduce accurate UDM mapping.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `triggeringEvents.actor.type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip`: Removed mapping of `triggeringEvents.actorIP` raw log field from `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip` UDM fields since the field represents the principal IP details.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `triggeringEvents.actorIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when the value contains a valid IP address.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `triggeringEvents.actorIPMeta.reputation` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents the security result details.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Mapped `triggeringEvents.actorIPMeta.reputation` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Removed mapping of `triggeringEvents.category` raw log field from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field to introduce accurate UDM mapping.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `triggeringEvents.category` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Removed mapping of `triggeringEvents.eventTime` raw log field from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field to introduce accurate UDM mapping.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `triggeringEvents.eventTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Removed mapping of `triggeringEvents.id` raw log field from `event.idm.read_only_udm.metadata.product_log_id` UDM field when the index is `0` since the field is redundant.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Removed mapping of `triggeringEvents.origin` raw log field from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field to introduce accurate UDM mapping.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `triggeringEvents.origin` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_type`: Newly mapped `detection.primaryActor.type` raw log field with `event.idm.read_only_udm.principal.resource.resource_type` UDM field when valid resource_type enum value is present.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `detection.primaryActor.type` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field when valid resource_type enum value is not present.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `triggeringEvents.actor.externalId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `detection.triggeringEvents.actorIPMeta.reputationDescription`, `triggeringEvents.actorIPMeta.reputationDescription` raw log fields with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `detection.primaryActor.externalId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `detection.primaryActor.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detection.primaryActor.id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.mitreTactics` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents the security attack tactics details.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Mapped `detection.mitreTactics` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `mitreTactics` raw log field from `event.idm.read_only_udm.additional.fields` UDM field since the field represents the security attack tactics details.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Mapped `mitreTactics` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Removed mapping of `detection.actors.nativeType` raw log field from `event.idm.read_only_udm.target.user.attribute.labels` UDM field since the mapping is redundant.  
\- Implemented hierarchical mapping for the `event.idm.read_only_udm.security_result.severity` UDM field. The hierarchy is as follows: `threat.severity`, `detection.severity`, `issue.severity`, and `control.severity`.  
\- `event.idm.read_only_udm.security_result.severity`: Mapped `severity` field with `event.idm.read_only_udm.security_result.severity` UDM field. Implemented conditional mapping for the severity UDM field based on the following logic:  
\- When value is CRITICAL, map to CRITICAL.  
\- When value is ERROR, map to ERROR.  
\- When value is HIGH, map to HIGH.  
\- When value is WARN or MEDIUM, map to MEDIUM.  
\- When value is LOW, map to LOW.  
\- When value is empty (""), INFO, or INFORMATIONAL, map to INFORMATIONAL.   
2026-04-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.cloud.vpc.name`: Removed mapping of `entitySnapshot.cloudPlatform` from `event.idm.read_only_udm.principal.cloud.vpc.name` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `entitySnapshot.cloudPlatform` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.vpc.id`: Removed mapping of `entitySnapshot.providerId` from `event.idm.read_only_udm.principal.cloud.vpc.id` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `entitySnapshot.providerId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.id`: Removed mapping of `entitySnapshot.type` from `event.idm.read_only_udm.principal.cloud.project.id` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `entitySnapshot.type` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.resource_subtype`: Removed mapping of `entitySnapshot.nativeType` from `event.idm.read_only_udm.principal.cloud.project.resource_subtype` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `entitySnapshot.nativeType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.name`: Removed mapping of `entitySnapshot.name` from `event.idm.read_only_udm.principal.cloud.project.name` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `entitySnapshot.name` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of `resource.id` from `event.idm.read_only_udm.target.resource.id` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `resource.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.id`: Removed mapping of `resource.subscriptionId` from `event.idm.read_only_udm.target.cloud.project.id` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `resource.subscriptionId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.name`: Removed mapping of `resource.subscriptionName` from `event.idm.read_only_udm.target.cloud.project.name` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `resource.subscriptionName` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.id`: Removed mapping of `account.externalId` from `event.idm.read_only_udm.target.cloud.project.id` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `account.externalId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.name`: Removed mapping of `account.name` from `event.idm.read_only_udm.target.cloud.project.name` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `account.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type` : Removed mapping of `primaryActor.type` from `event.idm.read_only_udm.principal.resource.type` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.resource_type`: Mapped `primaryActor.type` raw log field with `event.idm.read_only_udm.principal.resource.resource_type` UDM field when valid resource_type enum value is present.  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of `primaryResource.id` from `event.idm.read_only_udm.target.resource.id` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `primaryResource.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Removed mapping of `primaryResource.type` from `event.idm.read_only_udm.target.resource.type` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Mapped `primaryResource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field when valid resource_type enum value is present.  
\- `event.idm.read_only_udm.target.cloud.project.name`: Removed mapping of `primaryResource.cloudAccount.name` from `event.idm.read_only_udm.target.cloud.project.name` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `primaryResource.cloudAccount.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.id`: Removed mapping of `primaryResource.cloudAccount.externalId` from `event.idm.read_only_udm.target.cloud.project.id` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `primaryResource.cloudAccount.externalId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `triggeringEvent.actorIPMeta.autonomousSystemOrganization` from `event.idm.read_only_udm.principal.labels` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `triggeringEvent.actorIPMeta.autonomousSystemOrganization` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `triggeringEvent.actorIPMeta.autonomousSystemNumber` from `event.idm.read_only_udm.principal.labels` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `triggeringEvent.actorIPMeta.autonomousSystemNumber` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `triggeringEvent.actorIPMeta.isForeign` from `event.idm.read_only_udm.principal.labels` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `triggeringEvent.actorIPMeta.isForeign` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `triggeringEvent.actorIPMeta.reputation` from `event.idm.read_only_udm.principal.labels` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `triggeringEvent.actorIPMeta.reputation` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `triggeringEvent.actorIPMeta.reputationSource` from `event.idm.read_only_udm.principal.labels` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `triggeringEvent.actorIPMeta.reputationSource` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.about.resource.type`: Removed mapping of `triggeringEvent.actor.type` from `event.idm.read_only_udm.about.resource.type` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.about.resource.resource_type`: Mapped `triggeringEvent.actor.type` raw log field with `event.idm.read_only_udm.about.resource.resource_type` UDM field when valid resource_type enum value is present.  
\- `event.idm.read_only_udm.principal.location.region_latitude`: Removed mapping of `client.geographicalContext.geolocation.lat` from `event.idm.read_only_udm.principal.location.region_latitude` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Mapped `client.geographicalContext.geolocation.lat` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_longitude`: Removed mapping of `client.geographicalContext.geolocation.lon` from `event.idm.read_only_udm.principal.location.region_longitude` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Mapped `client.geographicalContext.geolocation.lon` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.about.resource.type`: Removed mapping of `triggeringEvent.resources.type` from `event.idm.read_only_udm.about.resource.type` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.about.resource.resource_type`: Mapped `triggeringEvent.resources.type` raw log field with `event.idm.read_only_udm.about.resource.resource_type` UDM field when valid resource_type enum value is present.  
\- `event.idm.read_only_udm.target.resource.type`: Removed mapping of `resource.type` from `event.idm.read_only_udm.target.resource.type` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Mapped `resource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field when valid resource_type enum value is present.  
\- `event.idm.read_only_udm.about.resource.type`: Removed mapping of `resources.type` from `event.idm.read_only_udm.about.resource.type` UDM field since the field is deprecated.  
\- `event.idm.read_only_udm.about.resource.resource_type`: Mapped `resources.type` raw log field with `event.idm.read_only_udm.about.resource.resource_type` UDM field when valid resource_type enum value is present.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `actor.name`, `triggeringEvent.runtimeDetails.processTree.executionTime`, `primaryResource.nativeType`,`primaryResource.kubernetesCluster.name`,`primaryActor.name`, `primaryResource.kubernetesCluster.externalId`, `primaryResource.kubernetesCluster.id`, `primaryResource.kubernetesNamespace.externalId`, `primaryResource.kubernetesNamespace.id`, `primaryResource.kubernetesNamespace.providerUniqueId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.namespace`: Mapped `primaryResource.kubernetesNamespace.name` raw log field with `event.idm.read_only_udm.target.namespace` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Mapped `primaryResource.kubernetesCluster.name` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional check to set the `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` if principal userid, principal email address, target userid, target email address are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional check to set the `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` if target/principal resource details and target/principal user details are both present.   
2026-03-27 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.primaryResource.externalId` from `event.idm.read_only_udm.additional.fields` UDM field to introduce accurate UDM mapping for this field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `detection.primaryResource.externalId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detection.primaryResource.name` from `event.idm.read_only_udm.additional.fields` UDM field to introduce accurate UDM mapping for this field.  
\- `event.idm.read_only_udm.target.hostname`: Mapped `detection.primaryResource.name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `triggeringEvent.runtimeDetails.processTree.n.currentWorkingDirectory` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `triggeringEvent.runtimeDetails.processTree.1.command` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `triggeringEvent.runtimeDetails.processTree.1.path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha1`: Newly mapped `triggeringEvent.runtimeDetails.processTree.1.hash` raw log field with `event.idm.read_only_udm.principal.process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.size`: Newly mapped `triggeringEvent.runtimeDetails.processTree.1.size` raw log field with `event.idm.read_only_udm.principal.process.file.size` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `triggeringEvent.runtimeDetails.processTree.0.username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `triggeringEvent.runtimeDetails.processTree.0.command` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `triggeringEvent.runtimeDetails.processTree.0.path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha1`: Newly mapped `triggeringEvent.runtimeDetails.processTree.0.hash` raw log field with `event.idm.read_only_udm.target.process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.target.process.file.size`: Newly mapped `triggeringEvent.runtimeDetails.processTree.0.size` raw log field with `event.idm.read_only_udm.target.process.file.size` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: If `detection.primaryResource.type` is `VIRTUAL_MACHINE` or `detection.primaryResource.nativeType` is `EC2 Instance`, updated the value of `event.idm.read_only_udm.target.resource.resource_type` to `VIRTUAL_MACHINE`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_user` is `true` and `event.idm.read_only_udm.metadata.event_type` is `GENERIC_EVENT`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- Added a grok pattern on `triggeringEvent.actorIP` to extract `triggeringEvent_actorIP`.   
2026-03-17 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.summary`: Removed mapping of `detection.title` from `event.idm.read_only_udm.security_result.summary` UDM field because, in order to introduce accurate mapping for this UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `detection.title` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Removed mapping of `trigger.ruleName` from `event.idm.read_only_udm.security_result.rule_name` UDM field because, in order to introduce accurate mapping for this UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `trigger.ruleName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `detection_cloudOrganizations`, `detection_triggeringEvent_actorIP`, `detection.primaryActor.actingAs.externalId`, `detection.primaryActor.actingAs.id`, `detection.primaryActor.actingAs.name`, `detection.primaryActor.actingAs.type`, `detection.primaryActor.actingAs.providerUniqueId` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `det_resource.status`, `det_resource.cloudProviderURL` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Added IP check for failed logs this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.additional.fields`  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.user.product_object_id`  
\- `event.idm.read_only_udm.principal.user.user_display_name`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.detection_fields`  
\- `event.idm.read_only_udm.security_result.rule_id`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.security_result.threat_id`  
\- `event.idm.read_only_udm.security_result.url_back_to_product`  
\- `event.idm.read_only_udm.target.url`  
\- `event.idm.read_only_udm.target.user.product_object_id`  
\- `event.idm.read_only_udm.target.user.user_display_name`  
\- `event.idm.read_only_udm.target.user.userid`  
2026-03-13 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `actor_externalId`, `actor_name` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `actor_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `actor_nativeType` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `actor_type`, `resource_type`, `threat_cloudPlatform`, `threat_resolutionNote`, `threat_resolvedAt`, `threat_projects`, `threat_notes`, `tactic_val`, `technique_val`, `threat.updatedAt`, `tdrName`, `detectionId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource_externalId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `resource_nativeType` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `org_id`, `org_name`, `org_cloudProvider`, `org_externalId`, `resource_externalId`, `resource_id`, `resource_nativeType`, `resource_name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `threat.threatURL` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `threat.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `threat.title` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `threat.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `threat.status` raw log fields with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `threat.created` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `threat.severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `resource_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `actor_id`, `actor_nativeType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2026-02-03 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `det_resource.kubernetesCluster.id`, `det_resource.kubernetesCluster.externalId`, `process_command`, `process_container_id`, `process_container_name`, `process.container.externalId`, `process.container.imageId`, `process.container.imageExternalId`, `process_hash`, `process_id`, `process_path`, `process.username`, `process.userId` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `det_resource.kubernetesnamespace.id`, `triggeringEvent.runtimeDetails.processTree.1.hash`, `triggeringEvent.runtimeDetails.processTree.0.username`, `triggeringEvent.runtimeDetails.currentWorkingDirectory` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `triggeringEvent.runtimeDetails.processTree.0.path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `triggeringEvent.runtimeDetails.processTree.2.path` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.size`: Newly mapped `process.size` raw log field with `event.idm.read_only_udm.target.process.file.size` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Changed mapping for `event.idm.read_only_udm.metadata.product_event_type` from `trigger.type` to `trigger.source` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `trigger.source` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `trigger.type` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `detection.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `detection.threatId` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `detection.detectionURL` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `detection.threatURL`, `actor.type`, `primaryActor.type`, `triggeringEvent.actor.externalId`, `triggeringEvent.actor.id`, `triggeringEvent.actor.name`, `triggeringEvent.actor.type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `detection.title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `detection.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.severity`: Newly mapped `detection.severity` raw log field with `event.idm.read_only_udm.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detection.tdrId`, `detection.tdrSource`, `detection.mitreTactics`, `detection.mitreTechniques`, `account.cloudPlatform`, `account.externalId`, `account.id`, `account.name`, `detection.createdAt`, `detection.primaryResource.externalId`, `detection.primaryResource.id`, `detection.primaryResource.name`, `detection.primaryResource.type`, `detection.triggeringEventsCount`, `triggeringEvent.actorIPMeta.autonomousSystemNumber`, `triggeringEvent.actorIPMeta.autonomousSystemOrganization`, `triggeringEvent.actorIPMeta.country`, `triggeringEvent.actorIPMeta.isForeign`, `triggeringEvent.actorIPMeta.reputationSource`, `triggeringEvent.category`, `triggeringEvent.cloudPlatform`, `triggeringEvent.eventTime`, `triggeringEvent.externalId`, `triggeringEvent.id`, `triggeringEvent.name`, `triggeringEvent.origin`, `triggeringEvent.source`, `triggeringEvent.status` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `detection.timeframe.start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `detection.timeframe.end` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor.externalId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `actor.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `actor.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `primaryActor.externalId` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `primaryActor.id` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `primaryActor.name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `metadata_data.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `triggeringEvent.cloudProviderUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `triggeringEvent.actorIPMeta.reputation`, `det_resource.type`, `det_resource.externalId`, `det_resource.id`, `det_resource.name`, `det_resource.nativeType`, `det_resource.region` raw log fields with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `triggeringEvent.actorIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `actor.nativeType` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `primaryActor.nativeType` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `triggeringEvent.description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.   
2025-12-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `actor.id`, `trigger.source`, `trigger.updatedFields`, `issue.projects`, `resource.cloudPlatform`, `control.name`, `id`, `threatURL`, `tdrId`, `tdrSource`, `account.cloudPlatform`, `account.externalId`, `account.id`, `account.name`, `primaryActor.id`, `primaryActor.actingAs`, `primaryActor.email`, `primaryActor.nativeType`, `primaryActor.providerUniqueId`, `resource.externalId`, `resource.cloudAccount.cloudPlatform`, `resource.cloudAccount.id`, `resource.cloudAccount.externalId`, `resource.cloudAccount.name`, `primaryResource.nativeType`, `primaryResource.externalId`, `primaryResource.cloudAccount.id`, `primaryResource.cloudAccount.cloudPlatform`, `triggeringEventsCount`, `triggeringEvent.source`, `mitreTactics`, `mitreTechniques` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `trigger.type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `trigger.ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `trigger.ruleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `trigger.changedBy` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `issue.id`, `triggeringEvent.id` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `issue.status`, `triggeringEvent.status` raw log fields with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `issue.created`, `createdAt`, `timeframe.start` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `resource.id`, `primaryResource.id` raw log fields with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `resource.name`, `primaryResource.name` raw log fields with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Newly mapped `resource.type`, `primaryResource.type` raw log fields with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.id`: Newly mapped `resource.subscriptionId`, `primaryResource.cloudAccount.externalId` raw log fields with `event.idm.read_only_udm.target.cloud.project.id` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.name`: Newly mapped `resource.subscriptionName`, `primaryResource.cloudAccount.name` raw log fields with `event.idm.read_only_udm.target.cloud.project.name` UDM field.  
\- `event.idm.read_only_udm.target.asset.location.country_or_region`: Newly mapped `resource.region`, `primaryResource.region` raw log fields with `event.idm.read_only_udm.target.asset.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `resource.status` raw log fields with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `resource.cloudProviderURL`, `primaryResource.cloudProviderURL`, `triggeringEvent.cloudProviderUrl` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `control.id`, `risk`, `triggeringEvent.cloudPlatform` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `control.description`, `triggeringEvent.description` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `control.severity`, `issue.severity`, `severity` raw log fields with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `control.IssueURL`, `DetectionURL` raw log fields with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `threatId` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `title`, `triggeringEvent.name` raw log fields with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `timeframe.end` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `primaryActor.externalId` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped `primaryActor.type` raw log field with `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `primaryActor.name` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resource.nativeType`, `actor.type` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.resource_obj.resource.attribute.labels`: Newly mapped `resource.status` raw log field with `event.idm.read_only_udm.resource_obj.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `resource.region` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.resource_obj.url`: Newly mapped `resource.cloudProviderURL` raw log field with `event.idm.read_only_udm.resource_obj.url` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `triggeringEvent.actorIP` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `triggeringEvent.actor.id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.about_obj.user.user_display_name`: Newly mapped `triggeringEvent.actor.name` raw log field with `event.idm.read_only_udm.about_obj.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.about_obj.resource.type`: Newly mapped `triggeringEvent.actor.type` raw log field with `event.idm.read_only_udm.about_obj.resource.type` UDM field.  
\- `event.idm.read_only_udm.principal.asset.location.country_or_region`: Newly mapped `triggeringEvent.actorIPMeta.country` raw log field with `event.idm.read_only_udm.principal.asset.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Newly mapped `triggeringEvent.actorIPMeta.reputation`, `triggeringEvent.actorIPMeta.reputationSource`, `triggeringEvent.actorIPMeta.autonomousSystemOrganization`, `triggeringEvent.actorIPMeta.autonomousSystemNumber`, `triggeringEvent.actorIPMeta.isForeign` raw log fields with `event.idm.read_only_udm.principal.labels` UDM field.  
\- `event.idm.read_only_udm.about_obj.resource.attribute.labels`: Newly mapped `triggeringEvent.category`, `triggeringEvent.eventTime`, `triggeringEvent.origin` raw log fields with `event.idm.read_only_udm.about_obj.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `triggeringEvent.externalId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `actor_name_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `actor_externalId_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field.   
2025-10-24 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record.trigger.source`, `record.cloudOrganizations`, `record.trigger.type`, `record.triggeringEventsCount`, `record.trigger.updatedFields`, `record.control.risks`, `record.resource.cloudPlatform` , `record.control.name`, `record.DetectionURL`, `record.threatURL`, `record.id`, `record.tdrId`, `record.tdrSource`, `mitreTactic`, `mitreTechniques`, `cloudAccounts.cloudPlatform`, `cloudAccounts.externalId`, `cloudAccounts.id`, `cloudAccounts.name`, `triggeringEvent.source`, `record.PrimaryResource.cloudAccount.cloudPlatform`, `record.PrimaryResource.externalId`, `record.primaryResource.nativeType`, `record.PrimaryResource.cloudAccount.id`, `record.PrimaryResource.providerUniqueId`, `record.PrimaryResource.status`, `record.PrimaryResource.VCSRepository`, `record.PrimaryResource.cloudOrganization`, `record.PrimaryResource.kubernetesNamespace`, `record.PrimaryResource.kubernetesCluster`, `record.trigger.updatedFields`, `record.resource.cloudPlatform`, `record.control.name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `record.trigger.ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `record.trigger.ruleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `record.trigger.changedBy` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `record.issue.id`, `triggeringEvent.id` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.alert_state`: Newly mapped `record.issue.status` raw log field with `event.idm.read_only_udm.security_result.alert_state` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `record.issue.severity`, `record.severity` raw log fields with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `record.issue.created`, `record.timeframe.start`, `createdAt` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `record.resource.id`, `record.PrimaryResource.id` raw log fields with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `record.resource.name`, `resource.name`, `record.PrimaryResource.name` raw log fields with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Newly mapped `record.resource.type`, `resource.type`, `record.PrimaryResource.type` raw log fields with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.id`: Newly mapped `record.resource.subscriptionId`, `record.PrimaryResource.cloudAccount.externalId` raw log fields with `event.idm.read_only_udm.target.cloud.project.id` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.name`: Newly mapped `record.resource.subscriptionName`, `record.PrimaryResource.cloudAccount.name` raw log fields with `event.idm.read_only_udm.target.cloud.project.name` UDM field.  
\- `event.idm.read_only_udm.target.asset.location.country_or_region`: Newly mapped `record.resource.region`, `record.PrimaryResource.region` raw log fields with `event.idm.read_only_udm.target.asset.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `record.resource.status` raw log fields with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `record.resource.cloudProviderURL`, `triggeringEvent.cloudProviderUrl`, `record.PrimaryResource.cloudProviderURL` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.control.id`, `record.issue.projects`, `triggeringEvent.actorIPMeta.category`, `triggeringEvent.cloudPlatform` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `record.control.description`, `triggeringEvent.description` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.about.url`: Newly mapped `record.control.IssueURL` raw log field with `event.idm.read_only_udm.security_result.about.url` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `record.threatId` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `record.title` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `record.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `record.timeframe.end` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `act.externalId` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `pactor.externalId` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `triggeringEvents.actor.id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.asset.location.country_or_region`: Newly mapped `triggeringEvent.actorIPMeta.country` raw log field with `event.idm.read_only_udm.principal.asset.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Newly mapped `triggeringEvent.actorIPMeta.autonomousSystemNumber`, `triggeringEvent.actorIPMeta.autonomousSystemOrganization`, `triggeringEvent.actorIPMeta.isForeign`, `triggeringEvent.actorIPMeta.reputation`, `triggeringEvent.actorIPMeta.reputationSource`, raw log fields with `event.idm.read_only_udm.principal.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `triggeringEvent.externalId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `triggeringEvent.name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resource.nativeType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `resource.region` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `triggeringEvent.status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- Added conditional check for `record.trigger.source`. If the value is `ISSUE`, the `security_result.alert_state` is set to `ALERTING` for an `OPEN` status and `NOT_ALERTING` for a `RESOLVED` status.   
2025-06-04 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly Mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM Field.  
\- event.idm.read_only_udm.metadata.timestamp: Newly Mapped `createdAt` raw log field with `event.idm.read_only_udm.metadata.timestamp` UDM Field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly Mapped `entitySnapshot.tags.io.kubernetes.pod.uid` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly Mapped `entitySnapshot.tags.io.kubernetes.pod.namespace` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly Mapped `entitySnapshot.tags.io.kubernetes.container.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly Mapped `entitySnapshot.tags.io.cri-containerd.kind` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly Mapped `entitySnapshot.tags.io.kubernetes.pod.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly Mapped `entitySnapshot.tags.maintainer` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.group.product_object_id: Newly Mapped `entitySnapshot.externalId` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM Field.  
\- event.idm.read_only_udm.principal.group.product_object_id: Newly Mapped `actionParameters.clientID` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM Field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM Field.  
\- event.idm.read_only_udm.principal.namespace: Newly Mapped `entitySnapshot.tags.io.kubernetes.pod.namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM Field.  
\- event.idm.read_only_udm.principal.asset_id: Newly Mapped `entitySnapshot.id` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM Field.  
\- event.idm.read_only_udm.principal.cloud.vpc.name: Newly Mapped `entitySnapshot.cloudPlatform` raw log field with `event.idm.read_only_udm.principal.cloud.vpc.name` UDM Field.  
\- event.idm.read_only_udm.principal.cloud.vpc.id: Newly Mapped `entitySnapshot.providerId` raw log field with `event.idm.read_only_udm.principal.cloud.vpc.id` UDM Field.  
\- event.idm.read_only_udm.principal.cloud.project.id: Newly Mapped `entitySnapshot.type` raw log field with `event.idm.read_only_udm.principal.cloud.project.id` UDM Field.  
\- event.idm.read_only_udm.principal.cloud.project.resource_subtype: Newly Mapped `entitySnapshot.nativeType` raw log field with `event.idm.read_only_udm.principal.cloud.project.resource_subtype` UDM Field.  
\- event.idm.read_only_udm.principal.cloud.project.name: Newly Mapped `entitySnapshot.name` raw log field with `event.idm.read_only_udm.principal.cloud.project.name` UDM Field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `entitySnapshot.status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `updatedAt` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `dueAt` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `statusChangedAt` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `sourceRule.id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `control.name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `control.description` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `control.resolutionRecommendation` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.summary: Newly Mapped `subcategories.title` raw log field with `event.idm.read_only_udm.security_result.category` UDM Field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `subcategories.category.name` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `subcategories.category.framework.name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `actionParameters.userPoolType` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `actionParameters.userpoolID` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `actionParameters.clientID` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.   
2024-03-04 |  Enhancement:  
\- Mapped `actionParameters.selection.preferences`, `actionParameters.input.patch.portalVisitHistory.dateTime`, and `actionParameters.input.patch.portalVisitHistory.type` to `additional.fields`  
\- Mapped `actionParameters.input.patch.portalVisitHistory.name`, `actionParameters.input.patch.portalVisitHistory.resourceName`, `actionParameters.input.patch.portalVisitHistory.resourceType`, `actionParameters.input.patch.portalVisitHistory.ruleType`, and `actionParameters.input.patch.portalVisitHistory.id` to `principal.resource.attribute.labels`.   
2024-02-08 |  Enhancement:  
\- Mapped `WIZ_IO` to `metadata.product_name` and `metadata.vendor_name`.  
\- Mapped `action` to `metadata.product_event_type`.  
\- Mapped `timestamp` to `metadata.event_timestamp`.  
\- Mapped `userAgent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped `sourceIP` to `principal.ip`.  
\- When action value is `Report`, then mapped `serviceAccount.name` to `principal.application`.  
\- Mapped `user.id` to `target.user.id`.  
\- Mapped `user.name` to `target.user.user_display_name`.  
\- Mapped `userEmail` to `target.user.email_addresses`.  
\- Mapped `actionParameters.role` to `target.user.attribute.roles`.  
\- Mapped `actionParameters.groups` and `actionParameters.products` to `security_result.detection_fields`.   
2023-12-15 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
