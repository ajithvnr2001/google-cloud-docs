---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jfrog-artifactory-changelog/
title: Change log for JFROG_ARTIFACTORY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:41.382750+00:00
---

# Change log for JFROG_ARTIFACTORY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jfrog-artifactory-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JFROG_ARTIFACTORY

Date | Changes  
---|---  
2026-08-20 |  Enhancement:  
\- Added a grok pattern to parse the new format of logs.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of the `hostname` field from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields since it represents a username and not a hostname.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `user` field with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-10-24 |  Enhancement:  
\- Added support for JSON format with a syslog header.  
\- Enhanced date parsing for `metadata.event_timestamp` to support additional formats: `yyyy-MM-ddTHH:mm:ss.SSSSSSZ`, `ISO8601`, and `RFC3339`.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `host` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `appname` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Duration` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.asset_id: Newly mapped `request_Uber-Trace-Id` raw log field to `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `time` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `StartUTC` raw log field to `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `user_agent` raw log field to `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.   
2025-09-16 |  Enhancement:  
\- Modified the grok pattern to improve parsing accuracy for IP address.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped the `syslog_priority` raw log field to the `event1.idm.read_only_udm.additional.fields` UDM field.   
2025-02-27 |  Enhancement:  
\- Mapped `data.repository_key`, `data.release_bundle_name`, `data.release_bundle_version`, `data.property_key`, `data.property_values`, `data.platforms.architecture`, and `data.platforms.os` to `additional.fields`.   
2025-02-19 |  Enhancement:  
\- Mapped `data.repo_key` ,`subscription_key`,`source`,`image_name`, `data.platforms` to `additional.fields`.  
\- Mapped `domain` to `principal.administrative_domain`.  
\- Mapped `event_type` to `metadata.product_event_type`.  
\- Mapped `data.path` to `target.file.full_path`.  
\- Mapped `data.name` to `target.user.user_display_name`.  
\- Mapped `data.size` to `target.file.size`.  
\- Mapped `SHA256` to `target.process.file.sha256`.   
2024-09-23 |  Enhancement:  
\- Added support to parse the unparsed logs.  
\- Mapped `target_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `desc` to `metadata.description`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `url` to `target.url`.  
\- Mapped `prin_url` to `principal.url`.  
\- Mapped `response_code` to `network.http.response_code`.  
\- Mapped `RequestMethod` to `network.http.method`.  
\- Mapped `RequestPath` to `target.url`.  
\- Mapped `DownstreamContentSize` and `DownstreamStatus` to `Additional.Fields`.  
\- Mapped `ServiceAddr` to `principal.hostname` and `principal.port`.  
\- Mapped `ClientAddr` to `target.ip` and `target.port`.  
\- Mapped `user_agent` to `network.http.user_agent`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `msg` to `security_result.description`.  
\- Mapped `protocol` to `network.application_protocol`.   
2023-08-25 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
