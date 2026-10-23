---
url: https://docs.cloud.google.com/sql/docs/mysql/troubleshooting/
title: Troubleshoot \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:16.797848+00:00
---

# Troubleshoot  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/troubleshooting "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshooting "View this page for the SQL Server database engine")

Check if your question or problem has already been addressed on one of the following pages: 

  * [FAQ](https://docs.cloud.google.com/sql/faq)
  * [Known issues](https://docs.cloud.google.com/sql/docs/mysql/known-issues)
  * [Error messages](https://docs.cloud.google.com/sql/docs/mysql/error-messages)
  * [Diagnose issues](https://docs.cloud.google.com/sql/docs/mysql/diagnose-issues)
  * [Debug connection issues](https://docs.cloud.google.com/sql/docs/mysql/debugging-connectivity)
  * [Orphan tables](https://docs.cloud.google.com/sql/docs/mysql/orphan-tables)
  * [Issues updating storage capacity](https://docs.cloud.google.com/sql/docs/mysql/issues-updating-storage-capacity)



Topics in this page include:

  * Backup and recovery
  * Cancel import and export
  * Cloning
  * Connectivity
  * Creating instances
  * Execute SQL using the Data API
  * External primary
  * External replica
  * Flags
  * High availability
  * Import and export
  * Logging
  * Managing instances
  * Private Service Connect
  * Replication



## Backup and recovery

Issue | Troubleshooting | You can't see the current operation's status. | The Google Cloud console reports only success or failure when the operation is done. It isn't designed to show warnings or other updates. Run the [ `gcloud sql operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/list) to list all operations for the given Cloud SQL instance.  
---|---  
You want to find out who issued an on-demand backup operation. | The user interface doesn't show the user who started an operation. Look in the [logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) and filter by text to find the user. You may need to use audit logs for private information. Relevant log files include:

  * `cloudsql.googlapis.com/mysql-general.log`
  * `cloudsql.googleapis.com/mysql.err`
  * If [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) is enabled and you have the required permissions to view them, `cloudaudit.googleapis.com/activity` may also be available. 

  
After an instance is deleted, you can't take a backup of the instance. | If you delete an instance without taking a [final backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#final-backups) of the data, then no data recovery is possible. However, if you restore the instance, then Cloud SQL also restores the backups. For more information on recovering a deleted instance, see [Retain backups after instance deletion](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retained-backups). If you have done an export operation, create a new instance and then do an import operation to recreate the database. Exports are written to Cloud Storage and imports are read from there. **Note:** Cloud SQL recommends that you take a final backup of your data before you delete the instance. This way, you can recreate any instances that you delete accidentally without contacting [Cloud Customer Care](https://docs.cloud.google.com/support).  
An automated backup is stuck for many hours and can't be canceled. | Backups can take a long time depending on the database size. If you really need to cancel the operation, you can ask [ customer support](https://docs.cloud.google.com/sql/docs/getting-support) to `force restart` the instance.  
A restore operation can fail when one or more users referenced in the SQL dump file don't exist. | Before restoring a SQL dump, all the database users who own objects or were granted permissions on objects in the dumped database must exist in the target database. If they don't, the restore operation fails to recreate the objects with the original ownership or permissions. [ Create the database users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) before restoring the SQL dump.  
You want to increase the number of days that you can keep automatic backups from seven to 30 days, or longer. | You can [ configure the number of automated backups to retain](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention), from 1 to 365. Automated backups get pruned regularly based on the retention value configured. Unfortunately, this means that the currently visible backups are the only automated backups you can restore from. To keep backups indefinitely, you can [create an on-demand backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#on-demand), as they are not deleted in the same way as automated backups. On-demand backups remain indefinitely. That is, they remain until they're deleted or the instance they belong to is deleted. Because that type of backup is not deleted automatically, it can affect billing.  
An automated backup failed and you didn't receive an email notification. | To have Cloud SQL notify you of the backup's status, [configure a log-based alert](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/view-audit-logs-for-automated-backups#configure-log-based).   
An automated or on-demand backup fails on an instance with more than 50 user-defined labels. | When Cloud SQL takes a backup, it copies your instance's user-defined labels to the underlying storage snapshot and appends internal system labels. If the combined number of labels exceeds the 64-label snapshot limit, the backup fails. To resolve this issue, remove excess labels so that the instance has 50 or fewer user-defined labels. For more information, see [Label instances](https://docs.cloud.google.com/sql/docs/mysql/label-instance#restrictions).  
Unable to delete an instance when you elect to take a final backup at instance deletion.  |  When you delete an instance, you're required to confirm whether you want to take a final backup for your instance prior to deleting it. If you enabled final backup using the `final-backup` instance setting, then the selection you make when you delete your instance must match the final backup instance configuration you set when you enabled final backup for your instance. To mitigate this issue, do one of the following:  


  * Set the final backup value to match the instance's existing backup configuration.
  * Leave the final backup field empty when you delete your instance. If you leave the field empty, then Cloud SQL takes the final backup configuration set in instance settings to take a final backup and define its retention.

To view your instance's final backup instance configuration, see [View instance information](https://docs.cloud.google.com/sql/docs/mysql/instance-info#console).   
Unable to create a replica instance after successfully creating a primary instance with the final backup setting.  |  If you create a new instance with the final backup instance setting enabled, then you must update the final backup organization policy to apply the backup configurations to the primary instance only. Final backups aren't supported for replica instances.  
For more information, see [Cloud SQL organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy).   
  
## Cancel import and export

Issue | Troubleshooting | Error message: `You can't cancel operation [operation-ID] because this operation isn't in progress.` |  You're trying to cancel an import or export operation that's completed, failed, or cancelled. If the operation is running, you can cancel it.  
---|---  
Error message: `You can't cancel operation [operation-ID] because Cloud SQL doesn't support the cancellation of an [operation-type] operation.` | Cloud SQL doesn't support the cancellation of the operation because it has an [operation type](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations#sqloperationtype) other than `IMPORT` or `EXPORT`.  
Error message: `The [operation-type] operation isn't cancelled. Wait and retry in a few seconds.` |  Cloud SQL can't cancel the import or export operation at this time. Try again in a few seconds. If the problem persists, contact [Google Cloud Support](https://docs.cloud.google.com/support).  
  
## Clone

Issue | Troubleshooting | Cloning fails with `constraints/sql.restrictAuthorizedNetworks` error. | The cloning operation is blocked by the `Authorized Networks` configuration. `Authorized Networks` are configured for public IP addresses in the Connectivity section of the Google Cloud console, and cloning is not permitted due to [security considerations](https://docs.cloud.google.com/sql/docs/mysql/connection-org-policy). Remove all `Authorized Networks` entries from the Cloud SQL instance if you can. Otherwise, [create a replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica) without any `Authorized Networks` entries.  
---|---  
Error message: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges. Please allocate new ranges for this service provider. Help Token: [help-token-id].` |  You're trying to use the Google Cloud console to clone an instance with a private IP address, but you didn't specify the allocated IP range that you want to use and the source instance isn't created with the specified range. As a result, the cloned instance is created in a random range. Use `gcloud` to clone the instance and provide a value for the   
`--allocated-ip-range-name` parameter. For more information, see [Cloning an instance with a private IP](https://docs.cloud.google.com/sql/docs/mysql/clone-instance#gcloud_1).  
  
## Connect

Issue | Troubleshooting | `Aborted connection`. | The issue might be: 

  * Networking instability.
  * No response to TCP keep-alive commands (either the client or the server isn't responsive, possibly overloaded)
  * The database engine connection lifetime was exceeded and the server ends the connection.

Applications must tolerate network failures and follow [best practices](https://docs.cloud.google.com/sql/docs/mysql/manage-connections) such as connection pooling and retrying. Most connection poolers catch these errors where possible. Otherwise the application must either retry or fail gracefully. For connection retry, we recommend the following methods:

  1. [Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff). Increase the time interval between each retry, exponentially.
  2. Add randomized backoff also.

Combining these methods helps reduce throttling.  
---|---  
Connection timeout or generic connection error when using private IP or VPC Network Peering. | Connection attempts fail with generic timeout or connection errors without diagnostic details. **Troubleshooting steps:**

  1. Run a [Network Intelligence Center Connectivity Test](https://docs.cloud.google.com/sql/docs/mysql/debugging-connectivity#diagnose-vpc-connectivity) between the source client and the Cloud SQL private IP on the database port (3306 for MySQL, 5432 for PostgreSQL, or 1433 for SQL Server). The test traces the packet path and identifies whether traffic is dropped by firewall rules, missing routes, or peering misconfigurations.
  2. Verify that the VPC Network Peering connection status is `ACTIVE`.
  3. Verify that firewall rules in the VPC network allow ingress traffic on the database port.
  4. If using non-RFC 1918 address ranges, verify that you updated the peering configuration to export subnet routes with public IP.

For more details and gcloud diagnostic commands, see [Diagnose VPC network and private IP connection failures](https://docs.cloud.google.com/sql/docs/mysql/debugging-connectivity#diagnose-vpc-connectivity).  
Error message: `Login failed for user ""` | You might encounter this login error during [Microsoft Entra ID authentication](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id). To resolve this issue, make sure that a SQL Server login exists for this Microsoft Entra ID user.  
Network connectivity issues with private IP instances | You might experience some of the following issues during integration setup: 

  * Slow operations to create Microsoft Entra ID logins
  * Unable to create Microsoft Entra ID logins
  * Unable to connect to the instance using Microsoft Entra ID authentication

For more information on how to help address these issues, see [Troubleshooting Microsoft Entra ID integration](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id).  
`Certificate verify failed`. | The client certificates have expired or the path to the certificates isn't correct. Regenerate the certificates by [recreating them](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#new-client).  
Slow connection establishment or connection timeouts when using IAM database authentication. | Connecting to a Cloud SQL instance using IAM database authentication takes several seconds or times out, while built-in database authentication connects normally. **Cause** : The instance is using a shared-core machine type (`db-f1-micro` or `db-g1-small`). Under CPU throttling, IAM database authentication takes longer to complete than built-in password authentication because it is more computationally intensive. **Resolution** :

  * Use [connection pooling](https://docs.cloud.google.com/sql/docs/mysql/manage-connections) or connect through the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy) to reuse authenticated connections.
  * Increase the client connection timeout (for example, to 10–15 seconds).
  * [Edit your instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance) to use a dedicated-core [machine type](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen) (such as `db-custom-*` or `db-n1-standard-*`).

For more information, see [Performance on shared-core instances](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-shared-core-performance).  
  
## Create instances

Issue | Troubleshooting | Error message: `The zone or region does not have sufficient resources to handle the request at the moment.` | The selected zone lacks capacity for the requested resources or the VM type at the time of the instance creation request. There might be simultaneous high operational demand in that specific regional location at the time of request. To resolve this issue, retry creating the instance in another zone or retry creating the instance in the same zone that received the error at a different time of day.  
---|---  
Error message: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges. Please allocate new ranges for this service provider`. | There are no more available addresses in the allocated IP range. There can be several possible scenarios: 

  * The size of the allocated IP range for the private service connection is smaller than /24.
  * The size of the allocated IP range for the private service connection is too small for the number of Cloud SQL instances.
  * The requirement on the size of allocated IP range will be larger if instances are created in multiple regions. See [allocated range size](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated_range_size)

To resolve this issue, you can either expand the existing allocated IP range or allocate an additional IP range to the private service connection. For more information, see [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access#allocate-ip-address-range). If you used the `--allocated-ip-range-name` flag while creating the Cloud SQL instance, you may only expand the specified IP range. If you're allocating a new range, take care that the allocation doesn't overlap with any existing allocations. After creating a new IP range, update the vpc peering with the following command:
    
    
    gcloud services vpc-peerings update \
    --service=servicenetworking.googleapis.com \
    --ranges=OLD_RESERVED_RANGE_NAME,NEW_RESERVED_RANGE_NAME \
    --network=VPC_NETWORK \
    --project=PROJECT_ID \
    --force
        

If you're expanding an existing allocation, take care to increase only the allocation range and not decrease it. For example, if the original allocation was 10.0.10.0/24, then make the new allocation at least 10.0.10.0/23. In general, if starting from a /24 allocation, decrementing the /mask by 1 for each condition (additional instance type group, additional region) is a good rule of thumb. For example, if trying to create both instance type groups on the same allocation, going from /24 to /23 is enough.  After expanding an existing IP range, update the vpc peering with following command:
    
    
    gcloud services vpc-peerings update \
    --service=servicenetworking.googleapis.com \
    --ranges=RESERVED_RANGE_NAME \
    --network=VPC_NETWORK \
    --project=PROJECT_ID
          
  
Error message: `Failed to create subnetwork. Router status is temporarily unavailable. Please try again later. Help Token: [token-ID]`. | Try to create the Cloud SQL instance again.  
Error message: `HTTPError 400: Invalid request: Incorrect Service Networking config for instance: PROJECT_ID:INSTANCE_NAME:SERVICE_NETWORKING_NOT_ENABLED.` |  Enable the [Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) using the following command and try to create the Cloud SQL instance again.
    
    
    gcloud services enable servicenetworking.googleapis.com \
    --project=PROJECT_ID
          
  
Error message: `Failed to create subnetwork. Required 'compute.projects.get' permission for PROJECT_ID`. | When you create an instance using with a Private IP address, a service account is created just-in-time using the Service Networking API. If you have only recently enabled the Service Networking API, then the service account might not get created and the instance creation fails. In this case, you must wait for the service account to propagate throughout the system or manually add it with the required permissions.  
Error message: `More than 3 subject alternative names are not allowed.` | You're trying to use a custom SAN to add more than three DNS names to the server certificate of a Cloud SQL instance. You can't add more than three DNS names to the instance.  
Error message: `Subject alternative names %s is too long. The maximum length is 253 characters.` | Make sure that any DNS names that you want to add to the server certificate of a Cloud SQL instance don't have more than 253 characters.  
Error message: `Subject alternative name %s is invalid.` | Verify that the DNS names that you want to add to the server certificate of a Cloud SQL instance meet the following criteria:

  * They don't have wildcard characters.
  * They don't have trailing dots.
  * They meet [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) specifications.

  
  
## Execute SQL using the Data API

Issue | Troubleshooting |  `The instance doesn't allow using ExecuteSql to access this instance. You can allow it by patching the instance with {settings: { dataApiAccess: "ALLOW_DATA_API" }}` |  The Data API is disabled by default. [Enable the Data API](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance#enable-disable-data-api) on the instance to resolve the issue.   
---|---  
`Secret cannot be provided when auto_iam_authn is true.` | When you set `auto_iam_authn` to `true`, you are authenticating to the database using IAM. This authentication method doesn't require a password or secret. See [ Authenticate using IAM](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance#authenticate-using-iam).   
`ExecuteSql API is not supported for instances in certain Assured Workloads control packages folders yet.` |  The SQL script and its execution response might transit through intermediate locations between your client and the location of the target instance. For this reason, requests will fail for instances in certain Assured Workloads projects. If your project is not enrolled in Assured Workloads but `constraints/sql.restrictNoncompliantResourceCreation` is manually enforced, then ask your organization's administrator to remove the constraint and the issue will be resolved on newly created instances.   
`IAM authentication is not enabled for the instance` |  [Configure the instance for IAM authentication](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance#configure-db-user) to resolve the issue.   
`The database is currently unavailable.` |  The instance might be restarting, undergoing maintenance, or in an unhealthy state. Check the instance's status and try again later.   
  
## Export

Issue | Troubleshooting | `HTTP Error 409: Operation failed because another operation was already in progress.` | There is already a pending operation for your instance. Only one operation is allowed at a time. Try your request after the current operation is complete.  
---|---  
`HTTP Error 403: The service account does not have the required permissions for the bucket.` | Ensure that the bucket exists and the service account for the Cloud SQL instance (which is performing the export) has the `Storage Object Creator` role (`roles/storage.objectCreator`) to allow export to the bucket. See [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).  
CSV export worked but SQL export failed. | CSV and SQL formats do export differently. The SQL format exports the entire database, and likely takes longer to complete. The CSV format lets you define which elements of the database to include in the export. [Use CSV exports](https://docs.cloud.google.com/sql/docs/mysql/import-export/exporting#csv) to export only what you need.  
Export is taking too long. | Cloud SQL does not support concurrent synchronous operations. Use [ export offloading](https://docs.cloud.google.com/sql/docs/mysql/import-export#best_practices_for_importing_and_exporting). At a high level, in export offloading, instead of issuing an export on the source instance, Cloud SQL spins up an offload instance to perform the export. Export offloading has several advantages, including increased performance on the source instance and the unblocking of administrative operations while the export is running. With export offloading, total latency can increase by the amount of time it takes to bring up the offload instance. Generally, for reasonably sized exports, latency is not significant. However, if your export is small enough, then you may notice the increase in latency.  
You want exports to be automated. | Cloud SQL does not provide a way to automate exports. You could build your own automated export system using Google Cloud products such as Cloud Scheduler, Pub/Sub, and Cloud Run functions, similar to this article on [ automating backups](https://betterprogramming.pub/how-to-automate-google-cloud-sql-backups-2de6d3cc7d01).  
  
## External primary

Issue | Troubleshooting | `Lost connection to MySQL server during query when dumping table`. | The source may have become unavailable, or the dump contained packets too large. Make sure the external primary is available to connect. You can also modify the values of the [net_read_timeout](https://dev.mysql.com/doc/refman/8.4/en/server-system-variables.html#sysvar_net_read_timeout) and [net_write_timeout](https://dev.mysql.com/doc/refman/8.4/en/server-system-variables.html#sysvar_net_write_timeout) flags on the source instance to stop the error. For more information on the allowable values for these flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags). To learn more about using `mysqldump` flags for managed import migration, see [ Allowed and default initial sync flags](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external#sync-flags)  
---|---  
Initial dump fails with timeout or lost connection errors (for example, `Dump timeout` or `Lost connection to MySQL server`). | This error can occur if one or more DDL statements interact with the parallel dump process, causing the process to wait indefinitely. **Resolution:** Don't execute DDL statements on the source database during the initial dump phase. Before you execute any DDL statements, restart the migration and wait for the initial dump phase to complete.  
The initial data migration was successful, but no data is being replicated. | One possible root cause could be your source database has defined replication flags which result in some or all database changes not being replicated over. Make sure the replication flags such as `binlog-do-db`, `binlog-ignore-db`, `replicate-do-db` or `replicate-ignore-db` are not set in a conflicting way. Run the command `show master status` on the primary instance to see the current settings.  
The initial data migration was successful but data replication stops working after a while. | Things to try:

  * Check the [ replication metrics](https://console.cloud.google.com/monitoring/dashboards/resourceList/cloudsql_database) for your replica instance in the Cloud Monitoring section of the Google Cloud console.
  * The errors from the MySQL IO thread or SQL thread can be found in [Cloud Logging](https://console.cloud.google.com/logs) in the `mysql.err` log files.
  * The error can also be found when connecting to the replica instance. Run the command `SHOW REPLICA STATUS`, and check for the following fields in the output: 
    * `Replica_IO_Running`
    * `Replica_SQL_Running`
    * `Last_IO_Error`
    * `Last_SQL_Error`

If you find the error `Unknown database DATABASE_NAME on query. Error_code: MY-001049`, then replication has failed due to a replicated SQL statement attempting to reference a database that wasn't selected for the migration. To recover replication, determine whether the error based on the message is due to DDL on one of the following objects:

  * An event or routine. You can run [`CALL mysql.skipReplicationError()`](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures#skipReplicationError) on the replica, which will prevent the event or routine from being replicated and resume replication.
  * A foreign key constraint or view. After you determine on which database the object modified by the statement resides, you have two options for recovery. You can either remove the database from the selected databases that are being migrated, or you can run [`CALL mysql.skipReplicationError()`](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures#skipReplicationError) on the replica to resume replication while skipping the constraint or propagation of the view to the replica.

  
`mysqld check failed: data disk is full`. | The data disk of the replica instance is full. Increase the disk size of the replica instance. You can either manually increase the disk size or enable auto storage increase.  
  
## External replica

Issue | Troubleshooting | Error message: `The slave is connecting ... master has purged binary logs containing GTIDs that the slave requires`. | The primary Cloud SQL instance has automatic backups and binary logs and point-in-time recovery is enabled, so it should have enough logs for the replica to be able to catch up. However, in this case although the binary logs exist, the replica doesn't know which row to start reading from. Create a new dump file using the correct flag settings, and configure the external replica using that file 

  1. Connect to your mysql client [through a Compute Engine instance](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine).
  2. [Run mysqldump](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html) and use the `--master-data=1` and `--flush-privileges` flags. **Important: Do not include the`--set-gtid-purged=OFF` flag**. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/import-export/exporting#export-mysqldump).
  3. Ensure that the dump file just created contains the `SET @@GLOBAL.GTID_PURGED='...'` line.
  4. Upload the dump file to a Cloud Storage bucket and [ configure the replica using the dump file](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica#configuring_the_external_replica).

  
---|---  
  
## Flags

Issue | Troubleshooting | After enabling a flag the instance loops between panicking and crashing. | Contact [ customer support](https://docs.cloud.google.com/sql/docs/getting-support) to request flag removal followed by a `hard drain`. This forces the instance to restart on a different host with a fresh configuration without the undesired flag or setting.   
---|---  
You see the error message `Bad syntax for dict arg` when trying to set a flag. | [ Complex parameter values](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file), such as comma-separated lists, require special treatment when used with gcloud commands.   
  
## High availability

Issue | Troubleshooting | You can't find the metrics for a manual failover. | Only automatic failovers go into the metrics.  
---|---  
Cloud SQL instance resources (CPU and RAM) are near 100% usage, causing the high availability instance to go down. | The instance machine size is too small for the load. [ Edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to upgrade to a larger machine size to get more CPUs and memory.   
  
## Import

Issue | Troubleshooting | `HTTP Error 409: Operation failed because another operation was already in progress`. | There is already a pending operation for your instance. Only one operation is allowed at a time. Try your request after the current operation is complete.  
---|---  
The import operation is taking too long. | Too many active connections can interfere with import operations. Close unused operations. Check the CPU and memory usage of your Cloud SQL instance to make sure there are plenty of resources available. The best way to ensure maximum resources for the import is to restart the instance before beginning the operation. A restart:

  * Closes all connections.
  * Ends any tasks that may be consuming resources.

  
An import operation can fail when one or more users referenced in the dump file don't exist. | Before importing a dump file, all the database users who own objects or were granted permissions on objects in the dumped database must exist in the target database. If they don't, the import operation fails to recreate the objects with the original ownership or permissions. [ Create the database users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) before importing.  
An import operation fails with an error that a table doesn't exist. | Tables can have foreign key dependencies on other tables, and depending on the order of operations, one or more of those tables might not yet exist during the import operation. Things to try: Add the following line at the start of the dump file:
    
    
    SET FOREIGN_KEY_CHECKS=0;
      

Additionally, add this line at the end of the dump file:
    
    
    SET FOREIGN_KEY_CHECKS=1;
      

These settings deactivate data integrity checks while the import operation is in progress, and reactivate them after the data is loaded. This doesn't affect the integrity of the data on the database, because the data was already validated during the creation of the dump file.  
  
## Integrate with Vertex AI

Issue | Troubleshooting  
---|---  
Error message: `Google ML integration API is supported only on MySQL version 8.0.36 or above.` | To enable the Vertex AI integration in Cloud SQL, you must have a Cloud SQL for MySQL database, version 8.0.36 or later. To upgrade your database to this version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).  
Error message: `Google ML Integration API is not supported on shared core instance. Please upsize your machine type.` | If you selected a shared core for the machine type of your instance, then you can't enable the Vertex AI integration in Cloud SQL. Upgrade your machine type to dedicated core. For more information, see [Machine Type](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen).  
Error message: `Google ML Integration is unsupported for this maintenance version. Please follow https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance to update the maintenance version of the instance.` | To enable the Vertex AI integration in Cloud SQL, the maintenance version of your instance must be `R20240130` or later. To upgrade your instance to this version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).  
Error message: `**Cannot invoke ml_predict_row if 'cloudsql.enable_google_ml_integration' is off.**` | The `cloudsql.enable_google_ml_integration `database flag is turned off. Cloud SQL can't integrate with Vertex AI.  
  
To turn this flag on, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:  
  
`gcloud sql instances patch INSTANCE_NAME --database-flags cloudsql.enable_google_ml_integration=on`  
  
Replace INSTANCE_NAME with the name of the primary Cloud SQL instance.  
Error message: `**Failed to connect to remote host: Connection refused.**` | The integration between Cloud SQL and Vertex AI isn't enabled. To enable this integration, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:  
  
`gcloud sql instances patch INSTANCE_NAME   
--enable-google-ml-integration `  
  
Replace INSTANCE_NAME with the name of the primary Cloud SQL instance.  
Error message: `**Vertex AI API has not been used in project PROJECT_ID before or it is disabled. Enable it by visiting /apis/api/aiplatform.googleapis.com/overview?project=PROJECT_ID then retry.**` | The Vertex AI API isn't enabled. For more information on enabling this API, see [Enable database integration with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai#enable-database-integration-with-vertex-ai).  
Error message: `**Permission 'aiplatform.endpoints.predict' denied on resource.**` | Vertex AI permissions aren't added to the Cloud SQL service account for the project where the Cloud SQL instance is located. For more information on adding these permissions to the service account, see [Grant the Cloud SQL service account Identity and Access Management (IAM) permissions to access Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai#grant-service-account).  
Error message: `**Publisher Model `projects/ PROJECT_ID/locations/REGION_NAME/publishers/google/models/MODEL_NAME` not found.**` | The machine learning model or the LLM doesn't exist in Vertex AI.   
Error message: `**Resource exhausted: grpc: received message larger than max.**` | The size of the request that Cloud SQL passes to Vertex AI exceeds the [gRPC](https://grpc.io/) limit of 4 MB per request.  
Error message: `**Cloud SQL attempts to send a request to Vertex AI. However, the instance is in the %s region, but the Vertex AI endpoint is in the %s region. Make sure the instance and endpoint are in the same region.**` | Cloud SQL attempts to send a request to Vertex AI. However, the instance is in one region, but the Vertex AI endpoint is in a different region. To resolve this issue, both the instance and endpoint must be in the same region.  
Error message: `**The Vertex AI endpoint isn't formatted properly.**` | The Vertex AI endpoint isn't formatted properly. For more information, see [Use private endpoints for online prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints).   
Error message: `**Quota exceeded for aiplatform.googleapis.com/online_prediction_requests_per_base_model with base model: textembedding-gecko.**` | The number of requests that Cloud SQL passes to Vertex AI exceeds the limit of 1,500 requests per minute per region per model per project.  
Error message: `**execute command denied to user DB_USER for routine 'mysql.ml_embedding'.**` | The MySQL database user doesn't have the necessary privileges to call the `mysql.ml_embedding` function. See [the required grants](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai#before-you-begin).  
  
## Logging

Issue | Troubleshooting  
Audit logs are not found. | Data-Access logs are only written if the operation is an authenticated user-driven API call that creates, modifies, or reads user-created data, or if the operation accesses configuration files or metadata of resources.   
Operations information is not found in logs. | You want to find more information about an operation. For example, a user was deleted but you can't find out who did it. The logs show the operation started but don't provide any more information. You must [enable audit logging](https://docs.cloud.google.com/logging/docs/audit) for detailed and personal identifying information (PII) like this to be logged.  
Logging is using a lot of disk space. | There are three kinds of log files that use disk space: redo logs, general logs and binary logs. Connect to the database and run these commands for details on each type:
    
    
    SHOW VARIABLES LIKE 'innodb_log_file%';
    
    SELECT ROUND(SUM(LENGTH(argument)/POW(1024,2),2)
    AS GB from mysql.general_log;
    
    SHOW BINARY LOGS;
          
  
Log files are hard to read. | You'd rather view the logs as json or text.You can use the [ `gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command along with linux post-processing commands to download the logs. To download the logs as JSON:
    
    
    gcloud logging read \
    "resource.type=cloudsql_database \
    AND logName=projects/PROJECT_ID \
    /logs/cloudsql.googleapis.com%2FLOG_NAME" \
    --format json \
    --project=PROJECT_ID \
    --freshness="1d" \
    > downloaded-log.json
        

To download the logs as TEXT:
    
    
    gcloud logging read \
    "resource.type=cloudsql_database \
    AND logName=projects/PROJECT_ID \
    /logs/cloudsql.googleapis.com%2FLOG_NAME" \
    --format json \
    --project=PROJECT_ID \
    --freshness="1d"| jq -rnc --stream 'fromstream(1|truncate_stream(inputs)) \
    | .textPayload' \
    --order=asc
    > downloaded-log.txt
         
  
## Manage instances

Issue | Troubleshooting | You want to find out what is using up storage. | For example, you notice that your database is using only 3 GB, but storage shows that 14 GB is being used. Space not used by database tables is typically used by transaction logs, temporary files, or other logs. You can view a breakdown of instance disk usage by data type using the [`cloudsql.googleapis.com/database/disk/bytes_used_by_data_type`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics) metric in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) or the **Disk storage by type** chart on the [System insights](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights#default-metrics) dashboard. Things to try:

  * For Cloud SQL for MySQL, the `database/disk/bytes_used_by_data_type` metric breaks down storage usage across `Data`, `Binlog`, `Tmp_data`, `Temporary files`, `Redo_log`, `Undo_log`, `General_log`, `Slow_log`, `Relaylog`, `Cloudsql_mysql_audit_log`, and `Other`. For more information, see [Troubleshoot high disk usage](https://docs.cloud.google.com/sql/docs/mysql/high-disk-usage). 
  * You can check the storage occupied by binary logs using the following command in the MySQL command-line interface: `SHOW BINARY LOGS;`
  * Temporary tables might also be occupying a significant amount of storage space. To check the temporary space usage, use the following command: `SELECT * FROM INFORMATION_SCHEMA.FILES WHERE TABLESPACE_NAME='innodb_temporary'\G`. 
  * The following command lets you check the redo log size: `SHOW VARIABLES LIKE 'innodb_log_file%';`
  * You can check the size of `general_log`, if it is enabled, with the help of this command: `SELECT ROUND(SUM(LENGTH(argument)/POW(1024,2)),2) AS GB from mysql.general_log;`
  * If needed, you can truncate your log tables by using the API. For more information, see the [instances.truncateLog reference page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/truncateLog). 
  * Learn more about [setting](https://docs.cloud.google.com/sql/docs/mysql/flags#tips) and [ configuring](https://docs.cloud.google.com/architecture/security-log-analytics) slow-query logs.

  
---|---  
Slow performance after restarting MySQL. | Cloud SQL allows caching of data in the InnoDB buffer pool. However, after a restart, this cache is always empty, and all reads require a round trip to the backend to get data. As a result, queries can be slower than expected until the cache is filled.   
Slow crash recovery. | A large `general_log` may have accumulated. You can reduce crash recovery time by preventing a large `general_log` from accumulating. If you have `general_log` on, truncate the table and only enable `general_log` for short periods of time. You can find out the size of the general logs by connecting to the database and running this query: `SELECT ROUND(SUM(LENGTH(argument)/POW(1024,2)),2) from mysql.general_log;`  
Queries are blocked. | It's possible for queries to lock the MySQL database causing all subsequent queries to block/timeout. Connect to the database and execute this query:  `SHOW PROCESSLIST`. The first item in the list may be the one holding the lock, which the subsequent items are waiting on. The `SHOW INNODB STATUS` query can also be helpful.  
You are unable to manually delete binary logs. | Binary logs cannot be manually deleted. Binary logs are automatically deleted with their associated automatic backup, which generally happens after about seven days.   
You want to find information about temporary files. | A file named `ibtmp1` is used for storing temporary data. This file is reset upon database restart. To find information about temporary file usage, connect to the database and execute the following query: `SELECT * FROM INFORMATION_SCHEMA.FILES WHERE TABLESPACE_NAME='innodb_temporary'\G`  
You want to find out about table sizes. | This information is available in the database. Connect to the database and execute the following query: `SELECT TABLE_SCHEMA, TABLE_NAME, sum(DATA_LENGTH+INDEX_LENGTH)/pow(1024,2) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT IN ('PERFORMANCE_SCHEMA','INFORMATION_SCHEMA','SYS','MYSQL') GROUP BY TABLE_SCHEMA, TABLE_NAME;`  
mysqld got a signal 11. | Try refactoring queries so that they don't create too many connections. If that doesn't resolve the issue, contact [customer support](https://docs.cloud.google.com/sql/docs/getting-support). Signal 11 usually represents a MySQL software issue.   
`InnoDB: page_cleaner: 1000ms intended loop took 5215ms. The settings might not be optimal.` | The page cleaner can't keep up with the rate of change on the instance. Once per second, the page cleaner scans the buffer pool for dirty pages to flush from the buffer pool to disk. The warning you see shows it has lots of dirty pages to flush, and it's taking more than one second to flush a batch of them to disk. [Shard the instance](https://docs.cloud.google.com/sql/docs/mysql/best-practices#data-arch) if possible. Using many smaller Cloud SQL instances is better than one large instance.  
Temporary storage increased automatic storage. | Automatic storage is enabled. Restart deletes the temporary files but not reduce the storage. Only [ customer support](https://docs.cloud.google.com/sql/docs/getting-support) can reset the instance size.  
Data is being automatically deleted. | Most likely a script is running somewhere in your environment. Look in the logs around the time of the deletion and see if there's a rogue script running from a dashboard or another automated process.  
The instance cannot be deleted. | You might see the error message `ERROR: (gcloud.sql.instances.delete) HTTP Error 409: The instance or operation is not in an appropriate state to handle the request`, or the instance may have a `INSTANCE_RISKY_FLAG_CONFIG` flag status. Some possible explanations include:

  * Another operation is in progress. Cloud SQL operations do not run concurrently. Wait for the other operation to complete.
  * The `INSTANCE_RISKY_FLAG_CONFIG` warning is triggered whenever at least one `beta` flag is being used. Remove the risky flag settings and restart the instance

  
The instance is stuck due to large temporary data size. | The system can create many temporary tables at one time, depending on the queries and the load. Unfortunately, you can't shrink the `ibtmp1` file by any method other than restarting the service. One mitigation option is to create the temporary table with `ROW_FORMAT=COMPRESSED`, so it is stored in file-per-table tablespaces in the temporary file directory. However, the downside is performance costs associated with creating and removing a file-per-table tablespace for each temporary table.  
Fatal error during upgrade. | Logs may reveal more, but in any case [customer support](https://docs.cloud.google.com/sql/docs/getting-support) may be needed to force re-create the instance.   
Instance is stuck on restart after running out of disk space. | Automatic storage increase capability isn't enabled. If your instance runs out of storage, and the automatic storage increase capability isn't enabled, your instance goes offline. To avoid this issue, you can [ edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to enable automatic storage increase.  
Your on-premises primary instance is stuck. | Google Cloud can't help with instances that are not in Cloud SQL.   
Slow shutdown on restart. | When an instance shuts down, any outstanding connections that don't end within 60 seconds make the shutdown unclean. By having connections that last less than 60 seconds, most unclean shutdowns can be avoided, including connections from the database command prompt. If you keep these connections open for hours or days, shutdowns can be unclean.  
A user cannot be deleted. | The user probably has objects in the database that depend on it. You need to drop those objects or reassign them to another user. Find out which objects are dependent on the user, then drop or reassign those objects to a different user. [ This article](https://blog.pythian.com/properly-removing-users-mysql/) discusses how to find the objects owned by the user.   
Particular queries are running slow. | Queries can be slow for many reasons, mostly due to specific database aspects. One reason that can involve Cloud SQL is network latency, when the source (writer or reader) resource and the destination (Cloud SQL) resource are in different regions. Refer to [ general performance tips](https://docs.cloud.google.com/sql/docs/mysql/diagnose-issues#tips) in particular. For slow database inserts, updates, or deletes, consider the following actions:

  * If you enable the `long_query_time`flag, you can check the logs for slow queries. Go to the [Logs Explorer](https://console.cloud.google.com/logs/query) page for your project and run a query like this: 
        
        resource.type="cloudsql_database"
        resource.labels.database_id="INSTANCE-ID"
        log_name="projects/PROJECT-ID/logs/cloudsql.googleapis.com%2Fmysql-slow.log"
              

You can [ download the logs in JSON or TEXT](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting#gcloud-logging-read) format for local processing.
  * Check the locations of the writer and database; sending data a long distance introduces latency.
  * Check the location of the reader and database; latency affects read performance even more than write performance

To reduce the latency the recommendation is to locate both the source and destination resources in the same region.  
Out of memory is indicated but monitoring charts don't show that. | An instance can fail and report `Out of memory` but the Google Cloud console or Cloud Monitoring charts seem to show there's still memory remaining. There are other factors beside your workload that can impact memory usage, such as the number of active connections and internal overhead processes. These aren't always reflected in the monitoring charts. Ensure that the instance has enough overhead to account for your workload plus some additional overhead.  
Recovering a deleted instance. | All data on an instance, including backups, is permanently lost when that instance is deleted. To preserve your data, [ export it to Cloud Storage](https://docs.cloud.google.com/sql/docs/mysql/import-export) before you [ delete an instance](https://docs.cloud.google.com/sql/docs/mysql/delete-instance). The Cloud SQL Admin role includes the permission to delete the instance. To prevent accidental deletion, grant this role only as needed.  
You want to rename an existing Cloud SQL instance. | Renaming an existing instance is not supported. There are other ways to accomplish the goal by creating a new instance. 

  * You can [clone the instance](https://docs.cloud.google.com/sql/docs/mysql/clone-instance) you want to rename and set a new name for the cloned instance. This allows you to create the new instance without having to import data manually. Just as when creating a new instance, the cloned instance has a new IP address.
  * You can [export](https://docs.cloud.google.com/sql/docs/mysql/import-export) data from your instance into a Cloud Storage bucket, create a new instance with the new name you want, and then [import](https://docs.cloud.google.com/sql/docs/mysql/import-export) the data into the new instance.

In both cases, you can delete your old instance after the operation is done. We recommend going with the cloning route since it has no impact on performance and doesn't require you to redo any instance configuration settings such as flags, machine type, storage size and memory.  
Error when deleting an instance. | If deletion protection is enabled for an instance, confirm your plans to delete the instance. Then [ disable deletion protection](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection) before deleting the instance.   
Error message: `429 Too Many Requests (rateLimitExceeded)`. | You might receive an HTTP `429 Too Many Requests` error with the reason `rateLimitExceeded` when an application or service account exceeds the Cloud SQL Admin API per-user rate quota. Because rate quotas are enforced per minute, per user, and per region, the aggregate project-level quota metrics on the Cloud Quotas page in the Google Cloud console might not show quota exhaustion. To diagnose which user or service account is exhausting the per-user rate limit:

  1. In the Google Cloud console, select the consumer project that initiates the requests, and then go to the **Metrics Explorer** page.
  2. Click **Select a metric** , and then enter `serviceruntime.googleapis.com/api/request_count` in the filter bar. In the submenus, select **Consumed API > Api > Request count**, and then click **Apply**.
  3. In the **Filter** element, click **Add filter** , select `response_code`, leave **Comparator** set to **= (equals)** , enter `429` in the **Value** field, and then click **Apply**.
  4. Click **Add filter** again, select `service` (enter `sqladmin.googleapis.com` in the **Value** field) or `method` (for example, enter `google.cloud.sql.v1.SqlInstancesService.Get` in the **Value** field), and then click **Apply**.
  5. In the **Aggregation** element, verify that the first menu is set to **Sum** , and then in the second menu (next to **by**), select `credential_id` to group requests by individual credential.
  6. In the results, find the credential ID (`credential_id`) with the highest number of `429` responses. This value is the OAuth 2.0 client ID of the service account or user credential that is exhausting the per-user rate limit.
  7. In the Google Cloud console, go to the **Service accounts** page and search for the OAuth 2.0 client ID matching the credential ID. The matching entry is the service account that is exhausting the per-user rate limit.

To resolve the error, implement client-side caching or exponential backoff in your application, distribute workloads across distinct service accounts, or request a quota adjustment. For more information, see [Troubleshoot rate limit errors](https://docs.cloud.google.com/sql/docs/mysql/quotas#troubleshoot-rate-limits).  
  
## Private Service Connect

Issue | Troubleshooting  
---|---  
The service attachment of the instance doesn't accept the Private Service Connect endpoint. | 

  1. Check the endpoint's status. 

### gcloud

To check the status, use the   
[`gcloud compute forwarding-rules describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe) command.
         
         gcloud compute forwarding-rules describe ENDPOINT_NAME \
         --project=PROJECT_ID \
         --region=REGION_NAME \
         | grep pscConnectionStatus

Make the following replacements:
     * ENDPOINT_NAME: the name of the endpoint
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the endpoint
     * REGION_NAME: the region name for the endpoint

### REST

Before using any of the request data, make the following replacements: 
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the Private Service Connect endpoint
     * REGION_NAME: the name of the region
     * ENDPOINT_NAME: the name of the endpoint
HTTP method and URL: 
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).  Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).  Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#forwardingRule",
      "id": "ENDPOINT_ID",
      "creationTimestamp": "2024-05-09T12:03:21.383-07:00",
      "name": "ENDPOINT_NAME",
      "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME",
      "IPAddress": "IP_ADDRESS",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_NAME",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/forwardingRules/ENDPOINT_NAME",
      "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default",
      "serviceDirectoryRegistrations": [
        {
          "namespace": "goog-psc-default"
        }
      ],
      "networkTier": "PREMIUM",
      "labelFingerprint": "LABEL_FINGERPRINT_ID",
      "fingerprint": "FINGERPRINT_ID",
      "pscConnectionId": "CONNECTION_ID",
      **"pscConnectionStatus": "ACCEPTED",**
      "allowPscGlobalAccess": true
    }
    

  2. Verify that the status of the endpoint is `ACCEPTED`. If the status is `PENDING`, then the instance isn't allowing the Google Cloud project that contains the endpoint. Make sure that the network project in which the endpoint is created is allowed. For more information, see [Edit an instance with Private Service Connect enabled](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#edit-psc-instance).

  
`ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: The resource 'projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME' was not found` | This error message can occur when reserving a static internal IP address for the Private Service Connect endpoint. Make sure the subnet specified exists in the project specified by the URI. If you want to create an endpoint in a service project but use a subnet from a Shared VPC network, you need to specify the subnet by its URI and use the host project's project ID in the URI. For more information, see [Create the endpoint manually](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-endpoint-manually).  
`ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: - The resource 'projects/PROJECT_ID/global/networks/NETWORK_NAME' was not found` | This error message can occur when you create a Private Service Connect endpoint manually. Make sure the network specified exists in the project specified by the URI. If you want to create an endpoint in a service project but use a Shared VPC network, you need to specify the network by its URI and use the host project's project ID in the URI. For more information, see [Create the endpoint manually](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-endpoint-manually).  
`Invalid consumer network status for PSC auto connection`. |  The consumer network is either not configured correctly, or not configured at all, and therefore, no endpoint is available to connect to. To connect to the endpoint, you'll need to check the status of the endpoint, and fix the error before trying to connect again.  
To check the status of an endpoint, see [Retrive the endpoint](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#retrieve-endpoint). The status of the endpoint can be one of the following:

  * `CONNECTION_POLICY_MISSING`: there is no matching service connection policy on the consumer network. Service connection policies are configured by network, by region. To reconfigure the network, see [Update a service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy). 
  * `CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED`: there is a matching service connection policy, but the [Service instance scope](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#custom-scope) field in the policy is not configured to allow connection to this Cloud SQL instance. Update the policy to configure the value of the **Service instance scope** field (`--producer-instance-location`) with the project, folder, or organization where the Cloud SQL instance resides. To reconfigure the service connection policy, see [Update a service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy). 
  * `POLICY_LIMIT_REACHED`: the service connection policy has reached its endpoint limit. To resolve, you'll need to increase the endpoint limit by [updating the service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy). 

  
`No permission to create a service connection policy`. |  You don't have the required permissions to create a service connection policy. To create a service connection policy, you need the `Compute Network Admin IAM` role. For more information, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions).   
The network attachment is unable to accept connections from the Private Service Connect interface when using [Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-outbound).  |  If your external network is unable to accept connections from the Private Service Connect interface, then the connection policies on your network attachment may not be configured correctly.  
  
Network attachments need to be configured to either accept all connections automatically, or configured manually with a list of accepted connections. For more information, see [Connection policies](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies).  Use the following command to verify the accepted connections in your network attachment:
    
    
        gcloud compute network-attachments describe default
        --region=REGION_ID
        

If the Private Service Connect interface isn't on the accepted list, then [update your network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#update). For more information, see [Manage network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments).   
  
## Replication

Issue | Troubleshooting | Read replica didn't start replicating on creation. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.   
---|---  
Unable to create read replica - invalidFlagValue error. | One of the flags in the request is invalid. It could be a flag you provided explicitly or one that was set to a default value. First, check that the value of the `max_connections` flag is greater than or equal to the value on the primary. If the `max_connections` flag is set appropriately, [inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.  
Unable to create read replica - unknown error. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error. If the error is: `set Service Networking service account as servicenetworking.serviceAgent role on consumer project`, you can manually create the service account necessary by following the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).  
Disk is full. | The primary instance disk size can become full during replica creation. [ Edit the primary instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to upgrade it to a larger disk size.   
The replica instance is using too much memory. | The replica uses temporary memory to cache often-requested read operations, which can lead it to use more memory than the primary instance. Restart the replica instance to reclaim the temporary memory space.  
Replication stopped. | The maximum storage limit was reached and automatic storage increase isn't enabled. [ Edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to enable `automatic storage increase`.  
Replication lag is consistently high. | The write load is too high for the replica to handle. Replication lag takes place when the SQL thread on a replica is unable to keep up with the IO thread. Some kinds of queries or workloads can cause temporary or permanent high replication lag for a given schema. Some of the typical causes of replication lag are: 

  * Slow queries on the replica. Find and fix them.
  * All tables must have a unique/primary key. Every update on such a table without a unique/primary key causes full table scans on th replica.
  * Queries like `DELETE ... WHERE field < 50000000` cause replication lag with row-based replication since a huge number of updates are piled up on the replica.

Some possible solutions include:

  * [ Configure parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication).
  * Set the [innodb_flush_log_at_trx_commit](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i) flag on the read replica to 2. See [Tips for working with flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips) for more information about this flag.
  * [ Edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to increase the size of the replica.
  * Reduce the load on the database.
  * Send read traffic to the read replica.
  * Index the tables.
  * Identify and fix slow write queries.
  * Recreate the replica.

  
Replication lag suddenly spikes. | This is caused by long-running transaction(s). When a transaction (single statement or multi-statements) commits on the source instance, the start time of the transaction is recorded in the binary log. When the replica receives this binlog event, it compares that timestamp with the current timestamp to calculate replication lag. Hence, a long-running transaction on the source would result in an immediate large replication lag on the replica. If the amount of row changes in the transaction is large, the replica would also spend a long time to execute it. During the time, replication lag is increasing. Once the replica finishes this transaction, the catch up period would depend on the write workload on the source and the replica's processing speed. To avoid a long transaction, some possible solutions include:

  * Break the transaction into multiple small transactions 
  * Chunk a single large write query into smaller batches 
  * Try to separate long SELECT queries from a transaction mixed with DMLs 

  
Changing parallel replication flags results in an error. | An incorrect value is set for one of or more of these flags. On the primary instance that's displaying the error message, set the parallel replication flags:

  1. Modify the `binlog_transaction_dependency_tracking` and `transaction_write_set_extraction`flags: 
     * `binlog_transaction_dependency_tracking=COMMIT_ORDER`
     * `transaction_write_set_extraction=OFF`
  2. Add the `slave_pending_jobs_size_max` flag: `slave_pending_jobs_size_max=33554432`
  3. Modify the `transaction_write_set_extraction` flag: `transaction_write_set_extraction=XXHASH64`
  4. Modify the `binlog_transaction_dependency_tracking` flag: `binlog_transaction_dependency_tracking=WRITESET`

  
Replica creation fails with timeout. | Long-running uncommitted transactions on the primary instance can cause read replica creation to fail. Recreate the replica after stopping all running queries.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
