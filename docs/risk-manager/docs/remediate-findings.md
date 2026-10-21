---
url: https://docs.cloud.google.com/risk-manager/docs/remediate-findings/
title: Remediating findings \u00a0|\u00a0 Cyber Insurance Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:44.621738+00:00
---

# Remediating findings  |  Cyber Insurance Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/risk-manager/docs/remediate-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cyber Insurance Hub ](https://docs.cloud.google.com/risk-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/risk-manager/docs/quickstarts)



Send feedback 

#  Remediating findings Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to remediate findings in reports.

A report combines aggregate findings from [Security Command Center](https://docs.cloud.google.com/security-command-center) and inventory data from [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory) to give an aggregate view of risk across your organization. These reports are aligned with the [CIS Google Cloud Computing Foundations Benchmark v1.2.0](https://www.cisecurity.org/insights/blog/cis-benchmarks-may-2021-update). For more information on this framework, see [CIS Benchmarks](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#cis-benchmarks).

As a best practice, start by remediating the findings that have the highest impact, as indicated in a Cyber Insurance Hub report.

## Before you begin

[Create a report](https://docs.cloud.google.com/risk-manager/docs/managing-reports#create).

## Remediating CIS Benchmark findings

Cyber Insurance Hub has integrated with Security Command Center [Premium and Enterprise tiers](https://cloud.google.com/security-command-center/pricing#tier-pricing) to simplify the remediation process for CIS Benchmark findings. If you're a Security Command Center [Standard tier](https://cloud.google.com/security-command-center/pricing#tier-pricing) customer, you can't use Security Command Center to inspect and remediate all individual CIS Benchmark findings on your Google Cloud resources. Upgrade to Premium tier or Enterprise tier to get full support. See [Activation overview](https://docs.cloud.google.com/security-command-center/activate-scc-overview) for more detailed information about how to activate each Security Command Center tier.

### Remediating CIS Benchmark findings with Security Command Center Premium or Enterprise tier

To inspect and remediate individual findings using Security Command Center, follow these steps:

  1. In a report, in the table of CIS benchmark topics, expand a CIS Benchmark topic to view the CIS Benchmarks for that topic.

  2. In a CIS Benchmark table row, click the finding count.

This links to Security Command Center to display the active findings related to that CIS Benchmark.

  3. In Security Command Center, in the table of findings, click the category of the finding that you want to remediate.

A pane opens with information on how to remediate that finding.




### Remediating CIS Benchmarks with Security Command Center Standard tier

While Cyber Insurance Hub reports provide a table of the CIS Benchmark topics identified across your organization, Security Command Center Standard tier doesn't let you pivot directly to the related findings in Security Command Center.

To view instructions on how to remediate general CIS Benchmarks, follow these steps:

  1. In a report, in the table of CIS benchmark topics, expand a CIS Benchmark topic to view the CIS Benchmarks for that topic.

  2. In a CIS Benchmark table row, click the CIS Benchmark description.

This links to the general remediation instructions for that CIS Benchmark.




You can also use the following instructions to remediate findings for CIS Benchmarks supported by Cyber Insurance Hub:

Identity and Access Management  
---  
[ 1.1 Ensure that corporate login credentials are used](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#non_org_iam_member)  
[ 1.2 Ensure that multi-factor authentication is enabled for all non-service accounts](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#mfa_not_enforced)  
[ 1.4 Ensure that there are only GCP-managed service account keys for each service account](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#user_managed_service_account_key)  
[ 1.5 Ensure that Service Account has no Admin privileges](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#admin_service_account)  
[ 1.6 Ensure that IAM users are not assigned the Service Account User or Service Account Token Creator roles at project level](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#over_privileged_service_account_user)  
[ 1.7 Ensure user-managed/external keys for service accounts are rotated every 90 days or less](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#service_account_key_not_rotated)  
[ 1.8 Ensure that Separation of duties is enforced while assigning service account related roles to users](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#service_account_role_separation)  
[ 1.9 Ensure that Cloud KMS cryptokeys are not anonymously or publicly accessible](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#kms_public_key)  
[ 1.10 Ensure KMS encryption keys are rotated within a period of 90 days](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#kms_key_not_rotated)  
[ 1.11 Ensure that Separation of duties is enforced while assigning KMS related roles to users](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#kms_role_separation)  
[ 1.12 Ensure API keys are not created for a project](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#api_key_exists)  
[ 1.13 Ensure API keys are restricted to use by only specified Hosts and Apps](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#api_key_apps_unrestricted)  
[ 1.14 Ensure API keys are restricted to only APIs that application needs access](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#api_key_apis_unrestricted)  
[ 1.15 Ensure API keys are rotated every 90 days](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#api_key_not_rotated)  
Logging and Monitoring  
[ 2.1 Ensure that Cloud Audit Logging is configured properly across all services and all users from a project](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#audit_logging_disabled)  
[ 2.2 Ensure that sinks are configured for all log entries](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#log_not_exported)  
[ 2.3 Ensure that retention policies on log buckets are configured using Bucket Lock](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#locked_retention_policy_not_set)  
[ 2.4 Ensure log metric filter and alerts exist for project ownership assignments/changes](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#owner_not_monitored)  
[ 2.5 Ensure that the log metric filter and alerts exist for Audit Configuration changes](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#audit_config_not_monitored)  
[ 2.6 Ensure that the log metric filter and alerts exist for Custom Role changes](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#custom_role_not_monitored)  
[ 2.7 Ensure that the log metric filter and alerts exist for VPC Network Firewall rule changes](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#firewall_not_monitored)  
[ 2.8 Ensure that the log metric filter and alerts exist for VPC network route changes](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#route_not_monitored)  
[ 2.9 Ensure that the log metric filter and alerts exist for VPC network changes](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#network_not_monitored)  
[ 2.10 Ensure that the log metric filter and alerts exist for Cloud Storage IAM permission changes](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#bucket_iam_not_monitored)  
[ 2.11 Ensure that the log metric filter and alerts exist for SQL instance configuration changes](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_instance_not_monitored)  
[ 2.12 Ensure that Cloud DNS logging is enabled for all VPC networks](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#dns_logging_disabled)  
Networking  
[ 3.1 Ensure that the default network does not exist in a project](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#default_network)  
[ 3.2 Ensure legacy network does not exist for a project](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#legacy_network)  
[ 3.3 Ensure that DNSSEC is enabled for Cloud DNS](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#dnssec_disabled)  
[ 3.4 Ensure that RSASHA1 is not used for the key-signing key in Cloud DNS DNSSEC](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#rsasha1_for_signing)  
[ 3.5 Ensure that RSASHA1 is not used for the zone-signing key in Cloud DNS DNSSEC](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#rsasha1_for_signing)  
[ 3.6 Ensure that SSH access is restricted from the internet](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#open_ssh_port)  
[ 3.7 Ensure that RDP access is restricted from the Internet](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#open_rdp_port)  
[ 3.8 Ensure that VPC Flow Logs is enabled for every subnet in a VPC Network](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#flow_logs_disabled)  
[ 3.9 Ensure no HTTPS or SSL proxy load balancers permit SSL policies with weak cipher suites](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#weak_ssl_policy)  
Virtual Machines  
[ 4.1 Ensure that instances are not configured to use the default service account](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#default_service_account_used)  
[ 4.2 Ensure that instances are not configured to use the default service account with full access to all Cloud APIs](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#full_api_access)  
[ 4.3 Ensure "Block Project-wide SSH keys" is enabled for VM instances](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#compute_project_wide_ssh_keys_allowed)  
[ 4.4 Ensure oslogin is enabled for a Project](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#os_login_disabled)  
[ 4.5 Ensure "Enable connecting to serial ports" is not enabled for VM Instance](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#compute_serial_ports_enabled)  
[ 4.6 Ensure that IP forwarding is not enabled on Instances](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#ip_forwarding_enabled)  
[ 4.7 Ensure VM disks for critical VMs are encrypted with Customer-Supplied Encryption Keys (CSEK)](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#disk_csek_disabled)  
[ 4.8 Ensure Compute instances are launched with Shielded VM enabled](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#shielded_vm_disabled)  
[ 4.9 Ensure that Compute instances do not have public IP addresses](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#public_ip_address)  
[ 4.11 Ensure that Compute instances have Confidential Computing enabled ](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#confidential_computing_disabled)  
Storage  
[ 5.1 Ensure that Cloud Storage bucket is not anonymously or publicly accessible](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#public_bucket_acl)  
[ 5.2 Ensure that Cloud Storage buckets have uniform bucket-level access enabled ](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#bucket_policy_only_disabled)  
Cloud SQL Database Services  
[ 6.1.1 Ensure that a MySQL database instance does not allow anyone to connect with administrative privileges ](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_no_root_password)  
[ 6.1.2 Ensure "skip_show_database" database flag for Cloud SQL Mysql instance is set to "on"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_skip_show_database_disabled)  
[ 6.1.3 Ensure that the "local_infile" database flag for a Cloud SQL Mysql instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_local_infile)  
[ 6.2.1 Ensure that the "log_checkpoints" database flag for Cloud SQL PostgreSQL instance is set to "on"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_checkpoints_disabled)  
[ 6.2.2 Ensure "log_error_verbosity" database flag for Cloud SQL PostgreSQL instance is set to "DEFAULT" or stricter](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_error_verbosity)  
[ 6.2.3 Ensure that the "log_connections" database flag for Cloud SQL PostgreSQL instance is set to "on"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_connections_disabled)  
[ 6.2.4 Ensure that the "log_disconnections" database flag for Cloud SQL PostgreSQL instance is set to "on"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_disconnections_disabled)  
[ 6.2.5 Ensure "log_duration" database flag for Cloud SQL PostgreSQL instance is set to "on"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_duration_disabled)  
[ 6.2.6 Ensure that the "log_lock_waits" database flag for Cloud SQL PostgreSQL instance is set to "on"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_lock_waits_disabled)  
[ 6.2.7 Ensure "log_statement" database flag for Cloud SQL PostgreSQL instance is set appropriately](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_statement)  
[ 6.2.8 Ensure "log_hostname" database flag for Cloud SQL PostgreSQL instance is set appropriately](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_hostname_enabled)  
[ 6.2.9 Ensure "log_parser_stats" database flag for Cloud SQL PostgreSQL instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_parser_stats_enabled)  
[ 6.2.10 Ensure "log_planner_stats" database flag for Cloud SQL PostgreSQL instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_planner_stats_enabled)  
[ 6.2.11 Ensure "log_executor_stats" database flag for Cloud SQL PostgreSQL instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_executor_stats_enabled)  
[ 6.2.12 Ensure "log_statement_stats" database flag for Cloud SQL PostgreSQL instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_statement_stats_enabled)  
[ 6.2.13 Ensure that the "log_min_messages" database flag for Cloud SQL PostgreSQL instance is set appropriately](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_min_messages)  
[ 6.2.14 Ensure "log_min_error_statement" database flag for Cloud SQL PostgreSQL instance is set to "Error" or stricter](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_min_error_statement_severity)  
[ 6.2.15 Ensure that the "log_temp_files" database flag for Cloud SQL PostgreSQL instance is set to "0" ](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_temp_files)  
[ 6.2.16 Ensure that the "log_min_duration_statement" database flag for Cloud SQL PostgreSQL instance is set to "-1"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_log_min_duration_statement_enabled)  
[ 6.3.1 Ensure "external scripts enabled" database flag for Cloud SQL SQL Server instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_external_scripts_enabled)  
[ 6.3.2 Ensure that the "cross db ownership chaining" database flag for Cloud SQL SQL Server instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_cross_db_ownership_chaining)  
[ 6.3.3 Ensure "user connections" database flag for Cloud SQL SQL Server instance is set as appropriate](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_user_connections_configured)  
[ 6.3.4 Ensure "user options" database flag for Cloud SQL SQL Server instance is not configured](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_user_options_configured)  
[ 6.3.5 Ensure "remote access" database flag for Cloud SQL SQL Server instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_remote_access_enabled)  
[ 6.3.6 Ensure "3625 (trace flag)" database flag for Cloud SQL SQL Server instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_trace_flag_3625)  
[ 6.3.7 Ensure that the "contained database authentication" database flag for Cloud SQL on the SQL Server instance is set to "off"](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_contained_database_authentication)  
[ 6.4 Ensure that the Cloud SQL database instance requires all incoming connections to use SSL](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#ssl_not_enforced)  
[ 6.5 Ensure that Cloud SQL database instances are not open to the world](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#public_sql_instance)  
[ 6.6 Ensure that Cloud SQL database instances do not have public IPs](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#sql_public_ip)  
[ 6.7 Ensure that Cloud SQL database instances are configured with automated backups](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#auto_backup_disabled)  
BigQuery  
[ 7.1 Ensure that BigQuery datasets are not anonymously or publicly accessible](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#public_dataset)  
[ 7.2 Ensure that all BigQuery Tables are encrypted with Customer-managed encryption key (CMEK)](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#bigquery_table_cmek_disabled)  
[ 7.3 Ensure that a Default Customer-managed encryption key (CMEK) is specified for all BigQuery Data Sets](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#dataset_cmek_disabled)  
  
## What's next?

  * Learn how to [approve a report](https://docs.cloud.google.com/risk-manager/docs/managing-reports#approve).
  * Learn how to [share a report with insurance partners](https://docs.cloud.google.com/risk-manager/docs/managing-reports#send).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
