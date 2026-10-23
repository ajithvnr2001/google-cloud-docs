---
url: https://docs.cloud.google.com/sql/docs/sqlserver/linked-servers/
title: About linked servers \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:04.374198+00:00
---

# About linked servers  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/linked-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  About linked servers Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

Linked servers give SQL Server the ability to read data from remote data sources and execute commands on remote databases. This page provides information about Cloud SQL instance permissions, things to consider when implementing linked servers, and the limitations of using linked servers.

## Linked server instance permissions

To set up linked servers, you need the following instance and user permissions:

  * `ALTER ANY LINKED SERVER`: Cloud SQL grants this permission when you add the `cloudsql enable linked servers` flag to your instance.
  * `ALTER ANY LOGIN`: Cloud SQL automatically grants this permission to the administrative user for the Cloud SQL instance. This permission lets you create a mapping between a login on Cloud SQL and a security account on a linked server.



For a list of the default permissions available for Cloud SQL instances, see [Default SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/users#default-users).

For information about how to grant the `ALTER ANY LINKED SERVER` or `ALTER ANY LOGIN` permission to additional accounts, see the example at [Granting server permissions](https://docs.cloud.google.com/sql/docs/sqlserver/users#grant-command).

## Considerations when using linked servers

This section has recommendations for handling security, performance, and reliability on linked servers.

### Security

To mitigate potential [security vulnerabilities](https://www.netspi.com/blog/technical/network-penetration-testing/how-to-hack-database-links-in-sql-server/), you need to ensure that linked servers have strong security protocols in place, such as the following:

  * Implement appropriate authentication and authorization mechanisms, such as [SSL encryption](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance).
  * Implement strict [password policies](https://learn.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-ver16).
  * Ensure that only authorized users have access to the linked server.
  * Ensure that sensitive data is properly encrypted and secured.
  * Ensure that logins only have access to the resources that you use during the configuration.



### Performance

There are a few factors that might impact performance on linked servers:

  * Linked servers can introduce latency and degrade performance when queries are complex, depending on the volume of data each server transfers. This can cause problems for applications that require real-time data synchronization.
  * When you use linked servers to run a query, a database engine creates a new connection and fetches data for every query you run. Data isn't cached and the server might [copy the entire table across the network](https://www.brentozar.com/archive/2021/07/why-are-linked-server-queries-so-bad/) every time you use a linked server.
  * Cloud SQL can't [create an optimized execution plan](https://datasteve.com/2020/04/02/linked-server-in-sql-server-the-good-the-bad-and-the-way-to-make-it-perfect/) for the remote server because it doesn't know how the remote server handles indexes and statistics.



To optimize performance, do the following:

  * Carefully design your queries and ensure that only the necessary data is being transferred between servers.
  * Use the [SQL Server distributed queries feature](https://learn.microsoft.com/en-us/host-integration-server/core/query-processor2).
  * Distribute queries across multiple servers.
  * Regularly monitor and optimize your linked server configuration to help ensure that it's running smoothly.



### Reliability

Any interruptions or failures in the link between servers can lead to significant downtime and potentially cause data loss.

To ensure reliable operation, it's important to implement appropriate failover and redundancy mechanisms. This can include the following:

  * Implement a backup linked server for failover.
  * Monitor server availability and performance.
  * Regularly test and validate your linked server configurations.



## Limitations

Linked servers for Cloud SQL have the following limitations:

  * Linked servers can't use data sources other than SQL Server.
  * Active Directory Authentication isn't available for linked Servers.
  * If you're using Private Service Connect to connect to a Cloud SQL instance, then you need to [enable Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-outbound) to use linked servers.
  * SQL Server Management Studio (SSMS) can't be used to configure a linked server. Instead, use the stored procedure mentioned in [Add a linked server](https://docs.cloud.google.com/sql/docs/sqlserver/manage-linked-servers#add_a_linked_server).
  * Linked servers aren't supported on instances that already have both private services access and Private Service Connect enabled.
  * You can't enable Private Service Connect on an instance that already has private services access and a linked server enabled.



For a full list of limitations for linked servers, see [Unsupported features & services](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-editions-and-components-2019?view=sql-server-ver16#Unsupported).

## What's next

  * Learn how to [enable, add, and configure linked servers](https://docs.cloud.google.com/sql/docs/sqlserver/manage-linked-servers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
