---
url: https://docs.cloud.google.com/alloydb/docs/language-connectors-overview/
title: AlloyDB Language Connectors overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:29.416822+00:00
---

# AlloyDB Language Connectors overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/language-connectors-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AlloyDB Language Connectors overview Stay organized with collections  Save and categorize content based on your preferences. 

To establish encrypted, authorized connections from your application to an AlloyDB for PostgreSQL instance without managing SSL certificates or running a separate proxy process, you can use the AlloyDB Language Connectors.

AlloyDB Language Connectors are client libraries that provide automated mutual TLS (mTLS) with TLS 1.3 and [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) authorization when connecting to an AlloyDB instance. The libraries create authorized connections to the proxy server on the AlloyDB instance on behalf of your application and pass those connections to your application's database driver. They don't provide a network path to an AlloyDB instance if a network path isn't already present.

AlloyDB provides the following AlloyDB Language Connectors:

  * [AlloyDB Java Connector](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors) ([GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-java-connector))
  * [AlloyDB Python Connector](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors) ([GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-python-connector))
  * [AlloyDB Go Connector](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors) ([GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-go-connector))
  * [AlloyDB Node.js Connector](https://github.com/GoogleCloudPlatform/alloydb-nodejs-connector)



## Benefits of AlloyDB Language Connectors

AlloyDB Language Connectors provide the following benefits when connecting to an AlloyDB cluster: 

  * **Access control** : Uses IAM permissions to control who or what can connect to your AlloyDB instances.
  * **Convenience** : Uses automatic mTLS to provide extended mutual security and removes the requirement to manage SSL certificates, configure firewall rules, or enable authorized external networks.



## How AlloyDB Language Connectors work

AlloyDB Language Connectors use a client-side library component to connect to a proxy server on the AlloyDB instance. The connector creates an ephemeral certificate that authorizes the client to connect to the server-side proxy. The server-side proxy limits access to the AlloyDB database by requiring a valid TLS certificate to connect.

You can use AlloyDB Language Connectors with [private IP](https://docs.cloud.google.com/alloydb/docs/private-ip) (private services access or Private Service Connect) or [public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip). AlloyDB Language Connectors default to a private IP connection.

AlloyDB Language Connectors use built-in database authentication by default. You can also configure AlloyDB Language Connectors to use [automatic IAM database authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth). For information about how to install and configure the connectors, see [Connect using the AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors).

You can also connect to an AlloyDB cluster by using the [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview). For more information about connecting to an AlloyDB cluster, see the [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview).

## What's next

  * [Connect using the AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
