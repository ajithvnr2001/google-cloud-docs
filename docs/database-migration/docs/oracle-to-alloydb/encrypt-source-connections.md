---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/encrypt-source-connections/
title: Configure encryption for source database connections \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:36.462985+00:00
---

# Configure encryption for source database connections  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/encrypt-source-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Configure encryption for source database connections Stay organized with collections  Save and categorize content based on your preferences. 

The following sections provide steps you need to perform to configure SSL/TLS encryption for your source network connections.

**Tip:** Remember that with regards to [ network connectivity](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-overview), Database Migration Service is considered the **client** and your source database is the **server**.

## Encrypt connections to self-hosted Oracle databases

The following sections contain details to help you configure SSL/TLS encryption for connections to self-hosted Oracle sources.

### Use TLS variant

To use TLS encryption for connections to a self-hosted source, do the following:

  1. Obtain an SSL/TLS certificate signed by a trusted Certificate Authority (CA). Consult your organization policies to make sure you use the right channels to get the certificate. Make sure you save the x509 PEM-encoded root CA certificate that signs your server certificate. You need to provide it for the source connection profile in Database Migration Service. 

It is possible to use self-signed certificates for this purpose (for example generated with the [ `openssl` command line tool](https://docs.openssl.org/master/man1/openssl/)), but we don't recommend them for production use. Your security systems might flag self-signed certificates as a vulnerability. 

  2. Configure TLS authentication on your source Oracle database. For more information, see [ Configuring a Transport Layer Security Connection without a Client Wallet](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/configuring-secure-sockets-layer-authentication.html#DBSEG-GUID-28A27D34-D642-45AB-BA0F-F20D4494FB38) in the Oracle documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-source-connection-profile), do the following: 
     1. Select **TLS** for the encryption type.
     2. In the **Source CA certificate** section, click **Browse** and upload the x509 PEM-encoded root CA certificate that signs your server certificate.



## Encrypt connections to Amazon RDS for Oracle

The following sections contain details to help you configure SSL/TLS encryption for connections to Amazon RDS for Oracle sources.

### Use TLS variant

To use TLS encryption for connections to Amazon RDS for Oracle, do the following:

  1. Enable the Oracle SSL encryption option on your Amazon RDS Oracle source database. For more information, see [ Using SSL with an RDS for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.SSL.html) in the Amazon RDS documentation. 
  2. Download the x509 PEM-encoded root CA certificate that signs your server certificate. This certificate is included in the certificate bundles provided by AWS. For more information, see [ Download certificate bundles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.CertificatesDownload) in the Amazon RDS documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-source-connection-profile), do the following: 
     1. Select **TLS** for the encryption type.
     2. In the **Source CA certificate** section, click **Browse** and upload the x509 PEM-encoded root CA certificate you downloaded in the certificate bundle.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
