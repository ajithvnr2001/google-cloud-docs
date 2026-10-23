---
url: https://docs.cloud.google.com/security-command-center/docs/secops-limits/
title: Google SecOps features in Security Command Center Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:25.991718+00:00
---

# Google SecOps features in Security Command Center Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/secops-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Resources ](https://docs.cloud.google.com/security-command-center/docs/resources)



Send feedback 

#  Google SecOps features in Security Command Center Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The Security Command Center Enterprise service tier offers [additional features](https://docs.cloud.google.com/security-command-center/docs/service-tiers) compared to the Standard and Premium tiers, including a selection of [Google Security Operations](https://cloud.google.com/security/products/security-operations) features and the ability to ingest data from other cloud providers. These features make Security Command Center a cloud-native application protection platform (CNAPP).

The Google Security Operations features in the Security Command Center Enterprise tier have different limits than those in the [Google Security Operations plans](https://cloud.google.com/security/products/security-operations#pricing). These limits are described in the following table.

Feature | Limits  
---|---  
[Applied Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/detection) | No access  
[Curated detections](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections) |  Limited to detecting [ cloud threats](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category) on Google Cloud, Microsoft Azure, and AWS.   
Custom rules |  20 custom single-event [ rules](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-overview#single-event-rule), multi-event rules aren't supported.   
Data retention | 3 months  
Gemini for Google Security Operations |  Limited to natural language search and case investigation summaries   
Google SecOps security information and event management (SIEM)  | Cloud data only.  
Google SecOps security orchestration, automation, and response (SOAR)  | Cloud response integrations only. For the list of supported integrations, see Supported Google Security Operations integrations. Supports one [SOAR environment](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments#add-a-new-environment).  
Log ingestion |  Limited to logs that are supported for cloud threat detection. For the list, see Supported log data collection in Google SecOps  
[ Risk analytics](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-overview) | No access  
  
## Supported Google Security Operations integrations

The following sections list the Google Security Operations Marketplace integrations that are supported with Security Command Center Enterprise. They are listed in separate columns in the following table.

  * **Packaged and preconfigured integrations** : are included in the **SCC Enterprise - Cloud Orchestration and Remediation** use case and are preconfigured to support cloud-native application protection platform (CNAPP) use cases. They are available when you activate [Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier) and [update the Enterprise use case](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update).

Configurations in the **SCC Enterprise - Cloud Orchestration and Remediation** use case include, as an example, dedicated playbooks that use Jira and ServiceNow with predefined handling of response cases. The integrations are preconfigured to support all cloud providers that Security Command Center Enterprise supports.

  * **Downloadable integrations** : with Security Command Center Enterprise, you can download the following integrations and use them in a playbook. The versions that you download from Google Security Operations Marketplace are not configured specifically for Security Command Center Enterprise and require additional manual configuration.




Each integration is listed by name. For information about a specific integration, see [Google Security Operations Marketplace integrations](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations).

**Type of application or information** | **Packaged and preconfigured integrations** | **Downloadable integrations**  
---|---|---  
Google Cloud and Google Workspace integrations | 

  * AppSheet
  * Google Alert Center
  * Google BigQuery
  * Google Chat
  * Google Chronicle
  * Google Cloud Asset Inventory
  * Google Cloud Compute
  * Google Cloud IAM
  * Google Cloud Policy Intelligence
  * Google Cloud Recommender
  * Google Cloud Storage
  * Google Kubernetes Engine
  * Google Rapid Response (GRR)
  * Google Security Command Center
  * Google Translate
  * GSuite
  * SCCEnterprise

| 

  * AppSheet
  * Google Alert Center
  * Google BigQuery
  * Google Chat
  * Google Chronicle
  * Google Cloud Asset Inventory
  * Google Cloud Compute
  * Google Cloud IAM
  * Google Cloud Policy Intelligence
  * Google Cloud Recommender
  * Google Cloud Storage
  * Google Kubernetes Engine
  * Google Rapid Response (GRR)
  * Google Security Command Center
  * Google Translate
  * GSuite
  * SCCEnterprise

  
Amazon Web Services integrations | 

  * AWS CloudTrail
  * AWS CloudWatch
  * AWS Elastic Compute Cloud (EC2)
  * AWS GuardDuty
  * AWS Identity and Access Management (IAM)
  * AWS IAM Access Analyzer
  * AWS S3
  * AWS Security Hub
  * AWS WAF

| 

  * AWS CloudTrail
  * AWS CloudWatch
  * AWS Elastic Compute Cloud (EC2)
  * AWS GuardDuty
  * AWS Identity and Access Management (IAM)
  * AWS IAM Access Analyzer
  * Amazon Macie*
  * AWS S3
  * AWS Security Hub
  * AWS WAF

  
Microsoft Azure and Office365 integrations | 

  * Azure Active Directory
  * Azure AD Identity Protection
  * Azure Security Center
  * Microsoft Graph Mail
  * Microsoft Teams

| 

  * Azure Active Directory
  * Azure AD Identity Protection
  * Azure Security Center
  * Microsoft Graph Mail
  * Microsoft Teams

  
IT service management (ITSM)-related applications | 

  * BMC Helix Remedyforce
  * BMC Remedy ITSM
  * CA Service Desk Manager
  * Easy Vista
  * Freshworks Freshservice
  * Jira
  * Micro Focus ITSMA
  * Service Desk Plus V3
  * ServiceNow
  * SysAid
  * Zendesk
  * Zoho Desk

| 

  * BMC Helix Remedyforce
  * BMC Remedy ITSM
  * CA Service Desk Manager
  * Easy Vista
  * Freshworks Freshservice
  * Jira
  * Micro Focus ITSMA
  * Service Desk Plus V3
  * ServiceNow
  * SysAid
  * Zendesk
  * Zoho Desk

  
Communication-related applications | 

  * Email V2
  * Exchange
  * Google Chat
  * Microsoft Graph Mail
  * Microsoft Teams
  * Slack

| 

  * Email V2
  * Exchange
  * Google Chat
  * Microsoft Graph Mail
  * Microsoft Teams
  * Slack

  
Threat intelligence | 

  * Mandiant Threat Intelligence
  * Mitre Att&ck
  * VirusTotalV3

| 

  * Mandiant Threat Intelligence
  * Mitre Att&ck
  * VirusTotalV3

  
* Integration is not packaged in the **SCC Enterprise - Cloud Orchestration and Remediation** use case  
  
## Key features in the Security Operations console

The Security Command Center Enterprise tier integrates key features from Google Security Operations, accessible through the Security Operations console. The following sections give a brief overview of the available features:

### Alerts & IOCs

This Security Operations console page lets you view alerts created by curated detections and custom rules. For information about investigating alerts, see the following in Google Security Operations documentation:

  * [Investigating a GCTI alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-uppercase-alert) generated by curated detections.
  * [Investigating an alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert).



### Cases

In the Security Operations console, you use cases to obtain details about findings, attach playbooks to finding alerts, apply automatic threat responses, and track the remediation of security issues.

For information, see [Cases overview](https://docs.cloud.google.com/security-command-center/docs/cases-overview).

### Playbooks

This Security Operations console page lets you manage playbooks included in the **SCC Enterprise - Cloud Orchestration and Remediation** use case.

For information about the integrations available in this use case, see Security Command Center service tiers.

For information about the available playbooks, see [Update the Enterprise use case](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update).

For information about using the Security Operations console **Playbooks** page, see [What's on the Playbooks page?](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen) in Google Security Operations documentation.

### Rules & Detections

This Security Operations console page lets you enable curated detections and create custom rules to identify patterns in data collected using the Security Operations console log data collection mechanisms. For information about the curated detections available with Security Command Center Enterprise, see [Investigate threats with curated detections](https://docs.cloud.google.com/security-command-center/docs/investigate-threat-findings).

### SIEM dashboards

This Security Operations console page lets you view Google Security Operations SIEM dashboards to analyze alerts created by Google Security Operations rules and data collected using the Security Operations console log data collection capabilities.

For more information about using SIEM dashboards, see [Dashboards overview](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview) in Google Security Operations documentation.

### SIEM search

This Security Operations console page lets you find Unified Data Model (UDM) events and alerts within your Google Security Operations instance. For more information, see [SIEM search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) in Google Security Operations documentation.

### SIEM settings

This Security Operations console page lets you change the configuration for features related to Google Security Operations SIEM. For information about using these features, see [Google Security Operations documentation](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview).

### SOAR dashboards

This Security Operations console page lets you view and create dashboards using SOAR data that can be used to analyze responses and cases. For more information about using SOAR dashboards, see [SOAR Dashboard Overview](https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/dashboard-overview) in Google Security Operations documentation.

### SOAR reports

This Security Operations console page lets you view reports against SOAR data. For more information about using SOAR reports, see [Understanding SOAR Reports](https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-reports/understanding-reports) in Google Security Operations documentation.

### SOAR search

This Security Operations console page lets you find specific cases or entities indexed by Google Security Operations SOAR. For more information, see [Work with the Search page in SOAR](https://docs.cloud.google.com/chronicle/docs/soar/investigate/search/working-with-search-screen) in Google Security Operations documentation.

### SOAR settings

This Security Operations console page lets you change the configuration for features related to Google Security Operations SOAR. For information about using these features, see [Google Security Operations documentation](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview).

## Supported Google SecOps log data collection

The following sections describe the type of log data that customers with Security Command Center Enterprise can ingest directly to the Google Security Operations tenant. This data collection mechanism is different than the [AWS connector in Security Command Center ](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) that collects resource and configuration data.

The information is grouped by cloud provider.

  * Google Cloud log data
  * Amazon Web Services log data
  * Microsoft Azure log data



For each type of log listed, the Google SecOps ingestion label is provided, for example `GCP_CLOUDAUDIT`. See [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers) for a complete list of Google SecOps ingestion labels.

###  Google Cloud 

The following Google Cloud data can be ingested to Google SecOps:

  * Cloud Audit Logs (`GCP_CLOUDAUDIT`)
  * Cloud Intrusion Detection System (`GCP_IDS`)
  * Cloud Next Generation Firewall (`GCP_NGFW_ENTERPRISE`)
  * [Cloud Asset Inventory metadata](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#export-asset-metadata)
  * [Sensitive Data Protection context](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#export-dlp-data)
  * [Model Armor logs](https://docs.cloud.google.com/model-armor/audit-logging-model-armor)



The following must also be enabled and routed to Cloud Logging:

  * [AlloyDB for PostgreSQL Data Access audit logs](https://docs.cloud.google.com/alloydb/docs/audit-logging)
  * [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring)
  * [Cloud NAT logs](https://docs.cloud.google.com/nat/docs/monitoring)
  * [Cloud Run](https://docs.cloud.google.com/run/docs/audit-logging)
  * [Cloud SQL for SQL Server Data Access audit logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging)
  * [Cloud SQL for MySQL Data Access audit logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)
  * [Cloud SQL for PostgreSQL Data Access audit logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)
  * [Compute Engine VM authlogs](https://docs.cloud.google.com/logging/docs/view/query-library#gce-filters)
  * [External Application Load Balancer backend service logs](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring)
  * [Generic Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access)
  * [Google Kubernetes Engine Data Access audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy)
  * [Google Workspace Admin Audit logs](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging)
  * [Google Workspace Login Audit logs](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging)
  * [IAM Data Access audit logs](https://docs.cloud.google.com/resource-manager/docs/audit-logging)
  * [Sensitive Data Protection context](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#export-dlp-data)
  * [Model Armor logs](https://docs.cloud.google.com/model-armor/audit-logging-model-armor)
  * AuditD logs
  * Windows event logs



For information about how to collect logs from Linux and Windows VM instances and send to Cloud Logging, see [Google Cloud Observability agents](https://docs.cloud.google.com/logging/docs/agent).

The Security Command Center Enterprise activation process automatically configures the ingestion of Google Cloud data to Google SecOps. For more information about this, see _Activate the Security Command Center Enterprise tier_ > [Provision a new instance](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#new-instance).

For information about how to modify the Google Cloud data ingestion configuration, see [Ingest Google Cloud data to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs).

###  Amazon Web Services 

The following AWS data can be ingested to Google SecOps:

  * AWS CloudTrail (`AWS_CLOUDTRAIL`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS EC2 HOSTS (`AWS_EC2_HOSTS`)
  * AWS EC2 INSTANCES (`AWS_EC2_INSTANCES`)
  * AWS EC2 VPCS (`AWS_EC2_VPCS`)
  * AWS Identity and Access Management (IAM) (`AWS_IAM`) 



For information about collecting AWS log data and using curated detections, see [Connect to AWS for log data collection](https://docs.cloud.google.com/security-command-center/docs/connect-secops-aws#aws-curated-detections).

###  Microsoft Azure 

The following Microsoft data can be ingested to Google SecOps:

  * Microsoft Azure Cloud Services (`AZURE_ACTIVITY`). See [Ingest Microsoft Azure activity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-azure-activity-logs) for information about how to set up data collection.
  * Microsoft Entra ID, previously Azure Active Directory (`AZURE_AD`). See [Collect Microsoft Azure AD logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad) for information about how to set up data collection.
  * Microsoft Entra ID audit logs, previously Azure AD audit logs (`AZURE_AD_AUDIT`). See [Collect Microsoft Azure AD logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad) for information about how to set up data collection.
  * Microsoft Defender for Cloud (`MICROSOFT_GRAPH_ALERT`). See [Collect Microsoft Graph API alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-graph-alert) for information about how to set up data collection. 



For information about collecting Azure log data and using curated detections, see [Connect to Microsoft Azure for log data collection](https://docs.cloud.google.com/security-command-center/docs/connect-secops-azure).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
