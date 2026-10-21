---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-source-connection-profile/
title: Create a source connection profile \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:50.778993+00:00
---

# Create a source connection profile  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-source-connection-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Create a source connection profile Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/create-source-connection-profile "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/create-source-connection-profile "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  
  


You can create a connection profile on its own or in the context of creating a specific migration job. Either way, all connection profiles are available for review and modification on the Connection profiles page, and can be reused across migration jobs.

Creating a source connection profile on its own is useful if the person who has the source access information is not the same person who creates the migration job. You can also reuse a source connection profile definition in multiple migration jobs. 

To see which source databases Database Migration Service supports, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest).

To create a source connection profile, follow these steps:

  1. Go to the [Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles) page in the Google Cloud Console.
  2. Click **Create profile**.
  3. On the **Create a connection profile** page, provide the following information required to connect to your source: 
     1. From the **Profile role** list, select **Source**.
     2. From the **Database engine** list, select your source database engine.

If you select **Cloud SQL for PostgreSQL** from this list, then a **Cloud SQL instance** list appears. Select the Cloud SQL instance that you want to migrate. 
     3. Enter a **Connection profile name**. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a migration job.
     4. Keep the auto-generated **Connection profile ID**.
     5. Enter a **Hostname** or **IP address**.

If the source database is hosted in Google Cloud or if a reverse SSH tunnel is used to connect the destination database to the source database, then specify the private (internal) IP address for the source database. This address will be accessible by the AlloyDB destination. For more information, see [Configure connectivity using VPC peering](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering).

For other connectivity methods, such as [IP allowlist](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods), provide the public IP address.

     6. Enter the **Port** that's used to access the host. The default PostgreSQL port is 5432.
  4. Enter a username and password for the source database. The user must have [these privileges](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database).
  5. In the **Connection profile region** section of the page, select the region where you want to save the connection profile.

Connection profiles, like all resources, are saved in a region. The connection profile should be created in the same region as the destination AlloyDB instance and the migration job. Region selection can impact availability in the case of regional downtime.
  6. Optional: If the connection is made over a public network (by using IP allowlists), then we recommend that you use [SSL/TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) encryption for the connection between the source and destination databases.

In the **Secure your connection** section, from the **Encryption type** list, you can select one of the following SSL/TLS configuration options:

     * **None** : The AlloyDB destination instance connects to the source database without encryption.
     * **TLS** authentication: When the AlloyDB destination instance connects to the source database, the instance authenticates the source, ensuring that the instance is connecting to the correct host securely. This prevents person-in-the-middle (PITM) attacks. For TLS authentication, the source doesn't authenticate the instance.

To use TLS authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the external server's certificate.

For more information about creating certificates and keys for your external server, see [Secure TCP/IP Connections with SSL](https://www.postgresql.org/docs/current/ssl-tcp.html).
     * **mTLS** authentication: When the destination instance connects to the source, the instance authenticates the source and the source authenticates the instance.

mTLS authentication provides the strongest security. However, if you don't want to provide the client certificate and private key when you create the AlloyDB destination instance, you can still use TLS authentication.

To use mTLS authentication, you must provide the following items when you create the source connection profile:

       * The certificate of the CA that signed the source database server's certificate (the CA certificate).
       * The certificate used by the instance to authenticate against the source database server (the client certificate).
       * The private key associated with the client certificate (the client key).

For more information about creating certificates and keys for your source database server, see [Secure TCP/IP Connections with SSL](https://www.postgresql.org/docs/current/ssl-tcp.html).

If you're having trouble uploading the key, then select the **Enter manually** option, and copy and paste the key into the text area.

  7. Click **Create** at the bottom of the page.

The **Connection profiles** page appears, and the newly created connection profile is displayed.




[ Previous arrow_back  Configure your source  ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database)

[ Next Review a migration job  arrow_forward  ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/review-migration-job)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


