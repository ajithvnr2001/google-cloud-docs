---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-firewall-changelog/
title: Change log for UMBRELLA_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:25.506538+00:00
---

# Change log for UMBRELLA_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UMBRELLA_FIREWALL

Date | Changes  
---|---  
2026-06-17 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type` : Updated `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT` when there is no machine data or user information present in the raw log.  
\- `event.idm.read_only_udm.intermediary.resource.type`: Removed mapping of `identitType` from `event.idm.read_only_udm.intermediary.resource.type` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.intermediary.resource.resource_subtype`: Mapped `identitType` raw log field with `event.idm.read_only_udm.intermediary.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.intermediary.resource.id`: Removed mapping of `identity_id` from `event.idm.read_only_udm.intermediary.resource.id` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.intermediary.resource.product_object_id`: Mapped `identity_id` raw log field with `event.idm.read_only_udm.intermediary.resource.product_object_id` UDM field.   
2026-06-09 |  Enhancement:  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `column37` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Changed key for `column25` from `app_ID` to `aws_region`.  
\- `event.idm.read_only_udm.additional.fields`: Changed key for `column26` from `aws_region` to `app_ID`.   
2025-10-06 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `egress_IP` raw log field to event.idm.read_only_udm.intermediary.ip.  
\- `event.idm.read_only_udm.intermediary.resource.type`: Newly mapped `identitType` raw log field to event.idm.read_only_udm.intermediary.resource.type.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `source_port` raw log field to event.idm.read_only_udm.principal.port.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `fqdns` raw log field to event.idm.read_only_udm.principal.administrative_domain.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `packets_sent` raw log field to event.idm.read_only_udm.network.sent_packets.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `received_packets` raw log field to event.idm.read_only_udm.network.received_packets.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytes_sent` raw log field to event.idm.read_only_udm.network.sent_bytes.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `bytes_received` raw log field to event.idm.read_only_udm.network.received_bytes.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `destination_country` raw log field to event.idm.read_only_udm.target.location.country_or_region.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `packetSize`, `destination_list_IDs`, `first_packet_timestamp`, `last_packet_timestamp`, `fw_event_ID`, `app_ID`, `aws_region`, `private_app_group_ID`, `private_flow`, `posture_ID`, `casi_category_IDs`, `traffic_source`, `content_category_IDs`, `content_category_list_IDs`, `organization_ID`, and `egress` raw log fields to event.idm.read_only_udm.additional.fields.  
\- Modified the initial `message` field by replacing the string ``, `` with ``,`` to correct CSV field separation.   
2025-09-06 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `principal_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `principal_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `pcdetails` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `tcdetails`raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `vcdetails` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `principalip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `principalip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly Mapped `column20` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly Mapped `phost` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field when phost is `AD Computers`, `Roaming Computers`, `Anyconnect Roaming Client`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly Mapped `phost` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field when phost is `AD Computers`, `Roaming Computers`, `Anyconnect Roaming Client`.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `phost` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field when phost is not null.  
\- event.idm.read_only_udm.target.hostname: Newly Mapped `thost` raw log field to `event.idm.read_only_udm.target.hostname` UDM field when thost is `AD Computers`, `Roaming Computers`, `Anyconnect Roaming Client`.  
\- event.idm.read_only_udm.target.asset.hostname: Newly Mapped `thost` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field when thost is `AD Computers`, `Roaming Computers`, `Anyconnect Roaming Client`.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `thost` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field when thost is not null.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `daction` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `dns_r_message` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-01-29 |  Enhancement:  
\- Added null check before mapping `originId` to `intermediary.resource.id`.  
\- Added null check before mapping `identity` to `intermediary.resource.name`.  
\- Added null check before mapping `dataCenter` to `intermediary.location.name`.   
2025-01-21 |  Enhancement:  
\- Added drop tag for not supported logs.  
\- Added support for new csv logs.  
\- Mapped `organization_id` to `principal.asset.attribute.labels`.  
\- Mapped `http_response_code` to `network.http.response_code`.  
\- Mapped `rule_Id` to `security_result.rule_id`.  
\- Mapped `sec_description` to `security_result.description`  
\- Mapped `sec_action` to `security_result.action`.  
\- Mapped `intermediary_hostname` to `intermediary.hostname`  
\- Mapped `most_granular_identity` to `principal.asset.attribute.labels`.  
\- Mapped `granular_identity` to `target.asset.attribute.labels`.  
\- Mapped `http_method` to `network.http.method`.  
\- Mapped `usr_agent` to `network.http.user_agent`.  
\- Mapped `refer_url` to `network.http.referral_url`.  
\- Mapped `target_url` to `target.url`.  
\- Mapped `_internalip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `_externalip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `response_size` to `network.received_bytes`.  
\- Mapped `dns_rrtype` to `network.dns.questions`.  
\- Mapped `response_code` to `network.dns.response_code`.  
\- Mapped `desc` to `metadata.description`.  
\- Mapped `principal_host` to `principal.hostname`.  
\- Mapped `target_host` to `target.hostname`.  
\- Added condition check before mapping `direction` to `network.direction`.   
2022-09-02 |  Enhancement:  
\- Migrated customer specific parser to default parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
