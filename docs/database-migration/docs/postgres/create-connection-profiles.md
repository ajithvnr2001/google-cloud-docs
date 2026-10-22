---
url: https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles/
title: Create a source connection profile \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:28.886778+00:00
---

# Create a source connection profile  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Create a source connection profile Stay organized with collections  Save and categorize content based on your preferences. 

Connection profiles capture identifiers for your source databases. Each connection profile contains the minimum required amount of information Database Migration Service needs to facilitate data movement between the data source and destination.

To create a source connection profile, follow these steps:

### Console

  1. Go to the [ Connection Profiles](https://docs.cloud.google.com/database-migration/docs/postgres/dbmigration/connection-profiles) page in the Google Cloud Console. 
  2. Click **Create profile**.
  3. On the **Create a connection profile** page, from the **Profile role** list, select **Source**. 
  4. From the **Database engine** list, select your source database engine. If you select **Cloud SQL for PostgreSQL** from this list, then an **Instance ID** list appears. Select the ID of the Cloud SQL instance that you want to migrate. 
  5. In the **Connection profile name** field, enter a human-readable name for your connection profile. This value is displayed in the connection profile list.
  6. Keep the auto-generated **Connection profile ID**.
  7. Enter a **Hostname** or **IP address**. 
     * The value you use here depends on the connectivity method you use for your migration. For example, if the source database is hosted in Google Cloud, or if a reverse SSH tunnel is used to connect the destination database to the source database, then specify the private (internal) IP address for the source database. For more information, see [ Network connectivity overview](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods). 

     * For migrations that connect over the public internet by using an IP allowlist, provide the public IP address of the source database. 
  8. Enter the **Port** that's used to access the host. The default PostgreSQL port is 5432.
  9. Enter a username and password for the source database. The user must have the required replication privileges on your source database. For more information, see [ Configure source database](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database). 
  10. In the **Connection profile region** section of the page, select the region where you want to save the connection profile. Connection profiles, like all resources, are saved in a region. Region selection doesn't impact which migration jobs can use them, or which regions can connect to the data location itself, but can impact availability in the case of regional downtime.
  11. Optional: If the connection is made over a public network (by using IP allowlists), then we recommend that you configure SSL/TLS encryption for the connection between the source and destination databases.

In the **Secure your connection** section, select one of the following SSL/TLS configuration options:

     * **None** : The Cloud SQL destination instance connects to the source database without encryption.
     * **Basic** : The Cloud SQL destination instance connects to the source database with encryption but doesn't verify the certificate authority (CA).
     * **TLS** authentication: When the Cloud SQL destination instance connects to the source database, the instance authenticates the source, ensuring that the instance is connecting to the correct host securely. To use TLS authentication, you must provide the x509 PEM-encoded certificate of the CA that signed the source server's certificate. 
     * **mTLS** authentication: When the destination instance connects to the source, the instance authenticates the source and the source authenticates the instance. To use mTLS authentication, you must provide: 
       * The certificate of the CA that signed the source database server's certificate (the CA certificate).
       * The certificate used by the instance to authenticate against the source database server (the client certificate).
       * The private key associated with the client certificate (the client key).
For more information about creating certificates and keys for your PostgreSQL server, see [ Secure TCP/IP Connections with SSL](https://www.postgresql.org/docs/current/ssl-tcp.html). 
  12. Click **Create**.

The **Connection profiles** page appears, and the newly created connection profile is displayed.




### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * SOURCE_CONN_ID with your source connection profile identifier.
  * REGION with the region where you want to save the connection profile.
  * SOURCE_IP_ADDRESS with the IP address of your source database.
  * SOURCE_PORT with the port of your source database (default is 5432).
  * SOURCE_USER with the username of the migration user on your source database.
  * SOURCE_PASSWORD with the password of the migration user on your source database.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles create postgresql \
      SOURCE_CONN_ID \
      --region=REGION \
      --role=SOURCE \
      --host=SOURCE_IP_ADDRESS \
      --port=SOURCE_PORT \
      --username=SOURCE_USER \
      --password=SOURCE_PASSWORD \
      --no-async

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles create postgresql `
      SOURCE_CONN_ID `
      --region=REGION `
      --role=SOURCE `
      --host=SOURCE_IP_ADDRESS `
      --port=SOURCE_PORT `
      --username=SOURCE_USER `
      --password=SOURCE_PASSWORD `
      --no-async

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles create postgresql ^
      SOURCE_CONN_ID ^
      --region=REGION ^
      --role=SOURCE ^
      --host=SOURCE_IP_ADDRESS ^
      --port=SOURCE_PORT ^
      --username=SOURCE_USER ^
      --password=SOURCE_PASSWORD ^
      --no-async

## What's next

  * [ Manage connection profiles](https://docs.cloud.google.com/database-migration/docs/postgres/manage-connection-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
