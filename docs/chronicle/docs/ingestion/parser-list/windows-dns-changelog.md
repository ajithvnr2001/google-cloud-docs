---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-dns-changelog/
title: Change log for WINDOWS_DNS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:52.830563+00:00
---

# Change log for WINDOWS_DNS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-dns-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINDOWS_DNS

Date | Changes  
---|---  
2026-09-25 |  \- additional.fields: Newly mapped `Type` raw log field with its corresponding translated string value in `additional.fields` UDM field.   
2026-09-01 |  \- Enhanced the Grok pattern to accurately map the `target.hostname` and `network.dns.questions.name` UDM fields.   
2026-07-29 |  \- Updated the field mapping for the WINDOWS_DNS parser.  
\- Please refer to the parser documentation page for information regarding the updated UDM mappings - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-dns#udm-mapping-delta   
2026-04-01 |  \- additional.fields: Newly mapped `SourceModuleName` raw log field with `additional.fields` UDM field.   
2026-01-13 |  \- intermediary.hostname: Added mapping of `syslog_host` field to `intermediary.hostname` instead to appropriately map the syslog header hostname.   
2026-01-02 |  \- intermediary.hostname: Newly mapped `Hostname` raw log field with `intermediary.hostname` UDM field for audit logs.   
2025-12-24 |  \- intermediary.ip: Added mapping of `syslog_host` field to `intermediary.ip` instead to appropriately map the syslog header ip.   
2025-11-17 |  \- intermediary.hostname: Removed mapping of `syslog_host` field from principal.hostname and mapped it to `intermediary.hostname` instead to appropriately map the syslog header hostname.  
\- Enhanced the Grok pattern to map the network.direction UDM field as INBOUND for `rcv` value and OUTBOUND for `snd` value.   
2025-09-12 |  \- `XML`: Added support for DNS Analytical logs in `XML` format.   
2025-03-19 |  \- Added a new Grok pattern to support the existing log format, which does not contain `\n` at the end of the line.   
2025-02-18 |  \- Updated the Grok pattern to support a new log structure.  
\- Added new pattern `dd-MM-yyyy HH:mm:ss` to the date filter for `EventTime` raw log field.   
2025-02-05 |  \- Mapped `resource_attributes.host.name` raw log field with `intermediary.hostname` UDM field.  
\- Mapped `resource_attributes.os.type` raw log field with `intermediary.asset.platform_software.platform` UDM field.   
2025-01-21 |  \- Modified the Grok pattern to parse events with a.m. and p.m. in the timestamp.   
2025-01-17 |  \- Added new pattern `M/d/yyyy HH:mm:ss A` to the date filter for `EventTime` raw log field.   
2024-06-25 |  \- Added support for logs with CSV data in the `Message` field.   
2024-06-19 |  \- Modified the Grok pattern to parse the logs in JSON format.  
\- Added support for new XML logs, which get ingested from the BindPlane agent.   
2024-05-28 |  Enhancement:  
\- Mapped `dns_record_type` to `additional.fields`.   
2024-05-15 |  Added additional mappings for deprecated `noun.labels`.   
2024-04-17 |  \- Updated mapping of `EventReceivedTime` and `EventTime` raw log fields.   
2024-03-13 |  \- Parsed data from `ANSWER SECTION` in the log.  
\- Update mapping of `metadata.event_timestamp` UDM field.   
2024-02-14 |  \- Parsed debug data from the log.   
2024-01-18 |  \- Added support for the text format log containing debug data.  
\- Added support for logs containing the date in the German format   
2023-12-13 |  Added support for logs containing Chinese characters.   
2023-11-29 |  \- Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-10-18 |  Added support for the text format.   
2023-10-04 |  Added validation before mapping the `sysloghost` to the `principal.hostname`.   
2023-08-23 |  Used `on_error` function to prevent error due to double UDM mapping.   
2023-06-28 |  \- Added support for escape characters (for example, `\r\n`) in NXLog `im_file` module logs.  
\- Changed mapping for data from answer section of message field and mapped other answer section data as well for DNS record requests of type `A`, `AAAA` and `PTR`.  
\- Deleted a dot `.` at the end of domain name for Microsoft Windows DNS logs   
2023-05-31 |  \- For DNS record requests of type A, AAAA and PTR, extracted data from answer section of `message` field and mapped it.  
\- Mapped `network.dns.questions.name` value to `target.hostname`.   
2023-05-02 |  Added support for DNS record requests of type A, AAAA and PTR.   
2023-02-15 |  Added a grok pattern to handle date format(MM-DD-YYYY) and time format without AM/PM.   
2022-07-08 |  Prioritized mapping events with STATUS_UPDATE instead of GENERIC_EVENT where `principal.ip` or `target.ip` or `principal.hostname` are not null.   
2022-05-11 |  Added support for Syslog header+JSON format.   
2022-04-13 |  Formal launch of Chronicle's Windows DNS parser.  
This represents a comprehensive refresh to Windows DNS parsing, and is built from the ground up for improved stability, coverage, and efficacy.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
