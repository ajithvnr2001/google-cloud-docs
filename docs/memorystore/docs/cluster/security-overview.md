---
url: https://docs.cloud.google.com/memorystore/docs/cluster/security-overview/
title: Security overview \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:40.709628+00:00
---

# Security overview  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/security-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Security overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the security provided for your cluster in Memorystore for Redis Cluster.

A cluster isn't publicly accessible. Access to the cluster is limited only to the clients that can access the [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoint configured for the cluster. For instructions on setting up connectivity, see [Networking setup guidance](https://docs.cloud.google.com/memorystore/docs/cluster/networking#networking_setup_guidance).

Management of clusters is secured using Identity and Access Management (IAM) role-based access control. For more information, see [Access Control with IAM](https://docs.cloud.google.com/memorystore/docs/cluster/access-control).

### Encryption

All network data to and from Memorystore for Redis Cluster is encrypted in transit at the network level according to Google Cloud's default [protection](https://docs.cloud.google.com/docs/security/encryption-in-transit) for any VM to VM traffic.

Memorystore for Redis Cluster doesn't encrypt data in memory. Also, Memorystore for Redis Cluster supports diskless replication. Unless you enable [persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview), Memorystore for Redis Cluster doesn't use disks during replication.

By enabling persistence, Memorystore for Redis Cluster encrypts your data by default. However, if you want to control your encryption keys, then you can use [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek) in Cloud Key Management Service (Cloud KMS) with CMEK-integrated services, including Memorystore for Redis Cluster.

## Security best practices

We recommend that you access your cluster in Memorystore for Redis Cluster by using trusted clients inside of the trusted environments. Don't expose the cluster to the internet directly, or, in general, to an environment where untrusted clients can access the cluster's TCP port or UNIX socket directly.

For example, if a web application uses a cluster as a database, cache, or messaging system, then the clients inside of the frontend (the web side) of the application query the cluster to generate pages or to perform operations that the user requests. In this case, the web application mediates access between the cluster and the untrusted clients. These clients are the user browsers that access the web application.

We recommend that you mediate untrusted access to the cluster by using a layer that does the following:

  * Implements access control lists (ACLs)
  * Validates user inputs
  * Decides which operations to perform against the cluster



For more information about security from Redis' point of view, see [Redis security](https://redis.io/docs/latest/operate/oss_and_stack/management/security/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
