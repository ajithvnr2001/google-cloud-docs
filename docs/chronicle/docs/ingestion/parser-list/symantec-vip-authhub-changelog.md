---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-vip-authhub-changelog/
title: Change log for SYMANTEC_VIP_AUTHHUB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:11.260402+00:00
---

# Change log for SYMANTEC_VIP_AUTHHUB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-vip-authhub-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_VIP_AUTHHUB

Date | Changes  
---|---  
2025-03-11 |  Enhancement:  
\- Mapped `azserver-idp-response-verify-cert-ext-idpId`, `__THIS_RESOURCE_ID` and `admin-identityprovider-create-ext-resourceGuid` to `principal.user.attribute.cloud.project.id`.   
2024-06-04 |  Enhancement:  
\- Mapped `client` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `referrer` to `network.http.referral_url`.  
\- Mapped `server` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `httpReferrer` to `network.http.referral_url`.  
\- Mapped `bytes_sent` to `network.sent_bytes`.  
\- Mapped `status` to `network.http.response_code`.  
\- Mapped `path` to `principal.file.full_path`.  
\- Mapped `protocol` to `network.application_protocol`.  
\- Mapped `userIP` to `principal.ip`, `principal.asset.ip`, `target.ip`, `target.asset.ip`, `intermediary.ip`, `intermediary.asset.ip`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `principalId` to `principal.user.userid`.  
\- Mapped `kubernetes.host` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `relVersion` to `metadata.product_version`.  
\- Mapped `thread` to `additional.fields`.  
\- Mapped `service` to `additional.fields`.  
\- Mapped `sub` to `additional.fields`.  
\- Mapped `subType` to `additional.fields`.  
\- Mapped `tid` to `additional.fields`.  
\- Mapped `tname` to `additional.fields`.  
\- Mapped `userDN` to `additional.fields`.  
\- Mapped `userGuid` to `additional.fields`.  
\- Mapped `userIdpGuid` to `additional.fields`.  
\- Mapped `userRiskLevel` to `additional.fields`.  
\- Mapped `userUniversalId` to `additional.fields`.  
\- Mapped `userRiskScore` to `additional.fields`.  
\- Mapped `userIp` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `__isAuditIdLcmIdStore` to `additional.fields`.  
\- Mapped `principalType` to `additional.fields`.  
\- Mapped `clientTid` to `additional.fields`.  
\- Mapped `identitySourceId` to `additional.fields`.  
\- Mapped `stream` to `additional.fields`.  
\- Mapped `logtag` to `additional.fields`.  
\- Mapped `type` to `additional.fields`.  
\- Mapped `remoteAddr` to `additional.fields`.  
\- Mapped `remoteUser` to `additional.fields`.  
\- Mapped `requestTime` to `additional.fields`.  
\- Mapped `vhost` to `additional.fields`.  
\- Mapped `contentType` to `additional.fields`.  
\- Mapped `requestId` to `additional.fields`.  
\- Mapped `clientTxnId` to `additional.fields`.  
\- Mapped `txnId` to `additional.fields`.  
\- Mapped `issuerUrl` to `target.url`.  
\- Mapped `kubernetes.labels.app.kubernetes.io_component` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.app.kubernetes.io_instance` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.app.kubernetes.io_name` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.app.kubernetes.io_managed-by` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.app.kubernetes.io_part-of` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.app.kubernetes.io_version` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.helm.sh_chart` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.helmChartName` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.imageTag` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.labels.pod-template-hash` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.annotations.cni.projectcalico.org_podIP` to `target.resource.attribute.labels`.  
\- Mapped `kubernetes.annotations.cni.projectcalico.org_podIPs` to `target.resource.attribute.labels`.  
\- Mapped `reqLength` to `additional.fields`.  
\- Set `metadata.event_type` to `NETWORK_CONNECTION` when `has_principal` and `has_target` are true.   
2024-05-09 |  New:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
