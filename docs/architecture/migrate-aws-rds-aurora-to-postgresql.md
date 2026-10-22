---
url: https://docs.cloud.google.com/architecture/migrate-aws-rds-aurora-to-postgresql/
title: Migrate from AWS to Google Cloud: Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL and AlloyDB for PostgreSQL \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:36.747315+00:00
---

# Migrate from AWS to Google Cloud: Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL and AlloyDB for PostgreSQL  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migrate-aws-rds-aurora-to-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate from AWS to Google Cloud: Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL and AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-09-12 UTC

Google Cloud provides tools, products, guidance, and professional services to migrate from Amazon Relational Database Service (RDS) or Amazon Aurora to Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL.

This document is intended for cloud and database administrators who want to plan, implement, and validate a database migration project. It's also intended for decision makers who are evaluating the opportunity to migrate and want an example of what a migration might look like.

This document focuses on a homogeneous database migration, which is a migration where the source and destination databases are the same database technology. In this migration guide, the source is Amazon RDS or Amazon Aurora for PostgreSQL, and the destination is Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL.

This document is part of a multi-part series about migrating from AWS to Google Cloud that includes the following documents:

  * [Get started](https://docs.cloud.google.com/architecture/migration-from-aws-get-started)
  * [Migrate from Amazon EC2 to Compute Engine](https://docs.cloud.google.com/architecture/migrate-amazon-ec2-to-compute-engine)
  * [Migrate from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage)
  * [Migrate from Amazon EKS to GKE](https://docs.cloud.google.com/architecture/migrate-amazon-eks-to-gke)
  * [Migrate from Amazon RDS and Amazon Aurora for MySQL to Cloud SQL for MySQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-sql-mysql)
  * Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL and AlloyDB for PostgreSQL (this document)
  * [Migrate from Amazon RDS for SQL Server to Cloud SQL for SQL Server](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-cloudsql-for-sqlserver)
  * [Migrate from AWS Lambda to Cloud Run](https://docs.cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun)



For this migration to Google Cloud, we recommend that you follow the migration framework described in [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#the_migration_path).

The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

You might migrate from your source environment to Google Cloud in a series of iterations—for example, you might migrate some workloads first and others later. For each separate migration iteration, you follow the phases of the general migration framework:

  1. Assess and discover your workloads and data.
  2. Plan and build a foundation on Google Cloud.
  3. Migrate your workloads and data to Google Cloud.
  4. Optimize your Google Cloud environment.



For more information about the phases of this framework, see [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).

To design an effective migration plan, we recommend that you validate each step of the plan, and ensure that you have a rollback strategy. To help you validate your migration plan, see [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices).

## Assess the source environment

In the assessment phase, you determine the requirements and dependencies to migrate your source environment to Google Cloud.

The assessment phase is crucial for the success of your migration. You need to gain deep knowledge about the workloads you want to migrate, their requirements, their dependencies, and about your current environment. You need to understand your starting point to successfully plan and execute a Google Cloud migration.

The assessment phase consists of the following tasks:

  1. Build a comprehensive inventory of your workloads.
  2. Catalog your workloads according to their properties and dependencies.
  3. Train and educate your teams on Google Cloud.
  4. Build experiments and proofs of concept on Google Cloud.
  5. Calculate the total cost of ownership (TCO) of the target environment.
  6. Choose the migration strategy for your workloads.
  7. Choose your migration tools.
  8. Define the migration plan and timeline.
  9. Validate your migration plan.



The database assessment phase helps you choose the size and specifications of your target Cloud SQL database instance that matches the source for similar performance needs. Pay special attention to disk size and throughput, IOPS, and number of vCPUs. Migrations might struggle or fail due to incorrect target database instance sizing. Incorrect sizing can lead to long migration times, database performance problems, database errors, and application performance problems. When deciding on the Cloud SQL instance, keep in mind that disk performance is based on the disk size and the number of vCPUs.

The following sections rely on [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads), and integrate the information in that document.

### Build an inventory of your Amazon RDS or Amazon Aurora instances

To define the scope of your migration, you create an inventory and collect information about your Amazon RDS and Amazon Aurora instances. Ideally, this should be an automated process because manual approaches are prone to error and can lead to incorrect assumptions.

Amazon RDS or Amazon Aurora and Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL might not have similar features, instance specifications, or operation. Some functionalities might be implemented differently or be unavailable. Areas of differences might include infrastructure, storage, authentication and security, replication, backup, high availability, resource capacity model and specific database engine feature integrations, and extensions. Depending on the database engine type, instance size, and architecture, there are also differences in the default values of database parameter settings.

Benchmarking can help you to better understand the workloads that are to be migrated and contributes to defining the right architecture of the migration target environment. Collecting information about performance is important to help estimate the performance needs of the Google Cloud target environment. Benchmarking concepts and tools are detailed in the Perform testing and validation of the migration process, but they also apply to the inventory building stage.

### Tools for assessments

For an initial overview assessment of your current infrastructure, we recommend that you use [Google Cloud Migration Center](https://docs.cloud.google.com/migration-center/docs/migration-center-overview) along with other specialized database assessment tools such as migVisor and Database Migration Assessment Tool (DMA).

With Migration Center, you can perform a complete assessment of your application and database landscape, including the technical fit for a database migration to Google Cloud. You receive size and configuration recommendations for each source database, and create a total cost of ownership (TCO) report for servers and databases.

For more information about assessing your AWS environment by using Migration Center, see [Import data from other cloud providers](https://docs.cloud.google.com/migration-center/docs/import-data-cloud-providers).

In addition to Migration Center, you can use the specialized tool migVisor. migVisor supports a variety of database engines and is particularly suitable for heterogeneous migrations. For an introduction to migVisor, see the [migVisor overview](https://doc.migvisor.com/mdoc/overview).

migVisor can identify artifacts and incompatible proprietary database features that can cause migration defaulting, and can point to workarounds. migVisor can also recommend a target Google Cloud solution, including initial sizing and architecture.

The migVisor database assessment output provides the following:

  * Comprehensive discovery and analysis of current database deployments.
  * Detailed report of migration complexity, based on the proprietary features used by your database.
  * Financial report with details on cost savings post migration, migration costs, and new operating budget.
  * Phased migration plan to move databases and associated applications with minimal disruption to the business.



To see some examples of assessment outputs, see [migVisor - Cloud migration assessment tool](https://solutionshub.epam.com/solution/migvisor-by-epam).

Note that migVisor temporarily increases database server utilization. Typically, this additional load is less than 3%, and can be run during non-peak hours.

The migVisor assessment output helps you to build a complete inventory of your RDS instances. The report includes generic properties (database engine version and edition, CPUs, and memory size), as well as details about database topology, backup policies, parameter settings, and special customizations in use.

If you prefer to use open source tools, you can use data collector scripts with (or instead of) the mentioned tools. These scripts can help you collect detailed information (about workloads, features, database objects, and database code) and build your database inventory. Also, scripts usually provide a detailed database migration assessment, including a migration effort estimation.

We recommend the open source tool DMA, which was built by Google engineers. It offers a complete and accurate database assessment, including features in use, database logic, and database objects (including schemas, tables, views, functions, triggers, and stored procedures).

To use DMA, download the collection scripts for your database engine from the [Git repository](https://googlecloudplatform.github.io/database-assessment/), and follow the instructions. Send the output files to Google Cloud for analysis. Google Cloud creates and delivers a database assessment readout, and provides the next steps in the migration journey.

### Identify and document the migration scope and affordable downtime

At this stage, you document essential information that influences your migration strategy and tooling. By now, you can answer the following questions:

  * Are your databases larger than 5 TB?
  * Are there any large tables in your database? Are they larger than 16 TB?
  * Where are the databases located ([regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) and zones), and what's their proximity to applications?
  * How often does the data change?
  * What is your data consistency model?
  * What are the options for destination databases?
  * How compatible are the source and destination databases?
  * Does the data need to reside in some physical locations?
  * Is there data that can be compressed and archived, or is there data that doesn't need migration at all?



To define the migration scope, decide what data to keep and what to migrate. Migrating all your databases might take considerable time and effort. Some data might remain in your source database backups. For example, old logging tables or archival data might not be needed. Alternatively, you might decide to move data after the migration process, depending on your strategy and tools.

Establish data migration baselines that help you compare and evaluate your outcomes and impacts. These baselines are reference points that represent the state of your data before and after the migration and help you make decisions. It's important to take measurements on the source environment that can help you evaluate your data migration's success. Such measurements include the following:

  * The size and structure of your data.
  * The completeness and consistency of your data.
  * The duration and performance of the most important business transactions and processes.



Determine how much downtime you can afford. What are the business impacts of downtime? Are there periods of low database activity, during which there are fewer users affected by downtime? If so, how long are such periods and when do they occur? Consider having a partial write only downtime, while read-only requests are still served.

### Assess your deployment and administration process

After you build the inventories, assess the operational and deployment processes for your database to determine how they need to be adapted to facilitate your migration. These processes are fundamental to how you prepare and maintain your production environment.

Consider how you complete the following tasks:

  * **Define and enforce security policies for your instances**. For example, you might need to replace Amazon Security Groups. You can use Google IAM roles, VPC firewall rules, and VPC Service Controls to control access to your Cloud SQL for PostgreSQL instances and constrain the data within a VPC.

  * **Patch and configure your instances**. Your existing deployment tools might need to be updated. For example, you might be using custom configuration settings in Amazon parameter groups or Amazon option groups. Your provisioning tools might need to be adapted to use Cloud Storage or Secret Manager to read such custom configuration lists.

  * **Manage monitoring and alerting infrastructure**. Metric categories for your Amazon source database instances provide observability during the migration process. Metric categories might include Amazon CloudWatch, Performance Insights, Enhanced Monitoring, and OS process lists.




### Complete the assessment

After you build the inventories from your Amazon RDS or Amazon Aurora environment, complete the rest of the activities of the assessment phase as described in [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/solutions/migration-to-gcp-assessing-and-discovering-your-workloads).

## Plan and build your foundation

In the plan and build phase, you provision and configure the infrastructure to do the following:

  * Support your workloads in your Google Cloud environment.
  * Connect your source environment and your Google Cloud environment to complete the migration.



The plan and build phase is composed of the following tasks:

  1. Build a resource hierarchy.
  2. Configure Google Cloud's Identity and Access Management (IAM).
  3. Set up billing.
  4. Set up network connectivity.
  5. Harden your security.
  6. Set up logging, monitoring, and alerting.



For more information about each of these tasks, see the [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation).

If you plan to use Database Migration Service for migration, see [Networking methods for Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods) to understand the networking configurations available for migration scenarios.

### Monitoring and alerting

Use Google [Cloud Monitoring](https://docs.cloud.google.com/monitoring), which includes predefined dashboards for several Google Cloud products, including a Cloud SQL monitoring dashboard. Alternatively, you can consider using third-party monitoring solutions that are integrated with Google Cloud, like Datadog and Splunk. For more information, see [About database observability](https://docs.cloud.google.com/sql/docs/mysql/observability).

## Migrate Amazon RDS and Amazon Aurora for PostgreSQL instances to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL

To migrate your instances, you do the following:

  1. Choose the migration strategy: continuous replication or scheduled maintenance.

  2. Choose the migration tools, depending on your chosen strategy and requirements.

  3. Define the migration plan and timeline for each database migration, including preparation and execution tasks.

  4. Define the preparation tasks that must be done to ensure the migration tool can work properly.

  5. Define the execution tasks, which include work activities that implement the migration.

  6. Define fallback scenarios for each execution task.

  7. Perform testing and validation, which can be done in a separate staging environment.

  8. Perform the migration.

  9. Perform the production cut-over.

  10. Clean up the source environment and configure the target instance.

  11. Perform tuning and optimization.




Each phase is described in the following sections.

## Choose your migration strategy

At this step, you have enough information to evaluate and select one of the following migration strategies that best suits your use case for each database:

  * **Scheduled maintenance (also called one-time migration or _big bang migration_)**: This approach is ideal if you can afford downtime. This option is relatively lower in cost and complexity, because your workloads and services won't require much refactoring. However, if the migration fails before completion, you have to restart the process, which prolongs the downtime.
  * **Continuous replication (also called online migration or _trickle migration_)**: For mission-critical databases, this option offers a lower risk of data loss and near-zero downtime. The efforts are split into several chunks, so if a failure occurs, rollback and repeat takes less time. However, setup is more complex and takes more planning and time. Additional effort is also required to refactor the applications that connect to your database instances. Consider one of the following variations:

    * Using the [Y (writing and reading)](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#y_writing_and_reading) approach, which is a form of parallel migration, duplicating data in both source and destination instances during the migration.
    * Using a data-access microservice, which reduces refactoring effort required by the Y (writing and reading) approach.



For more information about data migration strategies, see [Evaluating data migration approaches](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#data_migration_approaches).

The following diagram shows a flowchart based on example questions that you might have when deciding the migration strategy for a single database:

![Flowchart to help you choose the migration strategy.](https://docs.cloud.google.com/static/architecture/images/migrate-aws-to-gcp-choose-strategy.svg)

The preceding flowchart shows the following decision points:

  * Can you afford any downtime?

    * If no, adopt the continuous replication migration strategy.
    * If yes, continue to the next decision point.
  * Can you afford the downtime represented by the cut-over window while migrating data? The cut-over window represents the amount of time to take a backup of the database, transfer it to Cloud SQL, restore it, and then switch over your applications.

    * If no, adopt the continuous replication migration strategy.
    * If yes, adopt the scheduled maintenance migration strategy.



Strategies might vary for different databases, even when they're located on the same instance. A mix of strategies can produce optimal results. For example, migrate small and infrequently used databases by using the scheduled maintenance approach, but use continuous replication for mission-critical databases where having downtime is expensive.

Usually, a migration is considered completed when the switch between the initial source instance and the target instance takes place. Any replication (if used) is stopped and all reads and writes are done on the target instance. Switching when both instances are in sync means no data loss and minimal downtime.

For more information about data migration strategies and deployments, see [Classification of database migrations](https://docs.cloud.google.com/architecture/database-migration-concepts-principles-part-1#classification_of_database_migrations).

### Minimize downtime and migration-related impacts

Migration configurations that provide no application downtime require a more complicated setup. Find the right balance between setup complexity and downtime scheduled during low-traffic business hours.

Each migration strategy has a tradeoff and some impact associated with the migration process. For example, replication processes involve some additional load on your source instances and your applications might be affected by replication lag. Applications (and customers) might have to wait during application downtime, at least as long as the replication lag lasts before using the new database. In practice, the following factors might increase downtime:

  * Database queries can take a few seconds to complete. At the time of migration, in-flight queries might be aborted.
  * The cache might take some time to fill up if the database is large or has a substantial buffer memory.
  * Applications stopped in the source and restarted in Google Cloud might have a small lag until the connection to the Google Cloud database instance is established.
  * Network routes to the applications must be rerouted. Depending on how DNS entries are set up, this can take some time. When you update DNS records, reduce TTL before the migration.



The following common practices can help minimize downtime and impact:

  * Find a time period when downtime would have a minimal impact on your workloads. For example, outside normal business hours, during weekends, or other scheduled maintenance windows.
  * Identify parts of your workloads that can undergo migration and production cut-over at different stages. Your applications might have different components that can be isolated, adapted, and migrated with no impact. For example, frontends, CRM modules, backend services, and reporting platforms. Such modules could have their own databases that can be scheduled for migration earlier or later in the process.
  * If you can afford some latency on the target database, consider implementing a gradual migration. Use incremental, batched data transfers, and adapt part of your workloads to work with the stale data on the target instance.
  * Consider refactoring your applications to support minimal migration impact. For example, adapt your applications to write to both source and target databases, and therefore implement an application-level replication.



## Choose your migration tools

The most important factor for a successful migration is choosing the right migration tool. Once the migration strategy has been decided, review and decide upon the migration tool.

There are many tools available, each optimized for certain migration use cases. Use cases can include the following:

  * Migration strategy (scheduled maintenance or continuous replication).
  * Source and target database engines and engine versions.
  * Environments in which source instances and target instances are located.
  * Database size. The larger the database, the more time it takes to migrate the initial backup.
  * Frequency of the database changes.
  * Availability to use managed services for migration.



To ensure a seamless migration and cut-over, you can use application deployment patterns, infrastructure orchestration, and custom migration applications. However, specialized tools called managed migration services can facilitate the process of moving data, applications, or even entire infrastructures from one environment to another. They run the data extraction from the source databases, securely transport data to the target databases, and can optionally modify the data during transit. With these capabilities, they encapsulate the complex logic of migration and offer migration monitoring capabilities.

Managed migration services provide the following advantages:

  * **Minimize downtime** : Services use the built-in replication capabilities of the database engines when available, and perform replica promotion.

  * **Ensure data integrity and security** : Data is securely and reliably transferred from the source to the destination database.

  * **Provide a consistent migration experience** : Different migration techniques and patterns can be consolidated into a consistent, common interface by using database migration executables, which you can manage and monitor.

  * **Offer resilient and proven migration models** : Database migrations are infrequent but critical events. To avoid beginner mistakes and issues with existing solutions, you can use tools from experienced experts, rather than building a custom solution.

  * **Optimize costs** : Managed migration services can be more cost effective than provisioning additional servers and resources for custom migration solutions.




The next sections describe the migration tool recommendations, which depend on the chosen migration strategy.

### Tools for scheduled maintenance migrations

The following subsections describe the tools that can be used for one-time migrations, along with the limitations and best practices of each tool.

For one-time migrations to Cloud SQL for PostgreSQL or to AlloyDB for PostgreSQL, we recommend that you use database engine backups to both export the data from your source instance and import that data into your target instance. One-time migration jobs are not supported in Database Migration Service.

#### Built-in database engine backups

When significant downtime is acceptable, and your source databases are relatively static, you can use the database engine's built-in dump and load (also sometimes called backup and restore) capabilities.

Some effort is required for setup and synchronization, especially for a large number of databases, but database engine backups are usually readily available and straightforward to use. This approach is suitable for any database size, and it's usually more effective than other tools for large instances.

Database engine backups have the following general limitations:

  * Backups can be error prone, particularly if performed manually.
  * Data can be unsecured if the snapshots are not properly managed.
  * Backups lack proper monitoring capabilities.
  * Backups require effort to scale when migrating many databases.



You can use the PostgreSQL built-in backup utilities, `pg_dump` and `pg_dumpall`, to migrate both Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL. However, the `pg_dump` and `pg_dumapall` utilities have the following general limitations:

  * The built-in backup utilities should be used to migrate databases that are 500 GB in size or less. Dumping and restoring large databases can take a long time and may require substantial disk space and memory.
  * The `pg_dump` utility doesn't include users and roles. To migrate these user accounts and roles, you can use the `pg_dumpall` utility.
  * Cloud Storage supports a maximum single-object size of up to 5 terabytes (TB). If you have databases larger than 5 TB, the export operation to Cloud Storage fails. In this case, you need to break down your export files into smaller segments.



If you choose to use these utilities, consider the following restrictions and best practices:

  * Compress data to reduce cost and transfer duration. Use the `--jobs` option with the `pg_dump` command to run a given number of dump jobs simultaneously.
  * Use the `-z` option with the `pg_dump` command to specify the compression level to use. Acceptable values for this option range from 0 to 9. The default value is to compress at a 6 level. Higher values decrease the size of the dump file, but can cause high resource consumptions at the client host. If the client host has enough resources, higher compression levels can further lower the dump file size.
  * Use the correct flags when you create a SQL dump file.
  * Verify the imported database. Monitor the output of the `pg_restore` utility for any error messages during the restore process. Review PostgreSQL logs for any warnings or errors during the restore process. Run basic queries and table counts to verify your database integrity.



For further reading about limitations and best practices, see the following resources:

  * [Best practices for importing and exporting data with Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/import-export)
  * [Cloud SQL for PostgreSQL Known Issues](https://docs.cloud.google.com/sql/docs/postgres/known-issues#import-export)
  * [Import a DMP file in AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/import-dmp-file)
  * [Migrate users with credentials to AlloyDB for PostgreSQL or another Cloud SQL instance](https://medium.com/google-cloud/migrate-users-with-credentials-from-cloudsql-to-another-instance-or-alloydb-for-postgresql-e377a222d3f8)



#### Other approaches for scheduled maintenance migration

Using other approaches than the built-in backup utilities might provide more control and flexibility in your scheduled maintenance migration. These other types of approaches let you perform transformations, checks, or other operations on your data while doing the migration. You can consolidate multiple instances or databases into a single instance or database. Consolidating instances can help mitigate operational costs and ease your scalability issues.

One such alternative to back-up utilities is to use flat files to export and import your data. For more information about flat file import, see [Export and import using CSV files for Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-csv).

Another alternative is to use a managed import to set up replication from an external PostgreSQL database. When you use a managed import, there is an initial data load from the external database into the Cloud SQL for PostgreSQL instance. This initial load uses a service that extracts data from the external server - the RDS or Aurora instance - and imports it into the Cloud SQL for PostgreSQL instance directly. For more information, see [use a managed import to set up replication from external databases](https://docs.cloud.google.com/sql/docs/postgres/replication/managed-import-replication-from-external).

An alternative way to do a one-time data migration of your data is to export the tables from your source PostgreSQL database to CSV or SQL files. You can then import the CSV or SQL file into Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL. To export the date of your source instance, you can use the `aws_s3` extension for PostgreSQL. Alternatively, you can use Amazon Database Migration Service and an S3 bucket as a target. For detailed information about this approach, see the following resources:

  * [Installing the aws_s3 extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-s3-export.html#USER_PostgreSQL.S3Export.InstallExtension) for PostgreSQL
  * [Using Amazon S3 as a target for Amazon Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html)



You can also manually import data into an AlloyDB for PostgreSQL instance. The supported formats are as follows:

  * **CSV** : With this file format, each file in this format contains the contents of one table in the database. You can load the data into the CSV file by using the `psql` command-line program. For more information, see [Import a CSV file](https://docs.cloud.google.com/alloydb/docs/import-csv-file).
  * **DMP** : This file format contains the archive of an entire PostgreSQL database. You import data from this file by using the `pg_restore` utility. For more information, see [Import a DMP file](https://docs.cloud.google.com/alloydb/docs/import-dmp-file).
  * **SQL** : This file format contains the text reconstruction of a PostgreSQL database. The data in this file is processed by using the `psql` command line. For more information, see [Import a SQL file](https://docs.cloud.google.com/alloydb/docs/import-sql-file).



### Tools for continuous replication migrations

The following diagram shows a flowchart with questions that can help you choose the migration tool for a single database when you use a continuous replication migration strategy:

![Flowchart to help you choose a tool for continuous replication migrations.](https://docs.cloud.google.com/static/architecture/images/migrate-aws-to-gcp-continuous-replication-tools-postgresql.svg)

The preceding flowchart shows the following decision points:

  * Do you prefer to use managed migration services?

    * If yes, can you afford a few seconds of write downtime while the replication step takes place?

      * If yes, use Database Migration Service.
      * If no, explore other migration options.
    * If no, you must evaluate whether database engine built-in replication is supported:

      * If yes, we recommend that you use built-in replication.
      * If no, we recommend that you explore other migration options.



The following sections describe the tools that can be used for continuous migrations, along with their limitations and best practices.

#### Database Migration Service for continuous replication migration

Database Migration Service provides a specific job type for continuous migrations. These continuous migration jobs support high-fidelity migrations to Cloud SQL for PostgreSQL and to AlloyDB for PostgreSQL.

When you use Database Migration Service to migrate to Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL, there are prerequisites and limitations that are associated with each target instance:

  * If you are migrating to Cloud SQL for PostgreSQL, use the following resources:

    * The full list of prerequisites is provided in [Configure your source for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database).
    * The full list of limitations is provided in [Known limitations for PostgresQL](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations).
  * If you are migrating to AlloyDB for PostgreSQL, use the following resources:

    * The full list of prerequisites is provided in [Configure your source for PostgreSQL to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database).
    * The full list of limitations is provided in [Known limitations for PostgreSQL to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations).



#### Database engine built-in replication

Database engine built-in replication is an alternative option to Database Migration Service for a continuous migration.

Database replication represents the process of copying and distributing data from a database called the primary database to other databases called replicas. It's intended to increase data accessibility and improve the fault tolerance and reliability of a database system. Although database migration is not the primary purpose of database replication, it can be successfully used as a tool to achieve this goal. Database replication is usually an ongoing process that occurs in real time as data is inserted, updated, or deleted in the primary database. Database replication can be done as a one-time operation, or a sequence of batch operations.

Most modern database engines implement different ways of achieving database replication. One type of replication can be achieved by copying and sending the write ahead log or transaction log of the primary to its replicas. This approach is called physical or binary replication. Other replication types work by distributing the raw SQL statements that a primary database receives, instead of replicating file system level changes. These replication types are called logical replication. For PostgreSQL, there are also third-party extensions, such as `pglogical`, that implement logical replication relying on write-ahead logging (WAL).

Cloud SQL supports replication for PostgreSQL. However, there are some prerequisites and limitations.

The following are limitations and prerequisites for Cloud SQL for PostgreSQL:

  * The following Amazon versions are supported:

    * Amazon RDS 9.6.10 and later, 10.5 and later, 11.1 and later, 12, 13, 14
    * Amazon Aurora 10.11 and later, 11.6 and later, 12.4 and later, and 13.3 and later
  * The firewall of the external server must be configured to allow the internal IP range that has been allocated for the private services access of the VPC network. The Cloud SQL for PostgreSQL replica database uses the VPC network as its private network.

  * The firewall of the source database must be configured to allow the entire internal IP range that has been allocated for the private service connection of the VPC network. The Cloud SQL for PostgreSQL destination instance uses this VPC network in the `privateNetwork` field of its `IpConfiguration` setting.

  * When you install the pglogical extension on a Cloud SQL for PostgreSQL instance, make sure that you have set the `enable_pglogical` flag to `on` (for example, `cloudsql.enable_pglogical=on`).

  * Make sure the `shared_preload_libraries` parameter includes the `pglogical` extension on your source instance (for example, `shared_preload_libraries=pg_stat_statements,pglogical`). Set the `rds.logical_replication` parameter to 1. This setting enables write-ahead logs at the logical level.

These changes require a restart of the primary instance.




For more information about using Cloud SQL for PostgreSQL for replication, see the [external server checklist](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#external_server_checklist_2) in the [replication section for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external) and also [Set up logical replication and decoding for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) from the Cloud SQL official documentation.

AlloyDB for PostgreSQL supports replication through the pglogical extension. To enable the pglogical extension for replication, you can use the `CREATE EXTENSION` command. Before using that command, you must first set the database flags `alloydb.enable_pglogical` and `alloydb.logical_decoding` to `on` in the AlloyDB for PostgreSQL instance where you want to use the extension. Setting these flags requires a restart of the instance.

#### Other approaches for continuous replication migration

You can use Datastream to replicate near real-time changes of your source PostgreSQL instance. Datastream uses change data capture (CDC) and replication to replicate and synchronize data. You can then use Datastream for continuous replication from Amazon RDS and Amazon Aurora. You use Datastream to replicate changes from your PostgreSQL instance to either BigQuery or Cloud Storage. That replicated data can then be brought into your Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL instance with Dataflow by using a Dataflow Flex Template, or with Managed Service for Apache Spark.

For more information about using Datastream and Dataflow, see the following resources:

  * [Configure an Amazon RDS for PostgreSQL database in Datastream](https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-psql)
  * [Configure an Amazon Aurora PostgreSQL database in Datastream](https://docs.cloud.google.com/datastream/docs/configure-amazon-aurora-psql)
  * [Work with PostgreSQL database WAL log files](https://docs.cloud.google.com/datastream/docs/work-with-postgresql-database-wal-log-files)
  * [Stream changes to data in real time with Datastream](https://docs.cloud.google.com/datastream/docs/quickstart-change-streaming-to-gcs)
  * [Dataflow overview](https://docs.cloud.google.com/dataflow/docs/about-dataflow)
  * [Dataflow Flex Template to upload batch data from Google Cloud Storage to AlloyDB for PostgreSQL (and Postgres)](https://googlecloudplatform.github.io/cloud-solutions/dataflow-gcs-to-alloydb/)



#### Third-party tools for continuous replication migration

In some cases, it might be better to use one third-party tool for most database engines. Such cases might be if you prefer to use a managed migration service and you need to ensure that the target database is always in near-real-time sync with the source, or if you need more complex transformations like data cleaning, restructuring, and adaptation during the migration process.

If you decide to use a third-party tool, choose one of the following recommendations, which you can use for most database engines.

[Striim](https://www.striim.com/striim-for-google-cloud-sql/) is an end-to-end, in-memory platform for collecting, filtering, transforming, enriching, aggregating, analyzing, and delivering data in real time:

  * Advantages:

    * Handles large data volumes and complex migrations.
    * Built-in change data capture for SQL Server.
    * Preconfigured connection templates and no-code pipelines.
    * Able to handle mission-critical, large databases that operate under heavy transactional load.
    * Exactly-once delivery.
  * Disadvantages:

    * Not open source.
    * Can become expensive, especially for long migrations.
    * Some limitations in data definition language (DDL) operations propagation. For more information, see [Supported DDL operations](https://www.striim.com/docs/en/handling-schema-evolution.html#supported-ddl-operations) and [Schema evolution notes and limitations](https://www.striim.com/docs/en/handling-schema-evolution.html#schema-evolution-notes-and-limitations).



For more information about Striim, see [Running Striim in the Google Cloud](https://www.striim.com/docs/platform/en/running-striim-in-the-google-cloud-platform.html).

[Debezium](https://debezium.io/) is an open source distributed platform for CDC, and can stream data changes to external subscribers:

  * Advantages:

    * Open source.
    * Strong community support.
    * Cost effective.
    * Fine-grained control on rows, tables, or databases.
    * Specialized for change capture in real time from database transaction logs.
  * Disadvantages:

    * Requires specific experience with Kafka and ZooKeeper.
    * At-least-once delivery of data changes, which means that you need duplicates handling.
    * Manual monitoring setup using Grafana and Prometheus.
    * No support for incremental batch replication.



For more information about Debezium migrations, see [Near Real Time Data Replication using Debezium](https://medium.com/google-cloud/near-real-time-data-replication-using-debezium-fd32be6d192a).

[Fivetran](https://www.fivetran.com/) is an automated data movement platform for moving data out of and across cloud data platforms.

  * Advantages:

    * Preconfigured connection templates and no-code pipelines.
    * Propagates any schema changes from your source to the target database.
    * Exactly-once delivery of your data changes, which means that you don't need duplicates handling.
  * Disadvantages:

    * Not open source.
    * Support for complex data transformation is limited.



## Define the migration plan and timeline

For a successful database migration and production cut-over, we recommend that you prepare a well-defined, comprehensive migration plan. To help reduce the impact on your business, we recommend that you create a list of all the necessary work items.

Defining the migration scope reveals the work tasks that you must do before, during, and after the database migration process. For example, if you decide not to migrate certain tables from a database, you might need pre-migration or post-migration tasks to implement this filtering. You also ensure that your database migration doesn't affect your existing service-level agreement (SLA) and business continuity plan.

We recommend that your migration planning documentation include the following documents:

  * Technical design document (TDD)
  * RACI matrix
  * Timeline (such as a T-Minus plan)



Database migrations are an iterative process, and first migrations are often slower than the later ones. Usually, well-planned migrations run without issues, but unplanned issues can still arise. We recommend that you always have a rollback plan. As a best practice, follow the guidance from [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices#migration_planning).

### TDD

The TDD documents all technical decisions to be made for the project. Include the following in the TDD:

  * Business requirements and criticality
  * Recovery time objective (RTO)
  * Recovery point objective (RPO)
  * Database migration details
  * Migration effort estimates
  * Migration validation recommendations



### RACI matrix

Some migrations projects require a RACI matrix, which is a common project management document that defines which individuals or groups are responsible for tasks and deliverables within the migration project.

### Timeline

Prepare a timeline for each database that needs to be migrated. Include all work tasks that must be performed, and defined start dates and estimated end dates.

For each migration environment, we recommend that you create a T-minus plan. A T-minus plan is structured as a countdown schedule, and lists all the tasks required to complete the migration project, along with the responsible groups and estimated duration.

The timeline should account for not only pre-migration preparation tasks execution, but also validating, auditing, or testing tasks that happen after the data transfer takes place.

The duration of migration tasks typically depends on database size, but there are also other aspects to consider, like business logic complexity, application usage, and team availability.

A T-Minus plan might look like the following:

Date | Phase | Category | Tasks | Role | T-minus | Status  
---|---|---|---|---|---|---  
11/1/2023 | Pre-migration | Assessment | Create assessment report | Discovery team | -21 | Complete  
11/7/2023 | Pre-migration | Target preparation | Design target environment as described by the design document | Migration team | -14 | Complete  
11/15/2023 | Pre-migration | Company governance | Migration date and T-Minus approval | Leadership | -6 | Complete  
11/18/2023 | Migration | Set up DMS | Build connection profiles | Cloud migration engineer | -3 | Complete  
11/19/2023 | Migration | Set up DMS | Build and start migration jobs | Cloud migration engineer | -2 | Not started  
11/19/2023 | Migration | Monitor DMS | Monitor DMS Jobs and DDL changes in the source instance | Cloud migration engineer | -2 | Not started  
11/21/2023 | Migration | Cutover DMS | Promote DMS replica | Cloud migration engineer | 0 | Not started  
11/21/2023 | Migration | Migration validation | Database migration validation | Migration team | 0 | Not started  
11/21/2023 | Migration | Application test | Run capabilities and performance tests | Migration team | 0 | Not started  
11/22/2023 | Migration | Company governance | Migration validation GO or NO GO | Migration team | 1 | Not started  
11/23/2023 | Post-migration | Validate monitoring | Configure monitoring | Infrastructure team | 2 | Not started  
11/25/2023 | Post-migration | Security | Remove DMS user account | Security team | 4 | Not started  
  
### Multiple database migrations

If you have multiple databases to migrate, your migration plan should contain tasks for all of the migrations.

We recommend that you start the process by migrating a smaller, ideally non-mission-critical database. This approach can help you to build your knowledge and confidence in the migration process and tooling. You can also detect any flaws in the process in the early stages of the overall migration schedule.

If you have multiple databases to migrate, the timelines can be parallelized. For example, to speed up the migration process, you might choose to migrate a group of small, static, or less mission-critical databases at the same time, as shown in the following diagram.

![Parallel database migration tasks.](https://docs.cloud.google.com/static/architecture/images/migrate-aws-to-gcp-parallel-timeline.svg)

In the example shown in the diagram, databases 1-4 are a group of small databases that are migrated at the same time.

## Define the preparation tasks

The preparation tasks are all the activities that you need to complete to fulfill the migration prerequisites. Without the preparation tasks, the migration can't take place or the migration results in the migrated database being in an unusable state.

Preparation tasks can be categorized as follows:

  * Preparations and prerequisites for an Amazon RDS or Amazon Aurora instance
  * Source database preparation and prerequisites
  * Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL instance setup
  * Migration-specific setup



### Amazon RDS or Amazon Aurora instance preparation and prerequisites

Consider the following common setup and prerequisite tasks:

  * Depending on your migration path, you might need to allow remote connections on your RDS instances. If your RDS instance is configured to be private in your VPC, private [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) connectivity must exist between Amazon and Google Cloud.
  * You might need to configure a new security group to allow remote connections on required ports and apply the security group to your Amazon RDS or Amazon Aurora instance:

    * By default, in AWS, network access is turned off for database instances.
    * You can specify rules in a security group that allow access from an IP address range, port, or security group. The same rules apply to all database instances that are associated with that security group.
  * If you are migrating from Amazon RDS, make sure that you have enough free disk to buffer write-ahead logs for the duration of the full load operation on your Amazon RDS instance.

  * For ongoing replication (streaming changes through CDC), you must use a full RDS instance and not a read replica.

  * If you're using built-in replication, you need to set up your Amazon RDS or Amazon Aurora instance for replication for PostgreSQL. Built-in replication or tools that use built-in replication need logical replication for PostgreSQL.

  * If you're using third-party tools, upfront settings and configurations are usually required before using the tool. Check the documentation from the third-party tool.




For more information about instance preparation and prerequisites, see [Set up the external server for replication for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#set_up_the_external_server_for_replication).

### Source database preparation and prerequisites

  * If you choose to use Database Migration Service, configure your source database before connecting to it. For more information, see [Configure your source for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database) and [Configure your source for PostgreSQL to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database).

  * For tables that don't have primary keys, after Database Migration Service migrates the initial backup, only `INSERT` statements will be migrated to the target database during the CDC phase. `DELETE` and `UPDATE` statements are not migrated for those tables.

  * Consider that large objects can't be replicated by Database Migration Service, as the logical decoding facility in PostgreSQL doesn't support decoding changes to large objects.

  * If you choose to use built-in replication, consider that logical replication has certain [limitations with respect to data definition language (DDL) commands, sequences, and large objects](https://www.postgresql.org/docs/current/logical-replication-restrictions.html). Primary keys must exist or be added on tables that are to be enabled for CDC and that go through lots of updates.

  * Some third-party migration tools require that all large object columns are nullable. Any large object columns that are `NOT NULL` need to have that constraint removed during migration.

  * Take baseline measurements on your source environment in production use. Consider the following:

    * Measure the size of your data, as well as your workload's performance. How long do important queries or transactions take, on average? How long during peak times?
    * Document the baseline measurements for later comparison, to help you decide if the fidelity of your database migration is satisfactory. Decide if you can switch your production workloads and decommission your source environment, or if you still need it for fallback purposes.



### Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL instance setup

To have your target instance achieve similar performance levels to that of your source instance, choose the size and specifications of your target PostgreSQL database instance to match those of the source instance. Pay special attention to disk size and throughput, input/output operations per second (IOPS), and number of virtual CPUs (vCPUs). Incorrect sizing can lead to long migration times, database performance problems, database errors, and application performance problems. When deciding on the Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL instance, keep in mind that disk performance is based on the disk size and the number of vCPUs.

You must confirm the following properties and requirements before you create your Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL instances. If you want to change these properties and requirements later, you will need to recreate the instances.

  * Choose the project and [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) of your target Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL instances carefully. Instances can't be migrated between Google Cloud projects and regions without data transfer.

  * Migrate to a matching major version on Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL. For example, if you are using PostgreSQL 14.x on Amazon RDS or Amazon Aurora, you should migrate to Cloud SQL or AlloyDB for PostgreSQL for PostgreSQL version 14.x.

  * Replicate user information separately if you are using built-in database engine backups or Database Migration Service. For details, review the limitations in the Database engine specific backups section.

  * Review the database engine specific configuration flags and compare their source and target instance values. Make sure you understand their impact and whether they need to be the same or not. For example, when working with PostgreSQL, we recommend comparing the values from the `pg_settings` table on your source database to the one on the Cloud SQL and AlloyDB for PostgreSQL instance. Update flag settings as needed on the target database instance to replicate the source settings.

  * Depending on the nature of your workload, you might need to enable specific extensions to support your database. If your workload requires these extensions, review the supported PostgreSQL extensions and how to enable them in Cloud SQL and AlloyDB for PostgreSQL.




For more information about Cloud SQL for PostgreSQL setup, see [Instance configuration options](https://docs.cloud.google.com/sql/docs/postgres/instance-settings), [Database engine specific flags](https://docs.cloud.google.com/sql/docs/postgres/flags), and [supported extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

For more information about AlloyDB for PostgreSQL setup, see [Supported database flags](https://docs.cloud.google.com/alloydb/docs/reference/database-flags) and [supported extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions).

### Migration specific setup

If you can afford downtime, you can import SQL dump files to Cloud SQL and AlloyDB for PostgreSQL. In such cases you might need to create a Cloud Storage bucket to store the database dump.

If you use replication, you must ensure that the Cloud SQL and AlloyDB for PostgreSQL replica has access to your primary (source) database. This access can be gained by using the documented connectivity options.

Depending on your use case and criticality, you might need to implement a fallback scenario, which usually includes reversing the direction of the replication. In this case, you might need an additional replication mechanism from your target Cloud SQL and AlloyDB for PostgreSQL back to your source Amazon instance.

You can decommission the resources that connect your Amazon and Google Cloud environment after the migration is completed and validated.

If you're migrating to AlloyDB for PostgreSQL, consider using a Cloud SQL for PostgreSQL instance as a potential destination for your fallback scenarios. Use the pglogical extension to set up logical replication to that Cloud SQL instance.

For more information, see the following resources:

  * [Best practices for importing and exporting data](https://docs.cloud.google.com/sql/docs/postgres/import-export)
  * Connectivity for [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity) and [PostgreSQL to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity) in Database Migration Service



## Define the execution tasks

Execution tasks implement the migration work itself. The tasks depend on your chosen migration tool, as described in the following subsections.

### Built-in database engine backups

Use the `pg_dump` utility to create a backup. For more information about using this utility to import and export data, see the following resources:

  * [`pg_dump` utility documentation page](https://www.postgresql.org/docs/current/app-pgdump.html)
  * [Import data to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp#import_data_to)
  * [Import a DMP file to AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/import-dmp-file)



### Database Migration Service migration jobs

Define and configure migration jobs in Database Migration Service to migrate data from a source instance to the destination database. Migration jobs connect to the source database instance through user-defined connection profiles.

Test all the prerequisites to ensure the job can run successfully. Choose a time when your workloads can afford a small downtime for the migration and production cut-over.

In Database Migration Service, the migration begins with the initial schema dump and restore without indexes and constraints, followed by the data copy operation. After data copy completes, indexes and constraints are restored. Finally the continuous replication of changes from the source to the destination database instance is started.

Database Migration Service uses the [`pglogical`](https://github.com/2ndQuadrant/pglogical) extension for replication from your source to the target database instance. At the beginning of migration, this extension sets up replication by requiring exclusive short-term locks on all the tables in your source Amazon RDS or Amazon Aurora instance. For this reason, we recommend starting the migration when the database is least busy, and avoiding statements on the source during the dump and replication phase, as DDL statements are not replicated. If you must perform DDL operations, use the 'pglogical' functions to run DDL statements on your source instance or manually run the same DDL statements on the migration target instance, but only after the initial dump stage finishes.

The migration process with Database Migration Service ends with the promotion operation. Promoting a database instance disconnects the destination database from the flow of changes coming from the source database, and then the now standalone destination instance is promoted to a primary instance. This approach is also called a production switch.

For a fully detailed migration setup process, see the quick start guides for [PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres/quickstart)and [PostgreSQL to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quickstart).

### Database engine built-in replication

Cloud SQL supports two types of logical replication: the built-in logical replication of PostgreSQL and logical replication through the pglogical extension. For AlloyDB for PostgreSQL we recommend using the `pglogical` extension for replication. Each type of logical replication has its own features and limitations.

Built-in logical replication has the following features and limitations:

  * It's available in PostgreSQL 10 and later.
  * All changes and columns are replicated. Publications are defined at the table level.
  * Data is only replicated from base tables to base tables.
  * It doesn't perform sequence replication.
  * It's the recommended replication type when there are many tables that have no primary key. Set up built-in PostgreSQL logical replication. For tables without a primary key, apply the `REPLICA IDENTITY FULL` form so that built-in replication uses the entire row as the unique identifier instead of a primary key.



`pglogical` logical replication has the following features and limitations:

  * It's available in all PostgreSQL versions and offers cross version support.
  * Row filtering is available on the source.
  * It doesn't replicate `UNLOGGED` and `TEMPORARY` tables.
  * A primary key or unique key is required on tables to capture `UPDATE` and `DELETE` changes.
  * Sequence replication is available.
  * Delayed replication is possible.
  * It provides conflict detection and configurable resolution if there are multiple publishers or conflicts between replicated data and local changes.



For instructions on how to set up built-in PostgreSQL logical replication from an external server like Amazon RDS or Amazon Aurora for PostgreSQL, see the following resources:

  * [Set up built-in PostgreSQL logical replication](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication#set-up-native-postgresql-logical-replication)
  * [Set up logical replication with pglogical](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication#set-up-logical-replication-with-pglogical)



### Third-party tools

Define any execution tasks for the third-party tool you've chosen.

This section focuses on Striim as an example. Striim uses applications that acquire data from various sources, process the data, and then deliver the data to other applications or targets.

You use one or more flows to organize these migration processes within your custom applications. To code your custom applications, you have a choice of using a graphical programming tool or the Tungsten Query Language (TQL) programming language.

For more information about how to use Striim, see the following resources:

  * Striim basics: [Striim concepts](https://www.striim.com/docs/en/striim-concepts.html)

  * Striim in Google Cloud quickstart: [Running Striim in the Google Cloud](https://www.striim.com/docs/platform/en/running-striim-in-the-google-cloud-platform.html)

  * Configuration settings for continuous replication: [PostgreSQL](https://www.striim.com/docs/en/postgresql-cdc.html) and [SQL Server](https://www.striim.com/docs/en/sql-server-cdc.html#sql-server-setup)

  * Best practices guide: [Switching from an initial load to continuous replication](https://www.striim.com/docs/en/switching-from-initial-load-to-continuous-replication.html)




If you decide to use Striim to migrate your data, see the following guides on how to use Striim to migrate data into Google Cloud:

  * [Striim Migration Service to Google Cloud Tutorials](https://www.striim.com/videos/striim-migration-service-to-google-cloud-tutorials/)
  * [How to Migrate Transactional Databases to AlloyDB for PostgreSQL](https://www.striim.com/videos/how-to-migrate-transactional-databases-to-alloydb/)



## Define fallback scenarios

Define fallback action items for each migration execution task, to safeguard against unforeseen issues that might occur during the migration process. The fallback tasks usually depend on the migration strategy and tools used.

Fallback might require significant effort. As a best practice, don't perform production cut-over until your test results are satisfactory. Both the database migration and the fallback scenario should be properly tested to avoid a severe outage.

Define success criteria and timebox all your migration execution tasks. Doing a migration dry run helps collect information about the expected times for each task. For example, for a scheduled maintenance migration, you can afford the downtime represented by the cut-over window. However, it's important to plan your next action in case the one-time migration job or the restore of the backup fails midway. Depending on how much time of your planned downtime has elapsed, you might have to postpone the migration if the migration task doesn't finish in the expected amount of time.

A fallback plan usually refers to rolling back the migration after you perform the production cut-over, if issues on the target instance appear. If you implement a fallback plan, remember that it must be treated as a full database migration, including planning and testing.

If you choose not to have a fallback plan, make sure you understand the possible consequences. Having no fallback plan can add unforeseen effort and cause avoidable disruptions in your migration process.

Although a fallback is a last resort, and most database migrations don't end up using it, we recommend that you always have a fallback strategy.

### Simple fallback

In this fallback strategy, you switch your applications back to the original source database instance. Adopt this strategy if you can afford downtime when you fall back or if you don't need the transactions committed on the new target system.

If you do need all the written data on your target database, and you can afford some downtime, you can consider stopping writes to your target database instance, taking built-in backups and restoring them on your source instance, and then re-connecting your applications to the initial source database instance. Depending on the nature of your workload and amount of data written on the target database instance, you could bring it into your initial source database system at a later time, especially if your workloads aren't dependent on any specific record creation time or any time ordering constraints.

### Reverse replication

In this strategy, you replicate the writes that happen on your new target database after production cut-over back to your initial source database. In this way, you keep the original source in sync with the new target database and have the writes happening on the new target database instance. Its main disadvantage is that you can't test the replication stream until after you cut-over to the target database instance, therefore it doesn't allow end-to-end testing and it has a small period of no fallback.

Choose this approach when you can still keep your source instance for some time and you migrate using the continuous replication migration.

### Forward replication

This strategy is a variation of reverse replication. You replicate the writes on your new target database to a third database instance of your choice. You can point your applications to this third database, which connects to the server and runs read-only queries while the server is unavailable. You can use any replication mechanism, depending on your needs. The advantage of this approach is that it can be fully end-to-end tested.

Take this approach when you want to be covered by a fallback at all times or when you must discard your initial source database shortly after the production cut-over.

### Duplicate writes

If you choose a Y (writing and reading) or data-access microservice migration strategy, this fallback plan is already set. This strategy is more complicated, because you need to refactor applications or develop tools that connect to your database instances.

Your applications write to both initial source and target database instances, which lets you perform a gradual production cut-over until you are using only your target database instances. If there are any issues, you connect your applications back to the initial source with no downtime. You can discard the initial source and the duplicate writing mechanism when you consider the migration performed with no issues observed.

We recommend this approach when it's critical to have no migration downtime, have a reliable fallback in place, and when you have time and resources to perform application refactoring.

## Perform testing and validation

The goals of this step are to test and validate the following:

  * Successful migration of the data in the database.
  * Integration with existing applications after they are switched to use the new target instance.



Define the key success factors, which are subjective to your migration. The following are examples of subjective factors:

  * Which data to migrate. For some workloads, it might not be necessary to migrate all of the data. You might not want to migrate data that is already aggregated, redundant, archived, or old. You might archive that data in a Cloud Storage bucket, as a backup.
  * An acceptable percentage of data loss. This particularly applies to data used for analytics workloads, where losing part of the data does not affect general trends or performance of your workloads.
  * Data quality and quantity criteria, which you can apply to your source environment and compare to the target environment after the migration.
  * Performance criteria. Some business transactions might be slower in the target environment, but the processing time is still within defined expectations.



The storage configurations in your source environment might not map directly to Google Cloud environment targets. For example, configurations from the [General Purpose SSD (gp2 and gp3) volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html#gp3-ebs-volume-type) with IOPS burst performance or [Provisioned IOPS SSD](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html). To compare and properly size the target instances, benchmark your source instances, in both the assessment and validation phases.

In the benchmarking process, you apply production-like sequences of operations to the database instances. During this time, you capture and process metrics to measure and compare the relative performance of both source and target systems.

For conventional, server based configurations, use relevant measurements observed during peak loads. For flexible resource capacity models like Aurora Serverless, consider looking at historical metric data to observe your scaling needs.

The following tools can be used for testing, validation, and database benchmarking:

  * [HammerDB](https://www.hammerdb.com/about.html): an open source database benchmarking and load testing tool. It supports complex transactional and analytic workloads, based on industry standards, on multiple database engines (both TPROC-C and TPROC-H). HammerDB has detailed documentation and a wide community of users. You can share and compare results across several database engines and storage configurations. For more information, see [Load testing SQL Server using HammerDB](https://docs.cloud.google.com/compute/docs/tutorials/load-testing-sql-server-hammerdb) and [Benchmark Amazon RDS SQL Server performance using HammerDB](https://aws.amazon.com/blogs/database/benchmark-amazon-rds-sql-server-performance-using-hammerdb/).
  * [DBT2 Benchmark Tool](https://dev.mysql.com/downloads/benchmarks.html): benchmarking specialized for MySQL. A set of database workload kits mimics an application for a company that owns warehouses and involves a mix of read and write transactions. Use this tool if you want to use a ready-made online transaction processing (OLTP) load test.
  * [DbUnit](http://www.dbunit.org/): an open source unit testing tool used to test relational database interactions in Java. The setup and use is straightforward, and it supports multiple database engines (MySQL, PostgreSQL, SQL Server, and others). However, the test execution can be slow sometimes, depending on the size and complexity of the database. We recommend this tool when simplicity is important.
  * [DbFit](https://dbfit.github.io/dbfit/docs/): an open source database testing framework that supports test-driven code development and automated testing. It uses a basic syntax for creating test cases and features data-driven testing, version control, and test result reporting. However, support for complex queries and transactions is limited and it doesn't have large community support or extensive documentation, compared to other tools. We recommend this tool if your queries are not complex and you want to perform automated tests and integrate them with your continuous integration and delivery process.



To run an end-to-end test, including testing of the migration plan, always perform a migration dry run exercise. A dry run performs the full-scope database migration without switching any production workloads, and it offers the following advantages:

  * Lets you ensure that all objects and configurations are properly migrated.
  * Helps you define and execute your migration test cases.
  * Offers insights into the time needed for the actual migration, so you can calibrate your timeline.
  * Represents an occasion to test, validate, and adapt the migration plan. Sometimes you can't plan for everything in advance, so this helps you to spot any gaps.



Data testing can be performed on a small set of the databases to be migrated or the entire set. Depending on the total number of databases and the tools used for implementing their migration, you can decide to adopt a risk based approach. With this approach, you perform data validation on a subset of databases migrated through the same tool, especially if this tool is a managed migration service.

For testing, you should have access to both source and target databases and do the following tasks:

  * Compare source and target schemas. Check if all tables and executables exist. Check row counts and compare data at the database level.
  * Run custom data validation scripts.
  * Test that the migrated data is also visible in the applications that switched to use the target database (migrated data is read through the application).
  * Perform integration testing between the switched applications and the target database by testing various use cases. This testing includes both reading and writing data to the target databases through the applications so that the workloads fully support migrated data together with newly created data.
  * Test the performance of the most used database queries to observe if there's any degradation due to misconfigurations or wrong sizing.



Ideally, all these migration test scenarios are automated and repeatable on any source system. The automated test cases suite is adapted to perform against the switched applications.

If you're using Database Migration Service as your migration tool, see either the [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration) or [PostgreSQL to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/verify-migration) version of the "Verify a migration" topic.

### Data Validation Tool

For performing data validation, we recommend that you use the [Data Validation Tool (DVT)](https://github.com/GoogleCloudPlatform/professional-services-data-validator). The DVT is an open sourced Python CLI tool, backed by Google, that provides an automated and repeatable solution for validation across different environments.

The DVT can help streamline the data validation process by offering customized, multi-level validation functions to compare source and target tables on the table, column, and row level. You can also add validation rules.

The DVT covers many Google Cloud data sources, including AlloyDB for PostgreSQL, BigQuery, Cloud SQL, Spanner, JSON, and CSV files on Cloud Storage. It can also be integrated with Cloud Run functions and Cloud Run for event based triggering and orchestration.

The DVT supports the following types of validations:

  * Schema level comparisons
  * Column (including 'AVG', 'COUNT', 'SUM', 'MIN', 'MAX', 'GROUP BY', and 'STRING_AGG')
  * Row (including hash and exact match in field comparisons)
  * Custom query results comparison



For more information about the DVT, see the [Git repository](https://github.com/GoogleCloudPlatform/professional-services-data-validator) and [Data validation made easy with Google Cloud's Data Validation Tool](https://medium.com/google-cloud/dvt-google-clouds-data-validation-tool-bac307779635).

### Perform the migration

The migration tasks include the activities to support the transfer from one system to another.

Consider the following best practices for your data migration:

  * Inform the involved teams whenever a plan step begins and finishes.
  * If any of the steps take longer than expected, compare the time elapsed with the maximum amount of time allotted for that step. Issue regular intermediary updates to involved teams when this happens.
  * If the time span is greater than the maximal amount of time reserved for each step in the plan, consider rolling back.
  * Make "go or no-go" decisions for every step of the migration and cut-over plan.
  * Consider rollback actions or alternative scenarios for each of the steps.



Perform the migration by following your defined execution tasks, and refer to the documentation for your selected migration tool.

### Perform the production cut-over

The high-level production cut-over process can differ depending on your chosen migration strategy. If you can have downtime on your workloads, then your migration cut-over begins by stopping writes to your source database.

For continuous replication migrations, you typically do the following high-level steps in the cut-over process:

  * Stop writing to the source database.
  * Drain the source.
  * Stop the replication process.
  * Deploy the applications that point to the new target database.



After the data has been migrated by using the chosen migration tool, you validate the data in the target database. You confirm that the source database and the target databases are in sync and the data in the target instance adheres to your chosen migration success standards.

Once the data validation passes your criteria, you can perform the application level cut-over. Deploy the workloads that have been refactored to use the new target instance. You deploy the versions of your applications that point to the new target database instance. The deployments can be performed either through rolling updates, staged releases, or by using a blue-green deployment pattern. Some application downtime might be incurred.

Follow the best practices for your production cut-over:

  * Monitor your applications that work with the target database after the cut-over.
  * Define a time period of monitoring to consider whether or not you need to implement your fallback plan.
  * Note that your Cloud SQL or AlloyDB for PostgreSQL instance might need a restart if you change some database flags.
  * Consider that the effort of rolling back the migration might be greater than fixing issues that appear on the target environment.



### Cleanup the source environment and configure the Cloud SQL or AlloyDB for PostgreSQL instance

After the cut-over is completed, you can delete the source databases. We recommend performing the following important actions before the cleanup of your source instance:

  * Create a final backup of each source database. These backups provide you with an end state of the source databases. The backups might also be required in some cases for compliance with some data regulations.

  * Collect the database parameter settings of your source instance. Alternatively, check that they match the ones you've gathered in the inventory building phase. Adjust the target instance parameters to match the ones from the source instance.

  * Collect database statistics from the source instance and compare them to the ones in the target instance. If the statistics are disparate, it's hard to compare the performance of the source instance and target instance.




In a fallback scenario, you might want to implement the replication of your writes on the Cloud SQL instance back to your original source database. The setup resembles the migration process but would run in reverse: the initial source database would become the new target.

As a best practice to keep the source instances up to date after the cut-over, replicate the writes performed on the target Cloud SQL instances back to the source database. If you need to roll back, you can fall back to your old source instances with minimal data loss.

Alternatively, you can use another instance and replicate your changes to that instance. For example, when AlloyDB for PostgreSQL is a migration destination, consider setting up replication to a Cloud SQL for PostgreSQL instance for fallback scenarios.

In addition to the source environment cleanup, the following critical configurations for your Cloud SQL for PostgreSQL instances must be done:

  * Configure a maintenance window for your primary instance to control when disruptive updates can occur.
  * Configure the storage on the instance so that you have at least 20% available space to accommodate any critical database maintenance operations that Cloud SQL may perform. To receive an alert if available disk space gets lower than 20%, create a metrics-based alerting policy for the disk utilization metric.



Don't start an administrative operation before the previous operation has completed.

For more information about maintenance and best practices on Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL instances, see the following resources:

  * [About maintenance on Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/maintenance#management)
  * [About instance settings on Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/instance-settings)
  * [About maintenance on AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance)
  * [Configure an AlloyDB for PostgreSQL instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags)



For more information about maintenance and best practices, see [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/maintenance#management).

## Optimize your environment after migration

Optimization is the last phase of your migration. In this phase, you iterate on optimization tasks until your target environment meets your optimization requirements. The steps of each iteration are as follows:

  1. Assess your current environment, teams, and optimization loop.
  2. Establish your optimization requirements and goals.
  3. Optimize your environment and your teams.
  4. Tune the optimization loop.



You repeat this sequence until you've achieved your optimization goals.

For more information about optimizing your Google Cloud environment, see [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment) and [Google Cloud Well-Architected Framework: Performance optimization](https://docs.cloud.google.com/architecture/framework/performance-optimization).

### Establish your optimization requirements

Review the following optimization requirements for your Google Cloud environment and choose the ones that best fit your workloads:

#### Increase the reliability and availability of your database

With Cloud SQL, you can implement a high availability and disaster recovery strategy that aligns with your recovery time objective (RTO) and recovery point objective (RPO). To increase reliability and availability, consider the following:

  * In cases of read-heavy workloads, add read replicas to offload traffic from the primary instance.
  * For mission critical workloads, use the high-availability configuration, replicas for regional failover, and a robust disaster recovery configuration.
  * For less critical workloads, automated and on-demand backups can be sufficient.
  * To prevent accidental removal of instances, use instance deletion protection.

  * When migrating to Cloud SQL for PostgreSQL, consider using Cloud SQL Enterprise Plus edition to benefit from increased availability, log retention, and near-zero downtime planned maintenance. For more information about Cloud SQL Enterprise Plus, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/editions-intro#edition-features) and [Near-zero downtime planned maintenance](https://docs.cloud.google.com/sql/docs/postgres/maintenance#nearzero).

For more information on increasing the reliability and availability of your Cloud SQL for PostgreSQL database, see the following documents:

    * [Promote replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas)
    * [Cloud SQL database disaster recovery](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery)
    * [About Cloud SQL backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups)
    * [Prevent deletion of an instance documentation](https://docs.cloud.google.com/sql/docs/postgres/deletion-protection)
  * When migrating to [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance), configure backup plans and consider using the AlloyDB for PostgreSQL Auth Proxy. Consider creating and working with secondary clusters for cross-region replication.

For more information on increasing the reliability and availability of your [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance) database, see the following documents:

    * [AlloyDB for PostgreSQL under the hood: Business continuity](https://docs.cloud.google.com/alloydb/docs/maintenance)
    * [About the AlloyDB for PostgreSQL Auth proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview)
    * [Work with cross-region replication](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication)



#### Increase the cost effectiveness of your database infrastructure

To have a positive economic impact, your workloads must use the available resources and services efficiently. Consider the following options:

  * Provide the database with the minimum required storage capacity by doing the following:

    * To scale storage capacity automatically as your data grows, [enable automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen). However, ensure that you configure your instances to have some buffer in peak workloads. Remember that database workloads tend to increase over time.
  * Identify possible overestimated resources:

    * Rightsizing your Cloud SQL instances can reduce the infrastructure cost without adding additional risks to the capacity management strategy.
    * Cloud Monitoring provides predefined dashboards that help identify the health and capacity utilization of many Google Cloud components, including Cloud SQL. For details, see [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#listing_all_dashboards).
  * Identify instances that don't require high availability or disaster recovery configurations, and remove them from your infrastructure.

  * Remove tables and objects that are no longer needed. You can store them in a full backup or an archival Cloud Storage bucket.

  * Evaluate the most cost-effective storage type (SSD or HDD) for your use case.

    * For most use cases, SSD is the most efficient and cost-effective choice.
    * If your datasets are large (10 TB or more), latency-insensitive, or infrequently accessed, HDD might be more appropriate.
    * For details, see [Choose between SSD and HDD storage](https://docs.cloud.google.com/sql/docs/mysql/choosing-ssd-hdd).
  * Purchase [committed use discounts](https://docs.cloud.google.com/sql/cud#pricing) for workloads with predictable resource needs.

  * Use [Active Assist](https://docs.cloud.google.com/solutions/active-assist) to get cost insights and recommendations.

For more information and options, see [Do more with less: Introducing Cloud SQL cost optimization recommendations with Active Assist](https://cloud.google.com/blog/products/databases/reduce-cloud-sql-costs-with-optimizations-by-active-assist).

  * When migrating to Cloud SQL for PostgreSQL, you can reduce overprovisioned instances and identify idle Cloud SQL for PostgreSQL instances.

For more information on increasing the cost effectiveness of your Cloud SQL for PostgreSQL database instance, see the following documents:

    * [Enable automatic storage increases for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen)
    * [Identify idle Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/recommender-sql-idle)
    * [Reduce overprovisioned Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/recommender-sql-overprovisioned)
    * [Optimize queries with high memory usage](https://docs.cloud.google.com/sql/docs/postgres/recommender-optimize-high-memory-queries)
    * [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#listing_all_dashboards)
    * [Choose between SSD and HDD storage](https://docs.cloud.google.com/sql/docs/postgres/choosing-ssd-hdd)
    * [Committed use discounts](https://docs.cloud.google.com/sql/cud#pricing)
    * [Active Assist](https://docs.cloud.google.com/solutions/active-assist)
  * When using [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance), you can do the following to increase cost effectiveness:

    * Use the columnar engine to efficiently perform certain analytical queries such as aggregation functions or table scans.
    * Use cluster storage quota [recommender](https://docs.cloud.google.com/recommender/docs/whatis-activeassist) for AlloyDB for PostgreSQL to detect clusters which are at risk of hitting the storage quota.

For more information on increasing the cost effectiveness of your [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance) database infrastructure, see the following documentation sections:

    * [About the AlloyDB for PostgreSQL columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about)
    * [Optimize underprovisioned AlloyDB for PostgreSQL clusters](https://docs.cloud.google.com/alloydb/docs/recommender-optimize-underprovisioned-cluster)
    * [Increase cluster storage quota for AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/recommender-increase-cluster-storage-quota)
    * [Monitor active queries](https://docs.cloud.google.com/alloydb/docs/monitor-active-queries)



#### Increase the performance of your database infrastructure

Minor database-related performance issues frequently have the potential to impact the entire operation. To maintain and increase your Cloud SQL instance performance, consider the following guidelines:

  * If you have a large number of database tables, they can affect instance performance and availability, and cause the instance to lose its SLA coverage.
  * Ensure that your instance isn't constrained on memory or CPU.

    * For performance-intensive workloads, ensure that your instance has at least 60 GB of memory.
    * For slow database inserts, updates, or deletes, check the locations of the writer and database; sending data over long distances introduces latency.
  * Improve query performance by using the predefined Query Insights dashboard in Cloud Monitoring (or similar database engine built-in features). Identify the most expensive commands and try to optimize them.

  * Prevent database files from becoming unnecessarily large. Set [`autogrow`](https://docs.microsoft.com/en-us/troubleshoot/sql/admin/considerations-autogrow-autoshrink) in MBs rather than as a percentage, using increments appropriate to the requirement.

  * Check reader and database location. Latency affects read performance more than write performance.




When migrating from Amazon RDS and Aurora for PostgreSQL to Cloud SQL for PostgreSQL, consider the following guidelines:

  * Use caching to improve read performance. Inspect the various statistics from the [`pg_stat_database`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW) view. For example, the `blks_hit / (blks_hit + blks_read)` ratio should be greater than 99%. If this ratio isn't greater than 99%, consider increasing the size of your instance's RAM. For more information, see [PostgreSQL statistics collector](https://www.postgresql.org/docs/current/static/monitoring-stats.html).
  * Reclaim space and prevent poor index performance. Depending on how often your data is changing, either set a schedule to run the `VACUUM` command on your Cloud SQL for PostgreSQL.
  * Use Cloud SQL Enterprise Plus edition for increased machine configuration limits and data cache. For more information about Cloud SQL Enterprise Plus, see [Introduction to ](https://docs.cloud.google.com/sql/docs/editions-intro#edition-features)Cloud SQL[ editions](https://docs.cloud.google.com/sql/docs/editions-intro#edition-features).
  * Switch to [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance). If you switch, you can have full PostgreSQL compatibility, better transactional processing, and fast transactional analytics workloads supported on your processing database. You also get a recommendation for new indexes through the use of the index advisor feature.



For more information about increasing the performance of your Cloud SQL for PostgreSQL database infrastructure, see Cloud SQL performance improvement documentation for [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/diagnose-issues#performance).

When migrating from Amazon RDS and Aurora for PostgreSQL to AlloyDB for PostgreSQL, consider the following guidelines to increase the performance of your AlloyDB for PostgreSQL database instance:

  * Use the [AlloyDB for PostgreSQL columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about) to accelerate your analytical queries.
  * Use the [index advisor](https://docs.cloud.google.com/alloydb/docs/use-index-advisor) in [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance). The index advisor tracks the queries that are regularly run against your database and it analyzes them periodically to recommend new indexes that can increase their performance.
  * [Improve query performance by using Query Insights in AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/using-query-insights).



#### Increase database observability capabilities

Diagnosing and troubleshooting issues in applications that connect to database instances can be challenging and time-consuming. For this reason, a centralized place where all team members can see what's happening at the database and instance level is essential. You can monitor Cloud SQL instances in the following ways:

  * Cloud SQL uses built-in memory custom agents to collect query telemetry.

    * Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) to collect measurements of your service and the Google Cloud resources that you use. [Cloud Monitoring](https://docs.cloud.google.com/monitoring) includes predefined dashboards for several Google Cloud products, including a Cloud SQL monitoring dashboard.
    * You can create custom dashboards that help you monitor metrics and set up alert policies so that you can receive timely notifications.
    * Alternatively, you can consider using third-party monitoring solutions that are integrated with Google Cloud, such as Datadog and Splunk.
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) collects logging data from common application components.

  * [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) collects latency data and executed query plans from applications to help you track how requests propagate through your application.

  * [Database Center](https://docs.cloud.google.com/database-center/docs/overview) provides an AI-assisted, centralized database fleet overview. You can monitor the health of your databases, availability configuration, data protection, security, and industry compliance.




For more information about increasing the observability of your database infrastructure, see the following documentation sections:

  * [Monitor Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance)
  * [Monitor instances with AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/monitor-instance)



### General Cloud SQL and AlloyDB for PostgreSQL best practices and operational guidelines

Apply the best practices for Cloud SQL to configure and tune the database.

Some important Cloud SQL general recommendations are as follows:

  * If you have large instances, we recommend that you split them into smaller instances, when possible.
  * Configure storage to accommodate critical database maintenance. Ensure you have at least 20% available space to accommodate any critical database maintenance operations that Cloud SQL might perform.
  * Having too many database tables can affect database upgrade time. Ideally, aim to have under 10,000 tables per instance.
  * Choose the appropriate size for your instances to account for transaction (binary) log retention, especially for high write activity instances.



To be able to efficiently handle any database performance issues that you might encounter, use the following guidelines until your issue is resolved:

**Scale up infrastructure** : Increase resources (such as disk throughput, vCPU, and RAM). Depending on the urgency and your team's availability and experience, vertically scaling your instance can resolve most performance issues. Later, you can further investigate the root cause of the issue in a test environment and consider options to eliminate it.

**Perform and schedule database maintenance operations** : Index defragmentation, statistics updates, vacuum analyze, and reindex heavily updated tables. Check if and when these maintenance operations were last performed, especially on the affected objects (tables, indexes). Find out if there was a change from normal database activities. For example, recently adding a new column or having lots of updates on a table.

**Perform database tuning and optimization** : Are the tables in your database properly structured? Do the columns have the correct data types? Is your data model right for the type of workload? Investigate your [slow queries](https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html) and their execution plans. Are they using the available indexes? Check for index scans, locks, and waits on other resources. Consider adding indexes to support your critical queries. Eliminate non-critical indexes and foreign keys. Consider rewriting complex queries and joins. The time it takes to resolve your issue depends on the experience and availability of your team and can range from hours to days.

**Scale out your reads** : Consider having read replicas. When scaling vertically isn't sufficient for your needs, and database tuning and optimization measures aren't helping, consider scaling horizontally. Routing read queries from your applications to a read replica improves the overall performance of your database workload. However, it might require additional effort to change your applications to connect to the read replica.

**Database re-architecture** : Consider partitioning and indexing the database. This operation requires significantly more effort than database tuning and optimization, and it might involve a data migration, but it can be a long-term fix. Sometimes, poor data model design can lead to performance issues, which can be partially compensated by vertical scale-up. However, a proper data model is a long-term fix. Consider partitioning your tables. Archive data that isn't needed anymore, if possible. Normalize your database structure, but remember that denormalizing can also improve performance.

**Database sharding** : You can scale out your writes by sharding your database. Sharding is a complicated operation and involves re-architecting your database and applications in a specific way and performing data migration. You split your database instance in multiple smaller instances by using a specific partitioning criteria. The criteria can be based on customer or subject. This option lets you horizontally scale both your writes and reads. However, it increases the complexity of your database and application workloads. It might also lead to unbalanced shards called hotspots, which would outweigh the benefit of sharding.

For Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL, consider the following best practices:

  * To offload traffic from the primary instance, add read replicas. You can also use a load balancer such as HAProxy to manage traffic to the replicas. However, avoid too many replicas as this hinders the `VACUUM` operation. For more information on using HAProxy, see the official [HAProxy](http://www.haproxy.org/) website.
  * Optimize the `VACUUM` operation by increasing system memory and the `maintenance_work_mem` parameter. Increasing system memory means that more tuples can be batched in each iteration.
  * Because larger indexes consume a significant amount of time for the index scan, set the `INDEX_CLEANUP` parameter to `OFF` to quickly clean up and freeze the table data.
  * When using [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance), use the AlloyDB for PostgreSQL System Insights dashboard and audit logs. The AlloyDB for PostgreSQL System Insights dashboard displays metrics of the resources that you use, and lets you monitor them. For more details, see the guidelines from the [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance) topic in the [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/maintenance) documentation.



For more details, see the following resources:

  * [General best practices section](https://docs.cloud.google.com/sql/docs/postgres/best-practices) and [Operational Guidelines](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines) for Cloud SQL for PostgreSQL
  * [About maintenance](https://docs.cloud.google.com/alloydb/docs/maintenance) and [Overview](https://docs.cloud.google.com/alloydb/docs/overview) for AlloyDB for PostgreSQL



## What's next

  * Read about [other AWS to Google Cloud migration journeys](https://docs.cloud.google.com/architecture/migration-from-aws-get-started).
  * Learn how to [compare AWS and Azure services to Google Cloud](https://docs.cloud.google.com/free/docs/aws-azure-gcp-service-comparison).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Alex Cârciu](https://www.linkedin.com/in/alex-carciu) | Solutions Architect
  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect



Other contributor: [Somdyuti Paul](https://www.linkedin.com/in/somdyuti-paul-042aa27) | Data Management Specialist

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-09-12 UTC."],[],[]] 
