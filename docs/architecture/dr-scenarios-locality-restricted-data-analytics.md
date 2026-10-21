---
url: https://docs.cloud.google.com/architecture/dr-scenarios-locality-restricted-data-analytics/
title: Disaster recovery use cases: locality-restricted data analytics applications \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:20:13.108430+00:00
---

# Disaster recovery use cases: locality-restricted data analytics applications  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/dr-scenarios-locality-restricted-data-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Disaster recovery use cases: locality-restricted data analytics applications Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-20 UTC

This document is part of a series that discusses [disaster recovery (DR)](https://docs.cloud.google.com/solutions/backup-dr) in Google Cloud. This document describes how to apply the locality restrictions from the document, [Architecting disaster recovery for locality-restricted workloads](https://docs.cloud.google.com/architecture/architecting-disaster-recovery-for-locality-restricted-workloads), to data analytics applications. Specifically, this document describes how the components that you use in a data analytics platform fit into a DR architecture that meets locality restrictions that your applications or data might be subject to.

The series consists of the following parts:

  * [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)
  * [Disaster recovery building blocks](https://docs.cloud.google.com/architecture/dr-scenarios-building-blocks)
  * [Disaster recovery scenarios for data](https://docs.cloud.google.com/architecture/dr-scenarios-for-data)
  * [Disaster recovery scenarios for applications](https://docs.cloud.google.com/architecture/dr-scenarios-for-applications)
  * [Architecting disaster recovery for locality-restricted workloads](https://docs.cloud.google.com/architecture/architecting-disaster-recovery-for-locality-restricted-workloads)
  * [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/architecture/disaster-recovery)
  * Disaster recovery use cases: locality-restricted data analytics applications (this document)



This document is intended for systems architects and IT managers. It assumes that you have the following knowledge and skills:

  * Basic familiarity with Google Cloud data analytics services such as [Dataflow](https://docs.cloud.google.com/dataflow), [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc), [Managed Service for Apache Airflow,](https://docs.cloud.google.com/composer) [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), [Cloud Storage](https://docs.cloud.google.com/storage), and [BigQuery](https://docs.cloud.google.com/bigquery).
  * Basic familiarity with Google Cloud networking services such as [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn).
  * Familiarity with disaster recovery planning.
  * Familiarity with [Apache Hive](https://hive.apache.org/) and [Apache Spark](https://spark.apache.org/).



## Locality requirements for a data analytics platform

Data analytics platforms are typically complex, multi-tiered applications that store data at rest. These applications produce events that are processed and stored in your analytics system. Both the application itself and the data stored in the system might be subject to locality regulations. These regulations vary not just across countries, but also across industry verticals. Therefore, you should have a clear understanding about [your data locality requirements](https://docs.cloud.google.com/architecture/architecting-disaster-recovery-for-locality-restricted-workloads#define_your_locality_requirements) before you start to design your DR architecture.

You can determine whether your data analytics platform has any locality requirements by answering the following two questions:

  * Does your application need to be deployed to a specific region?
  * Is your data at rest restricted to a specific region?



If you answer "no" to both questions, your data analytics platform doesn't have any locality-specific requirements. Because your platform doesn't have locality requirements, follow the DR guidance for compliant services and products outlined in the [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

However, if you answer "yes" to either of the questions, your application is locality-restricted. Because your analytics platform is locality-restricted, you must ask the following question: [Can you use encryption techniques to mitigate data-at-rest requirements?](https://docs.cloud.google.com/architecture/architecting-disaster-recovery-for-locality-restricted-workloads#define_your_locality_requirements)

If you're able to use encryption techniques, you can use the multi-regional and dual-regional services of Cloud External Key Manager and Cloud Key Management Service. You can then also follow the standard high availability and disaster recovery (HA/DR) techniques outlined in [Disaster recovery scenarios for data](https://docs.cloud.google.com/architecture/dr-scenarios-for-data).

If you are unable to use encryption techniques, you must use custom solutions or partner offerings for DR planning. For more information about techniques for addressing locality restrictions for DR scenarios, see [Architecting disaster recovery for locality-restricted workloads](https://docs.cloud.google.com/architecture/architecting-disaster-recovery-for-locality-restricted-workloads).

## Components in a data analytics platform

When you understand locality requirements, the next step is to understand the components that your data analytics platform uses. Some common components of data analytics platform are databases, data lakes, processing pipelines, and data warehouses, as described in the following list:

  * Google Cloud has a set of [database services](https://cloud.google.com/products/databases) that fit different use cases.
  * Data lakes, data warehouses, and processing pipelines can have slightly differing definitions. This document uses a set of definitions that reference Google Cloud services:

    * A [data lake](https://cloud.google.com/learn/what-is-a-data-lake) is a scalable and secure platform for ingesting and storing data from multiple systems. A typical data lake might use Cloud Storage as the central storage repository.
    * A processing pipeline is an end-to-end process that takes data or events from one or more systems, transforms that data or event, and loads it into another system. The pipeline could follow either an [extract, transform, and load (ETL) or extract, load, and transform (ELT) process](https://docs.cloud.google.com/architecture/dw2bq/dw-bq-data-pipelines#etl). Typically, the system into which the processed data is loaded is a data warehouse. Pub/Sub, Dataflow, and Managed Service for Apache Spark are commonly used components of a processing pipeline.
    * A [data warehouse](https://cloud.google.com/learn/what-is-a-data-warehouse) is an enterprise system used for analysis and reporting of data, which usually comes from an operational database. BigQuery is a commonly used data warehouse system running on Google Cloud.



Depending on the locality requirements and the data analytics components that you are using, the actual DR implementation varies. The following sections demonstrate this variation with two use cases.

## Batch use case: a periodic ETL job

The first use case describes a batch process in which a retail platform periodically collects sales events as files from various stores and then writes the files to a Cloud Storage bucket. The following diagram illustrates the data analytics architecture for this retailer's batch job.

![Architecture diagram of a batch use case that involves point-of-sales data.](https://docs.cloud.google.com/static/architecture/images/dr-scenarios-locality-restricted-data-analytics-batch.svg)

The architecture includes the following phases and components:

  * The **ingestion** phase consists of the stores sending their point-of-sale (POS) data to Cloud Storage. This ingested data awaits processing.
  * The **orchestration** phase uses Managed Airflow to orchestrate the end-to-end batch pipeline.
  * The **processing** phase involves an Apache Spark job running on a Managed Service for Apache Spark cluster. The Apache Spark job performs an ETL process on the ingested data. This ETL process provides business metrics.
  * The **data lake** phase takes the processed data and stores information in the following components: 
    * The processed data is commonly stored in Cloud Storage columnar formats such as [Parquet](https://parquet.apache.org/) and [ORC](https://orc.apache.org/) because these formats allow efficient storage and faster access for analytical workloads.
    * The metadata about the process data (such as databases, tables, columns, and partitions) is stored in the Hive metastore service supplied by [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/overview).



In locality-restricted scenarios, it might be difficult to provide redundant processing and orchestration capacity to maintain availability. Because the data is processed in batches, the processing and orchestration pipelines can be recreated, and batch jobs could be restarted after a disaster scenario is resolved. Therefore, for disaster recovery, the core focus is on recovering the actual data: the ingested POS data, the processed data stored in the data lake, and the metadata stored in the data lake.

### Ingestion into Cloud Storage

Your first consideration should be the locality requirements for the Cloud Storage bucket used to ingest the data from the POS system. Use this locality information when considering the following options:

  * If the locality requirements allow data at rest to reside in one of the multi-region or dual-region locations, choose the corresponding location type when you create the Cloud Storage bucket. The location type that you choose defines which Google Cloud regions are used to replicate your data at rest. If an outage occurs in one of the regions, data that resides in multi-region or dual-region buckets is still be accessible.
  * Cloud Storage also supports both [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) and [customer-supplied encryption keys (CSEK)](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys). Some locality rules allow data at rest to be stored in multiple locations when you use CMEK or CSEK for key management. If your locality rules allow the use of CMEK or CSEK, you can design your DR architecture to use Cloud Storage regions.
  * Your locality requirements might not permit you to use either location types or encryption-key management. When you can't use location types or encryption-key management, you can use the [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync) command to synchronize data to another location, such as on-premises storage or storage solutions from another cloud provider.



If a disaster occurs, the ingested POS data in the Cloud Storage bucket might have data that has not yet been processed and imported into the data lake. Alternatively, the POS data might not be able to be ingested into the Cloud Storage bucket. For these cases, you have the following disaster recovery options:

  * **Let the POS system retry.** In the event that the system is unable to write the POS data to Cloud Storage, the data ingestion process fails. To mitigate this situation, you can implement a [retry strategy](https://docs.cloud.google.com/storage/docs/retry-strategy) to allow the POS system to retry the data ingestion operation. Because Cloud Storage provides [high durability](https://docs.cloud.google.com/storage/docs/availability-durability), data ingestion and the subsequent processing pipeline will resume with little to no data loss after the Cloud Storage service resumes.

  * **Make copies of ingested data.** Cloud Storage supports both multi-region and dual-region [location types](https://docs.cloud.google.com/storage/docs/locations). Depending on your data locality requirements, you might be able to set up a multi-region or dual-region Cloud Storage bucket to increase data availability. You can also use tools like the `gcloud storage` Google Cloud CLI command to synchronize data between Cloud Storage and another location.




### Orchestration and processing of ingested POS data

In the architecture diagram for the batch use case, [Managed Airflow](https://docs.cloud.google.com/composer/docs/concepts/overview) carries out the following steps:

  * Validates that new files have been uploaded to the Cloud Storage ingestion bucket.
  * Starts an ephemeral Managed Service for Apache Spark cluster.
  * Starts an Apache Spark job to process the data.
  * Deletes the Managed Service for Apache Spark cluster at the end of the job.



Managed Airflow uses [directed acyclic graph (DAG)](https://docs.cloud.google.com/composer/docs/concepts/overview#workflows_dags_and_tasks) files that define these series of steps. These DAG files are stored in a Cloud Storage bucket that is not shown in the architecture diagram. In terms of dual-region and multi-region locality, the DR considerations for the DAG files bucket are the same as the ones discussed for the ingestion bucket.

Managed Service for Apache Spark clusters are ephemeral. That is, the clusters only exist for as long as the processing stage runs. This ephemeral nature means that you don't have to explicitly do anything for DR in regard to the Managed Service for Apache Spark clusters.

### Data lake storage with Cloud Storage

The Cloud Storage bucket that you use for the data lake has the same locality considerations as the ones discussed for the ingestion bucket: dual-region and multi-region considerations, the use of encryption, and the use of `gcloud storage rsync` gcloud CLI command.

When designing the DR plan for your data lake, think about the following aspects:

  * **Data size.** The volume of data in a data lake can be large. Restoring a large volume of data takes time. In a DR scenario, you need to consider the impact that the data lake's volume has on the amount of time that it takes to restore data to a point that meets the following criteria:

    * Your application is available.
    * You meet your [recovery time objective (RTO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) value.
    * You get the data checkpoint that you need to met your [recovery point objective (RPO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) value.

For the current batch use case, Cloud Storage is used for the data lake location and provides high durability. However, ransomware attacks have been on a rise. To ensure that you have the ability to recover from such attacks, it would be prudent to follow the best practices that are outlined in, [How Cloud Storage delivers 11 nines of durability](https://cloud.google.com/blog/products/storage-data-transfer/understanding-cloud-storage-11-9s-durability-target).

  * **Data dependency.** Data in data lakes are usually consumed by other components of a data analytics system such as a processing pipeline. In a DR scenario, the processing pipeline and the data on which it depends should share the same RTO. In this context, focus on how long you can have the system be unavailable.

  * **Data age.** Historical data might allow for higher RPO. This type of data might have already been analyzed or processed by other data analytics components and might have been persisted in another component that has its own DR strategies. For example, sales records that are exported to Cloud Storage are imported daily to BigQuery for analysis. With proper DR strategies for BigQuery, historical sales records that have been imported to BigQuery might have lower recovery objectives than those which haven't been imported.




### Data lake metadata storage with Dataproc Metastore

Dataproc Metastore is an [Apache Hive metastore](https://cwiki.apache.org/confluence/display/Hive/Design#Design-Metastore) that is fully managed, highly available, autohealing, and serverless. The metastore provides data abstraction and data discovery features. The metastore can be [backed up](https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata) and [restored](https://docs.cloud.google.com/dataproc-metastore/docs/restore-metadata) in the case of a disaster. The Dataproc Metastore service also lets you [export](https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata) and [import](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata) metadata. You can add a task to export the metastore and maintain an external backup along with your ETL job.

If you encounter a situation where there is a metadata mismatch, you can recreate the metastore from the data itself by using the [`MSCK`](https://spark.apache.org/docs/latest/sql-ref-syntax-ddl-repair-table.html) command.

## Streaming use case: change data capture using ELT

The second use case decribes a retail platform that uses change data capture (CDC) to update backend inventory systems and to track real-time sales metrics. The following diagram shows an architecture in which events from a transactional database, such as Cloud SQL, are processed and then stored in a data warehouse.

![Architecture diagram of a streaming use case that involves change data capture of retail data.](https://docs.cloud.google.com/static/architecture/images/dr-scenarios-locality-restricted-data-analytics-streaming.svg)

The architecture includes the following phases and components:

  * The ingestion phase consists of the incoming change events being pushed to Pub/Sub. As a message delivery service, Pub/Sub is used to reliably ingest and distribute streaming analytics data. Pub/Sub has the additional benefits of being both scalable and serverless.
  * The processing phase involves using Dataflow to perform an ELT process on the ingested events.
  * The data warehouse phase uses BigQuery to store the processed events. The merge operation inserts or updates a record in BigQuery. This operation allows the information stored in BigQuery to keep up to date with the transactional database.



While this CDC architecture doesn't rely on Managed Airflow, some CDC architectures require Managed Airflow to orchestrate the integration of the stream into batch workloads. In those cases, the Managed Airflow workflow implements integrity checks, backfills, and projections that can't be done in real time because of latency constraints. DR techniques for Managed Airflow are discussed in the batch processing use case discussed earlier in the document.

For a streaming data pipeline, you should consider the following when planning your DR architecture:

  * **Pipeline dependencies.** Processing pipelines take input from one or more systems (the sources). Pipelines then process, transform, and store these inputs into some other systems (the sinks). It's important to design your DR architecture to achieve your end-to-end RTO. You need to ensure that the RPO of the data sources and sinks allow you to meet the RTO. In addition to designing your cloud architecture to meet your locality requirements, you'll also need to design your originating CDC sources to allow your end-to-end RTO to be met.
  * **Encryption and locality.** If encryption lets you mitigate locality restrictions, you can use [Cloud KMS](https://cloud.google.com/security/products/security-key-management), to attain the following goals: 
    * Manage your own encryption keys.
    * Take advantage of the encryption capability of individual services.
    * Deploy services in regions that would otherwise be not available to use due to locality restrictions.
  * **Locality rules on data in motion.** Some locality rules might apply only to data at rest but not to data in motion. If your locality rules don't apply to data in motion, design your DR architecture to use resources in other regions to improve the recovery objectives. You can supplement the regional approach by integrating encryption techniques.



### Ingestion into Pub/Sub

If you don't have locality restrictions, you can publish messages to the [global Pub/Sub endpoint](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#service_endpoints). Global Pub/Sub endpoints are visible and accessible from any Google Cloud location.

If your locality requirements allow the use of encryption, it's possible to configure Pub/Sub to achieve a similar level of high availability as global endpoints. Although Pub/Sub messages are encrypted with Google-owned and Google-managed encryption keys by default, you can [configure Pub/Sub to use CMEK](https://docs.cloud.google.com/pubsub/docs/encryption#using-cmek) instead. By using Pub/Sub with CMEK, you are able to meet locality rules about encryption while still maintaining high availability.

Some locality rules require messages to stay in a specific location even after encryption. If your locality rules have this restriction, you can specify the [message storage policy](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) of a Pub/Sub topic and restrict it to a region. If you use this message storage approach, messages that are published to a topic are never persisted outside of the set of Google Cloud regions that you specify. If your locality rules allow more than one Google Cloud region to be used, you can increase service availability by enabling those regions in the Pub/Sub topic. You need to be aware that implementing a message storage policy to restrict Pub/Sub resource locations does come with [trade-offs concerning availability](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction#performance_and_availability_implications).

A Pub/Sub subscription lets you store unacknowledged messages for up to 7 days without any restrictions on the number of messages. If your service level agreement allows delayed data, you can buffer the data in your Pub/Sub subscription if the pipelines stop running. When the pipelines are running again, you can process the backed-up events. This design has the benefit of having a low RPO. For more information about the resource limits for Pub/Sub, see [resource limits for Pub/Sub quotas](https://docs.cloud.google.com/pubsub/quotas#resource_limits).

### Event processing with Dataflow

Dataflow is a managed service for executing a wide variety of data processing patterns. The [Apache Beam SDK](https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status) is an open source programming model that lets you develop both batch and streaming pipelines. You create your pipelines with an Apache Beam program and then run them on the Dataflow service.

When designing for locality restrictions, you need to consider where your sources, sinks, and temporary files are located. If these file locations are outside of your job's region, your data might be sent across regions. If your locality rules allow data to be processed in a different location, design your DR architecture to deploy workers in other Google Cloud regions to provide high availability.

If your locality restrictions limit processing to a single location, you can create a Dataflow job that is restricted to a specific region or zone. When you submit a Dataflow job, you can specify the [regional endpoint, worker region, and worker zone](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints#using_regional_endpoints) parameters. These parameters control where workers are deployed and where job metadata is stored.

Apache Beam provides a framework that allows pipelines to be executed across various runners. You can design your DR architecture to take advantage of this capability. For example, you might design a DR architecture to have a backup pipeline that runs on your local on-premises Spark cluster by using [Apache Spark Runner](https://beam.apache.org/documentation/runners/spark/). For information about whether a specific runner is capable of carrying out a certain pipeline operation, see [Beam Capability Matrix](https://beam.apache.org/documentation/runners/capability-matrix/).

If encryption lets you mitigate locality restrictions, you can use [CMEK in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys) to both encrypt pipeline state artifacts, and access sources and sinks that are protected with Cloud KMS keys. Using encryption, you can design a DR architecture that uses regions that would otherwise be not available due to locality restrictions.

### Data warehouse built on BigQuery

Data warehouses support analytics and decision-making. Besides containing an analytical database, data warehouses contain multiple analytical components and procedures.

When designing the DR plan for your data warehouse, think about the following characteristics:

  * **Size.** Data warehouses are much larger than online transaction processing (OLTP) systems. It's not uncommon for data warehouses to have terabytes to petabytes of data. You need to consider how long it would take to restore this data to achieve your RPO and RTO values. When planning your DR strategy, you must also factor in the cost associated with recovering terabytes of data. For more information about DR mitigation techniques for BigQuery, see the BigQuery information in the section on [backup and recovery mechanisms for the managed database services on Google Cloud](https://docs.cloud.google.com/architecture/dr-scenarios-for-data#managed-database-services-on-gcp).

  * **Availability.** When you create a BigQuery dataset, you select a location in which to store your data: [regional](https://docs.cloud.google.com/bigquery/docs/locations#regional-locations) or [multi-region](https://docs.cloud.google.com/bigquery/docs/locations#multi-regional-locations). A regional location is a single, specific geographical location, such as Iowa (`us-central1`). A multi-region location is a large geographic area, such as the United States (US) or Europe (EU), that contains two or more geographic places.

**Note:** In BigQuery, a multi-region location does not provide cross-region replication nor regional redundancy. Data will be stored in a single region within the geographic location.

When designing your DR plan to meet locality restrictions, the failure domain (that is, whether the failure occurs at the machine level, zonal, or regional) will have a direct impact on you meeting your defined RTO. For more information about these failure domains and how they affect availability, see [Availability and durability of BigQuery](https://docs.cloud.google.com/bigquery/docs/availability).

  * **Nature of the data.** Data warehouses contain historic information, and most of the older data is often static. Many data warehouses are designed to be [append-only](https://wikipedia.org/wiki/Append-only). If your data warehouse is append-only, you may be able to achieve your RTO by restoring just the data that is being appended. In this approach, you backup just this appended data. If there is a disaster, you'll then be able to restore the appended data and have your data warehouse available to use, but with a subset of the data.

  * **Data addition and update pattern.** Data warehouses are typically updated using ETL or ELT patterns. When you have controlled update paths, you can reproduce recent update events from alternative sources.




Your locality requirements might limit whether you can use a single region or multiple regions for your data warehouse. Although BigQuery datasets can be regional, multi-region storage is the simplest and most cost-effective way to ensure the availability of your data if a disaster occurs. If multi-region storage is not available in your region, but you can use a different region, use the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/copying-datasets#setting_up_a_dataset_copy) to copy your dataset to a different region. If you can use encryption to mitigate the locality requirements, you can manage your own encryption keys with [Cloud KMS and BigQuery](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption).

If you can use only one region, consider backing up the BigQuery tables. The most cost-effective solution to backup tables is to use [BigQuery exports](https://docs.cloud.google.com/bigquery/docs/exporting-data). Use [Cloud Scheduler](https://docs.cloud.google.com/scheduler) or [Managed Airflow](https://docs.cloud.google.com/composer) to periodically schedule an export job to write to Cloud Storage. You can use [formats](https://docs.cloud.google.com/bigquery/docs/exporting-data#export_formats_and_compression_types) such as Avro with SNAPPY compression or JSON with GZIP compression. While you are designing your export strategies, take note of the [limits](https://docs.cloud.google.com/bigquery/quotas#export_jobs) on exports.

You might also want to store BigQuery backups in columnar formats such as Parquet and ORC. These provide high compression and also allow interoperability with many open source engines, such as Hive and Presto, that you might have in your on-premises systems. The following diagram outlines the process of exporting BigQuery data to a columnar format for storage in an on-premises location.

![Architecture diagram showing the exporting of BigQuery data into columnar storage for disaster recovery.](https://docs.cloud.google.com/static/architecture/images/dr-scenarios-locality-restricted-data-analytics-bqexport.svg)

Specifically, this process of exporting BigQuery data to an on-premises storage location involves the following steps:

  * The BigQuery data is sent to an Apache Spark job on Managed Service for Apache Spark. The use of the Apache Spark job permits [schema evolution](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#schema-merging).
  * After the Managed Service for Apache Spark job has processed the BigQuery files, the processed files are written to Cloud Storage and then transferred to an on-premises DR location.
  * Cloud Interconnect is used to connect your Virtual Private Cloud network to your on-premises network.
  * The transfer to the on-premises DR location can occur through the Spark job.



If your warehouse design is append-only and is partitioned by date, you need to [create a copy of the required partitions](https://docs.cloud.google.com/bigquery/docs/tables#creating_a_table_from_a_query_result) in a new table before you [run a BigQuery export job](https://docs.cloud.google.com/bigquery/docs/exporting-data#exporting_table_data) on the new table. You can then use a tool such as `gcloud storage` gcloud CLI command to transfer the updated files to your backup location on-premises or in another cloud. (Egress charges might apply when you transfer data out of Google Cloud.)

For example, you have a sales data warehouse that consists of an append-only `orders` table in which new orders are appended to the partition that represents the current date. However, a return policy might allow items to be returned within 7 days. Therefore, records in the `orders` table from within the last 7 days might be updated. Your export strategies need to take the return policy into account. In this example, any export job to backup the `orders` table needs to also export the partitions representing orders within the last 7 days to avoid missing updates due to returns.

## What's next

  * Read other articles in this DR series: 
    * [Disaster recovery planning guide](https://docs.cloud.google.com/solutions/dr-scenarios-planning-guide)
    * [Disaster recovery building blocks](https://docs.cloud.google.com/solutions/dr-scenarios-building-blocks)
    * [Disaster recovery scenarios for data](https://docs.cloud.google.com/solutions/dr-scenarios-for-data)
    * [Disaster recovery scenarios for applications](https://docs.cloud.google.com/solutions/dr-scenarios-for-applications)
    * [Architecting disaster recovery for locality-restricted workloads](https://docs.cloud.google.com/architecture/architecting-disaster-recovery-for-locality-restricted-workloads)
    * [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/architecture/disaster-recovery)
  * Read the whitepaper: Learn about [data residency, operational transparency, and privacy for European customers on Google Cloud](https://services.google.com/fh/files/misc/googlecloud_european_commitments_whitepaper.pdf).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Grace Mollison](https://www.linkedin.com/in/grace-mollison-6296614) | Solutions Lead
  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-20 UTC."],[],[]] 
