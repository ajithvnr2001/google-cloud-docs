---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dns-atd-changelog/
title: Change log for GCP_DNS_ATD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:02.237091+00:00
---

# Change log for GCP_DNS_ATD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dns-atd-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_DNS_ATD

Date | Changes  
---|---  
2025-07-25 |  \- Newly created parser.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `Google Cloud DNS Threat Detector` to event.idm.read_only_udm.metadata.product_name.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `Google Cloud` to event.idm.read_only_udm.metadata.vendor_name.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record.insertId` raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record.timestamp` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `record.receiveTimestamp` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.network.dns.response_code: Newly mapped `record.jsonPayload.dnsQuery.responseCode` raw log field to event.idm.read_only_udm.network.dns.response_code.  
\- event.idm.read_only_udm.network.dns.answers: Newly mapped `record.jsonPayload.dnsQuery.rdata` raw log field to event.idm.read_only_udm.network.dns.answers.  
\- event.idm.read_only_udm.network.dns.questions.name: Newly mapped `record.jsonPayload.dnsQuery.queryName` raw log field to event.idm.read_only_udm.network.dns.questions.name.  
\- event.idm.read_only_udm.target.ip: Newly mapped `record.jsonPayload.dnsQuery.destinationIp` raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `record.jsonPayload.dnsQuery.destinationIp` raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `record.jsonPayload.dnsQuery.sourceIp` raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `record.jsonPayload.dnsQuery.sourceIp` raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `record.jsonPayload.dnsQuery.vmInstanceId` raw log field to event.idm.read_only_udm.principal.resource.id.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `record.jsonPayload.dnsQuery.protocol` raw log field to event.idm.read_only_udm.network.ip_protocol.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `record.resource.labels.id` raw log field to event.idm.read_only_udm.principal.resource.product_object_id.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `record.resource.labels.location` raw log field to event.idm.read_only_udm.principal.location.name.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `record.jsonPayload.dnsQuery.location` raw log field to event.idm.read_only_udm.principal.location.country_or_region.  
\- event.idm.read_only_udm.principal.resource.type: Newly mapped `record.resource.type` raw log field to event.idm.read_only_udm.principal.resource.type.  
\- event.idm.read_only_udm.security_result.threat_id: Newly mapped `record.jsonPayload.threatInfo.threatId` raw log field to `event.idm.read_only_udm.security_result.threat_id`.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `record.jsonPayload.threatInfo.threatDescription` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `record.severity` raw log field to `event.idm.read_only_udm.security_result.severity`.  
\- event.idm.read_only_udm.security_result.confidence: Newly mapped `record.jsonPayload.threatInfo.confidence` raw log field to `event.idm.read_only_udm.security_result.confidence`.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `record.jsonPayload.dnsQuery.vmProjectNumber` and `record.jsonPayload.dnsQuery.projectNumber` raw log fields to event.idm.read_only_udm.principal.resource.attribute.labels.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.jsonPayload.dnsQuery.authAnswer`, `record.jsonPayload.dnsQuery.queryTime`, `record.logName`, `record.jsonPayload.partnerId` and `record.jsonPayload.detectionTime` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.jsonPayload.dnsQuery.responseCode`, `record.jsonPayload.threatInfo.threatIndicatorType`, `record.jsonPayload.threatInfo.threatIndicator`, `record.jsonPayload.threatInfo.threatFeed`, `record.jsonPayload.threatInfo.category`, `record.jsonPayload.threatInfo.type`, `record.jsonPayload.threatInfo.threat`, `record.jsonPayload.threatInfo.severity` and `record.resource.labels.resource_container` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
