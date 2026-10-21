---
url: https://docs.cloud.google.com/architecture/framework/sustainability/optimize-storage/
title: Optimize data and storage for sustainability \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:22.432796+00:00
---

# Optimize data and storage for sustainability  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/sustainability/optimize-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Optimize data and storage for sustainability Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-28 UTC

This principle in the sustainability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability) provides recommendations to help you optimize the energy efficiency and carbon footprint for your storage resources in Google Cloud.

## Principle overview

Stored data isn't a passive resource. Energy is consumed and carbon emissions occur throughout the lifecycle of data. Every gigabyte of stored data requires physical infrastructure that's continuously powered, cooled, and managed. To achieve sustainable cloud architecture, treat data as a valuable but environmentally costly asset and prioritize proactive data governance.

Your decisions about data retention, quality, and location can help you achieve substantial reductions in cloud costs and energy consumption. Minimize the data that you store, optimize where and how data you store data, and implement automated deletion and archival strategies. When you reduce data clutter, you improve system performance and fundamentally reduce the long-term environmental footprint of your data.

## Recommendations

To optimize your data lifecycle and storage resources for sustainability, consider the recommendations in the following sections.

### Prioritize high-value data

Stored data that's unused, duplicated, or obsolete continues to consume energy to power the underlying infrastructure. To reduce the storage-related carbon footprint, use the following techniques.

#### Identify and eliminate duplication

Establish policies to prevent the needless replication of datasets across multiple Google Cloud projects or services. Use central data repositories like [BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro) or [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets) as single sources of truth and grant appropriate access to these repositories.

#### Remove shadow data and dark data

_Dark data_ is data for which the utility or owner is unknown. _Shadow data_ means unauthorized copies of data. Scan your storage systems and find dark data and shadow data by using a data discovery and cataloging solution like [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction). Regularly audit these findings and implement a process for archival or deletion of dark and shadow data as appropriate.

#### Minimize the data volume for AI workloads

Store only the features and processed data that are required for model training and serving. Where possible, use techniques like data sampling, aggregation, and synthetic data generation to achieve model performance without relying on massive raw datasets.

#### Integrate data quality checks

Implement automatic data validation and data cleaning pipelines by using services like [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview), [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview), or Knowledge Catalog at the point of data ingestion. Low-quality data causes wasted storage space. It also leads to unnecessary energy consumption when the data is used later for analytics or AI training.

#### Review the value density of data

Periodically review high-volume datasets like logs and IoT streams. Determine whether any data can be summarized, aggregated, or down-sampled to maintain the required information density and reduce the physical storage volume.

#### Critically evaluate the need for backups

Assess the need for backups of data that you can regenerate with minimal effort. Examples of such data include intermediate ETL results, ephemeral caches, and training data that's derived from a stable, permanent source. Retain backups for only the data that is unique or expensive to recreate.

### Optimize storage lifecycle management

Automate the storage lifecycle so that when the utility of data declines, the data is moved to an energy-efficient storage class or retired, as appropriate. Use the following techniques.

#### Select an appropriate Cloud Storage class

Automate the transition of data in Cloud Storage to lower-carbon storage classes based on access frequency by using [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle).

  * Use Standard storage for only actively used datasets, such as current production models.
  * Transition data such as older AI training datasets or less-frequently accessed backups to Nearline or Coldline storage.
  * For long-term retention, use Archive storage, which is optimized for energy efficiency at scale.



#### Implement aggressive data lifecycle policies

Define clear, automated time to live (TTL) policies for non-essential data, such as log files, temporary model artifacts, and outdated intermediate results. Use lifecycle rules to automatically delete such data after a defined period.

#### Mandate resource tagging

Mandate the use of consistent resource tags and labels for all of your Cloud Storage buckets, BigQuery datasets, and persistent disks. Create tags that indicate the data owner, purpose of the data, and the retention period. Use Organization Policy Service constraints to ensure that required tags, such as retention period, are applied to resources. Tags let you automate lifecycle management, create granular FinOps reports, and produce carbon emissions reports.

#### Right-size and deprovision compute storage

Regularly audit persistent disks that are attached to Compute Engine instances and ensure that the disks aren't over-provisioned. Use snapshots only when they are necessary for backup. Delete old, unused snapshots. For databases, use data retention policies to reduce the size of the underlying persistent disks.

#### Optimize the storage format

For storage that serves analytics workloads, prefer compressed, columnar formats like Parquet or optimized Avro over row-based formats like JSON or CSV. Columnar storage significantly reduces physical disk-space requirements and improves the read efficiency. This optimization helps to reduce energy consumption for the associated compute and I/O operations.

### Optimize regionality and data movement

The physical location and movement of your data affect the consumption of network resources and the energy required for storage. Optimize data regionality by using the following techniques.

#### Select low-carbon storage regions

Depending on your compliance requirements, store data in Google Cloud regions that use a higher percentage of carbon-free energy (CFE) or that have lower grid carbon intensity. Restrict the creation of storage buckets in high-carbon regions by using the [resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) Organization Policy constraint. For information about CFE and carbon-intensity data for Google Cloud regions, see [Carbon-free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).

#### Minimize replication

Replicate data across regions only to meet mandatory disaster recovery (DR) or high-availability (HA) requirements. Cross-region and multi-region replication operations significantly increase the energy cost and carbon footprint of your data.

#### Optimize data processing locations

To reduce energy consumption for network data transfer, deploy compute-intensive workloads like AI training and BigQuery processing in the same region as the data source.

#### Optimize data movement for your partners and customers

To move large volumes of data across cloud services, locations, and providers, encourage your partners and customers to use [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) or data-sharing APIs. Avoid mass data dumps. For public datasets, use [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) buckets to shift the data transfer and processing costs and the environmental impact to end users.

[ Previous arrow_back  Develop energy-efficient software  ](https://docs.cloud.google.com/architecture/framework/sustainability/energy-efficient-software)

[ Next Continuously measure and improve  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/sustainability/continuously-measure-improve)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-28 UTC."],[],[]] 
