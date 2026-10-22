---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stormshield-firewall-changelog/
title: Change log for STORMSHIELD_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:09.525628+00:00
---

# Change log for STORMSHIELD_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stormshield-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for STORMSHIELD_FIREWALL

Date | Changes  
---|---  
2026-02-04 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ruleid` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `id` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_host` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `dstcontinent` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels`. As dst is much more appropriate field for target.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dstcontinent` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `src_country` raw log field to `event.idm.read_only_udm.principal.location.country_or_region`. As dst is much more appropriate field for target.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dst_country` raw log field to `event.idm.read_only_udm.target.location.country_or_region`.   
2026-01-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `port` raw log field to `event.idm.read_only_udm.principal.port`.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `remotenet` raw log field to `event.idm.read_only_udm.target.ip`.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `remotenet` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `localnet` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `localnet` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `site` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `urlruleid` raw log field to `event.idm.read_only_udm.security_result.rule_id`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `status`, `auditid`, `tgt` (renamed from `target`), `sensible`, `contentpolicy`, `cnruleid`, `vulnid`, `family` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dstiprep` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Ethernet0`, `Ethernet1`, `Ethernet2`, `Ethernet3`, `Ethernet4`, `Ethernet5`, `Ethernet6`, `Ethernet7`, `Ethernet8`, `Ethernet9`, `Ethernet10`, `Ethernet11`, `Pvm`, `Qid0`, `ipsec`, `security`, `sslvpn0`, `sslvpn1`, `system`, `tz`, `startime`, `ipv`, `method`, `error`, `ikev`, `phase`, `side`, `cookie_i`, `cookie_r`, `spi_in`, `spi_out`, `solution`, `remote`, `targetclient`, `targetserver`, `discovery` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `product` raw log field to `event.idm.read_only_udm.principal.process.command_line`.  
\- Added support for the event `logtype` values: `web`, `ssl`, `monitor`, `auth`, `vpn`, `xvpn`, and `pvm`.  
\- Corrected mapping for `event.idm.read_only_udm.security_result.rule_id` to use the value of the `ruleid` variable instead of the literal string `ruleid`.  
\- Enhanced IP address validation and extraction for fields: `ipaddr`, `ipaddr1`, `remotenet`, and `localnet`.  
\- Refactored `metadata.event_type` assignment logic to be more conditional based on the presence of principal, target, user, and hostname information.  
\- Implemented dynamic mapping for various raw fields to UDM `additional.fields`, `security_result.detection_fields`, or `target.resource.attribute.labels` based on their keys.  
\- Raw field `target` is now renamed to `tgt` before key-value parsing.   
2023-06-29 |  Enhancement:  
\- Added a Grok pattern to support a new syslog header format.   
2022-08-08 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
