---
url: https://docs.cloud.google.com/alloydb/docs/connection-overview/
title: Connection overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:49.051173+00:00
---

# Connection overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connection overview Stay organized with collections  Save and categorize content based on your preferences. 

To connect your applications and tools securely to AlloyDB for PostgreSQL databases, you can configure networking, authorization, authentication, and connection pooling:

  * **Networking:** AlloyDB instances use public or private IP addresses on a [Virtual Private Cloud](https://docs.cloud.google.com/vpc/docs/overview) (VPC) network. Several options allow secure connections from applications running outside the VPC network.

  * **Authorization:** The AlloyDB Auth Proxy and AlloyDB Language Connectors let you use [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview) (IAM) to control who has access to your data. Your VPC network's firewall rules let you further tune access to AlloyDB resources.

  * **Authentication:** Use standard PostgreSQL user-authentication techniques to sign in to your instances. AlloyDB also supports IAM-based authentication using standard PostgreSQL user roles.

  * **Pooling:** To improve reliability, performance, and scalability, use standard PostgreSQL client-side connection pooling and server-side managed connection pooling.




For guidance on choosing the right connectivity setup for your workload, see [Choose a connectivity option](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity).

## Networking

Even though an AlloyDB instance contains many nodes, your applications connect to an instance through a single, static IP address. This address can be either a private IP address on the VPC network that you specify when first setting up an instance's cluster, or a public IP address that allows direct connections from outside of the VPC network.

### Private IP

When you configure AlloyDB with private IP, your instance gets a private IP address within your VPC network.

Private IP addresses affect connections to your application in two ways:

  * Applications running elsewhere within your project's VPC network can connect to the instance—or to a proxy representing the instance—without additional steps or resources.

As an example, [Connect from Compute Engine](https://docs.cloud.google.com/alloydb/docs/connect-psql) shows how to connect to your AlloyDB instance by running the `psql` command-line program on a Compute Engine VM within your VPC network.

  * Applications running outside the VPC network require an intermediary service to connect to the AlloyDB instance. Solutions include running proxy services on a VM within the instance's VPC network, or using other Google Cloud products to establish a permanent connection between your application and your VPC network.

For more information, see [Connect to a cluster from outside its VPC](https://docs.cloud.google.com/alloydb/docs/connect-external).




Connections over private IP typically provide lower latency and limited attack vectors because they don't require traversing the internet.

To learn more about private IP in AlloyDB, see [Private IP overview](https://docs.cloud.google.com/alloydb/docs/private-ip).

### Public IP

When you configure AlloyDB with public IP, your instance gets a public IP address for inbound connections that is accessible on the public internet. Optionally, you can use _authorized external networks_ to specify a range of IP addresses in CIDR format that can access your instance.

We recommend using public IP with AlloyDB Language Connectors or the AlloyDB Auth Proxy to ensure secure connections between the client and your instance.

For more information about adding a public IP address and authorized external networks to your instance, see [Connect using public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip).

AlloyDB also supports outbound connections from your instance to the public internet. When you enable outbound public IP, AlloyDB provides a consistent and predictable source IP address for traffic leaving your AlloyDB instance to the public internet. When you enable this feature, AlloyDB provisions a pair of static public IP addresses that are exclusively used for outbound connections from your instance.

Outbound connections are particularly useful for the following scenarios:

  * **Database migration** : When migrating your data from an external database to AlloyDB using [Database Migration Service](https://docs.cloud.google.com/database-migration/docs/overview), you can configure the external database's firewall to allow connections from the specific outbound IP addresses of your AlloyDB instance, ensuring a secure data transfer path.

  * **Foreign data wrappers** : If you need to query data from an external database within AlloyDB using foreign data wrappers such as `postgres_fdw` or `oracle_fdw`, you can add your instance's outbound IP addresses to the external database's allowlist. This configuration allows AlloyDB to securely connect and query the external data source.




When you enable outbound public IP, you can view the assigned IP addresses in the Google Cloud console or by using the gcloud CLI. You can then use these IP addresses to configure firewall rules or access control lists (ACLs) on your external systems to grant your AlloyDB instance access to your external systems.

For more information about enabling outbound public IP, see [Add outbound connectivity to an instance](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#add-outbound-connectivity).

## Authorization

You can control access to an AlloyDB cluster by using AlloyDB Language Connectors, the AlloyDB Auth Proxy, or VPC firewall rules.

### AlloyDB Language Connectors

AlloyDB Language Connectors are client libraries that provide automated mTLS using TLS 1.3 and IAM authorization when connecting to an AlloyDB cluster.

You can use these libraries directly from their respective programming languages. They provide the same capabilities as the Auth Proxy without requiring an external process. This approach provides improved security and reduced configuration requirements to connect to AlloyDB.

For more information, see [AlloyDB Language Connectors overview](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview).

### Connect using gcloud

For interactive database sessions, you can use the `gcloud beta alloydb connect` command. This command simplifies the connection process by automatically managing a local instance of the AlloyDB Auth Proxy and starting a `psql` client session for you.

For more information, see [Connect using gcloud](https://docs.cloud.google.com/alloydb/docs/connect-gcloud).

### Control access with IAM and the AlloyDB Auth Proxy

Although you can connect directly to an instance through its IP address, we recommend using the AlloyDB Auth Proxy in production environments. It provides IAM-based access control and end-to-end encryption between the proxy and your cluster.

For more information, see [About the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview).

### Limit VPC access with firewall rules

As with any cloud-based project, you should tune your VPC network's firewall rules to restrict network access only to the IP ranges or subnetworks that your applications connect from. This practice is especially important with external applications, as detailed in [Connect to a cluster from outside its VPC](https://docs.cloud.google.com/alloydb/docs/connect-external).

For more information about configuring your VPC network's firewall, see [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

## Authentication

AlloyDB supports two kinds of database users, each of which has its own way of authenticating with your databases:

  * Standard PostgreSQL user roles authenticate using a username and password. You manage these accounts using ordinary PostgreSQL user-management techniques. For more information, see [Manage PostgreSQL users with built-in authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles).

  * IAM user and service accounts authenticate as database users using OAuth 2.0 tokens. You manage these accounts using the Google Cloud IAM system. For more information, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).




After authenticating with an AlloyDB instance, an application can treat the instance like an ordinary PostgreSQL server. After establishing networking and authorization routes to an instance, you can use standard PostgreSQL techniques to sign in to an instance and access your data. This holds true whether manually signing in with a tool like `psql`, or connecting to your database programmatically using a PostgreSQL code library.

Typically, your first authentication with a new AlloyDB cluster involves signing in to its primary instance as its `postgres` user, using the password that you specify when creating the cluster. From there, you can create database users without administrative privileges for your application's use.

If you don't set a password for `postgres` when creating a cluster, then you can't sign in to the cluster. To sign in, either set a password for `postgres` or create an additional user. For more information, see [Manage PostgreSQL users with built-in authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles).

## Pooling

_Connection pooling_ is a technique that helps you ensure that your workload has a reliable and performant connection to your database. It is useful on both the client and the server side.

### Client connection pooling

When you connect to AlloyDB, use a client connection pool. The client connection pool creates multiple connections to your database and makes sure that those connections stay active and healthy throughout the lifetime of your workload. This approach ensures that your workload has a reliable connection to your database.

**Note:** In some cases, a client connection pool might be unnecessary. The following are example scenarios:

  * When you run queries manually from the command line.
  * When you use a language that doesn't support client connection pooling.
  * When the workload is ephemeral and won't maintain a long-lived connection.



You can use any standard client connection pool that supports PostgreSQL. Keep in mind the following:

  * The client connection pool library is sometimes separate from the PostgreSQL driver.
  * The PostgreSQL driver sometimes includes client connection pooling functionality in the same library.



The following are commonly used connection pool libraries:

  * [HikariCP](https://github.com/brettwooldridge/HikariCP) for Java
  * [SQLAlchemy](https://docs.sqlalchemy.org/en/20/core/pooling.html) for Python
  * [pgxpool](https://pkg.go.dev/github.com/jackc/pgx/v5#hdr-Connection_Pool) for Go
  * [node-postgres](https://node-postgres.com/features/pooling) for Node.js
  * [Npgsql](https://www.npgsql.org/) for .NET



If the library supports PostgreSQL, you can use it with AlloyDB.

### Configure client connection pools

To get the best performance out of your client connection pool, you might need to configure the pool size. Use the following formula as a starting point:
    
    
    connections = (vCPU count * 2) + 1
    

For more information, see [About Pool Sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing). Depending on real-world loads, you might need to perform additional tuning.

### Use managed connection pooling

In addition to client connection pooling, AlloyDB also supports server-side connection pooling with [managed connection pooling](https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling).

While you can use managed connection pooling for any transactional workload, managed connection pooling is best suited for applications that contain more short-lived connections, or applications that might experience a connection surge. For more information, see [Configure managed connection pooling](https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling).

## What's next

  * [Choose a connectivity option](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity).
  * Learn how to [connect using the gcloud CLI](https://docs.cloud.google.com/alloydb/docs/connect-gcloud).
  * Learn how to [connect to an AlloyDB instance with the `psql` command-line shell](https://docs.cloud.google.com/alloydb/docs/connect-psql). This guide includes instructions for setting up a VM within your VPC network and installing `psql` on it.

  * Learn how to [create a database](https://docs.cloud.google.com/alloydb/docs/database-create).

  * Learn how to [install and use the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect) to establish secure connections with your AlloyDB instance.

  * Learn about connecting using [AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview).

  * Learn how to connect from VS Code or an AI-powered CLI using [Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
