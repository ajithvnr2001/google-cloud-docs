---
url: https://docs.cloud.google.com/sql/docs/sqlserver/private-ip/
title: Private IP configuration options \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:20.624305+00:00
---

# Private IP configuration options  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/private-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Private IP configuration options Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/private-ip "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/private-ip "View this page for the PostgreSQL database engine") | SQL Server

This document describes the options you have for configuring a Cloud SQL instance to support private IP connections.

Private IP connections offer better security and lower latency than public IP connections. You can use private IP connections to provide access across regions to your Cloud SQL instance as well as connections to external sources.

You can connect to your instance using a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) between projects.

For Terraform solutions for Cloud SQL networking, see [Simplified cloud networking configuration solutions](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions).

## Private IP connection options

Use one or both of the following two methods to configure a Cloud SQL instance with a private IP address:

  * [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect): gives you the flexibility of connecting from multiple VPC networks, including cross-cloud and on-premise VPC networks. Private Service Connect is recommended over private services access because it provides better IP address space management, scalability and security controls. Private Service Connect is the default private IP connectivity option in the Google Cloud console for new projects. For more information, see the [Overview of Private Service Connect in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect).

  * [Private services access](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-services-access): is an earlier type of private IP connectivity, based on VPC Network Peering. Private services access only allows connections from one VPC network. You need additional configuration to [connect from multiple VPC networks](https://docs.cloud.google.com/sql/docs/sqlserver/connect-multiple-vpcs). For more information, see the [Overview of private services access in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-services-access). VPC networks.




When you use the Google Cloud console to create a Cloud SQL instance, if you choose **Private IP** under **Connections** , then, depending on your use case, you can select either **Private Service Connect (PSC)** (default), **Private Service Access (PSA)** , or both.

### Restrictions for private IP connection options

The following restrictions apply to private IP connections:

  * Instances configured with Private Service Connect don't have visibility into the IP addresses of clients.
  * Instances configured with both Private Service Connect and private services access can't change the [associated VPC network](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access#change-psa-config) for private services access.



## Requirements for private IP connections

To create and manage private IP connections using either private services access or Private Service Connect, your network and application environment must meet certain requirements, and you need to have the right Identity and Access Management permissions. For the full list of API and IAM requirements, see the following pages:

  * [Configure private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access)
  * [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
