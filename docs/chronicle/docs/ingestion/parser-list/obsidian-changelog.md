---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/obsidian-changelog/
title: Change log for OBSIDIAN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:22:33.272751+00:00
---

# Change log for OBSIDIAN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/obsidian-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OBSIDIAN

Date | Changes  
---|---  
2026-03-26 |  Enhancement  
\- Added support for json format logs.  
\- Added a Grok pattern on `raw.intelligenceCatalogReference.mitreProperties.description` to extract MITRE details.  
\- Added a KV filter on `details` field to extract alert details.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `raw.event_dataDatetime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `raw.generatedDatetime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `Actor` from `details` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `raw.actors.name`, `Actor Email` and `raw.relatedActorEmails` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `Tenant` from `details` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `raw.humanReadableDescription.plain` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `Alert ID` from `details` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `raw.intelligenceCatalogReference.taxonomy.behavior` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `raw.service.name`, `raw.processing_start_time`, `raw.intelligenceCatalogReference.name`, `Alert Name`, `Description`, `Event Time`, `Alert Generated Time`, `Service`, `URL`, `Tactic`, `Technique` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `icr_taxonomy_technique_name`, `raw.alert_id`, `raw.humanReadableDescription.tagged`, `raw.intelligenceCatalogReference.detectionType`, `Severity`, `raw.intelligenceCatalogReference.description`, `raw.workflowProperties.status`, `raw.id`, `raw.context.alert_context.fmt_date`, `raw.context.alert_context.fmt_time`, `raw.context.alert_context.rule_version`, `raw.context.alert_context.title_service`, `raw.context.alert_context.total`, `raw.context.alert_context.window_size`, `raw.ticketId`, `raw.intelligenceCatalogReference.mitreProperties.id`, `raw.intelligenceCatalogReference.mitreProperties.name`, `raw.intelligenceCatalogReference.mitreProperties.url`, `raw.intelligenceCatalogReference.taxonomy.tactic.name`, `raw.intelligenceCatalogReference.taxonomy.technique.name`, `raw.severity`, `technique_name`, `impact`, `citation1`, `context1`, `citation2`, `context2`, `linked_technique1`, `link1`, `context3`, `linked_technique2`, `link2`, `linked_technique3`, `link3`, `linked_technique4`, `link4`, `context4`, `linked_technique5`, `link5`, `remainder`, `Behavior`, `raw.actors.id`, `raw.actors.name`, `raw.relatedEmailDomains` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `raw.relatedTenants` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.category`: If `intelligenceCatalogReference.taxonomy.technique.name` is `Brute Force`, updated value of `event.idm.read_only_udm.security_result.category` to `BRUTE_FORCE`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `Actor` from `details` is present, updated `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.   
2026-03-17 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Newly mapped `application` (extracted from `description_field`) raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `description_kv.Alert_ID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `description_kv.URL` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `description_kv.Behavior`, `TicketId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `description_kv.Alert_Name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `description_kv.Actor` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `description_kv.Actor_Email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `description_kv.IP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `description_kv.Target` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description_kv.Description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `description_kv.Event_Time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `description_kv.Alert_Generated_Time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `description_kv.Service` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `description_kv.Tenant` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields  
\- `event.idm.read_only_udm.security_result.priority_details`: Newly mapped `Priority` raw log field with `event.idm.read_only_udm.security_result.priority_details` UDM field  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `StartTime` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `Name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `description_kv.Severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `SourceSystemName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set the `event_type` to `USER_UNCATEGORIZED` when user data and principal machine data is present.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `description_kv.Tactic` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `description_kv.Technique` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.   
2026-01-13 |  Enhancement:  
\- Added support for logs with the following format: `relatedEvents.[event details]`  
\- Renamed from relatedEvents.results to rel_events.  
\- Renamed from relatedEvents to rel_events.   
2025-12-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventDatetime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `generatedDatetime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `humanReadableDescription.plain` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `intelligenceCatalogReference.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `intelligenceCatalogReference.dashboard` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `intelligenceCatalogReference.identifier` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `intelligenceCatalogReference.id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `intelligenceCatalogReference.name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field".  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `actors.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `actors.name` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `relatedEvents.results.actors.name` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `relatedEvents.results.rawEvent.context.user.identity.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `relatedEvents.results.rawEvent.context.user.emails` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `relatedEvents.results.ipAddress.raw` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `relatedEvents.results.ipAddress.raw` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `relatedEvents.results.rawEvent.insecure_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `relatedEvents.results.rawEvent.insecure_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `relatedEvents.results.rawEvent.secure_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `relatedEvents.results.rawEvent.secure_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `relatedEvents.results.rawEvent.context.browser` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `relatedEvents.results.rawEvent.context.user.identity.id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `relatedEvents.results.rawEvent.context.user_agent_data.platformVersion` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `relatedEvents.results.rawEvent.context.org.orgToken` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `relatedEvents.results.rawEvent.url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `relatedEvents.results.rawEvent.tab_url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `relatedEvents.results.rawEvent.suspicious_clipboard_text` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `relatedEvents.results.rawEvent.enrichments.geo_ip_data.ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `relatedEvents.results.rawEvent.enrichments.geo_ip_data.ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `relatedEvents.results.rawEvent.enrichments.geo_ip_data.country` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.location.city`: Newly mapped `relatedEvents.results.rawEvent.enrichments.geo_ip_data.city` raw log field with `event.idm.read_only_udm.target.location.city` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `relatedEvents.results.rawEvent.enrichments.geo_ip_data.hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `relatedEvents.results.rawEvent.enrichments.geo_ip_data.hostname` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `alertExtraData.city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `alertExtraData.country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `alertExtraData.ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `alertExtraData.ipAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `alertExtraData.region` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `alertExtraData.userAgentString` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- Added a Grok pattern to parse the `result_ip` field.  
\- Added a conditional check to map `intelligenceCatalogReference.severity` to `event.idm.read_only_udm.security_result.severity` UDM field if the latter is empty.  
\- Processed the `labels` array to populate `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Processed `intelligenceCatalogReference.mitreProperties` to populate `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Processed the `actors` array to populate `event.idm.read_only_udm.additional.fields` and `event.idm.read_only_udm.security_result.detection_fields` UDM fields.  
\- Processed the `target_datas` array to populate `event.idm.read_only_udm.additional.fields` and `event.idm.read_only_udm.security_result.detection_fields` UDM fields.  
\- Mapped `ticketId` to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Extensively processed the `relatedEvents.results` array, mapping various nested fields to UDM fields under `principal`, `target`, `additional.fields`, and `security_result.detection_fields` UDM fields.  
\- Added a conditional check to validate the email format for `principal_user_email_addresses` UDM field before mapping.  
\- Updated the logic for setting `event.idm.read_only_udm.metadata.event_type` UDM field based on the presence of principal and target information, including a new condition for `NETWORK_CONNECTION`.   
2025-11-08 |  Enhancement:  
\- Newly created parser.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `metadata_data.product_log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `metadata_data.product_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `metadata_data.product_event_data_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `metadata_data.product_deployment_id` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `metadata_data.description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.log_type`: Newly mapped `metadata_data.log_type` raw log field with `event.idm.read_only_udm.metadata.log_type` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `network_data.http.user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `additional_data.principal_data_enrichment.product_object_id`, `additional_data.principal_data_enrichment.references.databricks.databricks.ServicePrincipal.active`, `additional_data.principal_data_enrichment.references.databricks.databricks.ServicePrincipal.applicationId`, `additional_data.principal_data_enrichment.references.databricks.databricks.ServicePrincipal.displayName`, `additional_data.principal_data_enrichment.references.databricks.databricks.ServicePrincipal.id`, `additional_data.principal_data_enrichment.references.databricks.databricks.ServicePrincipal.roles`, `additional_data.raw_event`, `version`, `user_identity.email`, `service_name`, `request_id`, `audit_level`, `event_data_id`, `additional_data.target_data_enrichment.product_object_id`, `additional_data.target_data_enrichment.references.zoom.zoom.Meeting.id`, `additional_data.target_data_enrichment.references.zoom.zoom.Meeting.topic`, `additional_data.target_data_enrichment.references.zoom.zoom.Meeting.type`, `additional_data.target_data_enrichment.references.zoom.zoom.Meeting.uuid`, `principal_data.resource.resource_type`, `raw_event_data_data_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `principal_data.user.product_object_id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principal_data.user.userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `principal_data.user.user_display_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `principal_data.application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `principal_data.ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `principal_data.ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `principal_data.ip_geo_artifact.ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `principal_data.ip_geo_artifact.ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `principal_data.ip_geo_artifact.location.city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `principal_data.ip_geo_artifact.location.country_or_region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Newly mapped `principal_data.ip_geo_artifact.location.region_coordinates.latitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Newly mapped `principal_data.ip_geo_artifact.location.region_coordinates.longitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `principal_data.ip_geo_artifact.location.state` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `principal_data.user.email_addresses` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.phone_numbers`: Newly mapped `principal_data.user.phone_numbers` raw log field with `event.idm.read_only_udm.principal.user.phone_numbers` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `metadata_data.event_data_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `metadata_data.collected_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `metadata_data.ingested_timestamp` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `action_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `raw.settings.tenant` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `raw.service.serviceId` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `message_data` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `raw.summary` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `raw.setting_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `raw.transition` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `url` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `raw.event_data_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `raw.name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `raw.compliant`, `raw.standards`, `principal_data.ip_geo_artifact.as_owner`, `raw.value.boolean`, `raw.old_value.boolean`, `raw.recommendation.value.boolean`, `raw.from_state`, `raw.to_state`, `raw.accepted`, `raw.is_tuned`, `raw.org_id`, `raw.posture_type`, `raw.config_url_path`, `raw.settings.control`, `raw.domains` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `workspace_id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `response.status_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `principal_data.resource.resource_subtype` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` if `has_target_resource` is true and `has_user` is true, else if `has_principal` is true then mapped to `STATUS_UPDATE`, else mapped to `GENERIC_EVENT`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
