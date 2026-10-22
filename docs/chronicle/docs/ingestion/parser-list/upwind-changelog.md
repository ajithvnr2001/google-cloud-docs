---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/upwind-changelog/
title: Change log for UPWIND \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:25.356115+00:00
---

# Change log for UPWIND  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/upwind-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UPWIND

Date | Changes  
---|---  
2026-08-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `event.data.initiator.data.user_name` raw log fields with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `event.data.initiator.data.uid` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `event.data.initiator.data.user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM fields.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `event.data.initiator.type` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `event.data.initiator.data.source_ips` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `event.data.initiator.data.groups` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set the value of `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine data is present.   
2026-05-14 |  \- Newly created parser.  
\- Added support for JSON format logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `last_seen_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `first_seen_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `title` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `upwind_console_link` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `resource.id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `resource.name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `resource.cloud_account_id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `resource.type` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `resource.region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `resource.namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `resource.upwind_asset_id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.cloud.environment`: If `resource.cloud_provider` is AWS, updated the value of `event.idm.read_only_udm.principal.asset.attribute.cloud.environment` to AMAZON_WEB_SERVICES.  
\- `event.idm.read_only_udm.principal.resource.parent`: Newly mapped `resource.cluster_id` raw log field with `event.idm.read_only_udm.principal.resource.parent` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `trigger.policy_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `trigger.policy_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `event.data.name` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `event.data.command` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `event.data.user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event.type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `event.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `processtree.host_process_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_pid`: Newly mapped `processtree.host_parent_process_id` raw log field with `event.idm.read_only_udm.principal.process.parent_pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `processtree.command` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `attack.tactic_id`, `attack.tactic_name` raw log fields with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `attack.technique_id`, `attack.technique_name` raw log fields with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `type`, `status`, `link.href`, `event.data.execution_count`, `event.data.status`, `event.data.pattern`, `event.data.validation`, `occurrence_count`, `links.href` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `GENERIC_EVENT` to `event.idm.read_only_udm.metadata.event_type` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
