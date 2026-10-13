---
url: https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview/
title: Overview of Event Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:10.069457+00:00
---

# Overview of Event Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of Event Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

## What is Event Threat Detection?

Event Threat Detection is a built-in service for the Security Command Center Premium tier that continuously monitors your organization or projects and identifies threats within your systems in near-real time. Event Threat Detection is regularly updated with new detectors to identify emerging threats at cloud scale.

## How Event Threat Detection works

Event Threat Detection monitors the [Cloud Logging](https://docs.cloud.google.com/logging/docs/basic-concepts) stream for your organization or projects. If you activate Security Command Center Premium tier at the organization level, Event Threat Detection consumes logs for your projects as they are created and Event Threat Detection can monitor [Google Workspace Logs](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging). Cloud Logging contains log entries of API calls and other actions that create, read, or modify the configuration or metadata of your resources. Google Workspace logs track user sign-ins to your domain and provide a record of actions performed on your Google Workspace Admin Console.

Log entries contain status and event information that Event Threat Detection uses to quickly detect threats. Event Threat Detection applies detection logic and proprietary threat intelligence methods, such as identifying indicators of compromise (IoC), profiling over a sliding window of time, machine learning, and anomaly detection, to identify threats in near-real time.

When Event Threat Detection detects a threat, it writes a finding to Security Command Center. If you activate Security Command Center Premium tier at the organization level, Security Command Center can write findings to a Cloud Logging project. From Cloud Logging and Google Workspace logging, you can export findings to other systems with Pub/Sub and process them with Cloud Run functions.

If you activate Security Command Center Premium tier at the organization level, you can additionally use [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/overview) to investigate some findings. Google SecOps is a Google Cloud service that lets you investigate threats and pivot through related entities in a unified timeline. For instructions on sending findings to Google SecOps, see [Investigate findings in Google SecOps](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection#investigate_findings).

Your ability to view and edit findings and logs is determined by the Identity and Access Management (IAM) roles you are granted. For more information on Security Command Center IAM roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

### Sensitive data enrichment

Event Threat Detection is integrated with Sensitive Data Protection to enrich sensitive resource findings. If you have enabled Sensitive Data Protection discovery scans and configured them to [send results to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc), Event Threat Detection can use the sensitivity metadata of your BigQuery and Cloud Storage resources to adjust findings:

  * **Category changes** : If a resource is identified by Sensitive Data Protection as having high or moderate sensitivity, the finding category is updated to a specific category that indicates the resource is sensitive. For example, if a leaked service account key is used to access a sensitive bucket, the finding category changes from `Initial Access: Leaked Service Account Key Used` to `Initial Access: Leaked Service Account Key Affecting Sensitive Data`.
  * **Severity upgrades** : If the default severity of the finding is less than **High** (that is, **Low** or **Medium**), the severity is upgraded by one level (for example, from **Medium** to **High**).



For a list of rules that support sensitive data enrichment, see Event Threat Detection default rules.

## Event Threat Detection rules

Rules define the type of threats that Event Threat Detection detects and the types of logs that must be enabled for detectors to work. **Admin Activity** audit logs are always written; you can't configure or disable them.

Event Threat Detection includes the following default rules:

Active ScanBrute forceCommand and ControlCredential AccessData DestructionDefense EvasionDenial of ServiceDiscoveryExfiltrationImpactImpair DefensesInhibit System RecoveryInitial AccessLateral MovementMalwarePersistencePrivilege EscalationResource DevelopmentClear all

Display name | API name | Log source types | Description | Sensitive data enrichment  
---|---|---|---|---  
Active Scan: Log4j Vulnerable to RCE | Unavailable | [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring#using_logging) |  Log4j vulnerability scanners initiated and identified DNS queries for unobfuscated domains. This vulnerability can lead to remote code execution (RCE). Findings are classified as **High** severity by default.  | —  
Impact: Deleted Google Cloud Backup and DR host | `BACKUP_HOSTS_DELETE_HOST` |  **Cloud Audit Logs** :  
[ Backup and DR Service Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A host was deleted from the Backup and DR management console. Applications that are associated with the deleted host might not be protected. Findings are classified as **Low** severity by default.  | —  
Impact: Google Cloud Backup and DR expire image | `BACKUP_EXPIRE_IMAGE` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A user requested the deletion of a backup image from the Backup and DR management console. The deletion of a backup image does not prevent future backups. Findings are classified as **Medium** severity by default.  | —  
Impact: Google Cloud Backup and DR remove plan | `BACKUP_REMOVE_PLAN` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A backup plan with multiple policies for an application was deleted from Backup and DR. The deletion of a backup plan can prevent future backups. Findings are classified as **Medium** severity by default.  | —  
Impact: Google Cloud Backup and DR expire all images | `BACKUP_EXPIRE_IMAGES_ALL` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A user requested the deletion of all backup images for a protected application from the Backup and DR management console. The deletion of backup images does not prevent future backups. Findings are classified as **High** severity by default.  | —  
Impact: Google Cloud Backup and DR delete template | `BACKUP_TEMPLATES_DELETE_TEMPLATE` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A predefined backup template, which is used to set up backups for multiple applications, was deleted from the Backup and DR management console. The ability to set up backups in the future might be impacted. Findings are classified as **Medium** severity by default.  | —  
Impact: Google Cloud Backup and DR delete policy | `BACKUP_TEMPLATES_DELETE_POLICY` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A Backup and DR policy, which defines how a backup is taken and where it is stored, was deleted from the Backup and DR management console. Future backups that use the policy might fail. Findings are classified as **Low** severity by default.  | —  
Impact: Google Cloud Backup and DR delete profile | `BACKUP_PROFILES_DELETE_PROFILE` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A Backup and DR profile, which defines which storage pools should be used to store backups, was deleted from the Backup and DR management console. Future backups that use the profile might fail. Findings are classified as **Low** severity by default.  | —  
Impact: Google Cloud Backup and DR remove appliance | `BACKUP_APPLIANCES_REMOVE_APPLIANCE` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A backup appliance was deleted from the Backup and DR management console. Applications that are associated with the deleted backup appliance might not be protected. Findings are classified as **Medium** severity by default.  | —  
Impact: Google Cloud Backup and DR delete storage pool | `BACKUP_STORAGE_POOLS_DELETE` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A storage pool, which associates a Cloud Storage bucket with Backup and DR, was removed from the Backup and DR management console. Future backups to this storage target will fail. Findings are classified as **Low** severity by default.  | —  
Impact: Google Cloud Backup and DR reduced backup expiration | `BACKUP_REDUCE_BACKUP_EXPIRATION` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  The expiration date for a backup protected by Backup and DR was reduced through the Backup and DR management console. Findings are classified as **Low** severity by default.  | —  
Impact: Google Cloud Backup and DR reduced backup frequency | `BACKUP_REDUCE_BACKUP_FREQUENCY` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  The Backup and DR backup schedule was modified to reduce backup frequency through the Backup and DR management console. Findings are classified as **Low** severity by default.  | —  
Impact: Deleted Google Cloud Backup and DR Vault | `BACKUP_DELETE_VAULT` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A backup vault was deleted. Findings are classified as **High** severity by default.  | —  
Impact: Deleted Google Cloud Backup and DR Backup | `BACKUP_DELETE_VAULT_BACKUP` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A backup stored in a backup vault was manually deleted. Findings are classified as **High** severity by default.  | —  
Impact: Deleted Google Cloud Backup and DR plan association | `BACKUP_DELETE_BACKUP_PLAN_ASSOCIATION` |  **Cloud Audit Logs** :  
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  A backup plan from Backup and DR was removed from a workload. Findings are classified as **High** severity by default.  | —  
Brute force SSH | `BRUTE_FORCE_SSH` |  [ authlog](https://docs.cloud.google.com/logging/docs/view/query-library#gce-filters) | An actor successfully gained SSH access on a host through brute force techniques. Findings are classified as **High** severity by default.  | —  
Cloud IDS: THREAT_IDENTIFIER | `CLOUD_IDS_THREAT_ACTIVITY` | [Cloud IDS logs](https://docs.cloud.google.com/intrusion-detection-system/docs/logging) |  [Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs/overview) detected threat events.  Cloud IDS detects layer 7 attacks by analyzing mirrored packets and, when a threat event is detected, sends a threat-class finding to Security Command Center. Finding category names start with "Cloud IDS" followed by the Cloud IDS threat identifier.  The Cloud IDS integration with Event Threat Detection does not include Cloud IDS vulnerability detections. Findings are classified as **Low** severity by default.  To learn more about Cloud IDS detections, see [ Cloud IDS Logging information](https://docs.cloud.google.com/intrusion-detection-system/docs/logging).  | —  
Privilege Escalation: External Member Added To Privileged Group | `EXTERNAL_MEMBER_ADDED_TO_PRIVILEGED_GROUP` |  **Google Workspace Logs** :  
[Login Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#2)  
**Permissions** :  
`DATA_READ` |  An external member was added to a privileged Google Group (a group granted sensitive roles or permissions). A finding is generated only if the group doesn't already contain other external members from the same organization as the newly added member. To learn more, see Unsafe Google Group changes.  This finding isn't available for project-level activations. Findings are classified as **High** or **Medium** severity, depending on the sensitivity of the roles associated with the group change. For more information, see Sensitive IAM roles and permissions.  | —  
Privilege Escalation: Privileged Group Opened To Public | `PRIVILEGED_GROUP_OPENED_TO_PUBLIC` |  **Google Workspace** :  
[Admin Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#3)  
**Permissions** :  
`DATA_READ` |  A privileged Google Group (a group granted sensitive roles or permissions) was changed to be accessible to the general public. To learn more, see Unsafe Google Group changes.  This finding isn't available for project-level activations. Findings are classified as **High** or **Medium** severity, depending on the sensitivity of the roles associated with the group change. For more information, see Sensitive IAM roles and permissions.  | —  
Privilege Escalation: Sensitive Role Granted To Hybrid Group | `SENSITIVE_ROLE_TO_GROUP_WITH_EXTERNAL_MEMBER` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  Sensitive roles were granted to a Google Group with external members. To learn more, see Unsafe Google Group changes.  Findings are classified as **High** or **Medium** severity, depending on the sensitivity of the roles associated with the group change. For more information, see Sensitive IAM roles and permissions.  | —  
Defense Evasion: Breakglass Workload Deployment Created ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `BINARY_AUTHORIZATION_BREAKGLASS_WORKLOAD_CREATE` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  Workloads were deployed by using the break-glass flag to override [Binary Authorization](https://docs.cloud.google.com/binary-authorization) controls. Findings are classified as **Low** severity by default.  | —  
Defense Evasion: Breakglass Workload Deployment Updated ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `BINARY_AUTHORIZATION_BREAKGLASS_WORKLOAD_UPDATE` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  Workloads were updated by using the break-glass flag to override [Binary Authorization](https://docs.cloud.google.com/binary-authorization) controls. Findings are classified as **Low** severity by default.  | —  
Discovery: Evidence of Port Scanning from AI Agent ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_PORT_SCANNING_EVIDENCE` |  **Agent Engine Logs** :  
[Agent Engine Logs](https://docs.cloud.google.com/agent-builder/agent-engine/manage/logging) |  An AI agent exhibited horizontal or vertical port scanning behavior. Findings are classified as **Low** severity by default.  | —  
Discovery: AI Agent Unauthorized Service Account API Call ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_UNAUTHORIZED_SERVICE_ACCOUNT_API_CALL` |  **Cloud Audit Logs** :  
[Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A service account made an unauthorized API call to an outside project through an AI agent. This behavior can indicate that an unauthorized user is attempting to gain details about resources, enable or disable services, or perform other unauthorized actions through an AI agent. Findings are classified as **Low** severity by default.  |  Category: `Discovery: AI Agent Unauthorized Service Account API Call Affecting Sensitive Data`  
Severity: Low to Medium   
Defense Evasion: GCS Bucket IP Filtering Modified | `GCS_BUCKET_IP_FILTERING_MODIFIED` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A user or service account changed the IP filtering configuration for a Cloud Storage bucket. Findings are classified as **Low** severity by default.  | —  
Defense Evasion: Modify VPC Service Control | `DEFENSE_EVASION_MODIFY_VPC_SERVICE_CONTROL` |  **Cloud Audit Logs** [VPC Service Controls audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) |  An existing VPC Service Controls perimeter was changed that would lead to a reduction in the protection offered by that perimeter.  This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Defense Evasion: Project HTTP Policy Block Disabled | `PROJECT_HTTP_POLICY_BLOCK_DISABLED` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A user or service account successfully triggered an action to disable [storage.secureHttpTransport](https://cloud.google.com/storage/docs/org-policy-constraints#block-unencrypted-http) on a project. This also applies when the action is taken at an org-level or folder-level since policies applied at this level are inherited by child projects by default. Findings are classified as **Low** severity by default.  | —  
Discovery: AI Agent Service Account Self-Investigation ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_IAM_ANOMALOUS_BEHAVIOR_SERVICE_ACCOUNT_GETS_OWN_IAM_POLICY` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
**Permissions** :  
`DATA_READ` |  An identity associated with an AI agent was used to investigate the roles and permissions associated with that same service account. Findings are classified as **Low** severity if the request was authorized, or **High** severity if the request was not authorized.  | —  
Discovery: Can get sensitive Kubernetes object check | `GKE_CONTROL_PLANE_CAN_GET_SENSITIVE_OBJECT` |  **Cloud Audit Logs** :  
[ GKE Data Access logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  A potentially malicious actor attempted to determine what sensitive objects in GKE they can query for, by using the [ `kubectl auth can-i get`](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#checking-api-access) command. Specifically, the rule detects whether the actor checked for API access on the following objects: 

  * `*` (all)
  * [ `cluster-admin`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) `ClusterRole`
  * [ `Secret`](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)

Findings are classified as **Low** severity by default.  | —  
Discovery: Service Account Self-Investigation | `SERVICE_ACCOUNT_SELF_INVESTIGATION` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
**Permissions** :  
`DATA_READ` |  An IAM service account credential was used to investigate the roles and permissions associated with that same service account.  **Sensitive roles** Findings are classified as **High** or **Medium** severity, depending on the sensitivity of the roles granted. For more information, see Sensitive IAM roles and permissions.  | —  
Credential Access: AI Agent Anomalous Access to Metadata Service ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_ANOMALOUS_ACCESS_TO_METADATA_SERVICE` |  **Agent Engine Logs** :  
[Agent Engine Logs](https://docs.cloud.google.com/agent-builder/agent-engine/manage/logging) |  An AI agent fetched a service account token from a metadata server. Findings are classified as **Low** severity by default.  | —  
Evasion: Access from Anonymizing Proxy | `ANOMALOUS_ACCESS` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  Google Cloud service modifications originated from an IP address associated with the Tor network. Findings are classified as **Medium** severity by default.  | —  
Exfiltration: BigQuery Data Exfiltration | `DATA_EXFILTRATION_BIG_QUERY` |  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions)  
**Permissions** :  
`DATA_READ` |  Detects the following scenarios:

  * Resources owned by the protected organization were saved outside of the organization, including copy or transfer operations.  This scenario is indicated by a subrule of `exfil_to_external_table` and **High** severity. 
  * Attempts were made to access BigQuery resources that are protected by VPC Service Controls.  This scenario is indicated by a subrule of `vpc_perimeter_violation` and **Low** severity. 

|  Category: `Exfiltration: Sensitive BigQuery Data Exfiltration`  
Severity: Low to Medium   
Exfiltration: BigQuery Data Extraction | `DATA_EXFILTRATION_BIG_QUERY_EXTRACTION` |  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions)  
**Permissions** :  
`DATA_READ` |  Detects the following scenarios:

  * A BigQuery resource owned by the organization was saved, through extraction operations, to a Cloud Storage bucket outside the organization. 
  * A BigQuery resource owned by the protected organization was saved, through extraction operations, to a publicly accessible Cloud Storage bucket owned by that organization. 

For project-level activations of the Security Command Center Premium tier, this finding is available only if the Standard-legacy tier is enabled in the parent organization.. Findings are classified as **Low** severity by default. |  Category: `Exfiltration: Sensitive BigQuery Data Extraction`  
Severity: Low to Medium   
Exfiltration: AI Agent Initiated BigQuery VPC Perimeter Violation ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `AGENT_ENGINE_BIG_QUERY_EXFIL_VPC_PERIMETER_VIOLATION`  
|  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions) **Permissions** :  
`DATA_READ` |  Detects an attempt by an AI agent to access BigQuery resources that are protected by VPC Service Controls. Findings are classified as **Low** severity by default.  | —  
Exfiltration: AI Agent Initiated BigQuery Data Exfiltration to External Table ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `AGENT_ENGINE_BIG_QUERY_EXFIL_TO_EXTERNAL_TABLE`  
|  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions) **Permissions** :  
`DATA_READ` |  Detects when resources owned by the protected organization were saved outside of the organization by an AI agent, including copy or transfer operations. Findings are classified as **High** severity by default.  |  Category: `Exfiltration: AI Agent Initiated Sensitive BigQuery Data Exfiltration to External Table`  
Severity: No change (default High)   
Exfiltration: AI Agent Initiated CloudSQL Exfiltration to Public Bucket ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `AGENT_ENGINE_CLOUDSQL_EXFIL_EXPORT_TO_PUBLIC_GCS`  
|  **Cloud Audit Logs** : [MySQL data access logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
[PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[SQL Server data access logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging) |  Detects when live instance data was exported by an AI agent to a Cloud Storage bucket that is owned by the organization and is publicly accessible.  For project-level activations of the Security Command Center Premium tier, this finding is available only if the Standard-legacy tier is enabled in the parent organization.. Findings are classified as **High** severity by default.  | —  
Exfiltration: AI Agent Initiated CloudSQL Exfiltration to External Bucket ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `AGENT_ENGINE_CLOUDSQL_EXFIL_EXPORT_TO_EXTERNAL_GCS` |  **Cloud Audit Logs** : [MySQL data access logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
[PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[SQL Server data access logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging) |  Detects when live instance data was exported by an AI agent to a Cloud Storage bucket outside of the organization.  For project-level activations of the Security Command Center Premium tier, this finding is available only if the Standard-legacy tier is enabled in the parent organization.. Findings are classified as **High** severity by default.  | —  
Exfiltration: AI Agent Initiated BigQuery Data Extraction ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_BIG_QUERY_EXFIL_TO_CLOUD_STORAGE` |  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions) **Permissions** :  
`DATA_READ` |  Detects the following scenarios of a BigQuery data extraction initiated by an AI agent:

  * A BigQuery resource owned by the protected organization was saved, through extraction operations, to a Cloud Storage bucket outside the organization. 
  * A BigQuery resource owned by the protected organization was saved, through extraction operations, to a publicly accessible Cloud Storage bucket owned by that organization. 

For project-level activations of the Security Command Center Premium tier, this finding is available only if the Standard-legacy tier is enabled in the parent organization.. Findings are classified as **Low** severity by default. |  Category: `Exfiltration: AI Agent Initiated Sensitive BigQuery Data Extraction`  
Severity: Low to Medium   
Exfiltration: BigQuery Data to Google Drive | `DATA_EXFILTRATION_BIG_QUERY_TO_GOOGLE_DRIVE` |  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions)  
**Permissions** :  
`DATA_READ` |  A BigQuery resource that is owned by the protected organization was saved, through extraction operations, to a Google Drive folder. Findings are classified as **Low** severity by default.  |  Category: `Exfiltration: Sensitive BigQuery Data to Google Drive`  
Severity: Low to Medium   
Exfiltration: Move to Public BigQuery resource | `DATA_EXFILTRATION_BIG_QUERY_TO_PUBLIC_RESOURCE` |  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions)  
**Permissions** :  
`DATA_READ` |  A BigQuery resource was saved to a public resource owned by your organization. Findings are classified as **Medium** severity by default. | —  
Exfiltration: Cloud SQL Data Exfiltration |  `CLOUDSQL_EXFIL_EXPORT_TO_EXTERNAL_GCS  
CLOUDSQL_EXFIL_EXPORT_TO_PUBLIC_GCS` |  **Cloud Audit Logs** : [MySQL data access logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
[PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[SQL Server data access logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging) |  Detects the following scenarios:

  * Live instance data was exported to a Cloud Storage bucket outside of the organization. 
  * Live instance data was exported to a Cloud Storage bucket that is owned by the organization and is publicly accessible. 

For project-level activations of the Security Command Center Premium tier, this finding is available only if the Standard-legacy tier is enabled in the parent organization.. Findings are classified as **High** severity by default.  | —  
Exfiltration: Cloud SQL Restore Backup to External Organization | `CLOUDSQL_EXFIL_RESTORE_BACKUP_TO_EXTERNAL_INSTANCE` |  **Cloud Audit Logs** : [MySQL admin activity logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
[PostgreSQL admin activity logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[SQL Server admin activity logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging) |  The backup of a Cloud SQL instance was restored to an instance outside of the organization. Findings are classified as **High** severity by default.  | —  
Exfiltration: Cloud SQL Over-Privileged Grant | `CLOUDSQL_EXFIL_USER_GRANTED_ALL_PERMISSIONS` |  **Cloud Audit Logs** : [PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
**Note** : You must enable [the pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit) extension to use this rule.  |  A Cloud SQL for PostgreSQL user or role was granted all privileges to a database, or to all tables, procedures, or functions in a schema. Findings are classified as **Low** severity by default.  | —  
Initial Access: Database Superuser Writes to User Tables | `CLOUDSQL_SUPERUSER_WRITES_TO_USER_TABLES` |  **Cloud Audit Logs** : [ Cloud SQL for PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[Cloud SQL for MySQL data access logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
**Note** : You must enable [the pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit) extension for PostgreSQL or [database auditing](https://docs.cloud.google.com/sql/docs/mysql/use-db-audit) for MySQL to use this rule.  |  A Cloud SQL superuser (`postgres` for PostgreSQL servers or `root` for MySQL users) wrote to non-system tables. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: AlloyDB Over-Privileged Grant | `ALLOYDB_USER_GRANTED_ALL_PERMISSIONS` |  **Cloud Audit Logs** : [ AlloyDB for PostgreSQL data access logs](https://docs.cloud.google.com/alloydb/docs/audit-logging)  
**Note** : You must enable [the pgAudit](https://docs.cloud.google.com/alloydb/docs/pgaudit/enable-audit) extension to use this rule.  |  An AlloyDB for PostgreSQL user or role was granted all privileges to a database, or to all tables, procedures, or functions in a schema. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: AlloyDB Database Superuser Writes to User Tables | `ALLOYDB_SUPERUSER_WRITES_TO_USER_TABLES` |  **Cloud Audit Logs** : [AlloyDB for PostgreSQL data access logs](https://docs.cloud.google.com/alloydb/docs/audit-logging)  
**Note** : You must enable [the pgAudit](https://docs.cloud.google.com/alloydb/docs/pgaudit/enable-audit) extension to use this rule.  |  An AlloyDB for PostgreSQL superuser (`postgres`) wrote to non-system tables. Findings are classified as **Low** severity by default.  | —  
Initial Access: AI Agent Identity Excessive Permission Denied Actions ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_EXCESSIVE_FAILED_ATTEMPT` |  **Cloud Audit Logs** : [Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  An identity associated with an AI agent repeatedly triggered _permission denied_ errors by attempting changes across multiple methods and services. Findings are classified as **Medium** severity by default.  | —  
Initial Access: Dormant Service Account Action | `DORMANT_SERVICE_ACCOUNT_USED_IN_ACTION` |  **Cloud Audit Logs** : [Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A dormant [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) triggered an action. In this context, a service account is considered dormant if it has been inactive for more than 180 days. Findings are classified as **High** severity by default.  |  Category: `Initial Access: Dormant Service Account Action taken Affecting Sensitive Data`  
Severity: No change (default High)   
Privilege Escalation: Dormant Service Account Granted Sensitive Role | `DORMANT_SERVICE_ACCOUNT_ADDED_IN_IAM_ROLE` |  **Cloud Audit Logs** : [IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A dormant [ user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) was granted one or more sensitive IAM roles. In this context, a service account is considered dormant if it has been inactive for more than 180 days. **Sensitive roles** Findings are classified as **High** or **Medium** severity, depending on the sensitivity of the roles granted. Findings are classified as **Medium** severity by default. For more information, see Sensitive IAM roles and permissions.  | —  
Privilege Escalation: Impersonation Role Granted For Dormant Service Account | `DORMANT_SERVICE_ACCOUNT_IMPERSONATION_ROLE_GRANTED` |  **Cloud Audit Logs** : [IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A principal was granted [ permissions to impersonate](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) a dormant user-managed service account. In this context, a service account is considered dormant if it has been inactive for more than 180 days. Findings are classified as **Medium** severity by default.  | —  
Initial Access: Dormant Service Account Key Created | `DORMANT_SERVICE_ACCOUNT_KEY_CREATED` |  **Cloud Audit Logs** : [Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A key was created for a dormant [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed). In this context, a service account is considered dormant if it has been inactive for more than 180 days. Findings are classified as **High** severity by default.  | —  
Initial Access: Leaked Service Account Key Used | `LEAKED_SA_KEY_USED` |  **Cloud Audit Logs** : [Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  
[Data Access logs](https://docs.cloud.google.com/logging/docs/audit#data-access) |  A leaked service account key was used to authenticate the action. In this context, a leaked service account key is one that was posted on the public internet. Findings are classified as **High** severity by default.  |  Category: `Initial Access: Leaked Service Account Key Affecting Sensitive Data`  
Severity: No change (default High)   
Initial Access: Excessive Permission Denied Actions | `EXCESSIVE_FAILED_ATTEMPT` |  **Cloud Audit Logs** : [Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A principal repeatedly triggered _permission denied_ errors by attempting changes across multiple methods and services. Findings are classified as **Medium** severity by default.  | —  
Persistence: Strong Authentication Disabled |  [ `ENFORCE_STRONG_AUTHENTICATION`](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-security-settings#ENFORCE_STRONG_AUTHENTICATION) |  **Google Workspace** :  
[Admin Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#3) |  2-step verification was disabled for the organization. This finding isn't available for project-level activations. Findings are classified as **Medium** severity by default. | —  
Persistence: Two Step Verification Disabled |  [ `2SV_DISABLE`](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/login#2sv_disable) |  **Google Workspace Logs** :  
[Login Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#2)  
**Permissions** :  
`DATA_READ` |  A user disabled 2-step verification. This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Initial Access: Account Disabled Hijacked |  [ `ACCOUNT_DISABLED_HIJACKED`](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/login#account_disabled_hijacked) |  **Google Workspace Logs** :  
[Login Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#2)  
**Permissions** :  
`DATA_READ` |  A user's account was suspended due to suspicious activity. This finding isn't available for project-level activations. Findings are classified as **Medium** severity by default. | —  
Initial Access: Disabled Password Leak |  [ `ACCOUNT_DISABLED_PASSWORD_LEAK`](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/login#account_disabled_password_leak) |  **Google Workspace Logs** :  
[Login Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#2)  
**Permissions** :  
`DATA_READ` |  A user's account was disabled because a password leak was detected. This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Initial Access: Government Based Attack |  [ `GOV_ATTACK_WARNING`](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/login#gov_attack_warning) |  **Google Workspace Logs** :  
[Login Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#2)  
**Permissions** :  
`DATA_READ` |  Government-backed attackers might have tried to compromise a user account or computer.  This finding isn't available for project-level activations. Findings are classified as **High** severity by default. | —  
Initial Access: Log4j Compromise Attempt | Unavailable |  **Cloud Load Balancing Logs** :  
[ Cloud HTTP Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring)  
**Note** : You must enable external Application Load Balancer logging to use this rule.  |  Java Naming and Directory Interface (JNDI) [lookups](https://logging.apache.org/log4j/2.x/manual/lookups.html) within headers or URL parameters were detected. These lookups might indicate attempts at Log4Shell exploitation. These findings have low severity, because they only indicate a detection or exploit attempt, not a vulnerability or a compromise.  This rule is always on. Findings are classified as **Low** severity by default. | —  
Initial Access: Suspicious Login Blocked |  [ `SUSPICIOUS_LOGIN`](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/login#suspicious_login) |  **Google Workspace Logs** :  
[Login Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#2)  
**Permissions** :  
`DATA_READ` |  A suspicious login to a user's account was detected and blocked. This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Log4j Malware: Bad Domain | `LOG4J_BAD_DOMAIN` | [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring#using_logging) |  Log4j exploit traffic was detected based on a connection to, or a lookup of, a known domain used in Log4j attacks. Findings are classified as **Low** severity by default.  | —  
Log4j Malware: Bad IP | `LOG4J_BAD_IP` |  [VPC flow logs](https://docs.cloud.google.com/vpc/docs/flow-logs)  
[Firewall Rules logs](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging)  
[Cloud NAT logs](https://docs.cloud.google.com/nat/docs/monitoring) |  Log4j exploit traffic was detected based on a connection to a known IP address used in Log4j attacks. Findings are classified as **Low** severity by default.  | —  
Malware: bad domain | `MALWARE_BAD_DOMAIN` | [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring#using_logging) |  Malware was detected based on a connection to, or a lookup of, a known bad domain. Findings are classified as **Low** severity by default.  | —  
Malware: bad IP | `MALWARE_BAD_IP` |  [VPC flow logs](https://docs.cloud.google.com/vpc/docs/flow-logs)  
[Firewall Rules logs](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging)  
[Cloud NAT logs](https://docs.cloud.google.com/nat/docs/monitoring) | Malware was detected based on a connection to a known bad IP address. Findings are classified as **Low** severity by default. | —  
Malware: Cryptomining Bad Domain | `CRYPTOMINING_POOL_DOMAIN` | [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring#using_logging) |  Cryptomining was detected based on a connection to, or a lookup of, a known mining domain. Findings are classified as **Low** severity by default.  | —  
Malware: Cryptomining Bad IP | `CRYPTOMINING_POOL_IP` |  [VPC flow logs](https://docs.cloud.google.com/vpc/docs/flow-logs)  
[Firewall Rules logs](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging)  
[Cloud NAT logs](https://docs.cloud.google.com/nat/docs/monitoring) | Cryptomining was detected based on a connection to a known mining IP address. Findings are classified as **Low** severity by default. | —  
Persistence: GCE Admin Added SSH Key | `GCE_ADMIN_ADD_SSH_KEY` |  **Cloud Audit Logs** :  
[Compute Engine Admin Activity audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging) |  The Compute Engine instance metadata SSH key value was modified on an established instance (older than 1 week). Findings are classified as **Low** severity by default.  | —  
Persistence: GCE Admin Added Startup Script | `GCE_ADMIN_ADD_STARTUP_SCRIPT` |  **Cloud Audit Logs** :  
[Compute Engine Admin Activity audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging) |  The Compute Engine instance metadata startup script value was modified on an established instance (older than 1 week). Findings are classified as **Low** severity by default.  | —  
Persistence: IAM Anomalous Grant | `IAM_ANOMALOUS_GRANT` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  This finding includes subrules that provide more specific information about each instance of this finding.  The following list shows all possible subrules:

  * `external_service_account_added_to_policy`, `external_member_added_to_policy`: Privileges were granted to IAM users and service accounts that are not members of your organization or, if Security Command Center is activated at the project level only, your project.  **Note** : If Security Command Center is activated at the organization level at any tier, then this detector uses an organization's existing IAM policies as context. If Security Command Center activation is only at the project level, then the detector uses only the project's IAM policies as context.  If a sensitive IAM grant to an external member occurs, and there are less than three existing IAM policies that are similar to it, this detector generates a finding.  **Sensitive roles** Findings are classified as **High** or **Medium** severity, depending on the sensitivity of the roles granted. Findings are classified as **High** severity by default. For more information, see Sensitive IAM roles and permissions. 
  * `external_member_invited_to_policy`: An external member was invited as the owner of the project through the `InsertProjectOwnershipInvite` API. 
  * `custom_role_given_sensitive_permissions`: The `setIAMPolicy` permission was added to a custom role. 
  * `service_account_granted_sensitive_role_to_member`: Privileged roles were granted to members through a service account. This subrule is triggered by a subset of sensitive roles that include only basic IAM roles and certain data storage roles. For more information, see Sensitive IAM roles and permissions. 
  * `policy_modified_by_default_compute_service_account`: A default Compute Engine service account was used to modify project IAM settings. 

| —  
Persistence: Sensitive AI Permission Added to Custom Role ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `SENSITIVE_AI_PERMISSION_ADDED_TO_CUSTOM_ROLE` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A sensitive AI permission was added to an IAM [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles). For more information, see Sensitive IAM roles and permissions for AI. Findings are classified as **Medium** severity by default.  | —  
Persistence: Sensitive Role Granted by AI Agent ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `SENSITIVE_ROLE_GRANTED_BY_AI_AGENT` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  An AI agent granted a sensitive IAM role. Findings are classified as **Medium** severity for medium-sensitivity roles, or **High** severity for high-sensitivity roles. For more information, see Sensitive IAM roles and permissions for AI.  | —  
Persistence: Sensitive Role Granted to External AI Agent ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `EXTERNAL_AI_AGENT_GRANTED_SENSITIVE_ROLE` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  An AI agent from an external organization was granted a sensitive IAM role. Findings are classified as **Medium** severity for medium-sensitivity roles, or **High** severity for high-sensitivity roles. For more information, see Sensitive IAM roles and permissions for AI.  | —  
Persistence: Unmanaged Account Granted Sensitive Role ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `UNMANAGED_ACCOUNT_ADDED_IN_IAM_ROLE` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A sensitive role was granted to an [unmanaged account](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts). Findings are classified as **High** severity by default.  | —  
Persistence: New API Method  
| `ANOMALOUS_BEHAVIOR_NEW_API_METHOD` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  IAM service accounts used anomalous access to Google Cloud services. Findings are classified as **Low** severity by default. |  Category: `Persistence: New API Method Affecting Sensitive Data`  
Severity: Low to Medium   
Persistence: New Geography | `IAM_ANOMALOUS_BEHAVIOR_IP_GEOLOCATION` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  IAM user and service accounts accessed Google Cloud from anomalous locations, based on the geolocation of the requesting IP addresses.  This finding isn't available for project-level activations and they are classified as **Low** severity by default. | —  
Persistence: New User Agent | `IAM_ANOMALOUS_BEHAVIOR_USER_AGENT` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  IAM service accounts accessed Google Cloud from anomalous or suspicious user agents. This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Persistence: SSO Enablement Toggle |  [ `TOGGLE_SSO_ENABLED`](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-domain-settings#TOGGLE_SSO_ENABLED) |  **Google Workspace** :  
[Admin Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#3) |  The Enable SSO (single sign-on) setting on the admin account was disabled. This finding isn't available for project-level activations. Findings are classified as **High** severity by default. | —  
Persistence: SSO Settings Changed |  [ `CHANGE_SSO_SETTINGS`](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-domain-settings#CHANGE_SSO_SETTINGS) |  **Google Workspace** :  
[Admin Audit](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#3) |  The SSO settings for the admin account were changed. This finding isn't available for project-level activations. Findings are classified as **High** severity by default. | —  
Privilege Escalation: Anomalous Impersonation of Service Account for Admin Activity  | `ANOMALOUS_SA_DELEGATION_IMPERSONATION_OF_SA_ADMIN_ACTIVITY` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A potentially anomalous [impersonated service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) was used for an administrative activity. Findings are classified as **Medium** severity by default.  |  Category: `Privilege Escalation: Anomalous Impersonation of Service Account for Admin Activity Affecting Sensitive Data`  
Severity: Medium to High   
Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity  | `ANOMALOUS_SA_DELEGATION_MULTISTEP_ADMIN_ACTIVITY` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  An anomalous multistep [ delegated request](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-delegated) was found for an administrative activity. Findings are classified as **Medium** severity by default.  |  Category: `Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity Affecting Sensitive Data`  
Severity: Medium to High   
Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access  | `ANOMALOUS_SA_DELEGATION_MULTISTEP_DATA_ACCESS` |  **Cloud Audit Logs** :  
[Data Access logs](https://docs.cloud.google.com/logging/docs/audit#data-access) |  An anomalous multistep [ delegated request](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-delegated) was found for a data access activity. Findings are classified as **Medium** severity by default.  |  Category: `Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access Affecting Sensitive Data`  
Severity: Medium to High   
Privilege Escalation: Anomalous Service Account Impersonator for Admin Activity | `ANOMALOUS_SA_DELEGATION_IMPERSONATOR_ADMIN_ACTIVITY` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A potentially anomalous [caller or impersonator](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) in a delegation chain was used for an administrative activity. Findings are classified as **Medium** severity by default.  |  Category: `Privilege Escalation: Anomalous Service Account Impersonator for Admin Activity Affecting Sensitive Data`  
Severity: Medium to High   
Privilege Escalation: Anomalous Service Account Impersonator for Data Access | `ANOMALOUS_SA_DELEGATION_IMPERSONATOR_DATA_ACCESS` |  **Cloud Audit Logs** :  
[Data Access logs](https://docs.cloud.google.com/logging/docs/audit#data-access) |  A potentially anomalous [caller or impersonator](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) in a delegation chain was used for a data access activity. Findings are classified as **Medium** severity by default.  |  Category: `Privilege Escalation: Anomalous Service Account Impersonator for Data Access Affecting Sensitive Data`  
Severity: Medium to High   
Privilege Escalation: Changes to sensitive Kubernetes RBAC objects | `GKE_CONTROL_PLANE_EDIT_SENSITIVE_RBAC_OBJECT` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  To escalate privilege, a potentially malicious actor attempted to modify a `ClusterRole`, `RoleBinding`, or `ClusterRoleBinding` role-based access control (RBAC) object of the sensitive [ `cluster-admin`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) role by using a `PUT` or `PATCH` request. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: Create Kubernetes CSR for master cert | `GKE_CONTROL_PLANE_CSR_FOR_MASTER_CERT` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  A potentially malicious actor created a Kubernetes master [ certificate signing request](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests) (CSR), which gives them [ `cluster-admin`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) access. Findings are classified as **High** severity by default.  | —  
Privilege Escalation: Creation of sensitive Kubernetes bindings | `GKE_CONTROL_PLANE_CREATE_SENSITIVE_BINDING` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  To escalate privilege, a potentially malicious actor attempted to create a new `RoleBinding` or `ClusterRoleBinding` object for the [ `cluster-admin`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) role. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: Get Kubernetes CSR with compromised bootstrap credentials | `GKE_CONTROL_PLANE_GET_CSR_WITH_COMPROMISED_BOOTSTRAP_CREDENTIALS` |  **Cloud Audit Logs** :  
[ GKE Data Access logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  A potentially malicious actor queried for a [ certificate signing request](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/) (CSR), with the `kubectl` command, using compromised bootstrap credentials. Findings are classified as **High** severity by default.  | —  
Privilege Escalation: Launch of privileged Kubernetes container | `GKE_CONTROL_PLANE_LAUNCH_PRIVILEGED_CONTAINER` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  A potentially malicious actor created a Pod that contains privileged containers or containers with privilege escalation capabilities.  A privileged container has the `privileged` field set to `true`. A container with privilege escalation capabilities has the `allowPrivilegeEscalation` field set to `true`. For more information, see the [ SecurityContext v1 core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#securitycontext-v1-core) API reference in the Kubernetes documentation. Findings are classified as **Low** severity by default.  | —  
Persistence: Service Account Key Created | `SERVICE_ACCOUNT_KEY_CREATION` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A service account key was created. Service account keys are long-lived credentials that increase the risk of unauthorized access to Google Cloud resources. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: Global Shutdown Script Added | `GLOBAL_SHUTDOWN_SCRIPT_ADDED` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) | A global shutdown script was added to a project. Findings are classified as **Low** severity by default. | —  
Persistence: Global Startup Script Added | `GLOBAL_STARTUP_SCRIPT_ADDED` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) | A global startup script was added to a project. Findings are classified as **Low** severity by default. | —  
Defense Evasion: Organization level TokenCreatorRole Added | `ORG_LEVEL_SERVICE_ACCOUNT_TOKEN_CREATOR_ROLE_ADDED` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) | The [ Service Account Token Creator IAM role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) was granted at the organization level. Findings are classified as **Low** severity by default.  | —  
Defense Evasion: Folder level TokenCreatorRole Added | `FOLDER_LEVEL_SERVICE_ACCOUNT_TOKEN_CREATOR_ROLE_ADDED` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  The [ Service Account Token Creator IAM role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) was granted at the folder level. Findings are classified as **Low** severity by default.  | —  
Defense Evasion: Project level TokenCreatorRole Added | `PROJECT_LEVEL_SERVICE_ACCOUNT_TOKEN_CREATOR_ROLE_ADDED` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  The [ Service Account Token Creator IAM role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) was granted at the project level. Findings are classified as **Low** severity by default.  | —  
Defense Evasion: Organization Level TokenCreator Role Granted to AI Agent ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AI_AGENT_GRANTED_TOKEN_CREATOR_ROLE_ORG` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  An AI agent was granted the [ Service Account Token Creator IAM role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) at the organization level. Findings are classified as **High** severity by default.  | —  
Defense Evasion: Folder Level TokenCreator Role Granted to AI Agent ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AI_AGENT_GRANTED_TOKEN_CREATOR_ROLE_FOLDER` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  An AI agent was granted the [ Service Account Token Creator IAM role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) at the folder level. Findings are classified as **High** severity by default.  | —  
Defense Evasion: Project Level TokenCreator Role Granted to AI Agent | `AI_AGENT_GRANTED_TOKEN_CREATOR_ROLE_PROJECT` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  An AI agent was granted the [ Service Account Token Creator IAM role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) at the project level. Findings are classified as **High** severity by default.  | —  
Lateral Movement: OS Patch Execution From Service Account Temporarily unavailable | `OS_PATCH_EXECUTION_FROM_SERVICE_ACCOUNT` |  **Cloud Audit Logs**.  
[VM Manager audit logs](https://docs.cloud.google.com/compute/vm-manager/docs/audit-logging) |  A service account used the [Compute Engine Patch feature](https://docs.cloud.google.com/compute/docs/os-patch-management) to update the operating system of any currently running Compute Engine instance. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor VM Manager activity, use [VM Manager audit logs](https://docs.cloud.google.com/compute/vm-manager/docs/audit-logging).  | —  
Lateral Movement: Modified Boot Disk Attached to Instance ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `MODIFY_BOOT_DISK_ATTACH_TO_INSTANCE` |  **Cloud Audit Logs** :  
[Compute Engine audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging) |  A boot disk was detached from one Compute Engine instance and attached to another, which could indicate a malicious attempt to compromise the system using a modified boot disk. Findings are classified as **Low** severity by default.  | —  
Credential Access: Secrets Accessed In Kubernetes Namespace | `SECRETS_ACCESSED_IN_KUBERNETES_NAMESPACE` |  **Cloud Audit Logs** :  
[ GKE Data Access logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Secrets or service account tokens were accessed by a service account in the current Kubernetes namespace. Findings are classified as **Low** severity by default.  | —  
Resource Development: Offensive Security Distro Activity | `OFFENSIVE_SECURITY_DISTRO_ACTIVITY` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A Google Cloud resource was successfully manipulated through known penetration testing or offensive security distros. Findings are classified as **Low** severity by default.  |  Category: `Resource Development: Offensive Security Distro Activity Affecting Sensitive Data`  
Severity: Low to Medium   
Privilege Escalation: AI Agent Token Generation Using signJwt ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_TOKEN_GENERATION_SIGN_JWT` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
|  A service account associated with an AI agent used the [ `serviceAccounts.signJwt`](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signJwt) method to generate an access token for another service account.  Findings are classified as **Low** severity by default. | —  
Privilege Escalation: AI Agent Token Generation Using Implicit Delegation ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_TOKEN_GENERATION_IMPLICIT_DELEGATION` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
|  The `iam.serviceAccounts.implicitDelegation` permission was misused to generate access tokens from a more privileged service account through an AI agent. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: AI Agent Cross-Project OpenID Token Generation ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_TOKEN_GENERATION_CROSS_PROJECT_OPENID` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
|  The `iam.serviceAccounts.getOpenIdToken` IAM permission was used across projects through an AI agent.  This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Privilege Escalation: AI Agent Cross-Project Access Token Generation ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_TOKEN_GENERATION_CROSS_PROJECT_ACCESS_TOKEN` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
|  The `iam.serviceAccounts.getAccessToken` IAM permission was used across projects through an AI agent.  This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Privilege Escalation: New Service Account is Owner or Editor Temporarily unavailable | `SERVICE_ACCOUNT_EDITOR_OWNER` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A new service account was created with Editor or Owner roles for a project. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor IAM changes, [IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging).  | —  
Discovery: Information Gathering Tool Used | `INFORMATION_GATHERING_TOOL_USED` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  ScoutSuite usage was detected. ScoutSuite is a cloud security auditing tool that is known to be used by threat actors. Findings are classified as **Low** severity by default.  |  Category: `Discovery: Information Gathering Tool Affecting Sensitive Data`  
Severity: Low to Medium   
Privilege Escalation: Suspicious Token Generation Temporarily unavailable | `SUSPICIOUS_TOKEN_GENERATION_IMPLICIT_DELEGATION` |  **Cloud Audit Logs** :  
[IAM audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  The `iam.serviceAccounts.implicitDelegation` permission was misused to generate access tokens from a more privileged service account. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor IAM activity, use [IAM audit logs](https://docs.cloud.google.com/iam/docs/audit-logging).  | —  
Privilege Escalation: Suspicious Token Generation Temporarily unavailable | `SUSPICIOUS_TOKEN_GENERATION_SIGN_JWT` |  **Cloud Audit Logs** :  
[IAM audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A service account used the [ `serviceAccounts.signJwt`](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signJwt) method to generate an access token for another service account. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor IAM activity, use [IAM audit logs](https://docs.cloud.google.com/iam/docs/audit-logging).  | —  
Privilege Escalation: Suspicious Token Generation Temporarily unavailable | `SUSPICIOUS_TOKEN_GENERATION_CROSS_PROJECT_OPENID` |  **Cloud Audit Logs** :  
[IAM audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  The `iam.serviceAccounts.getOpenIdToken` IAM permission was used across projects.  This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. This rule is temporarily unavailable. To monitor IAM activity, use [IAM audit logs](https://docs.cloud.google.com/iam/docs/audit-logging).  | —  
Privilege Escalation: Suspicious Token Generation Temporarily unavailable | `SUSPICIOUS_TOKEN_GENERATION_CROSS_PROJECT_ACCESS_TOKEN` |  **Cloud Audit Logs** :  
[IAM audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  The `iam.serviceAccounts.getAccessToken` IAM permission was used across projects.  This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. This rule is temporarily unavailable. To monitor IAM activity, use [IAM audit logs](https://docs.cloud.google.com/iam/docs/audit-logging).  | —  
Privilege Escalation: Suspicious Cross-Project Permission Use | `SUSPICIOUS_CROSS_PROJECT_PERMISSION_DATAFUSION` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  The `datafusion.instances.create` IAM permission was used across projects.  This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Command and Control: DNS Tunneling Temporarily unavailable | `DNS_TUNNELING_IODINE_HANDSHAKE` | [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring#using_logging) | The handshake of the DNS tunneling tool Iodine was detected. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor DNS activity, use [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring#using_logging).  | —  
Defense Evasion: VPC Route Masquerade Attempt | `VPC_ROUTE_MASQUERADE` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  VPC routes masquerading as Google Cloud default routes were manually created, allowing egress traffic to external IP addresses. Findings are classified as **High** severity by default.  | —  
Impact: Billing Disabled Temporarily unavailable | `BILLING_DISABLED_SINGLE_PROJECT` |  **Cloud Audit Logs** :  
[Cloud Billing Admin Activity audit logs](https://docs.cloud.google.com/billing/docs/audit-logging) | Billing was disabled for a project. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor changes to billing, use [Cloud Billing Admin Activity audit logs](https://docs.cloud.google.com/billing/docs/audit-logging).  | —  
Impact: Billing Disabled Temporarily unavailable | `BILLING_DISABLED_MULTIPLE_PROJECTS` |  **Cloud Audit Logs** :  
[Cloud Billing Admin Activity audit logs](https://docs.cloud.google.com/billing/docs/audit-logging) |  Billing was disabled for multiple projects in an organization within a short time period. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor changes to billing, use [Cloud Billing Admin Activity audit logs](https://docs.cloud.google.com/billing/docs/audit-logging).  | —  
Impact: VPC Firewall High Priority Block | `VPC_FIREWALL_HIGH_PRIORITY_BLOCK` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A [VPC firewall rule](https://docs.cloud.google.com/firewall/docs/firewalls) that blocks all egress traffic was added at priority 0. Findings are classified as **Low** severity by default.  | —  
Impact: VPC Firewall Mass Rule DeletionTemporarily unavailable | `VPC_FIREWALL_MASS_RULE_DELETION` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) were mass deleted by non-service accounts.  This rule is temporarily unavailable. To monitor updates to your firewall rules, use the [Cloud audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging). Findings are classified as **Low** severity by default.  | —  
Impact: Service API Disabled | `SERVICE_API_DISABLED` |  **Cloud Audit Logs** :  
[IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  A Google Cloud service API was disabled in a production environment. Findings are classified as **Low** severity by default.  | —  
Impact: Managed Instance Group Autoscaling Set To Maximum Temporarily unavailable | `MIG_AUTOSCALING_SET_TO_MAX` |  **Cloud Audit Logs** :  
[Compute Engine Admin Activity audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging) |  A [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) was configured for maximum autoscaling. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor changes to Compute Engine assets, use [Compute Engine Admin Activity audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging).  | —  
Discovery: Unauthorized Service Account API Call Temporarily unavailable | `UNAUTHORIZED_SERVICE_ACCOUNT_API_CALL` |  **Cloud Audit Logs** :  
[Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) | A service account made an unauthorized cross-project API call. Findings are classified as **Low** severity by default.  This rule is temporarily unavailable. To monitor service account usage, use [Admin Activity audit logs.](https://docs.cloud.google.com/logging/docs/audit#admin-activity) | —  
Defense Evasion: Anonymous Sessions Granted Cluster Admin Access | `ANONYMOUS_SESSIONS_GRANTED_CLUSTER_ADMIN` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  A role-based access control (RBAC) `ClusterRoleBinding` object was created, adding the `root-cluster-admin-binding` behavior to anonymous users. Findings are classified as **Low** severity by default.  | —  
Persistence: New Geography for AI Service | `AI_IAM_ANOMALOUS_BEHAVIOR_IP_GEOLOCATION` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  IAM user and service accounts accessed Google Cloud AI services from anomalous locations, based on the geolocation of the requesting IP addresses.  This finding isn't available for project-level activations and they are classified as **Low** severity by default. | —  
Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Admin Activity  | `AI_ANOMALOUS_SA_DELEGATION_MULTISTEP_ADMIN_ACTIVITY` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  An anomalous multistep [ delegated request](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-delegated) was found for an administrative activity of an AI service. Findings are classified as **Medium** severity by default.  | —  
Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Data Access  | `AI_ANOMALOUS_SA_DELEGATION_MULTISTEP_DATA_ACCESS` |  **Cloud Audit Logs** :  
[Data Access logs](https://docs.cloud.google.com/logging/docs/audit#data-access) |  An anomalous multistep [ delegated request](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-delegated) was found for a data access activity of an AI service. Findings are classified as **Medium** severity by default.  | —  
Privilege Escalation: Anomalous Service Account Impersonator for AI Admin Activity | `AI_ANOMALOUS_SA_DELEGATION_IMPERSONATOR_ADMIN_ACTIVITY` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A potentially anomalous [caller or impersonator](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) in a delegation chain was used for an administrative activity of an AI service. Findings are classified as **Medium** severity by default.  | —  
Privilege Escalation: Anomalous Service Account Impersonator for AI Data Access | `AI_ANOMALOUS_SA_DELEGATION_IMPERSONATOR_DATA_ACCESS` |  **Cloud Audit Logs** :  
[Data Access logs](https://docs.cloud.google.com/logging/docs/audit#data-access) |  A potentially anomalous [caller or impersonator](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) in a delegation chain was used for a data access activity of an AI service. Findings are classified as **Medium** severity by default.  | —  
Privilege Escalation: Anomalous Impersonation of Service Account for AI Admin Activity  | `AI_ANOMALOUS_SA_DELEGATION_IMPERSONATION_OF_SA_ADMIN_ACTIVITY` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A potentially anomalous [impersonated service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) was used for an administrative activity of an AI service. Findings are classified as **Medium** severity by default.  | —  
Persistence: New AI API Method  
| `AI_ANOMALOUS_BEHAVIOR_NEW_API_METHOD` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  IAM service accounts used anomalous access to Google Cloud AI services. Findings are classified as **Low** severity by default. | —  
Initial Access: Dormant Service Account Activity in AI Service | `AI_DORMANT_SERVICE_ACCOUNT_USED_IN_ACTION` |  **Cloud Audit Logs** : [Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A dormant [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) triggered an action in AI services. In this context, a service account is considered dormant if it has been inactive for more than 180 days. Findings are classified as **High** severity by default.  | —  
Initial Access: Anonymous GKE Resource Created from the Internet ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `GKE_RESOURCE_CREATED_ANONYMOUSLY_FROM_INTERNET` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy).  |  A resource was created by [ an effectively anonymous internet user](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac#default-roles-groups). Findings are classified as **High** severity by default.  | —  
Initial Access: GKE Resource Modified Anonymously from the Internet ([Preview](https://cloud.google.com/products/#product-launch-stages))  | `GKE_RESOURCE_MODIFIED_ANONYMOUSLY_FROM_INTERNET` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  A resource was manipulated by [ an effectively anonymous internet user](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac#default-roles-groups). Findings are classified as **High** severity by default.  | —  
Privilege Escalation: Effectively Anonymous Users Granted GKE Cluster Access  | `GKE_ANONYMOUS_USERS_GRANTED_ACCESS` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created an RBAC binding that references one of the following users or groups: 

  * `system:anonymous`
  * `system:unauthenticated`
  * `system:authenticated`

These users and groups are effectively anonymous and should be avoided when creating role bindings or cluster role bindings to any RBAC roles. Review the binding to ensure that it is necessary. If the binding isn't necessary, remove it. Findings are classified as **Medium** severity by default.  | —  
Execution: Suspicious Exec or Attach to a System Pod ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `GKE_SUSPICIOUS_EXEC_ATTACH` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone used the `exec` or `attach` commands to get a shell or execute a command on a container running in the `kube-system` namespace. These methods are sometimes used for legitimate debugging purposes. However, the `kube-system` namespace is intended for system objects created by Kubernetes, and unexpected command execution or shell creation should be reviewed. Findings are classified as **Medium** severity by default.  | —  
Privilege Escalation: Workload Created with a Sensitive Host Path Mount ([Preview](https://cloud.google.com/products/#product-launch-stages))  | `GKE_SENSITIVE_HOSTPATH` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created a workload that contains a `hostPath` volume mount to a sensitive path on the host node's file system. Access to these paths on the host filesystem can be used to access privileged or sensitive information on the node and for container escapes. If possible, don't allow any `hostPath` volumes in your cluster. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: Workload with shareProcessNamespace enabled ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `GKE_SHAREPROCESSNAMESPACE_POD` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone deployed a workload with the `shareProcessNamespace` option set to `true`, allowing all containers to share the same Linux process namespace. This could allow an untrusted or compromised container to escalate privileges by accessing and controlling environment variables, memory, and other sensitive data from processes running in other containers. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: ClusterRole with Privileged Verbs ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `GKE_CLUSTERROLE_PRIVILEGED_VERBS` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created an RBAC `ClusterRole` that contains the `bind`, `escalate`, or `impersonate` verbs. A subject that's bound to a role with these verbs can impersonate other users with higher privileges, bind to additional `Roles` or `ClusterRoles` that contain additional permissions, or modify their own ClusterRole permissions. This might lead to those subjects gaining cluster-admin privileges. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: ClusterRoleBinding to Privileged Role | `GKE_CRB_CLUSTERROLE_AGGREGATION_CONTROLLER` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created an RBAC `ClusterRoleBinding` that references the default `system:controller:clusterrole-aggregation-controller` `ClusterRole`. This default `ClusterRole` has the `escalate` verb, which allows subjects to modify the privileges of their own roles, allowing for privilege escalation. Findings are classified as **Low** severity by default.  | —  
Defense Evasion: Manually Deleted Certificate Signing Request (CSR)  | `GKE_MANUALLY_DELETED_CSR` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone manually deleted a certificate signing request (CSR). CSRs are automatically removed by a garbage collection controller, but malicious actors might manually delete them to evade detection. If the deleted CSR was for an approved and issued certificate, the potentially malicious actor now has an additional authentication method to access the cluster. The permissions associated with the certificate vary depending on which subject they included, but can be highly privileged. Kubernetes does not support certificate revocation. Findings are classified as **Low** severity by default.  | —  
Credential Access: Failed Attempt to Approve Kubernetes Certificate Signing Request (CSR)  | `GKE_APPROVE_CSR_FORBIDDEN` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone attempted to manually approve a certificate signing request (CSR) but the action failed. Creating a certificate for cluster authentication is a common method for attackers to create persistent access to a compromised cluster. The permissions associated with the certificate vary depending on which subject they included, but can be highly privileged. Findings are classified as **Low** severity by default.  | —  
Credential Access: Manually Approved Kubernetes Certificate Signing Request (CSR) ([Preview](https://cloud.google.com/products/#product-launch-stages))  | `GKE_CSR_APPROVED` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone manually approved a certificate signing request (CSR). Creating a certificate for cluster authentication is a common method for attackers to create persistent access to a compromised cluster. The permissions associated with the certificate vary depending on which subject they included, but can be highly privileged. Findings are classified as **Low** severity by default.  | —  
Execution: Kubernetes Pod Created with Potential Reverse Shell Arguments  | `GKE_REVERSE_SHELL_POD` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created a Pod that contains commands or arguments that are commonly associated with a [reverse shell](https://attack.mitre.org/techniques/T1059/). Attackers use reverse shells to expand or maintain their initial access to a cluster and to execute arbitrary commands. Findings are classified as **Medium** severity by default.  | —  
Defense Evasion: Potential Kubernetes Pod Masquerading | `GKE_POD_MASQUERADING` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone deployed a Pod with a naming convention that is similar to the default workloads that GKE creates for regular cluster operation. This technique is called [masquerading](https://attack.mitre.org/techniques/T1036/). Findings are classified as **Medium** severity by default.  | —  
Privilege Escalation: Suspicious Kubernetes Container Names - Exploitation and Escape ([Preview](https://cloud.google.com/products/#product-launch-stages))  | `GKE_SUSPICIOUS_EXPLOIT_POD` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone deployed a Pod with a naming convention that is similar to common tools used for container escapes or to execute other attacks on the cluster. Findings are classified as **Medium** severity by default.  | —  
Persistence: Service Account Created in sensitive namespace  | `GKE_SERVICE_ACCOUNT_CREATION_SENSITIVE_NAMESPACE` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created a service account in a sensitive namespace. The `kube-system` and `kube-public` namespaces are critical for GKE cluster operations, and unauthorized service accounts could compromise cluster stability and security. Findings are classified as **Low** severity by default.  | —  
Impact: Suspicious Kubernetes Container Names - Cryptocurrency Mining Temporarily unavailable | `GKE_SUSPICIOUS_CRYPTOMINING_POD` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone deployed a Pod with a naming convention that is similar to common cryptocurrency coin miners. This may be an attempt by an attacker who has achieved initial access to the cluster to use the cluster's resources for cryptocurrency mining. Findings are classified as **High** severity by default.  This rule is temporarily unavailable. To monitor Kubernetes activity, use [ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy).  | —  
Execution: Workload triggered in sensitive namespace | `GKE_SENSITIVE_NAMESPACE_WORKLOAD_TRIGGERED` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone deployed a workload (for example, a Pod or Deployment) in the `kube-system` or `kube-public` namespaces. These namespaces are critical for GKE cluster operations, and unauthorized workloads could compromise cluster stability or security. Findings are classified as **Low** severity by default.  | —  
Execution: GKE launch excessively capable container ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `GKE_EXCESSIVELY_CAPABLE_CONTAINER_CREATED` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created a container with one or more of the following capabilities in a cluster with an elevated security context: 

  * `CAP_SYS_MODULE`
  * `CAP_SYS_RAWIO`
  * `CAP_SYS_PTRACE`
  * `CAP_SYS_BOOT`
  * `CAP_DAC_READ_SEARCH`
  * `CAP_NET_ADMIN`
  * `CAP_BPF`

These capabilities can be used to escape from containers. Use caution when provisioning these capabilities. Findings are classified as **Low** severity by default.  | —  
Persistence: GKE Webhook Configuration Detected | `GKE_WEBHOOK_CONFIG_CREATED` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  A webhook configuration was detected in your GKE cluster. Webhooks can intercept and modify Kubernetes API requests, potentially allowing attackers to persist within your cluster or manipulate resources. Findings are classified as **Low** severity by default.  | —  
Defense Evasion: Static Pod Created | `GKE_STATIC_POD_CREATED` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created a static Pod in your GKE cluster. Static Pods run directly on the node and bypass the Kubernetes API server, which makes them more difficult to monitor and control. Attackers can use static Pods to evade detection or maintain persistence. Findings are classified as **Low** severity by default.  | —  
Initial Access: Successful API call made from a TOR proxy IP | `GKE_TOR_PROXY_IP_REQUEST` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  A successful API call was made to your GKE cluster from an IP address associated with the Tor network. Tor provides anonymity, which attackers often exploit to hide their identity. Findings are classified as **High** severity by default.  |  Category: `Initial Access: Successful API call made from a TOR proxy IP Affecting Sensitive Data`  
Severity: No change (default High)   
Initial Access: GKE NodePort service created | `GKE_NODEPORT_SERVICE_CREATED` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone created a NodePort service. NodePort services expose Pods directly on a node's IP address and static port, which make the Pods accessible from outside the cluster. This can introduce a significant security risk because it could allow an attacker to exploit vulnerabilities in the exposed service to gain access to the cluster or sensitive data. Findings are classified as **Medium** severity by default.  | —  
Impact: GKE kube-dns modification detected ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `GKE_KUBE_DNS_MODIFICATION` |  **Cloud Audit Logs** :  
[ GKE Admin Activity logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Someone modified the kube-dns configuration in your GKE cluster. GKE kube-dns is a critical component of your cluster's networking, and its misconfiguration could lead to a security breach. Findings are classified as **Medium** severity by default.  | —  
Impact: Cryptomining Commands | `CLOUD_RUN_JOBS_CRYPTOMINING_COMMANDS` |  **Cloud Audit Logs** :  
[ IAM System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event) |  Specific cryptomining commands were attached to a Cloud Run job during execution. Findings are classified as **High** severity by default.  | —  
Execution: Cryptomining Docker Image | `CLOUD_RUN_CRYPTOMINING_DOCKER_IMAGES` |  **Cloud Audit Logs** :  
[ IAM System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event) |  Specific known bad docker images were attached to a new or existing Cloud Run service or job. Findings are classified as **High** severity by default.  | —  
Privilege Escalation: Default Compute Engine Service Account SetIAMPolicy | `CLOUD_RUN_SERVICES_SET_IAM_POLICY` |  **Cloud Audit Logs** :  
[Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  The default Compute Engine service account was used to set the IAM policy for a Cloud Run service. This is a potential post exploit action when a Compute Engine token is compromised from a serverless service. Findings are classified as **Low** severity by default.  | —  
Initial Access: CloudDB Successful login from Anonymizing Proxy IP | `CLOUD_DB_LOGIN_SUCCEEDED_ANON_IP` |  **Cloud Audit Logs** : [AlloyDB for PostgreSQL data access logs](https://docs.cloud.google.com/alloydb/docs/audit-logging)  
[ Cloud SQL for PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[Cloud SQL for MySQL data access logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
**Note** : You must enable IP logging in PostgreSQL to use this rule for AlloyDB and Postgres.  |  A successful login was detected in your database instance from a known anonymizing IP address. This could indicate an attacker gaining initial access to your instance. Findings are classified as **High** severity by default.  | —  
Credential Access: CloudDB Failed login from Anonymizing Proxy IP | `CLOUD_DB_LOGIN_FAILED_ANON_IP` |  **Cloud Audit Logs** : [AlloyDB for PostgreSQL data access logs](https://docs.cloud.google.com/alloydb/docs/audit-logging)  
[ Cloud SQL for PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[Cloud SQL for MySQL data access logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
**Note** : You must enable IP logging in PostgreSQL to use this rule for AlloyDB and Postgres.  |  A failed login was detected in your database instance from a known anonymizing IP address. This could indicate an attacker attempting unauthorized access to your instance. Findings are classified as **Medium** severity by default.  | —  
  
For deprecated and shut down rules, see [Deprecations](https://docs.cloud.google.com/security-command-center/docs/deprecations). 

### Custom modules for Event Threat Detection

In addition to built-in detection rules, Event Threat Detection provides module templates that you can use to create custom detection rules. For more information, see [Overview of custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview).

To create detection rules for which no custom module templates are available, you can [export your log data to BigQuery](https://docs.cloud.google.com/logging/docs/export/bigquery), and then run unique or recurring SQL queries that capture your threat models.

### Unsafe Google Group changes

This section explains how Event Threat Detection uses Google Workspace logs, Cloud Audit Logs, and IAM policies to detect unsafe Google Groups changes. Detecting Google Groups changes is only supported when you activate Security Command Center at the organization level.

Google Cloud customers can use [Google groups](https://docs.cloud.google.com/iam/docs/groups-best-practices) to manage roles and permissions for members in their organizations, or apply access policies to collections of users. Instead of granting roles directly to members, administrators can grant roles and permissions to Google Groups, and then add members to specific groups. Group members inherit all of a group's roles and permissions, which lets members access specific resources and services.

While Google Groups are a convenient way to manage access control at scale, they can pose a risk if external users from outside your organization or domain are added to _privileged_ groups—groups that are granted sensitive roles or permissions. Sensitive roles control access to security and network settings, logs, and personally identifiable information (PII), and are not recommended for external group members.

In large organizations, administrators might not be aware when external members are added to privileged groups. Cloud Audit Logs record role grants to groups, but those log events don't contain information on group members, which can obscure the potential impact of some group changes.

If you [share your Google Workspace logs](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs#view_logs_in_console) with Google Cloud, Event Threat Detection monitors your logging streams for new members added to your organization's Google Groups. Because the logs are at the organization level, Event Threat Detection can scan Google Workspace logs only when you activate Security Command Center at the organization level. Event Threat Detection can't scan these logs when you activate Security Command Center at the project level.

Event Threat Detection identifies external group members and, using Cloud Audit Logs, reviews each affected group's IAM roles to check whether the groups are granted sensitive roles. That information is used to detect the following unsafe changes for privileged Google Groups:

  * External group members added to privileged groups
  * Sensitive roles or permissions granted to groups with external group members
  * Privileged groups that are changed to allow anyone in the general public to join



Event Threat Detection writes findings to Security Command Center. Findings contain the email addresses of newly added external members, internal group members that initiate events, group names, and the sensitive roles associated with groups. You can use the information to remove external members from groups or revoke sensitive roles granted to groups.

For more information on Event Threat Detection findings, see Event Threat Detection rules.

### Sensitive IAM roles and permissions

This section explains how Event Threat Detection defines sensitive IAM roles. For sensitive roles and permissions for AI threats, see Sensitive IAM roles and permissions for AI.

Detections like IAM Anomalous Grant and Unsafe Google Group changes generate findings only if changes involve high- or medium-sensitivity roles. The sensitivity of roles impacts the severity rating assigned to findings.

  * High-sensitivity roles control critical services in organizations, including billing, firewall settings, and logging. Findings that match these roles are classified as **High** severity.
  * Medium-sensitivity roles have editing permissions that let principals make changes to Google Cloud resources; and viewing and executing permissions on data storage services that often hold sensitive data. The severity assigned to findings depends on the resource: 
    * If medium-sensitivity roles are granted at the organization level, findings are classified as **High** severity.
    * If medium-sensitivity roles are granted at lower levels in your resource hierarchy (folders, projects, and buckets, among others), findings are classified as **Medium** severity.



Granting these sensitive roles is considered dangerous if the grantee is an _External Member_ or an abnormal identity, like a principal that has been inactive for a long time.

Granting sensitive roles to external members creates a potential threat because they can be abused for account compromise and data exfiltration.

Finding categories that use these sensitive roles include:

  * Persistence: IAM Anomalous Grant 
    * Subrule: `external_service_account_added_to_policy`
    * Subrule: `external_member_added_to_policy`
  * Privilege Escalation: Sensitive Role Granted To Hybrid Group
  * Privilege Escalation: Dormant Service Account Granted Sensitive Role



Finding categories that use a subset of the sensitive roles include:

  * Persistence: IAM Anomalous Grant 
    * Subrule: `service_account_granted_sensitive_role_to_member`



The `service_account_granted_sensitive_role_to_member` subrule targets both external and internal members generally and therefore uses only a subset of sensitive roles, as explained in Event Threat Detection rules.

Category | Role | Description  
---|---|---  
**Basic roles** : contain thousands of permissions across all Google Cloud services.  | `roles/owner` |  [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic)  
`roles/editor`  
**Security roles** : control access to security settings  | `roles/cloudkms.*` |  All [ Cloud Key Management Service roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles)  
`roles/cloudsecurityscanner.*` |  All [ Web Security Scanner roles](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)  
`roles/dlp.*` |  All [Sensitive Data Protection roles](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles)  
`roles/iam.*` |  All [ IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions/iam)  
`roles/secretmanager.*` |  All [ Secret Manager roles](https://docs.cloud.google.com/secret-manager/docs/access-control)  
`roles/securitycenter.*` |  All [Security Command Center roles](https://docs.cloud.google.com/security-command-center/docs/access-control)  
**Logging roles** : control access to an organization's logs  | `roles/errorreporting.*` |  All [Error Reporting roles](https://docs.cloud.google.com/error-reporting/docs/iam)  
`roles/logging.*` |  All [Cloud Logging roles](https://docs.cloud.google.com/logging/docs/access-control)  
`roles/stackdriver.*` |  All [Cloud Monitoring roles](https://docs.cloud.google.com/monitoring/access-control)  
**Personal information roles** : control access to resources that contain personally identifiable information, including banking and contact information  | `roles/billing.*` |  All [Cloud Billing roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access)  
`roles/healthcare.*` |  All [ Cloud Healthcare API roles](https://docs.cloud.google.com/healthcare-api/docs/concepts/access-control)  
`roles/essentialcontacts.*` |  All [ Essential Contacts roles](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts)  
**Networking roles** : control access to an organization's network settings  | `roles/dns.*` | All [Cloud DNS roles](https://docs.cloud.google.com/dns/docs/access-control)  
`roles/domains.*` |  All [Cloud Domains roles](https://docs.cloud.google.com/domains/docs/access-control)  
`roles/networkconnectivity.*` |  All [ Network Connectivity Center roles](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control)  
`roles/networkmanagement.*` |  All [ NCC roles](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control)  
`roles/privateca.*` |  All [ Certificate Authority Service roles](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles)  
**Service roles** : control access to service resources in Google Cloud  | `roles/cloudasset.*` |  All [ Cloud Asset Inventory roles](https://docs.cloud.google.com/asset-inventory/docs/access-control#permissions)  
`roles/servicedirectory.*` |  All [ Service Directory roles](https://docs.cloud.google.com/service-directory/docs/access-control)  
`roles/servicemanagement.*` |  All [ Service Management roles](https://docs.cloud.google.com/service-infrastructure/docs/service-management/access-control)  
`roles/servicenetworking.*` |  All [ Service Networking roles](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking)  
`roles/serviceusage.*` |  All [Service Usage roles](https://docs.cloud.google.com/service-usage/docs/access-control)  
**Compute Engine roles** : control access to Compute Engine virtual machines, which carry long-running jobs and are associated with firewall rules  |  `roles/compute.admin` `roles/compute.instanceAdmin` `roles/compute.instanceAdmin.v1` `roles/compute.loadBalancerAdmin` `roles/compute.networkAdmin` `roles/compute.orgFirewallPolicyAdmin` `roles/compute.orgFirewallPolicyUser` `roles/compute.orgSecurityPolicyAdmin` `roles/compute.orgSecurityPolicyUser` `roles/compute.orgSecurityResourceAdmin` `roles/compute.osAdminLogin` `roles/compute.publicIpAdmin` `roles/compute.securityAdmin` `roles/compute.storageAdmin` `roles/compute.xpnAdmin` |  All [Compute Engine](https://docs.cloud.google.com/compute/docs/access/iam) **Admin** and **Editor** roles   
Category | Role | Description  
---|---|---  
**Editing roles** : IAM roles that include permissions to make changes to Google Cloud resources  |  Examples: `roles/storage.objectAdmin` `roles/file.editor` `roles/source.writer` `roles/container.developer` |  Role names usually end with titles like **Admin** , **Owner** , **Editor** , or **Writer**.  Expand the node in the last row of the table to see  All medium-sensitivity roles  
**Data storage roles** : IAM roles that include permissions to view and execute data storage services  |  Examples: `roles/cloudsql.viewer` `roles/cloudsql.client` `roles/bigquery.dataViewer` `roles/bigquery.user` `roles/spanner.databaseReader` `roles/spanner.databaseUser` | Expand the node in the last row of the table to see All medium-sensitivity roles  
All medium-sensitivity roles [ Access Approval](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval)

  * `roles/accessapproval.approver`
  * `roles/accessapproval.configEditor`

[ Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/access-control)

  * `roles/accesscontextmanager.gcpAccessAdmin`
  * `roles/accesscontextmanager.policyAdmin`
  * `roles/accesscontextmanager.policyEditor`

[ Actions](https://docs.cloud.google.com/iam/docs/roles-permissions/actions)

  * `roles/actions.Admin`

[ AI Platform](https://docs.cloud.google.com/iam/docs/roles-permissions/ml)

  * `roles/ml.admin`
  * `roles/ml.developer`
  * `roles/ml.jobOwner`
  * `roles/ml.modelOwner`
  * `roles/ml.modelUser`

[ API Gateway](https://docs.cloud.google.com/api-gateway/docs/api-access-overview)

  * `roles/apigateway.admin`

[App Engine](https://docs.cloud.google.com/appengine/docs/standard/python/roles)

  * `roles/appengine.appAdmin`
  * `roles/appengine.appCreator`
  * `roles/appengine.serviceAdmin`

[ Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control)

  * `roles/containeranalysis.admin`
  * `roles/containeranalysis.notes.attacher`
  * `roles/containeranalysis.notes.editor`
  * `roles/containeranalysis.occurrences.editor`

[ AutoML](https://docs.cloud.google.com/iam/docs/roles-permissions/automl)

  * `roles/automl.admin`
  * `roles/automl.editor`

[ BigQuery](https://docs.cloud.google.com/bigquery/docs/access-control)

  * `roles/bigquery.admin`
  * `roles/bigquery.dataEditor`
  * `roles/bigquery.dataOwner`
  * `roles/bigquery.dataViewer`
  * `roles/bigquery.resourceAdmin`
  * `roles/bigquery.resourceEditor`
  * `roles/bigquery.resourceViewer`
  * `roles/bigquery.user`

[Bigtable](https://docs.cloud.google.com/bigtable/docs/access-control)

  * `roles/bigtable.admin`
  * `roles/bigtable.reader`
  * `roles/bigtable.user`

[ Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/reference/permissions-and-roles)

  * `roles/binaryauthorization.attestorsAdmin`
  * `roles/binaryauthorization.attestorsEditor`
  * `roles/binaryauthorization.policyAdmin`
  * `roles/binaryauthorization.policyEditor`

[Cloud Autoscaling](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling)

  * `roles/autoscaling.metricsWriter`
  * `roles/autoscaling.sitesAdmin`
  * `roles/autoscaling.stateWriter`

[Cloud Build](https://docs.cloud.google.com/build/docs/iam-roles-permissions)

  * `roles/cloudbuild.builds.builder`
  * `roles/cloudbuild.builds.editor`

[ Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/access-control)

  * `roles/deploymentmanager.editor`
  * `roles/deploymentmanager.typeEditor`

[ Cloud Endpoints](https://docs.cloud.google.com/iam/docs/roles-permissions/endpoints)

  * `roles/endpoints.portalAdmin`Beta

[Cloud Monitoring](https://docs.cloud.google.com/monitoring/access-control)

  * `roles/monitoring.admin`
  * `roles/monitoring.alertPolicyEditor`
  * `roles/monitoring.dashboardEditor`
  * `roles/monitoring.editor`
  * `roles/monitoring.metricWriter`
  * `roles/monitoring.notificationChannelEditor`
  * `roles/monitoring.servicesEditor`
  * `roles/monitoring.uptimeCheckConfigEditor`

[ Cloud Run](https://docs.cloud.google.com/run/docs/securing/managing-access)

  * `roles/run.admin`
  * `roles/run.developer`

[ Cloud Run functions](https://docs.cloud.google.com/functions/docs/reference/iam/roles)

  * `roles/cloudfunctions.admin`
  * `roles/cloudfunctions.developer`
  * `roles/cloudfunctions.invoker`

[Cloud Runtime Configuration API](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig)

  * `roles/runtimeconfig.admin`

[ Cloud Scheduler](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudscheduler)

  * `roles/cloudscheduler.admin`

[ Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs/configure-access-control)

  * `roles/source.admin`
  * `roles/source.writer`

[Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions)

  * `roles/cloudsql.admin`
  * `roles/cloudsql.editor`
  * `roles/cloudsql.client`
  * `roles/cloudsql.instanceUser`
  * `roles/cloudsql.viewer`

[ Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

  * `roles/storage.admin`
  * `roles/storage.hmacKeyAdmin`
  * `roles/storage.objectAdmin`
  * `roles/storage.objectCreator`
  * `roles/storage.objectViewer`
  * `roles/storage.legacyBucketOwner`
  * `roles/storage.legacyBucketWriter`
  * `roles/storage.legacyBucketReader`
  * `roles/storage.legacyObjectOwner`
  * `roles/storage.legacyObjectReader`

[ Cloud Tasks](https://docs.cloud.google.com/tasks/docs/reference-access-control)

  * `roles/cloudtasks.admin`
  * `roles/cloudtasks.enqueuer`
  * `roles/cloudtasks.queueAdmin`
  * `roles/cloudtasks.taskDeleter`

[ Cloud TPU](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu)

  * `tpu.admin`

[Cloud Trace](https://docs.cloud.google.com/tasks/docs/reference-access-control)

  * `roles/cloudtrace.admin`
  * `roles/cloudtrace.agent`

[Compute Engine](https://docs.cloud.google.com/compute/docs/access/iam)

  * `roles/compute.imageUser`
  * `roles/compute.osLoginExternalUser`
  * `roles/osconfig.guestPolicyAdmin`
  * `roles/osconfig.guestPolicyEditor`
  * `roles/osconfig.osPolicyAssignmentAdmin`
  * `roles/osconfig.osPolicyAssignmentEditor`
  * `roles/osconfig.patchDeploymentAdmin`

[Customer Usage Data Processing](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing)

  * `roles/dataprocessing.admin`

[Data Catalog](https://docs.cloud.google.com/data-catalog/docs/concepts/iam)

  * `roles/datacatalog.admin`
  * `roles/datacatalog.categoryAdmin`
  * `roles/datacatalog.entryGroupCreator`
  * `roles/datacatalog.entryGroupOwner`
  * `roles/datacatalog.entryOwner`

[ Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/access-control)

  * `roles/dataflow.admin`
  * `roles/dataflow.developer`

[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/iam/iam)

  * `roles/dataproc.admin`
  * `roles/dataproc.editor`

[ Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/iam-roles)

  * `roles/metastore.admin`
  * `roles/metastore.editor`

[Datastore](https://docs.cloud.google.com/datastore/docs/access/iam)

  * `roles/datastore.importExportAdmin`
  * `roles/datastore.indexAdmin`
  * `roles/datastore.owner`
  * `roles/datastore.user`

[Eventarc](https://docs.cloud.google.com/eventarc/docs/roles-permissions)

  * `roles/eventarc.admin`
  * `roles/eventarc.developer`
  * `roles/eventarc.eventReceiver`

[ Filestore](https://docs.cloud.google.com/iam/docs/roles-permissions/endpoints)

  * `roles/file.editor`

[ Firebase](https://firebase.google.com/docs/projects/iam/roles)

  * `roles/firebase.admin`
  * `roles/firebase.analyticsAdmin`
  * `roles/firebase.developAdmin`
  * `roles/firebase.growthAdmin`
  * `roles/firebase.qualityAdmin`
  * `roles/firebaseabt.admin`
  * `roles/firebaseappcheck.admin`
  * `roles/firebaseappdistro.admin`
  * `roles/firebaseauth.admin`
  * `roles/firebasecrash.symbolMappingsAdmin`
  * `roles/firebasecrashlytics.admin`
  * `roles/firebasedatabase.admin`
  * `roles/firebasedynamiclinks.admin`
  * `roles/firebasehosting.admin`
  * `roles/firebaseinappmessaging.admin`
  * `roles/firebaseml.admin`
  * `roles/firebasenotifications.admin`
  * `roles/firebaseperformance.admin`
  * `roles/firebasepredictions.admin`
  * `roles/firebaserules.admin`
  * `roles/firebasestorage.admin`
  * `roles/cloudconfig.admin`
  * `roles/cloudtestservice.testAdmin`

[Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/iam)

  * `vmwareengine.vmwareengineAdmin`

[ Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#roles)

  * `roles/container.admin`
  * `roles/container.clusterAdmin`
  * `roles/container.developer`

[ Google Kubernetes Engine Hub](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke)

  * `roles/gkehub.admin`
  * `roles/gkehub.gatewayAdmin`
  * `roles/gkehub.connect`

[Google Security Operations Service Management](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm)

  * `roles/chroniclesm.admin`

[ Google Workspace](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons)

  * `roles/gsuiteaddons.developer`

[Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/managing-access)

  * `roles/iap.admin`
  * `roles/iap.settingsAdmin`

[Identity Platform](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform)

  * `roles/identityplatform.admin`

[Identity Toolkit](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit)

  * `roles/identitytoolkit.admin`

[ Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/access-control)

  * `roles/managedidentities.admin`
  * `roles/managedidentities.domainAdmin`
  * `roles/managedidentities.viewer`

[ Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/access-control)

  * `roles/redis.admin`
  * `roles/redis.editor`

[OAuthConfig](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig)

  * `roles/oauthconfig.editor`

[ On-Demand Scanning API](https://docs.cloud.google.com/iam/docs/roles-permissions/ondemandscanning)

  * `roles/ondemandscanning.admin`

[ Ops Config Monitoring](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring)

  * `roles/opsconfigmonitoring.resourceMetadata.writer`

[ Organization Policy Service](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy)

  * `roles/axt.admin`
  * `roles/orgpolicy.policyAdmin`

[ Proximity Beacon](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon)

  * `roles/proximitybeacon.attachmentEditor`
  * `roles/proximitybeacon.beaconEditor`

[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/access-control)

  * `roles/pubsub.admin`
  * `roles/pubsub.editor`

[ Pub/Sub Lite](https://docs.cloud.google.com/pubsub/lite/docs/access-control)

  * `roles/pubsublite.admin`
  * `roles/pubsublite.editor`
  * `roles/pubsublite.publisher`

[ reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/access-control)

  * `roles/recaptchaenterprise.admin`
  * `roles/recaptchaenterprise.agent`

[ Recommendations](https://docs.cloud.google.com/retail/docs/iam#roles)

  * `roles/automlrecommendations.admin`
  * `roles/automlrecommendations.editor`

[ Recommender](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender)

  * `roles/recommender.billingAccountCudAdmin`
  * `roles/recommender.cloudAssetInsightsAdmin`
  * `roles/recommender.cloudsqlAdmin`
  * `roles/recommender.computeAdmin`
  * `roles/recommender.firewallAdmin`
  * `roles/recommender.iamAdmin`
  * `roles/recommender.productSuggestionAdmin`
  * `roles/recommender.projectCudAdmin`

[ Resource Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager)

  * `roles/resourcemanager.folderAdmin`
  * `roles/resourcemanager.folderCreator`
  * `roles/resourcemanager.folderEditor`
  * `roles/resourcemanager.folderIamAdmin`
  * `roles/resourcemanager.folderMover`
  * `roles/resourcemanager.lienModifier`
  * `roles/resourcemanager.organizationAdmin`
  * `roles/resourcemanager.projectCreator`
  * `roles/resourcemanager.projectDeleter`
  * `roles/resourcemanager.projectIamAdmin`
  * `roles/resourcemanager.projectMover`
  * `roles/resourcemanager.tagAdmin`

[ Resource Settings](https://docs.cloud.google.com/resource-manager/docs/resource-settings/manage-resource-settings#required-permissions)

  * `roles/resourcesettings.admin`

[AI Commerce Search API](https://docs.cloud.google.com/iam/docs/roles-permissions/retail)

  * `roles/retail.admin`
  * `roles/retail.editor`

[ Serverless VPC Access](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess)

  * `roles/vpcaccess.admin`

[ Service Consumer Management](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement)

  * `roles/serviceconsumermanagement.tenancyUnitsAdmin`

[Spanner](https://docs.cloud.google.com/spanner/docs/iam)

  * `roles/spanner.admin`
  * `roles/spanner.backupAdmin`
  * `roles/spanner.backupWriter`
  * `roles/spanner.databaseAdmin`
  * `roles/spanner.restoreAdmin`
  * `roles/spanner.databaseReader`
  * `roles/spanner.databaseUser`

[ Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview#permissions_and_role_requirements_for)

  * `roles/storagetransfer.admin`
  * `roles/storagetransfer.user`

[ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/general/access-control)

  * `roles/aiplatform.admin`
  * `roles/aiplatform.featurestoreAdmin`
  * `roles/aiplatform.migrator`
  * `roles/aiplatform.user`

[ Vertex AI Workbench user-managed notebooks](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/iam)

  * `roles/notebooks.admin`
  * `roles/notebooks.legacyAdmin`

[Workflows](https://docs.cloud.google.com/workflows/docs/access-control)

  * `roles/workflows.admin`
  * `roles/workflows.editor`

  
  
### Sensitive IAM roles and permissions for AI

For Event Threat Detection findings related to [AI threats](https://docs.cloud.google.com/security-command-center/docs/ai-threats), sensitive roles are defined differently compared to sensitive roles for non-AI threats.

  * High-sensitivity roles for AI findings include the following [basic](https://docs.cloud.google.com/iam/docs/roles-overview#basic), [legacy basic](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic), and [predefined](https://docs.cloud.google.com/iam/docs/roles-overview#predefined) roles:

    * `roles/admin`
    * `roles/writer`
    * `roles/owner`
    * `roles/editor`
    * `roles/resourcemanager.organizationAdmin`
    * `roles/iam.securityAdmin`
  * Medium-sensitivity roles for AI findings include all administrator, editor, owner, and service agent roles for any Google Cloud service. The following roles are also considered medium-sensitivity roles:

    * `roles/cloudkms.cryptoKeyDecrypter`
    * `roles/compute.osAdminLogin`
    * `roles/compute.osLogin`
    * `roles/iam.serviceAccountTokenCreator`
    * `roles/iam.serviceAccountUser`
    * `roles/logging.configWriter`
    * `roles/logging.privateLogViewer`
    * `roles/secretmanager.secretAccessor`
  * Low-sensitivity roles for AI findings include the following:

    * `roles/cloudfunctions.developer`
    * `roles/run.developer`
    * `roles/appengine.deployer`
    * `roles/iam.workloadIdentityUser`
    * `roles/iam.serviceAccountOpenIdTokenCreator`
    * `roles/artifactregistry.createOnPushWriter`



Sensitive AI permissions include those that allow creating, updating, deleting, or exporting AI models and data, managing access control to AI services (for example, `setIamPolicy`), and utilizing AI capabilities such as making predictions. This also includes permissions to manage sensitive credentials, such as Storage HMAC keys, which are often used in conjunction with AI workloads.

## Log types and activation requirements

This section lists the logs that Event Threat Detection uses, along with the threats that Event Threat Detection looks for in each log, and what, if anything, you need to do to turn on each log.

You need to turn a log on for Event Threat Detection only if all of the following are true:

  * You are using the product or service that writes to the log.
  * You need to protect the product or service against the threats that Event Threat Detection detects in the log.
  * The log is a data access audit log or other log that is off by default.



Certain threats can be detected in multiple logs. If Event Threat Detection can detect a threat in a log that is already turned on, you don't need to turn on another log to detect that same threat.

If a log isn't listed in this section, Event Threat Detection does not scan it, even if it is turned on. For more information, see Potentially redundant log scans.

As described in the following table, some log types are only available at the organization level. If you activate Security Command Center at the project level, Event Threat Detection doesn't scan these logs and doesn't produce any findings.

**Tip:** To help you evaluate which logs to export and analyze to meet your security and compliance needs, use Google Cloud's [Log Scoping Tool](https://docs.cloud.google.com/architecture/exporting-stackdriver-logging-for-security-and-access-analytics#log_scoping_tool).

### Foundational log sources

Event Threat Detection uses foundational data sources to detect potentially malicious activities in your network.

  * If you enable Event Threat Detection _without_ VPC Flow Logs, Event Threat Detection immediately starts analyzing an independent, duplicate, and internal stream of VPC Flow Logs. To further investigate an existing Event Threat Detection finding, you need to enable VPC Flow Logs and manually navigate to Logs Explorer and Flow Analyzer. If you enable VPC Flow Logs at a later date, only future findings will contain the relevant links for further investigation.

  * If you enable Event Threat Detection _with_ VPC Flow Logs, Event Threat Detection immediately starts analyzing the VPC Flow Logs in your deployment and provides links to Logs Explorer and Flow Analyzer to help you investigate further.




### Logs for network detection of malware

Event Threat Detection can provide network detection of malware by scanning any one of the following logs:

  * Cloud DNS logging
  * Cloud NAT logging
  * Firewall Rules Logging
  * VPC Flow Logs



You don't need to enable more than one of Cloud NAT logging, Firewall Rules Logging, or VPC Flow Logs.

If you are already using Cloud DNS logging, Event Threat Detection can detect malware using domain resolution. For most users, the Cloud DNS logs are sufficient for the network detection of malware.

If you need another level of visibility beyond domain resolution, you can turn on VPC Flow Logs, but VPC Flow Logs can incur costs. To manage these costs, we recommend increasing the aggregation interval to 15 minutes and reducing the sample rate to between 5% and 10%, but there is a tradeoff between recall (higher sample) and cost management (lower sample rate). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).

If you are already using Firewall Rules Logging or Cloud NAT logging, these logs are useful in place of VPC Flow Logs.

### Supported log data and threats detected

This section lists the Cloud Logging and Google Workspace logs that you can turn on or otherwise configure to increase the number of threats that Event Threat Detection can detect.

Certain threats, such as threats posed by the anomalous impersonation or delegation of a service account, can be found in most audit logs. For these types of threats, you determine which logs you need to turn on based on the products and services you are using.

**Logging costs** : Before you turn on a log for Event Threat Detection to scan, make sure you understand how Cloud Logging charges for the log data. After turning on a log, monitor the log for a couple of days to ensure that the log doesn't incur any unexpected Logging costs. 

Although the scanning of logs by Event Threat Detection does not incur any additional costs, depending on the volume of log data that your organizations and projects produce, Cloud Logging may charge you for the ingestion and storage of the log data. 

For information about how Logging charges for logging, see [Cloud Logging pricing](https://docs.cloud.google.com/stackdriver/pricing#logging-costs). 

The following table shows specific logs you can enable and the type of threats that can be detected.

Log type | Threats detected | Configuration required  
---|---|---  
[ AlloyDB for PostgreSQL Data Access audit logs](https://docs.cloud.google.com/alloydb/docs/audit-logging) |  Credential Access: CloudDB Failed login from Anonymizing Proxy IP Initial Access: CloudDB Successful login from Anonymizing Proxy IP Privilege Escalation: AlloyDB Database Superuser Writes to User Tables Privilege Escalation: AlloyDB Over-Privileged Grant | 

  * [ Activate Logging Data Access audit logs for AlloyDB for PostgreSQL](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)
  * To detect the Privilege Escalation: AlloyDB Database Superuser Writes to User Tables and Privilege Escalation: AlloyDB Over-Privileged Grant threats, you must also enable the [pgAudit extension](https://docs.cloud.google.com/alloydb/docs/pgaudit/enable-audit)

  
[ authlogs/authlog on virtual machines](https://docs.cloud.google.com/logging/docs/view/query-library#gce-filters) | Brute force SSH |  Install the [Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-index) or the legacy [Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/install-index) on your VM hosts   
[Cloud DNS logging](https://docs.cloud.google.com/dns/docs/monitoring) |  Log4j Malware: Bad Domain Malware: bad domain Malware: Cryptomining Bad Domain |  [ Turn on Cloud DNS logging See also Logs for network detection of malware.](https://docs.cloud.google.com/dns/docs/monitoring#using_logging)  
[ Cloud SQL MySQL Data Access audit logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging) |  Credential Access: CloudDB Failed login from Anonymizing Proxy IP Exfiltration: Cloud SQL Data Exfiltration Exfiltration: AI Agent Initiated Cloud SQL Exfiltration to Public Bucket Exfiltration: AI Agent Initiated Cloud SQL Exfiltration to External Bucket Initial Access: CloudDB Successful login from Anonymizing Proxy IP |  [ Activate Logging Data Access audit logs for Cloud SQL for MySQL](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)  
[Cloud NAT logging](https://docs.cloud.google.com/nat/docs/monitoring) |  Log4j Malware: Bad IP Malware: bad IP Malware: Cryptomining Bad IP |  [ Turn on Cloud NAT logging](https://docs.cloud.google.com/nat/docs/monitoring#configuring_logging) See also Logs for network detection of malware.  
[ Cloud SQL PostgreSQL Data Access audit logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging) |  Credential Access: CloudDB Failed login from Anonymizing Proxy IP Exfiltration: Cloud SQL Data Exfiltration Exfiltration: AI Agent Initiated Cloud SQL Exfiltration to Public Bucket Exfiltration: AI Agent Initiated Cloud SQL Exfiltration to External Bucket Exfiltration: Cloud SQL Over-Privileged Grant Initial Access: CloudDB Successful login from Anonymizing Proxy IP | 

  * [ Activate Logging Data Access audit logs for Cloud SQL for PostgreSQL.](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)
  * To detect the Exfiltration: Cloud SQL Over-Privileged Grant threat, you must also enable the [pgAudit extension](https://docs.cloud.google.com/sql/docs/postgres/pg-audit)

  
[ External Application Load Balancer backend service logs](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring) | Initial Access: Log4j Compromise Attempt |  [ Turn on external Application Load Balancer logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring)  
[ Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) |  Log4j Malware: Bad IP Malware: bad IP Malware: Cryptomining Bad IP |  [ Turn on Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging) See also Logs for network detection of malware.  
[ Generic Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) |  Initial Access: Leaked Service Account Key Used Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Data Access Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access Privilege Escalation: Anomalous Service Account Impersonator for AI Data Access Privilege Escalation: Anomalous Service Account Impersonator for Data Access |  [ Activate Logging Data Access audit logs.](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)  
[ Google Kubernetes Engine (GKE) Data Access audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) |  Discovery: Can get sensitive Kubernetes object check  Privilege Escalation: Get Kubernetes CSR with compromised bootstrap credentials |  [ Activate Logging Data Access audit logs for GKE](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)  
[ Google Workspace Admin Audit logs](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging) |  Persistence: SSO Enablement Toggle Persistence: SSO Settings Changed Persistence: Strong Authentication Disabled Persistence: Two Step Verification Disabled Privilege Escalation: Privileged Group Opened To Public |  [ Share Google Workspace Admin Audit logs with Cloud Logging](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs#share_audit_logs) This log type can't be scanned in project-level activations.  
[ Google Workspace Login Audit logs](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging) |  Credential Access: External Member Added To Privileged Group Initial Access: Account Disabled Hijacked Initial Access: Disabled Password Leak Initial Access: Government Based Attack Initial Access: Suspicious Login Blocked Persistence: Two Step Verification Disabled |  [ Share Google Workspace Login Audit logs with Cloud Logging](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs#share_audit_logs) This log type can't be scanned in project-level activations.  
[ IAM Data Access audit logs](https://docs.cloud.google.com/resource-manager/docs/audit-logging) |  Discovery: AI Agent Service Account Self-Investigation Discovery: Service Account Self-Investigation Privilege Escalation: AI Agent Cross-Project Access Token Generation Privilege Escalation: AI Agent Cross-Project OpenID Token Generation Privilege Escalation: AI Agent Token Generation Using Implicit Delegation Privilege Escalation: AI Agent Token Generation Using signJwt |  [ Activate Logging Data Access audit logs for Resource Manager](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)  
[ SQL Server Data Access audit logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging) | Exfiltration: Cloud SQL Data Exfiltration Exfiltration: AI Agent Initiated Cloud SQL Exfiltration to Public Bucket Exfiltration: AI Agent Initiated Cloud SQL Exfiltration to External Bucket |  [ Activate Logging Data Access audit logs for Cloud SQL for SQL Server](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)  
[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) |  Log4j Malware: Bad IP Malware: bad IP Malware: Cryptomining Bad IP |  [Turn on VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) See also Logs for network detection of malware.  
  
### Logs that are always on

The following table lists the Cloud Logging logs that you don't need to turn on or configure. These logs are always on and Event Threat Detection scans them automatically.

Log type | Threats detected | Configuration required  
---|---|---  
[ Agent Engine Logs](https://docs.cloud.google.com/agent-builder/agent-engine/manage/logging) |  Credential Access: AI Agent Anomalous Access to Metadata Service ([Preview](https://cloud.google.com/products/#product-launch-stages)) Discovery: Evidence of Port Scanning from AI Agent ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  None   
[ Backup and DR Admin Activity audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging) |  Impact: Google Cloud Backup and DR expire all images  Impact: Deleted Google Cloud Backup and DR Backup  Impact: Deleted Google Cloud Backup and DR host  Impact: Deleted Google Cloud Backup and DR plan association  Impact: Deleted Google Cloud Backup and DR Vault  Impact: Google Cloud Backup and DR delete policy  Impact: Google Cloud Backup and DR delete profile  Impact: Google Cloud Backup and DR delete template  Impact: Google Cloud Backup and DR expire image  Impact: Google Cloud Backup and DR reduce backup expiration  Impact: Google Cloud Backup and DR reduce backup frequency  Impact: Google Cloud Backup and DR remove appliance  Impact: Google Cloud Backup and DR remove plan  Inhibit system recovery: Google Cloud Backup and DR delete storage pool  | None  
[ BigQueryAuditMetadata Data Access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs) |  Exfiltration: AI Agent Initiated BigQuery Data Extraction Exfiltration: AI Agent Initiated BigQuery Data Exfiltration to External Table Exfiltration: AI Agent Initiated BigQuery VPC Perimeter Violation Exfiltration: BigQuery Data Exfiltration Exfiltration: BigQuery Data Extraction Exfiltration: BigQuery Data to Google Drive Exfiltration: Move to Public BigQuery resource ([Preview](https://cloud.google.com/products/#product-launch-stages)) | None  
[ Generic Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  Defense Evasion: GCS Bucket IP Filtering Modified  Defense Evasion: Project HTTP Policy Block Disabled  Defense Evasion: Folder level TokenCreatorRole Added Defense Evasion: Folder Level TokenCreator Role Granted to AI Agent Defense Evasion: Organization level TokenCreatorRole Added Defense Evasion: Organization Level TokenCreator Role Granted to AI Agent Defense Evasion: Project level TokenCreatorRole Added Defense Evasion: Project Level TokenCreator Role Granted to AI Agent Discovery: AI Agent Unauthorized Service Account API Call Initial Access: AI Agent Identity Excessive Permission Denied Actions Initial Access: Dormant Service Account Action Initial Access: Dormant Service Account Activity in AI Service Initial Access: Dormant Service Account Key Created Initial Access: Excessive Permission Denied Actions Initial Access: Leaked Service Account Key Used Lateral Movement: Modified Boot Disk Attached to Instance ([Preview](https://cloud.google.com/products/#product-launch-stages))  Persistence: GCE Admin Added SSH Key Persistence: GCE Admin Added Startup Script Persistence: New AI API Method Persistence: New API Method Persistence: New Geography Persistence: New Geography for AI Service Persistence: New User Agent Persistence: Sensitive AI Permission Added to Custom Role Persistence: Sensitive Role Granted to External AI Agent Persistence: Sensitive Role Granted by AI Agent Privilege Escalation: Anomalous Impersonation of Service Account for Admin Activity  Privilege Escalation: Anomalous Impersonation of Service Account for AI Admin Activity  Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity  Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Admin Activity  Privilege Escalation: Anomalous Service Account Impersonator for Admin Activity  Privilege Escalation: Anomalous Service Account Impersonator for AI Admin Activity  | None  
[ Google Kubernetes Engine (GKE) Admin Activity audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging) |  Credential Access: Failed Attempt to Approve Kubernetes Certificate Signing Request (CSR)  Credential Access: Manually Approved Kubernetes Certificate Signing Request (CSR) ([Preview](https://cloud.google.com/products/#product-launch-stages))  Defense Evasion: Anonymous Sessions Granted Cluster Admin Access Defense Evasion: Manually Deleted Certificate Signing Request (CSR)  Defense Evasion: Potential Kubernetes Pod Masquerading  Defense Evasion: Static Pod Created  Execution: GKE launch excessively capable container ([Preview](https://cloud.google.com/products/#product-launch-stages))  Execution: Kubernetes Pod Created with Potential Reverse Shell Arguments  Execution: Suspicious Exec or Attach to a System Pod ([Preview](https://cloud.google.com/products/#product-launch-stages))  Execution: Workload triggered in sensitive namespace  Impact: GKE kube-dns modification detected ([Preview](https://cloud.google.com/products/#product-launch-stages))  Impact: Suspicious Kubernetes Container Names - Cryptocurrency Mining  Initial Access: Anonymous GKE Resource Created from the Internet ([Preview](https://cloud.google.com/products/#product-launch-stages))  Initial Access: GKE NodePort service created  Initial Access: GKE Resource Modified Anonymously from the Internet ([Preview](https://cloud.google.com/products/#product-launch-stages))  Initial Access: Successful API call made from a TOR proxy IP  Persistence: GKE Webhook Configuration Detected  Persistence: Service Account Created in sensitive namespace  Privilege Escalation: Changes to sensitive Kubernetes RBAC objects  Privilege Escalation: ClusterRole with Privileged Verbs ([Preview](https://cloud.google.com/products/#product-launch-stages))  Privilege Escalation: ClusterRoleBinding to Privileged Role  Privilege Escalation: Create Kubernetes CSR for master cert Privilege Escalation: Creation of sensitive Kubernetes bindings Privilege Escalation: Effectively Anonymous Users Granted GKE Cluster Access  Privilege Escalation: Launch of privileged Kubernetes container Privilege Escalation: Suspicious Kubernetes Container Names - Exploitation and Escape ([Preview](https://cloud.google.com/products/#product-launch-stages))  Privilege Escalation: Workload Created with a Sensitive Host Path Mount ([Preview](https://cloud.google.com/products/#product-launch-stages))  Privilege Escalation: Workload with shareProcessNamespace enabled ([Preview](https://cloud.google.com/products/#product-launch-stages))  | None  
[ IAM Admin Activity audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) |  Persistence: IAM Anomalous Grant ([Preview](https://cloud.google.com/products/#product-launch-stages)) Persistence: Unmanaged Account Granted Sensitive Role Privilege Escalation: Default Compute Engine Service Account SetIAMPolicy  Privilege Escalation: Dormant Service Account Granted Sensitive Role  Privilege Escalation: Impersonation Role Granted For Dormant Service Account  Privilege Escalation: Sensitive Role Granted To Hybrid Group | None  
[ IAM System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event) |  Execution: Cryptomining Docker Image Impact: Cryptomining Commands | None  
[ MySQL Admin Activity logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging) | Exfiltration: Cloud SQL Restore Backup to External Organization | None  
[ PostgreSQL Admin Activity logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging) | Exfiltration: Cloud SQL Restore Backup to External Organization | None  
[ SQL Server Admin Activity logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging) | Exfiltration: Cloud SQL Restore Backup to External Organization | None  
[ VPC Service Controls Audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) | Defense Evasion: Modify VPC Service Control ([Preview](https://cloud.google.com/products/#product-launch-stages)) | None  
  
## What's next

  * Learn about [using Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection).
  * Learn how to [investigate and develop response plans](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) for threats.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
