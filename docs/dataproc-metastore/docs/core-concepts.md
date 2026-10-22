---
url: https://docs.cloud.google.com/dataproc-metastore/docs/core-concepts/
title: Dataproc Metastore core concepts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:43.075071+00:00
---

# Dataproc Metastore core concepts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/core-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore core concepts Stay organized with collections  Save and categorize content based on your preferences. 

Use the following concepts to help you understand how Dataproc Metastore works and the different features you can use with your service.

## Dataproc Metastore versions

When you create a Dataproc Metastore service, you can choose to use a _Dataproc Metastore 2 service_ or a _Dataproc Metastore 1 service_.

### Dataproc Metastore 2

Dataproc Metastore 2 uses a scaling factor to determine how many resources your service uses at a given time. After you create a Dataproc Metastore 2, you can scale the service up or down by modifying the scaling factor.

  * Dataproc Metastore 2 is the new generation of the service that offers horizontal scalability in addition to Dataproc Metastore features. For more information, see [features and benefits](https://docs.cloud.google.com/dataproc-metastore/docs/overview#why-use-Dataproc%20Metastore).

  * Dataproc Metastore 2 has a different pricing plan than Dataproc Metastore. For more information, see [pricing plans and scaling configurations](https://cloud.google.com/dataproc-metastore/pricing).




### Dataproc Metastore 1

Dataproc Metastore 1 uses service tiers to determine how many resources your service uses at a given time. Service tiers provide a predictable, predetermined amount of resources.

### Check your Dataproc Metastore version

You can check what version of Dataproc Metastore you're using in the Google Cloud console.

  * **Dataproc Metastore 2** : The configuration table contains the following value: **Edition Enterprise - Single Region**.
  * **Dataproc Metastore 1** : The configuration table contains one of the following values: **Tier: DEVELOPER** or **Tier: ENTERPRISE**.



## Common Dataproc Metastore terms

The following terms are used commonly throughout the Dataproc Metastore ecosystem and documentation.

#### Services

  * **Apache Hive**. Hive is a popular open source data warehouse system built on Apache Hadoop. Hive offers a SQL-like query language called HiveQL, which is used to analyze large, structured datasets.
  * **Apache Hive metastore**. The Hive metastore holds metadata about Hive tables, such as their schema and location.
  * **Managed Service for Apache Spark**. Managed Service for Apache Spark is a fast, easy-to-use, fully managed service on Google Cloud for running Apache Spark and Apache Hadoop workloads in a simple, cost-efficient way. After you create a Dataproc Metastore, you can connect to it from a Managed Service for Apache Spark cluster.
  * **Managed Service for Apache Spark cluster**. After you create a Dataproc Metastore service, you can connect to it from a Managed Service for Apache Spark cluster. You can also use Dataproc Metastore with various other clusters, such as self-managed Apache Hive, Apache Spark, or Presto clusters.
  * **Dataproc Metastore service**. The name of the metastore instance you create in Google Cloud. You can have one or many different metastore services in your implementation.
  * **Private Service Connect**. Private Service Connect lets you set up a private connection to Dataproc Metastore metadata across VPC networks. You can use it for networking as an alternative to VPC peering.
  * **VPC Service Controls**. VPC Service Controls improves your ability to mitigate the risk of data exfiltration from Google Cloud services by allowing you to create perimeters that protect the resources and data of services that you explicitly specify.



#### Concepts

  * **Tables**. All Hive applications have managed internal or unmanaged external tables that store your data.
  * **Hive warehouse directory**. The default location where managed table data is stored.
  * **Artifacts bucket**. A Cloud Storage bucket that is created in your project automatically with every metastore service that you create. This bucket can be used to store your service artifacts, such as exported metadata and managed table data. By default, the artifacts bucket stores the default warehouse directory of your Dataproc Metastore service.
  * **Endpoints**. A Dataproc Metastore service provides clients access to the stored Hive Metastore metadata through one or more network endpoints. Dataproc Metastore provides URIs for these endpoints.
  * **Endpoint protocols**. The over-the-wire network protocol used for communication between Dataproc Metastore and Hive Metastore clients. Dataproc Metastore supports Apache Thrift and gRPC endpoints.
  * **Metadata Federation**. A feature that lets you access metadata that is stored in multiple Dataproc Metastore instances.
  * **Auxiliary versions**. A feature that lets you connect multiple Hive client versions to the same Dataproc Metastore service.



## Hive metastore concepts

Using a Dataproc Metastore service requires that you understand basic Hive metastore concepts. For more information, see [Hive Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore).

## Network Requirements

The Dataproc Metastore service requires networking access to work correctly. For more information, see [Configure network requirements](https://docs.cloud.google.com/dataproc-metastore/docs/access-service).

## Project configurations

There are a number of possible project configurations you can use when deploying a Managed Service for Apache Spark cluster and a Dataproc Metastore service. For more information, see [cross-project deployment](https://docs.cloud.google.com/dataproc-metastore/docs/cross-project-deployment).

## What's next

  * [Create a service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Import metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
