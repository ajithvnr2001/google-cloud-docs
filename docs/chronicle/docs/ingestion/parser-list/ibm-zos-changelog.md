---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-zos-changelog/
title: Change log for IBM_ZOS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:01.441448+00:00
---

# Change log for IBM_ZOS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-zos-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_ZOS

Date | Changes  
---|---  
2026-04-29 |  Enhancement:  
\- Added grok pattern to extract `devTime`.  
\- Added grok pattern to extract `server_ip`, `client_ip`, `tls_cipher`, `tls_key_exchange`, `tls_auth`, `bytes_in`, `conn_begin_count`, `conn_end_count`, `duration_minutes`, `duration_seconds` from `sum`.  
\- If `sum` grok fails, mapped `sum` to `event.idm.read_only_udm.metadata.description`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `server_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tls_cipher` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `duration_seconds` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tlsProtVer` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `devTimeFormat`, `tlsalg`, `tlschn`, `connsBeg`, `connsEnd`, `tlsKexAlg`, `partialBeg`, `partialEnd`, `shortBeg`, `shortEnd`, `activeBeg`, `activeEnd`, `tlskeylen`, `tlsCCertSig`, `tlsMsgAuth`, `tlsNegCipher`, `tlsSCertSig`, `dn`, `duration_minutes`, `conn_begin_count`, `conn_end_count`, `bytes_in`, `tls_auth`, `tls_key_exchange` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `sum` contains `SMFDUMP`, `src` and `dst` are not empty, set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `usrName` is not empty and `event_type` is not `NETWORK_CONNECTION`, `USER_RESOURCE_UPDATE_CONTENT`, or `USER_RESOURCE_ACCESS`, set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `usrName` is empty, `src` is empty, `box` is empty and `event.idm.read_only_udm.metadata.event_type` is `STATUS_UPDATE`, set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.   
2026-04-02 |  Enhancement:  
\- Added support for SYSLOG format.  
\- Modified a grok pattern on `job` to extract `job_id` and `job_group`.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `syslog_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `syslog_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `dstPackets` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `srcPackets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `saConnId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `sysname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.process.file.names`: Newly mapped `jobname` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `jobid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `sysplex`, `stack` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `action` is `COMPLETE`, set the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `sum` contains `Connection` or `Short` set the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.network.ip_protocol`: If `IPproto` is `TCP`, set the value of `event.idm.read_only_udm.network.ip_protocol` to `TCP`.   
2025-11-05 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `usrPriv`, `usrGroups` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `class` raw log field(s) with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `res` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `prof`, `dsn` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `devTime`: Converted type to ISO8601 with error handling for date_parsing_error.  
\- The kv filter now uses strict whitespace handling.   
2024-10-26 |  Enhancement:  
\- Added support to handle SYSLOG logs.   
2023-07-25 |  Bug-Fix -  
\- Updated values set for `metadata.vendor_name` and `metadata.product_name`.   
2022-09-08 |  Fix -  
\- Corrected a typo error.   
2022-08-09 |  Enhancement: Mapped following fields:  
\- user_out to target.user.userid.  
\- name_out to target.user.user_display_name.  
\- perf_out to target.user.employee_id.  
\- department_out to target.user.department.  
\- ug_out to target.user.office_address.name.  
\- timestamp to src.user.hire_date.  
\- timestamp_end to src.user.termination_date.  
\- user_in to src.user.userid.  
\- name_in to src.user.user_display_name.  
\- perf_in to src.user.employee_id.  
\- department_in to src.user.department.  
\- status to security_result.summary.  
\- userid to principal.user.userid.  
\- username to user.user_display_name.  
\- n_ex_fail to security_result.action_details and mapped security_result.action to FAIL.  
\- type_trx to target.resource.name and mapped TASK to target.resource.resource_type.  
\- email to principal.user.email_addresses.  
\- l_email to observer.user.email_addresses.  
\- class to target.resource.parent.  
\- resource to target.resource.name.  
\- mot to product_event_type.  
\- metadata.event_type to USER_UNCATEGORIZED where mot is not null.  
\- metadata.event_type to USER_RESOURCE_UPDATE_CONTENT where userid is not null.  
\- Added new Grok patterns for logs that has EVENT_TYPES in ALTUSER, CONNECT, ALTGROUP, ADDGROUP, DELGROUP, PERMIT, REMOVE, SETROPTS, RACDCERT and mapped followings fields:  
\- EVENT_QUAL to security_result.summary.  
\- SYSTEM_SMFID to principal.hostname.  
\- VIOLATION to security_result.category.  
\- USER_NDFND to principal.user.user_authentication_status.  
\- USER_WARNING to security_result.severity.  
\- EVT_USER_ID to principal.user.userid.  
\- EVT_GRP_ID to principal.group.group_display_name.  
\- LOG_CLASS, LOG_ACCESS, LOG_USER, LOG_SPECIAL, LOG_NONOMVS, LOG_OMVSNPRV, AUTH_OMVSSU, AUTH_OMVSSYS to security_result.outcomes.  
\- LOG_RACINIT, BACKOUT_FAIL, PROF_SAME, to security_result.action.  
\- TERM to principal.resource_ancestors.name.  
\- JOB_NAME to principal.resource.name.  
\- LOG_ALWAYS, LOG_CMDVIOL, TERM_LEVEL, LOG_GLOBAL, LOG_LEVEL, LOG_LOGOPT, LOG_SECL, LOG_COMPATM, LOG_APPLAUD to principal.resource.attribute.permissions.  
\- USR_SECL to principal.user.attribute.labels.  
\- RACF_VERSION to security_result.rule_version.  
\- ALU_OWN_ID to about.user.userid.  
\- ALU_OLD_SECL, ALU_UTK_SECL to target.user.attribute.labels.  
\- ALU_UTK_ENCR, ALU_UTK_PRE19, ALU_UTK_DEFAULT, ALU_UTK_VERPROF, ALU_UTK_ERROR, ALU_NOAUTH_CLAUTH, ALU_NOAUTH_GROUP, ALU_NOAUTH_PROF to security_result.outcomes.  
\- ALU_UTK_NJEUNUSR, ALU_UTK_LOGUSR, ALU_UTK_SPECIAL, ALU_UTK_UNKNUSR, ALU_UTK_PRIV, ALU_UTK_SURROGAT to target.user.attribute.roles.  
\- ALU_UTK_TRUSTED to target.user.group_identifiers.  
\- ALU_UTK_SESSTYPE, CON_UTK_SESSTYPE, ALG_UTK_SESSTYPE to metadata.description.  
\- ALU_UTK_REMOTE, ALU_UTK_SPCLASS, CON_UTK_REMOTE to principal.resource.resource_subtype.  
\- ALU_UTK_EXECNODE, ALG_UTK_EXECNODE about.resource.name.  
\- ALU_UTK_SUSER_ID, CON_UTK_SUSER_ID, ALG_UTK_SUSER_ID to src.user.userid.  
\- ALU_UTK_SNODE, CON_UTK_SNODE, ALG_UTK_SNODE to src.resource.name.  
\- ALU_UTK_SGRP_ID, CON_UTK_SGRP_ID, ALG_UTK_SGRP_ID to src.user.group_identifiers.  
\- ALU_UTK_SPOE, CON_UTK_SPOE, ALG_UTK_SPOE to principal.port.  
\- ALU_UTK_USER_ID, CON_OWN_ID, CON_UTK_USER_ID, ALG_OWN_ID, AG_OWN_ID, ALG_UTK_USER_ID to about.user.userid.  
\- ALU_USER_NAME, CON_USER_NAME, ALG_USER_NAME, AG_USER_NAME to about.user.user_display_name.  
\- ALU_UTK_GRP_ID, CON_UTK_GRP_ID, ALG_UTK_GRP_ID to about.group.product_object_id.  
\- ALU_UTK_DFT_GRP, CON_UTK_DFT_GRP, CON_UTK_DFT_SECL, ALG_UTK_DFT_GRP to target.group.attribute.labels.  
\- ALU_UTK_DFT_SECL, ALG_UTK_DFT_SECL to target.user.attribute.labels.  
\- ALU_APPC_LINK, CON_APPC_LINK, ALG_UTK_SECL, ALG_APPC_LINK to about.resource.attribute.labels.  
\- ALU_USER_ID, CON_USER_ID to target.user.userid.  
\- CON_UTK_ENCR, CON_UTK_PRE19, CON_UTK_VERPROF, CON_UTK_DEFAULT, CON_UTK_ERROR, ALG_UTK_ENCR, ALG_UTK_PRE19, ALG_UTK_VERPROF, ALG_UTK_DEFAULT, ALG_UTK_ERROR, AG_UTK_ENCR, AG_UTK_PRE19, AG_UTK_VERPROF, AG_UTK_DEFAULT, AG_UTK_ERROR to security_result.outcomes.  
\- CON_UTK_NJEUNUSR, CON_UTK_LOGUSR, CON_UTK_SPECIAL, CON_UTK_UNKNUSR, CON_UTK_SECL, ALG_UTK_NJEUNUSR, ALG_UTK_LOGUSR, ALG_UTK_SPECIAL, ALG_UTK_UNKNUSR, AG_UTK_NJEUNUSR, AG_UTK_LOGUSR, AG_UTK_SPECIAL, AG_UTK_UNKNUSR to target.user.attribute.roles.  
\- CON_UTK_TRUSTED, ALG_UTK_TRUSTED, AG_UTK_TRUSTED to target.user.group_identifiers.  
\- CON_UTK_SURROGAT, ALG_UTK_SURROGAT to target.user.attribute.roles.  
\- CON_UTK_SPCLASS, ALG_UTK_REMOTE, ALG_UTK_SPCLASS to about.resource.resource_subtype.   
2022-06-03 |  Enhancement  
\- Enhanced parser to parse CSV logs.  
\- Mapped box field from log to udm principal.hostname.  
\- Added check for src and dst not null prior to mapping of event_type to NETWORK_CONNECTION.  
\- Added check for userName not null prior to mapping of event_type to USER_RESOURCE_UPDATE_CONTENT or USER_RESOURCE_ACCESS.   
2022-05-04 |  Enhancement - Create a new default parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
