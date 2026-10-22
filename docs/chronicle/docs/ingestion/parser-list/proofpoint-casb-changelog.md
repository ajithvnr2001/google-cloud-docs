---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-casb-changelog/
title: Change log for PROOFPOINT_CASB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:50.223992+00:00
---

# Change log for PROOFPOINT_CASB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-casb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PROOFPOINT_CASB

Date | Changes  
---|---  
2026-01-16 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.process.pid: Newly mapped `event1.agent.pid` raw log field with `event.idm.read_only_udm.intermediary.process.pid` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event1.activity.primaryCategory` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `event1.feed.vendor` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `event1.feed.product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `event1.user.email`, `event1.user.directory.manager.email` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `event1.user.displayName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `event1.user.directory.title` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `event1.user.groups.name` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `event1.endpoint.net.interfaces.ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `event1.process.application.name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `resource.hashes.value` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.file.mime_type: Newly mapped `resource.contentType` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `resource.hashes.value` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.file.mime_type: Newly mapped `resource.contentType` raw log field with `event.idm.read_only_udm.principal.file.mime_type` UDM field.  
\- event.idm.read_only_udm.principal.user.department: Newly mapped `event1.user.directory.department.name` raw log field with `event.idm.read_only_udm.principal.user.department` UDM field.  
\- event.idm.read_only_udm.principal.user.company_name: Newly mapped `event1.user.directory.company.name` raw log field with `event.idm.read_only_udm.principal.user.company_name` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `event1.site.url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `event1.site.categorization.details.categories.name` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `event1.components.policies.id`, `event1.activity.policies.id`, `event1.activity.signals.name`, `event1.intelligence.findings.kind`, `indicator.kind`, `indicator.id`, `indicator.name`, `indicator._collations.key_value`, `match.op`, `match.result.value`, `param.value`, `event1.annotations.workflow.state.disposition.status.id`, `event1.annotations.workflow.state.status`, `event1.incident.status`, `event1.site.categorization.details.status`, `event1.site.reputation.details.status`, `event1.incident.severity` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `device.attributes.key`, `device.attributes.value`, `device.attributes._collations.key_value`, `event1.site.reputation.level`, `event1.agent.kind`, `event1.activity.trigger`, `event1.endpoint.fqdn`, `event1.endpoint.os.name`, `event1.endpoint.alias`, `event1.user.directory.ou` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-03-20 |  Enhancement:  
\- Mapped `id` , `tenant_id` and `type` fields to `additional.fields`.  
\- Mapped `sub_type` to `target.resource.resource_subtype`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `description` to `security_result.description`.  
\- Mapped `title` to `metadata.description`.  
\- Mapped `threat` to `security_result.threat_name`.  
\- Mapped `sub_category` to `security_result.summary`.  
\- Mapped `category` to `security_result.category_details`.  
\- Mapped `classification id to `security_result.rule_id".  
\- Mapped `ip_address` to `principal.ip`.  
\- Mapped `geo_location_latitude` to `principal.location.region_latitude`.  
\- Mapped `geo_location_longitude` to `principal.location.region_longitude`.  
\- Mapped `location` to `principal.location.name`.  
\- Mapped `user_agent` to `network.http.user_agent`.  
\- Mapped `full_name` to `principal.user.user_display_name`.  
\- Mapped `user_email` to `principal.user.email_addresses`.  
\- Mapped `user_id` to `principal.user.userid`.  
\- Mapped `event_id` to `metadata.product_log_id`.  
\- Mapped `cloud_services` to `target.application`.   
2025-03-14 |  Enhancement:  
\- Added support for new format of JSON logs.   
2024-09-07 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
