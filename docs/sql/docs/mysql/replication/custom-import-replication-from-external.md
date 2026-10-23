---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/custom-import-replication-from-external/
title: Use a custom import to set up replication from large external databases \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:37.506425+00:00
---

# Use a custom import to set up replication from large external databases  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/custom-import-replication-from-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use a custom import to set up replication from large external databases Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes the process for setting up external server replication using a custom import. These steps are the best option when you need to replicate from a large external database.

You must complete all the steps on this page. When finished, you can administer and monitor the replica the same way as you would any other Cloud SQL instance.

This process is supported only for external servers that are configured to use global transaction identifier (GTID)-based replication. Before replication can be initiated, you need to load data from the external server into the Cloud SQL replica. If you don't use GTID-based replication, then Cloud SQL can't identify the exact binary log position from which to begin replication. If you can't use GITD-based replication, then you need to configure your dump tool to institute a global read-only lock during the dump process.

GTID replication isn't supported for [certain versions of Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.html), Amazon Aurora 5.6, and early releases of [Amazon Aurora 5.7](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-replication-gtid.html).

## Before you begin

Before you start, you should have [configured the external server](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setting_up_the_external_server_for_replication), created the [source representation instance](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-source-instance), and set up the [Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-replica-instance).

## Update permissions for the replication user

The replication user on the external server is configured to accept connections from any host (`%`). You should update this user account so that it can only be used with the Cloud SQL replica. Open a terminal on the source database server and enter these commands:

###  mysql Client 
    
    
        UPDATE mysql.user
        SET Host='NEW_HOST' WHERE Host='OLD_HOST' AND User='USERNAME';
        GRANT REPLICATION SLAVE, EXECUTE ON *.*
        TO 'GCP_USERNAME'@'HOST';
        FLUSH PRIVILEGES;

###  example 
    
    
    UPDATE mysql.user
    SET Host='192.0.2.0' WHERE Host='%' AND User='replicationUser';
    GRANT REPLICATION SLAVE, EXECUTE ON *.*
    TO 'gcp_user'@'gmail.com';
    FLUSH PRIVILEGES;
    

Property | Description  
---|---  
NEW_HOST | Specify the outgoing IP of the Cloud SQL replica.  
OLD_HOST | The current value assigned to `Host` that you want to change.  
USERNAME | The replication user account on the external server.  
GCP_USERNAME | The username for the GCP user account.  
HOST | The hostname for the GCP user account.  
  
## Set up the Cloud SQL replica as a primary instance

Because Cloud SQL replica instances are read-only, in order to perform a custom import, you need to [promote the Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica) to a standalone instance. Once the initial data import is complete, you demote the instance back to a replica.

## Perform a custom dump and import

In this section, we show you how to create the dump file and import it into the eventual Cloud SQL replica using [`mydumper`](https://github.com/maxbube/mydumper) or the [`mysqldump`](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) client utilities.

When you dump the data, you might need to exclude MySQL generic databases, including `mysql`, and `sys`, if they exist on the source instance. Otherwise, the data import fails. See [How to exclude (or include) databases?](https://github.com/maxbube/mydumper#how-to-exclude-or-include-databases).

### Use `mydumper` and `myloader`

To create a dump file and import it to Cloud SQL:

  1. Create a dump file of the external server database using `mydumper`.
         
         $ mydumper -u USERNAME -p PASSWORD \
                       --threads=16 -o ./backup \
                       -h HOST \
                       --no-locks \
                       --regex '^(?!(mysql\.|sys\.))'

Property | Description  
---|---  
USERNAME | The name of the replication user account or user account on the external server that has database read permissions.  
PASSWORD | Replication user password.  
HOST | The IPv4 or DNS address for the external server.  
  2. Import the data into the Cloud SQL instance using `myloader`.
         
         $ myloader -u REPLICA_USERNAME -p REPLICA_PASSWORD \
                     --threads=16 \
                     -d ./backup -h HOST -o

Property | Description  
---|---  
REPLICA_USERNAME | The user account on the Cloud SQL instance.  
REPLICA_PASSWORD | Cloud SQL instance user password.  
HOST | The IPv4 for the Cloud SQL instance.  
  3. Write down the GTID or binlog information of the data dump. You need this information when configuring the replication with the stored procedures.

To get the GTID or binlog information of the data dump, run the following command:
         
         sudo cat ./backup/metadata




### Use `mysqldump`

  1. Create a dump using `mysqldump`:

###  `mysqldump`
         
         mysqldump \
             --host=EXTERNAL_HOST \
             --port=EXTERNAL_PORT \
             --user=USERNAME\
             --password=PASSWORD \
             --databases=DATABASE_LIST  \
             --hex-blob \
             --master-data=EXTERNAL_DATA  \
             --no-autocommit \
             --default-character-set=utf8mb4 \
             --single-transaction \
             GTID_PURGED \
             ADD_DROP_TABLE \
             ROUTINES \
             COMPRESS \
             GZIP

Property | Description  
---|---  
EXTERNAL_HOST | The IPv4 or DNS address for the external server.  
EXTERNAL_PORT | The port for the external server. If the external server is hosted on Cloud SQL, this is `3306`.  
USERNAME | The name of the replication user account or user account on the external server that has database read permissions.  
USER_PASSWORD | Replication user password.  
DATABASE_LIST | Space-separated list of all databases on the external server, except for the system databases (`sys`,`mysql`, `performance_schema`, and `information_schema`). Use the `SHOW DATABASES` MySQL command to list your databases.  
EXTERNAL_DATA | If your external server does not support GTID, and you have permission to access the global read lock on it, use `--master-data=1`. Otherwise, don't use this property.  
GTID_PURGED | If your external server supports GTID, use `--set-gtid-purged=on`; otherwise, don't use this property.  
ADD_DROP_TABLE | If you want to add a `DROP TABLE` statement before each `CREATE TABLE` statement, include `--add-drop-table`.  
ROUTINES | If you want to show stored routines, such as procedures and functions, in the output for dumped databases, include `--routines`.  
COMPRESS | If you want to compress all information sent between the Cloud SQL replica and the external server, use `--compress`.  
GZIP | If you want to compress the dump file even more, use `| gzip`. If your database contains data that does not compress well, such as binary incompressible data or JPG images, don't use this.  
  
###  example 
         
         mysqldump \
             --host=192.0.2.1 \
             --port=3306 \
             --user=replicationUser \
             --password \
             --databases guestbook journal \
             --hex-blob \
             --master-data=1 \
             --no-autocommit \
             --default-character-set=utf8mb4 \
             --single-transaction \
             --compress \
             | gzip

  2. Write down the GTID or binlog information of the data dump. You need this information to configure the replication with the Cloud SQL stored procedures.

For the GTID, look for a line similar to the following:
         
         SET @@GLOBAL.GTID_PURGED='32eb1e6a-17b6-11ea-a39e-06d94ac3ec98:1-33496';

For the binlog, look for a line similar to the following:
         
         CHANGE MASTER TO MASTER_LOG_FILE='mysql-bin-changelog.033877', MASTER_LOG_POS=360;

  3. Remove the following lines in the dump file that require super privileges. Since Cloud SQL users don't have super privileges, these lines cause the import to fail.

For GTID-based replication: Remove the SET GTID_PURGED statement along with the session variable setting statement in the dump. For example:
         
         ...
            SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
            SET @@SESSION.SQL_LOG_BIN= 0;
            ...
            SET @@GLOBAL.GTID_PURGED='32eb1e6a-17b6-11ea-a39e-06d94ac3ec98:1-33496';
            ...
            SET @@SESSION.SQL_LOG_BIN=@MYSQLDUMP_TEMP_LOG_BIN;

For binlog-based replication, remove the CHANGE MASTER statement. For example:
         
         ...
            CHANGE MASTER TO MASTER_LOG_FILE='mysql-bin-changelog.033877', MASTER_LOG_POS=360;
             ...

  4. Import the data into the Cloud SQL replica, using the `mysql` CLI:

###  `mysql`
         
         mysql -h REPLICA_HOST -u REPLICA_USER \
         -p REPLICA_DATABASE_NAME RESULT_FILE

Property | Description  
---|---  
REPLICA_HOST | Host on which MySQL server is located.  
REPLICA_USER | MySQL user name to use when connecting to the server.  
REPLICA_DATABASE_NAME | Name of the database where the data is located.  
RESULT_FILE | Name of the dump file to import.  
  
###  example 
         
         mysql -h 255.255.255.255 -u replica_username -p replica_db < result.sql
         




You can also import the dump file using a Google Cloud bucket. See [Importing data from a SQL dump file into Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/import-export/importing#mysqldump).

## Demote the Cloud SQL instance

To demote the Cloud SQL instance to a Cloud SQL replica, use the [demoteMaster](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/demoteMaster) method on the instance.

  1. Prepare a request JSON file with the name of the instance you want to demote.

###  Source JSON 
         
         {
             "demoteMasterContext": {
               "masterInstanceName": SOURCE_REPRESENTATION_INSTANCE_NAME,
               "skipReplicationSetup": true
               }
          }

Property | Description  
---|---  
SOURCE_REPRESENTATION_INSTANCE_NAME | The name of the source representation instance.  
  
###  example 
         
         {
              "demoteMasterContext": {
                "masterInstanceName": "cloudsql-source-instance",
                "skipReplicationSetup": true
              }
            }

  2. Open a terminal and use the following commands to invoke `demoteMaster`:

###  curl 
         
         gcloud auth login
           ACCESS_TOKEN="$(gcloud auth print-access-token)"
           curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @JSON_PATH \
             -X POST \
           https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE-NAME/demoteMaster

Property | Description  
---|---  
JSON_PATH | The path to the `JSON` file.  
PROJECT_ID | The ID of your project in Google Cloud.  
INSTANCE-NAME | The name of the instance to demote.  
  
###  example 
         
         gcloud auth login
            ACCESS_TOKEN="$(gcloud auth print-access-token)"
            curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
              --header 'Content-Type: application/json' \
              --data @./source.json \
              -X POST \
            https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances/cloudsql-replica-instance/demoteMaster




### What you should see when you finish

To ensure your instances were set up correctly, go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances).

You should see your source representation instance and Cloud SQL replica. They look similar to the following:

Instance ID | Type | Public IP  
---|---|---  
(-) source-representation-instance | MySQL external primary | 10.68.48.3:3306  
replica-instance | MySQL read replica | 34.66.48.59  
  
## Start replication on the Cloud SQL instance

**Note:** IP addresses should be preserved in the Promote or Demote steps. If another operation comes in between the steps, then the IP address of the Cloud SQL instance may change. If replication is broken because of a connectivity issue, check the outgoing IP addresses and make sure that the appropriate IP addresses are allowlisted on the external source.

This step uses Cloud SQL stored procedures. The Cloud SQL stored procedures are installed after calling the `demoteMaster` request. They are removed after calling `promoteReplica`. For more information, see [Stored procedures for replication management](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures#stored_procedures_for_replication_management).

  1. Log on to the replica instance. For more information, see [Connecting using a database client from a local machine](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip).
  2. Use the `mysql.resetMaster` stored procedure to reset replication settings.
         
         mysql> call mysql.resetMaster();

  3. Configure the replication. This step requires the GTID or binlog information that you previously wrote down.

###  GTID 

     1. Configure the `gtid_purged` field with the `mysql.skipTransactionWithGtid(GTID_TO_SKIP)` stored procedure.
Property | Description  
---|---  
GTID_TO_SKIP | The [GTID set](https://dev.mysql.com/doc/refman/5.7/en/replication-gtids-concepts.html#replication-gtids-concepts-gtid-sets) value to configure.  
  
For example: 
    
    mysql> call mysql.skipTransactionWithGtid('32eb1e6a-17b6-11ea-a39e-06d94ac3ec98:1-33496');

     1. Run the `mysql.setupExternalSourceAutoPosition(HOST, PORT, USER_NAME, USER_PASSWORD, MASTER_AUTO_POSITION, USE_SSL, USE_SSL_CLIENT_AUTH)` stored procedure.
Property | Description  
---|---  
HOST | Source endpoint.  
PORT | Source port.  
USER_NAME | Source user.  
USER_PASSWORD | Source user password.  
MASTER_AUTO_POSITION | Value of the `master_auto_position` parameter. Possible values are `0`, `1`.  
USE_SSL | Whether to use SSL-based replication. Possible values are `true`, `false`. If `true`, you need to set the `caCertificate` field in the `DemoteMaster` request.  
USE_SSL_CLIENT_AUTH | Whether to use SSL client authentication. Possible values are `true`, `false`. If `true`, you need to set the [`clientKey` and `clientCertificates`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/demoteMaster#demotemastermysqlreplicaconfiguration) fields in the `demoteMaster` request.  
      
    mysql> call mysql.setupExternalSourceAutoPosition('1.1.1.1', 3306, \
        'USERNAME', 'PASSWORD', \
        /* master_auto_position= */ 1,false, false); \

###  binlog 

Run the `mysql.setupExternalSource(HOST, PORT, USER_NAME, USER_PASSWORD, SOURCE_LOG_NAME, SOURCE_LOG_POS, USE_SSL, USE_SSL_CLIENT_AUTH)` stored procedure.

Property | Description  
---|---  
HOST | Source endpoint.  
PORT | Source port.  
USER_NAME | Source user.  
USER_PASSWORD | Source user password.  
SOURCE_LOG_NAME | The name of the binary log on the source database instance that contains the replication information.  
SOURCE_LOG_POS | The location in the `mysql_binary_log_file_name` binary log at which replication starts reading the replication information.  
USE_SSL | Whether to use SSL-based replication. Possible values are `true`, `false`. If `true`, you need to set the `caCertificate` field in the `DemoteMaster` request.  
USE_SSL_CLIENT_AUTH | Whether to use SSL client authentication. Possible values are `true`, `false`. If `true`, you need to set the [`clientKey` and `clientCertificates`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/demoteMaster#demotemastermysqlreplicaconfiguration) fields in the `demoteMaster` request.  
      
    mysql> call mysql.setupExternalSource('1.1.1.1', 3306, \
        'user_name', 'password', 'mysql-bin-changelog.033877', 360, \
        false, false);

  4. Use the `mysql.startReplication()` stored procedure to start replication from the external database.
         
         mysql> call mysql.startReplication();

  5. Verify the replication status. Make sure that both the `Slave_IO_Running` and `Slave_SQL_Running` fields say `YES`.
         
         mysql> show slave status\G

The output from this command looks similar to the following:
         
         *************************** 1. row ***************************
                            Slave_IO_State: Waiting for master to send event
                               Master_Host: 1.1.1.1
                               Master_User: user_name
                               Master_Port: 3306
                             Connect_Retry: 60
                           Master_Log_File: mysql-bin-changelog.000001
                       Read_Master_Log_Pos: 1
                            Relay_Log_File: relay-log.000002
                             Relay_Log_Pos: 1
                     Relay_Master_Log_File: mysql-bin-changelog.000001
                          Slave_IO_Running: Yes
                         Slave_SQL_Running: Yes
                           Replicate_Do_DB:
                       Replicate_Ignore_DB:
                        Replicate_Do_Table:
                    Replicate_Ignore_Table:
                   Replicate_Wild_Do_Table:
               Replicate_Wild_Ignore_Table: mysql.%
                                Last_Errno: 0
                                Last_Error:
                              Skip_Counter: 0
                       Exec_Master_Log_Pos: 412
                           Relay_Log_Space: 752
                           Until_Condition: None
                            Until_Log_File:
                             Until_Log_Pos: 0
                        Master_SSL_Allowed: No
                        Master_SSL_CA_File:
                        Master_SSL_CA_Path:
                           Master_SSL_Cert:
                         Master_SSL_Cipher:
                            Master_SSL_Key:
                     Seconds_Behind_Master: 0
             Master_SSL_Verify_Server_Cert: No
                             Last_IO_Errno: 0
                             Last_IO_Error:
                            Last_SQL_Errno: 0
                            Last_SQL_Error:
               Replicate_Ignore_Server_Ids:
                          Master_Server_Id: 1509941531
                               Master_UUID: 1cb2c80e-90f0-11eb-9ea3-02389b1c2e6f
                      Master_Info_File: mysql.slave_master_info
                             SQL_Delay: 0
                   SQL_Remaining_Delay: NULL
               Slave_SQL_Running_State: Slave has read all r
                    Master_Retry_Count: 86400
                           Master_Bind:
               Last_IO_Error_Timestamp:
              Last_SQL_Error_Timestamp:
                        Master_SSL_Crl:
                    Master_SSL_Crlpath:
                    Retrieved_Gtid_Set:
                     Executed_Gtid_Set: 478af53c-bd24-11eb-be72-42010a80002a:1-226
                         Auto_Position: 0
            1 row in set (0.00 sec)




## Proceed with replication

Once you start replication from the external server, you need to monitor replication and then complete your migration. To learn more, see [Monitoring replication](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#monitoring_replication).

## Troubleshoot

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
  
### Review your replication logs

When you verify your replication settings, logs are produced.

You can view these logs by following these steps:

  1. Go to the Logs Viewer in the Google Cloud console. 

[Go to the Logs Viewer](https://console.cloud.google.com/logs?resource=cloudsql_database)

  2. Select the Cloud SQL replica from the **Instance** dropdown.
  3. Select the `replication-setup.log` log file.



If the Cloud SQL replica is unable to connect to the external server, confirm the following:

  * Any firewall on the external server is configured to allow connections from the Cloud SQL replica's outgoing IP address.
  * Your SSL/TLS configuration is correct.
  * Your replication user, host, and password are correct.



## What's next

  * Learn about [updating an instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance).
  * Learn about [managing replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas).
  * Learn about [monitoring instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance).
  * Learn about [promoting your Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica) to [promote the replica to a standalone instance and stop replicating from the external server](https://docs.cloud.google.com/sql/docs/mysql/migrate-data#migrating-to-sql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
