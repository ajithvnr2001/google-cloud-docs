---
url: https://docs.cloud.google.com/dataproc-metastore/docs/overview/
title: Dataproc Metastore overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:39.544651+00:00
---

# Dataproc Metastore overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore overview Stay organized with collections  Save and categorize content based on your preferences. 

Dataproc Metastore is a fully managed [Apache Hive metastore](https://cwiki.apache.org/confluence/display/Hive/Design#Design-Metastore) (HMS) that runs on Google Cloud. An HMS is the established standard in the open source big data ecosystem for managing technical metadata, such as schemas, partitions, and column statistics in a relational database.

Dataproc Metastore is highly available, auto-healing, and serverless. Use it to manage [data lake](https://cloud.google.com/learn/what-is-a-data-lake) metadata and provide interoperability between the various data processing engines and tools that you're using.

## How Dataproc Metastore works

You can use a Dataproc Metastore service by connecting it to a Managed Service for Apache Spark cluster. A Managed Service for Apache Spark cluster includes components that rely on an HMS to drive query planning and execution.

This integration lets you keep your table information between jobs or make metadata available to other clusters and other processing engines.

For example, implementing a metastore might help you designate that a subset of your files contains revenue data, as opposed to manually tracking the filenames. In this case, you can define a table for those files and store the metadata in Dataproc Metastore. After, you can connect it to a Managed Service for Apache Spark cluster and query the table for information using Hive, Spark SQL, or other query services.

**Dataproc Metastore versions**

When you create a Dataproc Metastore service, you can choose to use a _Dataproc Metastore 2 service_ or a _Dataproc Metastore 1 service_.

  * Dataproc Metastore 2 is the new generation of the service that offers horizontal scalability in addition to Dataproc Metastore 1 features. For more information, see features and benefits.

  * Dataproc Metastore 2 has a different pricing plan than Dataproc Metastore. For more information, see [pricing plans and scaling configurations](https://cloud.google.com/dataproc-metastore/pricing).




### Common use cases

All use cases listed in this section are supported by Dataproc Metastore 2 and Dataproc Metastore 1, unless otherwise noted.

  * **Assign meaning to your data.** Create a centralized metadata repository that's shared among many ephemeral Managed Service for Apache Spark clusters. Use different open source software (OSS) engines, such as [Apache Hive](https://hive.apache.org) , [Apache Spark](https://spark.apache.org/), and [Presto](https://prestodb.io/).

  * **Build a unified view of your data.** Provide interoperability between Google Cloud services, such as Managed Service for Apache Spark, Knowledge Catalog, and BigQuery, or use other open source-based partner offerings on Google Cloud.




### Features and benefits

All features listed in this section are supported by Dataproc Metastore 2 and Dataproc Metastore 1, unless otherwise noted.

  * **OSS compatibility**. Connect to your existing data processing engines, such as Apache Hive, Apache Spark, and Presto.

  * **Management**. Create or update a metastore within minutes, complete with fully configured monitoring and operation tasks.

  * **Integration**. Integrate with other Google Cloud products, such as using BigQuery as the source of metadata for a Managed Service for Apache Spark cluster.

  * **Built-in security**. Use established Google Cloud security protocols, such as [Identity and Access Management (IAM)](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control) and [Kerberos authentication](https://docs.cloud.google.com/dataproc-metastore/docs/configure-kerberos).

  * **Simple import**. Import existing metadata stored in an external Hive Metastore into a Dataproc Metastore service.

  * **Automatic Backups**. Configure automatic metastore backups to help avoid data loss.

  * **Performance monitoring**. Set performance tiers to dynamically respond to highly intensive workloads and spikes, without pre-warming or caching.

  * **High availability (HA)**.

    * **Dataproc Metastore 2.** Provides zonal high availability (HA) without requiring any specific configuration or on-going management. This is accomplished by automatically replicating backend databases and HMS servers across multiple zones in the region you choose. In addition to Zonal HA, Dataproc Metastore 2 supports regional HA and Disaster Recovery (DR).
    * **Dataproc Metastore 1.** By default, provides zonal high availability (HA) without requiring any specific configuration or on-going management. This is accomplished by automatically replicating backend databases and HMS servers across multiple zones in the region you choose.

For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

  * **Scalability**.

    * **Dataproc Metastore 2.** Use a horizontal scaling factor to determine how many resources your service needs to use at a given time. The scaling factor can be manually controlled or set to autoscale when needed.
    * **Dataproc Metastore 1.** Choose between a developer tier or enterprise tier when you set up your service. This tier determines how many resources your service needs to use at a given time.
  * **Support**. Benefit from standard Google Cloud SLAs and support channels.




## Integrations with Google Cloud

All integrations listed in this section are supported by Dataproc Metastore 1 and Dataproc Metastore 2, unless otherwise noted.

  * **Managed Service for Apache Spark.** Connect to a Managed Service for Apache Spark cluster, so you can serve metadata for OSS big data workloads.
  * **BigQuery.** Query BigQuery datasets in your Managed Service for Apache Spark workloads.
  * **Knowledge Catalog.** Query structured and semi-structured data discovered in a Knowledge Catalog lake.
  * **Data Catalog.** Sync Dataproc Metastore with Data Catalog to enable search and discovery of metadata.
  * **Logging and Monitoring.** Integrate Dataproc Metastore with Cloud Monitoring and Logging products.
  * **Authentication and IAM.** Rely on standard OAuth authentication used by other Google Cloud products, which supports using granular Identity and Access Management roles to enable access control for individual resources.



## Next steps

  * Get started with the quickstart guide, [Deploying a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster).
  * Understand [Dataproc Metastore pricing](https://cloud.google.com/dataproc-metastore/pricing).
  * Understand [quotas and limits for Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/quotas).
  * Read the [Dataproc Metastore release notes](https://docs.cloud.google.com/dataproc-metastore/docs/release-notes).
  * Access Dataproc Metastore using the [Google Cloud console](https://console.cloud.google.com/dataproc/metastore), the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/metastore) or with the [Dataproc Metastore API](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
