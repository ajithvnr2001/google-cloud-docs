---
url: https://docs.cloud.google.com/datastream/docs/diagnose-issues/
title: Diagnose issues \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:01.265092+00:00
---

# Diagnose issues  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/diagnose-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Diagnose issues Stay organized with collections  Save and categorize content based on your preferences. 

The stream might incur errors during runtime.

  * Some errors, such as a bad password on the source database, are recoverable, meaning they can be fixed and the stream resumes automatically.
  * Errors may impact a single object, such as an event containing unsupported data types. Other errors may impact several objects or the entire stream, such as when Datastream can't connect to the source database.
  * Depending on the error, information is provided in the **Streams** or **Stream details** pages of the Datastream UI. You can also use Datastream's APIs to retrieve information about the error.



To troubleshoot an error, navigate to the stream to view the error, and follow the steps outlined in the error message.

This page contains information about configuration, connectivity, Oracle, and MySQL errors, along with steps for troubleshooting the errors.

## Configuration and connectivity errors

Error | Troubleshooting steps  
---|---  
Failure connecting to the source database (generic). | This can happen for various reasons. To troubleshoot this error:

  1. Ensure that the source database is up and reachable.
  2. Navigate to the source connection profile from the **Streams** or **Connection profiles** pages.
  3. Verify that the connection profile connectivity information is correct.
  4. Verify that the username and password match.
  5. Verify that the username exists on the database and has the required privileges.
  6. Save any changes that you made on the **Connection profiles** page.

The stream resumes automatically.  
Failure connecting to source database (IP allowlisting). | This can happen if the connectivity method chosen is **IP allowlist** , but one or more of the outgoing IP addresses of Datastream aren't added properly on the source database. Make sure that the outgoing IP addresses displayed in the Datastream connection profile are configured on the network firewall so that the source database server can accept connections from these IP addresses. After this is fixed, the stream resumes automatically.  
Failure connecting to the source database (Forward SSH tunnel). | This can happen if there's an issue with the Forward SSH tunnel. Check the status of the tunnel. If the tunnel is stopped, then it needs to be started. After this is fixed, the stream resumes automatically.  
Datastream can't connect to a bastion host through a Forward SSH tunnel. | Verify that the Forward SSH tunnel configuration is configured correctly in the source connection profile, and that the port is open on the SSH tunnel server.  
Failure connecting to the source database because of bad certificates. | This can happen if there's an issue with the certificates provided when defining the source connection profile. Navigate to the **Connection profiles** page, and then select the given connection profile. Verify that the certificates are set up correctly. After making your changes, save the connection profile, and the stream resumes automatically.  
Failure using private connectivity to connect to the source database. | This error concerns the VPC peering private connectivity method. 

  1. Make sure that you've completed all of the prerequisites [VPC peering prerequisites](https://docs.cloud.google.com/datastream/docs/vpc-peering#vpc-prereqs).
  2. After [creating the private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration), verify that the [route](https://docs.cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes) which contains the internal IP address of the database appears in the **Exported routes** tab of the **VPC Network Peering** page. To do this, go to the [**VPC Network Peering**](https://console.cloud.google.com/networking/vpc-connectivity/peering) page, and then search for the peering that was added (the name is `peering-[UUID]`). The route can be found in the **Exported routes** tab. If this route doesn't exist, then add it manually.
  3. Datastream doesn't check for [overlapping with dynamic peering routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#restrictions). Providing a subnet that overlaps with a dynamic route may lead to connectivity issues. Therefore, we don't recommend using a subnet that's part of a dynamic route.
  4. Make sure that the custom routes for the Datastream IP address ranges are advertised correctly. If the custom routes are missing, see [Custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes).
  5. If you're still having issues connecting to the source database, then see [Set up a reverse proxy](https://docs.cloud.google.com/datastream/docs/private-connectivity#set-up-reverse-proxy).

  
Failure using Private Service Connect interface to connect to the source database. | 

  1. Make sure that you've completed all of the [prerequisites](https://docs.cloud.google.com/datastream/docs/psc-interfaces#psci-prereqs).
  2. Make sure that your firewall rules allow the subnetwork of the provided network attachment to connect to the source database.
  3. Make sure that the custom routes for the Datastream IP address ranges are advertised correctly. If the custom routes are missing, see [Custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes).

  
Connectivity type STATIC_SERVICE_IP_CONNECTIVITY isn't allowed while Org Policy constraints/datastream.disablePublicConnectivity is on. | You selected the public [IP allowlist or Forward SSH tunnel](https://docs.cloud.google.com/datastream/docs/network-connectivity-options) network connectivity methods for the connection profile that you're creating. However, the **Block Public Connectivity Methods** organization policy for Datastream is enabled. Therefore, you can't select public connectivity methods for your connection profile. To resolve this issue, either select the private [VPC peering](https://docs.cloud.google.com/datastream/docs/network-connectivity-options) or [Private Service Connect interfaces](https://docs.cloud.google.com/datastream/docs/private-connectivity-options) network connectivity method or disable the organization policy. To disable the organization policy:

  1. Go to the [**Organization policies**](https://console.cloud.google.com/iam-admin/orgpolicies) page in the Google Cloud Console.
  2. Select the **Datastream - Block Public Connectivity Methods** organization policy.
  3. Click **EDIT**. If the **EDIT** button is disabled, then you don't have the `orgpolicy.policy.get` and `orgpolicy.policy.set` permissions to modify this organization policy. For more information about obtaining these permissions, see [IAM permissions reference ](https://docs.cloud.google.com/iam/docs/permissions-reference).
  4. In the **Applies to** section of the page, select **Customize**.
  5. In the **Enforcement** section, select **Off**. By selecting the **Off** option, you're disabling enforcement of the constraint associated with this organization policy. You can use public connectivity methods for your connection profile.
  6. Click **SAVE**.
  7. Return to the Oracle connection profile that you're creating, and then click **CREATE**.

It may take a few minutes for the changes that you made to the organization policy to take effect. Also, for more information about organization policies, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).  
When configuring the source database for my stream, I can't find the tables and schemas I want to transfer in the list of objects to include. | This can happen if your database has thousands of tables and schemas. Some of them might not be included in the list of objects to pull when configuring the source for the stream in the Google Cloud console. Instead of selecting **Specific schemas and tables** in the **Select objects to include** section, select **Custom**. In the **Object matching criteria** field, enter the schemas and tables that you want Datastream to pull.  
I've added multiple tables to my stream using the **Objects to include** menu. However, when I look at the **Objects** tab in **Stream details** , I can see that some tables are missing. | Make sure that there's at least one CDC update to each of these tables so that Datastream can recognize the changes and automatically include the tables in the stream.  
Failure loading the list of objects when using the **Objects to include** menu in the Google Cloud console. | This can happen if your database has more than 5,000 schemas and tables. Use a different method to specify which objects to include, or use the Datastream API. For more information, see [Configure source databases](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuresourcedb).  
Events dropped during streaming and not replicated in the destination. | Datastream might drop unsupported events during streaming. You can perform the following actions to address the issue:

  * Manually trigger a backfill of the entire table. This works if the discarded events are `UPSERT` events only. If the dropped events include `DELETE` events, then you need to truncate the table in BigQuery before performing the backfill. For information about how to perform a backfill, see [Initiate backfill](https://docs.cloud.google.com/datastream/docs/manage-backfill-for-the-objects-of-a-stream#initiatebackfill).
  * Contact Google Support and ask them to perform a partial backfill. This is possible only if you can identify the dropped events with a SQL `WHERE` clause, and if none of the events are `DELETE` events.
  * Disregard the issue if the number of discarded events is low or if the discarded events aren't significant.

  
We timed out while attempting to connect to the data source. Ensure that the hostname and port configuration are accurate, and that the data source is accessible. | Because the Datastream network can't be peered directly with a private services network (for example, a Cloud SQL instance) when using VPC peering, you need to use a network address translation (NAT) VM to establish connectivity between Datastream and your resource. For more information about how to set up a NAT VM, see [Configure VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering).   
The schema of object OBJECT_NAME is too large for Datastream to process. | Datastream doesn't support replicating events with corresponding source schemas larger than 2,621,440 Unicode characters. These events are dropped with the following reason code: `UNSUPPORTED_LARGE_SCHEMA`. You might want to exclude some of the columns or rename them. Alternatively, you can exclude the object with the large schema.  
Stream state has changed. | While there can be more than one reason for this error to occur, a common underlying issue is invalid source configuration. If your stream fails to start with this error message, check your source configuration for duplicate keys or table names, data inconsistencies or schema conflicts. Many of the issues can be resolved by editing the failed stream settings directly in the Google Cloud console and adjusting entries for included and excluded objects. For more information, see [Modify configuration information about the source database](https://docs.cloud.google.com/datastream/docs/modify-a-stream#modifystreamsourceinfo).  
  
## Oracle errors

Error | Troubleshooting steps  
---|---  
Supplemental logging is configured incorrectly on the source database. | An error fetching ongoing, change data capture (CDC) data can happen if the supplemental logging configuration isn't correct on the source database. Verify that supplemental logging is configured correctly. Specifically, confirm that supplemental logging is turned on for the database tables that are being streamed from the source into the destination. The stream resumes automatically.  
Unable to resume replication as log position is lost. | This error can occur when the replication process is paused for a long time, which causes the log position to be lost. Streams shouldn't be paused for periods of time that approach the log retention period. Recreate the stream.  
Log files are missing, either partially or entirely. | The log files may have been deleted. Oracle purges log files as soon as they can unless you specify a minimum rotation period to keep them around. In the Oracle server, set how long the log files should be retained. For example, use `CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 4 DAYS;` to keep the log files around for at least 4 days. For an RDS deployment, use `exec rdsadmin.rdsadmin_util.set_configuration('archivelog retention hours',96);`  
The exclude list subsumes the include list. | The include list is contained completely within the exclude list, so the list of objects that Datastream pulls from the source is empty. Modify the object selection, and then try again.  
The logging mode for Oracle database isn't set to [ARCHIVELOG](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database). | Change the logging mode, and then try again.  
Datastream returns an `ORA-00942: table or view does not exist` error message, but everything is configured properly. | This can be a result of caching on the Oracle server. Recreating the database user should fix the caching issue.  
Changes to an Oracle source aren't reflected in the destination when the stream is already running. | If you use LogMiner as your CDC method, Datastream reads from archived redo log files. In such a case, the changes you make to the source aren't reflected in the destination until the log is archived. To see the changes in the destination, change the CDC method to binary log reader,change the log archive policy, or manually force a log switch. For more information, see [Work with Oracle database redo log files](https://docs.cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files).  
Oracle CDC configuration validation failed. | You selected a CDC method for which your source database wasn't configured. Select a different method, or complete the configuration for your CDC method. For more details, see [Configure a source Oracle database](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database).  
There's an unexpected internal error. | For more details, contact Google Support.  
  
## MySQL errors

Error | Troubleshooting steps  
---|---  
Binlog is configured incorrectly on the source database. | This can happen for continuous MySQL streams if the binlog configuration is incorrect on the source database. To troubleshoot this error, perform the following actions:

  1. Verify that binlog is configured correctly.
  2. Confirm that the binary log format of the MySQL database is set to `ROW`.
  3. Restart the stream.

  
Unable to resume replication as binlog position is lost. | This error can occur when the replication process is paused for a long time, which causes the binlog position to be lost. Streams shouldn't be paused for periods of time that approach the binlog retention period. Recreate the stream.  
Failure running the stream because of incompatible source database and destination versions. | This can happen when the source database doesn't adhere to the [version support matrix](https://docs.cloud.google.com/datastream/docs/sources#versionsformysqlsourcedb). To troubleshoot this error, perform the following actions:

  1. Ensure that the source database adheres to the matrix.
  2. Recreate the stream with the updated source database.

  
AWS RDS MySQL source binlogs are missing, either partially or entirely. | The binlogs may have been deleted. AWS RDS purges binlogs as soon as they can unless you specify a minimum rotation period to keep them around. In the source AWS RDS MySQL instance, set how long, in hours, the binlogs should be retained. For example, use `mysql.rds_set_configuration('binlog retention hours', 168);` to keep the binlogs around for at least 7 days.  
The exclude list subsumes the include list. | The include list is contained completely within the exclude list, so the list of objects that Datastream pulls from the source is empty. Modify the object selection, and then try again.  
Datastream can't replicate a MySQL database. | Make sure that Datastream has permissions to replicate the database.  
When creating a connection profile for a MySQL source, multiple PEM-encoded SSL certificates aren't accepted in the **Encryption type** menu. | Datastream doesn't support SSL certificate chains in MySQL connection profiles. Only single, x509 PEM-encoded certificates are supported.  
High latency when streaming from a MySQL source. | Increase the Datastream ability to read from the source database:

  * [Reduce the maximum binary log (binlog) file size](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_max_binlog_size) for your source database. Reducing the size increases the number of binlog files.
  * If there are multiple binlog files, set the number of [maximum concurrent CDC tasks](https://docs.cloud.google.com/datastream/docs/manage-streams#maxcdctasks) for the stream accordingly. Having multiple binlog files lets Datastream read source database events concurrently, up to the number set in the `maxConcurrentCdcTasks` field.

  
MySQL CDC configuration validation failed. | Your source database wasn't configured for the CDC method that you selected. Select a different method, or complete the configuration for your CDC method. For more details, see [Configure a source MySQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-mysql-database).  
There's an unexpected internal error. | For more details, contact Google Support.  
  
## PostgreSQL errors

Error | Troubleshooting steps  
---|---  
Logical decoding is configured incorrectly on the source database. | Verify that logical decoding is configured correctly. See [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).  
Replication slot does not exist. | An error fetching ongoing, change data capture (CDC) data can happen if the replication slot doesn't exist on the database. Verify that the replication slot is configured correctly. See [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).  
Replication slot is configured with a wrong plugin. | This error can occur if the replication slot is configured with a plugin different than `pgoutput`. Verify that the replication slot is configured correctly. See [Source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/sources-postgresql#postgresqlbehavior) for more information.  
Replication slot is active in a different process. | This error can occur when the replication slot is being used by another process. Replication slots can only be used by a single process at a time. Make sure that you don't use the same replication slot in any other process except for Datastream.  
Publication is not configured properly. | This error can occur when when the publication isn't configured to expose the tables which are included in the stream configuration. Verify that the publication is configured correctly. See [Configure information about the source database for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuresourcedbinfo).  
Publication does not exist. | This error can occur if the publication doesn't exist on the database. Verify that the publication is configured correctly. See [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).  
Unable to resume replication as WAL files are lost. | This error can occur when the replication process is paused for a long time, which causes the WAL files to be lost. Streams shouldn't be paused for periods of time that approach the WAL files retention period. Recreate the stream.  
The exclude list subsumes the include list. | The include list is contained completely within the exclude list, so the list of objects that Datastream pulls from the source is empty. Modify the object selection, and then try again.  
Datastream can't replicate a PostgreSQL schema. | Make sure that Datastream has permissions to replicate the schema.  
Large transactions on the source database cause issues with data replication and synchronization. | If you insert, update or delete a significant number of records in the source database, the replication slot might get overloaded with the corresponding events. Datastream needs time to read and process these events. Because PostgreSQL replication slots are single-threaded, processing other changes in the replication slot, including changes to data in other tables, is delayed until Datastream catches up with all the changes in the replication slot.  
Large transactions on the source database cause low CDC throughput. | Datastream doesn't support multi-threaded CDC in PostgreSQL. To overcome this limitation, and to increase your CDC throughput, you can split the source into multiple streams, each with its own publication and replication slot. For example, you might want to create one stream for the largest table in your database and another for all the other tables, or one stream for your top-priority tables and another for the remaining ones. The use cases might vary, so you need to consider what makes the most sense in your specific CDC scenario. For information about creating a publication, see [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).  
Unsupported events dropped with reason code: `BIGQUERY_TOO_MANY_PRIMARY_KEYS`. | When the PostgreSQL replica identity for a table is set to `FULL`, then Datastream treats all the columns in this table as primary keys. If there are more than 16 columns in the table, then this violates the [BigQuery CDC limitation](https://docs.cloud.google.com/bigquery/docs/change-data-capture#prerequisites) and causes the error. To solve the issue, complete the following steps: 

  1. Change the replica identity to `DEFAULT`: 
         
         ALTER TABLE TABLE_NAME REPLICA IDENTITY DEFAULT

Replace TABLE_NAME with the name of the table for which you want to change the replica identity.
  2. Remove the table from the stream's list of objects to include. For more information, see [Modify configuration information about the source database](https://docs.cloud.google.com/datastream/docs/modify-a-stream#modifystreamsourceinfo).
  3. Delete the table from BigQuery. For more information, see [Delete tables](https://docs.cloud.google.com/bigquery/docs/managing-tables#deleting_tables).
  4. In Datastream, add the table to the stream again by editing your source configuration.

  
There's an unexpected internal error. | For more details, contact Google Support.  
  
## SQL Server errors

Error | Troubleshooting steps  
---|---  
CDC is disabled for the database DATABASE_NAME. | Change data capture (CDC) must be enabled for the database. Datastream needs direct read access to transaction logs in order to replicate real time changes to the source database, and to get complete log information. Enable CDC for the database and try again. For information about enabling CDC for a database, see [Configure a source SQL Server database](https://docs.cloud.google.com/datastream/docs/sqlserver/configure-your-source-sql-server-database).  
Tables with CDC disabled. | Change data capture (CDC) must be enabled for all the tables included in the stream. Datastream needs direct read access to transaction logs in order to replicate real time changes to source tables, and to get complete log information. Enable CDC for the tables included in the stream and try again. For information about enabling CDC for source tables, see [Configure a source SQL Server database](https://docs.cloud.google.com/datastream/docs/sqlserver/configure-your-source-sql-server-database).  
Missing permissions. | Datastream is missing the necessary permissions to read from the source. Grant the appropriate privileges to the user account that is used to connect to your database, and try again.  
The SQL Server EDITION_NAME edition is not supported. | Datastream doesn't support this SQL Server edition. For more information about supported editions of SQL Server, see [Overview of SQL Server as a source](https://docs.cloud.google.com/datastream/docs/sqlserver/sources-sqlserver#sqlserverversions).  
The SQL Server version VERSION_NAME of the Standard edition is not supported. | Datastream doesn't support this version of the SQL Server Standard edition. For more information about supported versions of SQL Server, see [Overview of SQL Server as a source](https://docs.cloud.google.com/datastream/docs/sqlserver/sources-sqlserver#sqlserverversions).  
The stream is unable to read the event in LSN "YOUR_LSN" because the transaction log seems to be truncated. | This issue can occur when transaction logs no longer exist on the source database. When you replicate data from a SQL Server source using the transaction logs CDC method, the logs might get truncated before Datastream reads them. When that happens, Datastream can't reliably replicate the source database to the destination. To resolve the issue, recover your stream or consider using the change tables CDC method instead. For more information about differences between the two methods, see [Overview of SQL Server as a source](https://docs.cloud.google.com/datastream/docs/sources-sqlserver#change-tables).  
SQL Server CDC configuration: failed. | The CDC method that you have selected doesn't comply with your database configuration. Change the CDC method and try again.  
  
## Salesforce errors

Error | Troubleshooting steps  
---|---  
Insufficient permissions. | The user of the connected app or the external client app that you configured to authenticate the connection between your Salesforce org and Datastream doesn't have sufficient permissions to access the data that you want to replicate. Make sure that you configured your Salesforce source correctly. For more information, see [Configure a Salesforce source](https://docs.cloud.google.com/datastream/docs/configure-salesforce-org).  
Bulk API 2.0 disabled. | Bulk API 2.0 is enabled by default for _Performance_ , _Unlimited_ , _Enterprise_ and _Developer_ editions. This error message indicates that the API is either disabled in your edition, or the credentials that you use don't have sufficient permissions. Make sure that the user profile that you use has the `API Enabled` permission granted.  
Limit exceeded. | You've exceeded the Salesforce API query limit. You see this message when you reach 90% of your API limit quota. In such a case, Datastream retries the operation at a later time. You might want to consider increasing your Salesforce API quota.  
Deleted limit exceeded. | When querying for deleted records, Salesforce limits the response to 600,000 record identifiers. The lowest querying granularity in Salesforce is one minute, and if you delete more than 600,000 records within a minute, Salesforce returns this error.  
Authentication error. | Datastream can't authenticate with Salesforce. You probably used the wrong credentials or domain name.  
  
## MongoDB errors

Error | Troubleshooting steps  
---|---  
Authentication failed. | Please check if the `authSource` for the Datastream user is `admin`. The Datastream user must be created in the `admin` database. This database is a privileged database that lets users run certain [administrative commands](https://www.mongodb.com/docs/manual/reference/command/#std-label-admin-commands).  
Database login failed. | Check your username and password and try again. Also, ensure that your user account has been created within the `admin` database. If the problem persists, it's possible that your user account was deleted or created incorrectly.  
Excluded objects list is invalid: `{exclude_list}`. | Specify your excluded objects in the following format: `DATABASE_NAME.COLLECTION_NAME.FIELD_NAME.NESTED_FIELD_NAME` with optional wildcards. Valid examples: `db.*`, `database.collection.*`, `database.*.field.*`.  
We're missing the necessary permissions to read from the source. | Assign the `readAnyDatabase` role to your user and try again.  
MongoDB version VERSION_NAME is not supported. | Please use version 5.0 or higher.  
Datastream was unable to execute the `buildinfo` command to determine the MongoDB version. | Ensure that the user has the necessary permissions to execute the `buildinfo` command and try again. For more information about the required permissions, see [Configure a MongoDB database](https://docs.cloud.google.com/datastream/docs/mongodb/configure-mongodb).  
The connection to the MongoDB cluster timed out. | Ensure that you've provided the correct hostname and credentials, and try again.  
We are unable to read the necessary data due to insufficient permissions. | Assign the `readAnyDatabase` role to the account that is used to connect to your MongoDB cluster, and try again.  
The user account that is used to connect to your MongoDB cluster does not exist. | Please create the user account and try again.  
We were unable to connect using the provided information. | Please verify that the correct connection format (SRV or Standard) is used and all the necessary information (like replica set names for replica set connection string) is included. For more information, see [Create a connection profile for a MongoDB database](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4mongodb).  
We encountered a MongoDB exception. Source error message: `{source_error}`. | If the source error message is unclear, contact Google Support.  
  
## Spanner errors

Error | Troubleshooting steps  
---|---  
Spanner read error. | If your Spanner database exists in a different project than the one in which Datastream is running, then make sure you've provided the [necessary permissions](https://docs.cloud.google.com/datastream/docs/configure-spanner#before-you-begin). Also, make sure that your Spanner database has sufficient CPU resources and isn't throttling requests.  
Change stream out of retention. | You can't recover a stream that experienced this error. The error means that Datastream has fallen behind your Spanner change stream retention window and lost data. If the retention window was short, for example if it lasted seconds or minutes, you can try to increase it and create a new stream.  
  
## BigQuery errors

Error | Troubleshooting steps  
---|---  
`BIGQUERY_UNSUPPORTED_PRIMARY_KEY_CHANGE, details: Failed to write to BigQuery due to an unsupported primary key change: adding primary keys to existing tables is not supported.` | If the primary key changes in the source, you must drop the table in BigQuery and initiate backfill again. This is a limitation of BigQuery, because there's no way to ensure correct merging of new events with existing rows if the primary key is different. For more information, see [Configure a BigQuery destination](https://docs.cloud.google.com/datastream/docs/destination-bigquery#known-limitations).  
The destination BigQuery table has significantly more records than the source table. | This can happen when the source table doesn't have a primary key. In such a case, Datastream processes the table in the append-only write mode, and each event for a given row appears as a separate row in BigQuery.  
Data gets duplicated when performing backfill in the **Append-only** write mode. | When you select the **Append-only** write mode for your stream, your data is appended in BigQuery as a stream of `INSERT`, `UPDATE-INSERT`, `UPDATE-DELETE` and `DELETE` events, without any consolidation. This might cause duplicate rows to be written to BigQuery when you perform backfill, or when an issue occurs and the BigQuery writer re-tries the write operations. To address the issue, we recommend that you run a de-duplication query similar to the following on a regular basis: `SELECT * FROM (SELECT *, row_number() OVER (PARTITION BY datastream_metadata.uuid) AS num FROM TABLE_NAME) WHERE num=1`  
Datastream is configured for the merge write mode, but changes aren't merged in BigQuery. | Verify that there's a primary key in your source table. BigQuery needs it to merge the changes into the destination table. A `UNIQUE` constraint doesn't fulfill the `PRIMARY KEY` requirement for merging events.If there's no primary key, consider adding one in either the source or destination table. To add a primary key in your destination BigQuery table, follow these steps:

  1. Pause the stream.
  2. Truncate the table in BigQuery.
  3. [Add the primary key](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#alter_table_add_primary_key_statement) to the table definition.
  4. Resume the stream.
  5. Trigger backfill for the table.

  
Unable to add a primary key, remove a primary key, or change the primary key definition for a table that's already replicated to BigQuery. | By default, Datastream doesn't support adding a primary key to a table that's already replicated to BigQuery without a primary key or removing a primary key from a table that's replicated to BigQuery with a primary key. You can, however, change the primary key definition for a source table replicated to BigQuery that already has a primary key:

  1. [Check the total latency metric for the stream](https://docs.cloud.google.com/datastream/docs/monitor-a-stream) and wait at least as long as the current latency to ensure that any in-flight events are written to the destination. This allows all events with the original primary key to be successfully streamed.
  2. [Pause the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#pauseastream).
  3. Copy the `CREATE TABLE` data definition language (DDL) command for the table in BigQuery: 
         
         SELECT ddl FROM PROJECT_ID.DATASET.INFORMATION_SCHEMA.TABLES
               WHERE table_name='TABLE_NAME';

Replace the following:
     * PROJECT_ID: the identifier of your Google Cloud project.
     * DATASET_ID: the identifier of the dataset in BigQuery.
     * TABLE_NAME: the name of the table for which you want to copy the DDL command.
  4. Drop the table in BigQuery.
  5. Adjust the `CREATE TABLE` DDL command with the new primary keys. Include the partition and cluster keys, and the `max_staleness` `OPTION`: 
         
         CREATE TABLE `[PROJECT_ID].[DATASET_ID].[TABLE_NAME]`
             (
               product_id INT64 NOT NULL,
               product_name STRING,
               datastream_metadata STRUCT,
               PRIMARY KEY (product_id) NOT ENFORCED
             )
             CLUSTER BY dept_no
             OPTIONS(
               max_staleness=INTERVAL '0-0 0 0:MINS:0' YEAR TO SECOND
             );
             ;
             

Replace the following:
     * PROJECT_ID: the identifier of your Google Cloud project.
     * DATASET_ID: the identifier of the dataset in BigQuery.
     * TABLE_NAME: the name of the table for which you copied the DDL command.
     * MINS: the number of minutes that you want to set for the `max_staleness` option, for example `15`.
  6. Run the adjusted query to recreate the table in BigQuery.
  7. [Resume the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#resumeastream).
  8. [Initiate backfill for the table](https://docs.cloud.google.com/datastream/docs/manage-backfill-for-the-objects-of-a-stream#initiatebackfill).

  
  
## What's next

  * To learn how to look for potential issues with your stream, see [Troubleshoot a stream](https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream).
  * To learn how to configure your source database, see [Sources](https://docs.cloud.google.com/datastream/docs/sources).
  * To learn how to configure your BigQuery or Cloud Storage destination, see [Destinations](https://docs.cloud.google.com/datastream/docs/destinations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
