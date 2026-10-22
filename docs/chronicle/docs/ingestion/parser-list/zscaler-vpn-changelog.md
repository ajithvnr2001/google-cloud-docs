---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-vpn-changelog/
title: Change log for ZSCALER_VPN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:21.193238+00:00
---

# Change log for ZSCALER_VPN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-vpn-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZSCALER_VPN

Date | Changes  
---|---  
2026-02-10 |  Enhancement:  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `ClientCity` raw log field to `event.idm.read_only_udm.principal.location.city`.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `Platform` raw log field to `event.idm.read_only_udm.principal.platform`.  
\- Added logic to conditionally populate event.idm.read_only_udm.target.hostname from `Host` or `Hostname` raw fields.  
\- Added logic to populate event.idm.read_only_udm.principal.hostname from the `Hostname` raw field when `Host` is also present.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `Host` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `Hostname` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `TimestampConnectionStart`, `TimestampConnectionEnd`, `TimestampCATx`, `TimestampCARx`, `TimestampZENFirstRxClient`, `TimestampZENFirstTxClient`, `TimestampZENLastRxClient`, `TimestampZENLastTxClient`, `TimestampConnectorZENSetupComplete`, `TimestampZENFirstRxConnector`, `TimestampZENFirstTxConnector`, `TimestampZENLastRxConnector`, `TimestampZENLastTxConnector`, `ZENBytesRxClient`, `ZENBytesTxClient`, `ZENTotalBytesRxConnector`, `ZENBytesRxConnector`, `ZENTotalBytesTxConnector`, `ZENBytesTxConnector` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Modified the parser to handle carriage returns and newlines (\r\n) in the raw log message to avoid parsing issues and used `replace` instead of `rename` for `Host` and `Hostname` fields to fix the failing logs. Due to this, the following UDM fields are now being parsed correctly:  
\- `event.idm.read_only_udm.extensions.auth.type`  
\- `event.idm.read_only_udm.intermediary[].ip[]`  
\- `event.idm.read_only_udm.intermediary[].port`  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.network.received_bytes`  
\- `event.idm.read_only_udm.network.sent_bytes`  
\- `event.idm.read_only_udm.network.session_id`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip[]`  
\- `event.idm.read_only_udm.principal.ip[]`  
\- `event.idm.read_only_udm.principal.location.country_or_region`  
\- `event.idm.read_only_udm.principal.location.region_latitude`  
\- `event.idm.read_only_udm.principal.location.region_longitude`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.principal.user.email_addresses[]`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result[].about.labels[].key`  
\- `event.idm.read_only_udm.security_result[].about.labels[].value`  
\- `event.idm.read_only_udm.security_result[].action[]`  
\- `event.idm.read_only_udm.security_result[].description`  
\- `event.idm.read_only_udm.security_result[].rule_name`  
\- `event.idm.read_only_udm.security_result[].summary`  
\- `event.idm.read_only_udm.target.application`  
\- `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.asset.ip[]`  
\- `event.idm.read_only_udm.target.ip[]`  
\- `event.idm.read_only_udm.target.port`  
\- `event.idm.read_only_udm.target.user.email_addresses[]`  
\- `event.idm.read_only_udm.target.user.group_identifiers[]`  
\- `event.idm.read_only_udm.target.user.userid`  
2023-06-08 |  Enhancement -  
\- Reduced generic percentage.   
2023-01-04 |  Bug-Fix-  
\- Mapped `LogTimestamp` to `event_timestamp`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
