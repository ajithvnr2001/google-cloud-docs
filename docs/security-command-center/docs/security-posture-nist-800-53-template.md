---
url: https://docs.cloud.google.com/security-command-center/docs/security-posture-nist-800-53-template/
title: Predefined posture template for NIST SP 800-53 \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:22.166830+00:00
---

# Predefined posture template for NIST SP 800-53  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/security-posture-nist-800-53-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Predefined posture template for NIST SP 800-53 Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the detective policies that are included in the v1.0 version of the predefined posture template for the [National Institute of Standards and Technology (NIST) SP 800-53 standard](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final). This template includes a policy set that defines the Security Health Analytics detectors that apply to workloads that must be compliant with the NIST SP 800-53 standard.

You can deploy this posture template without making any changes.

## Security Health Analytics detectors

The following table describes the Security Health Analytics detectors that are included in this posture template.

Detector name | Description  
---|---  
`BIGQUERY_TABLE_CMEK_DISABLED` | This detector checks whether a BigQuery table isn't configured to use a customer-managed encryption key (CMEK). For more information, see [Dataset vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataset-findings).  
`PUBLIC_DATASET` | This detector checks whether a dataset is configured to be open to public access. For more information, see [Dataset vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataset-findings).  
`SQL_CROSS_DB_OWNERSHIP_CHAINING` | This detector checks whether the `cross_db_ownership_chaining` flag in Cloud SQL for SQL Server is enabled.  
`INSTANCE_OS_LOGIN_DISABLED` | This detector checks whether OS Login is not turned on.  
`SQL_SKIP_SHOW_DATABASE_DISABLED` | This detector checks whether the `skip_show_database` flag in Cloud SQL for MySQL is disabled.  
`SQL_EXTERNAL_SCRIPTS_ENABLED` | This detector checks whether the `external scripts enabled` flag in Cloud SQL for SQL Server is enabled.  
`VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED` | This detector checks whether VPC Flow Logs is not turned on.  
`API_KEY_EXISTS` | This detector checks whether a project is using API keys instead of standard authentication.  
`SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY` | This detector checks whether the `log_min_error_statement` flag in Cloud SQL for PostgreSQL doesn't have an appropriate severity level.  
`COMPUTE_SERIAL_PORTS_ENABLED` | This detector checks whether serial ports are enabled.  
`SQL_LOG_DISCONNECTIONS_DISABLED` | This detector checks whether the `log_disconnections` flag in Cloud SQL for PostgreSQL is disabled.  
`COMPUTE_PROJECT_WIDE_SSH_KEYS_ALLOWED` | This detector checks whether project-wide SSH keys are being used.  
`KMS_PROJECT_HAS_OWNER` | This detector checks whether a user has the **Owner** permission on a project that includes keys.  
`KMS_KEY_NOT_ROTATED` | This detector checks whether rotation for the Cloud Key Management Service encryption is not turned on.  
`ESSENTIAL_CONTACTS_NOT_CONFIGURED` | This detector checks whether you have at least one [Essential Contact](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).  
`AUDIT_LOGGING_DISABLED` | This detector checks whether audit logging is turned off for a resource.  
`LOCKED_RETENTION_POLICY_NOT_SET` | This detector checks whether the locked retention policy is set for logs.  
`DNS_LOGGING_DISABLED` | This detector checks whether DNS logging is enabled on the VPC network.  
`LOG_NOT_EXPORTED` | This detector checks whether a resource doesn't have a log sink configured.  
`KMS_ROLE_SEPARATION` | This detector checks for separation of duties for Cloud KMS keys.  
`DISK_CSEK_DISABLED` | This detector checks whether customer supplied encryption key (CSEK) support is turned off for a VM.  
`SQL_USER_CONNECTIONS_CONFIGURED` | This detector checks whether the `user connections` flag in Cloud SQL for SQL Server is configured.  
`API_KEY_APIS_UNRESTRICTED` | This detector checks whether API keys are being used too broadly.  
`SQL_LOG_MIN_MESSAGES` | This detector checks whether the `log_min_messages` flag in Cloud SQL for PostgreSQL isn't set to `warning`.  
`SQL_LOCAL_INFILE` | This detector checks whether the `local_infile` flag in Cloud SQL for MySQL is enabled.  
`SQL_LOG_MIN_DURATION_STATEMENT_ENABLED` | This detector checks whether the `log_min_duration_statement` flag in Cloud SQL for PostgreSQL isn't set to `-1`.  
`DATASET_CMEK_DISABLED` | This detector checks whether CMEK support is turned off for a BigQuery dataset.  
`OPEN_SSH_PORT` | This detector checks whether a firewall has an open SSH port that allows generic access. For more information, see [Firewall vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#firewall-findings).  
`FIREWALL_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC firewall rule changes.  
`SQL_LOG_STATEMENT` | This detector checks whether the `log_statement` flag in Cloud SQL for PostgreSQL Server isn't set to `ddl`.  
`SQL_PUBLIC_IP` | This detector checks whether a Cloud SQL database has an external IP address.  
`IP_FORWARDING_ENABLED` | This detector checks whether IP forwarding is turned on.  
`DATAPROC_CMEK_DISABLED` | This detector checks whether CMEK support is turned off for a Managed Service for Apache Spark cluster.  
`CONFIDENTIAL_COMPUTING_DISABLED` | This detector checks whether Confidential Computing is turned off.  
`KMS_PUBLIC_KEY` | This detector checks whether a Cloud Key Management Service cryptographic key is publicly accessible. For more information, see [KMS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#kms-findings).  
`SQL_INSTANCE_NOT_MONITORED` | This detector checks whether logging is turned off for Cloud SQL configuration changes.  
`SQL_TRACE_FLAG_3625` | This detector checks whether the `3625 (trace flag)` flag in Cloud SQL for SQL Server is disabled.  
`DEFAULT_NETWORK` | This detector checks whether the default network exists in a project.  
`DNSSEC_DISABLED` | This detector checks whether DNS security (DNSSEC) is turned off for Cloud DNS. For more information, see [DNS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dns-findings).  
`API_KEY_NOT_ROTATED` | This detector checks whether an API key has been rotated within the last 90 days.  
`SQL_LOG_CONNECTIONS_DISABLED` | This detector checks whether the `log_connections` flag in Cloud SQL for PostgreSQL is disabled.  
`LEGACY_NETWORK` | This detector checks whether a legacy network exists in a project.  
`IAM_ROOT_ACCESS_KEY_CHECK` | This detector checks whether IAM root access key is accessible.  
`PUBLIC_IP_ADDRESS` | This detector checks whether an instance has an external IP address.  
`OPEN_RDP_PORT` | This detector checks whether a firewall has an open RDP port.  
`INSTANCE_OS_LOGIN_DISABLED` | This detector checks whether OS Login is not turned on.  
`ADMIN_SERVICE_ACCOUNT` | This detector checks whether a service account has **Admin** , **Owner** , or **Editor** privileges.  
`SQL_USER_OPTIONS_CONFIGURED` | This detector checks whether the `user options` flag in Cloud SQL for SQL Server is configured.  
`FULL_API_ACCESS` | This detector checks whether an instance is using a default service account with full access to all Google Cloud APIs.  
`DEFAULT_SERVICE_ACCOUNT_USED` | This detector checks whether the default service account is being used.  
`NETWORK_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC network changes.  
`SQL_CONTAINED_DATABASE_AUTHENTICATION` | This detector checks whether the `contained database authentication` flag in Cloud SQL for SQL Server is enabled.  
`PUBLIC_BUCKET_ACL` | This detector checks whether a bucket is publicly accessible.  
`LOAD_BALANCER_LOGGING_DISABLED` | This detector checks whether logging is turned off for the load balancer.  
`OVER_PRIVILEGED_SERVICE_ACCOUNT_USER` | This detector checks whether a user has service account roles at the project level, instead of for a specific service account.  
`SQL_REMOTE_ACCESS_ENABLED` | This detector checks whether the `remote_access` flag in Cloud SQL for SQL Server is enabled.  
`CUSTOM_ROLE_NOT_MONITORED` | This detector checks whether logging is turned off for custom role changes.  
`AUTO_BACKUP_DISABLED` | This detector checks whether a Cloud SQL database doesn't have automatic backups turned on.  
`RSASHA1_FOR_SIGNING` | This detector checks whether RSASHA1 is used for key signing in Cloud DNS zones.  
`CLOUD_ASSET_API_DISABLED` | This detector checks whether Cloud Asset Inventory is turned off.  
`SQL_LOG_ERROR_VERBOSITY` | This detector checks whether the `log_error_verbosity` flag in Cloud SQL for PostgreSQL isn't set to `default`.  
`ROUTE_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC network route changes.  
`BUCKET_POLICY_ONLY_DISABLED` | This detector checks whether uniform bucket-level access is configured.  
`BUCKET_IAM_NOT_MONITORED` | This detector checks whether logging is turned off for IAM permission changes in Cloud Storage.  
`PUBLIC_SQL_INSTANCE` | This detector checks whether a Cloud SQL allows connections from all IP addresses.  
`SERVICE_ACCOUNT_ROLE_SEPARATION` | This detector checks for separation of duties for service account keys.  
`AUDIT_CONFIG_NOT_MONITORED` | This detector checks whether audit configuration changes are being monitored.  
`OWNER_NOT_MONITORED` | This detector checks whether logging is turned off for project ownership assignments and changes.  
  
## View the posture template

To view the posture template for NIST 800-53, do the following: 

### gcloud

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



Execute the [`gcloud scc posture-templates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc posture-templates describe \
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/nist_800_53

#### Windows (PowerShell)
    
    
    gcloud scc posture-templates describe `
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/nist_800_53

#### Windows (cmd.exe)
    
    
    gcloud scc posture-templates describe ^
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/nist_800_53

The response contains the posture template.

### REST

Before using any of the request data, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



HTTP method and URL: 
    
    
    GET https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/nist_800_53

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/nist_800_53"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/nist_800_53" | Select-Object -Expand Content

The response contains the posture template.

## What's next

  * [Create a security posture using this predefined posture template](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
