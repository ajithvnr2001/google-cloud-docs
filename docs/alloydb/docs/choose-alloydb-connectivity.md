---
url: https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity/
title: Choose a connectivity option \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:08.586917+00:00
---

# Choose a connectivity option  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Choose a connectivity option Stay organized with collections  Save and categorize content based on your preferences. 

To select the right network topology and connection method for your AlloyDB for PostgreSQL workload, compare private IP (private services access or Private Service Connect), public IP, direct connections, the AlloyDB Auth Proxy, and the AlloyDB Language Connectors:

  * What kind of network setup to use with AlloyDB.
  * How to connect securely.
  * Connection best practices.
  * How your workload location affects your connectivity requirements.



For more information, see the [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview).

## Recommended options to connect to AlloyDB

Use the following table to learn recommended connectivity options for your workloads:

  * Whether direct connections, or Language Connectors or the Auth Proxy, are recommended for [private IP](https://docs.cloud.google.com/alloydb/docs/private-ip) (private services access or Private Service Connect) and [public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip).
  * Connection requirements such as a Serverless VPC Access connector and Direct VPC egress. For more information, see [Compare Direct VPC egress and VPC connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc).
  * Considerations for private IP—[private services access](https://docs.cloud.google.com/alloydb/docs/about-private-services-access) versus [Private Service Connect](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect)—and [public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip).



## Assess your workload

Before you choose a connectivity option, assess your workload. AlloyDB supports connectivity for your workload environment for the following:

  * Cloud Run, Cloud Shell, and non-Google SaaS products
  * Cloud Run functions
  * App Engine flexible environment and App Engine standard environment
  * Google Kubernetes Engine and Compute Engine
  * On-premises environments

Workload environment | Private IP | Public IP | Description  
---|---|---|---  
Direct | Connector | Direct | Connector  
Developer laptop | ❌️ | ❌️ | ✅ | ✅ | We recommend that you use the [`gcloud beta alloydb connect`](https://docs.cloud.google.com/alloydb/docs/connect-gcloud) command. Alternatively, you can use the [Auth Proxy with public IP](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect). Connecting to private IP is possible, but it requires [additional setup](https://docs.cloud.google.com/alloydb/docs/connect-external).   
Cloud Shell | ❌ | ❌ | ✅ | ✅ | We recommend that you use the [`gcloud beta alloydb connect`](https://docs.cloud.google.com/alloydb/docs/connect-gcloud) command. Alternatively, you can use the [Auth Proxy with public IP](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect) from Cloud Shell. Connecting to private IP is possible, but it requires [additional setup](https://docs.cloud.google.com/alloydb/docs/connect-external).   
Cloud Run, Cloud Run functions | ✅ | ✅ | ✅ | ✅ | Requires a Serverless VPC Access connector or Direct VPC egress.  
App Engine Standard, Flex | ✅ | ✅ | ✅ | ✅ | Requires a Serverless VPC Access connector.  
GKE, Compute Engine | ✅ | ✅ | ✅ | ✅ | We recommend that you use private IP. Use private services access when you don't require transitive VPC Network Peering. Otherwise, use Private Service Connect.  
On-premises | ✅ | ✅ | ✅ | ✅ | Private IP requires a network path from on-premises to the target instance. Public IP with Language Connectors or with the Auth Proxy is a secure alternative that doesn't require extensive network setup.  



### Best practices for connectivity based on your workload

When you connect to AlloyDB, consider the following based on your workload environment.

#### Cloud Shell

  * Use the [Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview) with [public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip) to connect with Cloud Shell. Cloud Shell doesn't support connecting to a Virtual Private Cloud (VPC) network. It has no connectivity to private services access or Private Service Connect instances. In addition, Cloud Shell doesn't have a stable outbound IP address for use in authorized external networks. If you don't use the Auth Proxy or Language Connectors, you must allow all IP address ranges— for example, `0.0.0.0/0`. We don't recommend this approach for production instances.



#### Cloud Run and Cloud Run functions

  * For private IP, both direct connections and Language Connectors or the Auth Proxy should use Direct VPC egress.
  * For public IP, you must use [Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors) or the [Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview). Alternatively, you can allow all IP address ranges—for example, `0.0.0.0/0`—in authorized external networks, but that approach is not recommended for production instances given the security risk.



#### App Engine standard environment and App Engine flexible environment

  * Use a Serverless VPC Access connector for private IP, regardless of whether you're using a Language Connector or the Auth Proxy.
  * For public IP, you must use Language Connectors or the Auth Proxy. Alternatively, you can allow all IP address ranges (for example, `0.0.0.0/0`) in authorized external networks. Due to security risks, however, we don't recommend this approach for production instances.



#### GKE and Compute Engine

  * You can use both direct connections and Language Connectors or the Auth Proxy for connecting to AlloyDB.



#### On-premises

  * You can use both direct connections and Language Connectors or the Auth Proxy for connecting to AlloyDB. The Language Connectors and Auth Proxy don't create a network path. Make sure that there is a network path between your workload and the AlloyDB instance.



## Secure connections with the AlloyDB Auth Proxy and connectors

The AlloyDB Language Connectors and the AlloyDB Auth Proxy provide enhanced security features like [Identity and Access Management (IAM) database authentication](https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication) and [mTLS](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview), but these features require additional setup. Direct connections, while encrypted by default, don't support client certificates or higher SSL modes—`verify-ca` and `verify-full`. We recommend that you use Language Connectors or the Auth Proxy with public IP, and use direct connections for private IP only when Language Connectors or the Auth Proxy isn't feasible.

IAM database authentication supports two approaches: individual authentication and group authentication. Group authentication is supported for database version `POSTGRES_15` and later, and does not support managed connection pooling.

Connection method | Encrypted connection | IAM authentication | IAM authorization | mTLS  
---|---|---|---|---  
Direct connection | ✅ | ✅ | ❌ | ❌  
Language Connectors or the Auth Proxy | ✅ | ✅ | ✅ | ✅  
  
### Best practices for secure connectivity

  * When you create a cluster, you must specify a private IP interface so that the cluster can be created. If you want to use public IP, we recommend that you choose Private Service Connect as the private IP interface.
  * Use Language Connectors or the Auth Proxy for security features like IAM authorization and authentication, and mTLS, even though they require some setup. For example, this approach is well-suited if you want to run the AlloyDB Auth Proxy as a sidecar or you want to use an AlloyDB Language Connector. If you use Language Connectors or the Auth Proxy, your database connection might experience a small increase in latency.
  * Use direct connections for optimal performance, and when Language Connectors or the Auth Proxy isn't feasible. Direct connections are encrypted by default (`sslmode=require`), but they don't have support for client certificates or higher SSL modes. Only use direct connections when Language Connectors or the Auth Proxy can't be used.



## Assess your network topology

For network topology, we recommend that you use [private services access](https://docs.cloud.google.com/alloydb/docs/about-private-services-access) for AlloyDB connections. Use [Private Service Connect](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect) to avoid transitive peering issues with multiple VPC networks. Public IP is suitable for connections from non-Google Cloud SaaS products, especially when private IP is impractical.

Network topology | Multi-VPC connections | Non-Google SaaS clients | Supports on-premises connections | Description  
---|---|---|---|---  
Private services access | ❌ | ❌ | ✅ | Transitive VPC connectivity isn't supported by default. You can run a SOCKS5 proxy manually for cross-VPC connectivity, but this approach is complex.  
Private Service Connect | ✅ | ❌ | ✅ | Provides the simplest configuration when you want to connect to AlloyDB from more than one VPC network.  
Public IP | ✅ | ✅ | ✅ | To avoid having to identify the source workload's CIDR ranges for authorized external networks, public IP is best paired with the [Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors) or the [Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect).  
  
### Best practices for connectivity based on your network topology

  * Default to [private services access](https://docs.cloud.google.com/alloydb/docs/about-private-services-access).
  * When you're dealing with multiple VPC networks, use Private Service Connect to circumvent transitive peering issues.
  * For non-Google Cloud SaaS products, choose a public network topology when you're integrating with Software-as-a-Service (SaaS) products that aren't hosted on Google Cloud, especially if private IP connectivity isn't feasible. Private IP is enabled by default, so you must explicitly configure public IP in these scenarios.
  * Whenever possible, use the Language Connectors or the Auth Proxy when you use public IP to achieve a secure connection without having to configure authorized external networks.



## What's next

  * [Create and query a database](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).
  * [Connect using the gcloud CLI](https://docs.cloud.google.com/alloydb/docs/connect-gcloud).
  * [Connect from Compute Engine](https://docs.cloud.google.com/alloydb/docs/connect-psql).
  * [Connect from Cloud Shell using the Auth Proxy](https://docs.cloud.google.com/alloydb/docs/quickstart/connect-cloud-shell).
  * [Connect through Cloud VPN or Cloud Interconnect](https://docs.cloud.google.com/alloydb/docs/connect-external#vpn).
  * [Connect using Data Agent Kit](https://docs.cloud.google.com/data-agent-kit).
  * Learn [AlloyDB connection concepts](https://docs.cloud.google.com/alloydb/docs/connection-overview).
  * [Learn about IAM database authentication](https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
