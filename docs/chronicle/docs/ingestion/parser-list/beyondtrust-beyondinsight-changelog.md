---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-beyondinsight-changelog/
title: Change log for BEYONDTRUST_BEYONDINSIGHT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:33.105224+00:00
---

# Change log for BEYONDTRUST_BEYONDINSIGHT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-beyondinsight-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BEYONDTRUST_BEYONDINSIGHT

Date | Changes  
---|---  
2026-03-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `nvps.filehash` (key: `filehash`) raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-12 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Removed mapping of `sourceip` from `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields when `agentid` is `AppAudit` in order to introduce more accurate mapping.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`:Newly mapped `sourceip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `agentid` is `AppAudit` in order to introduce more accurate mapping.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `nvps.xforwardedfor` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Added a new json filter to parse `nvps.xforwardedfor` raw log field.   
2026-03-03 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `nvps.userid` from `event.idm.read_only_udm.additional.fields` UDM field. As it is a product specific field, it should be mapped to `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Mapped `nvps.userid` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `eventid` from `event.idm.read_only_udm.additional.fields` UDM field. As it is better suited to be mapped to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Mapped `eventid` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `nvps.target` from `event.idm.read_only_udm.additional.fields` UDM field. As it is better suited to be mapped to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`:  
\- If `nvps.target` is not empty, updated the value of `event.idm.read_only_udm.target.resource.name` to the value of `nvps.target`.  
\- If `nvps.target` is empty and `nvps.title` is not empty, updated the value of `event.idm.read_only_udm.target.resource.name` to the value of `nvps.title`.  
\- Corrected UDM field name from `secrity_result.description` to `security_result.description`.  
\- `event.idm.read_only_udm.security_result.description`:  
\- If `nvps.description` is not empty, updated the value of `event.idm.read_only_udm.security_result.description` to the value of `nvps.description`.  
\- If `nvps.description` is empty and `nvps.reason` is not empty, updated the value of `event.idm.read_only_udm.security_result.description` to the value of `nvps.reason`.  
\- Added a conditional check if `FolderId` is empty before replacing it with the value `nvps.folderid`.  
\- Added a conditional check if `Folder` is empty before already existing mapping of `nvps.folder`.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `nvps.email` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `nvps.ownersdisplay` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `nvps.filename` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `nvps.filehash` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `nvps.secretid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `nvps.secrettype` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `nvps.folderpath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`:  
\- If `user` is empty and `username` is empty and `nvps.username` is empty and `nvps.owner` is not empty, Set the value of `event.idm.read_only_udm.target.user.userid` to the value of `nvps.owner`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `nvps.notes` (key: `notes`), `nvps.ticketnumber` (key: `ticketnumber`), `nvps.approver` (key: `approver`), `nvps.ownerid` (key: `ownerid`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-02 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `ips` from `event.idm.read_only_udm.principal.ip` since it is target field.  
\- `event.idm.read_only_udm.target.ip`: Mapped `ips` raw log field to `event.idm.read_only_udm.target.ip` since it is target field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `ips` from `event.idm.read_only_udm.principal.asset.ip` since it is target field.  
\- `event.idm.read_only_udm.target.asset.ip`: Mapped `ips` raw log field to `event.idm.read_only_udm.target.asset.ip` since it is target field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `ManagedSystem` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `ManagedSystem` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `ManagedAccount` raw log field to `event.idm.read_only_udm.target.user.userid`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `TicketNumber`, `TicketSystem`, `LogTime`, `Failed`, `Reason`, `Approver`, `bt_Category` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Added grok patterns to extract `ReleaseRequestId` from the `msg` field.  
\- Added KV filter to parse the `Target` field.   
2025-11-19 |  Enhancement:  
\- Added support for JSON format embedded within the `message` field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility`, `Category`, `AuditID`, `ActionType`, `AppUserID`, `FolderId`, `Folder`, `SecretType`, `CanManageOwnership`, `CanShareSecret`, `priority`, `Password`, `Title`, `version`, `CreateDate` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.intermediary.ip`.  
\- `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.intermediary.asset.ip`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `Name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `SecretId` raw log field to `event.idm.read_only_udm.target.resource.id`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `username` raw log field to `event.idm.read_only_udm.principal.user.email_addresses`.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `URL` raw log field to `event.idm.read_only_udm.target.url`.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `userId` raw log field to `event.idm.read_only_udm.principal.user.product_object_id`.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `appname` raw log field to `event.idm.read_only_udm.metadata.product_name`.  
\- Added `gsub` mutations to sanitize field names from the JSON payload before key-value extraction.   
2025-11-07 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `dst_user` raw log field to `event.idm.read_only_udm.target.user.userid`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `dst_host` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `src_user` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `nvps.source` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `nvps.source` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname`.  
\- `event.idm.read_only_udm.target.application`: Newly mapped ``BeyondInsight Application GUI`` raw log field to `event.idm.read_only_udm.target.application`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `nvps.areaname`, `nvps.context`, `nvps.active`, `nvps.genericappliancehealthactive`, `nvps.beyondinsightapplicationauditactive`, `nvps_hostname`, `nvps.port`, `nvps.genericappliancehealthenabled`, `nvps.beyondinsightapplicationauditenabled`, `nvps.genericappliancehealthseverity`, `nvps.outputpipeline`, `nvps.name` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `nvps.hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `nvps.hostname` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname`.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `sourcehost` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `shost` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `src_host` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `src_host` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped ``MACHINE`` raw log field to `event.idm.read_only_udm.extensions.auth.type`.  
\- `event.idm.read_only_udm.target.application`: Newly mapped ``BeyondInsight Appliance Management GUI`` raw log field to `event.idm.read_only_udm.target.application`.  
\- `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `inter_ip` raw log field to `event.idm.read_only_udm.intermediary.asset.ip`.  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `sourceip` from `event.idm.read_only_udm.principal.ip` as `sourceip` is a intermediary field.  
\- `event.idm.read_only_udm.intermediary.ip`: Mapped `sourceip` raw log field to `event.idm.read_only_udm.intermediary.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `sourceip` from `event.idm.read_only_udm.principal.asset.ip` as `sourceip` is a intermediary field.  
\- `event.idm.read_only_udm.intermediary.asset.ip`: Mapped `sourceip` raw log field to `event.idm.read_only_udm.intermediary.asset.ip`.  
\- `event.idm.read_only_udm.target.hostname`: Removed mapping of `nvps.clienthost` from `event.idm.read_only_udm.target.hostname` as `nvps.clienthsot` is mapped to intermediary.hostname as it is a intermediary.  
\- `event.idm.read_only_udm.intermediary.hostname`: Mapped `nvps.clienthost` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `nvps.clienthost` from `event.idm.read_only_udm.target.asset.hostname` as `nvps.clienthsot` is mapped to intermediary.asset.hostname as it is a intermediary.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `nvps.clienthost` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname`.  
\- `event.idm.read_only_udm.principal.hostname`: Removed mapping of `nvps.name` from `event.idm.read_only_udm.principal.hostname` as this is not the hostname. It is the name of the forwarder that has been configured.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `nvps.name` from `event.idm.read_only_udm.principal.asset.hostname` as this is not the hostname. It is the name of the forwarder that has been configured.  
\- Added grok patterns to extract `dst_user`, `dst_host`, `src_user`, `src_host`, and `src_ip` from the `eventdesc` field.  
\- Conditionally set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` or `USER_LOGOUT` based on `eventdesc` content and `agentid`.  
\- Added grok pattern to handle IP addresses within the `nvps.hostname` field, extracting to `nvps_hostname`.   
2025-07-23 |  Enhancement:  
\- Added gsubs to ensure proper mapping of KV format logs.  
\- Modified a gsub to ensure proper mapping of `OS` and `Agent Version` raw log fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `EventType` raw log field to `event.idm.read_only_udm.additional.fields` (with key `Event Type`).  
\- Added a grok pattern to check if `souirceip` is a valid IP address before mapping it to `event.idm.read_only_udm.principal.ip` UDM field.   
2025-05-13 |  Enhancement:  
\- Added support to handle the `#` character in the UDM Fields.  
\- Added support for the parsing the metadata.event_type.  
\- Added support required null checks while doing the mapping.   
2025-04-21 |  Enhancement:  
\- Added a grok pattern to support new format of SYSLOG logs.  
\- Added gsub to fix the kv parsing issue.   
2025-02-06 |  Enhancement:  
\- Added support to map the unparsed fields.   
2024-11-22 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
