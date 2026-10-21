---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-emps-changelog/
title: Change log for FIREEYE_EMPS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:35:15.829400+00:00
---

# Change log for FIREEYE_EMPS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-emps-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FIREEYE_EMPS

Date | Changes  
---|---  
2026-08-04 |  Enhancement  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `sourceDnsDomain` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields, as `sourceDnsDomain` represents a domain name rather than a target host.  
\- `event.idm.read_only_udm.network.dns_domain`: Mapped `sourceDnsDomain` raw log field with `event.idm.read_only_udm.network.dns_domain` UDM field.   
2026-07-06 |  Enhancement  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_name` field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `device_event_class_id` field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-15 |  Enhancement  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `flexString2` from `event.idm.read_only_udm.additional.fields` UDM field when `flexString2Label` is equal to `subject` since `flexString2` consists of email subject details.  
\- `event.idm.read_only_udm.network.email.subject`: Mapped `flexString2` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Updated the value of `event.idm.read_only_udm.metadata.product_name` from `EMPS` to `EX`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `version`, `device_product` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-15 |  Enhancement  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `cs1` and `cs1Label` from `event.idm.read_only_udm.additional.fields` UDM field when `cs1Label` is equal to `sname` to map to a more appropriate UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `cs1` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field when `cs1Label` is equal to `sname`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `cs4` and `cs4Label` from `event.idm.read_only_udm.additional.fields` UDM field when `cs4Label` is equal to `link` to map to a more appropriate UDM field.  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Mapped `cs4` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field when `cs4Label` is equal to `link`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `suser` raw log field from `event.idm.read_only_udm.principal.user.user_display_name` UDM field since `suser` contains valid email addresses of the sender.  
\- `event.idm.read_only_udm.network.email.from`: Mapped `suser` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Removed mapping of `duser` raw log field from `event.idm.read_only_udm.target.user.user_display_name` UDM field since `duser` contains valid email addresses of the recipient.  
\- `event.idm.read_only_udm.network.email.to`: Mapped `duser` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `fname` from `event.idm.read_only_udm.additional.fields` UDM field to map to a more appropriate UDM field since `fname` of the file's name.  
\- `event.idm.read_only_udm.target.file.names`: Mapped `fname` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.about.file.sha256`, `event.idm.read_only_udm.about.file.full_path`: Removed mapping of `fileHash` from `event.idm.read_only_udm.about.file.sha256` and `event.idm.read_only_udm.about.file.full_path` UDM field when `fileHash` contains a valid md5 hash value. The raw log field `filehash` represents the md5 hash value.  
\- `event.idm.read_only_udm.target.file.md5`: Mapped `fileHash` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `flexString1` and `flexString1Label` from `event.idm.read_only_udm.additional.fields` UDM field when `flexString1Label` is equal to `sha256sum` to map to a more appropriate UDM field.  
\- `event.idm.read_only_udm.about.file.sha256`: Mapped `flexString1` raw log field with `event.idm.read_only_udm.about.file.sha256` UDM field when `flexString1Label` is equal to `sha256sum`.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `observer_application` raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_severity_label` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `start` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` raw log field with `EMAIL_TRANSACTION` when sender and recipient email addresses are present.   
2024-10-29 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
