---
url: https://docs.cloud.google.com/security-command-center/docs/security-posture-cis-20-template/
title: Predefined posture template for CIS Benchmark v2.0 \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:59.477206+00:00
---

# Predefined posture template for CIS Benchmark v2.0  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/security-posture-cis-20-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Predefined posture template for CIS Benchmark v2.0 Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the detective policies that are included in the v1.0 version of the predefined posture template for [Center for Internet Security (CIS) Google Cloud Computing Platform Benchmark v2.0.0](https://www.cisecurity.org/benchmark/google_cloud_computing_platform). This predefined posture template helps you detect when your Google Cloud environment doesn't align with the CIS Benchmark.

You can deploy this posture template without making any changes.

The following table describes the Security Health Analytics detectors that are included in the posture template. For more information about these detectors, see [Vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

Detector name | Description  
---|---  
`ACCESS_TRANSPARENCY_DISABLED` | This detector checks whether [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) is turned off.  
`ADMIN_SERVICE_ACCOUNT` | This detector checks whether a service account has **Admin** , **Owner** , or **Editor** privileges.  
`ESSENTIAL_CONTACTS_NOT_CONFIGURED` | This detector checks whether you have at least one [Essential Contact](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).  
`API_KEY_APIS_UNRESTRICTED` | This detector checks whether API keys are being used too broadly.  
`API_KEY_APPS_UNRESTRICTED` | This detector checks whether API keys are being used in an unrestricted way, allowing use by any untrusted app.  
`API_KEY_EXISTS` | This detector checks whether a project is using API keys instead of standard authentication.  
`API_KEY_NOT_ROTATED` | This detector checks whether an API key has been rotated within the last 90 days.  
`AUDIT_CONFIG_NOT_MONITORED` | This detector checks whether audit configuration changes are being monitored.  
`AUDIT_LOGGING_DISABLED` | This detector checks whether audit logging is turned off for a resource.  
`AUTO_BACKUP_DISABLED` | This detector checks whether a Cloud SQL database doesn't have automatic backups turned on.  
`BIGQUERY_TABLE_CMEK_DISABLED` | This detector checks whether a BigQuery table isn't configured to use a customer-managed encryption key (CMEK). For more information, see [Dataset vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataset-findings).  
`BUCKET_IAM_NOT_MONITORED` | This detector checks whether logging is turned off for IAM permission changes in Cloud Storage.  
`BUCKET_POLICY_ONLY_DISABLED` | This detector checks whether uniform bucket-level access is configured.  
`CLOUD_ASSET_API_DISABLED` | This detector checks whether Cloud Asset Inventory is turned off.  
`COMPUTE_PROJECT_WIDE_SSH_KEYS_ALLOWED` | This detector checks whether project-wide SSH keys are being used.  
`COMPUTE_SERIAL_PORTS_ENABLED` | This detector checks whether serial ports are enabled.  
`CONFIDENTIAL_COMPUTING_DISABLED` | This detector checks whether Confidential Computing is turned off.  
`CUSTOM_ROLE_NOT_MONITORED` | This detector checks whether logging is turned off for custom role changes.  
`DATAPROC_CMEK_DISABLED` | This detector checks whether CMEK support is turned off for a Managed Service for Apache Spark cluster.  
`DATASET_CMEK_DISABLED` | This detector checks whether CMEK support is turned off for a BigQuery dataset.  
`DEFAULT_NETWORK` | This detector checks whether the default network exists in a project.  
`DEFAULT_SERVICE_ACCOUNT_USED` | This detector checks whether the default service account is being used.  
`DISK_CSEK_DISABLED` | This detector checks whether customer supplied encryption key (CSEK) support is turned off for a VM.  
`DNS_LOGGING_DISABLED` | This detector checks whether DNS logging is enabled on the VPC network.  
`DNSSEC_DISABLED` | This detector checks whether DNSSEC is turned off for Cloud DNS zones.  
`FIREWALL_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC firewall rule changes.  
`VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED` | This detector checks whether VPC Flow Logs is not turned on.  
`FULL_API_ACCESS` | This detector checks whether an instance is using a default service account with full access to all Google Cloud APIs.  
`INSTANCE_OS_LOGIN_DISABLED` | This detector checks whether OS Login is not turned on.  
`IP_FORWARDING_ENABLED` | This detector checks whether IP forwarding is turned on.  
`KMS_KEY_NOT_ROTATED` | This detector checks whether rotation for the Cloud Key Management Service encryption is not turned on.  
`KMS_PROJECT_HAS_OWNER` | This detector checks whether a user has the **Owner** permission on a project that includes keys.  
`KMS_PUBLIC_KEY` | This detector checks whether a Cloud Key Management Service cryptographic key is publicly accessible. For more information, see [KMS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#kms-findings).  
`KMS_ROLE_SEPARATION` | This detector checks for separation of duties for Cloud KMS keys.  
`LEGACY_NETWORK` | This detector checks whether a legacy network exists in a project.  
`LOCKED_RETENTION_POLICY_NOT_SET` | This detector checks whether the locked retention policy is set for logs.  
`LOAD_BALANCER_LOGGING_DISABLED` | This detector checks whether logging is turned off for the load balancer.  
`LOG_NOT_EXPORTED` | This detector checks whether a resource doesn't have a log sink configured.  
`MFA_NOT_ENFORCED` | This detector checks whether a user isn't using 2-step verification.  
`NETWORK_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC network changes.  
`NON_ORG_IAM_MEMBER` | This detector checks whether a user isn't using organization credentials.  
`OPEN_RDP_PORT` | This detector checks whether a firewall has an open RDP port.  
`OPEN_SSH_PORT` | This detector checks whether a firewall has an open SSH port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`OS_LOGIN_DISABLED` | This detector checks whether OS Login is turned off.  
`OVER_PRIVILEGED_SERVICE_ACCOUNT_USER` | This detector checks whether a user has service account roles at the project level, instead of for a specific service account.  
`OWNER_NOT_MONITORED` | This detector checks whether logging is turned off for project ownership assignments and changes.  
`PUBLIC_BUCKET_ACL` | This detector checks whether a bucket is publicly accessible.  
`PUBLIC_DATASET` | This detector checks whether a dataset is configured to be open to public access. For more information, see [Dataset vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataset-findings).  
`PUBLIC_IP_ADDRESS` | This detector checks whether an instance has an external IP address.  
`PUBLIC_SQL_INSTANCE` | This detector checks whether a Cloud SQL allows connections from all IP addresses.  
`ROUTE_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC network route changes.  
`RSASHA1_FOR_SIGNING` | This detector checks whether RSASHA1 is used for key signing in Cloud DNS zones.  
`SERVICE_ACCOUNT_KEY_NOT_ROTATED` | This detector checks whether a service account key has been rotated within the last 90 days.  
`SERVICE_ACCOUNT_ROLE_SEPARATION` | This detector checks for separation of duties for service account keys.  
`SHIELDED_VM_DISABLED` | This detector checks whether Shielded VM is turned off.  
`SQL_CONTAINED_DATABASE_AUTHENTICATION` | This detector checks whether the `contained database authentication` flag in Cloud SQL for SQL Server is enabled.  
`SQL_CROSS_DB_OWNERSHIP_CHAINING` | This detector checks whether the `cross_db_ownership_chaining` flag in Cloud SQL for SQL Server is enabled.  
`SQL_EXTERNAL_SCRIPTS_ENABLED` | This detector checks whether the `external scripts enabled` flag in Cloud SQL for SQL Server is enabled.  
`SQL_INSTANCE_NOT_MONITORED` | This detector checks whether logging is turned off for Cloud SQL configuration changes.  
`SQL_LOCAL_INFILE` | This detector checks whether the `local_infile` flag in Cloud SQL for MySQL is enabled.  
`SQL_LOG_CONNECTIONS_DISABLED` | This detector checks whether the `log_connections` flag in Cloud SQL for PostgreSQL is disabled.  
`SQL_LOG_DISCONNECTIONS_DISABLED` | This detector checks whether the `log_disconnections` flag in Cloud SQL for PostgreSQL is disabled.  
`SQL_LOG_ERROR_VERBOSITY` | This detector checks whether the `log_error_verbosity` flag in Cloud SQL for PostgreSQL isn't set to `default`.  
`SQL_LOG_MIN_DURATION_STATEMENT_ENABLED` | This detector checks whether the `log_min_duration_statement` flag in Cloud SQL for PostgreSQL isn't set to `-1`.  
`SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY` | This detector checks whether the `log_min_error_statement` flag in Cloud SQL for PostgreSQL doesn't have an appropriate severity level.  
`SQL_LOG_MIN_MESSAGES` | This detector checks whether the `log_min_messages` flag in Cloud SQL for PostgreSQL isn't set to `warning`.  
`SQL_LOG_STATEMENT` | This detector checks whether the `log_statement` flag in Cloud SQL for PostgreSQL Server isn't set to `ddl`.  
`SQL_NO_ROOT_PASSWORD` | This detector checks whether a Cloud SQL database with an external IP address doesn't have a password for the root account.  
`SQL_PUBLIC_IP` | This detector checks whether a Cloud SQL database has an external IP address.  
`SQL_REMOTE_ACCESS_ENABLED` | This detector checks whether the `remote_access` flag in Cloud SQL for SQL Server is enabled.  
`SQL_SKIP_SHOW_DATABASE_DISABLED` | This detector checks whether the `skip_show_database` flag in Cloud SQL for MySQL is disabled.  
`SQL_TRACE_FLAG_3625` | This detector checks whether the `3625 (trace flag)` flag in Cloud SQL for SQL Server is disabled.  
`SQL_USER_CONNECTIONS_CONFIGURED` | This detector checks whether the `user connections` flag in Cloud SQL for SQL Server is configured.  
`SQL_USER_OPTIONS_CONFIGURED` | This detector checks whether the `user options` flag in Cloud SQL for SQL Server is configured.  
`SSL_NOT_ENFORCED` | This detector checks whether a Cloud SQL database instance doesn't require all incoming connections to use SSL.  
`USER_MANAGED_SERVICE_ACCOUNT_KEY` | This detector checks whether a user manages a service account key.  
`WEAK_SSL_POLICY` | This detector checks whether an instance has a weak SSL policy.  
  
## View the posture template

To view the posture template for CIS Benchmark v2.0, do the following: 

### gcloud

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



Execute the [`gcloud scc posture-templates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc posture-templates describe \
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/cis_2_0

#### Windows (PowerShell)
    
    
    gcloud scc posture-templates describe `
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/cis_2_0

#### Windows (cmd.exe)
    
    
    gcloud scc posture-templates describe ^
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/cis_2_0

The response contains the posture template.

### REST

Before using any of the request data, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



HTTP method and URL: 
    
    
    GET https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/cis_2_0

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/cis_2_0"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/cis_2_0" | Select-Object -Expand Content

The response contains the posture template.

## What's next

  * [Create a security posture using this predefined posture template](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
