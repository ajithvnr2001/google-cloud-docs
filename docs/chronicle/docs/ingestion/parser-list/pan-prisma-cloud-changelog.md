---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-prisma-cloud-changelog/
title: Change log for PAN_PRISMA_CLOUD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:50.166851+00:00
---

# Change log for PAN_PRISMA_CLOUD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-prisma-cloud-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PAN_PRISMA_CLOUD

Date | Changes  
---|---  
2024-11-18 |  Enhancement:  
\- Mapped `id` to `metadata.product_log_id`.   
2024-03-28 |  Enhancement:  
\- When `ipAddress` is not a valid IP address, then mapped `ipAddress` to `additional.fields`.  
\- When `user` is a valid email address, then mapped `user` to `target.user.email_addresses`.  
\- When `user` is not a valid email address, then mapped `user` to `target.user.userid`.  
\- Mapped `policy_id` and `resource_name` fields in `action` field to `target.resource.attribute.labels`.   
2024-02-21 |  Enhancement:  
\- Added `on_error` check for `date` block.  
\- Mapped `alertRules` to `sec_result.detection_fields`.  
\- Mapped `policy.policyId` to `sec_result.rule_id`.  
\- Mapped `policy.policyType` to `sec_result.rule_type`.  
\- Mapped `policy.severity` to `sec_result.severity`.  
\- Mapped `policy.recommendation` to `metadata.description`.  
\- Mapped `resource.data.architecture` to `principal.asset.hardware.cpu_platform`.  
\- Mapped `resource.name` to `target.resource.name`.  
\- Mapped `resource.accountId` to `target.resource.product_object_id`.  
\- Mapped `resource.regionId` to `target.location.country_or_region`.  
\- Mapped `resource.cloudServiceName` to `target.resource.attribute.labels`.  
\- Mapped `resource.resourceApiName` to `target.resource.attribute.labels`.  
\- Mapped `alertrule.createdBy` to `principal.user.email_addresses`.  
\- Mapped `resource.unifiedAssetId` to `principal.asset.asset_id`.  
\- Mapped `resource.data.selfLink` to `about.url`.  
\- Mapped `resource.data.sourceImage` to `principal.resource.attribute.labels`.  
\- Mapped `resource.data.sizeGb` to `principal.resource.attribute.labels`.  
\- Mapped `resource.data.physicalBlockSizeBytes` to `principal.resource.attribute.labels`.  
\- Mapped `resource.data.labelFingerprint` to `sec_result.detection_fields`.  
\- When `reason` is `NEW_ALERT`, set `metadata.event_type` to `USER_RESOURCE_CREATION`.   
2024-02-13 |  Enhancement:  
\- Added support for new customer logs.   
2022-08-09 |  Enhancement:  
\- Added conditional conversion check for field `timestamp`.  
\- Added following mapping when value of the field `resourceType` is `Login`:  
\- The field `ipAddress` is mapped to `principal.ip`.  
\- The field `user` is mapped to `target.user.email_addresses`.  
\- The field `result` is mapped to `security_result.action_details`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
