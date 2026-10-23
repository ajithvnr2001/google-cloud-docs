---
url: https://docs.cloud.google.com/sql/docs/postgres/troubleshooting/
title: Troubleshoot \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:03.409526+00:00
---

# Troubleshoot  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshooting "View this page for the SQL Server database engine")

Check if your question or problem has already been addressed on one of the following pages: 

  * [FAQ](https://docs.cloud.google.com/sql/faq)
  * [Known issues](https://docs.cloud.google.com/sql/docs/postgres/known-issues)
  * [Error messages](https://docs.cloud.google.com/sql/docs/postgres/error-messages)
  * [Diagnose issues](https://docs.cloud.google.com/sql/docs/postgres/diagnose-issues)
  * [Debug connection issues](https://docs.cloud.google.com/sql/docs/postgres/debugging-connectivity)
  * [Issues updating storage capacity](https://docs.cloud.google.com/sql/docs/postgres/issues-updating-storage-capacity)



Topics in this page include:

  * Backup and recovery
  * Cancel import and export
  * Cloning
  * Connectivity
  * Creating instances
  * Execute SQL using the Data API
  * Flags
  * High availability
  * Import and export
  * Integrate with Vertex AI
  * Logging
  * Managing instances
  * Private Service Connect
  * Replication



## Backup and recovery

Issue | Troubleshooting | You can't see the current operation's status. | The Google Cloud console reports only success or failure when the operation is done. It isn't designed to show warnings or other updates. Run the [ `gcloud sql operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/list) to list all operations for the given Cloud SQL instance.  
---|---  
You want to find out who issued an on-demand backup operation. | The user interface doesn't show the user who started an operation. Look in the [logs](https://docs.cloud.google.com/sql/docs/postgres/logging#viewing_logs) and filter by text to find the user. You may need to use audit logs for private information. Relevant log files include:

  * `cloudsql.googleapis.com/postgres.log`
  * If [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) is enabled and you have the required permissions to view them, `cloudaudit.googleapis.com/activity` may also be available. 

  
After an instance is deleted, you can't take a backup of the instance. | If you delete an instance without taking a [final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backups) of the data, then no data recovery is possible. However, if you restore the instance, then Cloud SQL also restores the backups. For more information on recovering a deleted instance, see [Retain backups after instance deletion](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#retained-backups). If you have done an export operation, create a new instance and then do an import operation to recreate the database. Exports are written to Cloud Storage and imports are read from there. **Note:** Cloud SQL recommends that you take a final backup of your data before you delete the instance. This way, you can recreate any instances that you delete accidentally without contacting [Cloud Customer Care](https://docs.cloud.google.com/support).  
An automated backup is stuck for many hours and can't be canceled. | Backups can take a long time depending on the database size. If you really need to cancel the operation, you can ask [ customer support](https://docs.cloud.google.com/sql/docs/getting-support) to `force restart` the instance.  
A restore operation can fail when one or more users referenced in the SQL dump file don't exist. | Before restoring a SQL dump, all the database users who own objects or were granted permissions on objects in the dumped database must exist in the target database. If they don't, the restore operation fails to recreate the objects with the original ownership or permissions. [ Create the database users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) before restoring the SQL dump.  
You want to increase the number of days that you can keep automatic backups from seven to 30 days, or longer. | You can [ configure the number of automated backups to retain](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#retention), from 1 to 365. Automated backups get pruned regularly based on the retention value configured. Unfortunately, this means that the currently visible backups are the only automated backups you can restore from. To keep backups indefinitely, you can [create an on-demand backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backing-up#on-demand), as they are not deleted in the same way as automated backups. On-demand backups remain indefinitely. That is, they remain until they're deleted or the instance they belong to is deleted. Because that type of backup is not deleted automatically, it can affect billing.  
An automated backup failed and you didn't receive an email notification. | To have Cloud SQL notify you of the backup's status, [configure a log-based alert](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/view-audit-logs-for-automated-backups#configure-log-based).   
An automated or on-demand backup fails on an instance with more than 50 user-defined labels. | When Cloud SQL takes a backup, it copies your instance's user-defined labels to the underlying storage snapshot and appends internal system labels. If the combined number of labels exceeds the 64-label snapshot limit, the backup fails. To resolve this issue, remove excess labels so that the instance has 50 or fewer user-defined labels. For more information, see [Label instances](https://docs.cloud.google.com/sql/docs/postgres/label-instance#restrictions).  
An instance is repeatedly failing because it is cycling between the failure and backup restore states. Attempts to connect to and use the database following restore fail.  | 

  * There could be too many open connections. Too many connections can result from errors that occur in the middle of a connection where there are no `autovacuum` settings to clean up dead connections.
  * Cycling can occur if any custom code is using retry logic that doesn't stop after a few failures.
  * There could be too much traffic. Use connection pooling and other [best practices for connectivity](https://docs.cloud.google.com/sql/docs/postgres/manage-connections).

Things to try:

  1. Verify that the database is [ set up for `autovacuum`](https://www.postgresql.org/docs/9.6/runtime-config-autovacuum.html).
  2. Check if there is any connection retry logic set up in custom code.
  3. Turn down traffic until the database recovers and then slowly turn traffic back up.

  
You find you are missing data when performing a backup/restore operation. | Tables were created as unlogged. For example: `CREATE UNLOGGED TABLE ...`. These tables are not included in a restore from a backup:

  * The contents of unlogged tables doesn't survive failover on an HA instance.
  * Unlogged tables don't survive postgres crashes.
  * Unlogged tables are not replicated to read replicas.
  * Unlogged tables are automatically wiped during backup restore.

The solution is to avoid using unlogged tables if you want to restore those tables through a backup. If you're restoring from a database that already has unlogged tables, then you can dump the database to a file, and reload the data after modifying the dumped file to `ALTER TABLE` to `SET LOGGED` on those tables.  
Unable to delete an instance when you elect to take a final backup at instance deletion.  |  When you delete an instance, you're required to confirm whether you want to take a final backup for your instance prior to deleting it. If you enabled final backup using the `final-backup` instance setting, then the selection you make when you delete your instance must match the final backup instance configuration you set when you enabled final backup for your instance. To mitigate this issue, do one of the following:  


  * Set the final backup value to match the instance's existing backup configuration.
  * Leave the final backup field empty when you delete your instance. If you leave the field empty, then Cloud SQL takes the final backup configuration set in instance settings to take a final backup and define its retention.

To view your instance's final backup instance configuration, see [View instance information](https://docs.cloud.google.com/sql/docs/postgres/instance-info#console).   
Unable to create a replica instance after successfully creating a primary instance with the final backup setting.  |  If you create a new instance with the final backup instance setting enabled, then you must update the final backup organization policy to apply the backup configurations to the primary instance only. Final backups aren't supported for replica instances.  
For more information, see [Cloud SQL organization policies](https://docs.cloud.google.com/sql/docs/postgres/org-policy/org-policy).   
  
## Cancel import and export

Issue | Troubleshooting | Error message: `You can't cancel operation [operation-ID] because this operation isn't in progress.` |  You're trying to cancel an import or export operation that's completed, failed, or cancelled. If the operation is running, you can cancel it.  
---|---  
Error message: `You can't cancel operation [operation-ID] because Cloud SQL doesn't support the cancellation of an [operation-type] operation.` | Cloud SQL doesn't support the cancellation of the operation because it has an [operation type](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations#sqloperationtype) other than `IMPORT` or `EXPORT`.  
Error message: `The [operation-type] operation isn't cancelled. Wait and retry in a few seconds.` |  Cloud SQL can't cancel the import or export operation at this time. Try again in a few seconds. If the problem persists, contact [Google Cloud Support](https://docs.cloud.google.com/support).  
  
## Clone

Issue | Troubleshooting | Cloning fails with `constraints/sql.restrictAuthorizedNetworks` error. | The cloning operation is blocked by the `Authorized Networks` configuration. `Authorized Networks` are configured for public IP addresses in the Connectivity section of the Google Cloud console, and cloning is not permitted due to [security considerations](https://docs.cloud.google.com/sql/docs/postgres/connection-org-policy). Remove all `Authorized Networks` entries from the Cloud SQL instance if you can. Otherwise, [create a replica](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica) without any `Authorized Networks` entries.  
---|---  
Error message: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges. Please allocate new ranges for this service provider. Help Token: [help-token-id].` |  You're trying to use the Google Cloud console to clone an instance with a private IP address, but you didn't specify the allocated IP range that you want to use and the source instance isn't created with the specified range. As a result, the cloned instance is created in a random range. Use `gcloud` to clone the instance and provide a value for the   
`--allocated-ip-range-name` parameter. For more information, see [Cloning an instance with a private IP](https://docs.cloud.google.com/sql/docs/postgres/clone-instance#gcloud_1).  
  
## Connect

Issue | Troubleshooting | `Aborted connection`. | The issue might be: 

  * Networking instability.
  * No response to TCP keep-alive commands (either the client or the server isn't responsive, possibly overloaded)
  * The database engine connection lifetime was exceeded and the server ends the connection.

Applications must tolerate network failures and follow [best practices](https://docs.cloud.google.com/sql/docs/postgres/manage-connections) such as connection pooling and retrying. Most connection poolers catch these errors where possible. Otherwise the application must either retry or fail gracefully. For connection retry, we recommend the following methods:

  1. [Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff). Increase the time interval between each retry, exponentially.
  2. Add randomized backoff also.

Combining these methods helps reduce throttling.  
---|---  
Connection timeout or generic connection error when using private IP or VPC Network Peering. | Connection attempts fail with generic timeout or connection errors without diagnostic details. **Troubleshooting steps:**

  1. Run a [Network Intelligence Center Connectivity Test](https://docs.cloud.google.com/sql/docs/postgres/debugging-connectivity#diagnose-vpc-connectivity) between the source client and the Cloud SQL private IP on the database port (3306 for MySQL, 5432 for PostgreSQL, or 1433 for SQL Server). The test traces the packet path and identifies whether traffic is dropped by firewall rules, missing routes, or peering misconfigurations.
  2. Verify that the VPC Network Peering connection status is `ACTIVE`.
  3. Verify that firewall rules in the VPC network allow ingress traffic on the database port.
  4. If using non-RFC 1918 address ranges, verify that you updated the peering configuration to export subnet routes with public IP.

For more details and gcloud diagnostic commands, see [Diagnose VPC network and private IP connection failures](https://docs.cloud.google.com/sql/docs/postgres/debugging-connectivity#diagnose-vpc-connectivity).  
Error message: `Login failed for user ""` | You might encounter this login error during [Microsoft Entra ID authentication](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id). To resolve this issue, make sure that a SQL Server login exists for this Microsoft Entra ID user.  
Network connectivity issues with private IP instances | You might experience some of the following issues during integration setup: 

  * Slow operations to create Microsoft Entra ID logins
  * Unable to create Microsoft Entra ID logins
  * Unable to connect to the instance using Microsoft Entra ID authentication

For more information on how to help address these issues, see [Troubleshooting Microsoft Entra ID integration](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id).  
`Certificate verify failed`. | The client certificates have expired or the path to the certificates isn't correct. Regenerate the certificates by [recreating them](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#new-client).  
Slow connection establishment or connection timeouts when using IAM database authentication. | Connecting to a Cloud SQL instance using IAM database authentication takes several seconds or times out, while built-in database authentication connects normally. **Cause** : The instance is using a shared-core machine type (`db-f1-micro` or `db-g1-small`). Under CPU throttling, IAM database authentication takes longer to complete than built-in password authentication because it is more computationally intensive. **Resolution** :

  * Use [connection pooling](https://docs.cloud.google.com/sql/docs/postgres/manage-connections) or connect through the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy) to reuse authenticated connections.
  * Increase the client connection timeout (for example, to 10–15 seconds).
  * [Edit your instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance) to use a dedicated-core [machine type](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#machine-type-2ndgen) (such as `db-custom-*` or `db-n1-standard-*`).

For more information, see [Performance on shared-core instances](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication#iam-shared-core-performance).  
`FATAL: database 'user' does not exist`. | `gcloud sql connect --user` only works with the default `postgres` user. Connect with the default user, then change users.  
You want to find out who is connected. | Log into the database and run this command: 
    
    
    SELECT datname,
    usename,
    application_name as appname,
    client_addr,
    state,
    now() - backend_start as conn_age,
    now() - state_change as last_activity_age
    FROM pg_stat_activity
    WHERE backend_type = 'client backend'
    ORDER BY 6 DESC
    LIMIT 20
         
  
`Hostname/IP does not match certificate's altnames: Host: localhost. is not in the cert's altnames`. | The host address does not match the address in the server certificate's alternative names. If you are using Node.js with **verify-full** or its equivalent, please use the DNS name for the **servername** parameter. The DNS name can be found in the server certificate using **openssl**. For example, `openssl x509 -in server-cert.pem -noout -text |grep 'DNS:'`.
    
    
     ssl: {
      rejectUnauthorized: true,
      ca: fs.readFileSync("/path/to/server/CA"),
      servername: 'N-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx.us-central1.sql.goog'
    }  
  
## Create instances

Issue | Troubleshooting | Error message: `The zone or region does not have sufficient resources to handle the request at the moment.` | The selected zone lacks capacity for the requested resources or the VM type at the time of the instance creation request. There might be simultaneous high operational demand in that specific regional location at the time of request. To resolve this issue, retry creating the instance in another zone or retry creating the instance in the same zone that received the error at a different time of day.  
---|---  
Error message: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges. Please allocate new ranges for this service provider`. | There are no more available addresses in the allocated IP range. There can be several possible scenarios: 

  * The size of the allocated IP range for the private service connection is smaller than /24.
  * The size of the allocated IP range for the private service connection is too small for the number of Cloud SQL instances.
  * The requirement on the size of allocated IP range will be larger if instances are created in multiple regions. See [allocated range size](https://docs.cloud.google.com/sql/docs/postgres/private-ip#allocated_range_size)

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

Issue | Troubleshooting |  `The instance doesn't allow using ExecuteSql to access this instance. You can allow it by patching the instance with {settings: { dataApiAccess: "ALLOW_DATA_API" }}` |  The Data API is disabled by default. [Enable the Data API](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#enable-disable-data-api) on the instance to resolve the issue.   
---|---  
`Secret cannot be provided when auto_iam_authn is true.` | When you set `auto_iam_authn` to `true`, you are authenticating to the database using IAM. This authentication method doesn't require a password or secret. See [ Authenticate using IAM](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#authenticate-using-iam).   
`ExecuteSql API is not supported for instances in certain Assured Workloads control packages folders yet.` |  The SQL script and its execution response might transit through intermediate locations between your client and the location of the target instance. For this reason, requests will fail for instances in certain Assured Workloads projects. If your project is not enrolled in Assured Workloads but `constraints/sql.restrictNoncompliantResourceCreation` is manually enforced, then ask your organization's administrator to remove the constraint and the issue will be resolved on newly created instances.   
`IAM authentication is not enabled for the instance` |  [Configure the instance for IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#configure-db-user) to resolve the issue.   
`The database is currently unavailable.` |  The instance might be restarting, undergoing maintenance, or in an unhealthy state. Check the instance's status and try again later.   
  
## Export

Issue | Troubleshooting | `HTTP Error 409: Operation failed because another operation was already in progress.` | There is already a pending operation for your instance. Only one operation is allowed at a time. Try your request after the current operation is complete.  
---|---  
`HTTP Error 403: The service account does not have the required permissions for the bucket.` | Ensure that the bucket exists and the service account for the Cloud SQL instance (which is performing the export) has the `Storage Object Creator` role (`roles/storage.objectCreator`) to allow export to the bucket. See [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).  
CSV export worked but SQL export failed. | CSV and SQL formats do export differently. The SQL format exports the entire database, and likely takes longer to complete. The CSV format lets you define which elements of the database to include in the export. [Use CSV exports](https://docs.cloud.google.com/sql/docs/mysql/import-export/exporting#csv) to export only what you need.  
Export is taking too long. | Cloud SQL does not support concurrent synchronous operations. Use [ export offloading](https://docs.cloud.google.com/sql/docs/postgres/import-export#best_practices_for_importing_and_exporting). At a high level, in export offloading, instead of issuing an export on the source instance, Cloud SQL spins up an offload instance to perform the export. Export offloading has several advantages, including increased performance on the source instance and the unblocking of administrative operations while the export is running. With export offloading, total latency can increase by the amount of time it takes to bring up the offload instance. Generally, for reasonably sized exports, latency is not significant. However, if your export is small enough, then you may notice the increase in latency.  
Create Extension error. | The dump file contains references to unsupported extension. Edit the dump file to remove the references.  
Error using `pg_dumpall`. | Using the `[pg_dumpall](https://www.postgresql.org/docs/current/app-pg-dumpall.html)` utility with the `--global` flag requires the superuser role, but this role isn't supported in Cloud SQL for PostgreSQL. To prevent errors from occurring while performing export operations that include user names, also use the `--no-role-passwords` flag.   
The export operation times out before exporting anything, and you see the error message `Could not receive data from client: Connection reset by peer.` | If Cloud Storage does not receive any data within a certain time frame, typically around seven minutes, the connection resets. It's possible the initial export query is taking too long to run. Do a manual export using the [ `pg_dump` tool](https://www.postgresql.org/docs/12/app-pgdump.html).  
You want exports to be automated. | Cloud SQL does not provide a way to automate exports. You could build your own automated export system using Google Cloud products such as Cloud Scheduler, Pub/Sub, and Cloud Run functions, similar to this article on [ automating backups](https://betterprogramming.pub/how-to-automate-google-cloud-sql-backups-2de6d3cc7d01).  
  
## Flags

Issue | Troubleshooting | You set the time zone for a session, but it expires when you log off. |  Connect to the database and set the database time zone to the one you want, either per user or per database. In Cloud SQL for PostgreSQL, you can specify the following. These settings remain after a session is closed, mimicking a `.conf` configuration:
    
    
    ALTER DATABASE dbname SET TIMEZONE TO 'timezone';
    ALTER USER username SET TIMEZONE TO 'timezone';

These settings apply only to new connections to the database. To see the change to the time zone, disconnect from the instance and then reconnect to it.  
---|---  
  
## High availability

Issue | Troubleshooting | You can't find the metrics for a manual failover. | Only automatic failovers go into the metrics.  
---|---  
Cloud SQL instance resources (CPU and RAM) are near 100% usage, causing the high availability instance to go down. | The instance machine size is too small for the load. [ Edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to upgrade to a larger machine size to get more CPUs and memory.   
  
## Import

Issue | Troubleshooting | Error message: `permission denied for schema public` | For PostgreSQL versions 15 and later, if the target database is created from `template0`, then importing data might fail. To resolve this issue, provide public schema privileges to the `cloudsqlsuperuser` user by running the `GRANT ALL ON SCHEMA public TO cloudsqlsuperuser` SQL command.  
---|---  
`HTTP Error 409: Operation failed because another operation was already in progress`. | There is already a pending operation for your instance. Only one operation is allowed at a time. Try your request after the current operation is complete.  
The import operation is taking too long. | Too many active connections can interfere with import operations. Close unused operations. Check the CPU and memory usage of your Cloud SQL instance to make sure there are plenty of resources available. The best way to ensure maximum resources for the import is to restart the instance before beginning the operation. A restart:

  * Closes all connections.
  * Ends any tasks that may be consuming resources.

  
An import operation can fail when one or more users referenced in the dump file don't exist. | Before importing a dump file, all the database users who own objects or were granted permissions on objects in the dumped database must exist in the target database. If they don't, the import operation fails to recreate the objects with the original ownership or permissions. [ Create the database users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) before importing.  
After importing data, the size of your data disk usage is much higher. | There may be an unexpected disk usage after importing data. This usage may be because of using [point-in-time recovery](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#disk-usage). To resolve this, after you import data, disable point-in-time recovery if you want to delete logs and recover storage. Keep in mind that decreasing the storage used doesn't shrink the size of the storage provisioned for the instance.  
Error message: `GRANT stderr: ERROR: must be member of role ROLE_NAME` | This error message appears if you try to [import a SQL dump file](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-sql) that's uploaded in Cloud Storage to a Cloud SQL database, and the import job has run for about four days. ROLE_NAME is a custom database role defined in the source PostgreSQL database. The default `cloudsqlsuperuser` user imports the SQL dump file. However, this user might not belong to the ROLE_NAME role. To resolve this issue, complete the following steps:

  1. Create the ROLE_NAME role in the destination database where you're importing the SQL dump file.
  2. Don't use the `cloudsqlsuperuser` user to import the file. Instead, in the destination database, specify a user who's a member of the ROLE_NAME role. To specify the user, run the following command: `gcloud sql import sql INSTANCE URI [--async]   
[--database=DATABASE, -d DATABASE] [--user=USER] [GCLOUD_WIDE_FLAG …]`

  
  
## Integrate with Vertex AI

Issue | Troubleshooting  
---|---  
Error message: `Google ML integration API is supported only on Postgres version 12 or above.` | To enable the Vertex AI integration in Cloud SQL, you must have a Cloud SQL for PostgreSQL database, version 12 or later. To upgrade your database to this version, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace).  
Error message: `Google ML Integration API is not supported on shared core instance. Please upsize your machine type.` | If you selected a shared core for the machine type of your instance, then you can't enable the Vertex AI integration in Cloud SQL. Upgrade your machine type to dedicated core. For more information, see [Machine Type](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#machine-type-2ndgen).  
Error message: `Google ML Integration is unsupported for this maintenance version. Please follow https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance to update the maintenance version of the instance.` | To enable the Vertex AI integration in Cloud SQL, the maintenance version of your instance must be `R20240130` or later. To upgrade your instance to this version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).  
Error message: `**Cannot invoke ml_predict_row if 'cloudsql.enable_google_ml_integration' is off.**` | The `cloudsql.enable_google_ml_integration `database flag is turned off. Cloud SQL can't integrate with Vertex AI.  
  
To turn this flag on, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:  
  
`gcloud sql instances patch INSTANCE_NAME --database-flags cloudsql.enable_google_ml_integration=on`  
  
Replace INSTANCE_NAME with the name of the primary Cloud SQL instance.  
Error message: `**Failed to connect to remote host: Connection refused.**` | The integration between Cloud SQL and Vertex AI isn't enabled. To enable this integration, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:  
  
`gcloud sql instances patch INSTANCE_NAME   
--enable-google-ml-integration `  
  
Replace INSTANCE_NAME with the name of the primary Cloud SQL instance.  
Error message: `**Vertex AI API has not been used in project PROJECT_ID before or it is disabled. Enable it by visiting /apis/api/aiplatform.googleapis.com/overview?project=PROJECT_ID then retry.**` | The Vertex AI API isn't enabled. For more information on enabling this API, see [Enable database integration with Vertex AI](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai#enable-database-integration-with-vertex-ai).  
Error message: `**Permission 'aiplatform.endpoints.predict' denied on resource.**` | Vertex AI permissions aren't added to the Cloud SQL service account for the project where the Cloud SQL instance is located. For more information on adding these permissions to the service account, see [Grant the Cloud SQL service account Identity and Access Management (IAM) permissions to access Vertex AI](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai#grant-service-account).  
Error message: `**Publisher Model `projects/ PROJECT_ID/locations/REGION_NAME/publishers/google/models/MODEL_NAME` not found.**` | The machine learning model or the LLM doesn't exist in Vertex AI.   
Error message: `**Resource exhausted: grpc: received message larger than max.**` | The size of the request that Cloud SQL passes to Vertex AI exceeds the [gRPC](https://grpc.io/) limit of 4 MB per request.  
Error message: `**Cloud SQL attempts to send a request to Vertex AI. However, the instance is in the %s region, but the Vertex AI endpoint is in the %s region. Make sure the instance and endpoint are in the same region.**` | Cloud SQL attempts to send a request to Vertex AI. However, the instance is in one region, but the Vertex AI endpoint is in a different region. To resolve this issue, both the instance and endpoint must be in the same region.  
Error message: `**The Vertex AI endpoint isn't formatted properly.**` | The Vertex AI endpoint isn't formatted properly. For more information, see [Use private endpoints for online prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints).   
Error message: `**Quota exceeded for aiplatform.googleapis.com/online_prediction_requests_per_base_model with base model: textembedding-gecko.**` | The number of requests that Cloud SQL passes to Vertex AI exceeds the limit of 1,500 requests per minute per region per model per project.  
  
## Logging

Issue | Troubleshooting | Logging uses a lot of CPU and memory on your Cloud SQL instance.  | Logging needs to be tuned. The `log_statement` flag can be set to none and the `logging_collector` flag can be set to off. If logging is still occurring, there may be other log-related flags that can be tuned. You can [ edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to modify these flags.  
---|---  
Audit logs are not found. | Data-Access logs are only written if the operation is an authenticated user-driven API call that creates, modifies, or reads user-created data, or if the operation accesses configuration files or metadata of resources.   
Operations information is not found in logs. | You want to find more information about an operation. For example, a user was deleted but you can't find out who did it. The logs show the operation started but don't provide any more information. You must [enable audit logging](https://docs.cloud.google.com/logging/docs/audit) for detailed and personal identifying information (PII) like this to be logged.  
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
         
  
Query logs are not found in PostgreSQL logs. | You need to enable the pgaudit flags. 

  1. From a terminal, connect to your database: 
         
         gcloud sql connect INSTANCE_NAME
               

  2. Run this command to create the extension: 
         
         CREATE EXTENSION pgaudit;
               

  3. Exit the database, and from a terminal run the following command: 
         
         gcloud sql instances patch INSTANCE_NAME \
         --database-flags=cloudsql.enable_pgaudit=on,pgaudit.log=all
              


  
  
## Manage instances

Issue | Troubleshooting | You want to find out what is using up storage. | For example, you notice that your database is using only 3 GB, but storage shows that 14 GB is being used. Space not used by database tables is typically used by transaction logs, temporary files, or other logs. You can view a breakdown of instance disk usage by data type using the [`cloudsql.googleapis.com/database/disk/bytes_used_by_data_type`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics) metric in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) or the **Disk storage by type** chart on the [System insights](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights#default-metrics) dashboard. Things to try:

  * For Cloud SQL for PostgreSQL, the `database/disk/bytes_used_by_data_type` metric breaks down storage usage across `Data`, `Wal` (write-ahead logs), `Archived_wal_log` (archived write-ahead logs when point-in-time recovery logs are stored on disk), `Tmp_data`, `Audit_log`, `Replication_slot`, and `Other`.
  * To check the size of each database on your Cloud SQL for PostgreSQL instance, connect to the database and run the following query: `SELECT pg_database.datname, pg_size_pretty(pg_database_size(pg_database.datname)) AS size FROM pg_database;`
  * To check whether point-in-time recovery (PITR) logs are stored on disk or in Cloud Storage, see [Check the storage location of transaction logs used for PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/configure-pitr#check-log-storage-location). 

  
---|---  
You want to find out what queries are running now. | Connect to the database and run the following query: `SELECT datname, username, application_name as appname, client_addr, state, now() - backend_start as conn_age, now() - xact_start as xact_age, now() - query_start as query_age, now() - state_change as last_activity_age, wait_event_type, wait_event, query FROM pg_stat_activity WHERE state <> 'idle' ORDER BY 8 DESC LIMIT 20; `  
You want to find out what units are being used for a specific field. | Connect to the database and run the following query (using your own `FIELD_NAME`):  `SELECT name, setting, unit FROM pg_settings WHERE name = 'FIELD_NAME'`.  
You want to find the current value of a database setting. | Connect to the database and run the following query (using your own `SETTING_NAME`): `SHOW SETTING_NAME;` Run `SHOW ALL;` to see all settings.  
You want to stop a blocked background process. | The user needs to have the `pg_signal_backend` role. Run the following commands:

  1. GRANT pg_signal_backend TO USERNAME;
               

  2. Find the process ID of the blocked or stuck process: 
         
         SELECT pid, username, state, query FROM pg_stat_activity;
               

  3. Stop a running or idle process using these commands: 
         
         SELECT pg_cancel_backend(pid)
                     FROM pg_stat_activity
                     WHERE username = 'USERNAME';
               
               
         
         SELECT pg_terminate_backend(pid)
                     FROM pg_stat_activity
                     WHERE username = 'USERNAME';
               
               


  
Instance is nearing 100% consumption of transaction IDs. | Your internal monitoring warns that the instance is nearing 100% consumption of transaction IDs. You want to avoid transaction wraparound, which can block writes. The autovacuum job might be blocked, or might not be reclaiming the transaction IDs fast enough to keep up with the workload. In order to avoid any outages due to transaction wraparound problem, you can review these [self-servicing tips](https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound) for dealing with TXID wraparound. For general tuning advice, see [ Optimizing, monitoring, and troubleshooting vacuum operations in PostgreSQL](https://docs.cloud.google.com/static/solutions/optimizing-monitoring-troubleshooting-vacuum-operations-postgresql.pdf).  
Temporary storage increased automatic storage. | Automatic storage is enabled. Restart deletes the temporary files but not reduce the storage. Only [ customer support](https://docs.cloud.google.com/sql/docs/getting-support) can reset the instance size.  
Data is being automatically deleted. | Most likely a script is running somewhere in your environment. Look in the logs around the time of the deletion and see if there's a rogue script running from a dashboard or another automated process.  
The instance cannot be deleted. | You might see the error message `ERROR: (gcloud.sql.instances.delete) HTTP Error 409: The instance or operation is not in an appropriate state to handle the request`, or the instance may have a `INSTANCE_RISKY_FLAG_CONFIG` flag status. Some possible explanations include:

  * Another operation is in progress. Cloud SQL operations do not run concurrently. Wait for the other operation to complete.
  * The `INSTANCE_RISKY_FLAG_CONFIG` warning is triggered whenever at least one `beta` flag is being used. Remove the risky flag settings and restart the instance

  
The instance is stuck due to large temporary data size. | The system can create many temporary tables at one time, depending on the queries and the load. Unfortunately, you can't shrink the `ibtmp1` file by any method other than restarting the service. One mitigation option is to create the temporary table with `ROW_FORMAT=COMPRESSED`, so it is stored in file-per-table tablespaces in the temporary file directory. However, the downside is performance costs associated with creating and removing a file-per-table tablespace for each temporary table.  
Fatal error during upgrade. | Logs may reveal more, but in any case [customer support](https://docs.cloud.google.com/sql/docs/getting-support) may be needed to force re-create the instance.   
Instance is stuck on restart after running out of disk space. | Automatic storage increase capability isn't enabled. If your instance runs out of storage, and the automatic storage increase capability isn't enabled, your instance goes offline. To avoid this issue, you can [ edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to enable automatic storage increase.  
Your on-premises primary instance is stuck. | Google Cloud can't help with instances that are not in Cloud SQL.   
Slow shutdown on restart. | When an instance shuts down, any outstanding connections that don't end within 60 seconds make the shutdown unclean. By having connections that last less than 60 seconds, most unclean shutdowns can be avoided, including connections from the database command prompt. If you keep these connections open for hours or days, shutdowns can be unclean.  
A user cannot be deleted. | The user probably has objects in the database that depend on it. You need to drop those objects or reassign them to another user. Find out which objects are dependent on the user, then drop or reassign those objects to a different user. [ This thread on Stack Exchange](https://dba.stackexchange.com/questions/155332/find-objects-linked-to-a-postgresql-role) discusses how to find the objects owned by the user.   
Particular queries are running slow. | Queries can be slow for many reasons, mostly due to specific database aspects. One reason that can involve Cloud SQL is network latency, when the source (writer or reader) resource and the destination (Cloud SQL) resource are in different regions. Refer to [ general performance tips](https://docs.cloud.google.com/sql/docs/mysql/diagnose-issues#tips) in particular. For slow database inserts, updates, or deletes, consider the following actions:

  * Check the locations of the writer and database; sending data a long distance introduces latency.
  * Check the location of the reader and database; latency affects read performance even more than write performance

To reduce the latency the recommendation is to locate both the source and destination resources in the same region.  
Out of memory is indicated but monitoring charts don't show that. | An instance can fail and report `Out of memory` but the Google Cloud console or Cloud Monitoring charts seem to show there's still memory remaining. There are other factors beside your workload that can impact memory usage, such as the number of active connections and internal overhead processes. These aren't always reflected in the monitoring charts. Ensure that the instance has enough overhead to account for your workload plus some additional overhead.  
Recovering a deleted instance. | All data on an instance, including backups, is permanently lost when that instance is deleted. To preserve your data, [ export it to Cloud Storage](https://docs.cloud.google.com/sql/docs/postgres/import-export) before you [ delete an instance](https://docs.cloud.google.com/sql/docs/postgres/delete-instance). The Cloud SQL Admin role includes the permission to delete the instance. To prevent accidental deletion, grant this role only as needed.  
You want to rename an existing Cloud SQL instance. | Renaming an existing instance is not supported. There are other ways to accomplish the goal by creating a new instance. 

  * You can [clone the instance](https://docs.cloud.google.com/sql/docs/postgres/clone-instance) you want to rename and set a new name for the cloned instance. This allows you to create the new instance without having to import data manually. Just as when creating a new instance, the cloned instance has a new IP address.
  * You can [export](https://docs.cloud.google.com/sql/docs/postgres/import-export) data from your instance into a Cloud Storage bucket, create a new instance with the new name you want, and then [import](https://docs.cloud.google.com/sql/docs/postgres/import-export) the data into the new instance.

In both cases, you can delete your old instance after the operation is done. We recommend going with the cloning route since it has no impact on performance and doesn't require you to redo any instance configuration settings such as flags, machine type, storage size and memory.  
Error when deleting an instance. | If deletion protection is enabled for an instance, confirm your plans to delete the instance. Then [ disable deletion protection](https://docs.cloud.google.com/sql/docs/postgres/deletion-protection) before deleting the instance.   
Error message: `429 Too Many Requests (rateLimitExceeded)`. | You might receive an HTTP `429 Too Many Requests` error with the reason `rateLimitExceeded` when an application or service account exceeds the Cloud SQL Admin API per-user rate quota. Because rate quotas are enforced per minute, per user, and per region, the aggregate project-level quota metrics on the Cloud Quotas page in the Google Cloud console might not show quota exhaustion. To diagnose which user or service account is exhausting the per-user rate limit:

  1. In the Google Cloud console, select the consumer project that initiates the requests, and then go to the **Metrics Explorer** page.
  2. Click **Select a metric** , and then enter `serviceruntime.googleapis.com/api/request_count` in the filter bar. In the submenus, select **Consumed API > Api > Request count**, and then click **Apply**.
  3. In the **Filter** element, click **Add filter** , select `response_code`, leave **Comparator** set to **= (equals)** , enter `429` in the **Value** field, and then click **Apply**.
  4. Click **Add filter** again, select `service` (enter `sqladmin.googleapis.com` in the **Value** field) or `method` (for example, enter `google.cloud.sql.v1.SqlInstancesService.Get` in the **Value** field), and then click **Apply**.
  5. In the **Aggregation** element, verify that the first menu is set to **Sum** , and then in the second menu (next to **by**), select `credential_id` to group requests by individual credential.
  6. In the results, find the credential ID (`credential_id`) with the highest number of `429` responses. This value is the OAuth 2.0 client ID of the service account or user credential that is exhausting the per-user rate limit.
  7. In the Google Cloud console, go to the **Service accounts** page and search for the OAuth 2.0 client ID matching the credential ID. The matching entry is the service account that is exhausting the per-user rate limit.

To resolve the error, implement client-side caching or exponential backoff in your application, distribute workloads across distinct service accounts, or request a quota adjustment. For more information, see [Troubleshoot rate limit errors](https://docs.cloud.google.com/sql/docs/postgres/quotas#troubleshoot-rate-limits).  
  
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
    

  2. Verify that the status of the endpoint is `ACCEPTED`. If the status is `PENDING`, then the instance isn't allowing the Google Cloud project that contains the endpoint. Make sure that the network project in which the endpoint is created is allowed. For more information, see [Edit an instance with Private Service Connect enabled](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#edit-psc-instance).

  
`ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: The resource 'projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME' was not found` | This error message can occur when reserving a static internal IP address for the Private Service Connect endpoint. Make sure the subnet specified exists in the project specified by the URI. If you want to create an endpoint in a service project but use a subnet from a Shared VPC network, you need to specify the subnet by its URI and use the host project's project ID in the URI. For more information, see [Create the endpoint manually](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-endpoint-manually).  
`ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource: - The resource 'projects/PROJECT_ID/global/networks/NETWORK_NAME' was not found` | This error message can occur when you create a Private Service Connect endpoint manually. Make sure the network specified exists in the project specified by the URI. If you want to create an endpoint in a service project but use a Shared VPC network, you need to specify the network by its URI and use the host project's project ID in the URI. For more information, see [Create the endpoint manually](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-endpoint-manually).  
`Invalid consumer network status for PSC auto connection`. |  The consumer network is either not configured correctly, or not configured at all, and therefore, no endpoint is available to connect to. To connect to the endpoint, you'll need to check the status of the endpoint, and fix the error before trying to connect again.  
To check the status of an endpoint, see [Retrive the endpoint](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#retrieve-endpoint). The status of the endpoint can be one of the following:

  * `CONNECTION_POLICY_MISSING`: there is no matching service connection policy on the consumer network. Service connection policies are configured by network, by region. To reconfigure the network, see [Update a service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy). 
  * `CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED`: there is a matching service connection policy, but the [Service instance scope](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#custom-scope) field in the policy is not configured to allow connection to this Cloud SQL instance. Update the policy to configure the value of the **Service instance scope** field (`--producer-instance-location`) with the project, folder, or organization where the Cloud SQL instance resides. To reconfigure the service connection policy, see [Update a service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy). 
  * `POLICY_LIMIT_REACHED`: the service connection policy has reached its endpoint limit. To resolve, you'll need to increase the endpoint limit by [updating the service connection policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#update-policy). 

  
`No permission to create a service connection policy`. |  You don't have the required permissions to create a service connection policy. To create a service connection policy, you need the `Compute Network Admin IAM` role. For more information, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions).   
The network attachment is unable to accept connections from the Private Service Connect interface when using [Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound).  |  If your external network is unable to accept connections from the Private Service Connect interface, then the connection policies on your network attachment may not be configured correctly.  
  
Network attachments need to be configured to either accept all connections automatically, or configured manually with a list of accepted connections. For more information, see [Connection policies](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies).  Use the following command to verify the accepted connections in your network attachment:
    
    
        gcloud compute network-attachments describe default
        --region=REGION_ID
        

If the Private Service Connect interface isn't on the accepted list, then [update your network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#update). For more information, see [Manage network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments).   
  
## Replication

Issue | Troubleshooting | Read replica didn't start replicating on creation. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.   
---|---  
Unable to create read replica - invalidFlagValue error. | One of the flags in the request is invalid. It could be a flag you provided explicitly or one that was set to a default value. First, check that the value of the `max_connections` flag is greater than or equal to the value on the primary. If the `max_connections` flag is set appropriately, [inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.  
Unable to create read replica - unknown error. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error. If the error is: `set Service Networking service account as servicenetworking.serviceAgent role on consumer project`, you can manually create the service account necessary by following the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).  
Disk is full. | The primary instance disk size can become full during replica creation. [ Edit the primary instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to upgrade it to a larger disk size.   
Disk space increases significantly. | A slot that's not actively used to track data causes PostgreSQL to hold onto WAL segments indefinitely, causing the disk space to grow indefinitely. If you use the [logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) features in Cloud SQL, replication slots are created and dropped automatically. Unused replication slots can be detected by querying the [`pg_replication_slots`](https://www.postgresql.org/docs/current/static/view-pg-replication-slots.html) system view and filtering on the `active` column. Unused slots can be dropped to remove WAL segments using the [`pg_drop_replication_slot`](https://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-REPLICATION) command.   
The replica instance is using too much memory. | The replica uses temporary memory to cache often-requested read operations, which can lead it to use more memory than the primary instance. Restart the replica instance to reclaim the temporary memory space.  
Replication stopped. | The maximum storage limit was reached and automatic storage increase isn't enabled. [ Edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to enable `automatic storage increase`.  
Replication lag is consistently high. | The write load is too high for the replica to handle. Replication lag takes place when the SQL thread on a replica is unable to keep up with the IO thread. Some kinds of queries or workloads can cause temporary or permanent high replication lag for a given schema. Some of the typical causes of replication lag are: 

  * Slow queries on the replica. Find and fix them.
  * All tables must have a unique/primary key. Every update on such a table without a unique/primary key causes full table scans on th replica.
  * Queries like `DELETE ... WHERE field < 50000000` cause replication lag with row-based replication since a huge number of updates are piled up on the replica.

Some possible solutions include:

  * [ Edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to increase the size of the replica.
  * Reduce the load on the database.
  * Send read traffic to the read replica.
  * Index the tables.
  * Identify and fix slow write queries.
  * Recreate the replica.

  
Errors when rebuilding indexes in PostgreSQL 9.6. | You get an error from PostgreSQL informing you that you need to rebuild a particular index. This can be done only on the primary instance. If you create a new replica instance, you soon get the same error again. [Hash indexes are not propagated to replicas](https://www.postgresql.org/docs/9.6/indexes-types.html) in PostgreSQL versions below 10. If you must use hash indexes, upgrade to PostgreSQL 10+. Otherwise, if you also want to use replicas, don't use hash indexes in PostgreSQL 9.6.  
Query on the primary instance is always running. | After creating a replica, the query `SELECT * from pg_stat_activity where state = 'active' and pid = XXXX and username = 'cloudsqlreplica'` is expected to run continuously on your primary instance.   
Replica creation fails with timeout. | Long-running uncommitted transactions on the primary instance can cause read replica creation to fail. Recreate the replica after stopping all running queries.  
If the primary instance and the replica have [different vCPU sizes](https://docs.cloud.google.com/sql/docs/postgres/instance-settings), then there might be query performance issues because the query optimizer takes vCPU sizes into account. |  To resolve this issue, complete the following steps:

  1. Turn on the [log_duration](https://docs.cloud.google.com/sql/docs/postgres/flags#postgres-l) flag and set the `log_statement` parameter to `ddl`. This provides you with both the queries and the run time on the database. However, depending on your workload, this might cause performance issues.
  2. On both the primary instance and the read replica, run `explain analyze` for the queries.
  3. Compare the query plan and check for differences.

If this is a specific query, then modify the query. For example, you can change the order of the joins to see if you get better performance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
