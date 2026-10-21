---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/appomni-changelog/
title: Change log for APPOMNI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:27:59.718310+00:00
---

# Change log for APPOMNI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/appomni-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for APPOMNI

Date | Changes  
---|---  
2026-08-31 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `related.ip` from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` and `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `related.ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields if it is a valid IP else mapped it to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `related.user` from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `related.user` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `effective`, `changes` from `event.idm.read_only_udm.about.labels` UDM field, since this field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `effective`, `changes` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `appomni.organization.uuid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-24 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `source.as.domain`, `raw_event.ueba.anomalous_fields.source.as.domain`, `raw_event.ueba.normal_state.source.as.domain.results`, `raw_event.ueba.normal_state.source.as.domain.counts`, `raw_event.ueba.rare_state.source.as.domain.results` and `raw_event.ueba.rare_state.source.as.domain.counts` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `APPOMNI` static value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `APPOMNI` static value with `event.idm.read_only_udm.metadata.product_name` UDM field.   
2025-05-16 |  Enhancement:  
\- This version is a parser overhaul with multiple changes and enhancements as listed below :  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `raw_event.dataset` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.log_type`: Mapped `raw_event.dataset` raw log field with `event.idm.read_only_udm.metadata.log_type` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Removed mapping of `raw_event.duration` from `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `raw_event.duration` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `appomni.event.dataset` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Mapped `appomni.event.dataset` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.alert_state`: Newly mapped `raw_event.kind` raw log field with `event.idm.read_only_udm.security_result.alert_state` UDM field. If `raw_event.kind` is equal to `event` then map `security_result.alert_state` to `NOT_ALERTING` else if `raw_event.kind` is equal to `alert` then map `security_result.alert_state` to `ALERTING`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `raw_event.url` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.url`: Mapped `raw_event.url` raw log field with `event.idm.read_only_udm.target.url` UDM field  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Removed mapping of `source.host.name` from `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Mapped `source.host.name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Removed mapping of `source.host.type` from `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.type`: Mapped `source.host.type` raw log field with `event.idm.read_only_udm.principal.asset.type` UDM field. If `source.host.type` is equal to `server` then map `principal.asset.type` to `SERVER` else if `source.host.type` is equal to `workstation` or `desktop` then map `principal.asset.type` to `WORKSTATION` else if `source.host.type` is equal to `laptop` then map `principal.asset.type` to `LAPTOP` else if `source.host.type` is equal to `mobile` then map `principal.asset.type` to `MOBILE` else if `source.host.type` is equal to `unknown` then map `principal.asset.type` to `unknown`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source.address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Removed mapping of `source.domain` from `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.network.dns_domain: Mapped `source.domain` raw log field with `event.idm.read_only_udm.principal.network.dns_domain` UDM field  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Removed mapping of `user_agent.os.name` from `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.platform: Mapped `user_agent.os.name` raw log field with `event.idm.read_only_udm.principal.platform` UDM field. If `user_agent.os.name` is `windows` then map `principal.platform` to `WINDOWS` else if `user_agent.os.name` is `linux` then map `principal.platform` to `LINUX` else if `user_agent.os.name` is `macos` then map `principal.platform` to `MAC` else if `user_agent.os.name` is `android` then map `principal.platform` to `ANDROID` else if `user_agent.os.name` is `ios` then map `principal.platform` to `IOS` else if `user_agent.os.name` is `chromeos` then map `principal.platform` to `CHROME_OS`.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Removed mapping of `user_agent.os.kernel` and `user_agent.os.platform` from `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `user_agent.os.kernel` and `user_agent.os.platform` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.target.asset.hostname: Removed mapping of `destination.host.hostname` from `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.hostname: Mapped `destination.host.hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field  
\- event.idm.read_only_udm.target.hostname: Removed mapping of `destination.domain` from `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.domain.name: Mapped `destination.domain` raw log field with `event.idm.read_only_udm.target.domain.name` UDM field  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped `destination.as.country` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field  
\- event.idm.read_only_udm.target.user.product_object_id: Removed mapping of `destination.user.id` from `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Mapped `destination.user.id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field  
\- event.idm.read_only_udm.principal.labels: Removed mapping of `user.identity.admin` , `user.identity.email` and ` user.identity.elevated` from `event.idm.read_only_udm.principal.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `user.identity.admin` and ` user.identity.elevated` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.intermediary.email: Mapped `user.identity.email` raw log field with `event.idm.read_only_udm.intermediary.email` UDM field  
\- event.idm.read_only_udm.principal.user.attribute.labels: Removed mapping of `source.user.domain` and `source.user.hash` from `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Mapped `source.user.domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field  
\- event.idm.read_only_udm.additional.fields: Mapped `source.user.hash` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `appomni.service.slug` , `source.as.type` , `rule.threat.tactic.reference` , `rule.threat.technique.reference` , `related.services.id` , `related.services.name` , `related.services.type` , `policy.category` , `policy.id` , `policy.name` , `appomni.event.enrichments` , `configuration.name` , `configuration.old_value` , `configuration.value` , `destination.as.service` , `destination.as.type` , `destination.indicators` , `destination.user.indicators` , `raw_event.ueba.anomalous_fields.source.as.number` , `raw_event.ueba.anomalous_fields.source.ip` , `raw_event.ueba.normal_state.source.as.number`, `raw_event.ueba.normal_state.source.ip` , `raw_event.ueba.rare_state.source.as.number` , `raw_event.ueba.rare_state.source.ip`, `file.directory` , `labels.some_key` , `policy.description` , `policy.outcome` , `resource.count` , `resource.owner.indicators` , `resource.parent.count` , `resource.parent.owner.domain` , `resource.parent.owner.email` , `resource.parent.owner.full_name` , `resource.parent.owner.hash` , `resource.parent.owner.id` , `resource.parent.owner.indicators` , `resource.parent.owner.name` , `resource.parent.owner.roles` , `rule.vendor_id` , `source.as.service` , `source.user.indicators` , `user.changes.indicators` , `user.effective.indicators`, `user.target.indicators` and `user.indicators` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `appomni.source.id` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `source.as.country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field  
\- event.idm.read_only_udm.principal.domain.name: Newly mapped `source.as.domain` raw log field with `event.idm.read_only_udm.principal.domain.name` UDM field  
\- event.idm.read_only_udm.security_result.attack_details.version: Newly mapped `rule.threat.framework` raw log field with `event.idm.read_only_udm.security_result.attack_details.version` UDM field  
\- event.idm.read_only_udm.security_result.attack_details.tactics.id: Newly mapped `rule.threat.tactic.id` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics.id` UDM field  
\- event.idm.read_only_udm.security_result.attack_details.tactics.name: Newly mapped `rule.threat.tactic.name` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics.name` UDM field  
\- event.idm.read_only_udm.security_result.attack_details.techniques.id: Newly mapped `rule.threat.technique.id` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.id` UDM field  
\- event.idm.read_only_udm.security_result.attack_details.techniques.name: Newly mapped `rule.threat.technique.name` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.name` UDM field  
\- event.idm.read_only_udm.src.user.product_object_id: Newly mapped `appomni.source.id` raw log field with `event.idm.read_only_udm.src.user.product_object_id` UDM field  
\- event.idm.read_only_udm.target.file.md5: Newly mapped `file.hash` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field  
\- event.idm.read_only_udm.intermediary.user.user_display_name: Newly mapped `user.identity.full_name` raw log field with `event.idm.read_only_udm.intermediary.user.user_display_name` UDM field  
\- event.idm.read_only_udm.intermediary.user.userid: Newly mapped `user.identity.id` raw log field with `event.idm.read_only_udm.intermediary.user.userid` UDM field  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `destination.as.domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field   
2025-01-07 |  Enhancement:  
\- Mapped `event.ueba.normal_state.authentication.raw_method.counts`, `event.ueba.normal_state.authentication.raw_method.results`, `event.ueba.normal_state.source.as.organization.name.results`, `event.ueba.normal_state.source.as.organization.name.counts`, `event.ueba.rare_state.authentication.raw_method.counts`, `event.ueba.rare_state.authentication.raw_method.results`, `event.ueba.rare_state.source.as.organization.name.results`, and `event.ueba.rare_state.source.as.organization.name.counts` to `additional.fields`.  
\- Mapped `event.ueba.anomalous_fields.source.as.organization.name` to `principal.network.organization_name`.   
2024-12-17 |  Enhancement:  
\- Mapped `indicators` to `additional.fields`.   
2024-11-27 |  Enhancement  
\- Changed the mappings from `about.labels` to `additional.fields`.   
2023-08-23 |  Enhanced existing parser.   
2023-06-12 |  Enhancement  
\- Mapped `resource.metadata.application` to `target.application`.  
\- Mapped `resource.metadata.entities` to `target.resource.attribute.labels`.  
\- Mapped `resource.metadata.query` to `target.process.command_line`.  
\- Mapped `resource.metadata.row_count` to `target.resource.attribute.labels`.  
\- Mapped `resource.metadata.type` to `target.resource.attribute.labels`.  
\- Mapped `resource.metadata.action_message` to `security_results.action_details`.  
\- Mapped `resource.metadata.language` to `security_results.about.label`.  
\- Mapped `labels.user_location` to `principal.asset.location.name`.  
\- Mapped `labels.login_key` to `principal.resource.attribute.labels`.  
\- Mapped `user.email` to `principal.user.email_addresses`.  
\- Mapped `user.full_name` to `principal.user.user_display_name`.  
\- Mapped `user.hash` to `principal.resource.attribute.labels`.  
\- Mapped `user.id` to `principal.user.userid`.  
\- Mapped `user.roles` to `principal.resource.attribute.labels`.  
\- Mapped `user_agent.original` to `network.http.user_agent`.  
\- Mapped `host.os.name` to `target.asset.platform_software.platform`.  
\- Mapped `host.os.version` to `target.asset.platform_software.platform_version`.  
\- Mapped `http.request.method` to `network.http.method`.  
\- Mapped `source.ip` to `principal.ip`.   
2023-04-25 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
