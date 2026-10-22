---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-misconfiguration-changelog/
title: Change log for GCP_SECURITYCENTER_MISCONFIGURATION \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:50.542822+00:00
---

# Change log for GCP_SECURITYCENTER_MISCONFIGURATION  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-misconfiguration-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_SECURITYCENTER_MISCONFIGURATION

Date | Changes  
---|---  
2025-12-04 |  Updated fields and events mappings by removing existing mappings and introducing more accurate ones.  
\- security_result.detection_fields[compliances_id]: Mapped `compliances.ids` raw log field with `security_result.detection_fields[compliances_id]` UDM field.  
\- about.labels[compliance_ids]: Removed mapping of `compliances.ids` from `about.labels[compliance_ids]` UDM field.  
\- security_result.detection_fields[compliances_version]: Mapped `compliances.version` raw log field with `security_result.detection_fields[compliances_version]` UDM field.  
\- about.labels[compliance_version]: Removed mapping of `compliances.version` from `about.labels[compliance_version]` UDM field.  
\- security_result.detection_fields[compliances_standard]: Mapped `compliances.standard` raw log field with `security_result.detection_fields[compliances_standard]` UDM field.  
\- about.labels[compliances_standard]: Removed mapping of `compliances.standard` from `about.labels[compliances_standard]` UDM field.  
\- target.resource.attribute.labels[kubernetes_pods_ns]: Mapped `kubernetes.pods.ns` raw log field with `target.resource.attribute.labels[kubernetes_pods_ns]` UDM field.  
\- target.resource_ancestors.attribute.labels[kubernetes_pods_ns]: Removed mapping of `kubernetes.pods.ns` from `target.resource_ancestors.attribute.labels[kubernetes_pods_ns]` UDM field.  
\- target.resource.attribute.labels[kubernetes_pods_name]: Mapped `kubernetes.pods.name` raw log field with `target.resource.attribute.labels[kubernetes_pods_name]` UDM field.  
\- target.resource_ancestors.name: Removed mapping of `kubernetes.pods.name` from `target.resource_ancestors.name` UDM field.  
\- additional.fields[externalSystems_assignees]: Mapped `externalSystems.assignees` raw log field with `additional.fields[externalSystems_assignees]` UDM field.  
\- about.resource.attribute.labels[externalSystems_assignees]: Removed mapping of `externalSystems.assignees` from `about.resource.attribute.labels[externalSystems_assignees]` UDM field.  
\- target.resource.attribute.labels[kubernetes_pods_containers_uri]: Mapped `kubernetes.pods.containers.uri` raw log field with `target.resource.attribute.labels[kubernetes_pods_containers_uri]` UDM field.  
\- target.resource_ancestors.attribute.labels[kubernetes_pods_containers_uri]: Removed mapping of `kubernetes.pods.containers.uri` from `target.resource_ancestors.attribute.labels[kubernetes_pods_containers_uri]` UDM field.  
\- target.resource.attribute.labels[kubernetes.pods.containers.labels]: Mapped `kubernetes.pods.containers.labels` raw log field with `target.resource.attribute.labels[kubernetes.pods.containers.labels]` UDM field.  
\- target.resource_ancestors.attribute.labels[kubernetes.pods.containers.labels]: Removed mapping of `kubernetes.pods.containers.labels` from `target.resource_ancestors.attribute.labels[kubernetes.pods.containers.labels]` UDM field.  
\- target.resource.attribute.labels[resource_projectName]: Mapped `resource.projectName` raw log field with `target.resource.attribute.labels[resource_projectName]` UDM field for events `Exfiltration: BigQuery Data Extraction`,`Exfiltration: BigQuery Data to Google Drive`,`Exfiltration: BigQuery Data Exfiltration`,`Exfiltration: CloudSQL Restore Backup to External Organization`.  
\- principal.resource.name: Removed mapping of `resource.projectName` from `principal.resource.name` UDM field for events `Exfiltration: BigQuery Data Extraction`,`Exfiltration: BigQuery Data to Google Drive`,`Exfiltration: BigQuery Data Exfiltration`,`Exfiltration: CloudSQL Restore Backup to External Organization`.  
\- target.resource.attribute.labels[resource_gcpMetadata_project]: Mapped `resource.gcpMetadata.project` raw log field with `target.resource.attribute.labels[resource_gcpMetadata_project]` UDM field.  
\- principal.resource.name: Removed mapping of `resource.gcpMetadata.project` from `principal.resource.name` UDM field.  
\- additional.fields[database_userName]: Mapped `database.userName` raw log field with `additional.fields[database_userName]` UDM field for event `Exfiltration: CloudSQL Over-Privileged Grant`.  
\- principal.user.userid: Removed mapping of `database.userName` from `principal.user.userid` UDM field for event `Exfiltration: CloudSQL Over-Privileged Grant`.  
\- target.resource.attribute.labels[kubernetes_pods_containers_name]: Mapped `kubernetes.pods.containers.name` raw log field with `target.resource.attribute.labels[kubernetes_pods_containers_name]` UDM field.  
\- target.resource_ancestors.attribute.labels[kubernetes_pods_containers_name]: Removed mapping of `kubernetes.pods.containers.name` from `target.resource_ancestors.attribute.labels[kubernetes_pods_containers_name]` UDM field.  
\- target.resource.attribute.labels[kubernetes_pods_containers_createTime]: Mapped `kubernetes.pods.containers.createTime` raw log field with `target.resource.attribute.labels[kubernetes_pods_containers_createTime]` UDM field.  
\- target.resource_ancestors.attribute.labels[kubernetes_pods_containers_createTime]: Removed mapping of `kubernetes.pods.containers.createTime` from `target.resource_ancestors.attribute.labels[kubernetes_pods_containers_createTime]` UDM field.  
\- target.resource.attribute.labels[kubernetes_pods_containers_imageId]: Mapped `kubernetes.pods.containers.imageId` raw log field with `target.resource.attribute.labels[kubernetes_pods_containers_imageId]` UDM field.  
\- target.resource_ancestors.attribute.labels[kubernetes_pods_containers_imageId]: Removed mapping of `kubernetes.pods.containers.imageId` from `target.resource_ancestors.attribute.labels[kubernetes_pods_containers_imageId]` UDM field.  
\- target.resource_ancestors.name: Mapped `resource.parent` raw log field with `target.resource_ancestors.name` UDM field.  
\- target.resource.attribute.labels[resource_parent]: Removed mapping of `resource.parent` from `target.resource.attribute.labels[resource_parent]` UDM field.  
\- target.resource.attribute.labels[resource_name]: Newly mapped `resource_name` raw log field with target.resource.name UDM field.   
2025-11-07 |  Updated fields and events mappings by removing existing mappings and introducing more accurate ones.  
\- metadata.event_type: Removed mapping of `SCAN_HOST` from `metadata.event_type` UDM field and mapped `SCAN_UNCATEGORIZED` instead for the `PUBLIC_COMPUTE_IMAGE` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `SCAN_HOST` instead for the `PUBLIC_IP_ADDRESS` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `SCAN_HOST` instead for the `SHIELDED_VM_DISABLED` event.  
\- metadata.event_type: Removed mapping of `SCAN_NETWORK` from `metadata.event_type` UDM field and mapped `SCAN_HOST` instead for the `COMPUTE_SERIAL_PORTS_ENABLED` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `SCAN_HOST` instead for the `IP_FORWARDING_ENABLED` event.  
\- metadata.event_type: Removed mapping of `SCAN_NETWORK` from `metadata.event_type` UDM field and mapped `SCAN_UNCATEGORIZED` instead for the `FIREWALL_RULE_LOGGING_DISABLED` event.  
\- metadata.event_type: Removed mapping of `SCAN_NETWORK` from `metadata.event_type` UDM field and mapped `SCAN_UNCATEGORIZED` instead for the `OWNER_NOT_MONITORED` event.  
\- metadata.event_type: Removed mapping of `SCAN_NETWORK` from `metadata.event_type` UDM field and mapped `SCAN_HOST` instead for the `PUBLIC_SQL_INSTANCE` event.  
\- metadata.event_type: Removed mapping of `SCAN_NETWORK` from `metadata.event_type` UDM field and mapped `SCAN_HOST` instead for the `SQL_PUBLIC_IP` event.  
\- metadata.event_type: Removed mapping of `SCAN_NETWORK` from `metadata.event_type` UDM field and mapped `SCAN_UNCATEGORIZED` instead for the `FLOW_LOGS_DISABLED` event.  
\- security_result.detection_fields: Removed mapping of `sourceProperties.Recommendation` from `security_result.detection_fields` UDM field.  
\- security_result.outcomes: Mapped `sourceProperties.Recommendation` raw log field with `security_result.outcomes` UDM field.  
\- security_result.detection_fields: Removed mapping of `sourceProperties.ExceptionInstructions` from `security_result.detection_fields` UDM field.  
\- security_result.outcomes: Mapped `sourceProperties.ExceptionInstructions` raw log field with `security_result.outcomes` UDM field.  
\- security_result.detection_fields: Removed mapping of `sourceProperties.Explanation` from `security_result.detection_fields` UDM field.  
\- security_result.outcomes: Mapped `sourceProperties.Explanation` raw log field with `security_result.outcomes` UDM field.  
\- security_result.detection_fields: Removed mapping of `sourceProperties.debug` from `security_result.detection_fields` UDM field.  
\- additional.fields: Mapped `sourceProperties.debug` raw log field with `additional.fields` UDM field.  
\- security_result.detection_fields: Removed mapping of `sourceProperties.debug2` from `security_result.detection_fields` UDM field.  
\- additional.fields: Mapped `sourceProperties.debug2` raw log field with `additional.fields` UDM field.   
2025-09-30 |  \- target.file.full_path: Newly mapped `finding.file.path` raw log field with `target.file.full_path` UDM field for the first file object entry.  
\- about.file.full_path: Newly mapped `finding.file.path` raw log field with `about.file.full_path` UDM field for all file entries except the first one.  
\- target.file.size: Newly mapped `finding.file.size` raw log field with `target.file.size` UDM field for file for the first file object entry.  
\- about.file.size: Newly mapped `finding.file.size` raw log field with `about.file.size` UDM field for all file entries except the first one.  
\- target.file.sha256: Newly mapped `finding.file.sha256` raw log field with `target.file.sha256` UDM field for the first file object entry.  
\- about.file.sha256: Newly mapped `finding.file.sha256` raw log field with `about.file.sha256` UDM field for all file entries except the first one.  
\- additional.fields : Newly mapped `finding.file.hashedSize` raw log field with `additional.fields` UDM field.  
\- additional.fields : Newly mapped `finding.file.partiallyHashed` raw log field with `additional.fields` UDM field.  
\- additional.fields : Newly mapped `finding.file.contents` raw log field with `additional.fields` UDM field.  
\- additional.fields : Newly mapped `finding.file.diskPath.partitionUuid` raw log field with `additional.fields` UDM field.  
\- additional.fields : Newly mapped `finding.file.diskPath.relativePath` raw log field with `additional.fields` UDM field.  
\- additional.fields : Newly mapped `finding.file.operations.type` raw log field with `additional.fields` UDM field.   
2025-06-23 |  \- Updated the security_result.url_back_to_product UDM field base URL value from https://console.cloud.google.com to https://console.us.cloud.google.com for location `us`.  
\- Updated the security_result.url_back_to_product UDM field base URL value from https://console.cloud.google.com to https://console.eu.cloud.google.com for location `eu`.   
2025-04-09 |  \- Updated the security_result.url_back_to_product UDM field base URL value from https://console.cloud.google.com to https://console.sa.cloud.google.com for location `sa`.   
2025-02-07 |  \- Updated the mapping for `security_result.url_back_to_product` UDM field. Added the project ID value from the raw log field value `resource.projectDisplayName` to end of the URL mapped to `security_result.url_back_to_product` UDM field with the prefix `;?project=`.   
2024-11-21 |  \- Added support for the v2 version of the SCC API, and the following fields are included as part of the update  
\- resource.gcpMetadata.project  
\- resource.gcpMetadata.projectDisplayName  
\- resource.gcpMetadata.parent  
\- resource.gcpMetadata.parentDisplayName  
\- resource.gcpMetadata.folders.resourceFolder  
\- resource.gcpMetadata.folders.resourceFolderDisplayName  
\- resource.gcpMetadata.organization   
2024-04-03 |  \- Added support for `GKE_PRIVILEGE_ESCALATION`, `GKE_RUN_AS_NONROOT`,`GKE_HOST_PATH_VOLUMES`,`GKE_HOST_NAMESPACES`,`GKE_PRIVILEGED_CONTAINERS`,`GKE_HOST_PORTS`,`GKE_CAPABILITIES` category.   
2024-02-28 |  \- Added support for `INSTANCE_OS_LOGIN_DISABLED` category.   
2024-02-14 |  \- Added support for `DNSSEC_DISABLED` category.   
2024-01-03 |  \- Added support for two categories, LEGACY_NETWORK and LOAD_BALANCER_LOGGING_DISABLED.   
2023-11-29 |  \- Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-05-02 |  1\. Created valid url for security_result.url_back_to_product UDM field  
2\. Added support for new custom category: kms_key_region_europe and kms_non_euro_region   
2023-05-01 |  Added additional mappings for deprecated labels.   
2023-04-12 |  Promoted GCP_SECURITYCENTER_MISCONFIGURATION parser to default.  
For the field mapping reference, see GCP_SECURITYCENTER https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-security-command-center-findings#field-mapping.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
