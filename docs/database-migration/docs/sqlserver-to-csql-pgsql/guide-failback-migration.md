---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide-failback-migration/
title: Set up failback replication \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:48.347196+00:00
---

# Set up failback replication  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide-failback-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Set up failback replication Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure a failback migration. In Database Migration Service, failback migrations use a very similar flow to the standard migrations: you configure your source and destination, create the connection profiles, and then run a migration job. The biggest difference is that the failback migration jobs require access to your original migration job and the conversion workspace.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud SQL (See [ Cloud SQL pricing](https://docs.cloud.google.com/sql/pricing).)
  * If used for storing Customer-managed Encryption Keys (CMEK): Cloud Storage (See [ Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).) 



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

## Before you begin

  1. Verify if failback migrations can fully support your scenario, especially the networking limitations and considerations for Write-Ahead Log files. For more information, see [ Failback migrations overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/failback-migration). 
  2. Complete the standard migration scenario with the following exceptions: 
     * After data is migrated, don't promote the migration job. We recommend that you create and test the failback migration job before the promotion step. 
     * Don't delete the conversion workspace or the migration job after you promote the destination instance. 

For more information, see [ SQL Server to Cloud SQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide). 




### Required roles

To get the permissions that you need to perform heterogeneous SQL Server migrations with Database Migration Service, ask your administrator to grant you the required IAM roles on your project:

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to perform heterogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform heterogeneous SQL Server migrations with Database Migration Service: 

  * `datamigration.*`
  * `cloudaicompanion.entitlements.get`

This permission is included in the `roles/datamigration.admin` role. It is required for the [ Gemini-enhanced conversion features](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini). 

  * `cloudsql.instances.create`
  * `cloudsql.instances.get`
  * `cloudsql.instances.list`
  * `cloudsql.instances.update`
  * `cloudsql.instances.delete`
  * `cloudsql.operations.get`
  * `cloudsql.users.list`
  * `cloudsql.users.get`
  * `cloudsql.users.create`
  * `cloudsql.users.update`
  * `cloudsql.users.delete`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Step 1. Prepare your Cloud SQL instance

For failback migrations, your migrated Cloud SQL instance is considered the **source**. This section guides you through the users, permissions, and networking steps.

### Configure users and replication settings

To configure the user account and replication settings for your Cloud SQL for PostgreSQL, do the following:

  1. Decide if you want to re-use the same user account that you configured for the original migration job. You can also create a dedicated migration user specifically for the failback migration job. See [ Create a user account](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) in the Cloud SQL documentation. 
  2. [ Connect to your Cloud SQL instance with the `psql` client](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip), and grant the required permissions to the dedicated migration user account: 
         
         GRANT CREATE ON DATABASE SRC_DB_NAME TO "SRC_USER_ACCOUNT_NAME";
         GRANT CREATE ON SCHEMA SCHEMA_NAME TO "SRC_USER_ACCOUNT_NAME";
         GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "SRC_USER_ACCOUNT_NAME";
         ALTER USER "SRC_USER_ACCOUNT_NAME" WITH REPLICATION;
         
         --If the tables are owned by a different user, grant the same user role to the migration account
         GRANT USER_WHO_OWNS_THE_TABLES" TO "SRC_USER_ACCOUNT_NAME";

  3. Enable logical decoding in your Cloud SQL for PostgreSQL. Set the `cloudsql.logical_decoding` flag to `on`. You have to restart your instance after modifying database flags for the setting to take effect. For more information, see [ Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags) in the Cloud SQL documentation. 
  4. We recommend that you adjust the Write-Ahead Log (WAL) parameters to control the log file size growth and avoid potential database issues. You can configure WAL parameters in Cloud SQL for PostgreSQL instance with database flags. You have to restart your instance after modifying database flags for the setting to take effect. For the exact steps, see [ Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags). 

Use the following flags:

     * `wal_sender_timeout`: This flag controls how long inactive replication connections can stay online before they are terminated. We recommend you configure it to be longer than 10 minutes. You can set this flag to `0` to completely disable connection timeouts. 
     * `max_replication_slots`: Set this flag if you plan to run multiple migration jobs from your Cloud SQL for PostgreSQL instance. Database Migration Service requires one slot per migration job. 
     * `max_wal_senders`: Set this flag if you plan to run multiple migration jobs from your Cloud SQL for PostgreSQL instance. This value should be greater than the number of `max_replication_slots` to account for any other WAL senders in your database. 

For example, if you plan to run 10 migration jobs, and your instance is already using 2 senders, then you should set `max_replication_slots` to at least 12 (10 + 2 = 12). 

  5. Certain WAL parameters can only be modified as PostgreSQL settings and aren't supported by Cloud SQL for PostgreSQL flags. We recommend you also consider adjusting the following variables: 

     * `statement_timeout`: Long-running transactions can cause logical replication slots to hold large amounts of WAL files, increasing the amount of disk space consumed. We recommend you analyze your average query times to find the optimal value that would prevent problematic queries but still allow for legitimate long-running running tasks. Expand the following section for more detailed guidance on who to find average query length in your database. 

#### Guidance: Track average query performance with the `pg_stat_statements` extension

You can use the `pg_stat_statements` extension to track the execution summary of all SQL statements executed on your server. 

       1. Enable the extension and let it monitor your SQL queries. For more information, see [ Enable extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions) in the Cloud SQL for PostgreSQL documentation. 
       2. After you gather enough information, run a query to find the top queries by execution time. You can use this example that fetches the top 5% longest queries: 
              
              SELECT
                  query,
                  calls,
                  total_exec_time / calls as avg_time_ms,
                  max_exec_time as max_time_ms
              FROM pg_stat_statements
              ORDER BY total_exec_time DESC LIMIT 10;

       3. Based on the results, try to plan for an optimal `statement_timeout` value. 

     * `max_slot_wal_keep_size`: Database Migration Service doesn't consume replication slots when you stop the failback migration job. Stopping a migration job for longer periods of time might cause significant WAL file growth, potentially causing instance failure. We recommend that you stop active migration jobs for short periods of time to avoid disruptions. You can use the PostgreSQL `max_slot_wal_keep_size` setting to estimate long replication slots can be stale. To check the value of this setting, use the `SHOW max_slot_wal_keep_size;` command. 




### Configure source connectivity

The source connectivity methods for failback migrations depend on what kind of Cloud SQL for PostgreSQL you used for the original migration. The following table shows an overview for public and private IP networking methods. 

Networking method| Description  
---|---  
Private IP connectivity with Private Service Connect interfaces | The recommended networking method for private IP connectivity. Private Service Connect interfaces don't require an extra proxy Virtual Machine (VM), and they don't consume the [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/vpc-peering#peering-limits).   
Private IP connectivity with VPC peering | VPC Network Peering connectivity is supported only for Private Services Access (PSA) instances. This method connects two Virtual Private Cloud (VPC) networks so that resources in each network can communicate with each other. This approach consumes [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/vpc-peering#peering-limits), and can be useful if you can't create [ network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments) in your project.   
Public IP connectivity | This connectivity method is available if you created your original instance with a Public IP enabled. We generally don't recommend using this approach. In the failback migration scenario, your source database is located in Google Cloud, so private IP connectivity is a simpler and more reliable approach. You can use the public IP connection if there are networking constraints for your scenario.   
  
### Private Service Connect interfaces

To configure private connectivity with Private Service Connect interfaces for failback replication, do the following: 

  1. Check if your source is a Private Service Connect-enabled or a Private Services Access (PSA) instance. Private Service Connect-enabled instances require additional network components to set up Private Service Connect interfaces.

You define the type of private IP configuration for your Cloud SQL database during instance creation. You can't later enable Private IP for an Cloud SQL instance. For more information, see [ Private networking options](https://docs.cloud.google.com/sql/docs/postgres/connection-options#private-networking-type) in Cloud SQL documentation. 

  2. _For Private Service Connect-enabled instances only_ : Create a Private Service Connect endpoint:

     1. Retrieve the information about your instance's service attachment. See [ Get the service attachment](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#get-service-attachment) section in the Cloud SQL documentation. 
     2. Create the Private Service Connect endpoint. See [ Create a Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-psc-endpoint) in the Cloud SQL documentation. 
  3. Create a network attachment in the Virtual Private Cloud where your source resides. Follow these steps: 
     1. In the Google Cloud console, go to the **Network attachments** page. 

[ Go to Network attachments](https://console.cloud.google.com/net-services/psc/list/networkAttachments)

     2. Click **Create network attachment**.
     3. Enter a name for the attachment.
     4. From the **Network** menu, select the VPC where your source resides. 
     5. For the region, use the same region where you plan to create the destination database. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 

     6. From the **Subnetwork** menu, select a subnet where you have at least 6 free usable IP addresses for Database Migration Service (that is, a `/29` range). 
     7. In **Connection preference** select **Accept connections for selected projects**. 

Database Migration Service automatically adds the producer project to the **Accepted projects** list when you later [ create the private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-private-connectivity-configuration#create-psci-config). 

**Caution:** The **Automatically accept connections for all projects** option is less secure because it allows any service to obtain IP addresses from your subnet. We don't recommend using this option. 
     8. Don't add **Accepted projects** or **Rejected projects**.
     9. Click **Create network attachment**.
  4. In Database Migration Service, [ create a private connectivity configuration for Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-private-connectivity-configuration#create-psci-config). 



### VPC Peering

To use VPC peering with your Cloud SQL for PostgreSQL, do the following: 

  1. Check if your source is a Private Service Connect-enabled or a Private Services Access (PSA) instance. Private Service Connect-enabled instances require additional network components to set up Private Service Connect interfaces.

You define the type of private IP configuration for your Cloud SQL database during instance creation. You can't later enable Private IP for an Cloud SQL instance. For more information, see [ Private networking options](https://docs.cloud.google.com/sql/docs/postgres/connection-options#private-networking-type) in Cloud SQL documentation. 

  2. In your project, ensure you have a Virtual Private Cloud network with [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

This is the network that you peer with Database Migration Service and your source database server. You need to have enough space to allocate IP ranges for both components. 

  3. In your Virtual Private Cloud network, create and configure a reverse proxy VM. This reverse proxy machine needs to forward traffic from your VPC directly to the private IP of your Cloud SQL for PostgreSQL instance. For more information, see [ Establish private connectivity using proxies](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-src-connection-reverse-proxy). 
  4. In Database Migration Service, [ create a private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-private-connectivity-configuration) to peer with the VPC network where your Cloud SQL has the private IP assigned. 



### Public IP connectivity

To use public IP connectivity (also referred to as the **IP allowlist** method), make sure the public IP is enabled for your source Cloud SQL for PostgreSQL instance and Database Migration Service public IP ranges are on the list of authorized networks. Do the following: 

  1. Verify the public IP address of your instance. For more information, see [ Configure public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) in the Cloud SQL documentation. 
  2. Add the Database Migration Service public IP addresses to the list of authorized external networks for your instance. See the following pages: 

     * [ Update the authorized external networks for an instance](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks) in the Cloud SQL documentation. 
     * [ List of Database Migration Service public IP addresses](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/ip-allowlists-and-regions). 



### Create source connection profile

For failback migrations, your migrated Cloud SQL for PostgreSQL database is considered the **source**. To create the source connection profile for a failback migration job run one of the following gcloud CLI commands:

### Private Service Connect interfaces

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * SRC_CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile. 
  * SRC_PROFILE_REGION with the identifier of the region where you want to save the connection profile. 
  * SRC_CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console. 
  * SRC_USERNAME with the username for your migration user account. 
  * SRC_DATABASE_NAME with the name of the database you want to migrate. **Note:** If you omit this flag, Database Migration Service defaults to use the same name as the SRC_USER value. 
  * SRC_PASSWORD with the password for your migration user account. 
  * SRC_HOST with the IP address where your source can be reached: 

    * **For Private Service Connect-enabled instances** : Use the IP of the endpoint you  created in the network configuration steps. 
    * **For PSA instances** : Use the private IP of your Cloud SQL for PostgreSQL instance. For more information, see [ View database details](https://docs.cloud.google.com/sql/docs/postgres/instance-info) in the Cloud SQL for PostgreSQL documentation. 
  * SRC_PRIVATE_CONNECTIVITY_CONFIGURATION with the URI of the private connectivity configuration. Use the following format: `projects/{project}/locations/{location}/privateConnections/{private-connectivity-configuration-identifier}`. For more information on how to view details of your private connectivity configurations, see [ View private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-private-connectivity-configs). 
  * (Optional) SSL/TLS encryption flags: If you want to use additional SSL/TLS options with your connection, you need to include extra flags when you create the connection profile. 

To see the flags and include them in the gcloud commands that follow, select the SSL/TLS variant from the drop-down menu. 

Unfiltered viewNone (default)Basic variantTLS variantMutual TLS (mTLS) variant
    * When Database Migration Service establishes a connection with your database, it doesn't send any SSL configuration string. It doesn't present any client certificates to the server, and it also doesn't verify any server certificates. The connection is secure by default, as it travels over private networks. You don't need to add any extra flags. 

    * The request that Database Migration Service sends to your database contains the declaration that the connection is established over a secured channel. Database Migration Service doesn't present any client certificates to the server, and it doesn't validate server certificates when they're presented by your database. 

To use the basic variant, the `--ssl-type=REQUIRED` flag is added to the command.

    * When Database Migration Service connects to your database, it declares that the connection is established over a secured channel. Database Migration Service doesn't present a client certificate to the server, but it does validate the server certificate authority (CA) to make sure that it's connecting to the right host. This prevents person-in-the-middle attacks. 

To use TLS authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed your database server certificate. You can download that certificate from your Cloud SQL instance. For more information, see [ Manage SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#view-ca-certs-content) in the Cloud SQL documentation. 

Replace the following variables: 
      * SERVER_HOSTNAME with your instance hostname, for example `--ssl-flags=server_certificate_hostname=my-server-hostname.com`. 
      * x509_PEM_CERTIFICATE with the raw text of your encoded certificate. **Caution:** You can't edit this variable directly on this page or in the sample commands that follow. Don't paste your certificate in the code sample widget. Instead, make the replacement only as you enter the command in the terminal. 

For example:  
`--ca-certificate="-----BEGIN CERTIFICATE REQUEST-----\n2929ufnskd1394igfhsgj====d123jeksnfaidhs1asde....\n-----END CERTIFICATE REQUEST-----"`

    * When Database Migration Service connects to your database, it declares that the connection is established over a secured channel. Database Migration Service then presents its client certificate to the server, and validates the server certificate authority (CA) to make sure that it's connecting to the right host. 

To use mTLS authentication you need to provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed your database server certificate, client certificate and its private key for Database Migration Service. To acquire these files for Cloud SQL connections, follow these steps: 

      1. Download the x509 PEM-encoded certificate of the CA that signed your database server certificate from from your Cloud SQL instance. For more information, see [ Manage SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#view-ca-certs-content) in the Cloud SQL documentation. 
      2. Create a new client certificate for Database Migration Service in your Cloud SQL instance. For more information, see [ Create a new client certificate](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#client-certs) in the Cloud SQL documentation. 
Replace the following variables: **Caution:** You can't edit some variables directly on this page or in the sample commands that follow. Don't paste your certificate in the code sample widget. Instead, make the replacements only as you enter the command in the terminal. 
      * SERVER_HOSTNAME with your instance hostname, for example `--ssl-flags=server_certificate_hostname=my-server-hostname.com`. 
      * x509_PEM_CERTIFICATE with the raw text of your encoded certificate. 

For example:  
`--ca-certificate="-----BEGIN CERTIFICATE REQUEST-----\n2929ufnskd1394igfhsgj====d123jeksnfaidhs1asde....\n-----END CERTIFICATE REQUEST-----"`

      * CLIENT_CERTIFICATE with the raw text of the Database Migration Service client certificate. 

For example:  
`--client-certificate="-----BEGIN CERTIFICATE REQUEST-----\uuwhfeojdnvaasondfpawsfeafds....\n-----END CERTIFICATE REQUEST-----"`

      * CLIENT_CERTIFICATE_PRIVATE_KEY with the raw text of Database Migration Service client certificate's private key. 

For example:  
`--private-key="-----BEGIN CERTIFICATE REQUEST-----\bgoegfdrthsa0caspkvbnas....\n-----END CERTIFICATE REQUEST-----"`




Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    create postgresql SRC_CONNECTION_PROFILE_ID \
      --no-async
      --display-name=CONNECTION_PROFILE_NAME \
      --region=SRC_REGION \
      --password=SRC_PASSWORD \
      --username=SRC_USER \
      --host=SRC_HOST \
      --port=1433 \
      --database=SRC_DATABASE_NAME \
      --private-connection=SRC_PRIVATE_CONNECTIVITY_CONFIGURATION \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY \
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME \
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT \
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME \
          --ca-certificate="x509_PEM_CERTIFICATE" \
          --client-certificate="CLIENT_CERTIFICATE" \
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --role=SOURCE
    

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create postgresql SRC_CONNECTION_PROFILE_ID `
      --no-async
      --display-name=CONNECTION_PROFILE_NAME `
      --region=SRC_REGION `
      --password=SRC_PASSWORD `
      --username=SRC_USER `
      --host=SRC_HOST `
      --port=1433 `
      --database=SRC_DATABASE_NAME `
      --private-connection=SRC_PRIVATE_CONNECTIVITY_CONFIGURATION \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY `
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME `
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT `
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME `
          --ca-certificate="x509_PEM_CERTIFICATE" `
          --client-certificate="CLIENT_CERTIFICATE" `
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --role=SOURCE
    

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create postgresql SRC_CONNECTION_PROFILE_ID ^
      --no-async
      --display-name=CONNECTION_PROFILE_NAME ^
      --region=SRC_REGION ^
      --password=SRC_PASSWORD ^
      --username=SRC_USER ^
      --host=SRC_HOST ^
      --port=1433 ^
      --database=SRC_DATABASE_NAME ^
      --private-connection=SRC_PRIVATE_CONNECTIVITY_CONFIGURATION \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY ^
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME ^
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT ^
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME ^
          --ca-certificate="x509_PEM_CERTIFICATE" ^
          --client-certificate="CLIENT_CERTIFICATE" ^
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --role=SOURCE
    

You should receive a response similar to the following:
    
    
    Waiting for connection profile [SRC_CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile SRC_CONNECTION_PROFILE_ID [OPERATION_ID]
    

### VPC Peering

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * SRC_CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile. 
  * SRC_PROFILE_REGION with the identifier of the region where you want to save the connection profile. 
  * SRC_CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console. 
  * SRC_USERNAME with the username for your migration user account. 
  * SRC_DATABASE_NAME with the name of the database you want to migrate. **Note:** If you omit this flag, Database Migration Service defaults to use the same name as the SRC_USER value. 
  * SRC_PASSWORD with the password for your migration user account. 
  * SRC_HOST with the IP address of proxy VM you  created in the network configuration steps. 
  * SRC_PRIVATE_CONNECTIVITY_CONFIGURATION with the URI of the private connectivity configuration. Use the following format: `projects/{project}/locations/{location}/privateConnections/{private-connectivity-configuration-identifier}`. For more information on how to view details of your private connectivity configurations, see [ View private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-private-connectivity-configs). 
  * (Optional) SSL/TLS encryption flags: If you want to use additional SSL/TLS options with your connection, you need to include extra flags when you create the connection profile. 

To see the flags and include them in the gcloud commands that follow, select the SSL/TLS variant from the drop-down menu. 

Unfiltered viewNone (default)Basic variantTLS variantMutual TLS (mTLS) variant
    * When Database Migration Service establishes a connection with your database, it doesn't send any SSL configuration string. It doesn't present any client certificates to the server, and it also doesn't verify any server certificates. The connection is secure by default, as it travels over private networks. You don't need to add any extra flags. 

    * The request that Database Migration Service sends to your database contains the declaration that the connection is established over a secured channel. Database Migration Service doesn't present any client certificates to the server, and it doesn't validate server certificates when they're presented by your database. 

To use the basic variant, the `--ssl-type=REQUIRED` flag is added to the command.

    * When Database Migration Service connects to your database, it declares that the connection is established over a secured channel. Database Migration Service doesn't present a client certificate to the server, but it does validate the server certificate authority (CA) to make sure that it's connecting to the right host. This prevents person-in-the-middle attacks. 

To use TLS authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed your database server certificate. You can download that certificate from your Cloud SQL instance. For more information, see [ Manage SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#view-ca-certs-content) in the Cloud SQL documentation. 

Replace the following variables: 
      * SERVER_HOSTNAME with your instance hostname, for example `--ssl-flags=server_certificate_hostname=my-server-hostname.com`. 
      * x509_PEM_CERTIFICATE with the raw text of your encoded certificate. **Caution:** You can't edit this variable directly on this page or in the sample commands that follow. Don't paste your certificate in the code sample widget. Instead, make the replacement only as you enter the command in the terminal. 

For example:  
`--ca-certificate="-----BEGIN CERTIFICATE REQUEST-----\n2929ufnskd1394igfhsgj====d123jeksnfaidhs1asde....\n-----END CERTIFICATE REQUEST-----"`

    * When Database Migration Service connects to your database, it declares that the connection is established over a secured channel. Database Migration Service then presents its client certificate to the server, and validates the server certificate authority (CA) to make sure that it's connecting to the right host. 

To use mTLS authentication you need to provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed your database server certificate, client certificate and its private key for Database Migration Service. To acquire these files for Cloud SQL connections, follow these steps: 

      1. Download the x509 PEM-encoded certificate of the CA that signed your database server certificate from from your Cloud SQL instance. For more information, see [ Manage SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#view-ca-certs-content) in the Cloud SQL documentation. 
      2. Create a new client certificate for Database Migration Service in your Cloud SQL instance. For more information, see [ Create a new client certificate](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#client-certs) in the Cloud SQL documentation. 
Replace the following variables: **Caution:** You can't edit some variables directly on this page or in the sample commands that follow. Don't paste your certificate in the code sample widget. Instead, make the replacements only as you enter the command in the terminal. 
      * SERVER_HOSTNAME with your instance hostname, for example `--ssl-flags=server_certificate_hostname=my-server-hostname.com`. 
      * x509_PEM_CERTIFICATE with the raw text of your encoded certificate. 

For example:  
`--ca-certificate="-----BEGIN CERTIFICATE REQUEST-----\n2929ufnskd1394igfhsgj====d123jeksnfaidhs1asde....\n-----END CERTIFICATE REQUEST-----"`

      * CLIENT_CERTIFICATE with the raw text of the Database Migration Service client certificate. 

For example:  
`--client-certificate="-----BEGIN CERTIFICATE REQUEST-----\uuwhfeojdnvaasondfpawsfeafds....\n-----END CERTIFICATE REQUEST-----"`

      * CLIENT_CERTIFICATE_PRIVATE_KEY with the raw text of Database Migration Service client certificate's private key. 

For example:  
`--private-key="-----BEGIN CERTIFICATE REQUEST-----\bgoegfdrthsa0caspkvbnas....\n-----END CERTIFICATE REQUEST-----"`




Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    create postgresql SRC_CONNECTION_PROFILE_ID \
      --no-async
      --display-name=CONNECTION_PROFILE_NAME \
      --region=SRC_REGION \
      --username=SRC_USER \
      --password=SRC_PASSWORD \
      --host=SRC_HOST \
      --port=1433 \
      --database=SRC_DATABASE_NAME \
      --private-connection=SRC_PRIVATE_CONNECTIVITY_CONFIGURATION \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY \
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME \
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT \
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME \
          --ca-certificate="x509_PEM_CERTIFICATE" \
          --client-certificate="CLIENT_CERTIFICATE" \
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --role=SOURCE
    

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create postgresql SRC_CONNECTION_PROFILE_ID `
      --no-async
      --display-name=CONNECTION_PROFILE_NAME `
      --region=SRC_REGION `
      --username=SRC_USER `
      --password=SRC_PASSWORD `
      --host=SRC_HOST `
      --port=1433 `
      --database=SRC_DATABASE_NAME `
      --private-connection=SRC_PRIVATE_CONNECTIVITY_CONFIGURATION \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY `
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME `
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT `
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME `
          --ca-certificate="x509_PEM_CERTIFICATE" `
          --client-certificate="CLIENT_CERTIFICATE" `
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --role=SOURCE
    

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create postgresql SRC_CONNECTION_PROFILE_ID ^
      --no-async
      --display-name=CONNECTION_PROFILE_NAME ^
      --region=SRC_REGION ^
      --username=SRC_USER ^
      --password=SRC_PASSWORD ^
      --host=SRC_HOST ^
      --port=1433 ^
      --database=SRC_DATABASE_NAME ^
      --private-connection=SRC_PRIVATE_CONNECTIVITY_CONFIGURATION \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY ^
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME ^
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT ^
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME ^
          --ca-certificate="x509_PEM_CERTIFICATE" ^
          --client-certificate="CLIENT_CERTIFICATE" ^
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --role=SOURCE
    

You should receive a response similar to the following:
    
    
    Waiting for connection profile [SRC_CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile SRC_CONNECTION_PROFILE_ID [OPERATION_ID]
    

### Public IP connectivity

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * SRC_CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile. 
  * SRC_PROFILE_REGION with the identifier of the region where you want to save the connection profile. 
  * SRC_CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console. 
  * SRC_USERNAME with the username for your migration user account. 
  * SRC_DATABASE_NAME with the name of the database you want to migrate. **Note:** If you omit this flag, Database Migration Service defaults to use the same name as the SRC_USER value. 
  * SRC_PASSWORD with the password for your migration user account. 
  * SRC_HOST with the public IP of your Cloud SQL for PostgreSQL instance. 
  * (Optional) SSL/TLS encryption flags: If you want to use additional SSL/TLS options with your connection, you need to include extra flags when you create the connection profile. 

To see the flags and include them in the gcloud commands that follow, select the SSL/TLS variant from the drop-down menu. 

Unfiltered viewNone (default)Basic variantTLS variantMutual TLS (mTLS) variant
    * When Database Migration Service establishes a connection with your database, it doesn't send any SSL configuration string. It doesn't present any client certificates to the server, and it also doesn't verify any server certificates. The connection is secure by default, as it travels over private networks. You don't need to add any extra flags. 

    * The request that Database Migration Service sends to your database contains the declaration that the connection is established over a secured channel. Database Migration Service doesn't present any client certificates to the server, and it doesn't validate server certificates when they're presented by your database. 

To use the basic variant, the `--ssl-type=REQUIRED` flag is added to the command.

    * When Database Migration Service connects to your database, it declares that the connection is established over a secured channel. Database Migration Service doesn't present a client certificate to the server, but it does validate the server certificate authority (CA) to make sure that it's connecting to the right host. This prevents person-in-the-middle attacks. 

To use TLS authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed your database server certificate. You can download that certificate from your Cloud SQL instance. For more information, see [ Manage SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#view-ca-certs-content) in the Cloud SQL documentation. 

Replace the following variables: 
      * SERVER_HOSTNAME with your instance hostname, for example `--ssl-flags=server_certificate_hostname=my-server-hostname.com`. 
      * x509_PEM_CERTIFICATE with the raw text of your encoded certificate. **Caution:** You can't edit this variable directly on this page or in the sample commands that follow. Don't paste your certificate in the code sample widget. Instead, make the replacement only as you enter the command in the terminal. 

For example:  
`--ca-certificate="-----BEGIN CERTIFICATE REQUEST-----\n2929ufnskd1394igfhsgj====d123jeksnfaidhs1asde....\n-----END CERTIFICATE REQUEST-----"`

    * When Database Migration Service connects to your database, it declares that the connection is established over a secured channel. Database Migration Service then presents its client certificate to the server, and validates the server certificate authority (CA) to make sure that it's connecting to the right host. 

To use mTLS authentication you need to provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed your database server certificate, client certificate and its private key for Database Migration Service. To acquire these files for Cloud SQL connections, follow these steps: 

      1. Download the x509 PEM-encoded certificate of the CA that signed your database server certificate from from your Cloud SQL instance. For more information, see [ Manage SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#view-ca-certs-content) in the Cloud SQL documentation. 
      2. Create a new client certificate for Database Migration Service in your Cloud SQL instance. For more information, see [ Create a new client certificate](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#client-certs) in the Cloud SQL documentation. 
Replace the following variables: **Caution:** You can't edit some variables directly on this page or in the sample commands that follow. Don't paste your certificate in the code sample widget. Instead, make the replacements only as you enter the command in the terminal. 
      * SERVER_HOSTNAME with your instance hostname, for example `--ssl-flags=server_certificate_hostname=my-server-hostname.com`. 
      * x509_PEM_CERTIFICATE with the raw text of your encoded certificate. 

For example:  
`--ca-certificate="-----BEGIN CERTIFICATE REQUEST-----\n2929ufnskd1394igfhsgj====d123jeksnfaidhs1asde....\n-----END CERTIFICATE REQUEST-----"`

      * CLIENT_CERTIFICATE with the raw text of the Database Migration Service client certificate. 

For example:  
`--client-certificate="-----BEGIN CERTIFICATE REQUEST-----\uuwhfeojdnvaasondfpawsfeafds....\n-----END CERTIFICATE REQUEST-----"`

      * CLIENT_CERTIFICATE_PRIVATE_KEY with the raw text of Database Migration Service client certificate's private key. 

For example:  
`--private-key="-----BEGIN CERTIFICATE REQUEST-----\bgoegfdrthsa0caspkvbnas....\n-----END CERTIFICATE REQUEST-----"`




Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    create postgresql SRC_CONNECTION_PROFILE_ID \
      --no-async
      --display-name=CONNECTION_PROFILE_NAME \
      --region=SRC_REGION \
      --password=SRC_PASSWORD \
      --username=SRC_USER \
      --host=SRC_HOST \
      --port=1433 \
      --database=SRC_DATABASE_NAME \
      --role=SOURCE \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY \
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME \
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT \
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME \
          --ca-certificate="x509_PEM_CERTIFICATE" \
          --client-certificate="CLIENT_CERTIFICATE" \
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --static-ip-connectivity
    

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create postgresql SRC_CONNECTION_PROFILE_ID `
      --no-async
      --display-name=CONNECTION_PROFILE_NAME `
      --region=SRC_REGION `
      --password=SRC_PASSWORD `
      --username=SRC_USER `
      --host=SRC_HOST `
      --port=1433 `
      --database=SRC_DATABASE_NAME `
      --role=SOURCE \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY `
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME `
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT `
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME `
          --ca-certificate="x509_PEM_CERTIFICATE" `
          --client-certificate="CLIENT_CERTIFICATE" `
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --static-ip-connectivity
    

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create postgresql SRC_CONNECTION_PROFILE_ID ^
      --no-async
      --display-name=CONNECTION_PROFILE_NAME ^
      --region=SRC_REGION ^
      --password=SRC_PASSWORD ^
      --username=SRC_USER ^
      --host=SRC_HOST ^
      --port=1433 ^
      --database=SRC_DATABASE_NAME ^
      --role=SOURCE \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY ^
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME ^
          --ca-certificate="x509_PEM_CERTIFICATE" \
        *   --ssl-type=SERVER_CLIENT ^
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME ^
          --ca-certificate="x509_PEM_CERTIFICATE" ^
          --client-certificate="CLIENT_CERTIFICATE" ^
          --private-key="CLIENT_CERTIFICATE_PRIVATE_KEY" \
    
      --static-ip-connectivity
    

You should receive a response similar to the following:
    
    
    Waiting for connection profile [SRC_CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile SRC_CONNECTION_PROFILE_ID [OPERATION_ID]
    

## Step 2. Prepare your destination (the original source instance)

To prepare your SQL Server instance for failback replication, you need to configure connectivity, user permissions, and replication settings. In failback migrations, your original source SQL Server instance is considered the **destination**.

### Configure users and replication settings

The migration user for the failback job requires the `db_owner` role. If you want to use the same migration user account you configured for the standard migration job, you also need to remove the `db_denydatawriter` role from that account. (The `db_denydatawriter` role is required for the standard migration job. For more information, see [ Configure source database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-source-database).)

For detailed steps, select the tab relevant for your original source database offering:

### Cloud SQL for SQL Server

To configure failback replication to your original Cloud SQL for SQL Server source, do the following: 

  1. Decide if you want to re-use the same user account that you configured for the original migration job. You can also create a dedicated migration user specifically for the failback migration job. See [ Create a user](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users#creating) in the Cloud SQL documentation. 
  2. Connect to your Cloud SQL instance with a SQL client. You can use the following methods: 
     * [ `sqlcmd` client](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip). You can use this method to connect to your instance private IP, but it might require that you create a Compute Engine virtual machine. 
     * [ `gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect) command. This command works only for Cloud SQL instances that have a public IP address enabled. 
  3. Assign the `db_owner` roles to the migration user account. Run the following command: 
         
         EXEC sp_addrolemember 'db_owner', 'USER_NAME';
         --If you re-use the migration user account, also remove the `db_denydatawriter` role
         EXEC sp_removerolemember 'db_denydatawriter', 'USER_NAME';

  4. Alter your triggers with the `NOT FOR REPLICATION` option. To avoid data integrity violations, you need to prevent your triggers from firing during the replication process. Do the following: 

     1. Query your database for all triggers that don't use the `NOT FOR REPLICATION` setting: 
            
            SELECT
                s.name AS [Schema],
                t.name AS [Table],
                tr.name AS [TriggerName]
            FROM sys.triggers tr
            INNER JOIN sys.tables t ON tr.parent_id = t.object_id
            INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE tr.is_not_for_replication = 0;

     2. Alter every trigger with the `NOT FOR REPLICATION` option: 
            
            ALTER TRIGGER TRIGGER_NAME
            ON TABLE_NAME
            AFTER INSERT
            NOT FOR REPLICATION
            AS
            BEGIN
                YOUR_ORIGINAL_TRIGGER_BODY
            END;

  5. Disable foreign key constraints for replication. Drop the keys and then re-create them, altering the constraints with the `NOT FOR REPLICATION` option. For an example command, see the [ Disable foreign key constraints for replication](https://learn.microsoft.com/en-us/sql/relational-databases/tables/disable-foreign-key-constraints-for-replication) page in the Microsoft documentation. 

  6. Disable lock escalation for each replicated table. This operation is required to avoid deadlocks when changes are applied to SQL Server tables in parallel. 

To disable lock escalation at the instance level, run the following command: 
         
         DBCC TRACEON (1211, -1);

You can enable the setting after you promote the failback migration job.




### Self-hosted SQL Server

To configure failback replication to your original self-hosted SQL Server source, do the following: 

  1. Connect to your source instance with a SQL client, for example the [ `sqlcmd`](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility) utility. 
  2. Decide if you want to re-use the same user account that you configured for the original migration job. You can also create a dedicated migration user specifically for the failback migration job: 
         
         USE master;
         CREATE LOGIN YOUR_LOGIN WITH PASSWORD = 'PASSWORD';
         CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;

  3. Assign the `db_owner` roles to the migration user account. Run the following command: 
         
         EXEC sp_addrolemember 'db_owner', 'USER_NAME';
         # If you re-use the migration user account, also remove the `db_denydatawriter` role
         EXEC sp_removerolemember 'db_denydatawriter', 'USER_NAME';

  4. Alter your triggers with the `NOT FOR REPLICATION` option. To avoid data integrity violations, you need to prevent your triggers from firing during the replication process. Do the following: 

     1. Query your database for all triggers that don't use the `NOT FOR REPLICATION` setting: 
            
            SELECT
                s.name AS [Schema],
                t.name AS [Table],
                tr.name AS [TriggerName]
            FROM sys.triggers tr
            INNER JOIN sys.tables t ON tr.parent_id = t.object_id
            INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE tr.is_not_for_replication = 0;

     2. Alter every trigger with the `NOT FOR REPLICATION` option: 
            
            ALTER TRIGGER TRIGGER_NAME
            ON TABLE_NAME
            AFTER INSERT
            NOT FOR REPLICATION
            AS
            BEGIN
                YOUR_ORIGINAL_TRIGGER_BODY
            END;

  5. Disable foreign key constraints for replication. Drop the keys and then re-create them, altering the constraints with the `NOT FOR REPLICATION` option. For an example command, see the [ Disable foreign key constraints for replication](https://learn.microsoft.com/en-us/sql/relational-databases/tables/disable-foreign-key-constraints-for-replication) page in the Microsoft documentation. 

  6. Disable lock escalation for each replicated table. This operation is required to avoid deadlocks when changes are applied to SQL Server tables in parallel. 

To disable lock escalation at the instance level, run the following command: 
         
         DBCC TRACEON (1211, -1);

You can enable the setting after you promote the failback migration job.




### Amazon RDS for SQL Server

To configure failback replication to your original Amazon RDS for SQL Server source, do the following: 

  1. Connect to your source instance with a SQL client. See [ Connecting to a DB instance running the Microsoft SQL Server database engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.html) in Amazon RDS documentation. 
  2. Decide if you want to re-use the same user account that you configured for the original migration job. You can also create a dedicated migration user specifically for the failback migration job: 
         
         USE master;
         CREATE LOGIN YOUR_LOGIN WITH PASSWORD = 'PASSWORD';
         CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;

  3. Assign the `db_owner` roles to the migration user account. Run the following command: 
         
         EXEC sp_addrolemember 'db_owner', 'USER_NAME';
         # If you re-use the migration user account, also remove the `db_denydatawriter` role
         EXEC sp_removerolemember 'db_denydatawriter', 'USER_NAME';

  4. Alter your triggers with the `NOT FOR REPLICATION` option. To avoid data integrity violations, you need to prevent your triggers from firing during the replication process. Do the following: 

     1. Query your database for all triggers that don't use the `NOT FOR REPLICATION` setting: 
            
            SELECT
                s.name AS [Schema],
                t.name AS [Table],
                tr.name AS [TriggerName]
            FROM sys.triggers tr
            INNER JOIN sys.tables t ON tr.parent_id = t.object_id
            INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE tr.is_not_for_replication = 0;

     2. Alter every trigger with the `NOT FOR REPLICATION` option: 
            
            ALTER TRIGGER TRIGGER_NAME
            ON TABLE_NAME
            AFTER INSERT
            NOT FOR REPLICATION
            AS
            BEGIN
                YOUR_ORIGINAL_TRIGGER_BODY
            END;

  5. Disable foreign key constraints for replication. Drop the keys and then re-create them, altering the constraints with the `NOT FOR REPLICATION` option. For an example command, see the [ Disable foreign key constraints for replication](https://learn.microsoft.com/en-us/sql/relational-databases/tables/disable-foreign-key-constraints-for-replication) page in the Microsoft documentation. 

  6. Disable lock escalation for each replicated table. This operation is required to avoid deadlocks when changes are applied to SQL Server tables in parallel. 

To disable lock escalation at the instance level, run the following command: 
         
         DBCC TRACEON (1211, -1);

You can enable the setting after you promote the failback migration job.




### Microsoft Azure SQL Managed Instance

To configure failback replication to your original Microsoft Azure SQL Managed Instance source, do the following: 

  1. Connect to your source instance with a SQL client, for example the [ `sqlcmd`](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility) utility, [ Azure Data Studio](https://learn.microsoft.com/en-us/azure-data-studio/connect), or [ SQL Server Management Studio](https://learn.microsoft.com/en-us/azure-data-studio/connect). 
  2. Decide if you want to re-use the same user account that you configured for the original migration job. You can also create a dedicated migration user specifically for the failback migration job: 
         
         USE master;
         CREATE LOGIN YOUR_LOGIN WITH PASSWORD = 'PASSWORD';
         CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;

  3. Assign the `db_owner` roles to the migration user account. Run the following command: 
         
         EXEC sp_addrolemember 'db_owner', 'USER_NAME';
         # If you re-use the migration user account, also remove the `db_denydatawriter` role
         EXEC sp_removerolemember 'db_denydatawriter', 'USER_NAME';

  4. Alter your triggers with the `NOT FOR REPLICATION` option. To avoid data integrity violations, you need to prevent your triggers from firing during the replication process. Do the following: 

     1. Query your database for all triggers that don't use the `NOT FOR REPLICATION` setting: 
            
            SELECT
                s.name AS [Schema],
                t.name AS [Table],
                tr.name AS [TriggerName]
            FROM sys.triggers tr
            INNER JOIN sys.tables t ON tr.parent_id = t.object_id
            INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE tr.is_not_for_replication = 0;

     2. Alter every trigger with the `NOT FOR REPLICATION` option: 
            
            ALTER TRIGGER TRIGGER_NAME
            ON TABLE_NAME
            AFTER INSERT
            NOT FOR REPLICATION
            AS
            BEGIN
                YOUR_ORIGINAL_TRIGGER_BODY
            END;

  5. Disable foreign key constraints for replication. Drop the keys and then re-create them, altering the constraints with the `NOT FOR REPLICATION` option. For an example command, see the [ Disable foreign key constraints for replication](https://learn.microsoft.com/en-us/sql/relational-databases/tables/disable-foreign-key-constraints-for-replication) page in the Microsoft documentation. 

  6. Disable lock escalation for each replicated table. This operation is required to avoid deadlocks when changes are applied to SQL Server tables in parallel. 

To disable lock escalation at the instance level, run the following command: 
         
         DBCC TRACEON (1211, -1);

You can enable the setting after you promote the failback migration job.




### Configure destination connectivity

Failback migration jobs support only Private Service Connect interfaces for connecting to your original SQL Server instance. Depending on your database type, this connectivity method might require additional network components.

#### For PSC-enabled Cloud SQL

For PSC-enabled Cloud SQL for SQL Server instances, there are no additional steps required to prepare your instance network connectivity for failback replication. At a later stage, when you  create the destination connection profile, you need to provide the the URI of the service attachment created for your instance.

You can check this URI on the instance details page. For more information, see [ View instance summary information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info) in the Cloud SQL documentation.

#### For self-hosted, Amazon RDS, and Microsoft Azure SQL Managed Instance

For non-PSC-enabled Cloud SQL for SQL Server, self-hosted SQL Server, Amazon RDS for SQL Server, and Microsoft Azure SQL Managed Instance instances, you need to create a Private Service Connect producer setup with a proxy VM and a service attachment. If one bastion virtual machine (VM) is not sufficient for your networking needs, configure an _instance group_ for your network producer setup. For more information, see [ Network connectivity in managed services](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-managed-services).

To configure the required networking setup, do the following:

  1. Set up direct connectivity between the instance and your Virtual Private Cloud. You need a private IP in the Virtual Private Cloud that can represent the connection to your destination instance. This is the address where the proxy VM is going to forward traffic. 

Depending on your network architecture, you might need to configure additional Cloud VPN gateways in your system. For more information, see the following pages in the Cloud VPN documentation: 

     * For self-hosted instances, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws)
     * For Amazon RDS for SQL Server instances, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws)
     * For Microsoft Azure SQL Managed Instance instances, see [ Create HA VPN connections between Google Cloud and Azure](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-azure)
  2. Create required Private Service Connect setup and the service attachment. We recommend that you use the Google Cloud CLI automation script. Expand the following section for full details. 

#### Create a Private Service Connect producer setup with a DANTE proxy VM

Before using any of the command data, make the following replacements:

     * PROJECT_ID with the project in which you create the Private Service Connect producer setup. 
     * REGION with the region in which you create the Private Service Connect producer setup.
     * ZONE with the zone within REGION in which you create all of the zonal resources (for example, the bastion VM). 
     * BASTION with a name for your bastion VM. 
     * DB_SUBNETWORK with the subnetwork to which the traffic will be forwarded. The subnetwork needs to have access to your destination database. 
     * DB_SUBNETWORK_GATEWAY with the IPv4 gateway of the subnetwork. 
     * PORT with the port that the bastion will use to expose the underlying database. 
     * DESTINATION_SQL_INSTANCE_PRIVATE_IP with the private IP address where your destination can be reached. 
       * For non-PSC-enabled Cloud SQL for SQL Server destinations, use the private IP of your instance. 
       * For destinations hosted outside Google Cloud, use the private IP of the connection that exposes your databases in the Google Cloud network. For example, that could be the IP address of the Cloud VPN you configured in the previous step. 

The following bash script uses Google Cloud CLI to create the Private Service Connect producer setup for the destination database. Note that some defaults might need to be adjusted; for example, the Private Service Connect subnet [ CIDR ranges](https://docs.cloud.google.com/vpc/docs/alias-ip#subnet_primary_and_secondary_cidr_ranges). 
    
    #!/bin/bash
    
    # Create the VPC network for the Database Migration Service Private Service Connect.
    gcloud compute networks create dms-psc-vpc \
    --project=PROJECT_ID \
    --subnet-mode=custom
    
    # Create a subnet for the Database Migration Service Private Service Connect.
    gcloud compute networks subnets create dms-psc-REGION \
    --project=PROJECT_ID \
    --range=10.0.0.0/16 --network=dms-psc-vpc \
    --region=REGION
    
    # Create a router required for the bastion to be able to install external
    # packages (for example, Dante SOCKS server):
    gcloud compute routers create ex-router-REGION \
    --network dms-psc-vpc \
    --project=PROJECT_ID \
    --region=REGION
    
    gcloud compute routers nats create ex-nat-REGION \
    --router=ex-router-REGION \
    --auto-allocate-nat-external-ips \
    --nat-all-subnet-ip-ranges \
    --enable-logging \
    --project=PROJECT_ID \
    --region=REGION
    
    # Create the bastion VM.
    gcloud compute instances create BASTION \
        --project=PROJECT_ID \
        --zone=ZONE \
        --image-family=debian-11 \
        --image-project=debian-cloud \
        --network-interface subnet=dms-psc-REGION,no-address \
        --network-interface subnet=DB_SUBNETWORK,no-address \
        --metadata=startup-script='#!/bin/bash
    
    # Route the private IP address using the gateway of the database subnetwork.
    # To find the gateway for the relevant subnetwork go to the VPC network page
    # in the Google Cloud console. Click VPC networks and select the database VPC
    # to see the details.
    ip route add DESTINATION_SQL_INSTANCE_PRIVATE_IP via DB_SUBNETWORK_GATEWAY
    
    # Install Dante SOCKS server.
    apt-get install -y dante-server
    
    # Create the Dante configuration file.
    touch /etc/danted.conf
    
    # Create a proxy.log file.
    touch proxy.log
    
    # Add the following configuration for Dante:
    cat > /etc/danted.conf << EOF
    logoutput: /proxy.log
    user.privileged: proxy
    user.unprivileged: nobody
    
    internal: 0.0.0.0 port = PORT
    external: ens5
    
    clientmethod: none
    socksmethod: none
    
    client pass {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error disconnect
    }
    client block {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error
    }
    socks pass {
            from: 0.0.0.0/0
            to: DESTINATION_SQL_INSTANCE_PRIVATE_IP/32
            protocol: tcp
            log: connect error disconnect
    }
    socks block {
            from: 0.0.0.0/0
            to: 0.0.0.0/0
            log: connect error
    }
    EOF
    
    # Start the Dante server.
    systemctl restart danted
    
    tail -f proxy.log'
    
    # Create the target instance from the created bastion VM.
    gcloud compute target-instances create bastion-ti-REGION \
    --instance=BASTION \
    --project=PROJECT_ID \
    --instance-zone=ZONE \
    --network=dms-psc-vpc
    
    # Create a forwarding rule for the backend service.
    gcloud compute forwarding-rules create dms-psc-forwarder-REGION \
    --project=PROJECT_ID \
    --region=REGION \
    --load-balancing-scheme=internal \
    --network=dms-psc-vpc \
    --subnet=dms-psc-REGION \
    --ip-protocol=TCP \
    --ports=all \
    --target-instance=bastion-ti-REGION \
    --target-instance-zone=ZONE
    
    # Create a TCP NAT subnet.
    gcloud compute networks subnets create dms-psc-nat-REGION-tcp \
    --network=dms-psc-vpc \
    --project=PROJECT_ID \
    --region=REGION \
    --range=10.1.0.0/16 \
    --purpose=private-service-connect
    
    # Create a service attachment.
    gcloud compute service-attachments create dms-psc-svc-att-REGION \
    --project=PROJECT_ID \
    --region=REGION \
    --producer-forwarding-rule=dms-psc-forwarder-REGION \
    --connection-preference=ACCEPT_MANUAL \
    --nat-subnets=dms-psc-nat-REGION-tcp
    
    # Create a firewall rule allowing the Private Service Connect NAT subnet.
    # access the Private Service Connect subnet
    gcloud compute \
    --project=PROJECT_ID firewall-rules create dms-allow-psc-tcp \
    --direction=INGRESS \
    --priority=1000 \
    --network=dms-psc-vpc \
    --action=ALLOW \
    --rules=all \
    --source-ranges=10.1.0.0/16 \
    --enable-logging
    
    # Print out the created service attachment.
    gcloud compute service-attachments describe dms-psc-svc-att-REGION \
    --project=PROJECT_ID \
    --region=REGION

  3. Optional: Consider if you want to use additional SSL/TLS certificates to secure the destination network connection. 

     * For **Source** connections (that is, connections to your _original Cloud SQL destination_), can only use the **REQUIRED** SSL/TLS variant. Failback migration jobs don't support the Cloud SQL Auth Proxy 
     * **Destination** connections are carried out safely over private networks, but you can also use additional certificates. Database Migration Service supports the same SSL/TLS variants for failback destinations as it does for source connections with standard migration jobs. For more information on how to prepare SSL/TLS certificates, use the same steps as described on the [ Configure encryption](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/encrypt-source-connections). 

If you create and configure the SSL/TLS certificates, you later need to provide the encryption keys in the destination connection profile. 




### Create destination connection profile

For failback migrations, your original source SQL Server instance is considered the **destination**.

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * DEST_CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile. 
  * DEST_PROFILE_REGION with the identifier of the region where you want to save the connection profile. 
  * DEST_CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console. 
  * DEST_USERNAME with the username for your migration user account. 
  * DEST_PASSWORD with the password for your migration user account. 
  * DATABASE with the name of your migrated database that you want to replicate back to the original source. 
  * DEST_HOST with the value relevant for your original source database provider. 

    * For PSC-enabled Cloud SQL instances, use the DNS name field.
    * For non-PSC-enabled Cloud SQL instances, self-hosted SQL Server, Amazon RDS for SQL Server, and Microsoft Azure instances, use the private IP of the instance. This is the IP address where you forward traffic with the proxy you configured in the connectivity section.
  * SERVICE_ATTACHMENT_URI with the identifier for the service attachment in your Private Service Connect setup. 

    * For PSC-enabled Cloud SQL instances, you can check the service attachment URI on the instance details page. For more information, see [ View instance summary information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info) in the Cloud SQL documentation. 
    * For non-PSC-enabled Cloud SQL, self-hosted SQL Server, Amazon RDS for SQL Server, or Microsoft Azure SQL Managed Instance instances, use URI of the service attachment you created in the connectivity section. 

To view details of the service attachment you created, you can use the `gcloud compute service-attachments describe dms-psc-svc-att-REGION` command. 

  * (Optional) SSL/TLS encryption flags: If you want to use additional SSL/TLS options with the destination connection, you need to include extra flags when you create the connection profile. 

To see the flags and include them in the gcloud commands that follow, select the SSL/TLS variant from the drop-down menu. 

Unfiltered viewNone (default)Basic variantTLS variant
    * When Database Migration Service establishes a connection with your database, it doesn't send any SSL configuration string. It doesn't present any client certificates to the server, and it also doesn't verify any server certificates. The connection is secure by default, as it travels over private networks. You don't need to add any extra flags. 

    * The request that Database Migration Service sends to your database contains the declaration that the connection is established over a secured channel. Database Migration Service doesn't present any client certificates to the server, and it doesn't validate server certificates when they're presented by your database. 

To use the basic variant, the `--ssl-type=REQUIRED` flag is added to the command.

    * When Database Migration Service connects to your database, it declares that the connection is established over a secured channel. Database Migration Service doesn't present a client certificate to the server, but it does validate the server certificate authority (CA) to make sure that it's connecting to the right host. This prevents person-in-the-middle attacks. 

To use TLS authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed your database server certificate. Replace the following variables: 

      * SERVER_HOSTNAME with your instance hostname, for example `--ssl-flags=server_certificate_hostname=my-server-hostname.com`. 
      * x509_PEM_CERTIFICATE with the raw text of your encoded certificate. **Caution:** You can't edit this variable directly on this page or in the sample commands that follow. Don't paste your certificate in the code sample widget. Instead, make the replacement only as you enter the command in the terminal. 

For example:  
`--ca-certificate="-----BEGIN CERTIFICATE REQUEST-----\n2929ufnskd1394igfhsgj====d123jeksnfaidhs1asde....\n-----END CERTIFICATE REQUEST-----"`




Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles \
    create sqlserver DEST_CONNECTION_PROFILE_ID \
      --no-async \
      --display-name=DEST_CONNECTION_PROFILE_NAME \
      --region=DEST_PROFILE_REGION \
      --password=DEST_PASSWORD \
      --username=DEST_USER \
      --database=DATABASE \
      --host=DEST_HOST \
      --port=1433 \
      --psc-service-attachment=SERVICE_ATTACHMENT_URI \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY \
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME \
          --ca-certificate="x509_PEM_CERTIFICATE" \
    
      --role=DESTINATION
    

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create sqlserver DEST_CONNECTION_PROFILE_ID `
      --no-async `
      --display-name=DEST_CONNECTION_PROFILE_NAME `
      --region=DEST_PROFILE_REGION `
      --password=DEST_PASSWORD `
      --username=DEST_USER `
      --database=DATABASE `
      --host=DEST_HOST `
      --port=1433 `
      --psc-service-attachment=SERVICE_ATTACHMENT_URI \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY `
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME `
          --ca-certificate="x509_PEM_CERTIFICATE" \
    
      --role=DESTINATION
    

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create sqlserver DEST_CONNECTION_PROFILE_ID ^
      --no-async ^
      --display-name=DEST_CONNECTION_PROFILE_NAME ^
      --region=DEST_PROFILE_REGION ^
      --password=DEST_PASSWORD ^
      --username=DEST_USER ^
      --database=DATABASE ^
      --host=DEST_HOST ^
      --port=1433 ^
      --psc-service-attachment=SERVICE_ATTACHMENT_URI \
      
        *   *   --ssl-type=REQUIRED \
        *   --ssl-type=SERVER_ONLY ^
          --ssl-flags=server_certificate_hostname=SERVER_HOSTNAME ^
          --ca-certificate="x509_PEM_CERTIFICATE" \
    
      --role=DESTINATION
    

You should receive a response similar to the following:
    
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

## Step 3. Create and start the failback migration job

Failback migration jobs need access to your original migration job. To create the failback migration job, do the following:

  1. Create the migration job. Run the following command (click the link to expand):

#### `gcloud database-migration migration-jobs create`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.
     * REGION with the region identifier where you want to save the migration job.
     * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
     * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile.
     * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
     * ORIGINAL_MIGRATION_JOB_ID with the identifier of your original migration job. 
     * MAX_CONCURRENT_CONNECTIONS with the number of maximum concurrent connections that Database Migration Service can establish to your destination instance. The default value for this parameter is `128`. Allowed values: minimum `2`, maximum `256`. 

Database Migration Service adjusts the number of connections to ensure the best performance within provided connection limit. Increasing the maximum connection limit can improve the migration speed, but introduces additional load on your destination databases. 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs create MIGRATION_JOB_ID \
      --no-async
      --display-name=MIGRATION_JOB_NAME \
      --region=REGION \
      --source=SOURCE_CONNECTION_PROFILE \
        --source=DESTINATION_CONNECTION_PROFILE \
      --type=CONTINUOUS \
      --original-migration-name=ORIGINAL_MIGRATION_JOB_ID \
      --max-concurrent-destination-connections=MAX_CONCURRENT_CONNECTIONS

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs create MIGRATION_JOB_ID `
      --no-async
      --display-name=MIGRATION_JOB_NAME `
      --region=REGION `
      --source=SOURCE_CONNECTION_PROFILE `
        --source=DESTINATION_CONNECTION_PROFILE `
      --type=CONTINUOUS `
      --original-migration-name=ORIGINAL_MIGRATION_JOB_ID `
      --max-concurrent-destination-connections=MAX_CONCURRENT_CONNECTIONS

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs create MIGRATION_JOB_ID ^
      --no-async
      --display-name=MIGRATION_JOB_NAME ^
      --region=REGION ^
      --source=SOURCE_CONNECTION_PROFILE ^
        --source=DESTINATION_CONNECTION_PROFILE ^
      --type=CONTINUOUS ^
      --original-migration-name=ORIGINAL_MIGRATION_JOB_ID ^
      --max-concurrent-destination-connections=MAX_CONCURRENT_CONNECTIONS

You should receive a response similar to the following:
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    

  2. Start the migration job. Run the following command (click the link to expand):

#### `gcloud database-migration migration-jobs start`

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your migration job is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    start MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    start MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    start MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: MIGRATION_JOB_ID
      verb: start
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

     * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
     * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.

  3. Keep monitoring your failback migration job with Database Migration Service observability features. For more information, see [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-job-metrics). **Caution:** Database Migration Service doesn't consume replication slots when you stop the failback migration job. Stopping a migration job for longer periods of time might cause significant WAL file growth, potentially causing instance failure. We recommend that you stop active migration jobs for short periods of time to avoid disruptions. The `max_slot_wal_keep_size` setting on your instance to can help you estimate how quickly your log files can fill up the disk. 



## What's next

  * You can promote the migration job to stop the failback replication process. See [ Promote a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/finalize-migration).

  * Learn more about other migration scenarios supported in Database Migration Service. See [ Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
