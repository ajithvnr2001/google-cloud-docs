---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-inspector-changelog/
title: Change log for AWS_INSPECTOR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:10:14.968766+00:00
---

# Change log for AWS_INSPECTOR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-inspector-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_INSPECTOR

Date | Changes  
---|---  
2026-08-21 |  \- `event.idm.read_only_udm.additional.fields`: Removed mapping of `type` from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `vulnerablePackages.arch`, `vulnerablePackages.epoch`, `vulnerablePackages.name`, `vulnerablePackages.sourceLayerHash`, `vulnerablePackages.version`, `resources.id`, `resources.partition`, `resources.provider`, `resources.region`, `resources.type`, `resources.details.awsEcrContainerImage.architecture`, `resources.details.awsEcrContainerImage.platform`, `resources.details.awsEcrContainerImage.registry`, `resources.details.awsEcrContainerImage.repositoryName`, `resource.details.awsEcrContainerImage.pushedAt`, `resource.details.awsEcrContainerImage.lastInUseAt`, `resource.details.awsEcrContainerImage.inUseCount` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `exploitAvailable`, `fixAvailable`, `epss.score`, `packageVulnerabilityDetails.cvss`, `inspectorScoreDetails.adjustedCvss.cvssSource`, `inspectorScoreDetails.adjustedCvss.scoreSource`, `vulnerablePackages.fixedInVersion`, `vulnerablePackages.packageManager`, `vulnerablePackages.release`, `vulnerablePackages.remediation` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `packageVulnerabilityDetails.referenceUrls` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.product_object_id`: Newly mapped `awsAccountId` raw log field with `event.idm.read_only_udm.target.resource_ancestors.product_object_id` UDM field  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `findingArn` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.first_found`: Newly mapped `firstObservedAt` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.first_found` UDM field  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `inspectorScore` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.last_found`: Newly mapped `lastObservedAt` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.last_found` UDM field  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `updatedAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cvss_base_score`: Newly mapped `inspectorScoreDetails.adjustedCvss.score` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cvss_base_score` UDM field  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cvss_vector`: Newly mapped `inspectorScoreDetails.adjustedCvss.scoringVector` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cvss_vector` UDM field  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cvss_version`: Newly mapped `inspectorScoreDetails.adjustedCvss.version` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cvss_version` UDM field  
\- `event.idm.read_only_udm.security_result.threat_feed_name`: Newly mapped `packageVulnerabilityDetails.source` raw log field with `event.idm.read_only_udm.security_result.threat_feed_name` UDM field  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cve_id`: Newly mapped `packageVulnerabilityDetails.vulnerabilityId` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.cve_id` UDM field  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `remediation.recommendation.text` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `resources.details.awsEcrContainerImage.imageTags` raw log field with `event.idm.read_only_udm.target.file.names` UDM field  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resources.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: If `index` is 0, Set the value of `event.idm.read_only_udm.security_result.url_back_to_product` to `refurl`.  
\- `event.idm.read_only_udm.target.location.name`: If `index` is 0, Set the value of `event.idm.read_only_udm.target.location.name` to `resources.region`.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: If `index` is 0, Set the value of `event.idm.read_only_udm.target.resource.resource_subtype` to `resources.type`.  
\- `event.idm.read_only_udm.target.asset.platform_software.platform_version`: If `index` is 0, Set the value of `event.idm.read_only_udm.target.asset.platform_software.platform_version` to `resources.details.awsEcrContainerImage.platform`.  
\- Added a grok pattern on `resource_id` to extract `resource_sha256_val`  
\- `event.idm.read_only_udm.target.file.sha256`: If `resource_sha256_val` is valid hash, Set the value of `event.idm.read_only_udm.target.file.sha256` to `resource_sha256_val`.  
\- `event.idm.read_only_udm.target.process.file.sha256`: If `vulnerablePackages_sourceLayerHash` is valid hash and `index` is 0, Set the value of `event.idm.read_only_udm.target.process.file.sha256` to `vulnerablePackages_sourceLayerHash`.  
\- `event.idm.read_only_udm.security_result.threat_status`: If `status` is ACTIVE, Set the value of `event.idm.read_only_udm.security_result.threat_status` to ACTIVE.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `packageVulnerabilityDetails.vendorSeverity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.   
2025-02-25 |  \- Added support to parse the unparsed logs.   
2025-02-04 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
