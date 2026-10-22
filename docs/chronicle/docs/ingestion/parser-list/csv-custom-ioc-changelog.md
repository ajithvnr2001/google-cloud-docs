---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/csv-custom-ioc-changelog/
title: Change log for CSV_CUSTOM_IOC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:33.495076+00:00
---

# Change log for CSV_CUSTOM_IOC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/csv-custom-ioc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CSV_CUSTOM_IOC

Date | Changes  
---|---  
2025-08-01 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- event.idm.entity.metadata.threat.first_discovered_time: Newly mapped first_discovered_str raw log field to event.idm.entity.metadata.threat.first_discovered_time.  
\- event.idm.entity.metadata.threat.category_details: Newly mapped threat_summary raw log field to event.idm.entity.metadata.threat.category_details.  
\- event.idm.entity.metadata.threat.last_updated_time: Newly mapped last_updated_str raw log field to event.idm.entity.metadata.threat.last_updated_time.  
\- event.idm.entity.metadata.interval.start_time: Newly mapped date_added raw log field to event.idm.entity.metadata.interval.start_time.  
\- event.idm.entity.entity.file.sha256: if indicator_value matches `^[a-fA-F0-9]{64}$` then map indicator_value to event.idm.entity.entity.file.sha256.  
\- event.idm.entity.entity.file.sha1: if indicator_value matches `^[a-fA-F0-9]{40}$` then map indicator_value to event.idm.entity.entity.file.sha1.  
\- if indicator_type is set to URL then set event.idm.entity.metadata.entity_type to URL.  
\- if indicator_type is set to HASH then set event.idm.entity.metadata.entity_type to FILE.  
\- if indicator_type is set to IP then set event.idm.entity.metadata.entity_type to IP_ADDRESS.  
\- Set event.idm.entity.metadata.product_name to Proofpoint Threat Intelligence.  
\- Set event.idm.entity.metadata.vendor_name to Proofpoint.  
\- Set event.ioc.confidence_score to HIGH.  
\- event.ioc.description: Newly mapped campaign raw log field to event.ioc.description.  
\- event.idm.entity.metadata.threat.description: Newly mapped campaign raw log field to event.idm.entity.metadata.threat.description.  
\- event.idm.entity.entity.hostname: Newly mapped hostname raw log field to event.idm.entity.entity.hostname.  
\- event.ioc.domain_and_ports.domain: Newly mapped hostname raw log field to event.ioc.domain_and_ports.domain.   
2024-02-15 |  Enhancement:  
\- When `itype` is `md5` and `value` is sha256 format, then mapped `value` to `entity.entity.file.sha256`.  
\- When `itype` is `md5` and `value` is sha1 format, then mapped `value` to `entity.entity.file.sha1`.   
2024-02-12 |  Enhancement:  
\- Added support for domain, URL, md5, file and email type logs.  
\- Mapped `email` to `entity.entity.user.email_addresses`.   
2024-02-02 |  Enhancement:  
\- Added support to new format logs.  
\- Mapped `srcip` to `entity.entity.ip` and `ioc.ip_and_ports.ip_address`.  
\- Mapped `classification` to `threat.category_details`.  
\- Mapped `confidence` to `threat.confidence_score`.  
\- Mapped `resource_uri` to `threat.url_back_to_product`.  
\- Mapped `country` to `entity.entity.location.country_or_region`.  
\- Mapped `lat` to `entity.entity.location.region_latitude`.  
\- Mapped `lon` to `entity.entity.location.region_longitude`.  
\- Mapped `md5` to `entity.entity.file.md5`.  
\- Mapped `domain` to `entity.entity.hostname`.  
\- Mapped `date_first` to `threat.first_discovered_time`.  
\- Mapped `date_last` to `threat.last_updated_time`.  
\- Mapped `id` to `entity.metadata.product_entity_id`.  
\- Mapped `detail2` to `threat.description`.  
\- Mapped `detail` to `threat.summary`.  
\- Mapped `asn`, `import_session_id`, `itype`, `maltype`, `media`, `media_type`, `org`, `source`, `source_feed_id`, `state`, `trusted_circle_ids` and `update_id` to `threat.detection_fields`.   
2023-09-11 |  \- Added support for file type logs and mapped them as ENTITY data.   
2022-05-20 |  Enhancement:  
\- Added support for storing ENTITY data.  
\- Added support for IOC domains, IPs, and URLs in Custom IOC (CSV).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
