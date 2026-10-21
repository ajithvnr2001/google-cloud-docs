---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-estreamer-changelog/
title: Change log for CISCO_ESTREAMER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:24:19.041145+00:00
---

# Change log for CISCO_ESTREAMER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-estreamer-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_ESTREAMER

Date | Changes  
---|---  
2025-03-17 |  Enhancement:  
\- Changed mapping for `dvcpid` from `security_result.about.process.pid` to `intermediary.process.pid`.  
\- Changed the name of `additional_start.key` from `start` to `StartTime`.  
\- Removed mapping of `dvcpid` from `security_result.about.process.pid`.   
2025-02-26 |  Enhancement:  
\- If `act` is `Block`, then mapped `BLOCK` to `security_result.action`. Mapped `cs5` to `security_result.description`.  
\- If `cs5` is `DNS Cryptomining`, `URL Cryptomining`, or `Cryptomining`, mapped `SOFTWARE_PUA` to `security_result.category`.  
\- If `cs5` is `CnC`, mapped `NETWORK_COMMAND_AND_CONTROL` to `security_result.category`.  
\- If `cs5` is `Tor_exit_node`, mapped `TOR_EXIT_NODE` to `security_result.category`.  
\- If `cs5` is `DNS Phishing` or `Phishing`, mapped `PHISHING` to `security_result.category`.  
\- If `cs5` is `Malicious`, `DNS Malicious`, `DNS Malware`, `URL Malicious`, or `Malware`, mapped `NETWORK_MALICIOUS` to `security_result.category`.   
2025-02-13 |  Enhancement:  
\- Changed mapping for `request` from `network.http.referral_url` to `target.url`.  
\- Added a new Grok pattern to handle edge cases for parsing domain name from `request`.   
2024-11-28 |  Enhancement:  
\- Changed the mapping of `hostname` from `principal.hostname` to `intermediary.hostname`.  
\- Changed the mapping of `dvchost` from `target.hostname` to `intermediary.hostname`.  
\- Mapped `destinationDnsDomain` to `target.hostname` and `target.asset.hostname`.  
\- Added event_types `NETWORK_HTTP`, `NETWORK_DHCP`, and `NETWORK_DNS`.   
2024-06-21 |  Enhancement:  
\- Mapped `app` to `network.application_protocol`.   
2024-06-20 |  Enhancement:  
\- Mapped `request` to `network.http.referral_url`.  
\- Mapped `fsize` to `target.file.size`.  
\- Mapped `fileHash` to `target.file.sha256`.  
\- Mapped `fileType` to `target.file.mime_type`.  
\- Mapped `fname` to `target.file.full_path`.  
\- Mapped `deviceExternalId` to `principal.asset.asset_id`.  
\- If `deviceDirection` is equal to `1` then mapped `network.direction` to `OUTBOUND` and if `deviceDirection` is equal to `0` then mapped `network.direction` to `INBOUND`.  
\- Mapped `app` to `network.application_protocol`.  
\- Mapped `destinationDnsDomain` to `network.dns.questions.name`.  
\- Mapped `outcome` to `security_result.summary`.  
\- If `act` is equal to `Malware Block` then mapped `security_result.action` to `BLOCK`.   
2024-06-04 |  Bug-fix  
\- Updated Grok to parser unparsed logs.   
2024-05-15 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
