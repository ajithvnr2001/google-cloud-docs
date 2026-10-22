---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/exchange-mail-changelog/
title: Change log for EXCHANGE_MAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:10.845350+00:00
---

# Change log for EXCHANGE_MAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/exchange-mail-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for EXCHANGE_MAIL

Date | Changes  
---|---  
2025-09-30 |  Enhancement:  
\- Added a grok pattern on `column6` data field to extract `sessionid` , `msg_id` raw log fields.  
\- Corrected the mapping of the `column3` data field in order to map the data correctly to the `event.idm.read_only_udm.network.application_protocol` UDM field.  
-`event.idm.read_only_udm.additional.fields`: Newly mapped `column5` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
-`event.idm.read_only_udm.metadata.description`: Newly mapped `column6` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.   
2025-03-19 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- If `c-ip` is a valid IP address, then mapped `c-ip` to `target.ip` and `target.asset.ip`. Otherwise, mapped `c-ip` to `target.hostname` and `target.asset.hostname`.  
\- If `s-ip` is a valid IP address, then mapped `s-ip` to `principal.ip` and `principal.asset.ip`. Otherwise, mapped `s-ip` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `s-port` to `principal.port`.  
\- Mapped `cs-method` to `network.http.method`.  
\- Mapped `cs_referer` to `network.http.referral_url`.  
\- Mapped `cs_user_agent` to `network.http.user_agent`.  
\- Mapped `timestamp` to `metadata.event_timestamp`.  
\- Mapped `cs-username` to `principal.user.userid`.  
\- Mapped `sc-status` to `network.http.response_code`.  
\- Mapped `sc-substatus` and `sc-win32-status` to `additional.fields`.  
\- Mapped `time-taken`, `cs-uri-stem` and `cs-uri-query` to `security_result.detection_fields`.   
2024-08-06 |  Enhancement:  
\- When `column3` is `application_protocol`, then mapped it to `network.application_protocol`.  
\- Added a Grok pattern to parse `column6` and to extract `target_ip_1`.   
2024-07-08 |  Enhancement:  
\- Added support for new pattern of CSV logs.  
\- Added a Grok pattern to check if ip is valid before mapping.  
\- Added a Grok pattern over `column6` to extract `target_ip_1`, `target_ip_2`, and `target_ip_3`.  
\- Mapped `target_ip_1`, `target_ip_2`, and `target_ip_3` to `target.ip` and `target.asset.ip`.  
\- If `column2` is not valid IP address, `column2` mapped to `metadata.product_log_id`.  
\- If `column4` is not valid IP address, `column4` mapped to `metadata.product_event_type`.   
2024-06-18 |  Enhancement:  
\- Mapped `schema-version` to `additional.fields`.   
2024-03-22 |  Enhancement:  
\- Changed mapping of `OriginalFromAddress` from `target.user.email_addresses` to `principal.user.email_addresses`.  
\- Added support for new pattern of CSV logs.  
\- Mapped `sender-address`, `column20`, and `from_mail` to `principal.user.email_addresses`.  
\- Mapped `column13` and `to_mail` to `target.user.email_addresses`.   
2024-03-18 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- Mapped `Hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `ProcessID` to `principal.process.pid`.  
\- Mapped `SourceName` to `principal.resource.attribute.labels`.  
\- Mapped `Message` to `security_result.description`.  
\- Mapped `Category` to `security_result.category_details`.  
\- Mapped `Severity` to `security_result.severity`.  
\- Mapped `SeverityValue` to `security_result.severity_details`.  
\- Mapped `Keywords`, `ThreadID`, `Task`, `RecordNumber`, `Channel` and `EventID` to `security_result.detection_fields`.   
2024-03-01 |  Enhancement:  
\- Added support for new pattern of syslog logs.  
\- Mapped `AgentDevice`, `AgentLogFile`, `AgentLogFormat`, `AgentLogProtocol`, `PluginVersion`, and `sc-substatus` to `additional.fields`.  
\- Mapped `client-ip` and `original-client-ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `client-hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `server-ip` and `original-server-ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `server-hostname` to `target.hostname` and `target.asset.hostname`.  
\- When `has_principal` is `true`, then set `metadata.event_type` to `STATUS_UPDATE`.  
\- When `event_type` is `GENERIC_EVENT` and `has_principal_email` or `has_target_email` is `true`, then set `metadata.event_type` to `USER_UNCATEGORIZED`.   
2024-02-15 |  Enhancement  
\- Added CSV block to parse CSV logs.  
\- Mapped `Coloumn2` and `Coloumn25` to `principal.ip` and `principal.assest.ip`.  
\- Mapped `Coloumn3` to `principal.hostname` and `principal.assest.hostname`.  
\- Mapped `Coloumn4` to `target.ip` and `target.assest.ip`.  
\- Mapped `Coloumn5` to `target.hostname` and `target.assest.hostname`.  
\- Added new Grok at `Coloumn6` patterns to retrieve `EventReceivedTime` and `client_submit_time`.  
\- Mapped `Coloumn9` to `metadata.product_event_type`.  
\- Mapped `Coloumn10` to `intermediary.resource.attribute.labels`.  
\- Mapped `Coloumn12`,`Coloumn8`,`Coloumn7`,`Coloumn15`,`Coloumn24` and `Coloumn28` to `additional.fields`.  
\- Mapped `Coloumn13` to `network.email.to`.  
\- Mapped `Coloumn16` to `target.resource.attribute.labels`.  
\- Mapped `Coloumn19` to `network.email.subject`.  
\- Mapped `Coloumn20` to `network.email.from`.  
\- Mapped `Coloumn22` to `sec_result.description`.  
\- Mapped `Coloumn26` to `target.ip` and `target.assest.ip`.  
\- Mapped `Coloumn29` to `metadata.product_log_id`.  
\- Mapped `Coloumn30` to `metadata.product_version`.  
\- Added new date match filter to parse `EventReceivedTime`.  
\- Replaced Grok pattern with CSV blocks.   
2024-02-08 |  Enhancement:  
\- Added a new Grok pattern to parse new type of logs of format SYSLOG + KV.  
\- Mapped `version` to `metadata.product_version`.  
\- Mapped `sec_result_desc` to `network.email.subject`.   
2023-12-17 |  Enhancement  
\- Added new Grok patterns to parse new type of logs of format SYSLOG + KV.  
\- Mapped `MailboxDatabaseGuid`, `Mailboxes`, `StoreObjectIds`, `DeliveryLatency` to `security_result.detection_fields`.  
\- Mapped `client_submit_time`, `event_source`, `AttachCount`, `network_id` to `additional.fields`.  
\- Mapped `sec_result_desc` to `security_result.description`.  
\- Mapped `product_event_type` to `metadata.product_event_type`.  
\- Mapped `msg_id` to `network.email.mail_id`.  
\- Mapped `guid` to `metadata.product_log_id`.  
\- Mapped `internal_msgid` to `intermediary.resource.attribute.labels`.  
\- Mapped `recipients` to `target.user.email_addresses`.  
\- Mapped `recipients_status`,`recipents_count` to `target.resource.attribute.labels`.  
\- Mapped `msg_size` to `network.sent_bytes`.   
2023-11-20 |  Enhancement  
\- Added new Grok patterns to parse new type of logs of format SYSLOG + Key-Value.  
\- Mapped `host` to `event.idm.read_only_udm.principal.hostname`.  
\- Mapped `email_address` to `event.idm.read_only_udm.principal.user.email_addresses`.  
\- Mapped `ProxiedClientHostname` to `event.idm.read_only_udm.intermediary.hostname`.  
\- Mapped `ProxyHop1`, `MessageValue`, `IncludeInSla`, `Microsoft_Exchange_Transport_MailRecipient_RequiredTlsAuthLevel`, `IsSmtpResponseFromExternalServer`, `SlaExclusionReason`, `MsgRecipCount`, `FirstForestHop`, `PrioritizationReason`, and `TransportTrafficSubType` to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Mapped `DeliveryPriority` to `event.idm.read_only_udm.security_result.priority`.  
\- Mapped `ProxiedClientIPAddress` to `event.idm.read_only_udm.intermediary.ip`.  
\- Mapped `version` from `TransportTrafficSubType` to `event.idm.read_only_udm.metadata.product_version`.  
\- If `event.idm.read_only_udm.principal.user.email`, `event.idm.read_only_udm.target.user.email`, and either `event.idm.read_only_udm.principal.hostname` or `event.idm.read_only_udm.principal.ip` are present, then set `event.idm.read_only_udm.metadata.event_type` to `EMAIL_TRANSACTION`.   
2023-10-20 |  Enhancement  
\- Added a Grok pattern to parser logs with non-integer `session_id`.  
\- Mapped `AccountForest`, `DeliveryPriority`, `IsProbe`, `PersistProbeTrace`, `ProbeType` to `security_result.detection_fields`.   
2023-06-16 |  Enhancement  
Added grok to parse failing logs.  
\- Mapped `product_id` to `metadata.product_log_id`.  
\- Mapped `OriginalFromAddress` to `principal.user.email_addresses`.  
\- Mapped `E2ELatency`, `P2RecipStat`, `FromEntity`, `ToEntity` to `sec_result.detection_fields`.  
\- Wrote Grok pattern to parse failing logs.   
2022-11-25 |  ENHANCEMENT  
\- Handled unparsed logs by writing grok and mapping fields.  
\- Added condition check for date field.  
\- Mapped severity to security_result.severity.  
\- Mapped `sessionid` to `network.session_id`.  
\- Mapped `u_path` to `target.url`.   
2022-06-14 |  \- Modified the code to parse, mapped `EMAIL From` to network.email.from and `RCPT To` to network.email.to.  
\- Mapped `sequence-number` to additional.filed as key/value pair.   
2022-05-02 |  Bug - Modified the code to support 24hr time format for the `EventReceivedTime` field.  
Added regexp condition for email address parsing error.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
