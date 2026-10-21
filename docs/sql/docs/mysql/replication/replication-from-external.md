---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external/
title: Configure Cloud SQL and the external server for replication \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:53:43.936820+00:00
---

# Configure Cloud SQL and the external server for replication  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Configure Cloud SQL and the external server for replication Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to configure your external server for replication to Cloud SQL, create a source representation instance on Cloud SQL, and replicate the data to Cloud SQL. You need to go through all the steps on this page before proceeding to the replication steps.

An alternative to the steps described on this page is the [Database Migration Service](https://docs.cloud.google.com/database-migration/docs), which offers continuous replication or one-time database migration from an external server to Cloud SQL.

## Before you begin

Before configuring replication, review the following prerequisites and terminology.

### Terminology

  * **External server.** The MySQL server external to Cloud SQL that you want to replicate data from. It's also referred to as the source database or the external database server. It can be another Cloud SQL instance or any other database server, such as on-premises or Amazon Relational Database Service (RDS).

  * **Source representation instance.** A mock of a Cloud SQL instance that represents the external server to the Cloud SQL replica. It's visible in the Google Cloud console and appears like a regular Cloud SQL instance, but it doesn't contain data, require configuration or maintenance, or affect billing.

  * **Cloud SQL replica.** The Cloud SQL instance that replicates from the external server. Also known as the external primary read replica.

  * **Replication user account.** The MySQL user account on the external server with sufficient permissions to allow replication between the external server and the Cloud SQL replica.

  * **Managed import.** The process of importing data directly from the external server to the Cloud SQL replica. In this situation, Cloud SQL connects to the external server using the replication user account and runs the data dump directly on the external server to import data to the Cloud SQL replica.




### Set up a Google Cloud project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  8. Make sure you have the Cloud SQL Admin, Storage Admin, and Compute Viewer roles on your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




### Install the Google Cloud SDK

To configure replication, [install Google Cloud SDK](https://docs.cloud.google.com/sdk/install) for your external server. You might want to install the SDK on your external server unless it's already installed elsewhere.

## Set up the external server for replication

### External server checklist

  * Ensure that MySQL 5.7, MySQL 8.0, MySQL 8.4, or MySQL 9.7 is installed on your external server. MySQL Community Edition, Cloud SQL for MySQL, Amazon Aurora, MySQL on Amazon RDS, and Microsoft Azure Database for MySQL Flexible Server are supported.

    * You must use a major version of MySQL on your Cloud SQL replica that is the same as or greater than the version of MySQL running on your external server.
    * If MySQL 5.5 is installed on the external server, then GTID isn't supported.
  * Ensure that [binary logs are enabled](https://dev.mysql.com/doc/refman/8.4/en/binary-log.html) and that:

    * [Row-based binary logging](https://dev.mysql.com/doc/refman/8.4/en/replication-rbr-usage.html) is used.
    * Binary logs are retained for a long enough period to support the database migration. Generally a week is sufficient.
  * Take note of whether your external server has [GTID](https://dev.mysql.com/doc/refman/8.4/en/replication-gtids.html) enabled. This affects the steps you need to take to set up replication.

  * Take note of whether your external server has global read-lock permissions. This affects the steps you need to take to set up replication.

  * If the Cloud SQL replica is enabled with a private IP address because the outgoing private IP address isn't static, configure the external server's firewall to allow the internal IP range allocated for the [private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) of the VPC network that the Cloud SQL replica uses as its private network.

The source database server's firewall must be configured to allow the entire **internal IP range** allocated for the **private service connection** of the VPC network that the Cloud SQL destination instance uses as the **privateNetwork** field of its [**ipConfiguration** settings](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external#setup-replica-instance).

To find the **internal IP range** :

    1. In the Google Cloud console, go to the **VPC networks** page.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

    2. Select the VPC network that you want to use.

    3. Click the **Private service connection** tab.

  * If your external server contains `DEFINER` clauses (views, events, triggers, or stored procedures), depending on the ordering of when these statements are executed, replication might fail. Learn more about [`DEFINER` usage](https://docs.cloud.google.com/sql/docs/mysql/import-export#definer-clause) and potential workarounds in Cloud SQL.

  * InnoDB is the only supported storage engine in Cloud SQL. Migrating with MyISAM might cause data inconsistency and requires data validation. For more information, see [Converting tables from MyISAM to InnoDB](https://dev.mysql.com/doc/refman/8.0/en/converting-tables-to-innodb.html) in MySQL documentation.


**Note:** If you're replicating from Amazon RDS: 

  * Take note that an external server using Amazon RDS doesn't support GTID in most situations, but does support GTID for MySQL 5.7.
  * Take note that an external server using Amazon RDS and Amazon Aurora doesn't support global read-lock permissions.



### Configure binary log retention

You should configure your external server to retain binary logs for at least 24 hours.

###  MySQL Community 

If your external server is using the MySQL Community Edition, you can use these MySQL commands to update your binary log retention settings.

  * MySQL 5.7: [`expire_logs_days`](https://dev.mysql.com/doc/refman/8.4/en/replication-options-binary-log.html#sysvar_expire_logs_days)

  * MySQL 8.0.x: [`expire_logs_days`](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_expire_logs_days), [`binlog_expire_logs_seconds`](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_expire_logs_seconds)

  * MySQL 8.4: [`binlog_expire_logs_seconds`](https://dev.mysql.com/doc/refman/8.4/en/replication-options-binary-log.html#sysvar_binlog_expire_logs_seconds)

  * MySQL 9.7: [`binlog_expire_logs_seconds`](https://dev.mysql.com/doc/refman/9.7/en/replication-options-binary-log.html#sysvar_binlog_expire_logs_seconds)




###  Cloud SQL for MySQL 

If your external server is using Cloud SQL for MySQL, by default, your binary logs are retained for seven days. You can [change this setting](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention).

###  Amazon RDS & Aurora 

If your external server is an Amazon RDS instance, you can use this command to update your binary log retention settings:
    
    
    call mysql.rds_set_configuration('binlog retention ', HOURS);
    

Property | Description  
---|---  
HOURS  | The total number of hours of binary logs for the Amazon RDS instance to retain.  
  
For more information, see [mysql.rds_set_configuration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_set_configuration.html).

###  Microsoft Azure 

By default, binary logging is enabled. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-server-parameters#log_bin_trust_function_creatorsthe).

  1. Set `binlog_expire_logs_seconds` to a period that's long enough to support the database migration.

For more information, see [Configure server parameters in Azure Database for MySQL](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/how-to-configure-server-parameters-portal) and the [`binlog_expire_logs_seconds`](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-server-parameters#binlog_expire_logs_seconds) parameter in the Microsoft documentation.

  2. Restart your server so that the changes you made can take effect.




### Create a replication user account

A MySQL user account dedicated to managing replication to the Cloud SQL replica must exist on your external server. This user account should only be used to manage replication. Depending on the migration approach you use, you might need to grant permissions to the user later.

To add a replication user account, open a terminal on the external server and enter these MySQL commands:

###  MySQL 
    
    
          CREATE USER 'USERNAME'@'%' IDENTIFIED BY 'PASSWORD';
          GRANT SELECT, SHOW VIEW ON *.* TO 'USERNAME'@'HOST';
          FLUSH PRIVILEGES;

###  example 
    
    
    CREATE USER 'replicationUser'@'%' IDENTIFIED BY '8*&fwwd';
    GRANT SELECT, SHOW VIEW ON *.* TO 'replicationUser'@'%';
    FLUSH PRIVILEGES;
    

Property | Description  
---|---  
USERNAME | The replication user account on the external server.  
PASSWORD | The password for the replication user account.  
HOST | Set this to `%` to accept all connections from any host. In a later step, this is changed to only accept connections from the Cloud SQL replica.  
  
## Set up a source representation instance

The source representation instance references the external server. It contains only the request data from the external server. Create the request data and use it in a `curl` command that creates the source representation instance in Cloud SQL.

### Create the request data

The request data contains basic information about your external server in JSON format. The request data can be configured for a Cloud SQL replica on a public or private network and should contain this information.

If you want to migrate a subset of databases from the source representation instance to the destination Cloud SQL instance, then use the `selectedObjects` parameter to specify the database names. If you don't use this parameter or provide an empty list as the value for the parameter, then all databases are migrated from the source to the destination.

###  source.json 
    
    
        {
          "name": "SOURCE_NAME",
          "region": "REGION",
          "databaseVersion": "DATABASE_VERSION",
          "onPremisesConfiguration": {
            "selectedObjects": "SELECTED_OBJECTS",
            "hostPort": "SOURCE_HOST",
            "username": "USERNAME",
            "password": "PASSWORD",
            "caCertificate": "SOURCE_CERT",
            "clientCertificate": "CLIENT_CERT",
            "clientKey": "CLIENT_KEY"
          }
        }

###  managed import example 
    
    
    // example of source.json for external server that
    // - initiates replication from a Cloud SQL managed import
    // - doesn't use SSL/TLS
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "MYSQL_5_7",
      "onPremisesConfiguration": {
        "selectedObjects":[{"database":"db1"}, {"database":"db2"}],
        "hostPort": "192.0.2.0:3306",
        "username": "replicationUser",
        "password": "486#@%*@"
      }
    }
    

###  dump file example 
    
    
    // example of source.json for external server that
    // - initiates replication from a file
    // - uses SSL/TLS
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "MYSQL_5_7",
      "onPremisesConfiguration": {
        "hostPort": "192.0.2.0:3306",
        "selectedObjects":[{"database":"db1"}, {"database":"db3"}],
        "username": "replicationUser",
        "password": "486#@%*@",
        "dumpFilePath": "gs://replica-bucket/source-database.sql.gz",
        "caCertificate": "content of your certificate",
        "clientCertificate": "content of your certificate",
        "clientKey": "content of your client key",
        "sslOption": "REQUIRE"
      }
    }
    

###  custom import example 
    
    
    // example of source.json for external server that
    // - initiates replication from a Cloud SQL custom import
    // - uses SSL/TLS
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "MYSQL_5_7",
      "onPremisesConfiguration": {
        "hostPort": "192.0.2.0:3306",
        "selectedObjects":[{"database":"db1"}, {"database":"db3"}],
        "username": "replicationUser",
        "password": "486#@%*@",
        "sslOption": "REQUIRE"
      }
    }
    

Property | Description  
---|---  
SOURCE_NAME | The name of the source representation instance to create.  
REGION | The [region](https://docs.cloud.google.com/sql/docs/mysql/locations) where you want the source representation instance to reside.  
DATABASE_VERSION | The database version running on your external server. The options are `MYSQL_5_7`, `MYSQL_8_0`, `MYSQL_8_4`, or `MYSQL_9_7`.   
SELECTED_OBJECTS | A comma-separated list of objects, containing the databases that you're migrating from the source representation instance to the destination Cloud SQL instance.  
SOURCE HOST | The IPv4 address and port for the external server, or the DNS address for the external server. If you use a DNS address, then it can contain up to 60 characters. If the external server is hosted on Cloud SQL, then the port is `3306` .  
USERNAME | The replication user account on the external server.  
PASSWORD | The password for the replication user account.  
BUCKET | The name of the bucket that contains the dump file. Include only if you're setting up replication with a dump file that exists in a Cloud Storage bucket.  
DUMP_FILE | A file in the bucket that contains the data from the external server.  
CLIENT_CA_CERT | The CA certificate on the external server. Include only if SSL/TLS is used on the external server.  
CLIENT_CERT | The client certificate on the external server. Required only for [server-client authentication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssltls_configuration). Include only if SSL/TLS is used on the external server.  
CLIENT_KEY | The private key file for the client certificate on the external server. Required only for [server-client authentication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#ssltls_configuration). Include only if SSL/TLS is used on the external server.  
SSL_OPTION | Whether SSL/TLS encryption is used to establish a connection between the source Microsoft Azure database and the destination Cloud SQL database. You can specify the following values for this parameter:

  * `SSL_OPTION_UNSPECIFIED:` the destination database connects to the source database without encryption.
  * `DISABLED:` SSL is deactivated when the replica connects to the source database.
  * `REQUIRE:` SSL is required for the replica to connect to the source database.
  * `VERIFY_CA:` use this parameter to specify whether server-only authentication or server-client authentication is used as part of the SSL/TLS encryption to connect between the source and destination databases. To use server-only authentication, for the `SOURCE_CERT` variable, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the external server's certificate. To use server-client authentication, make the following replacements:
    * `SOURCE_CERT:` provide the certificate of the CA that signed the source database server's certificate 
    * `CLIENT_CERT:` provide the certificate that the destination database uses to authenticate against the source database server
    * `CLIENT_KEY:` provide the private key associated with the client certificate

**Note:** For more information about server-only authentication and server-client authentication, see [Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-source-connection-profile).The default value for this parameter is `SSL_OPTION_UNSPECIFIED`.  
  
### Create a source representation instance

Before you start this step, create a JSON file that contains your source request data.

Then, to create the source representation instance in Cloud SQL, open a terminal and run the following commands:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @JSON_PATH \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances

###  example 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @./source.json \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances

Property | Description  
---|---  
PROJECT_ID | The ID for your project in Google Cloud.  
JSON_PATH | The path to the `JSON` file that contains the request data for the external server.  
  
## Update a source representation instance

If you update the [request data](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#create-source-request) from the external server, you can update the existing source representation instance to use the modified values.

### Modify the request data

Update the request data to include any fields that have changed. This includes the `hostPort`, `username`, `password`, `caCertificate`, `clientCertificate`, and `clientKey` fields. After updating the request data, use it in a `curl` command to update the instance in Cloud SQL.

To update the databases that you want to migrate from the source representation instance, update the list of database names that are associated with the `selectedObjects` parameter. If you don't use this parameter or provide an empty list as the value for the parameter, then all databases are migrated from the source to the destination.

The following example shows updating the `username` and `password` fields with a different username and password:

###  source.json 
    
    
        {
          "name": "SOURCE_NAME",
          "region": "REGION",
          "databaseVersion": "DATABASE_VERSION",
          "onPremisesConfiguration": {
            "selectedObjects": "SELECTED_OBJECTS",
            "username": "NEW_USERNAME",
            "password": "NEW_PASSWORD"
          }
        }

###  managed import example 
    
    
    // example of source.json for external server that
    // - initiates replication from a Cloud SQL managed import
    // - doesn't use SSL/TLS
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "MYSQL_5_7",
      "onPremisesConfiguration": {
        "selectedObjects":[{"database":"db1"}, {"database":"db3"}],
        "username": "newReplicationUser",
        "password": "525#@%*@"
      }
    }
    

###  dump file example 
    
    
    // example of source.json for external server that
    // - initiates replication from a file
    // - uses SSL/TLS
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "MYSQL_5_7",
      "onPremisesConfiguration": {
        "selectedObjects":[{"database":"db1"}, {"database":"db3"}],
        "username": "newReplicationUser",
        "password": "486#@%*@"
      }
    }
    

###  custom import example 
    
    
    // example of source.json for external server that
    // - initiates replication from a Cloud SQL custom import
    // - doesn't use SSL/TLS
    
    {
      "name": "cloudsql-source-instance",
      "region": "us-central1",
      "databaseVersion": "MYSQL_5_7",
      "onPremisesConfiguration": {
        "selectedObjects":[{"database":"db1"}, {"database":"db3"}],
        "username": "newReplicationUser",
        "password": "486#@%*@"
      }
    }
    

Property | Description  
---|---  
SOURCE_NAME | The name of the source representation instance.  
REGION | The [region](https://docs.cloud.google.com/sql/docs/mysql/locations) where the source representation instance resides.  
DATABASE_VERSION | The database version running on your external server. The options are `MYSQL_5_6`, `MYSQL_5_7`, `MYSQL_8_0`, `MYSQL_8_4`, or `MYSQL_9_7`.   
SELECTED_OBJECTS | An updated comma-separated list of objects, containing databases that you're migrating from the source representation instance instance to the destination Cloud SQL instance.  
NEW_USERNAME | The new replication user account on the external server.  
NEW_PASSWORD | The password for the new account.  
  
### Modify a source representation instance

Before you start this step, create a JSON file that contains your modified request data.

Then, to modify the source representation instance in Cloud SQL, open a terminal and run the following commands:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @JSON_PATH \
             -X PATCH \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/SOURCE_NAME

###  example 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @./source.json \
             -X PATCH \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances/cloudsql-source-instance

Property | Description  
---|---  
PROJECT_ID | The ID for your project in Google Cloud.  
JSON_PATH | The path to the `JSON` file that contains the request data for the external server.  
SOURCE_NAME | The name of the source representation instance.  
  
## Set up a Cloud SQL replica

The Cloud SQL replica eventually contains the data from the external server. In this step, you create the request data and use it in a `curl` command that creates the Cloud SQL replica in Cloud SQL.

### Create the request data

The request data contains basic information about your external server and Cloud SQL replica in JSON format. The request data can be configured for a Cloud SQL replica on a public or private network and should contain this information:

###  replica.json 
    
    
        {
            "settings": {
                "tier": "TIER",
                "dataDiskSizeGb": "DISK_SIZE",
                "ipConfiguration": {
                    "ipv4Enabled": "PUBLIC_IP_STATUS",
                    "privateNetwork": "projects/PROJECT_ID/global/networks/NETWORK_NAME"
                 },
                 "availabilityType": "AVAILABILITY_TYPE"
            },
            "masterInstanceName": "SOURCE_REPRESENTATION_INSTANCE_NAME",
            "region": "SOURCE_REGION",
            "databaseVersion": "DATABASE_VERSION",
            "name": "REPLICA_NAME"
        }

###  example 
    
    
        {
            "settings": {
                "tier": "db-custom-4-15360",
                "dataDiskSizeGb": "100"
            },
            "masterInstanceName": "source-instance",
            "region": "us-central1",
            "databaseVersion": "MYSQL_8_0",
            "name": "replica-instance"
        }

Property | Description  
---|---  
TIER | The [type of machine](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#settings-2ndgen) to host your replica instance. If you don't know which machine type to use, start with `db-custom-2-7680`. You can [change its size and other supported values](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#settings-2ndgen) later if needed.  
DISK_SIZE | The storage size for the Cloud SQL replica, in GB.  
PUBLIC_IP_STATUS | Determines whether the instance is assigned a public IP address. By default, the value of this property is `true`. To turn off the assignment of a public IP address for the replica, set the value to `false`. If your project has the [`constraints/sql.restrictPublicIp` organization policy](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy) enabled, then to create the Cloud SQL replica, you must set the value of the `ipv4Enabled` property to `false`. For more information about turning off public IP address assignment, see [Disable public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip#disable-public).  
PROJECT_ID | If the Cloud SQL replica is on a private network, then include the `privateNetwork` property in the `replica.json` file. For PROJECT_ID, specify the ID of your project in Google Cloud.  
NETWORK_NAME | The name of the private network to use with the Cloud SQL replica.  
AVAILABILITY_TYPE | The availability type of the Cloud SQL replica. By default, the value is `ZONAL`. To make the replica HA, set the value to `REGIONAL`. To learn about the allowed values, see [SqlAvailabilityType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#sqlavailabilitytype).   
After you create an external server HA replica, you cannot change it to a non-HA replica. This is true conversely as well. You cannot change an external server non-HA replica to an HA replica.   
Manual failover might lead to unrecoverable migration if attempted when the instance is still loading the initial data, or to temporary downtime if the instance is already replicating from the source. Check the [replication status](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#replication-status).  
SOURCE_REPRESENTATION_INSTANCE_NAME | The name of the source representation instance.  
SOURCE_REGION | The region assigned to the source representation instance.  
DATABASE_VERSION | The database version to use with the Cloud SQL replica. The options for this version are `MYSQL_5_6`, `MYSQL_5_7`, `MYSQL_8_0`, `MYSQL_8_4`, or `MYSQL_9_7`. Match the database version running on your external server, or set the value to no more than one version later.  
REPLICA_NAME | The name of the Cloud SQL replica to create.  
  
### Create the Cloud SQL replica

Before you start this step, create a JSON file that contains your replica request data. Then, to create a Cloud SQL replica, open a Cloud Shell terminal and run these commands:

###  curl 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @JSON_PATH \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances

###  example 
    
    
        gcloud auth login
        ACCESS_TOKEN="$(gcloud auth print-access-token)"
        curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
             --header 'Content-Type: application/json' \
             --data @./replica.json \
             -X POST \
             https://sqladmin.googleapis.com/sql/v1beta4/projects/MyProject/instances

Property | Description  
---|---  
PROJECT_ID | The ID of your project in Google Cloud, which must be the same as that of the source instance.  
JSON_PATH | The path to the `JSON` file that contains the request data for the Cloud SQL replica.  
  
### Verify your setup

To ensure your instances were set up correctly, go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances).

You should see your source representation instance and the Cloud SQL replica, in a listing similar to the following:

Instance ID | Type | Public IP  
---|---|---  
(-) source-representation-instance | Database external primary | 10.68.48.3:3306  
replica-instance | Database read replica | 34.66.48.59  
  
Also make sure that you have the `cloudsql.instances.migrate` permission on the Cloud SQL replica. This permission is included in the `cloudsql.admin` or `cloudsql.editor` [IAM roles](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

### Set the default user password and add other user accounts to the Cloud SQL replica

After you create the Cloud SQL replica, set the password for the default user. You can also add other user accounts to the replica, if required. You can't import database user accounts from the external server, but you can recreate the user accounts on the Cloud SQL replica. Do these activities before you replicate from the external server.

To set the password for the default user, use the [ `gcloud sql users set-password`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/set-password) command as follows.
    
    
    gcloud sql users set-password root \
    --host=% \
    --instance=INSTANCE_NAME \
    --password=PASSWORD

Replace INSTANCE_NAME with the name of the instance and PASSWORD with your selected password before running the command.

To create user accounts on the replica, see [Manage users with built-in authentication](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users). 

### Get the Cloud SQL replica's outgoing IP address

You can use the outgoing IP address of the Cloud SQL replica to create a secure connection between the external server and the Cloud SQL replica. You won't be charged for this IP address.

###  Console 

To get the outgoing IP address for the replica, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Next to the Cloud SQL replica's public IP address, hold the pointer over the **More info** tooltip and retrieve the outgoing IP address.

Note that the outgoing IP address is not the IP address displayed in the main listing for the replica in the Google Cloud console.




###  gcloud 

To get the outgoing IP address for the replica, run the following command:
    
    
    gcloud sql instances describe REPLICA_NAME --format="default(ipAddresses)"
    

Property | Description  
---|---  
REPLICA_NAME | The name of the Cloud SQL replica whose outgoing public IP address you want to retrieve.  
  
### Allow incoming connections on the external server

The Cloud SQL replica needs to connect to the external server for replication to succeed. You must configure the network firewall for your external server to accept connections from the Cloud SQL replica's outgoing IP address if the following conditions apply:

  * The external server is behind a firewall or some other network restriction.
  * Your Cloud SQL replica is using a public IP.



To connect to the Cloud SQL replica, you use the replica's primary IP address. This IP address is displayed in the Google Cloud console.

### Update the source representation instance to allow replication to the Cloud SQL replica

After you set up the source representation instance for the Cloud SQL replica, you might need to [update the source representation instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance). For example, these scenarios require an update to your configurations:

  * The host, port, or IP of the external server changes.
  * You want to use a different MySQL replication user.
  * The password of the MySQL replication user changes.
  * The SSL certificates used to securely connect to the external server change.



## Seed the Cloud SQL replica

There are three options for performing the initial load of data from the external server into the Cloud SQL replica:

  * A managed import uses a service that extracts data from the external server and imports it into the Cloud SQL instance directly. Cloud SQL recommends this option. You must use this option if your external server doesn't use global transaction identifier (GTID) replication. For more information, see [Using a managed import to set up replication from external databases](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external).
  * A dump file requires you to create a dump file of your external server, move it to a Cloud Storage bucket, and import it into Cloud SQL. You can only use this option if your external server uses GTID replication. For more information, see [Using a dump file to set up replication from external databases](https://docs.cloud.google.com/sql/docs/mysql/replication/dump-file-replication-from-external).
  * A custom import requires you to make a Cloud SQL primary instance, perform a custom data import using your preferred tools, demote it to a Cloud SQL replica, and then set up external server replication. This works best for multi-TB database migrations; however, you must use GTID replication. For more information, see [Using a custom import to set up replication from large external databases](https://docs.cloud.google.com/sql/docs/mysql/replication/custom-import-replication-from-external).



### Which option is right for you?

![Cloud SQL user flow diagram](https://docs.cloud.google.com/static/sql/images/choose-replication-option.svg)

## Monitor replication

When the Cloud SQL replica finishes the initial data load, it connects to the external server and applies all updates that were made after the export operation. [Confirm your replication status](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#check_replication_status).

It's important to check the replication status before promoting the replica to a standalone instance. If the replication process isn't successfully completed, a promoted replica doesn't have all the changes from your external server.

If replication delay is not trending toward 0, [take steps to address it](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting#highlag). 

If you want to migrate a subset of databases from the source representation instance to the destination Cloud SQL instance, then check the following per-database metrics:

Metric | Description  
---|---  
`database/mysql/external_sync/replica_lag` | Use this metric to help you decide when to promote the external server replica instance. This metric filters out any databases that aren't selected for migration and reports on replication lag for databases that are selected for migration.  
  
After the Cloud SQL replica has caught up with the external server and there's no replication delay on the Cloud SQL replica, connect to your database. Run the appropriate database commands to make sure that the contents are as expected when compared with the external server. Retain your external server until the necessary validations are done.

### Skip replication errors

During external server replication, you might encounter errors that you might want to skip in order to proceed with replication. To determine whether you've encountered a replication error, run one of the following commands.

For MySQL 8.0.25 and earlier:
    
    
    SHOW SLAVE STATUS;
    

For MySQL 8.0.26 and later:
    
    
    SHOW REPLICA STATUS;
    

You might encounter the following errors during external server replication:

  * Duplicate key errors can occur when you're inserting a row and you're migrating a dataset to Cloud SQL for MySQL from an on-premises database that includes MyISAM tables. In rare cases, there might be a bug with InnoDB.
  * Incompatibilities can occur when you're replicating certain statements from an earlier version of a primary instance to a later version of a replica instance. Normally the assumption is that any MySQL statement on a primary instance that's one major version earlier than the target replica can be replayed by the replica.
  * Incompatibilities can occur when you're migrating from a different MySQL build that has slightly different database support rules. For example:

    * Microsoft Azure MySQL has the statement [`FLUSH FIREWALL RULES`](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/how-to-manage-firewall-portal).
    * MariaDB Server has the statement [`FLUSH USER_STATISTICS`](https://mariadb.com/kb/en/flush/).
    * Percona for MySQL allows DDL to add a `DATETIME` column with a zero epoch default (for example, `1970-01-01 00:00:00`) which is not allowed in MySQL.



One mechanism for skipping errors is to set the [`slave_skip_errors`](https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html#sysvar_slave_skip_errors) or [`replica_skip_errors`](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_replica_skip_errors) configuration flag to skip the most recently encountered error code. To find the most recent error code, query the `LAST_ERROR_NUMBER` column of the [`performance_schema.replication_applier_status_by_worker`](https://dev.mysql.com/doc/refman/8.4/en/performance-schema-replication-applier-status-by-worker-table.html) table. Making this flag change skips all replication errors with the error code or codes in question.

**Warning:** Setting the skip errors flag can mask replication errors that require further investigation. The SQL worker threads will skip over the transactions that are generating errors.

If you encounter a single error, then you can skip the error and resume external server replication to by running the [mysql.skipReplicationError() stored procedure](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures#skipReplicationError) provided by Cloud SQL.

## Set up a cascading replica

After migration, you can create cascading read replicas under your Cloud SQL replica before promoting the Cloud SQL replica.

You can create cascading replicas for your Cloud SQL instance only if you are using [GTID replication](https://docs.cloud.google.com/sql/docs/mysql/replication#introduction). 

To create a cascading replica, run the following commands:

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. For MySQL 5.7 or later, [enable replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#enable_replication).
  3. Click the **Replicas** tab for the replica that will act as a parent for the replica that you want to create.
  4. Click **Create replica**.
  5. On the **Create read replica** page, update the instance ID, and any other configuration options, including the name, region, and zone.
  6. Click **Create**. 

Cloud SQL creates a replica. You're returned to the instance page for the parent replica.

  7. Follow steps 4-6 for each new cascading replica that you want to create.



### gcloud

  1. If you're using MySQL version 5.7 or later, enable binlogs for the primary of the new replica:  

         
         gcloud sql instances patch --enable-bin-log
               --project=cascade-replica PARENT_REPLICA_NAME

Replace PARENT_REPLICA_NAME with the name of the parent replica. 
  2. Create the new replica by specifying your Cloud SQL replica as the primary instance using the [`--master-instance-name`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) flag: 
         
         gcloud sql instances create REPLICA_NAME \
               --master-instance-name=PARENT_REPLICA_NAME \

Replace the following:  

     * REPLICA_NAME: the unique ID for the replica that you are creating
     * PARENT_REPLICA_NAME: the name of the Cloud SQL replica
  3. After the replica is created, you can see that the changes made to the primary instance are replicated through all the replicas in the cascading replicas chain.




### curl

  1. If you are using MySQL version 5.7 or later, enable binary logging:   
  
To enable binary logging, save the following JSON in a file named request.JSON, then invoke the curl command to enable binary logging.   

         
         {
           "settings":
           {
             "backupConfiguration":
             {
               "enabled": false,
               "binaryLogEnabled": true
             }
           }
         }

  2. To create a replica under the parent replica, edit the following JSON code sample and save it to a file called `request.json`: 
         
         {
           "masterInstanceName": "EXTERNAL_SERVER_REPLICA_NAME",
           "project": "PROJECT_ID",
           "name": "REPLICA_NAME",
           "region": "REPLICA_REGION",
           "settings":
             {
               "tier": "MACHINE_TYPE",
             }
         }

  3. Run the following command: 
         
         curl -X POST
         -H "Authorization: Bearer "$(gcloud auth print-access-token)
         -H "Content-Type: application/json; charset=utf-8"
         -d @request.json
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"




## Promote the replica

Promote your replica by following these steps:

  1. [Promote the replica to a primary instance](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica). Note that GTID and binary logs are turned on and the scheduled backups are enabled on the promoted replica.
  2. [Add read replicas to your instance](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica#create-2nd-gen).
  3. Optional: [Configure your instance for high availability (HA)](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-existing). To prevent additional downtime, you can enable HA while [setting up a replica](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-replica-instance) by setting `AVAILABILITY_TYPE` to `REGIONAL`.



## Limitations

  * If you select a database for migration, perform a migration, and later remove the database from the list of selected databases, then the previously migrated database content remains on the destination unless you delete the previously migrated database content explicitly.

  * If you attempt to migrate a specific database that depends on data in another database that isn't being migrated, then your selected database migration can fail. For more information about the errors you might encounter, see [Troubleshoot](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external#troubleshoot).

  * If you're migrating selected databases, then you can't use data definition language (DDL) statements for any routines or events of any database, regardless of any dependencies or whether you're selecting the database for migration.

  * You can't specify selected databases for migration that have literal `_` (underscores (`U+005F`)), `%` (percent symbols (`U+0025`)), or `,` (commas (`U+002C`)) in their database names.




## What's next

  * Learn how to use a [custom import to set up replication from large external databases](https://docs.cloud.google.com/sql/docs/mysql/replication/custom-import-replication-from-external).
  * Learn how to use a [dump file to set up replication from external databases](https://docs.cloud.google.com/sql/docs/mysql/replication/dump-file-replication-from-external).


  * Learn how to use a [managed import to set up replication from external databases](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
