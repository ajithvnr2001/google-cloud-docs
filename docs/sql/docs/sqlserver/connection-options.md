---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connection-options/
title: Choose how to connect to Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:55.022522+00:00
---

# Choose how to connect to Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connection-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Choose how to connect to Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connection-options "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connection-options "View this page for the PostgreSQL database engine") | SQL Server

This page provides an overview of the ways in which you can connect to your Cloud SQL instance.

Before you can connect to a Cloud SQL instance, you need to decide how to deploy and configure your Cloud SQL instance and supporting networking resources. If your Cloud SQL instance is already configured and deployed, then this page can help you understand the different ways that you can connect your clients to the existing instance.

## IP address type: private or public

When you first create your Cloud SQL instance, you can choose whether to configure the instance with a _public IP address_ , a _private IP address_ , or a _combination of both_.

You choose the IP address configuration of your instance based on your application requirements. Then after you configure your instance, you specify either a public IP address, a private IP address, or in some cases a DNS name in your client connection string.

| Private IP address | Public IP address  
---|---|---  
**Description** | Internal, Virtual Private Cloud (VPC) network-only (private) IP address  | An external, internet-accessible (public) IP address  
**Decision points** | Do you need to connect from clients hosted on VPC networks inside Google Cloud or from clients that have access to those VPC networks? If yes, then choose a **private IP address** for the instance. | Do you need to connect from clients outside the Google Cloud VPC network over the public internet? If yes, then choose a **public IP address** for the instance.  
**Configuration options** |  The following types of private networking configurations are supported:

  * [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect): connect to Cloud SQL instances from multiple VPC networks that belong to different groups, projects, or organizations. Private Service Connect is the default private IP connectivity option for new projects.
  * [Private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access): connect to Cloud SQL instances from a single VPC network based on VPC Network Peering.
For more information about choosing a private networking configuration, see [Private IP configuration options](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip). 
| When you connect directly to an instance using a public IP address, you must configure [authorized networks](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-networks). Another more secure alternative for connecting to a Cloud SQL instance that uses public IP is to use a Cloud SQL connector (such as the Cloud SQL Auth Proxy or one of the Cloud SQL Language Connectors). For instructions about adding a public IP to your instance, see [Configure public IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip). To connect to a Cloud SQL instance using a public IP address, you can use the [`sqlcmd` client](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip) or another available client.  
**Summary** |  **Recommendation** : For improved security, we recommend that you configure your instance with a private IP address type unless you have specific requirements for an internet-accessible Cloud SQL instance, or if you're connecting from a client that doesn't meet the requirements for a VPC.  
  
## Connection type: Cloud SQL connector or direct

When you make the connection to a Cloud SQL instance, you can use a Cloud SQL connector, or you can make a direct connection.

A Cloud SQL connector is either the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy) or one of the [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/language-connectors).

| Cloud SQL connector | Direct connection  
---|---|---  
**Description** | Cloud SQL Auth Proxy, a client-side proxy, and Cloud SQL Language Connectors, client-side libraries, provide simplified and secure access to your Cloud SQL instances, especially when you connect to an instance using a public IP address. | A direct connection from a client to a Cloud SQL instance provides a lower latency connection. A direct connection can be made from either a public or a private IP address.   
**Decision points** |  Cloud SQL connectors are beneficial in the following scenarios:

  * When you want to connect to a Cloud SQL instance using a public IP address without having to configure [authorized networks](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-networks).
  * When you want to encrypt traffic to and from the database automatically with server and client identity verification without having to manage SSL certificates.
  * When you're using IAM database authentication and want to refresh your OAuth 2.0 access tokens automatically.
  * When you're connecting from a client or application that uses a dynamically assigned or ephemeral IP address. Dynamic IP configuration can be common for Platform as a Service (PaaS) applications.

|  Using a direct connection provides the following benefits:

  * Lower latency compared to connections using Cloud SQL connectors.
  * No additional package or library dependency unlike Cloud SQL connectors.
  * When you use a direct connection, you're responsible for configuring the SSL/TLS settings.

  
**Configuration options** | 

  * [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy), or 
  * Cloud SQL Language Connectors, including
    * [Cloud SQL Java connector](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors#java)
    * [Cloud SQL Python connector](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors#python)
    * [Cloud SQL Go connector](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors#go)
    * [Cloud SQL Node.js connector](https://docs.cloud.google.com/static/sql/docs/sqlserver/connect-connectors#node.js)
The following Google Cloud services use an embedded Cloud SQL Auth Proxy when you connect to a Cloud SQL instance over public IP address:
    * [Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run)
    * [App Engine flexible environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard)
    * [App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible)

|  To configure SSL/TLS certificates on the Cloud SQL instance and for your client, do the following:

  1. [Choose a server CA mode for your instance](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies).
  2. Configure your instance to [enforce SSL/TLS encryption for connections on the instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#enforcing-ssl).
  3. [Create client certificates.](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#client-certs)
  4. Download your server and client certificates.

  
**Summary** | When you connect to a Cloud SQL instance, you can use either a Cloud SQL connector, or connect directly from clients. **General recommendation** : If you're connecting to an instance by a **private IP address** , use a direct connection. We also recommend that you enforce SSL and configure SSL/TLS certificates for your connection. If you're connecting to an instance by a **public IP address** , use a Cloud SQL connector (either the Cloud SQL Auth Proxy or one of the Cloud SQL Language Connectors).  
  
## Database authentication type: Managed Service for Microsoft Active Directory or built-in

When you connect to an instance, you must authenticate as a database user. You can choose between [built-in authentication in Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/users) or [Managed Microsoft AD](https://docs.cloud.google.com/sql/docs/sqlserver/ad).

### Remove networking options from an instance

Cloud SQL supports the removal of the following networking options from an instance:

  * Public IP from an instance with both private services access and public IP
  * Public IP from an instance with public IP, private services access, and Private Service Connect
  * Private Service Connect from an instance with both Private Service Connect and private services access
  * Private Service Connect from an instance with Private Service Connect, private services access, and public IP



### Enable networking options for an instance

Cloud SQL supports enabling the following connection options for instances:

  * Private services access on an instance with public IP only
  * Private Service Connect on an instance with private services access only
  * Private Service Connect on an instance with both private services access and public IP
  * Public IP on an instance with private services access only



### Limitations

  * You can't create an instance with both a public IP address and Private Service Connect.
  * You can't remove private services access from an instance with private services access and Private Service Connect.
  * You can't remove private services access from an instance with private services access and public IP.
  * If you have an instance that uses only public IP, then you can't enable both private services access and Private Service Connect at the same time. First, enable private services access, and then enable Private Service Connect.
  * You can't use authorized networks to do IP address-based allowlisting for Private Service Connect instances.



## Tools for connecting to Cloud SQL

The following table contains some options for connecting to Cloud SQL:

Connection option | More information  
---|---  
**Cloud SQL Auth Proxy** | 

  * [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy)
  * [Connecting using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#connecting-client)
  * [Connecting using the Cloud SQL Auth Proxy Docker Image](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#docker-proxy-image)

  
**[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)** | 

  * [`gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect)

  
**Cloud SQL language connectors** | 

  * [Connect using Cloud SQL Connectors for Java, Python and Go.](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors)

  
**Cloud Shell** | 

  * [Connecting using the Cloud Shell](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip#cloud-shell)

  
**Cloud Code** | 

  * [Connecting using Cloud Code in JetBrains IDE](https://docs.cloud.google.com/code/docs/intellij/connect-sql-database)

  
|   
Connect using third-party database administration tools |   
**SQL Server Management Studio** | 

  * [Connecting with SQL Server Management Studio](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-shell#connect-using-ssms)

  
**SSMS Object Explorer** | 

  * [Connecting with SSMS Object Explorer](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-shell#connect-using-object-explorer)

  
**Visual Studio** | 

  * [Visual Studio Code for SQL Server](https://code.visualstudio.com/)

  
  
## Troubleshoot

If you're having problems connecting, then check the following pages for help debugging or finding solutions to known issues:

  * [Debugging connection issues](https://docs.cloud.google.com/sql/docs/sqlserver/debugging-connectivity)
  * [Known connectivity errors](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshooting#connectivity)
  * [Troubleshooting Cloud SQL Auth Proxy connection](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#troubleshooting)
  * [Common connection issues](https://docs.cloud.google.com/sql/docs/sqlserver/diagnose-issues#connection)



## What's next

  * Learn how to connect with the [Quickstart for Cloud SQL for sqlserver](https://docs.cloud.google.com/sql/docs/sqlserver/quickstart).
  * Learn best practices for [managing database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections).
  * Learn about [IAM database authentication](https://docs.cloud.google.com/docs/authentication).
  * Learn about [connecting using a sqlcmd client from a local machine or Compute Engine](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip).
  * Learn about [configuring IP connectivity](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip). 
  * Learn about [the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy).
  * Learn about [options for support](https://docs.cloud.google.com/sql/docs/sqlserver/support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
