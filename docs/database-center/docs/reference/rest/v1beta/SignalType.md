---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType/
title: SignalType \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:29.298530+00:00
---

# SignalType  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  SignalType Stay organized with collections  Save and categorize content based on your preferences. 

Represents the type of a signal. More values are expected to be added as needed.

Enums  
---  
`SIGNAL_TYPE_UNSPECIFIED` | Unspecified.  
`SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED` | Represents if a resource is protected by automatic failover. Checks for resources that are configured to have redundancy within a region that enables automatic failover.  
`SIGNAL_TYPE_GROUP_MULTIREGIONAL` | Represents if a group is replicating across regions. Checks for resources that are configured to have redundancy, and ongoing replication, across regions.  
`SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY` | Represents if a resource has an automated backup policy.  
`SIGNAL_TYPE_SHORT_BACKUP_RETENTION` | Represents if a resources has a short backup retention period.  
`SIGNAL_TYPE_LAST_BACKUP_FAILED` | Represents if the last backup of a resource failed.  
`SIGNAL_TYPE_LAST_BACKUP_OLD` | Represents if the last backup of a resource is older than some threshold value.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0` | Represents if a resource violates CIS Google Cloud Platform Foundation 2.0.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.3.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.2.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.1.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.0.  
`SIGNAL_TYPE_VIOLATES_CIS_CONTROLS_V8_0` | Represents if a resource violates CIS Controls 8.0.  
`SIGNAL_TYPE_VIOLATES_NIST_800_53` | Represents if a resource violates NIST 800-53.  
`SIGNAL_TYPE_VIOLATES_NIST_800_53_R5` | Represents if a resource violates NIST 800-53 R5.  
`SIGNAL_TYPE_VIOLATES_NIST_CYBERSECURITY_FRAMEWORK_V1_0` | Represents if a resource violates NIST Cybersecurity Framework 1.0.  
`SIGNAL_TYPE_VIOLATES_ISO_27001` | Represents if a resource violates ISO-27001.  
`SIGNAL_TYPE_VIOLATES_ISO_27001_V2022` | Represents if a resource violates ISO 27001 2022.  
`SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1` | Represents if a resource violates PCI-DSS v3.2.1.  
`SIGNAL_TYPE_VIOLATES_PCI_DSS_V4_0` | Represents if a resource violates PCI-DSS v4.0.  
`SIGNAL_TYPE_VIOLATES_CLOUD_CONTROLS_MATRIX_V4` | Represents if a resource violates Cloud Controls Matrix v4.0.  
`SIGNAL_TYPE_VIOLATES_HIPAA` | Represents if a resource violates HIPAA.  
`SIGNAL_TYPE_VIOLATES_SOC2_V2017` | Represents if a resource violates SOC2 v2017.  
`SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING` | Represents if log_checkpoints database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED` | Represents if the log_duration database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_VERBOSE_ERROR_LOGGING` | Represents if the log_error_verbosity database flag for a Cloud SQL for PostgreSQL instance is not set to default or stricter (default or terse).  
`SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED` | Represents if the log_lock_waits database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_LOGGING_MOST_ERRORS` | Represents if the log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance is not set appropriately.  
`SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS` | Represents if the log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance does not have an appropriate severity level.  
`SIGNAL_TYPE_MINIMAL_ERROR_LOGGING` | Represents if the log_min_messages database flag for a Cloud SQL for PostgreSQL instance is not set to warning or another recommended value.  
`SIGNAL_TYPE_QUERY_STATS_LOGGED` | Represents if the databaseFlags property of instance metadata for the log_executor_status field is set to on.  
`SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME` | Represents if the log_hostname database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS` | Represents if the log_parser_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS` | Represents if the log_planner_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS` | Represents if the log_statement database flag for a Cloud SQL for PostgreSQL instance is not set to DDL (all data definition statements).  
`SIGNAL_TYPE_LOGGING_QUERY_STATS` | Represents if the log_statement_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES` | Represents if the log_temp_files database flag for a Cloud SQL for PostgreSQL instance is not set to "0". (NOTE: 0 = ON)  
`SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED` | Represents if the user connections database flag for a Cloud SQL for SQL Server instance is configured.  
`SIGNAL_TYPE_USER_OPTIONS_CONFIGURED` | Represents if the user options database flag for Cloud SQL SQL Server instance is configured or not.  
`SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS` | Represents if a resource is exposed to public access.  
`SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS` | Represents if a resources requires all incoming connections to use SSL or not.  
`SIGNAL_TYPE_NO_ROOT_PASSWORD` | Represents if a Cloud SQL database has a password configured for the root account or not.  
`SIGNAL_TYPE_WEAK_ROOT_PASSWORD` | Represents if a Cloud SQL database has a weak password configured for the root account.  
`SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED` | Represents if a SQL database instance is not encrypted with customer-managed encryption keys (CMEK).  
`SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED` | Represents if The contained database authentication database flag for a Cloud SQL for SQL Server instance is not set to off.  
`SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS` | Represents if he external scripts enabled database flag for a Cloud SQL for SQL Server instance is not set to off.  
`SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS` | Represents if the local_infile database flag for a Cloud SQL for MySQL instance is not set to off.  
`SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED` | Represents if the log_connections database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED` | Represents if the log_disconnections database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO` | Represents if the log_min_duration_statement database flag for a Cloud SQL for PostgreSQL instance is not set to -1.  
`SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS` | Represents if the remote access database flag for a Cloud SQL for SQL Server instance is not set to off.  
`SIGNAL_TYPE_DATABASE_NAMES_EXPOSED` | Represents if the skip_show_database database flag for a Cloud SQL for MySQL instance is not set to on.  
`SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED` | Represents if the 3625 (trace flag) database flag for a Cloud SQL for SQL Server instance is not set to on.  
`SIGNAL_TYPE_PUBLIC_IP_ENABLED` | Represents if public IP is enabled.  
`SIGNAL_TYPE_IDLE` | Represents idle instance helps to reduce costs.  
`SIGNAL_TYPE_OVERPROVISIONED` | Represents instances that are unnecessarily large for given workload.  
`SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES` | Represents high number of concurrently opened tables.  
`SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES` | Represents high table count close to SLA limit.  
`SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION` | Represents high number of unvacuumed transactions  
`SIGNAL_TYPE_UNDERPROVISIONED` | Represents need for more CPU and/or memory  
`SIGNAL_TYPE_OUT_OF_DISK` | Represents out of disk.  
`SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY` | Represents server certificate is near expiry.  
`SIGNAL_TYPE_DATABASE_AUDITING_DISABLED` | Represents database auditing is disabled.  
`SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS` | Represents not restricted to authorized networks.  
`SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP` | Represents violate org policy restrict public ip.  
`SIGNAL_TYPE_QUOTA_LIMIT` | Cluster nearing quota limit  
`SIGNAL_TYPE_NO_PASSWORD_POLICY` | No password policy set on resources  
`SIGNAL_TYPE_CONNECTIONS_PERFORMANCE_IMPACT` | Performance impact of connections settings  
`SIGNAL_TYPE_TMP_TABLES_PERFORMANCE_IMPACT` | Performance impact of temporary tables settings  
`SIGNAL_TYPE_TRANS_LOGS_PERFORMANCE_IMPACT` | Performance impact of transaction logs settings  
`SIGNAL_TYPE_HIGH_JOINS_WITHOUT_INDEXES` | Performance impact of high joins without indexes  
`SIGNAL_TYPE_SUPERUSER_WRITING_TO_USER_TABLES` | Detects events where a database superuser (postgres for PostgreSQL servers or root for MySQL users) writes to non-system tables.  
`SIGNAL_TYPE_USER_GRANTED_ALL_PERMISSIONS` | Detects events where a database user or role has been granted all privileges to a database, or to all tables, procedures, or functions in a schema.  
`SIGNAL_TYPE_DATA_EXPORT_TO_EXTERNAL_CLOUD_STORAGE_BUCKET` | Detects if database instance data exported to a Cloud Storage bucket outside of the organization.  
`SIGNAL_TYPE_DATA_EXPORT_TO_PUBLIC_CLOUD_STORAGE_BUCKET` | Detects if database instance data exported to a Cloud Storage bucket that is owned by the organization and is publicly accessible.  
`SIGNAL_TYPE_WEAK_PASSWORD_HASH_ALGORITHM` | Detects if a database instance is using a weak password hash algorithm.  
`SIGNAL_TYPE_NO_USER_PASSWORD_POLICY` | Detects if a database instance has no user password policy set.  
`SIGNAL_TYPE_HOT_NODE` | Detects if a database instance/cluster has a hot node.  
`SIGNAL_TYPE_NO_DELETION_PROTECTION` | Deletion Protection Disabled for the resource  
`SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY` | Detects if a database instance has no point in time recovery enabled.  
`SIGNAL_TYPE_RESOURCE_SUSPENDED` | Detects if a database instance/cluster has suspended resources.  
`SIGNAL_TYPE_EXPENSIVE_COMMANDS` | Detects that expensive commands are being run on a database instance impacting overall performance.  
`SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED` | Indicates that the instance does not have a maintenance policy configured.  
`SIGNAL_TYPE_INEFFICIENT_QUERY` | Indicates that the instance has inefficient queries detected.  
`SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD` | Indicates that the instance has read intensive workload.  
`SIGNAL_TYPE_MEMORY_LIMIT` | Indicates that the instance is nearing memory limit.  
`SIGNAL_TYPE_MAX_SERVER_MEMORY` | Indicates that the instance's max server memory is configured higher than the recommended value.  
`SIGNAL_TYPE_LARGE_ROWS` | Indicates that the database has large rows beyond the recommended limit.  
`SIGNAL_TYPE_HIGH_WRITE_PRESSURE` | Heavy write pressure on the database rows.  
`SIGNAL_TYPE_HIGH_READ_PRESSURE` | Heavy read pressure on the database rows.  
`SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED` | Encryption org policy not satisfied.  
`SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED` | Location org policy not satisfied.  
`SIGNAL_TYPE_OUTDATED_MINOR_VERSION` | Outdated DB minor version.  
`SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED` | Schema not optimized.  
`SIGNAL_TYPE_REPLICATION_LAG` | Replication delay.  
`SIGNAL_TYPE_OUTDATED_CLIENT` | Outdated client.  
`SIGNAL_TYPE_DATABOOST_DISABLED` | Databoost is disabled.  
`SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES` | Recommended maintenance policy.  
`SIGNAL_TYPE_EXTENDED_SUPPORT` | Resource version is in extended support.  
`SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE` | Represents a database version nearing end of life.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
