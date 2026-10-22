---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cassandra-changelog/
title: Change log for CASSANDRA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:27.820466+00:00
---

# Change log for CASSANDRA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cassandra-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CASSANDRA

Date | Changes  
---|---  
2026-03-27 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `authenticated_var` field from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce a more specific mapping.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `authenticated_var` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when both `user_var` and `authenticated_var` are not null.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `authenticated_var` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field when `authenticated_var` is not null and `user_var` is null.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `user_var` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when both `user_var` and `authenticated_var` are not null in order to introduce a more accurate mapping.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `user_var` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field when both `user_var` and `authenticated_var` are not null.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `operation` raw log field with `event.idm.read_only_udm.security_result.description` UDM field when `type` is `LOGIN`.  
\- `event.idm.read_only_udm.security_result.action`: If `operation` is `Successful`, set the value of `event.idm.read_only_udm.security_result.action` to `ALLOW` and mapped `security_result_action` field with `event.idm.read_only_udm.security_result.action` UDM field.   
2026-02-26 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.description`: Removed mapping of `operation` from `event.idm.read_only_udm.security_result.description` UDM field in order to introduce a more specific mapping for the raw log field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `operation` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field when `type` is `CQL_SELECT` in order to introduce a more specific mapping for the raw log field.  
\- Modified conditional check for mapping the `operation` raw log field which resulted in removal of `operation` raw log field from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when type is `LOGIN`, `has_principal` is `true`, and `has_target` is `true`.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED` when type is `LOGIN`, `has_principal` is `true`, and `has_target` is `true`.   
2026-02-10 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `operation` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `data.applicationName` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `data.hostName` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `data.hostName` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `host` and `data.initialControlConnection` and `data.contactPoints` raw log fields to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `host` and `data.initialControlConnection` and `data.contactPoints` raw log fields to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `source` and `data.localAddress` raw log fields to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source` and `data.localAddress` raw log fields to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `category` raw log fields to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `ks`, `cf` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `category`, `type` raw log fields to the `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `operation`, `thread_name`, `log_source`, `data.dataCenters`, `consistency_level`, `timestamp`, `authenticated`, `data.applicationVersion`, `metadata.name`, `metadata.timestamp`, `metadata.tags.language`, `metadata.insightType`, `metadata.insightMappingId`, `data.clientId`, `data.protocolVersion`, `data.executionProfiles.default.readTimeout`, `data.executionProfiles.default.loadBalancing.type`, `data.executionProfiles.default.loadBalancing.options.filterFunction`, `data.executionProfiles.default.loadBalancing.namespace`, `data.executionProfiles.default.speculativeExecution.type`, `data.executionProfiles.default.speculativeExecution.namespace`, `data.executionProfiles.default.consistency`, `data.executionProfiles.default.serialConsistency`, `data.executionProfiles.default.graphOptions.source`, `data.poolSizeByHostDistance.local`, `data.poolSizeByHostDistance.remote`, `data.poolSizeByHostDistance.ignored`, `data.heartbeatInterval`, `data.compression`, `data.reconnectionPolicy.type`, `data.reconnectionPolicy.options.maxAttempts`, `data.reconnectionPolicy.options.maxDelayMs`, `data.reconnectionPolicy.options.baseDelayMs`, `data.reconnectionPolicy.namespace`, `data.ssl.enabled`, `data.ssl.certValidation`, `data.authProvider.type`, `data.authProvider.namespace`, `data.periodicStatusInterval`, `data.platformInfo.os.name`, `data.platformInfo.os.version`, `data.platformInfo.os.arch`, `data.platformInfo.cpus.length`, `data.platformInfo.cpus.model`, `data.sessionId`, `data.controlConnection`, `data.driverName`, `data.applicationNameWasGenerated`, `data.driverVersion` raw log fields to the `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` based on conditional logic UDM field.  
\- Added a new grok pattern to the `message` field match to support a new log format(`SYSLOG+JSON`) of logs.  
\- Added a KV filter to parse the `kv_data` field.   
2022-04-13 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
