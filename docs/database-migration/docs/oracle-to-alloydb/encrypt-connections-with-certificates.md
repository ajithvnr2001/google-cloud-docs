---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/encrypt-connections-with-certificates/
title: Use SSL/TLS certificates to encrypt network connections \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:00.732252+00:00
---

# Use SSL/TLS certificates to encrypt network connections  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/encrypt-connections-with-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Use SSL/TLS certificates to encrypt network connections Stay organized with collections  Save and categorize content based on your preferences. 

Every connection Database Migration Service makes to your source database can be configured to use Secure Socket Layer/Transport Security Layer (SSL/TLS) encryption. This page provides an overview of available SSL/TLS encryption variants and the steps required to use them for your migration job.

SSL/TLS is mainly recommended for connections created over public networks where you need to expose a public IP address and port for your database. Regardless of which network connectivity method you use, your scenario might require that you use additional encryption.

Destination database connections are always encrypted by Database Migration Service. You don't need to configure additional certificates for those connections.

To understand how Database Migration Service uses SSL/TLS encryption, it's important to remember that with regards to [ network connectivity](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-overview), Database Migration Service is considered the **client** and your database (either source or destination database) is the **server**. Database Migration Service supports the following encryption variants:

None
    When Database Migration Service establishes a connection with your database, it doesn't send any SSL configuration string. It doesn't present any client certificates to the server, and it also doesn't verify any server certificates. 
TLS
    

When Database Migration Service connects to your database, it declares that the connection is established over a secured channel. Database Migration Service doesn't present a client certificate to the server, but it does validate the server certificate authority (CA) to make sure that it's connecting to the right host. This prevents person-in-the-middle attacks. 

To use TLS authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed your database server certificate. 

## What's next

  * Learn about encrypting source database connections. See [ Configure encryption for source database connections](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/encrypt-source-connections).

  * To get a complete, step-by-step migration walkthrough, see [ Oracle to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
