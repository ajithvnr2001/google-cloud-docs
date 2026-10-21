---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-xdr-changelog/
title: Change log for VECTRA_XDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:09:25.257428+00:00
---

# Change log for VECTRA_XDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-xdr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VECTRA_XDR

Date | Changes  
---|---  
2026-04-24 |  \- Mapped `entity_uid` raw log field with `principal.mac` or `principal.ip` UDM field based on value.  
\- Mapped details.http_hostname raw log field with target.hostname UDM field.  
\- Mapped details.http_hostname and details.http_url raw log fields with target.url UDM field.  
\- Mapped details.http_method raw log field with network.http.method UDM field.  
\- Mapped details.http_status raw log field with network.http.response_code UDM field.  
\- Mapped details.http_user_agent raw log field with network.http.user_agent UDM field.  
\- Mapped details.bytes_received raw log field with network.sent_bytes UDM field.  
\- Mapped details.bytes_sent raw log field with network.received_bytes UDM field.  
\- Mapped details.src_ip raw log field with principal.ip UDM field.  
\- Mapped details.dst_ip raw log field with target.ip UDM field.  
\- Mapped details.dst_port raw log field with target.port UDM field.   
2025-12-30 |  \- Mapped `caller_ip_addresses` from the `detail` object to `principal.ip`.   
2025-08-18 |  \- For events of type `account`, the IP extracted from the `name` field is now mapped to `target.ip` instead of `target.user.attribute.labels`.  
\- For events not of type `account`, the IP extracted from the `name` field is now mapped to `target.ip` instead of `target.hostname`.   
2025-05-14 |  \- Newly created label for Vectra XDR(RUX) logs.  
\- Previously the vectra RUX data supported under VECTRA_DETECT parser.  
\- Created new label VECTRA_XDR for RUX data.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
