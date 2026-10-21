---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-deception-changelog/
title: Change log for ZSCALER_DECEPTION \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:47:18.822823+00:00
---

# Change log for ZSCALER_DECEPTION  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-deception-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZSCALER_DECEPTION

Date | Changes  
---|---  
2026-06-29 |  Enhancements for ZSCALER_DECEPTION parser.   
2025-08-12 |  \- Promoted ZSCALER_DECEPTION Premium parser to default. You can see full details in the parser configuration page - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-zscaler-logs  
\- This version will have an RC period - we encourage you to opt-in and make the required adjustments before it'll be automatically promoted to Default  
\- Enhancements for `recon` event:  
\- `src.artifact.ip`: Mapped `abuseip.ipAddress` raw log field with `src.artifact.ip` UDM field  
\- `src.artifact.location.country_or_region`: Mapped `abuseip.countryCode` raw log field with `src.artifact.location.country_or_region` UDM field  
\- `src.artifact.last_seen_time`: Mapped `abuseip.lastReportedAt` raw log field with `src.artifact.last_seen_time` UDM field  
\- `additional.fields[decoy_appliance_name]`: Mapped `decoy.appliance.name` raw log field with `additional.fields[decoy_appliance_name]` UDM field  
\- `target.user.product_object_id`: Mapped `decoy.client.id` raw log field with `target.user.product_object_id` UDM field  
\- `target.user.user_display_name`: Mapped `decoy.client.name` raw log field with `target.user.user_display_name` UDM field  
\- `additional.fields[decoy_network_name]`: Mapped `decoy.network_name` raw log field with `additional.fields[decoy_network_name]` UDM field  
\- `security_result.rule_set`: Mapped `decoy.recon.dataset` raw log field with `security_result.rule_set` UDM field  
\- `security_result.rule_labels[decoy_recon_dataset_type]`: Mapped `decoy.recon.dataset_type` raw log field with `security_result.rule_labels[decoy_recon_dataset_type]` UDM field  
\- `target.resource.resource_subtype`: Mapped `decoy.type` raw log field with `target.resource.resource_subtype` UDM field  
\- `target.resource.product_object_id`: Mapped `decoy.id` raw log field with `target.resource.product_object_id` UDM field  
\- `target.resource.name`: Mapped `decoy.name` raw log field with `target.resource.name` UDM field  
\- `principal.network.http.user_agent`: Mapped `recon.user_agent.string` raw log field with `principal.network.http.user_agent` UDM field  
\- `principal.security_result.detection_fields[attacker_threat_parse_ids]`: Mapped `attacker.threat_parse_ids` raw log field with `principal.security_result.detection_fields[attacker_threat_parse_ids]` UDM field  
\- `principal.network.http.method`: Mapped `recon.method` raw log field with `principal.network.http.method` UDM field  
\- `principal.network.application_protocol`: Mapped `recon.scheme` raw log field with `principal.network.application_protocol` UDM field  
\- `principal.network.http.response_code`: Mapped `recon.status` raw log field with `principal.network.http.response_code` UDM field  
\- `metadata.event_type`: Mapping for `metadata.event_type` has been updated from `NETWORK_HTTP` to `NETWORK_CONNECTION`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
