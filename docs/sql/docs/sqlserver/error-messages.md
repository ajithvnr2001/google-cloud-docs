---
url: https://docs.cloud.google.com/sql/docs/sqlserver/error-messages/
title: Cloud SQL for SQL Server error messages \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:07.920778+00:00
---

# Cloud SQL for SQL Server error messages  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/error-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Cloud SQL for SQL Server error messages Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/error-messages "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/error-messages "View this page for the PostgreSQL database engine") | SQL Server

This page discusses some of the error messages encountered in Cloud SQL.

## Overview

Error messages in Cloud SQL come from many sources and appear in many places. Some error messages come from the database engines themselves, some from the Cloud SQL service, some from client applications, and some are returned by calls to the Cloud SQL Admin API.

This page includes some of the most common errors seen in Cloud SQL. If you don't find the error code or message you are looking for here, you can look for source reference material here: 

  * [SQL Server error reference pages](https://docs.microsoft.com/en-us/sql/relational-databases/errors-events/database-engine-events-and-errors?view=sql-server-ver15)




If you don't find the reference material for the error message that you're seeing, you can also search in some of these places where other users may have relevant experience: 

  * [Cloud SQL questions on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-sql%5D+error)
  * [Public issue tracker for Cloud SQL](https://issuetracker.google.com/savedsearches/559773)
  * [DBA Stack Exchange](https://dba.stackexchange.com/tags/google-cloud-sql/hot)
  * [Cloud SQL discuss group](https://groups.google.com/g/google-cloud-sql-discuss/search?q=error&sortBy=DATE)
  * [Google Cloud Slack community](https://googlecloud-community.slack.com/)
  * [Google Cloud on Reddit](https://www.reddit.com/r/googlecloud/)



## Operational errors

A | B | C | D | E | F | G | I | L | M | N | O | P | Q | R | S | T | U | W

Error message | Troubleshooting | Allocated IP range not found in network. | VPC peerings were not updated after an allocated range was modified or removed. You need to [ modify the private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modifying-connection). Use the following command, and make sure to use the `--force` argument:
    
    
    gcloud services vpc-peerings update \
    --network=VPC_NETWORK \
    --ranges=ALLOCATED_RANGES \
    --service=servicenetworking.googleapis.com \
    **--force**  
  
---|---  
Error message | Troubleshooting | Bad request. | This message can have many causes. `Illegal Argument` is one of the most common. In this case, the request is using either the wrong argument or an invalid value for the argument. For the many other causes, the error message might contain a useful hint. For `Illegal Argument`, check the request to make sure each argument is permissible and each value for the argument is valid. For all other causes, [check the log files](https://docs.cloud.google.com/sql/docs/sqlserver/logging) to see if there is more information there.  
---|---  
Error message | Troubleshooting | Cannot modify allocated ranges in CreateConnection. Please use UpdateConnection. | VPC peerings were not updated after an allocated range was modified or removed. You need to [modify the private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modifying-connection). Use the following command, and make sure to use the `--force` argument:
    
    
    gcloud services vpc-peerings update \
    --network=VPC_NETWORK \
    --ranges=ALLOCATED_RANGES \
    --service=servicenetworking.googleapis.com \
    **--force**  
  
---|---  
Constraints/sql.restrictAuthorizedNetworks. | The cloning operation is blocked by the `Authorized Networks` configuration. `Authorized Networks` are configured for public IP addresses in the Connectivity section of the Google Cloud console, and cloning isn't permitted due to [security considerations](https://docs.cloud.google.com/sql/docs/sqlserver/connection-org-policy). Remove all `Authorized Networks` entries from the Cloud SQL instance if you can. Otherwise, [create a replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica) without any `Authorized Networks` entries.  
Could not allocate a new page for database database_name because of insufficient disk space in filegroup `PRIMARY`. | The `PRIMARY` filegroup, which is the main and default filegroup in a database, has run out of space. Use the [`sp_helpdb`](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-helpdb-transact-sql?view=sql-server-ver15) command to get information about the database. Consider the following solutions:

  * Manually expand the disk space or reduce the data in the database. 
  * Ensure that [`Automatic storage increase`](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen) is enabled for the database instance.
  * Add more filegroups and move data into them.
  * Ensure that growth is not limited. Use the [`ALTER DATABASE`](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-file-and-filegroup-options?view=sql-server-ver15) command to enable autogrowth, if it is not already enabled, and to increase the maximum file size.
  * Manage [tempdb](https://docs.cloud.google.com/sql/docs/sqlserver/manage-tempdb) files. Use the [`DBCC OPENTRAN`](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-opentran-transact-sql?view=sql-server-ver15) and [`DBCC SQLPERF`](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-sqlperf-transact-sql?view=sql-server-ver15)commands to check for open transactions that can cause the tempdb file or the transaction log to grow.

  
Error message | Troubleshooting | Disk is full. | The primary instance disk size can become full during replica creation. [ Edit the primary instance](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance#editing_an_instance) to upgrade it to a larger disk size.  
---|---  
Error message | Troubleshooting | Failed to create subnetwork. | No more available addresses in the IP range. Couldn't find free blocks in allocated IP ranges. Please allocate new ranges for this service provider. There are no more available addresses in the allocated IP range. Consider these possible scenarios:

  * The size of the allocated IP range for the private service connection is smaller than /24.
  * The size of the allocated IP range for the private service connection is too small for the number of Cloud SQL instances.
  * The requirement on the size of allocated IP range will be larger if instances are created in multiple regions. See [allocated range size](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated_range_size)

For each of the previously listed scenarios, you can elect to either expand the existing or [ allocate an additional IP range](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access#allocating_an_ip_address_range) to the private service connection. If you're allocating a new range, take care to not create an allocation that overlaps with any existing allocations. After creating a new IP range, update the VPC peering with the following command:
    
    
    gcloud services vpc-peerings update \
    --service=servicenetworking.googleapis.com
    --ranges=OLD_RESERVED_RANGE_NAME,NEW_RESERVED_RANGE_NAME \
    --network=VPC_NETWORK
    --project=PROJECT_ID \
    --force

If you're expanding an existing allocation, take care to only increase the allocation range and not decrease it. For example, if the original allocation was 10.0.10.0/24, make the new allocation at least 10.0.10.0/23. In general, if starting from a /24 allocation, decrementing the /mask by 1 for each condition (additional instance type group, additional region) is a good rule of thumb. For example, if trying to create both instance type groups on the same allocation, going from /24 to /23 is enough. After expanding an existing IP range, update the vpc peering with following command:
    
    
    gcloud services vpc-peerings update \
    --service=servicenetworking.googleapis.com
    --ranges=RESERVED_RANGE_NAME \
    --network=VPC_NETWORK \
    --project=PROJECT_ID \
    --force  
  
---|---  
Error message | Troubleshooting | (gcloud.sql.connect) It seems your client does not have ipv6 connectivity and the database instance does not have an ipv4 address. | You're trying to connect to your private IP instance using Cloud Shell. Connecting from Cloud Shell to an instance with only a private IP address isn't supported.  
---|---  
Error message | Troubleshooting | Internal error. | The project could be missing the Service Networking service account required for this feature. You can manually create the service account by following the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).  
---|---  
Invalid request: Incorrect Service Networking config for instance. | `Service Networking API` isn't enabled in the project. [Enable the `Service Networking API`](https://console.cloud.google.com/apis/dashboard) in your project. If you see this error when you're trying to assign a private IP address to a Cloud SQL instance, and you're using a Shared VPC, you also need to enable the `Service Networking API` for the host project.  
Instance is not eligible for replica creation. | The primary instance doesn't meet the necessary requirements for replication. For a list of requirements, see [Replication limitations](https://docs.cloud.google.com/sql/docs/sqlserver/replication#sql-server-limitations).  
Error message | Troubleshooting | Login failed for user 'XXX'. | Confirm that the user has privileges on the instance and database to which they are trying to connect and ensure the right credentials are being used.  
---|---  
Login 'test' owns one or more database(s). Change the owner of the database(s) before dropping the login. | If you want to drop the user login associated with a database owner that's no longer active, [you must first assign a new database owner](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-databases#change-database-owner).  
Error message | Troubleshooting | Network association failed. | The `Service Networking API` isn't enabled in the project. [Enable the `Service Networking API`](https://console.cloud.google.com/apis/dashboard) in your project. If you see this error when you're trying to assign a private IP address to a Cloud SQL instance, and you're using a Shared VPC, you also need to enable the `Service Networking API` for the host project.  
---|---  
Error message | Troubleshooting | Operation failed because another operation was already in progress. | Most operations in Cloud SQL are synchronous. You can run only one at a time. Wait for the previous operation to finish before beginning another.  
---|---  
Error message | Troubleshooting | Quota exceeded. | You reached the limit of your per-minute or daily quota. Review the [quotas and limits](https://docs.cloud.google.com/sql/docs/sqlserver/quotas) for Cloud SQL. Request an increase to your quotas from the [Google Cloud console](https://console.cloud.google.com/).  
---|---  
Error message | Troubleshooting | Request is missing a valid API key. | You might not have a valid service account key JSON file, or it might not be stored in the expected location. Verify that you have a valid service account key JSON file in the location stored in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable and that the variable points to the correct location.  
---|---  
Error message | Troubleshooting | SSL error: invalid padding. | Server certificate error. Create a new server certificate and [rotate](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance).  
---|---  
System error occurred. | 

  * The user might not have all the Cloud Storage permissions it needs.
  * The database table might not exist.

Try these things ...

  * Check that you have at least `WRITER` permissions on the bucket and `READER` permissions on the export file. For more information on configuring access control in Cloud Storage, see [Create and Manage Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists)
  * Ensure the table exists. If the table does exist, confirm that you have the correct permissions on the storage bucket.

  
  
Error message | Troubleshooting | Unauthorized to connect. | There can be many causes because authorization occurs at many levels: 

  * At the database level, the database user must exist and its password match
  * At the project level, the user might not have the correct IAM permissions, including the `serviceusage.services.use` or `cloudsql.instances.connect` permissions.
  * At the network level, if the Cloud SQL instance is using public IP the connection's source IP must be in an authorized network.

Try these things ...

  * Ensure the user exists and its password matches.
  * Assign the `Service Usage Consumer` role to the user account. This role includes the permission `serviceusage.services.use`.
  * If using public IP, ensure the source IP is in an authorized network.

  
---|---  
Error message | Troubleshooting | x509: certificate isn't valid for any names. | Known issue: The [ Cloud SQL Proxy Dialer](https://github.com/GoogleCloudPlatform/cloudsql-proxy/tree/master/proxy#cloud-sql-proxy-dialer-for-go) isn't compatible with Go 1.15 at this time. Until fixed, see [ this discussion on GitHub](https://github.com/golang/go/issues/40748), which includes a workaround.  
---|---  
  
## Unknown errors

The following table shows some known cases where an `Unknown Error` can occur, and lists specific remedies where applicable. However, this is not a complete list. If you don't find your case in the table, check with the [public issue tracker for Cloud SQL](https://issuetracker.google.com/savedsearches/559773). If you don't find the issue there, consider [ submitting a report](https://issuetracker.google.com/issues/new?component=187202&template=0), or reviewing [other support options](https://docs.cloud.google.com/sql/docs/sqlserver/support).

Operation | The issue might be...  | Things to try... | Add user | If the user already exists in the database, this error can occur when you try to add them. | Check to make sure the user doesn't already exist in the database.  
---|---|---  
Backup | If you see this during automated or manual backups, it's likely the instance disk is full. | If the temporary file size is taking up too much space, you can restart the instance to remove the file and free up the disk space. Otherwise, you might need to upgrade your instance to a larger disk size.  
Clone | This can occur when there is a shortage of resources in the selected zone. | Try another zone in the region, or wait and try again later.  
Create instance | 

  * This can occur when you are trying to re-use the same name as a recently-deleted instance.
  * It can also be caused by intermittent connectivity issues.
  * The [logs](https://console.cloud.google.com/logs/query) might show that the Service Networking API is not enabled for the project.
  * The error has also been seen when trying to create multiple instances in parallel. For example, Terraform scripts make this attempt possible.
  * Another cause can be that a specific resource is exhausted or a quota limit has been exceeded. Look in the logs for an entry like `Quota 'INTERNAL_FORWARDING_RULES_WITH_TARGET_INSTANCE_PER_NETWORK' exceeded. Limit: 100.0 globally`
  * This error can occur if subnet creation fails when there are no more available addresses in the IP range.

| 

  * Instance names cannot be re-used until about a week after deletion.
  * In the case of intermittent connectivity issues, the only remedy is to try again.
  * [ Enable the Service Networking API](https://console.cloud.google.com/apis/dashboard) for the project.
  * Parallel instance creation scripts will only succeed in creating one of the instances. Modify the script to wait until each instance create operation is complete before continuing to the next one.
  * [Allocate new ranges](https://docs.cloud.google.com/sql/docs/troubleshooting#new-ranges-tips).

  
Export | If you see this while trying to export a database to a Cloud Storage bucket, the transfer may be failing due to a bandwidth issue. | The Cloud SQL instance may be located in a different region than the Cloud Storage bucket. Reading and writing data from one continent to another involves a lot of network usage, and can cause intermittent issues like this.  
Failover (automatic) | An automatic failover operation can produce this error message when the service detects that the primary instance is still responsive. | There is nothing to be done in this case. The failover won't occur because it isn't needed.  
Import | The import file may contain statements which require the superuser role. | Edit the file to remove any statements which require the superuser role.  
  
Cloud SQL also uses some third-party binaries (for example, `mysqld`), which can generate unknown error messages. Such errors are internal to the third-party binaries and are outside the scope of Cloud SQL. However, sometimes a more specific error can be found in the [ Cloud SQL log files](https://console.cloud.google.com/logs/query) at around the same time.

Also, sometimes it is an **error code** that is unknown. In this case, the complete message can be `Unknown Error Code`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
