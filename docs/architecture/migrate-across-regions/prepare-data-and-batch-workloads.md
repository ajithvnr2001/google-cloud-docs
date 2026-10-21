---
url: https://docs.cloud.google.com/architecture/migrate-across-regions/prepare-data-and-batch-workloads/
title: Migrate across Google Cloud regions: Prepare data and batch workloads for migration across regions \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:56:51.543559+00:00
---

# Migrate across Google Cloud regions: Prepare data and batch workloads for migration across regions  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migrate-across-regions/prepare-data-and-batch-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate across Google Cloud regions: Prepare data and batch workloads for migration across regions Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-02 UTC

This document describes how to design a data platform on Google Cloud to minimize the impact of a future expansion to other [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) or of a region-to-region migration. This document is part of a series that helps you to understand the impact of expanding your data platform to another region. It helps you learn how to do the following:

  * Prepare to move data and data pipelines.
  * Set up checks during the migration phases.
  * Create a flexible migration strategy by separating data storage and data computation.



The guidance in this series is also useful if you didn't plan for a migration across regions or for an expansion to multiple regions in advance. In this case, you might need to spend additional effort to prepare your infrastructure, workloads, and data for the migration across regions and for the expansion to multiple regions.

This document is part of a series:

  * [Get started](https://docs.cloud.google.com/architecture/migrate-across-regions)
  * [Design resilient single-region environments on Google Cloud](https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments)
  * [Architect your workloads](https://docs.cloud.google.com/architecture/migrate-across-regions/architect-workloads)
  * Prepare batch data pipelines for a migration across regions (this document)



This series assumes that you've read and are familiar with the following documents:

  * [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started): describes the general migration framework that you follow in this migration.
  * [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets): describes general concerns around moving data between regions, such as network bandwidth, cost, and security.



The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

During each migration step, you follow the phases defined in [Migration to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#the_migration_path):

  1. Assess and discover your workloads.
  2. Plan and build a foundation.
  3. Deploy your workloads.
  4. Optimize your environment.



## The modern data platform on Google Cloud

This section describes the different parts of a modern data platform, and how they're usually constructed in Google Cloud. Data platforms as a general concept can be divided into two sections:

  * The _data storage_ layer is where data is saved. The data that you're saving might be in the form of files where you manage actual bytes on a file system like Hadoop Distributed File System (HDFS) or Cloud Storage, or you might use a domain-specific language (DSL) to manage the data in a database management system.
  * The _data computation_ layer is any data processing that you might activate on top of the storage system. As with the storage layer, there are many possible implementations, and some data storage tools also handle data computation. The role of the data computation layer in the platform is to load data from the storage layer, process the data, and then save the results to a target system. The target system can be the source storage layer.



Some data platforms use multiple storage systems for their data storage layer, and multiple data computation systems for their data processing layer. In most cases, the data storage layer and the data computation layer are separated. For example, you might have implemented your data storage layer using these Google Cloud services:

  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [BigQuery storage](https://docs.cloud.google.com/bigquery/docs/storage_overview)
  * [Cloud SQL](https://docs.cloud.google.com/sql)
  * [Spanner](https://docs.cloud.google.com/spanner)
  * [Bigtable](https://docs.cloud.google.com/bigtable)



You might have implemented the data computation layer using other Google Cloud services like these:

  * [Dataflow](https://cloud.google.com/dataflow)
  * [Managed Service for Apache Spark](https://cloud.google.com/dataproc)
  * [BigQuery](https://cloud.google.com/bigquery)
  * Custom workloads on [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) or [Compute Engine](https://cloud.google.com/compute)
  * [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform/notebooks) or [Colaboratory](https://colab.google/)



To reduce the time and latency of communication, the cost of outbound data transfer, and the number of I/O operations between the storage layer and the computation layer, we recommend that you store the data in the same zone that you process the data in.

We also recommend that you keep your data storage layer separate from your data computation layer. Keeping these layers separate improves your flexibility in changing computation layers and migrating data. Keeping the layers separate also reduces your resource use because you don't have to keep the computation layer running all the time. Therefore, we recommend that you deploy your data storage and data computation on separate platforms in the same zone and region. For example, you can move your data storage from HDFS to Cloud Storage and use a Managed Service for Apache Spark cluster for computation.

## Assess your environment

In the assessment phase, you determine the requirements and dependencies to migrate the batch data pipelines that you've deployed:

  1. Build a comprehensive inventory of your data pipelines.
  2. Catalog your pipelines according to their properties and dependencies.
  3. Train and educate your teams on Google Cloud.
  4. Build an experiment and proof of concept on Google Cloud.
  5. Calculate the total cost of ownership (TCO) of the target environment.
  6. Choose the workloads that you want to migrate first.



For more information about the assessment phase and these tasks, see [Migration to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads). The following sections are based on the information in that document.

### Build your inventories

To scope your migration, you must understand the data platform environment where your data pipelines are deployed:

  1. Create an inventory of your _data infrastructure_ —the different storage layers and different computation layers that you're using for data storage and batch data processing.
  2. Create an inventory of the data pipelines that are scheduled to be migrated.
  3. Create an inventory of the datasets that are being read by the data pipelines and that need to be migrated.



To build an inventory of your data platform, consider the following for each part of the data infrastructure:

  * **Storage layers**. Along with standard storage platforms like Cloud Storage, consider other storage layers such as databases like Firebase, BigQuery, Bigtable, and Postgres, or other clusters like Apache Kafka. Each storage platform has its own strategy and method to complete migration. For example, Cloud Storage has data migration services, and a database might have a built-in migration tool. Make sure that each product that you're using for data storage is available to you in your target environment, or that you have a compatible replacement. Practice and verify the technical data transfer process for each of the involved storage platforms.
  * **Computation layers**. For each computation platform, verify the deployment plan and verify any configuration changes that you might have made to the different platforms.
  * **Network latency**. Test and verify the network latency between the source environment and the target environment. It's important for you to understand how long it will take for the data to be copied. You also need to test the network latency from clients and external environments (such as an on-premises environment) to the target environment in comparison to the source environment.
  * **Configurations and deployment**. Each data infrastructure product has its own setup methods. Take inventory of the custom configurations that you've made for each component, and which components you're using the default versions of for each platform (for example, which Managed Service for Apache Spark version or Apache Kafka version you're using). Make sure that those configurations are deployable as part of your automated deployment process.

You need to know how each component is configured because computational engines might behave differently when they're configured differently—particularly if the processing layer framework changes during the migration. For example, if the target environment is running a different version of Apache Spark, some configurations of the Spark framework might have changed between versions. This kind of configuration change can cause changes in outputs, serializations, and computation.

During the migration, we recommend that you use automated deployments to ensure that versions and configurations stay the same. If you can't keep versions and configurations the same, then make sure to have tests that validate the data outputs that the framework calculates.

  * **Cluster sizes**. For self-managed clusters, such as a long-living Managed Service for Apache Spark cluster or an Apache Kafka cluster running on Compute Engine, note the number of nodes and CPUs, and the memory for each node in the clusters. Migrating to another region might result in a change to the processor that your deployment uses. Therefore, we recommend that you profile and optimize your workloads after you deploy the migrated infrastructure to production. If a component is fully managed or serverless (for example Dataflow), the sizing will be part of each individual job, and not part of the cluster itself.




The following items that you assess in your inventory focus on the data pipelines:

  * **Data sources and sinks**. Make sure to account for the sources and sinks that each data pipeline uses for reading and writing data.
  * **Service Level Agreements (SLAs) and Service Level Objectives (SLOs)**. Batch data pipelines SLAs and SLOs are usually measured in time to completion, but they can also be measured in other ways, such as compute power used. This business metadata is important in driving business continuity and disaster recovery plan processes (BCDR), such as failing over a subset of your most critical pipelines to another region in the event of a zonal or regional failure.
  * **Data pipelines dependencies**. Some data pipelines rely on data that is generated by another data pipeline. When you split pipelines into migration sprints, make sure to consider data dependencies.
  * **Datasets generated and consumed**. For each data pipeline, identify datasets that the pipeline consumes, and which datasets it generates. Doing so can help you to identify dependencies between pipelines and between other systems or components in your overall architecture.



The following items that you assess in your inventory focus on the datasets to be migrated:

  * **Datasets**. Identify the datasets that need to be migrated to the target environment. You might consider some historical data as not needed for migration, or to be migrated at a different time, if the data is archived and isn't actively used. By defining the scope for the migration process and the migration sprints, you can reduce risks in the migration.
  * **Data sizes**. If you plan to compress files before you transfer them, make sure to note the file size before and after compression. The size of your data will affect the time and cost that's required to copy the data from the source to the destination. Considering these factors will help you to choose between downtime strategies, as described later in this document.
  * **Data structure**. Classify each dataset to be migrated and make sure that you understand whether the data is structured, semi-structured, or unstructured. Understanding data structure can inform your strategy for how to verify that data is migrated correctly and completely.



### Complete the assessment

After you build the inventories related to your Kubernetes clusters and workloads, complete the rest of the activities of the assessment phase in [Migration to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads).

## Plan and build your foundation

The plan and build phase of your migration to Google Cloud consists of the following tasks:

  1. Build a resource hierarchy.
  2. Configure Identity and Access Management (IAM).
  3. Set up billing.
  4. Set up network connectivity.
  5. Harden your security.
  6. Set up logging, monitoring, and alerting.



For more information about each of these tasks, see [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation).

## Migrate data and data pipelines

The following sections describes some of the aspects of the plan for migrating data and batch data pipelines. It defines some concepts around the characteristics of data pipelines that are important to understand when you create the migration plan. It also discusses some data testing concepts that can help increase your confidence in the data migration.

### Migration plan

In your migration plan, you need to include time to complete the data transfer. Your plan should account for network latency, time to test the data completeness and get any data that failed to migrate, and any network costs. Because data will be copied from one region to another, your plan for network costs should include inter-region network costs.

We recommend that you divide the different pipelines and datasets into sprints and migrate them separately. This approach helps to reduce the risks for each migration sprint, and it allows for improvements in each sprint. To improve your migration strategy and uncover issues early, we recommend that you prioritize smaller, non-critical workloads, before you migrate larger, more critical workloads.

Another important part of a migration plan is to describe the strategy, dependencies, and nature of the different data pipelines from the computation layer. If your data storage layer and data computation layer are built on the same system, we recommend that you monitor the performance of the system while data is being copied. Typically, the act of copying large amounts of data can cause I/O overhead on the system and degrade performance in the computation layer. For example, if you run a workload to extract data from a Kafka cluster in a batch fashion, the extra I/O operations to read large amounts of data can cause a degradation of performance on any active data pipelines that are still running in the source environment. In that kind of scenario, you should monitor the performance of the system by using any built-in or custom metrics. To avoid overwhelming the system, we recommend that you have a plan to decommission some workloads during the data copying process, or to throttle down the copy phase.

Because copying data makes the migration a long-running process, we recommend that you have contingency plans to address anything that might go wrong during the migration. For example, if data movement is taking longer than expected or if integrity tests fail before you put the new system online, consider whether you want to roll back or try to fix and retry failed operations. Although a rollback can be a cleaner solution, it can be time-consuming and expensive to copy large datasets multiple times. We recommend that you have a clear understanding and predefined tests to determine which action to take in which conditions, how much time to allow to try to create patches, and when to perform a complete rollback.

It's important to differentiate between the tooling and scripts that you're using for the migration, and the data that you're copying. Rolling back data movement means that you have to recopy data and either override or delete data that you already copied. Rolling back changes to the tooling and scripts is potentially easier and less costly, but changes to tooling might force you to recopy data. For example, you might have to recopy data if you create a new target path in a script that generates a Cloud Storage location dynamically. To help avoid recopying data, build your scripts to allow for resumability and idempotency.

#### Data pipeline characteristics

In order to create an optimal migration plan, you need to understand the characteristics of different data pipelines. It's important to remember that batch pipelines that write data are different from batch pipelines that read data:

  * **Data pipelines that write data** : Because it changes the state of the source system, it can be difficult to write data to the source environment at the same time that data is being copied to the target environment. Consider the runtimes of pipelines that write data, and try to prioritize their migration earlier in the overall process. Doing so will let you have data ready on the target environment before you migrate the pipelines that read the data.
  * **Data pipelines that read data** : Pipelines that read data might have different requirements for data freshness. If the pipelines that generate data are stopped on the source system, then the pipelines that read data might be able to run while data is being copied to the target environment.



Data is state, and copying data between regions isn't an atomic operation. Therefore, you need to be aware of state changes while data is being copied.

It's also important in the migration plan to differentiate between systems. Your systems might have different functional and non-functional requirements (for example, one system for batch and another for streaming). Therefore, your plan should include different strategies to migrate each system. Make sure that you specify the dependencies between the systems and specify how you will reduce downtime for each system during each phase of the migration.

A typical plan for a migration sprint should include the following:

  * **General strategy**. Describe the strategy for handling the migration in this sprint. For common strategies, see [Deploy your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads).
  * **List of tools and methods for data copy and resource deployment**. Specify any tool that you plan to use to copy data or deploy resources to the target environment. This list should include custom scripts that are used to copy Cloud Storage assets, standard tooling such as the Google Cloud CLI, and Google Cloud tools such as Migration Services.
  * **List of resources to deploy to the target environment**. List all resources that need to be deployed in the target environment. This list should include all data infrastructure components such as Cloud Storage buckets, BigQuery datasets, and Managed Service for Apache Spark clusters. In some cases, early migration sprints will include deployment of a sized cluster (such as a Managed Service for Apache Spark cluster) in a smaller capacity, while later sprints will include resizing to fit new workloads. Make sure that your plan includes potential resizing.
  * **List of datasets to be copied**. For each dataset, make sure to specify the following information: 
    * **Order in copying (if applicable)** : For most strategies, the order of operation might be important. An exception is the _scheduled maintenance_ strategy that's described later in this document.
    * **Size**
    * **Key statistics** : Chart key statistics, such as row number, that can help you to verify that the dataset was copied successfully.
    * **Estimated time to copy** : The time to complete your data transfer, based on the migration plan.
    * **Method to copy** : Refer to the tools and methods list described earlier in this document.
    * **Verification tests** : Explicitly list the tests that you plan to complete to verify that the data was copied in full.
    * **Contingency plan** : Describe what to do if any verification tests fail. Your contingency plan should specify when to retry and resume the copy or fill in the gap, and when to do a complete rollback and recopy the entire dataset.



#### Testing

This section describes some typical types of tests that you can plan for. The tests can help you to ensure data integrity and completeness. They can also help you to ensure that the computational layer is working as expected and is ready to run your data pipelines.

  * **Summary or hashing comparison** : In order to validate data completeness after copying data over, you need to compare the original dataset against the new copy on the target environment. If the data is structured inside BigQuery tables, you can't join the two tables in a query to see if all data exists, because the tables reside in different regions. Because of the cost and latency, BigQuery doesn't allow queries to join data across regions. Instead, the method of comparison must summarize each dataset and compare the results. Depending on the dataset structure, the method for summarizing might be different. For example, a BigQuery table might use an aggregation query, but a set of files on Cloud Storage might use a Spark pipeline to calculate a hash of each file, and then aggregate the hashes.
  * **Canary flows** : Canary flows activate jobs that are built to validate data integrity and completeness. Before you continue to business use cases like data analytics, it can be useful to run canary flow jobs to make sure that input data complies with a set of prerequisites. You can implement canary flows as custom-made data pipelines, or as flows in a [DAG](https://docs.cloud.google.com/composer/docs/concepts/overview#workflows_dags_and_tasks) based on Managed Service for Apache Airflow. Canary flows can help you to complete tasks like verifying that there are no missing values for certain fields, or validating that the row count of specific datasets matches the expected count.

You can also use canary flows to create digests or other aggregations of a column or a subset of the data. You can then use the canary flow to compare the data to a similar digest or aggregation that's taken from the copy of the data.

Canary flow methods are valuable when you need to evaluate the accuracy of data that's stored and copied in file formats, like Avro files on top of Cloud Storage. Canary flows don't normally generate new data, but instead they fail if a set of rules isn't met within the input data.

  * **Testing environment** : After you complete your migration plan, you should test the plan in a testing environment. The testing environment should include copying sampled data or staging data to another region, to estimate the time that it takes to copy data over the network. This testing helps you to identify any issues with the migration plan, and helps to verify that the data can be migrated successfully. The testing should include both functional and non-functional testing. Functional testing verifies that the data is migrated correctly. Non-functional testing verifies that the migration meets performance, security, and other non-functional requirements. Each migration step in your plan should include a validation criteria that details when the step can be considered complete.




To help with data validation, you can use the [Data Validation Tool (DVT)](https://cloud.google.com/blog/products/databases/automate-data-validation-with-dvt). The tool performs multi-leveled data validation functions, from the table level to the row level, and it helps you compare the results from your source and target systems.

Your tests should verify deployment of the computational layer, and test the datasets that were copied. One approach to do so is to construct a testing pipeline that can compute some aggregations of the copied datasets, and make sure the source datasets and the target datasets match. A mismatch between source and target datasets is more common when the files that you copy between regions aren't exact byte-copy representations between the source and target systems (such as when you change file formats or file compressions).

For example, consider a dataset that's composed of newline delimited JSON files. The files are stored in a Cloud Storage bucket, and are mounted as an external table in BigQuery. To reduce the amount of data moved over the network, you can perform Avro compression as part of the migration, before you copy files to the target environment. This conversion has many upsides, but it also has some risks, because the files that are being written to the target environment aren't a byte-copy representation of the files in the source environment.

To mitigate the risks from the conversion scenario, you can create a Dataflow job, or use BigQuery to calculate some aggregations and checksum hashes of the dataset (such as by calculating sums, averages, or quantiles for each numeric column). For string columns, you can compute aggregations on top of the string length, or on the hash code of that string. For each row, you can compute an aggregated hash from a combination of all the other columns, which can verify with high accuracy that one row is the same as its origin. These calculations are made on both the source and target environments, and then they're compared. In some cases, such as if your dataset is stored in BigQuery, you can't join tables from the source and target environments because they're in different regions, so you need to use a client that can connect to both environments.

You can implement the preceding testing methods either in BigQuery or as a batch job (such as in Dataflow). You can then run the aggregation jobs and compare the results calculated for the source environment to the results calculated for the target environment. This approach can help you to make sure that data is complete and accurate.

Another important aspect of testing the computational layer is to run pipelines that include all varieties of the processing engines and computational methods. Testing the pipeline is less important for managed computational engines like BigQuery or Dataflow. However, it's important to test the pipeline for non-managed computational engines like Managed Service for Apache Spark. For example, if you have a Managed Service for Apache Spark cluster that handles several different types of computation, such as Apache Spark, Apache Hive, Apache Flink, or Apache MapReduce, you should test each runtime to make sure that the different workload types are ready to be transferred.

#### Migration strategies

After you verify your migration plan with proper testing, you can migrate data. When you migrate data, you can use different strategies for different workloads. The following are examples of migration strategies that you can use as is or customize for your needs:

  * **Scheduled maintenance** : You plan when your cutover window occurs. This strategy is good when data is changed frequently, but SLOs and SLAs can withstand some downtime. This strategy offers high confidence of data transferred because data is completely stale while it's being copied. For more information, see [Scheduled maintenance](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#scheduled_maintenance) in "Migration to Google Cloud: Transferring your large datasets."
  * **Read-only cutover** : A slight variation of the scheduled maintenance strategy, where the source system data platform allows read-only data pipelines to continue reading data while data is being copied. This strategy is useful because some data pipelines can continue to work and provide insights to end systems. The disadvantage to this strategy is that the data that's produced is stale during the migration, because the source data doesn't get updated. Therefore, you might need to employ a catch-up strategy after the migration, to account for the stale data in the end systems.
  * **Fully active** : You copy the data at a specific timestamp, while the source environment is still active for both read and write data pipelines. After you copy the data and switch over to the new deployment, you perform a delta copy phase to get the data that was generated after the migration timestamp in the source environment. This approach requires more coordination and consideration compared to other strategies. Therefore, your migration plan must include how you will handle the update and delete operations on the source data.
  * **Double-writes** : The data pipelines can run on both the source and target environments, while data is being copied. This strategy avoids the delta copy phase that's required to backfill data if you use the fully active or read-only strategies. However, to help make sure that data pipelines are producing identical results, a double-writes strategy requires more testing before the migration. If you don't perform advance testing, you will encounter problems trying to consolidate a [split-brain](https://en.wikipedia.org/wiki/Split-brain_\(computing\)) scenario. The double-writes strategy also introduces potential costs of running the same workloads twice in different regions. This strategy has the potential to migrate your platform with zero downtime, but it requires much more coordination to execute it correctly.



### Post-migration testing

After the migration is complete, you should test data completeness and test the data pipelines for validity. If you complete your migration in sprints, you need to perform these tests after each sprint. The tests that you perform in this stage are similar to integration tests: you test the validity of a data pipeline that's running business use cases with full production-grade data as input, and then you inspect the output for validity. You can compare the output of the integration test to the output from the source environment by running the same data pipeline in both the source environment and in the target environment. This type of test works only if the data pipeline is deterministic, and if you can ensure that the input to both environments is identical.

You can confirm that the data is complete when it meets a set of predefined criteria, where the data in the source environment is equal (or similar enough) to the data in the target environment. Depending on the strategy that you used from the previous section, the data might not match one-to-one. Therefore, you need to predefine criteria to describe data completeness for your use case. For example, for time-series data, you might consider the data to be complete when the most up-to-date record is no more than five minutes behind the current timestamp.

### Cutover

After you verify and test the data and data pipelines on the target environment, you can start the cutover phase. Starting this phase means that clients might need to change their configuration to reference the new systems. In some cases, the configuration can't be the same as the configuration that's pointing to the source system. For example, if a service needs to read data from a Cloud Storage bucket, clients need to change the configuration for which bucket to use. Cloud Storage bucket names are globally unique, so your target environment Cloud Storage bucket will be different from the source environment.

During the cutover phase, you should decommission and unschedule the source environment workloads. We recommend that you keep the source environment data for some time, in case you need to roll back.

The pre-migration testing phase isn't as complete as a production run of a data pipeline. Therefore, after the cutover is complete and the target system is operational, you need to monitor the metrics, runtimes, and semantic outputs of your data pipelines. This monitoring will help you to catch errors that your testing phase might have missed, and it will help ensure the success of the migration.

## Optimize your environment

Optimization is the last phase of your migration. In this phase, you make your environment more efficient by executing multiple iterations of a repeatable loop until your environment meets your optimization requirements:

  1. Assess your current environment, teams, and optimization loop.
  2. Establish your optimization requirements and goals.
  3. Optimize your environment and your teams.
  4. Tune the optimization loop.



For more information about how to optimize your Google Cloud environment, see [Migration to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment).

## Prepare your Google Cloud data and computing resources for a migration across regions

This section provides an overview of the data and computing resources on Google Cloud and of the design principles to prepare for a migration across regions.

### BigQuery

Because BigQuery is a serverless SQL data warehouse, you don't have to deploy the computation layer. If some of your BigQuery clients specify regions for processing, you will need to adjust those clients. Otherwise, BigQuery is the same in the source environment and the target environment. BigQuery data is stored in two kinds of tables:

  * **BigQuery tables** : Tables in the BigQuery format. BigQuery manages the data files for you. For more information about migrating data in the BigQuery format, see [Manage datasets](https://docs.cloud.google.com/bigquery/docs/managing-datasets#copy_a_dataset).
  * **BigQuery external tables** : Tables for which the data is stored outside of BigQuery. After the data is moved, you will need to recreate the external tables in the new destination. For more information about migrating external tables, see [Introduction to external tables](https://docs.cloud.google.com/bigquery/docs/external-tables#moving_data_between_locations).



### Cloud Storage

Cloud Storage offers a [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/move-your-cloud-storage-data-to-another-location) that can help you migrate your data.

### Dataflow (Batch)

Dataflow is a Google-managed data processing engine. To help simplify your Dataflow migration and ensure that your jobs can be deployed to any region, you should inject all inputs and outputs as parameters to your job. Instead of writing input and output data locations in your source code, we recommend that you pass Cloud Storage paths and database connection strings as arguments or parameters.

### Managed Service for Apache Spark

Managed Service for Apache Spark is a managed Apache Hadoop environment that can run any workload that's compatible with the Apache Hadoop framework. It's compatible with frameworks such as Apache Spark, Apache Flink, and Apache Hive.

You can use Managed Service for Apache Spark in the following ways, which affect how you should migrate your Managed Service for Apache Spark environment across regions:

  * **Ephemeral clusters with data on Cloud Storage** : Clusters are built to run specific jobs, and they're destroyed after the jobs are done. This means that the HDFS layer or any other state of the cluster is also destroyed. If your configuration meets the following criteria, then this type of usage is easier to migrate compared to other types of usage: 
    * Inputs and outputs to your jobs aren't hardcoded in the source code. Instead, your jobs receive inputs and output as arguments.
    * The Managed Service for Apache Spark environment provisioning is automated, including the configurations for the individual frameworks that your environment is using.
  * **Long-living clusters with external data** : You have one or more clusters, but they're long-living clusters—even if there are no running jobs on the cluster, the cluster is still up and running. The data and compute are separate because the data is saved outside of the cluster on Google Cloud solutions like Cloud Storage or BigQuery. This model is usually effective when there are always jobs that are running on the cluster, so it doesn't make sense to tear down and set up clusters like in the ephemeral model. Because data and compute are separate, the migration is similar to migration of the ephemeral model.
  * **Long-living clusters with data in the cluster** : The cluster is long living, but the cluster is also keeping state, data, or both, inside the cluster, most commonly as data on HDFS. This type of use complicates the migration efforts because data and compute aren't separate; if you migrate one without the other, there is a high risk of creating inconsistencies. In this scenario, consider moving data and state outside of the cluster before the migration, to separate the two. If doing so is impossible, then we recommend that you use the scheduled maintenance strategy in order to reduce the risk of creating inconsistencies in your data.



Because there are many potential frameworks, and many versions and configurations of those frameworks, you need to test thoroughly before you execute your migration plan.

### Managed Airflow

Managed Airflow is Google Cloud's managed version of Apache Airflow, for orchestration and scheduling of flows. DAGs, configurations, and logs are managed in a Cloud Storage bucket that should be migrated with your Managed Airflow deployment. In order to migrate the state of your Managed Airflow deployment, you can [save and load environment snapshots](https://docs.cloud.google.com/composer/docs/save-load-snapshots).

If you've deployed any custom plugins to your Managed Airflow instance, we recommend that you apply an infrastructure-as-code methodology to recreate the environment in a fully automated manner.

Managed Airflow doesn't manage data but it activates other data processing frameworks and platforms. Therefore, migration of Managed Airflow can be completely isolated from the data. Managed Airflow also doesn't process data, so your deployment doesn't need to be in the same region as the data. Therefore, you can create a Managed Airflow deployment in the target environment, and still run pipelines on the source environment. In some cases, doing so can be useful for operating different pipelines in different regions while the entire platform is being migrated.

### Cloud Data Fusion

Cloud Data Fusion is a visual integration tool that helps you build data pipelines using a visual editor. Cloud Data Fusion is based on the open source project [CDAP](https://cdap.io/). Like Managed Airflow, Cloud Data Fusion doesn't manage data itself, but it activates other data processing frameworks and platforms. Your Cloud Data Fusion pipelines should be exported from the source environment and imported to the target environment in one of these ways:

  * **Manual process** : Use the web interface to [export and import pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines).
  * **Automated process** : Write a script that uses the CDAP API. For more information, see [CDAP reference](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference) and the [CDAP REST API documentation](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices).



Depending on the amount of flows that you need to migrate, you might prefer one method over the other. Using the CDAP API to build a migration script might be difficult, and it requires more software engineering skills. However, if you have a lot of flows, or if the flows change relatively frequently, an automated process might be the best approach.

## What's Next

  * Learn how to [design resilient single-region environments on Google Cloud](https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments).
  * Learn how to [minimize the costs of migrating your single- and multi-region environments](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs).
  * Learn when to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Eyal Ben Ivri](https://www.linkedin.com/in/eyalbenivri) | Cloud Solutions Architect

Other contributor: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-02 UTC."],[],[]] 
