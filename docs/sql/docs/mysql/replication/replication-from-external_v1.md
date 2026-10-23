---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external_v1/
title: Replicating from an external server (v1) \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:45.285252+00:00
---

# Replicating from an external server (v1)  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)



Send feedback 

#  Replicating from an external server (v1) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Caution:** Please use this document only if you implemented replication before September 21, 2020. Otherwise, [use the current workflow here](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external).

This page describes how to create a configuration that replicates data from a source database server to MySQL replicas.

The source database server can be any MySQL server that meets all of the server requirements, including Cloud SQL instances. Instances hosted by other cloud providers can also serve as the data source, provided they meet the requirements, including supporting GTID.

For more detailed information about this configuration, see [About Replicating from an External Server](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server).

## Before you begin

Before you set up replication from an external server, you must complete the following steps:

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  * Install and authenticate the [](https://docs.cloud.google.com/sdk/downloads)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 
  * Ensure that your server meets the requirements for the source database server. 
  * Determine what [level of security](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options) you require for the connections between the primary instance and the replica, and obtain the required certificate files. 
  * Decide which [Google Cloud region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) you want to use to contain your Cloud SQL replica. 
  * Assemble the required information about your source database server:

    * External IPv4 address and port number

By default, MySQL uses port 3306.

    * MySQL replication user account and password
    * MySQL version number
    * Location of all required SSL/TLS certificates and keys, depending on the [level of security](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options) you selected
  * Be prepared to update the network firewall for your source database server to accept connections from the Cloud SQL replica.

This step must be completed within 30 minutes of creating the replica.

  * If you are not a project owner, you must have the `Storage Admin` role. 



## Requirements for the source database server

Before you can replicate from an external server to a Cloud SQL replica, ensure that the source database server meets these configuration requirements:

  * Running MySQL Community Edition, version 5.6 or 5.7.

  * Binary logs enabled. [Learn more](https://dev.mysql.com/doc/refman/8.4/en/binary-log.html).

  * Binary logs retained long enough for replica to complete the import.

Generally, a week is sufficient. [Learn more about setting the binary log retention policy](https://dev.mysql.com/doc/refman/8.4/en/replication-options-binary-log.html#sysvar_expire_logs_days).

  * Using row-based binary logging. [Learn more](https://dev.mysql.com/doc/refman/8.4/en/replication-rbr-usage.html).

  * GTID enabled, and GTID consistency enforced.

[Learn more about GTID](https://dev.mysql.com/doc/refman/8.4/en/replication-gtids.html). See the option for [enforcing GTID consistency](https://dev.mysql.com/doc/refman/8.4/en/replication-options-gtids.html#sysvar_enforce_gtid_consistency).

  * All tables (except tables in system databases) use the InnoDB storage engine.

[Learn more about InnoDB](https://dev.mysql.com/doc/refman/8.4/en/innodb-storage-engine.html). [Learn more about converting to InnoDB](https://dev.mysql.com/doc/refman/8.4/en/converting-tables-to-innodb.html).

  * MySQL user account with the `REPLICATION_SLAVE` privilege.

Configure this account to accept connections from anywhere (host = `%`). You can restrict access to this user in a later step. Do not use this user account for any purpose other than replication.

[Learn more about privileges](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_replication-slave). [Learn more about user accounts](https://docs.cloud.google.com/sql/docs/mysql/users#mysql_user_account_format).

  * An externally accessible IPv4 address and TCP port.




## Configuration process

To set up replication from an external database server, you perform the following steps:

  1. Create a Cloud Storage bucket for your data.
  2. Export your data to Cloud Storage.
  3. Set up the replication configuration.
  4. Configure the source database server to accept connections from the replica.

**Note:** this step must be done within 30 minutes of replica creation.
  5. Restrict access to the MySQL replication user.

  6. Finalize the replica configuration.

  7. Confirm replication status.

  8. Clean up your storage.




### 1\. Create a Cloud Storage bucket for your data

Create a bucket to temporarily hold your data during the export process, or use an existing bucket.

For more information about creating a bucket, see [Creating Storage Buckets](https://docs.cloud.google.com/storage/docs/creating-buckets). For more information about the Storage Admin role, see [Cloud Storage IAM Roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

### 2\. Export your data to Cloud Storage

The replica looks for its data in Cloud Storage, so you put a copy of the server's data there. You can continue to accept write operations to your server after the export. After the replica finishes importing the dump file, it starts processing all changes since the export was taken and eventually catches up to the primary.

**Important:** While [mysqldump](https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html) is running, do not perform any [DDL operations](https://dev.mysql.com/doc/refman/8.4/en/glossary.html#glos_ddl) on the primary instance. Doing so could cause inconsistencies in the export file.

From a machine with the gcloud CLI installed and network connectivity to your MySQL server, run the following command:
    
    
    mysqldump \
        -h [PRIMARY_INSTANCE_IP] -P [PRIMARY_INSTANCE_PORT] -u [USERNAME] -p \
        --databases [DBS]  \
        --hex-blob  --skip-triggers  --master-data=1  \
        --order-by-primary --no-autocommit \
        --default-character-set=utf8mb4 \
        --single-transaction --set-gtid-purged=on | gzip | \
        gcloud storage cp - gs://[BUCKET]/[PATH_TO_DUMP]
    
    If the source of the migration is a Relational Database Service (RDS) for MySQL,
    the master-data flag is not supported and should not be specified.
    This command might look like the following example:
    
    mysqldump \
        -h [PRIMARY_INSTANCE_IP] -P [PRIMARY_INSTANCE_PORT] -u [USERNAME] -p \
        --databases [DBS]  \
        --hex-blob  --skip-triggers \
        --order-by-primary --no-autocommit \
        --default-character-set=utf8mb4 \
        --single-transaction --set-gtid-purged=on | gzip | \
        gcloud storage cp - gs://[BUCKET]/[PATH_TO_DUMP]
    
    Additionally, you should configure RDS instances to retain binlogs for a
    a longer period of time.
    This command might look like the following example:
    
    // Sets the retention period to one day.
    call mysql.rds_set_configuration('binlog retention hours', 24);
    

**Note:** You must use a version of mysqldump that supports the `--set-gtid-purged` flag. This is required for the export to be usable by the replica. The `mysqldump` utility bundled with MySQL versions 5.6 and 5.7 supports this flag.

Replace `[PROPERTIES_IN_BRACKETS]` with the following values:

Property | Value  
---|---  
`[PRIMARY_INSTANCE_IP]` | The IPv4 address for the source database server.  
`[PRIMARY_INSTANCE_PORT]` | The port for the source database server.  
`[USERNAME]` | The MySQL replication user account.  
`[PASSWORD]` | The password for the MySQL replication user account.  
`[DBS]` | Space-separated list of all databases on the source database server, except for the system databases (`sys`, `mysql`, `performance_schema`, and `information_schema`). Use the `SHOW DATABASES` MySQL command to list your databases.  
`[BUCKET]` | The name of the bucket you created to hold the export file.  
`[PATH_TO_DUMP]` | The path to the export file.  
**Note:** The `gzip` command causes the dump file to be compressed. If your database contains data that does not compress well, such as binary incompressible data or JPG images, remove `gzip |` from the previous command.

If you see a warning about partial dumps and GTIDs, that is expected.

This command might look like the following example:
    
    
    mysqldump \
        -h 192.0.2.1 -P 3306 -u replicationUser \
        --databases guestbook  \
        --hex-blob  --skip-triggers  --master-data=1  \
        --order-by-primary --no-autocommit \
        --default-character-set=utf8mb4 \
        --single-transaction --set-gtid-purged=on | gzip | \
        gcloud storage cp - gs://export-bucket/hq-primary1.sql.gz
    

### 3\. Create the replication configuration

If the replica is using private IP, the source database server must be [configured](https://docs.cloud.google.com/sql/docs/mysql/private-ip) for access from the replica's VPC. Creating replicas on Private VPCs is only supported through the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and the Cloud SQL Admin API.

###  Console 

This step creates the Cloud SQL replica and the [source representation instance](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#config-description).

  1. Open the Cloud SQL instance list in the Google Cloud console.

[Open the instance list](https://console.cloud.google.com/sql/instances)

  2. Click **Migrate data** in the button bar to open the Cloud SQL Migration Assistant.

  3. Click **Begin migration**.

  4. In the **Source database name** field, provide a name for the replication configuration in Cloud SQL.

This name is a reference for the configuration, use any valid Cloud SQL instance name.

  5. Enter the IP address and port number for your source database server.

  6. Provide the user name and password for the MySQL user that will be used for the replication connection.

  7. Select the MySQL version of your source database server.

  8. If you are using SSL/TLS for the connection between the replica and the source database server (recommended), select **Enable SSL/TLS security** and provide the SSL/TLS certificate information for your source server.

For more information about SSL/TLS options, see [SSL/TLS options](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options).

  9. Click **Next** , and fill in the details for your replica.

To ensure that the import happens as efficiently as possible, configure the replica with roughly enough storage to contain the database. Size the cores and memory to be similar to the source server.

  10. Provide the path to the dump file you uploaded to Cloud Storage earlier.

  11. Click **Create** to create the replica.

  12. Click **Next**.




###  gcloud 

  1. Create the [source representation instance](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#config-description).
         
         gcloud beta sql instances create [REPLICA_NAME] \
             --region=[REGION] --database-version=[MYSQL_VERSION] \
             --source-ip-address=[SOURCE_IP] --source-port=[SOURCE_PORT]
         

If the replica is using a private IP address, also add: \--network=[VPC_NETWORK_NAME]

Replace `[PROPERTIES_IN_BRACKETS]` with the following values:

Property | Value  
---|---  
`[SOURCE_REPRESENTATION_NAME]` | The name of the source representation instance. Use any valid Cloud SQL instance name.  
`[REGION]` | The [region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) where you want your Cloud SQL replicas to reside.  
`[MYSQL_VERSION]` | The MySQL version running on your source database server: `MYSQL_5_6` or `MYSQL_5_7`.  
`[SOURCE_IP]` | The externally accessible IPv4 address for the source database server.  
`[SOURCE_PORT]` | The externally accessible port for the source database server.  
  2. Create the Cloud SQL replica:
         
         gcloud beta sql instances create [REPLICA_NAME] \
             --master-instance-name=[SOURCE_REPRESENTATION_NAME] \
             --master-username=[USERNAME] --prompt-for-master-password \
             --master-dump-file-path=gs://[BUCKET]/[PATH_TO_DUMP] \
             --master-ca-certificate-path=[SOURCE_SERVER_CA_PATH] \
             --client-certificate-path=[CLIENT_CERT_PATH] \
             --client-key-path=[PRIVATE_KEY_PATH] \
             --tier=[MACHINE_TYPE] --storage-size=[DISK_SIZE]
         

If the replica is using a private IP address, also add: \--network=[VPC_NETWORK_NAME]

Replace `[PROPERTIES_IN_BRACKETS]` with the following values:

Property | Value  
---|---  
`[REPLICA_NAME]` | The name of the Cloud SQL read replica. Use any valid Cloud SQL instance name.  
`[SOURCE_REPRESENTATION_NAME]` | The name of the source representation instance you created in the previous step.  
`[USERNAME]` | The MySQL replication user account on the source database server.  
`[BUCKET]` | The name of the bucket you created to hold the export file.  
`[PATH_TO_DUMP]` | The path to the export file.  
`[SOURCE_SERVER_CA_PATH]` | The local path to where the CA certificate of the source database server is stored. Required only for SSL/TLS.  
`[CLIENT_CERT_PATH]` | The local path to where the client certificate is stored. Required only for [server-client authentication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options).  
`[PRIVATE_KEY_PATH]` | The local path to where the private key file for the client certificate is stored. Required only for [server-client authentication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options).  
`[MACHINE_TYPE]` | The [size](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#settings-2ndgen) of your replica. Generally, the replica is about the same size as the source database server. If you are unsure what machine type to use, start with `db-custom-2-7680`. You can change its size later if needed.  
`[DISK_SIZE]` | The storage size for the replica, in GB. For best performance, create the replica with roughly enough storage to hold the entire import file.  
`[VPC_NETWORK_NAME]` | VPC in the format of: projects/[PROJECT_ID]/global/networks/[NETWORK_NAME]  



###  cURL 

**1\. Create the Cloud SQL[source representation instance](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#config-description)**
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data '{
             "name": "[SOURCE_REPRESENTATION_NAME]",
             "region": "[REGION]",
             "databaseVersion": "[MYSQL_VERSION]",
             "onPremisesConfiguration": {
                 "hostPort": "[SOURCE_SERVER_IP]:[SOURCE_SERVER_PORT]"
             }
         }' \
         -X POST \
         https://www.googleapis.com/sql/v1beta4/projects/[PROJECT-ID]/instances
    

Replace `[PROPERTIES_IN_BRACKETS]` with the following values:

Property | Value  
---|---  
`[SOURCE_REPRESENTATION_NAME]` | The name of the source representation instance. Use any valid Cloud SQL instance name.  
`[REGION]` | The [region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) where you want your Cloud SQL replicas to reside.  
`[MYSQL_VERSION]` | The MySQL version running on your source database server: `MYSQL_5_6` or `MYSQL_5_7`.  
`[SOURCE_SERVER_IP]` | The externally accessible IPv4 address for the source database server.  
`[SOURCE_SERVER_PORT]` | The externally accessible port for the source database server.  
`[PROJECT_ID]` | The project ID for your Google Cloud project.  
  
For example, to create a source representation instance named `hq-primary1`, for a source database server with the IP address of `192.0.2.0` open on port `3306`, and running MySQL 5.7, for Cloud SQL replicas in the `MyProject` project and the `us-central1` region, you would use the following commands:
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data '{
             "name": "hq-primary1",
             "region": "us-central1",
             "databaseVersion": "MYSQL_5_7",
             "onPremisesConfiguration": {
                 "hostPort": "192.0.2.0:3306"
             }
         }' \
         -X POST \
         https://www.googleapis.com/sql/v1beta4/projects/MyProject/instances
    

**2\. Create the Cloud SQL replica**

In this step, you create a Cloud SQL read replica, using the source representation server to represent the source database server, and provide the replica with the data you loaded into Cloud Storage in the previous step.

Because this API call requires you to provide sensitive information, [use a JSON file](https://docs.cloud.google.com/sql/docs/mysql/admin-api#json-file) to provide your data to cURL, rather than providing it on the command line.

Create the data file:
    
    
    {
        "replicaConfiguration": {
            "mysqlReplicaConfiguration": {
                "username": "[USERNAME]",
                "password": "[PASSWORD]",
                "dumpFilePath": "gs://[BUCKET]/[PATH_TO_DUMP]",
                "caCertificate": "[SOURCE_SERVER_CA]",
                "clientCertificate": "[CLIENT_CERT]",
                "clientKey": "[PRIVATE_KEY]"
            }
         },
         "settings": {
             "tier": "[MACHINE_TYPE]",
             "dataDiskSizeGb": "[DISK_SIZE]"
         },
         "masterInstanceName": "[SOURCE_REPRESENTATION_NAME]",
         "region": "[REGION]",
         "databaseVersion": "[MYSQL_VERSION]",
         "name": "[REPLICA_NAME]"
    }
    

If the replica is using a private IP address, also add to settings: "ipConfiguration.privateNetwork" with the value in the format of: "projects/[PROJECT_ID]/global/networks/[NETWORK_NAME]"

Replace `[PROPERTIES_IN_BRACKETS]` with the following values:

Property | Value  
---|---  
`[USERNAME]` | The MySQL replication user account on the source database server.  
`[PASSWORD]` | The password for the MySQL replication user account.  
`[BUCKET]` | The name of the bucket you created to hold the export file.  
`[PATH_TO_DUMP]` | The path to the export file.  
`[SOURCE_SERVER_CA]` | The CA certificate of the source database server. Required only for SSL/TLS. Paste the certificate into the request body.  
`[CLIENT_CERT]` | The client certificate. Required only for [server-client authentication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options). Paste the certificate into the request body.  
`[PRIVATE_KEY]` | The private key file for the client certificate. Required only for [server-client authentication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssl-options). Paste the key into the request body.  
`[MACHINE_TYPE]` | The size of your replica. Generally, the replica is about the same size as the source database server. If you are unsure what machine type to use, start with `db-custom-2-7680`. You can change its size later if needed.  
`[DISK_SIZE]` | The storage size for the replica, in GB. For best performance, create the replica with enough storage to hold the entire import.  
`[SOURCE_REPRESENTATION_NAME]` | The name of the source representation instance you created previously.  
`[REGION]` | The region where you created the source representation instance. The read replicas must be in the same region as the source representation instance.  
`[MYSQL_VERSION]` | The MySQL version running on your source database server: `MYSQL_5_6` or `MYSQL_5_7`.  
`[REPLICA_NAME]` | The name of the Cloud SQL read replica. Use any valid Cloud SQL instance name.  
  
At the command line, call the API:
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data @[PATH_TO_DATA_FILE] \
         -X POST \
         https://www.googleapis.com/sql/v1beta4/projects/[PROJECT-ID]/instances
    

For the source representation instance and bucket we created earlier, the data file, `data.json`, might look like the following example:
    
    
    {
        "replicaConfiguration": {
            "mysqlReplicaConfiguration": {
                "username": "replicationUser",
                "password": "486#@%*@",
                "dumpFilePath": "gs://export-bucket/hq-primary1.sql.gz",
                "caCertificate": "[SOURCE_SERVER_CA]",
                "clientCertificate": "[CLIENT_CERT]",
                "clientKey": "[PRIVATE_KEY]"
            }
        },
        "settings": {
            "tier": "db-custom-4-15360",
            "dataDiskSizeGb": "100"
        },
        "masterInstanceName": "hq-primary1",
        "region": "us-central1",
        "databaseVersion": "MYSQL_5_7",
        "name": "hq-primary1-replica1"
    }
    

And the cURL command would look like this:
    
    
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data @./data.json
         -X POST \
         https://www.googleapis.com/sql/v1beta4/projects/MyProject/instances
    

When the read replica can access the dump file, it begins the import process. The duration of the import process depends on the dump file size, the replica machine type, and the database schema. As a general guide for estimation, expect the replica to import approximately 25-50 GB per hour.

The replica stays in the `PENDING_CREATE` state until the import process is complete; then the replica changes to the `RUNNABLE` state.

**Important:** After the import process completes, the replica uses the binary logs on the source server to catch up to the current state of the source server. The time this step takes depends on the size of your database and your database load. Make sure your binary log retention policy retains binary logs long enough to let the replica copy all the binary logs. A retention policy of a week provides ample time.

### 4\. Configure the source database server to accept connections from the replica

The replica needs to connect to the source database server for replication to succeed. If your source database server is behind a firewall or some other network restriction, you must enable network access for the replica, using the replica's `OUTGOING` IP address. Note that this is _not_ the IP address displayed in the main listing for the replica in the Google Cloud console. You can retrieve the `OUTGOING` IP address by hovering over the **More info** tool tip for the IP address, or by using the `gcloud` command below.

**Important:** You must complete this step within 30 minutes of creating the replica. If you do not, the replica will not be successfully created, and you will need to recreate the replica.

  1. Retrieve the read replica's IP addresses:
         
         gcloud sql instances describe [REPLICA_NAME] --format="default(ipAddresses)"

  2. Configure the network firewall, if necessary, for your source database server to accept connections from the `OUTGOING` IP address. 
  3. Confirm that the replica has successfully connected to the source database server.

     1. The replica's icon in the instance listing page is no longer spinning, and is green.
     2. Go to the Logs Viewer in the Google Cloud console. 

[Go to the Logs Viewer](https://console.cloud.google.com/logs?resource=cloudsql_database)

     3. Select the replica from the **Instance** dropdown. 
     4. Select the `replication-setup.log` log file.

If the replica is not able to connect to the source database server, confirm the following items:

        * Any firewall on the source database server is configured to allow connections from the replica's `OUTGOING` IP address. 
        * Your SSL/TLS configuration is correct. 
        * Your replication user, host, and password are correct. 



### 5\. Restrict access to the MySQL replication user

This step is optional but recommended for security.

The MySQL replication user on the source database server is configured to accept connections from any host (`%`). Update that user account to accept connections only from the replica's `OUTGOING` IP address:
    
    
        UPDATE mysql.user SET Host='[OUTGOING_IP]' WHERE Host='%' AND User='[USERNAME]';
        FLUSH PRIVILEGES;
    

### 6\. Finalize the replica configuration

  1. Configure a user account on the replica.

You can do this by using the Google Cloud console, the gcloud CLI tool, or the Cloud SQL API. However, you cannot use the `mysql` client. For more information about MySQL users, see [MySQL users](https://docs.cloud.google.com/sql/docs/mysql/users).

**To create a user using the Google Cloud console:**

     1. Go to the Cloud SQL Instances page in the Google Cloud console.  
[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances)
     2. Click the instance name to open its **Instance details** page.
     3. Select the **Users** tab.
     4. Click **Create user account**.
     5. In the **Create user account** dialog, specify the details for your user.
     6. Click **Create**.
  2. Authorize access to the replica from any client you plan to use to connect to the replica using public IP addresses.

For instructions, see [Adding an authorized address or address range](https://docs.cloud.google.com/sql/docs/mysql/configure-ip#add). To connect to the replica, you use the replica's `PRIMARY` IP address. This IP address is displayed in the Google Cloud console.

You can otherwise use [any other connection method](https://docs.cloud.google.com/sql/docs/mysql/how-to#connecting) to connect to the replica.




### 7\. Confirm replication status

When the replica finishes importing the dump file, it connects to the on- premises server and applies all the updates that were made after the export was taken.

**It's important to[ check the replication status](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#checking_replication_status) before promoting the replica** to a stand-alone instance. If the replication process is not complete and successful, a promoted replica doesn't have all the changes from your external instance.

### 8\. (Optional) Promote the replica to a stand-alone instance

After checking the replication status, if you want to completely replace ('migrate') the source database server with Cloud SQL, [promote the replica](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica) to become a stand-alone, primary instance. After the replica becomes the primary instance, it is no longer connected to the original source database server.

[ Create a new replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica) for the new primary instance, and restart your connecting applications to point to the new primary instance (for write operations) or the new replica (for read operations).

### 9\. Clean up your storage

  1. Delete the export file:
         
         gcloud storage rm gs://[BUCKET]/[PATH_TO_DUMP]
         

  2. If you no longer need the bucket, delete the bucket: 
         
         gcloud storage rm gs://[BUCKET] --recursive
         




For more information, see the Cloud Storage documentation for [Deleting Objects](https://docs.cloud.google.com/storage/docs/deleting-objects) and [Deleting Buckets](https://docs.cloud.google.com/storage/docs/deleting-buckets).

## Update the configuration

To update the configuration settings later, you can [edit the source representation instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance). If you need to update the [on premises configuration settings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#OnPremisesConfiguration), note that `hostPort` and `type` cannot be updated.

## What's next

  * Learn about [updating an instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance).
  * Learn about [managing replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
