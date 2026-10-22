---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-prisma-ca-changelog/
title: Change log for PAN_PRISMA_CA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:50.556867+00:00
---

# Change log for PAN_PRISMA_CA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-prisma-ca-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PAN_PRISMA_CA

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record.policy.labels` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-08-05 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page `https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-ca`.   
2026-05-29 |  Enhancement:  
\- Changed the keys for `aggregatedAlerts` arrays (accountIDs, clusters, collections, names) from index-based to static names in `target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `dropped` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-03-30 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alarmType`, `errorType` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.environment`: Removed mapping of `alarmType` from `event.idm.read_only_udm.principal.cloud.environment` UDM field because it is a deprecated UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.cloud.environment`: When `alarmType` contains `CLOUD`, set the value of `event.idm.read_only_udm.principal.asset.attribute.cloud.environment` to `GOOGLE_CLOUD_PLATFORM`.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `USER_UNCATEGORIZED` to `event.idm.read_only_udm.metadata.event_type` when log contains principal and user data.   
2026-03-06 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.severity`:  
\- If severity is `ERROR` or `CRITICAL`, updated the value of `event.idm.read_only_udm.security_result.severity` to `CRITICAL`.  
\- If severity is `LOW` or `MINOR`, updated the value of `event.idm.read_only_udm.security_result.severity` to `LOW`.  
\- If severity is `WARNING` or `MEDIUM`, updated the value of `event.idm.read_only_udm.security_result.severity` to `MEDIUM`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record.resource.data.document.Version` (key: `Version`), all key-value pairs from the `record.resource.data.document.Statement` array (with keys generated in the format `Statement_KEY_INDEX`), and all key-value pairs from the `record.resource.data.entities.policyRoles` array (with keys generated in the format `policyRole_KEY_INDEX`) to the `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `isPermissionBoundarySet` (key: `isPermissionBoundarySet`), `isDefaultVersion` (key: `isDefaultVersion`), `isAttached` (key: `isAttached`) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-28 |  Enhancement:  
\- Enhanced `severity` parsing logic to handle `LOW` severity as well.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.hasFinding`, `record.additionalInfo.saveSearchId` and `record.policyId` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `record.resourceType`, `record.resource.resourceType` raw log fields to `event.idm.read_only_udm.principal.resource.resource_subtype`.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `record.resource.account` raw log field to `event.idm.read_only_udm.target.resource.product_object_id`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record.resource.data.tags` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `record.tags`, `record.resource.data.secretVersionsToStages.terraform-20260122172341570100000002` raw log fields to `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- `event.idm.read_only_udm.target.cloud.project.id`: Newly mapped `record.accountId`, `record.resource.accountId` raw log fields to `event.idm.read_only_udm.target.cloud.project.id`.   
2025-09-05 |  Enhancement:  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields, event.idm.read_only_udm.security_result.detection_fields.   
2025-09-02 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `record.time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `record.hostname` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `record.hostname` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `record.fqdn` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `record.fqdn` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `record.containerName` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `record.containerName` raw log field to `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `record.containerID` raw log field to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `record.imageName`, `record.imageID`, `record.cluster` raw log fields to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `record.namespace` raw log field to `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `record.accountID`, `record.provider` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `record.region` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `audit.os` raw log field to `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `audit.user` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `audit.type` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `audit.effect` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `audit.msg` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `audit.pid` raw log field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `audit.processPath` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `audit.command` raw log field to `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `audit.attackType` raw log field to `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `audit.severity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `audit.attackTechniques`, `audit._id`, `audit.count`, `audit.container`, `record._id`, `record.serialNum`, `record.collections`, `record.profileID` and `record.shouldCollect` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `audit.ruleName` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.acknowledged` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `record.category` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped `record.type` raw log field to `event.idm.read_only_udm.principal.resource.type` UDM field.   
2025-01-22 |  Enhancement:  
\- Added a `gsub` to support new pattern of JSON logs.  
\- Mapped `emailValue` to `principal.user.email_addresses`.   
2024-12-19 |  Enhancement:  
\- Mapped `account_id` to `target.user.userid`.   
2024-12-14 |  Enhancement:  
\- Added support for unparsed `aggregatedAlerts` fields.   
2024-12-05 |  Enhancement:  
\- Mapped `record.region` to `principal.location.country_or_region`.  
\- Mapped `record.policy.name` to `security_result.description`.  
\- Mapped `record.account.cloudType` to `principal.cloud.environment`.  
\- Mapped `record.policy.policyType`, `record.policy.recommendation`, and `record.policy.description` to `security_result.detection_fields`.  
\- Mapped `record.policy.severity` to `security_result.severity`.  
\- Mapped `record.policy.labels` to `additional.fields`.   
2024-11-27 |  Enhancement:  
\- Refreshed parser to have multi-valued arrayed entries altered to access commonly used fields without duplication within the array index.   
2024-11-14 |  Enhancement:  
\- Added support for a new pattern of JSON logs.  
\- Mapped `callbackUrl` to `metadata.url_back_to_product`.  
\- Mapped `errorMessage` to `metadata.description`.  
\- Mapped `notificationRuleName` to `security_result.rule_name`.  
\- Mapped `body`, `title` to `additional.fields`.  
\- Mapped `alarmType` to `principal.cloud.environment`.  
\- Mapped `severity` to `security_result.severity`.   
2024-10-31 |  Enhancement:  
\- Mapped all instances of `aggregatedAlert.compilanceIssues` to different `security_result` blocks.   
2024-10-17 |  Enhancement:  
\- Mapped `aggregatedAlert.vulnerabilities.imageID` to `extensions.vulns.vulnerabilities.about.file.sha256`.  
\- Mapped `aggregatedAlert.vulnerabilities.imageName` to `extensions.vulns.vulnerabilities.about.file.path`.  
\- Mapped `aggregatedAlert.vulnerabilities.distribution` to `extensions.vulns.vulnerabilities.name`.  
\- Mapped `aggregatedAlert.vulnerabilities.newVulnerabilities.severity` to `extensions.vulns.vulnerabilities.severity`.  
\- Mapped `aggregatedAlert.vulnerabilities.newVulnerabilities.cve` to `extensions.vulns.vulnerabilities.cve_id`  
\- Mapped `aggregatedAlert.vulnerabilities.newVulnerabilities.link` to `extensions.vulns.vulnerabilities.about.url`.  
\- Mapped `aggregatedAlert.vulnerabilities.newVulnerabilities.status` to `extensions.vulns.vulnerabilities.description`.  
\- Mapped `aggregatedAlert.vulnerabilities.newVulnerabilities.packages`, `aggregatedAlert.vulnerabilities.newVulnerabilities.packageVersion`, and `aggregatedAlert.vulnerabilities.newVulnerabilities.sourcePackage` to `target.resource.attribute.labels`.   
2024-09-15 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-06-21 |  Enhancement:  
\- Added support for a new pattern of unparsed JSON logs.   
2024-06-18 |  Enhancement:  
\- Mapped `policyLabels` to `additional.fields`.  
\- Mapped `policyType` to `security_result.detection_fields`.   
2024-06-17 |  Enhancement:  
\- Mapped `resource.unifiedAssetId` to `principal.asset.asset_id`.  
\- Mapped `policyName` to `security_result.description`.  
\- Mapped `resource.resourceConfigJsonAvailable`, `resource.resourceDetailsAvailable`, and `policy.deleted` to `additional.fields`.  
\- Mapped `policy.recommendation`, `policy.policyType`, and `policy.description` to `security_result.detection_fields`.  
\- Mapped `resource.url` to `principal.url`.  
\- Mapped `reason` to `security_result.summary`.  
\- Mapped `resource.region` to `principal.location.state`.  
\- Mapped `resource.regionId` to `principal.location.country_or_region`.  
\- Mapped `resource.resourceType` to `target.resource.resource_subtype`.  
\- Mapped `resource.accountId` to `target.resource.product_object_id` and `target.resource.id`.  
\- Mapped `resource.url` to `principal.url`.'  
\- Mapped `reason` to `security_result.summary`.  
\- If `resource.cloudType` value is `gcp`, set `principal.cloud.environment` to `GOOGLE_CLOUD_PLATFORM`.   
2023-12-10 |  Enhancement:  
\- Added a Grok pattern to extract JSON part.  
\- Mapped `resourceId` to `principal.resource.product_object_id`.  
\- Mapped `accountId` to `target.resource.product_object_id`.  
\- Mapped `alertRuleName` to `security_result.rule_name`.  
\- Mapped `accountName` to `target.resource.name`.  
\- Mapped `hasFinding` to `security_result.detection_fields`.  
\- Mapped `resourceRegionId` to `principal.cloud.availability_zone`.  
\- Mapped `source` to `principal.application`.  
\- Mapped `callbackUrl` to `metadata.url_back_to_product`.  
\- Mapped `alertRuleId` to `security_result.rule_id`.  
\- Mapped `alertId` to `security_result.detection_fields`.  
\- Mapped `policyLabels` to `additional.fields`.  
\- Mapped `policyName` to `security_result.description`.  
\- Mapped `resourceName` to `principal.resource.name`.  
\- Mapped `resourceRegion` to `principal.location.country_or_region`.  
\- Mapped `policyDescription` to `security_result.detection_fields`.  
\- Mapped `policyRecommendation` to `security_result.detection_fields`.  
\- Mapped `resourceCloudService` to `principal.resource.attribute.labels`.  
\- Mapped `resource.url` to `principal.url`.  
\- Mapped `alertTs` to `security_result.detection_fields`.  
\- Mapped `firstSeen` to `principal.asset.first_seen_time`.  
\- Mapped `lastSeen` to `principal.asset.last_discover_time`.  
\- Mapped `reason` to `security_result.summary`.  
\- Mapped `alertStatus` to `security_result.detection_fields`.  
\- If `severity` value is `HIGH`, set `security_result.severity` to `HIGH`.  
\- If `cloudType` value is `gcp`, set `principal.cloud.environment` to `GOOGLE_CLOUD_PLATFORM`.   
2023-08-17 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
