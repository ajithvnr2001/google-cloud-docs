---
url: https://docs.cloud.google.com/sql/docs/postgres/language-connectors/
title: Cloud SQL Language Connectors overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:54.423742+00:00
---

# Cloud SQL Language Connectors overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/language-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Cloud SQL Language Connectors overview Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/language-connectors "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/language-connectors "View this page for the SQL Server database engine")

This page summarizes the Cloud SQL Language Connectors and how to use them with your instances.

Cloud SQL Language Connectors are libraries that provide encryption and [IAM](https://docs.cloud.google.com/iam) authorization when connecting to a Cloud SQL instance. Cloud SQL Language Connectors create authorized connections to the server-side proxy on behalf of a user's application and pass that connection to the application's database driver. They don't provide a network path to a Cloud SQL instance if one is not already present.

Cloud SQL Language Connectors use a client-side component to connect to a proxy server on the Cloud SQL instance. The connector creates a temporary certificate that authorizes the holder to connect to the server-side proxy. The server-side proxy limits access to the Cloud SQL database by requiring a valid TLS certificate in order to connect.

Cloud SQL supports the following Cloud SQL Language Connectors:

  * [Cloud SQL Java connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#java)
  * [Cloud SQL Python connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#python)
  * [Cloud SQL Go connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#go)
  * [Cloud SQL Node.js connector](https://docs.cloud.google.com/static/sql/docs/postgres/connect-connectors#node.js)



Cloud SQL recommends using Cloud SQL Language Connectors to connect to your Cloud SQL instance. You can also connect to a Cloud SQL instance [using a database client](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip) or the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy). For more information about connecting to a Cloud SQL instance, see [About connection options](https://docs.cloud.google.com/sql/docs/postgres/connect-overview).

## Requirements

If your Cloud SQL instance uses [shared certificate authority (CA)](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#shared-regional-ca) as its `serverCaMode`, then on the client side, make sure that the Cloud SQL Language Connectors you're using meet the following version requirements:

  * [Cloud SQL Java connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#java): [v1.21.0](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/releases/tag/v1.21.0) or later
  * [Cloud SQL Go connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#go): [v1.12.0](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector/releases/tag/v1.12.0) or later
  * [Cloud SQL Node.js connector](https://docs.cloud.google.com/static/sql/docs/postgres/connect-connectors#node.js): [v1.4.0](https://github.com/GoogleCloudPlatform/cloud-sql-nodejs-connector/releases/tag/v1.4.0) or later

**Note:** [Cloud SQL Python connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#python) supports instances that use the shared CA configuration, but the connector doesn't verify server identity.

If your Cloud SQL instance uses [customer-managed CA](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#customer-managed-ca) as its `serverCaMode`, then on the client side, make sure that the Cloud SQL Language Connectors you're using meet the following version requirements:

  * [Cloud SQL Java connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#java): [v1.22.0](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/releases/tag/v1.22.0) or later
  * [Cloud SQL Go connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#go): [v1.14.0](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector/releases/tag/v1.14.0) or later
  * [Cloud SQL Node.js connector](https://docs.cloud.google.com/static/sql/docs/postgres/connect-connectors#node.js): [v1.6.0](https://github.com/GoogleCloudPlatform/cloud-sql-nodejs-connector/releases/tag/v1.6.0) or later



When an instance uses customer-managed CA as its server CA mode, you can configure the instance with a [custom DNS name](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#custom-dns-name). You provide the custom DNS name in the custom subject alternative name (SAN) field of the server certificate.

After you set up a custom DNS name for the instance, you can connect to the instance from Cloud SQL Language Connectors using the DNS name.

## Benefits of Cloud SQL Language Connectors

Cloud SQL Language Connectors provide the following benefits with connecting to a Cloud SQL instance: 

  * **IAM authorization** : Uses identity and access management (IAM) permissions to control who or what can connect to your Cloud SQL instances.
  * **Convenience** : Removes the requirement to manage SSL certificates, configure firewall rules, or enable authorized networks.



## Limitations

You can't use the Cloud SQL Language Connectors if you're using [context-aware access](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto) and IAM database authentication. When you try to login to the instance, IAM authentication fails.

## Enforce the use of Cloud SQL Language Connectors

By using [connector enforcement](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances#ConnectorEnforcement), you can enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to Cloud SQL instances. With connector enforcement, Cloud SQL rejects direct connections to the database.

If you're using a [Private Service Connect-enabled instance](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect), then there's a limitation. If the instance has connector enforcement enabled, then you can't create read replicas for the instance. Similarly, if the instance has read replicas, then you can't enable connector enforcement for the instance.

For more information about how to enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to an instance, see [Connect using Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#enforce).

## What's next

  * [Connect using the Cloud SQL Java Connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#java).
  * [Connect using the Cloud SQL Python Connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#python).
  * [Connect using the Cloud SQL Go Connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#go).
  * [Connect using the Cloud SQL Node.js Connector](https://docs.cloud.google.com/static/sql/docs/postgres/connect-connectors#node.js).
  * Learn more about the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
