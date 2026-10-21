---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-threat-changelog/
title: Change log for GCP_SECURITYCENTER_THREAT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:33:36.982029+00:00
---

# Change log for GCP_SECURITYCENTER_THREAT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-securitycenter-threat-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_SECURITYCENTER_THREAT

Date | Changes  
---|---  
2026-10-01 |  \- Enhanced the parser to map the `finding.sourceProperties.properties.vpcViolation.query` raw log field to the `security_result[0].description` UDM field for the `Exfiltration: BigQuery Data Exfiltration` category.   
2026-07-31 |  \- security_result.description: Newly mapped `sourceProperties.properties.vpcViolation.query` raw log field with `security_result.description` UDM field for event type `Exfiltration: BigQuery Data Exfiltration`.   
2025-12-05 |  \- target.resource.name: Newly mapped `database.displayName` raw log field with `target.resource.name` UDM field for event type `Privilege Escalation: AlloyDB Over-Privileged Grant`.  
\- target.process.command_line: Newly mapped `database.query` raw log field with `target.process.command_line` UDM field for event type `Privilege Escalation: AlloyDB Over-Privileged Grant`.  
\- additional.fields[database_userName]: Newly mapped `database.userName` raw log field with `additional.fields[database_userName]` UDM field for event type `Privilege Escalation: AlloyDB Over-Privileged Grant`.  
\- target.resource.attribute.labels[database_grantees]: Newly mapped `database.grantees` raw log field with `target.resource.attribute.labels[database_grantees]` UDM field for event type `Privilege Escalation: AlloyDB Over-Privileged Grant`.   
2025-12-04 |  Updated fields and events mappings by removing existing mappings and introducing more accurate ones.  
\- metadata.event_type: Removed mapping of `USER_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `SCAN_UNCATEGORIZED` instead for the `Discovery: Service Account Self-Investigation` event.  
\- metadata.event_type: Removed mapping of `SERVICE_MODIFICATION` from `metadata.event_type` UDM field and mapped `USER_RESOURCE_ACCESS` instead for the `Evasion: Access from Anonymizing Proxy` event.  
\- metadata.event_type: Removed mapping of `USER_RESOURCE_ACCESS` from `metadata.event_type` UDM field and mapped `USER_CHANGE_PERMISSIONS` instead for the `Exfiltration: CloudSQL Over-Privileged Grant` event.  
\- metadata.event_type: Removed mapping of `USER_CHANGE_PERMISSIONS` from `metadata.event_type` UDM field and mapped `SETTING_MODIFICATION` instead for the `Impair Defenses: Strong Authentication Disabled` event.  
\- metadata.event_type: Removed mapping of `USER_CHANGE_PERMISSIONS` from `metadata.event_type` UDM field and mapped `SETTING_MODIFICATION` instead for the `Impair Defenses: Two Step Verification Disabled` event.  
\- metadata.event_type: Removed mapping of `SETTING_MODIFICATION` from `metadata.event_type` UDM field and mapped `USER_UNCATEGORIZED` instead for the `Initial Access: Account Disabled Hijacked` event.  
\- metadata.event_type: Removed mapping of `SETTING_MODIFICATION` from `metadata.event_type` UDM field and mapped `USER_UNCATEGORIZED` instead for the `Initial Access: Disabled Password Leak` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_RESOURCE_ACCESS` instead for the `Persistence: New API MethodPreview` event.  
\- metadata.event_type: Removed mapping of `USER_RESOURCE_ACCESS` from `metadata.event_type` UDM field and mapped `PROCESS_LAUNCH` instead for the `Added Binary Executed` event.  
\- metadata.event_type: Removed mapping of `USER_RESOURCE_ACCESS` from `metadata.event_type` UDM field and mapped `NETWORK_CONNECTION` instead for the `Allowed Traffic Spike` event.  
\- metadata.event_type: Removed mapping of `USER_RESOURCE_UPDATE_CONTENT` from `metadata.event_type` UDM field and mapped `NETWORK_CONNECTION` instead for the `Increasing Deny Ratio` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `PROCESS_LAUNCH` instead for the `Malicious Script Executed` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_RESOURCE_ACCESS` instead for the `Initial Access: Dormant Service Account Action` event.  
\- metadata.event_type: Removed mapping of `USER_RESOURCE_ACCESS` from `metadata.event_type` UDM field and mapped `USER_RESOURCE_UPDATE_CONTENT` instead for the `Initial Access: Database Superuser Writes to User Tables` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_RESOURCE_ACCESS` instead for the `Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_RESOURCE_ACCESS` instead for the `Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access` event.  
\- metadata.event_type: Removed mapping of `USER_RESOURCE_ACCESS` from `metadata.event_type` UDM field and mapped `USER_CHANGE_PERMISSIONS` instead for the `Privilege Escalation: Dormant Service Account Granted Sensitive Role` event.  
\- metadata.event_type: Removed mapping of `USER_RESOURCE_UPDATE_CONTENT` from `metadata.event_type` UDM field and mapped `SCAN_UNCATEGORIZED` instead for the `Defense Evasion: Unexpected kernel code modification` event.  
\- metadata.event_type: Removed mapping of `USER_RESOURCE_UPDATE_CONTENT` from `metadata.event_type` UDM field and mapped `SCAN_UNCATEGORIZED` instead for the `Defense Evasion: Unexpected kernel read-only data modification` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `PROCESS_LAUNCH` instead for the `Execution: Added Malicious Binary Executed` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `PROCESS_LAUNCH` instead for the `Execution: Modified Malicious Binary Executed` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_RESOURCE_ACCESS` instead for the `Breakglass Account Used: break_glass_account` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `NETWORK_CONNECTION` instead for the `Configurable Bad Domain: APT29_Domains` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_CHANGE_PERMISSIONS` instead for the `Unexpected Role Grant: Forbidden roles` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `NETWORK_CONNECTION` instead for the `Configurable Bad IP` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `RESOURCE_CREATION` instead for the `Unexpected Compute Engine instance type` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `RESOURCE_CREATION` instead for the `Unexpected Compute Engine source image` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `RESOURCE_CREATION` instead for the `Unexpected Compute Engine region` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_CHANGE_PERMISSIONS` instead for the `Custom role with prohibited permission` event.  
\- metadata.event_type: Removed mapping of `SCAN_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_RESOURCE_ACCESS` instead for the `Unexpected Cloud API Call` event.  
\- target.resource.attribute.labels[kubernetes_nodes_name]: Mapped `kubernetes.nodes.name` raw log field with `target.resource.attribute.labels[kubernetes_nodes_name]` UDM field.  
\- target.resource_ancestors.name: Removed mapping of `kubernetes.nodes.name` from `target.resource_ancestors.name` UDM field.  
\- target.resource.attribute.labels[kubernetes_nodePools_name]: Mapped `kubernetes.nodePools.name` raw log field with `target.resource.attribute.labels[kubernetes_nodePools_name]` UDM field.  
\- target.resource_ancestors.name: Removed mapping of `kubernetes.nodePools.name` from `target.resource_ancestors.name` UDM field.  
\- target.resource.attribute.labels[kubernetes_nodePools_nodes_name]: Mapped `kubernetes.nodePools.nodes.name` raw log field with `target.resource.attribute.labels[kubernetes_nodePools_nodes_name]` UDM field.  
\- target.resource.attribute.labels[kubernetes_nodePools_nodes_name]: Removed mapping of `kubernetes.nodePools.nodes.name` from `target.resource.attribute.labels[kubernetes_nodePools_nodes_name]` UDM field.  
\- security_result.detection_fields[indicator_uri]: Mapped `indicator.uris` raw log field with `security_result.detection_fields[indicator_uri]` UDM field.  
\- about.url: Removed mapping of `indicator.uris` from `about.url` UDM field.  
\- additional.fields[sourceProperties_properties_scannerDomain]: Mapped `sourceProperties.properties.scannerDomain` raw log field with `additional.fields[sourceProperties_properties_scannerDomain]` UDM field.  
\- principal.labels[sourceProperties_properties_scannerDomain]: Removed mapping of `sourceProperties.properties.scannerDomain` from `principal.labels[sourceProperties_properties_scannerDomain]` UDM field.  
\- target.url: Mapped `sourceProperties.properties.extractionAttempt.jobLink, sourceProperties.properties.dataExfiltrationAttempt.jobLink` raw log field with `target.url` UDM field for event `Exfiltration: BigQuery Data Extraction` and `Exfiltration: BigQuery Data to Google Drive`.  
\- principal.process.file.full_path: Removed mapping of `sourceProperties.properties.extractionAttempt.jobLink, sourceProperties.properties.dataExfiltrationAttempt.jobLink` from `principal.process.file.full_path` UDM field for event `Exfiltration: BigQuery Data Extraction` and `Exfiltration: BigQuery Data to Google Drive`.  
\- additional.fields[properties_dataExfiltrationAttempt_job_jobId]: Mapped `sourceProperties.properties.dataExfiltrationAttempt.job.jobId, sourceProperties.properties.extractionAttempt.job.jobId` raw log field with `additional.fields[properties_dataExfiltrationAttempt_job_jobId]` UDM field for event `Exfiltration: BigQuery Data Extraction` and `Exfiltration: BigQuery Data to Google Drive`.  
\- principal.process.pid: Removed mapping of `sourceProperties.properties.dataExfiltrationAttempt.job.jobId, sourceProperties.properties.extractionAttempt.job.jobId` from `principal.process.pid` UDM field for event `Exfiltration: BigQuery Data Extraction` and `Exfiltration: BigQuery Data to Google Drive`.  
\- additional.fields[sourceProperties_properties_serviceAccountGetsOwnIamPolicy_callerUserAgent]: Mapped `sourceProperties.properties.serviceAccountGetsOwnIamPolicy.callerUserAgent` raw log field with `additional.fields[sourceProperties_properties_serviceAccountGetsOwnIamPolicy_callerUserAgent]` UDM field.  
\- principal.user.attribute.labels[sourceProperties_properties_serviceAccountGetsOwnIamPolicy_callerUserAgent]: Removed mapping of `sourceProperties.properties.serviceAccountGetsOwnIamPolicy.callerUserAgent` from `principal.user.attribute.labels[sourceProperties_properties_serviceAccountGetsOwnIamPolicy_callerUserAgent]` UDM field.  
\- security_result.threat_feed_name: Mapped `sourceProperties.properties.threatIntelligenceSource` raw log field with `security_result.threat_feed_name` UDM field.  
\- security_result.about.application: Removed mapping of `sourceProperties.properties.threatIntelligenceSource` from `security_result.about.application` UDM field.  
\- security_result.attack_details.tactics.name: Mapped `mitreAttack.additionalTactics` raw log field with `security_result.attack_details.tactics.name` UDM field.  
\- security_result.detection_fields[mitreAttack_additionalTactics]: Removed mapping of `mitreAttack.additionalTactics` from `security_result.detection_fields[mitreAttack_additionalTactics]` UDM field.  
\- security_result.attack_details.techniques.name: Mapped `mitreAttack.additionalTechniques` raw log field with `security_result.attack_details.techniques.name` UDM field.  
\- security_result.detection_fields[mitreAttack_additionalTechniques]: Removed mapping of `mitreAttack.additionalTechniques` from `security_result.detection_fields[mitreAttack_additionalTechniques]` UDM field.  
\- security_result.attack_details.tactics.name: Mapped `mitreAttack.primaryTactic` raw log field with `security_result.attack_details.tactics.name` UDM field.  
\- security_result.detection_fields[mitreAttack_primaryTactic]: Removed mapping of `mitreAttack.primaryTactic` from `security_result.detection_fields[mitreAttack_primaryTactic]` UDM field.  
\- security_result.attack_details.techniques.name: Mapped `mitreAttack.primaryTechniques.0` raw log field with `security_result.attack_details.techniques.name` UDM field.  
\- security_result.detection_fields[mitreAttack_primaryTechniques]: Removed mapping of `mitreAttack.primaryTechniques.0` from `security_result.detection_fields[mitreAttack_primaryTechniques]` UDM field.  
\- security_result.attack_details.version: Mapped `mitreAttack.version` raw log field with `security_result.attack_details.version` UDM field.  
\- security_result.detection_fields[mitreAttack_version]: Removed mapping of `mitreAttack.version` from `security_result.detection_fields[mitreAttack_version]` UDM field.  
\- security_result.detection_fields[sourceProperties_contextUris_mitreUri_url]: Mapped `sourceProperties.contextUris.mitreUri.url` raw log field with `security_result.detection_fields[sourceProperties_contextUris_mitreUri_url]` UDM field.  
\- security_result.detection_fields[sourceProperties.contextUris.mitreUri.url]: Removed mapping of `sourceProperties.contextUris.mitreUri.url` from `security_result.detection_fields[sourceProperties.contextUris.mitreUri.url]` UDM field.  
\- security_result.detection_fields[sourceProperties_contextUris_mitreUri_displayName]: Mapped `sourceProperties.contextUris.mitreUri.displayName` raw log field with `security_result.detection_fields[sourceProperties_contextUris_mitreUri_displayName]` UDM field.  
\- security_result.detection_fields[sourceProperties.contextUris.mitreUri.displayName]: Removed mapping of `sourceProperties.contextUris.mitreUri.displayName` from `security_result.detection_fields[sourceProperties.contextUris.mitreUri.url]` UDM field.  
\- security_result.detection_fields[sourceProperties_contextUris_relatedFindingUri_url]: Mapped `sourceProperties.contextUris.relatedFindingUri.url` raw log field with `security_result.detection_fields[sourceProperties_contextUris_relatedFindingUri_url]` UDM field.  
\- metadata.url_back_to_product: Removed mapping of `sourceProperties.contextUris.relatedFindingUri.url` from `metadata.url_back_to_product` UDM field.  
\- security_result.detection_fields[sourceProperties_contextUris_virustotalIndicatorQueryUri_url]: Mapped `sourceProperties.contextUris.virustotalIndicatorQueryUri.url` raw log field with `security_result.detection_fields[sourceProperties_contextUris_virustotalIndicatorQueryUri_url]` UDM field.  
\- security_result.detection_fields[sourceProperties.contextUris.virustotalIndicatorQueryUri.url]: Removed mapping of `sourceProperties.contextUris.virustotalIndicatorQueryUri.url` from `security_result.detection_fields[sourceProperties.contextUris.virustotalIndicatorQueryUri.url]` UDM field.  
\- security_result.detection_fields[sourceProperties_contextUris_virustotalIndicatorQueryUri_displayName]: Mapped `sourceProperties.contextUris.virustotalIndicatorQueryUri.displayName` raw log field with `security_result.detection_fields[sourceProperties_contextUris_virustotalIndicatorQueryUri_displayName]` UDM field.  
\- security_result.detection_fields[sourceProperties.contextUris.virustotalIndicatorQueryUri.displayName]: Removed mapping of `sourceProperties.contextUris.virustotalIndicatorQueryUri.url` from `security_result.detection_fields[sourceProperties.contextUris.virustotalIndicatorQueryUri.url]` UDM field.  
\- security_result.detection_fields[sourceProperties_contextUris_workspacesUri_url]: Mapped `sourceProperties.contextUris.workspacesUri.url` raw log field with `security_result.detection_fields[sourceProperties_contextUris_workspacesUri_url]` UDM field.  
\- security_result.detection_fields[sourceProperties.contextUris.workspacesUri.url]: Removed mapping of `sourceProperties.contextUris.workspacesUri.url` from `security_result.detection_fields[sourceProperties.contextUris.workspacesUri.url]` UDM field.  
\- security_result.detection_fields[sourceProperties_contextUris_workspacesUri_displayName]: Mapped `sourceProperties.contextUris.workspacesUri.displayName` raw log field with `security_result.detection_fields[sourceProperties_contextUris_workspacesUri_displayName]` UDM field.  
\- security_result.detection_fields[sourceProperties.contextUris.workspacesUri.displayName]: Removed mapping of `sourceProperties.contextUris.workspacesUri.displayName` from `security_result.detection_fields[sourceProperties.contextUris.workspacesUri.url]` UDM field.  
\- metadata.collected_timestamp: Mapped `createTime` raw log field with `metadata.collected_timestamp` UDM field.  
\- security_result.detection_fields[create_time]: Removed mapping of `createTime` from `security_result.detection_fields[create_time]` UDM field.  
\- target.process.command_line: Mapped `database.query` raw log field with `target.process.command_line` UDM field.  
\- src.process.command_line: Removed mapping of `database.query` from `src.process.command_line` UDM field.  
\- target.resource.attribute.labels[database_displayName]: Mapped `database.displayName` raw log field with `target.resource.attribute.labels[database_displayName]` UDM field.  
\- src.resource.attribute.labels[database_displayName]: Removed mapping of `database.displayName` from `src.resource.attribute.labels[database_displayName]` UDM field.  
\- target.resource.attribute.labels[database_grantees]: Mapped `database.grantees` raw log field with `target.resource.attribute.labels[database_grantees]` UDM field.  
\- src.resource.attribute.labels[database_grantees]: Removed mapping of `database.grantees` from `src.resource.attribute.labels[database_grantees]` UDM field.  
\- src.resource_ancestors.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_datasetId]: Mapped `sourceProperties.properties.extractionAttempt.sourceTable.datasetId` raw log field with `src.resource_ancestors.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_datasetId]` UDM field. for event `BigQuery Data Extraction`.  
\- src.resource.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_datasetId]: Removed mapping of `sourceProperties.properties.extractionAttempt.sourceTable.datasetId` from `src.resource.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_datasetId]` UDM field. for event `BigQuery Data Extraction`.  
\- src.resource_ancestors.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_projectId]: Mapped `sourceProperties.properties.extractionAttempt.sourceTable.projectId` raw log field with `src.resource_ancestors.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_projectId]` UDM field. for event `BigQuery Data Extraction`.  
\- src.resource.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_projectId]: Removed mapping of `sourceProperties.properties.extractionAttempt.sourceTable.projectId` from `src.resource.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_projectId]` UDM field. for event `BigQuery Data Extraction`.  
\- src.resource_ancestors.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_resourceUri]: Mapped `sourceProperties.properties.extractionAttempt.sourceTable.resourceUri` raw log field with `src.resource_ancestors.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_resourceUri]` UDM field. for event `BigQuery Data Extraction`.  
\- src.resource.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_resourceUri]: Removed mapping of `sourceProperties.properties.extractionAttempt.sourceTable.resourceUri` from `src.resource.attribute.labels[sourceProperties_properties_extractionAttempt_sourceTable_resourceUri]` UDM field. for event `BigQuery Data Extraction`.  
\- src.resource_ancestors.name: Mapped `sourceProperties.properties.extractionAttempt.sourceTable.tableId` raw log field with `src.resource_ancestors.name` UDM field. for event `BigQuery Data Extraction`.  
\- src.resource.product_object_id: Removed mapping of `sourceProperties.properties.extractionAttempt.sourceTable.tableId` from `src.resource.product_object_id` UDM field. for event `BigQuery Data Extraction`.  
\- additional.fields[sourceProperties_properties_restoreToExternalInstance_backupId]: Mapped `sourceProperties.properties.restoreToExternalInstance.backupId` raw log field with `additional.fields[sourceProperties_properties_restoreToExternalInstance_backupId]` UDM field.  
\- src.resource.attribute.labels[sourceProperties_properties_restoreToExternalInstance_backupId]: Removed mapping of `sourceProperties.properties.restoreToExternalInstance.backupId` from `src.resource.attribute.labels[sourceProperties_properties_restoreToExternalInstance_backupId]` UDM field.  
\- target.file.names: Mapped `sourceProperties.properties.extractionAttempt.destinations.objectName` raw log field with `target.file.names` UDM field.  
\- target.resource.attribute.labels[sourceProperties_properties_extractionAttempt_destinations_objectName]: Removed mapping of `sourceProperties.properties.extractionAttempt.destinations.objectName` from `target.resource.attribute.labels[sourceProperties_properties_extractionAttempt_destinations_objectName]` UDM field.  
\- principal.user.attribute.labels[sourceProperties_properties_anomalousLocation_notSeenInLast]: Mapped `sourceProperties.properties.anomalousLocation.notSeenInLast` raw log field with `principal.user.attribute.labels[sourceProperties_properties_anomalousLocation_notSeenInLast]` UDM field.  
\- target.user.attribute.labels[sourceProperties_properties_anomalousLocation_notSeenInLast]: Removed mapping of `sourceProperties.properties.anomalousLocation.notSeenInLast` from `target.user.attribute.labels[sourceProperties_properties_anomalousLocation_notSeenInLast]` UDM field.  
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
\- target.resource.name: Newly mapped `database.displayName` raw log field with `target.resource.name` UDM field.  
\- target.resource.attribute.labels[resource_name]: Newly mapped `resource_name` raw log field with target.resource.name UDM field.  
\- security_result.detection_fields[sourceProperties_contextUris_relatedFindingUri_displayName]: Newly mapped `sourceProperties.contextUris.relatedFindingUri.displayName` raw log field with `security_result.detection_fields[sourceProperties_contextUris_relatedFindingUri_displayName]` UDM field.   
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
2025-08-22 |  \- Updated the parser to handle validation for the `target.process.file.sha256` UDM field.   
2025-06-23 |  \- Updated the security_result.url_back_to_product UDM field base URL value from https://console.cloud.google.com to https://console.us.cloud.google.com for location `us`.  
\- Updated the security_result.url_back_to_product UDM field base URL value from https://console.cloud.google.com to https://console.eu.cloud.google.com for location `eu`.   
2025-04-09 |  \- Updated the security_result.url_back_to_product UDM field base URL value from https://console.cloud.google.com to https://console.sa.cloud.google.com for location `sa`.   
2025-04-07 |  \- `network.dns.questions.type` (New UDM field mapping) -> No UDM Mapping To Mapping of `sourceProperties.properties.dnsContexts.queryType` field from raw log.  
\- `network.dns.questions.name` (Removed Mapping Duplication) -> Previously, the UDM field `network.dns.questions.name` was mapped more than once to the raw log field `sourceProperties.properties.dnsContexts.queryName.` -> The duplication has been removed to ensure that the raw log field `sourceProperties.properties.dnsContexts.queryName` is mapped to the UDM field `network.dns.questions.name` only once.   
2025-02-07 |  \- Updated the mapping for `security_result.url_back_to_product` UDM field. Added the project ID value from the raw log field value `resource.projectDisplayName` to end of the URL mapped to `security_result.url_back_to_product` UDM field with the prefix `;?project=`.   
2024-12-26 |  Added support for raw log field `resource.resourcePathString`.   
2024-11-25 |  Mapped `access.callerIp` with `additional.fields` UDM field if the `access.callerIp` raw log field has value `gce-internal-ip`.   
2024-11-21 |  \- Added support for the v2 version of the SCC API, and the following fields are included as part of the update  
\- resource.gcpMetadata.project  
\- resource.gcpMetadata.projectDisplayName  
\- resource.gcpMetadata.parent  
\- resource.gcpMetadata.parentDisplayName  
\- resource.gcpMetadata.folders.resourceFolder  
\- resource.gcpMetadata.folders.resourceFolderDisplayName  
\- resource.gcpMetadata.organization   
2024-10-08 |  Mapped the `access.principalEmail` raw log field to `principal.user.userid` UDM field if there is a non-email value in the `access.principalEmail` raw log field.   
2024-08-13 |  Added mappings for the `finding.access.userAgent` raw log field.   
2024-04-24 |  \- Added support for mapping values to `principal.hostname` UDM field.   
2024-03-20 |  \- Added support for the following categories:  
\- `Configurable Bad IP`  
\- `Unexpected Compute Engine instance type`  
\- `Unexpected Compute Engine source image`  
\- `Unexpected Compute Engine region`  
\- `Custom role with prohibited permission`  
\- `Unexpected Cloud API Call`  
2024-02-28 |  \- Added support for additional findings.   
2024-02-14 |  1\. Added support for the following categories:  
\- Defense Evasion: Unexpected ftrace handler  
\- Defense Evasion: Unexpected interrupt handler  
\- Defense Evasion: Unexpected kernel code modification  
\- Defense Evasion: Unexpected kernel modules  
\- Defense Evasion: Unexpected kernel read-only data modification  
\- Defense Evasion: Unexpected kprobe handler   
2024-01-31 |  \- Added support for `Initial Access: Dormant Service Account Key Created`, `Unexpected Child Shell` and `Process Tree` categories.   
2024-01-03 |  \- Added logic to merge multiple `security_result` blocks into one.   
2023-12-13 |  \- Changed the mapping of `security_result.action` UDM field.   
2023-11-29 |  \- Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-08-23 |  Extracted `projectName` from the `resourceName` log field.   
2023-07-26 |  Updated mapping of the `canonicalName` log field.   
2023-07-09 |  Fixed principal_user_emailaddresses mapping.   
2023-06-28 |  Added support for category `account_has_leaked_credentials`.   
2023-06-14 |  1\. Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.  
2\. Added support for below mentioned categories:  
\- Defense Evasion: Unexpected ftrace handler  
\- Defense Evasion: Unexpected interrupt handler  
\- Defense Evasion: Unexpected kernel code modification  
\- Defense Evasion: Unexpected kernel modules  
\- Defense Evasion: Unexpected kernel read-only data modification  
\- Defense Evasion: Unexpected kprobe handler  
\- Defense Evasion: Unexpected processes in runqueue  
\- Defense Evasion: Unexpected system call handler  
\- Reverse Shell   
2023-05-31 |  Added support for category `Application DDoS Attack Attempt`.   
2023-05-17 |  1\. Added support for category `Initial Access: Excessive Permission Denied Actions`.  
2\. Handled UDM event type validation error.   
2023-05-02 |  Created a valid url for the `security_result.url_back_to_product` field.   
2023-05-01 |  Added additional mappings for deprecated labels.   
2023-04-12 |  Promoted GCP_SECURITYCENTER_THREAT parser to default.  
For the field mapping reference, see: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-security-command-center-findings#field-mapping.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
