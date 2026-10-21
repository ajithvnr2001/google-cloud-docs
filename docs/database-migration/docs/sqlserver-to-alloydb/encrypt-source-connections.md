---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/encrypt-source-connections/
title: Configure encryption for source database connections \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:51.163789+00:00
---

# Configure encryption for source database connections  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/encrypt-source-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Configure encryption for source database connections Stay organized with collections  Save and categorize content based on your preferences. 

The following sections provide steps you need to perform to configure SSL/TLS encryption for your source network connections. Refer to the section relevant for your source database:

  * Encrypt connections to self-hosted SQL Server databases
  * Encrypt connections to Amazon RDS for SQL Server
  * Encrypt connections to Microsoft Azure databases
  * Encrypt connections to Cloud SQL for SQL Server

**Tip:** Remember that with regards to [ network connectivity](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-overview), Database Migration Service is considered the **client** and your source database is the **server**.

## Encrypt connections to self-hosted SQL Server databases

The following sections contain details to help you configure SSL/TLS encryption for connections to self-hosted SQL Server sources.

### Use basic encryption

To use the basic encryption for connections to a self-hosted source, do the following:

  1. Make sure your source database server meets the requirements to use SSL certificates. For more information, see [ Certificate requirements for SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/certificate-requirements) in the Microsoft documentation. 
  2. Obtain a TLS certificate signed by a trusted Certificate Authority (CA). Consult your organization policies to make sure you use the right channels to get the certificate. 

It is possible to use self-signed certificates for this purpose (for example generated with the [ `openssl` command line tool](https://docs.openssl.org/master/man1/openssl/)), but we don't recommend them for production use. Your security systems might flag self-signed certificates as a vulnerability. 

  3. On your source database server, do the following: 
     1. Install the server certificate by using SQL Server Configuration Manager. For more information, see [ Install a certificate for a single SQL Server instance](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/manage-certificates#provision-single-server-cert) in the Microsoft documentation. 

Now when client applications connect to your server, they can request to use SSL connections. Your server presents its certificate when Database Migration Service establises the connection. 

     2. Optional: Enforce SSL encryption for all client connections.

To further increase security, you can configure your server to always require that client applications use encrypted connections. For more information, see [ Enforce SSL connections for SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-sql-server-encryption#step-2-configure-encryption-settings-in-sql-server) in the Microsoft documentation. 

  4. You don't need to prepare any more certificate files. Make sure you select the **Basic** encryption type when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile). 



### Use TLS variant

To use TLS encryption for connections to a self-hosted source, do the following:

  1. Make sure your source database server meets the requirements to use SSL certificates. For more information, see [ Certificate requirements for SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/certificate-requirements) in the Microsoft documentation. 
  2. Obtain an SSL/TLS certificate signed by a trusted Certificate Authority (CA). Consult your organization policies to make sure you use the right channels to get the certificate. Make sure you save the x509 PEM-encoded root CA certificate that signs your server certificate. You need to provide it for the source connection profile in Database Migration Service. 

It is possible to use self-signed certificates for this purpose (for example generated with the [ `openssl` command line tool](https://docs.openssl.org/master/man1/openssl/)), but we don't recommend them for production use. Your security systems might flag self-signed certificates as a vulnerability. 

  3. On your source database server, do the following: 
     1. Install the server certificate by using SQL Server Configuration Manager. For more information, see [ Install a certificate for a single SQL Server instance](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/manage-certificates#provision-single-server-cert) in the Microsoft documentation. 

Now when client applications connect to your server, they can request to use SSL connections. Your server presents its certificate when Database Migration Service establises the connection. 

     2. Optional: Enforce SSL encryption for all client connections.

To further increase security, you can configure your server to always require that client applications use encrypted connections. For more information, see [ Enforce SSL connections for SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-sql-server-encryption#step-2-configure-encryption-settings-in-sql-server) in the Microsoft documentation. 

  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. Select **TLS** for the encryption type.
     2. In the **Source CA certificate** section, click **Browse** and upload the x509 PEM-encoded root CA certificate that signs your server certificate.



## Encrypt connections to Amazon RDS for SQL Server

The following sections contain details to help you configure SSL/TLS encryption for connections to Amazon RDS for SQL Server sources.

### Use basic encryption

By default, Amazon RDS for SQL Server uses SSL/TLS encryption when the connecting client requests it in the connection string. You can optionally [ enforce SSL/TLS for all connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.SSL.Using.html#SQLServer.Concepts.General.SSL.Forcing), but you don't need to configure anything on your Amazon RDS source to use basic encryption.

To use **basic** encryption, select the **Basic** encryption type when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile).

### Use TLS variant

To use TLS encryption for connections to Amazon RDS for SQL Server, do the following:

  1. By default, Amazon RDS for SQL Server uses SSL/TLS encryption when the connecting client requests it in the connection string. You don't need to enable any specific configuration on your source. 
  2. Optional: Enforce SSL encryption for all client connections.

To further increase security, you can configure your server to always require that client applications use encrypted connections. For more information, see [ Forcing connections to your DB instance to use SSL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.SSL.Using.html#SQLServer.Concepts.General.SSL.Forcing) in the Amazon RDS documentation. 

  3. Download the x509 PEM-encoded root CA certificate that signs your server certificate. This certificate is included in the certificate bundles provided by AWS. For more information, see [ Download certificate bundles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.CertificatesDownload) in the Amazon RDS documentation. 
  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. Select **TLS** for the encryption type.
     2. In the **Source CA certificate** section, click **Browse** and upload the x509 PEM-encoded root CA certificate you downloaded in the certificate bundle.



## Encrypt connections to Microsoft Azure databases

The following sections contain details to help you configure SSL/TLS encryption for connections to Microsoft Azure SQL Managed Instance or Microsoft Azure SQL Database source databases.

### Use basic encryption

By default, Microsoft Azure SQL Managed Instance and Microsoft Azure SQL Database [ require that all client connections use SSL/TLS encryption](https://learn.microsoft.com/en-us/azure/azure-sql/database/security-overview?view=azuresql#transport-layer-security-encryption-in-transit). You don't need to configure anything on your source database.

It's not possible to connect to SQL Server Azure sources without encryption. When you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), at minimum you must use the **Basic** encryption type.

### Use TLS variant

To use TLS encryption for connections to SQL Server sources in Microsoft Azure, do the following:

  1. By default, Microsoft Azure SQL Managed Instance and Microsoft Azure SQL Database [ require that all client connections use SSL/TLS encryption](https://learn.microsoft.com/en-us/azure/azure-sql/database/security-overview?view=azuresql#transport-layer-security-encryption-in-transit). You don't need to configure anything on your source database. 
  2. Download the x509 PEM-encoded root CA certificate that signs your server certificate. For SQL Server sources on Microsoft Azure, you need to use the **Baltimore CyberTrust Root**. For more information, see [ Azure Certificate Authority details](https://learn.microsoft.com/en-us/azure/security/fundamentals/azure-ca-details) in the Microsoft documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. Select **TLS** for the encryption type.
     2. In the **Source CA certificate** section, click **Browse** and upload the x509 PEM-encoded **Baltimore CyberTrust Root** certificate. 



## Encrypt connections to Cloud SQL for SQL Server

The following sections contain details to help you configure SSL/TLS encryption for connections to Cloud SQL for SQL Server sources.

### Use basic encryption

By default, Cloud SQL for SQL Server instances accept both encrypted and unencrypted client connections. You can optionally [ enforce SSL/TLS for all connections](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#enforcing-ssl), but you don't need to configure anything on your Cloud SQL source to use basic encryption.

To use **basic** encryption, select the **Basic** encryption type when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile).

### Use TLS variant

To use TLS encryption for connections to Cloud SQL for SQL Server sources, do the following:

### Console

  1. By default, Cloud SQL for SQL Server instances accept both encrypted and unencrypted client connections. You don't need to enable any specific configuration on your source. 
  2. Optional: Enforce SSL encryption for all client connections.

To further increase security, you can configure your server to always require that client applications use encrypted connections. For more information, see [ Enforce SSL/TLS encryption](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#enforcing-ssl) in the Cloud SQL for SQL Server documentation. 

  3. Download the x509 PEM-encoded root CA certificate that signs your server certificate: 
     1. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[ Go to **Cloud SQL Instances**](https://console.cloud.google.com/sql/instances)

     2. Click the name of your Cloud SQL for SQL Server source instance. 

The instance **Overview** page opens.

     3. Go to the **Connections** > **Security** tab.
     4. In the **Manage server CA certificates** section, click **Download certificates**. 

The `server-ca.pem` file downloads to your machine.

  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. Select **TLS** for the encryption type.
     2. In the **Source CA certificate** section, click **Browse** and upload the `server-ca.pem` you downloaded from your Cloud SQL for SQL Server instance. 



### gcloud

  1. Download the server certificate file. 

Cloud SQL for SQL Server creates a server certificate automatically when you create the instance. You need to download this file to later use it in the source connection profile. Run the following command (click the link to expand): 

#### `gcloud sql ssl server-ca-certs list`

Before using any of the command data below, make the following replacements: 

     * CLOUDSQL_INSTANCE_NAME with the name of your Cloud SQL instance.
     * DIRECTORY_PATH with the path to the folder where you want to save the server certificate.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta sql ssl server-ca-certs list \
    --format="value(cert)" \
    --instance=CLOUDSQL_INSTANCE_NAME > \
    DIRECTORY_PATH/server-ca.pem

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta sql ssl server-ca-certs list `
    --format="value(cert)" `
    --instance=CLOUDSQL_INSTANCE_NAME > `
    DIRECTORY_PATH/server-ca.pem

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta sql ssl server-ca-certs list ^
    --format="value(cert)" ^
    --instance=CLOUDSQL_INSTANCE_NAME > ^
    DIRECTORY_PATH/server-ca.pem

**Result** : 

The `server-ca.pem` file is now downloaded to your machine.

  2. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. Select **TLS** for the encryption type.
     2. In the **Source CA certificate** section, click **Browse** and upload the `server-ca.pem` you downloaded from your Cloud SQL for SQL Server instance. 



## What's next

  * All source connections can be configured to use SSL/TLS encryption, regardless of the networking method you use. To learn more about source database network connectivity, see [ Source database networking methods](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-source).

  * To get a complete, step-by-step migration walkthrough, see [ SQL Server to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
