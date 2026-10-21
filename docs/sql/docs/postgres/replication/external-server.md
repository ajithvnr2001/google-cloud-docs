---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/external-server/
title: About replicating from an external server \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:59.926571+00:00
---

# About replicating from an external server  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/external-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  About replicating from an external server Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page describes a configuration that replicates data from a source database server to PostgreSQL replicas. This configuration is sometimes referred to as an _external server_ configuration.

The source database server can be any PostgreSQL server, including servers running on other Google Cloud services (such as Cloud SQL or Compute Engine) or on other cloud providers (such as Amazon RDS), if they meet the requirements. For step-by-step instructions for setting up this configuration, see [Replicating from an external server](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external).

## Use cases for external server configuration

External server configuration helps you achieve the following goals:

  1. Migrate your data from your self-managed PostgreSQL server to Google Cloud with a minimum of downtime.

  2. Retain colocation and control of your server while off-loading the administration of the replicas to Cloud SQL.

This use case is sometimes called a _hybrid cloud_. Replication between your self-managed server and the Cloud SQL replica continues indefinitely.




## External replication configuration

External replication configuration includes the following instances:

  * The PostgreSQL server that you manage, also called the _source database server_.
  * The Cloud SQL replica.

There can be multiple replicas for a single source database server.

  * The _source representation instance_.

The source representation instance is a Cloud SQL instance that represents the source database server to the Cloud SQL replica. It is visible in the Google Cloud console and appears the same as a regular Cloud SQL instance, but it contains no data, requires no configuration or maintenance, and does not affect billing.




The following diagram shows these instances:

![Diagram of the three instances making up an external replication configuration](https://docs.cloud.google.com/static/sql/images/external-master-2nd-gen-pg.png)

## SSL/TLS configuration

Replicating from an external server requires that all changes to the data be sent between the source database server and the Cloud SQL replicas.

If the connection is made over a public network (by using IP allowlists), Google recommend using SSL/TLS encryption for the connection between the source and destination databases.

Cloud SQL offers the following options for SSL/TLS configuration: 

  * None: the Cloud SQL destination instance connects to the source database without encryption.
  * Server-only authentication

**Note:** For information about creating certificates and keys for your external server, see [Secure TCP/IP Connections with SSL](https://www.postgresql.org/docs/current/static/ssl-tcp.html).

### Server-only authentication

When the replica connects to the primary instance, the replica authenticates the primary instance. This helps make sure the replica connects to the correct host and helps prevent on-path attacks. The primary instance doesn't authenticate the replica.

To use server-only authentication, at replica creation time, provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the external server's certificate. The CA must contain only a single certificate, and it must be self signed. In other words, the Certificate Authority that signed the server's certificate must be a root CA.

### External server SSL expiration notification

If the external server's server CA certificate is expiring, then [rotate the SSL certificates](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance), including the server CA certificate on the on-premises instance.

For more information, see [Manage SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance).

## Multiple replicas from the same database server

You can create multiple replicas from the same source database server. You might want to provide more bandwidth or create replicas in different regions.

If you're creating multiple replicas in the same region, they can all use the same source representation instance or different ones. If you use the Google Cloud console to create multiple replicas, they will have different source representation instances.

If you're creating multiple replicas in different regions, they must have different source representation instances.

You cannot create more than one replica in the same operation. As soon as you finish creating the replica configuration for the first replica, you can start [creating the replica configuration](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#setup-replica-instance) for the other replicas. You don't need to wait until the first replica is completely functional before starting to create other replicas.

## Cascading replicas for an external server

[Cascading read replicas](https://docs.cloud.google.com/sql/docs/postgres/replication#cascading-replicas) let you create a read replica under another read replica in the same or different region. You can add up to four levels of cascading replicas, including the primary instance. When you promote the replica at the top of a cascading replica hierarchy, it becomes the primary instance and its cascading replicas continue to replicate.

With external servers, you can create read replicas under an external server replica after migrating your data, but before promoting the external server replica to primary. This lets you test read replica topologies before the external server replica is promoted.

**Note:** You can't directly promote a cascading read replica that's a replica of an external server replica. First, promote the external server replica. Then, you can promote the replica of the promoted external server replica.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
