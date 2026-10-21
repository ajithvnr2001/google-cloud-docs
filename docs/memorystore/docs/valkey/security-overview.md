---
url: https://docs.cloud.google.com/memorystore/docs/valkey/security-overview/
title: Security overview \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:21.258520+00:00
---

# Security overview  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/security-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Security overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the security provided for your Memorystore for Valkey instance.

A Memorystore for Valkey instance isn't publicly accessible. Access to the instance is limited only to the clients that can access the [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoint configured for the instance. For instructions on setting up connectivity, see [Networking setup guidance](https://docs.cloud.google.com/memorystore/docs/valkey/networking#networking_setup_guidance).

Management of Memorystore for Valkey instances is secured using Identity and Access Management (IAM) role-based access control. For more information, see [Access control](https://docs.cloud.google.com/memorystore/docs/valkey/access-control).

## Encryption

All network data to and from Memorystore for Valkey is encrypted in transit at the network level according to Google Cloud's default [protection](https://docs.cloud.google.com/docs/security/encryption-in-transit) for any VM to VM traffic.

Memorystore for Valkey doesn't encrypt data in memory. Also, Memorystore for Valkey supports diskless replication. Unless you enable [persistence](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview), Memorystore for Valkey doesn't use disks during replication.

By enabling persistence, Memorystore for Valkey encrypts your data by default. However, if you want to control your encryption keys, then you can use [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/memorystore/docs/valkey/about-cmek) in Cloud Key Management Service (Cloud KMS) with CMEK-integrated services, including Memorystore for Valkey.

## Security best practices

We recommend that you access your Memorystore for Valkey instance by using trusted clients inside of the trusted environments. Don't expose the instance to the internet directly, or, in general, to an environment where untrusted clients can access the instance's TCP port or UNIX socket directly.

For example, if a web application uses an instance as a database, cache, or messaging system, then the clients inside of the frontend (the web side) of the application query the instance to generate pages or to perform operations that the user requests. In this case, the web application mediates access between the instance and the untrusted clients. These clients are the user browsers that access the web application.

We recommend that you mediate untrusted access to the instance by using a layer that does the following:

  * Implements access control lists (ACLs)
  * Validates user inputs
  * Decides which operations to perform against the instance



For more information about security from Valkey's point of view, see [Valkey security](https://valkey.io/topics/security/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
