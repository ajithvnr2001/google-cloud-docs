---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/secureauth-sso-changelog/
title: Change log for SECUREAUTH_SSO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:38:57.386202+00:00
---

# Change log for SECUREAUTH_SSO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/secureauth-sso-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SECUREAUTH_SSO

Date | Changes  
---|---  
2026-04-20 |  Enhancement:  
\- Added support for JSON+KV log formats.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `i_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.port: Newly mapped `i_port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `parsed.LogChannel` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `parsed.FormatVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `parsed.EventID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `parsed.CompanyID` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `parsed.Realm` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `parsed.UserHostAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `parsed.UserHostAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `host.name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `host.name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.id: Newly mapped `parsed.RequestID` raw log field with `event.idm.read_only_udm.metadata.id` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `meta.cloud.availability_zone` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `meta.cloud.region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `host.id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `LogstashPod` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `fields.ApplianceID` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `LogChannel`, `FormatVersion`, `EventID`, `Version`, `parsed.UserAgent`, `parsed.ApplianceID`, `beat.name`, `beat.hostname`, `beat.version`, `fields.CompanyID`, `derived.CompanyIndex`, `_version`, `derived.EventType`, `prospector.type`, `input.type`, `parsed_Message` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `meta.cloud.machine_type`, `ApplianceType`, `parsed.Version`, `host.architecture`, `host.os.platform`, `host.os.version`, `host.os.build`, `host.os.family`, `host.os.name`, `meta.cloud.provider`, `derived.LogChannelIndex`, `document_id`, `meta.cloud.instance_id`, `tags` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2025-07-24 |  \- Added a gsub to parse proper value.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `Realm` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `CompanyID`, `PEN`, `ApplianceID`, `ApplianceMachineName`, `RequestID`, `UseJava` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2023-07-09 |  \- Added support for a new log format: SYSLOG + KV.  
\- Added a Grok pattern to parse the new logs.   
2022-04-25 |  New: Updated and converted customer-specific version to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
