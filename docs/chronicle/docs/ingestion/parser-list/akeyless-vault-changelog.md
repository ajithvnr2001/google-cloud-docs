---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akeyless-vault-changelog/
title: Change log for AKEYLESS_VAULT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:18.848622+00:00
---

# Change log for AKEYLESS_VAULT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akeyless-vault-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AKEYLESS_VAULT

Date | Changes  
---|---  
2026-04-20 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `remote_addr` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `request_parameters.resolved_item_name` raw log fields to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `status` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `event.idm.read_only_udm.security_result.action` UDM field with `action` raw log field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `action` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` UDM field with `action` raw log field.   
2026-04-08 |  Enhancement:  
\- Added a Grok pattern to parse new pattern of SYSLOG logs.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed second element of `remote_addr` raw log field from the `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields as it represents gateway ip more than a client ip.  
\- `event.idm.read_only_udm.intermediary.ip`: Mapped the second element of `remote_addr` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `syslog_hostname` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `process_name` raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.observer.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.observer.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- Added a conditional check before already existing mapping of `request_parameters.unique_id` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `request_parameters.unique_id` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `item_type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `request_parameters.session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `duration_in_ms`, `request_parameters.source`, and `request_parameters.item_accessibility` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2023-09-16 |  Enhancement:  
\- Adjusted the parser to support JSON logs along with KV logs.  
\- Mapped `request_parameters.access_type` to `target.resource.attribute.labels`.  
\- Mapped `request_parameters.product` to `target.resource.attribute.labels`.  
\- Mapped `request_parameters.transaction_type` to `target.resource.attribute.labels`.  
\- Mapped `request_parameters.user_agent` to `target.resource.attribute.labels`.  
\- Mapped `request_parameters.unique_id` to `target.resource.attribute.labels`.  
\- Mapped `request_parameters.comment` to `target.resource.attribute.labels`.  
\- Mapped `request_parameters.token_id` to `target.resource.attribute.labels`.  
\- Mapped `request_parameters.operation` to `target.resource.attribute.labels`.  
\- Mapped `request_parameters.universal_identity_rotate_type` to `target.resource.attribute.labels`.  
\- Mapped `remote_addr array` to `principal.ip`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
