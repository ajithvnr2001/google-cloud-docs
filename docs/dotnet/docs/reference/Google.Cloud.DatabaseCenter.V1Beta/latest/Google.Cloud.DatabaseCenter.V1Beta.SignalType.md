---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalType
title: Database Center v1beta API - Enum SignalType (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:04.143588+00:00
---

# Database Center v1beta API - Enum SignalType (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Enum SignalType (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public enum SignalType

Reference documentation and code samples for the Database Center v1beta API enum SignalType.

Represents the type of a signal. More values are expected to be added as needed.

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Fields   
  
---  
**Name** | **Description**  
`ConnectionAttemptsNotLogged` | Represents if the log_connections database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`ConnectionMaxNotConfigured` | Represents if the user connections database flag for a Cloud SQL for SQL Server instance is configured.  
`ConnectionsPerformanceImpact` | Performance impact of connections settings  
`DataExportToExternalCloudStorageBucket` | Detects if database instance data exported to a Cloud Storage bucket outside of the organization.  
`DataExportToPublicCloudStorageBucket` | Detects if database instance data exported to a Cloud Storage bucket that is owned by the organization and is publicly accessible.  
`DatabaseAuditingDisabled` | Represents database auditing is disabled.  
`DatabaseNamesExposed` | Represents if the skip_show_database database flag for a Cloud SQL for MySQL instance is not set to on.  
`DataboostDisabled` | Databoost is disabled.  
`DisconnectionsNotLogged` | Represents if the log_disconnections database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`EncryptionKeyNotCustomerManaged` | Represents if a SQL database instance is not encrypted with customer-managed encryption keys (CMEK).  
`EncryptionOrgPolicyNotSatisfied` | Encryption org policy not satisfied.  
`ExcessiveLoggingOfClientHostname` | Represents if the log_hostname database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`ExcessiveLoggingOfParserStats` | Represents if the log_parser_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`ExcessiveLoggingOfPlannerStats` | Represents if the log_planner_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`ExpensiveCommands` | Detects that expensive commands are being run on a database instance impacting overall performance.  
`ExposedToExternalScripts` | Represents if he external scripts enabled database flag for a Cloud SQL for SQL Server instance is not set to off.  
`ExposedToLocalDataLoads` | Represents if the local_infile database flag for a Cloud SQL for MySQL instance is not set to off.  
`ExposedToPublicAccess` | Represents if a resource is exposed to public access.  
`ExposedToRemoteAccess` | Represents if the remote access database flag for a Cloud SQL for SQL Server instance is not set to off.  
`ExtendedSupport` | Resource version is in extended support.  
`GroupMultiregional` | Represents if a group is replicating across regions. Checks for resources that are configured to have redundancy, and ongoing replication, across regions.  
`HighJoinsWithoutIndexes` | Performance impact of high joins without indexes  
`HighNumberOfOpenTables` | Represents high number of concurrently opened tables.  
`HighNumberOfTables` | Represents high table count close to SLA limit.  
`HighReadPressure` | Heavy read pressure on the database rows.  
`HighTransactionIdUtilization` | Represents high number of unvacuumed transactions  
`HighWritePressure` | Heavy write pressure on the database rows.  
`HotNode` | Detects if a database instance/cluster has a hot node.  
`Idle` | Represents idle instance helps to reduce costs.  
`InefficientQuery` | Indicates that the instance has inefficient queries detected.  
`LargeRows` | Indicates that the database has large rows beyond the recommended limit.  
`LastBackupFailed` | Represents if the last backup of a resource failed.  
`LastBackupOld` | Represents if the last backup of a resource is older than some threshold value.  
`LocationOrgPolicyNotSatisfied` | Location org policy not satisfied.  
`LoggingExcessiveStatementInfo` | Represents if the log_min_duration_statement database flag for a Cloud SQL for PostgreSQL instance is not set to -1.  
`LoggingMostErrors` | Represents if the log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance is not set appropriately.  
`LoggingOnlyCriticalErrors` | Represents if the log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance does not have an appropriate severity level.  
`LoggingQueryStats` | Represents if the log_statement_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`LogsNotOptimizedForTroubleshooting` | Represents if log_checkpoints database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`MaxServerMemory` | Indicates that the instance's max server memory is configured higher than the recommended value.  
`MemoryLimit` | Indicates that the instance is nearing memory limit.  
`MinimalErrorLogging` | Represents if the log_min_messages database flag for a Cloud SQL for PostgreSQL instance is not set to warning or another recommended value.  
`NoAutomatedBackupPolicy` | Represents if a resource has an automated backup policy.  
`NoDeletionProtection` | Deletion Protection Disabled for the resource  
`NoMaintenancePolicyConfigured` | Indicates that the instance does not have a maintenance policy configured.  
`NoPasswordPolicy` | No password policy set on resources  
`NoPointInTimeRecovery` | Detects if a database instance has no point in time recovery enabled.  
`NoRootPassword` | Represents if a Cloud SQL database has a password configured for the root account or not.  
`NoUserPasswordPolicy` | Detects if a database instance has no user password policy set.  
`NotLoggingOnlyDdlStatements` | Represents if the log_statement database flag for a Cloud SQL for PostgreSQL instance is not set to DDL (all data definition statements).  
`NotLoggingTemporaryFiles` | Represents if the log_temp_files database flag for a Cloud SQL for PostgreSQL instance is not set to "0". (NOTE: 0 = ON)  
`OutOfDisk` | Represents out of disk.  
`OutdatedClient` | Outdated client.  
`OutdatedMinorVersion` | Outdated DB minor version.  
`Overprovisioned` | Represents instances that are unnecessarily large for given workload.  
`PublicIpEnabled` | Represents if public IP is enabled.  
`QueryDurationsNotLogged` | Represents if the log_duration database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`QueryLockWaitsNotLogged` | Represents if the log_lock_waits database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`QueryStatsLogged` | Represents if the databaseFlags property of instance metadata for the log_executor_status field is set to on.  
`QuotaLimit` | Cluster nearing quota limit  
`ReadIntensiveWorkload` | Indicates that the instance has read intensive workload.  
`RecommendedMaintenancePolicies` | Recommended maintenance policy.  
`ReplicationLag` | Replication delay.  
`ResourceFailoverProtected` | Represents if a resource is protected by automatic failover. Checks for resources that are configured to have redundancy within a region that enables automatic failover.  
`ResourceSuspended` | Detects if a database instance/cluster has suspended resources.  
`RestrictAuthorizedNetworks` | Represents not restricted to authorized networks.  
`SchemaNotOptimized` | Schema not optimized.  
`SensitiveTraceInfoNotMasked` | Represents if the 3625 (trace flag) database flag for a Cloud SQL for SQL Server instance is not set to on.  
`ServerAuthenticationNotRequired` | Represents if The contained database authentication database flag for a Cloud SQL for SQL Server instance is not set to off.  
`ServerCertificateNearExpiry` | Represents server certificate is near expiry.  
`ShortBackupRetention` | Represents if a resources has a short backup retention period.  
`SuperuserWritingToUserTables` | Detects events where a database superuser (postgres for PostgreSQL servers or root for MySQL users) writes to non-system tables.  
`TmpTablesPerformanceImpact` | Performance impact of temporary tables settings  
`TransLogsPerformanceImpact` | Performance impact of transaction logs settings  
`Underprovisioned` | Represents need for more CPU and/or memory  
`UnencryptedConnections` | Represents if a resources requires all incoming connections to use SSL or not.  
`Unspecified` | Unspecified.  
`UserGrantedAllPermissions` | Detects events where a database user or role has been granted all privileges to a database, or to all tables, procedures, or functions in a schema.  
`UserOptionsConfigured` | Represents if the user options database flag for Cloud SQL SQL Server instance is configured or not.  
`VerboseErrorLogging` | Represents if the log_error_verbosity database flag for a Cloud SQL for PostgreSQL instance is not set to default or stricter (default or terse).  
`VersionNearingEndOfLife` | Represents a database version nearing end of life.  
`ViolatePolicyRestrictPublicIp` | Represents violate org policy restrict public ip.  
`ViolatesCisControlsV80` | Represents if a resource violates CIS Controls 8.0.  
`ViolatesCisGcpFoundation10` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.0.  
`ViolatesCisGcpFoundation11` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.1.  
`ViolatesCisGcpFoundation12` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.2.  
`ViolatesCisGcpFoundation13` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.3.  
`ViolatesCisGcpFoundation20` | Represents if a resource violates CIS Google Cloud Platform Foundation 2.0.  
`ViolatesCloudControlsMatrixV4` | Represents if a resource violates Cloud Controls Matrix v4.0.  
`ViolatesHipaa` | Represents if a resource violates HIPAA.  
`ViolatesIso27001` | Represents if a resource violates ISO-27001.  
`ViolatesIso27001V2022` | Represents if a resource violates ISO 27001 2022.  
`ViolatesNist80053` | Represents if a resource violates NIST 800-53.  
`ViolatesNist80053R5` | Represents if a resource violates NIST 800-53 R5.  
`ViolatesNistCybersecurityFrameworkV10` | Represents if a resource violates NIST Cybersecurity Framework 1.0.  
`ViolatesPciDssV321` | Represents if a resource violates PCI-DSS v3.2.1.  
`ViolatesPciDssV40` | Represents if a resource violates PCI-DSS v4.0.  
`ViolatesSoc2V2017` | Represents if a resource violates SOC2 v2017.  
`WeakPasswordHashAlgorithm` | Detects if a database instance is using a weak password hash algorithm.  
`WeakRootPassword` | Represents if a Cloud SQL database has a weak password configured for the root account.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
