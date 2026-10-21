---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thinkst-canary-changelog/
title: Change log for THINKST_CANARY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:12:40.589804+00:00
---

# Change log for THINKST_CANARY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thinkst-canary-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for THINKST_CANARY

Date | Changes  
---|---  
2026-07-10 |  Enhancement:  
\- event.idm.read_only_udm.target.port: Newly mapped `DstPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `SrcPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.network.dns.questions: Newly mapped `Hostname` raw log field with `event.idm.read_only_udm.network.dns.questions` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `Hostname`, `Host` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Flock`, `Reminder`, `EventName`, `Merchant`, `TransactionAmount`, `TransactionCurrency`, `MerchantIdentifier` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped `Sec-Ch-Ua-Platform`, `Os` raw log fields with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `City` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `Country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `Ip`, `X-Forwarded-For` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.location.region_coordinates.latitude: Newly mapped `Latitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- event.idm.read_only_udm.principal.location.region_coordinates.longitude: Newly mapped `Longitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- event.idm.read_only_udm.principal.location.state: Newly mapped `Region` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `DocumentId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `TheirEmail` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.about.user.email_addresses: Newly mapped `OurEmail` raw log field with `event.idm.read_only_udm.about.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.file.mime_type: Newly mapped `Mimetypes` raw log field with `event.idm.read_only_udm.principal.file.mime_type` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `Pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.target.asset.attribute.labels: Newly mapped `MaskedCardNumber` raw log field with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `ConsoleCanarytokenDomain`, `ClientName`, `ClientVersion`, `Sec-Ch-Ua`, `Sec-Ch-Ua-Mobile`, `Sec-Ch-Ua-Platform`, `Browser`, `Os`, `Version`, `Platform`, `Language`, `Installed`, `Vendor`, `Name` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Content-Length`, `Content-Type`, `Enabled`, `ClientRole`, `MaxPacketSize`, `ProgramName`, `SequenceId`, `Token`, `Accept-Language`, `Accept-Encoding`, `Accept`, `Sec-Fetch-Dest`, `Sec-Fetch-Mode`, `Sec-Fetch-Site`, `Sec-Fetch-User`, `Upgrade-Insecure-Requests`, `Connection`, `Abbr`, `CountryCode`, `CountryCode3`, `CurrencyCode`, `HostDomain`, `Id`, `IsBogon`, `IsProxy`, `IsTor`, `IsV4Mapped`, `IsV6`, `IsVpn`, `LanguageCode`, `TimezoneName`, `Offset`, `RegionCode`, `Time`, `Valid`, `ContinentCode`, `Locale`, `PacketLength`, `ClientFlags`, `ClientAuthPlugin`, `CharacterSet`, `AcquirerIdentifier` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set event_type to `USER_UNCATEGORIZED` and `STATUS_UPDATE` when user or principal machine data is present else set event_type to `GENERIC_EVENT`.  
\- event.idm.read_only_udm.network.application_protocol: Set the `event.idm.read_only_udm.network.application_protocol` UDM field to `DNS` for DNS log.   
2026-06-26 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `description.matched_annotations.tripwire_trigger`, `description.events.password`, `description.events.MESSAGE` and `description.events.sectors` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `description.events.user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `description.events.cmd` and `description.events.db` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `description.events.OLD_LOGTYPE` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-06-02 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `description.events.transaction_date`,`description.acknowledged`, `description.local_time`, `elem.acquirer_identifier`, `elem.masked_card_number`, `elem.transaction_currency`, `elem.transaction_type`, `elem.ip_blocklist.is_proxy`,`elem.ip_blocklist.is_tor`, `elem.ip_blocklist.is_vpn`, `elem.timestamp`, `elem.timestamp_std` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `elem.client_public_key`, `elem.client_session_index`, `elem.geoip.city`, `elem.geoip.country`, `elem.geoip.country_code`, `elem.geoip.country_code3`, `elem.geoip.currency_code`, `elem.geoip.ip`, `elem.geoip.is_bogon`, `elem.geoip.is_v4_mapped`, `elem.geoip.is_v6`, `elem.geoip.language_code`, `elem.geoip.latitude`, `elem.geoip.longitude`, `elem.geoip.region`, `elem.geoip.region_code`, `elem.geoip.valid`, `elem.geoip.timezone.abbr`, `elem.geoip.timezone.date`, `elem.geoip.timezone.id`, `elem.geoip.timezone.name`, `elem.geoip.timezone.offset`, `elem.geoip.timezone.time`, `elem.src_host`, `elem.src_port` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `elem.merchant` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.location.city`: Newly mapped `elem.merchant_details.city` raw log field with `event.idm.read_only_udm.target.location.city` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `elem.merchant_details.country` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `elem.merchant_details.merchant_identifier` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `elem.merchant_details.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `elem.status`, `elem.transaction_amount` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-04-07 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Newly mapped `elem.INSTANCE_NAME` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `elem.HEADERS.`upgrade-insecure-requests`, `elem.HEADERS.cookie` and `elem.SKIN` raw log fields with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` when `_md_product_event_type` is `HTTP Page Load`.  
\- Added support for `HTTP Page Load` logs.   
2025-11-21 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `updated`, `updated_std`, `description.created_std`, `description.events_list`, `description.events.FUNC_CODE`, `description.events.FUNC_NAME`, `description.events.SFUNC_CODE`, `description.events.SFUNC_NAME`, `description.events.UNIT_ID`, `description.events.timestamp_std`, `elem.URL`, `description.local_time`, `elem.event_descrip`, `elem.lt`, `elem.offline_text`, `elem.uptime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `elem.why`, `elem.online`, `description.acknowledged`, `updated_time` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added conditional check for `_md_product_event_type` to include `HTTP Proxy Request`, `Offline Events Dropped`, `ModBus Request`, `New Canaries added`, `MySQL Login Attempt".  
\- Added conditional check for `_md_event_type` to default to `GENERIC_EVENT` if empty.  
\- Added conditional check for `_md_product_event_type` to include `Honeypot Scanner Detected`.  
\- event.idm.read_only_udm.metadata.event_type: If `_md_product_event_type` is `HTTP Proxy Request`, updated to `NETWORK_HTTP`.  
\- event.idm.read_only_udm.metadata.event_type: If `_md_product_event_type` is `MySQL Login Attempt`, updated to `USER_LOGIN`.  
\- event.idm.read_only_udm.metadata.event_type: If `_md_product_event_type` is `ModBus Request`, updated to `NETWORK_CONNECTION`.  
\- event.idm.read_only_udm.metadata.event_type: If `_md_product_event_type` is `New Canaries added` and other conditions are not met, updated to `GENERIC_EVENT`.  
\- event.idm.read_only_udm.metadata.event_type: If [_md_event_type] is "`, updated to `GENERIC_EVENT".  
\- Added a fallback mechanism for JSON parsing: If the initial parse fails, the an on error flag _not_json is set. A new field `message1` is created by prepending `{` to the original message, and JSON parsing is re-attempted on `message1`.   
2025-06-26 |  Enhancement:  
\- Added Grok patterns to parse the unparsed logs.  
\- Replaced `thinkst_canary_udm_host_port_scan_event.include`, `thinkst_canary_udm_canary_disconnected_reconnected_event.include`, `thinkst_canary_udm_custom_tcp_service_request_event.include`, `thinkst_canary_udm_ssh_login_attempt_event.include`, `thinkst_canary_udm_ftp_telnet_login_attempt_event.include`, `thinkst_canary_udm_canary_settings_changed_event.include`, `thinkst_canary_udm_http_page_load_event.include` with the actual code.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Request`, `Command`, `PasswordHash`, `NTPCommand`, `Key`, `Salt`, `Password`, `ClientHash`, `connection`, `accept`, `FunctionName`, `FunctionData`, `TCPBannerID`, `IncidentHash`, `accept-encoding`, `VNCServerChallenge`, `VNCClientResponse`, `VNCPassword`, `Settings`, `LoginType` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `Database' raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.network.ftp.command: Newly mapped `Action' raw log field with `event.idm.read_only_udm.network.ftp.command` UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `DistinguishedName' raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `Path` and `URL' raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `ShareName`, `SMBVersion`, `CanaryID' raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Added KV block to extract values from the Headers field.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `ReverseDNS' raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `CanaryPublicIP' raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `User' raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `EC2InstanceID' raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped `EC2Region' raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `Domain' raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.target.files.names: Newly mapped `RemoteSMBName' raw log field with `event.idm.read_only_udm.target.files.names` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `Success` raw log field as ALLOW when `Success` is true and BLOCK when `Success' is false with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.target.location.name: Newly mapped `CanaryLocation' raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `Username' raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `BackgroundContext' raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Added null condition check for all the fields.  
\- Added on_error to all the mutate replace blocks.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `User-Agent' raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `Filename' raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `ThinkstCanary_Hostname' raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `ThinkstCanary_Process' raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- Removed redundant code for `_dst_hostname`, `CanaryIP`, `_src_host_reverse`, `_dst_host` and `User-Agent`.   
2025-02-26 |  Enhancement:  
\- When `_md_product_event_type` is `Host port scan`, `description.logtype` is mapped to `security_result.detection_fields`.   
2025-02-04 |  Enhancement:  
\- When `_md_product_event_type` is `Host port scan` or `Custom TCP Service Request`, `description.logtype` is mapped to `security_result.detection_fields`.   
2024-07-17 |  Enhancement:  
\- Added support for the following events: `Remote registry connection`, `Canarytoken triggered`, `File share connection`, `RDP connection made`, and `Canary settings changed`.   
2024-07-03 |  Enhancement:  
\- Added support for `dns` logs.   
2024-05-10 |  Enhancement:  
\- Added support for `Flock Settings Changed` events.  
\- If value of `_md_product_event_type` is `Flock Settings Changed`, added a Grok pattern to extract `user_id` from the field `elem.SETTINGS`.  
\- Mapped `user_id` to `principal.user.userid`.   
2024-03-05 |  Enhancement:  
\- Added support for `SIP Request` events.  
\- Added support for `TFTP Request` events.  
\- Mapped `hash_id` to `principal.file.sha1`.  
\- Mapped `HEADERS.user-agent` to `network.http.user_agent`.  
\- Mapped `description.node_id` to `principal.resource.attribute.labels`.  
\- Mapped `description.flock_id` to `principal.resource.attribute.labels`.  
\- Mapped `description.flock_name` to `principal.resource.attribute.labels`.  
\- Mapped `description.logtype` to `security_result.detection_fields`.  
\- Mapped `description.events_count` to `security_result.detection_fields`.  
\- Mapped `HEADERS.allow` to `security_result.detection_fields`.  
\- Mapped `HEADERS.call-id` to `security_result.detection_fields`.  
\- Mapped `HEADERS.contact` to `security_result.detection_fields`.  
\- Mapped `HEADERS.sip` to `security_result.detection_fields`.  
\- Mapped `HEADERS.cseq` to `security_result.detection_fields`.  
\- Mapped `HEADERS.expires` to `security_result.detection_fields`.  
\- Mapped `HEADERS.from` to `security_result.detection_fields`.  
\- Mapped `HEADERS.to` to `security_result.detection_fields`.  
\- Mapped `HEADERS.max-forwards` to `security_result.detection_fields`.   
2023-12-08 |  Enhancement:  
\- Since all `THINKST_CANARY` alerts are `critical` by default, set `is_alert` to `true` for all events.  
\- Since all `THINKST_CANARY` alerts are `critical` by default, set `is_significant` to `true` for all events.  
\- Since all `THINKST_CANARY` alerts are `critical` by default, set `security_result.severity` to `CRITICAL` for all events.  
\- Added support for `NMAP OS Scan Detected` events.   
2023-12-07 |  Enhancement:  
\- Added support for `WinRM Login Attempt`, `Telnet Login Attempt`, `NMAP OS Scan Detected`, `Redis Command` events.  
\- Added support to parse new pattern of `_metadata_event_timestamp`,`_event_time`.   
2023-09-15 |  Enhancement:  
\- Added support for `VNC Login Attempt` events.   
2023-08-04 |  Bug Fix:  
Following changes have been made for Canarytoken triggered events:  
\- Mapped to more specific event_type, for example `NETWORK_CONNECTION`.  
\- As `resource.id` is deprecated, mapped `canarytoken` to principal.resource.product_object_id.  
\- Also `event.idm.is_alert` is set to `true` for the given event.  
\- Set `security_result.category` to 'NETWORK_SUSPICIOUS.   
2023-05-12 |  Bug Fix - Added support for logs having `description.summary`=`MSSQL Login Attempt` and mapped `event_type` to `USER_LOGIN`;   
2022-12-04 |  Bug Fix -  
\- Added support for `HTTP Login Attempt`, `FTP Login Attempt`, `Website Scan`, `Console Settings Changed`, `RDP Login Attempt`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
