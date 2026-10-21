---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/analytics-hybrid-multicloud-pattern/
title: Analytics hybrid and multicloud pattern \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:45.311923+00:00
---

# Analytics hybrid and multicloud pattern  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/analytics-hybrid-multicloud-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Analytics hybrid and multicloud pattern Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-11-27 UTC

This document discusses that the objective of the analytics hybrid and multicloud pattern is to capitalize on the split between transactional and analytics workloads.

In enterprise systems, most workloads fall into these categories:

  * _Transactional_ workloads include interactive applications like sales, financial processing, enterprise resource planning, or communication.
  * _Analytics_ workloads include applications that transform, analyze, refine, or visualize data to aid decision-making processes.



Analytics systems obtain their data from transactional systems by either querying APIs or accessing databases. In most enterprises, analytics and transactional systems tend to be separate and loosely coupled. The objective of the _analytics hybrid and multicloud_ pattern is to capitalize on this pre-existing split by running transactional and analytics workloads in two different computing environments. Raw data is first extracted from workloads that are running in the private computing environment and then loaded into Google Cloud, where it's used for analytical processing. Some of the results might then be fed back to transactional systems.

The following diagram illustrates conceptually possible architectures by showing potential data pipelines. Each arrow represents a possible data movement and transformation pipeline option that can be based on [ETL](https://cloud.google.com/learn/what-is-etl) or ELT, depending on the available [data quality](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview) and targeted use case.

To move your data into Google Cloud and unlock value from it, use [data movement](https://cloud.google.com/data-movement) services, a complete suite of data ingestion, integration, and replication services.

![Data flowing from an on-premises or other cloud environment into Google Cloud, through ingest, pipelines, storage, analytics, into the application and presentation layer.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/hybrid-multicloud.svg)

As shown in the preceding diagram, connecting Google Cloud with on-premises environments and other cloud environments can enable various data analytics use cases, such as data streaming and database backups. To power the foundational transport of a hybrid and multicloud analytics pattern that requires a high volume of data transfer, Cloud Interconnect and [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) provide dedicated connectivity to on-premises and other cloud providers.

## Advantages

Running analytics workloads in the cloud has several key advantages:

  * Inbound traffic—moving data from your private computing environment or other clouds to Google Cloud—[might be free of charge](https://docs.cloud.google.com/vpc/network-pricing#general).
  * Analytics workloads often need to process substantial amounts of data and can be bursty, so they're especially well suited to being deployed in a public cloud environment. By dynamically scaling compute resources, you can quickly process large datasets while avoiding upfront investments or having to overprovision computing equipment.
  * Google Cloud provides a rich set of services to manage data throughout its entire lifecycle, ranging from initial acquisition through processing and analyzing to final visualization. 
    * Data movement services on Google Cloud provide a complete suite of products to move, integrate, and transform data seamlessly in different ways.
    * Cloud Storage is well suited for [building a data lake](https://cloud.google.com/blog/topics/developers-practitioners/architect-your-data-lake-google-cloud-data-fusion-and-composer).
  * Google Cloud helps you to modernize and optimize your data platform to break down data silos. Using a [data lakehouse](https://cloud.google.com/discover/what-is-a-data-lakehouse) helps to standardize across different storage formats. It can also provide the flexibility, scalability, and agility needed to help ensure that your data generates value for your business, rather than inefficiencies. For more information, see [BigLake](https://cloud.google.com/biglake).

  * [BigQuery Omni,](https://docs.cloud.google.com/bigquery/docs/omni-introduction) provides compute power that runs locally to the storage on AWS or Azure. It also helps you query your own data stored in Amazon Simple Storage Service (Amazon S3) or Azure Blob Storage. This multicloud analytics capability lets data teams break down data silos. For more information about querying data stored outside of BigQuery, see [Introduction to external data sources](https://docs.cloud.google.com/bigquery/docs/external-data-sources).




## Best practices

To implement the _analytics hybrid and multicloud_ architecture pattern, consider the following general best practices:

  * Use the [handover networking pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/handover-pattern) to enable the ingestion of data. If analytical results need to be fed back to transactional systems, you might combine both the handover and the [_gated egress_](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress) pattern.
  * Use [Pub/Sub](https://docs.cloud.google.com/pubsub) queues or [Cloud Storage](https://docs.cloud.google.com/storage) buckets to hand over data to Google Cloud from transactional systems that are running in your private computing environment. These queues or buckets can then serve as sources for data-processing pipelines and workloads.
  * To deploy ETL and ELT data pipelines, consider using [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion) or [Dataflow](https://docs.cloud.google.com/dataflow) depending on your specific use case requirements. Both are fully managed, cloud-first data processing services for building and managing data pipelines.
  * To discover, classify, and protect your valuable data assets, consider using Google Cloud [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection) capabilities, like [de-identification techniques](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data). These techniques let you mask, encrypt, and replace sensitive data—like personally identifiable information (PII)—using a randomly generated or pre-determined key, where applicable and compliant.
  * When you're performing an initial data transfer from your private computing environment to Google Cloud, choose the transfer approach that is best suited for your dataset size and available bandwidth. For more information, see [Migration to Google Cloud: Transferring your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets).

  * If data transfer or exchange between Google Cloud and other clouds is required for the long term with high traffic volume, you should evaluate using Google Cloud [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) to help you establish high-bandwidth dedicated connectivity between Google Cloud and other cloud service providers (available in certain [locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#locations)).

  * If encryption is required at the connectivity layer, various options are available based on the selected hybrid connectivity solution. These options include VPN tunnels, HA VPN over Cloud Interconnect, and [MACsec for Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#encryption).

  * Use consistent tooling and processes across environments. In an analytics hybrid scenario, this practice can help increase operational efficiency, although it's not a prerequisite.




[ Previous arrow_back  Partitioned multicloud pattern  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern)

[ Next Edge hybrid pattern  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/edge-hybrid-pattern)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-11-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-11-27 UTC."],[],[]] 
