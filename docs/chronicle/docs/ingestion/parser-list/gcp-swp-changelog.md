---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-swp-changelog/
title: Change log for GCP_SWP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:55:29.831866+00:00
---

# Change log for GCP_SWP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-swp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_SWP

Date | Changes  
---|---  
2026-09-11 |  Enhancement:  
\- Modified grok patterns on `httpRequest.remoteIp` and `httpRequest.serverIp` to extract `remote_port` and `server_port` along with the IP addresses.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `remote_port` (extracted from `httpRequest.remoteIp`) raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `jsonPayload.enforcedGatewaySecurityPolicy.clientServiceAccount` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.server_name`: Newly mapped `jsonPayload.enforcedGatewaySecurityPolicy.serverNameIndication` raw log field to `event.idm.read_only_udm.network.tls.client.server_name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `jsonPayload.tlsSniHostname` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `server_port` (extracted from `httpRequest.serverIp`) raw log field to `event.idm.read_only_udm.principal.port` UDM field.   
2024-04-15 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
