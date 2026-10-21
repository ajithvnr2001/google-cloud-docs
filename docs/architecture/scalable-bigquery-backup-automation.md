---
url: https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/
title: Scalable BigQuery backup automation \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:05.265365+00:00
---

# Scalable BigQuery backup automation  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Scalable BigQuery backup automation Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-09-17 UTC

This architecture provides a framework and [reference deployment](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment) to help you develop your BigQuery backup strategy. This recommended framework and its automation can help your organization do the following:

  * Adhere to your organization's disaster recovery objectives.
  * Recover data that was lost due to human errors.
  * Comply with regulations.
  * Improve operational efficiency.



The scope of BigQuery data can include (or exclude) folders, projects, datasets, and tables. This recommended architecture shows you how to automate the recurrent backup operations at scale. You can use two backup methods for each table: [BigQuery snapshots](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro) and [BigQuery exports to Cloud Storage](https://docs.cloud.google.com/bigquery/docs/exporting-data).

This document is intended for cloud architects, engineers, and data governance officers who want to define and automate data policies in their organizations.

## Architecture

The following diagram shows the automated backup architecture:

![Architecture for the automated backup solution.](https://docs.cloud.google.com/static/architecture/images/bq-backup-manager-diagram.svg)![](https://docs.cloud.google.com/static/architecture/images/bq-backup-manager-diagram.svg)

The workflow that's shown in the preceding diagram includes the following phases:

  1. [Cloud Scheduler](https://docs.cloud.google.com/scheduler) triggers a run to the dispatcher service through a Pub/Sub message, which contains the scope of the BigQuery data that's included and excluded. Runs are scheduled by using a [cron expression](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules).
  2. The dispatcher service, which is built on [Cloud Run](https://docs.cloud.google.com/run), uses the BigQuery API to list the tables that are within the BigQuery scope.
  3. The dispatcher service submits one request for each table to the configurator service through a Pub/Sub message.
  4. The Cloud Run configurator service computes the backup policy of the table from one of the following defined options:

     1. The table-level policy, which is defined by data owners.
     2. The fallback policy, which is defined by the data governance officer, for tables that don't have defined policies.

For details about backup policies, see [Backup policies](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation#backup-policies).

  5. The configurator service submits one request for each table to the next service, based on the computed backup policy.

  6. Depending on the backup method, one of the following custom Cloud Run services submits a request to the BigQuery API and runs the backup process:

     1. The service for BigQuery snapshots backs up the table as a [snapshot](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro).
     2. The service for data exports backs up the table as a [data export to Cloud Storage](https://docs.cloud.google.com/bigquery/docs/exporting-data).
  7. When the backup method is a table data export, a Cloud Logging [log sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) listens to the export jobs completion events in order to enable the asynchronous execution of the next step.

  8. After the backup services complete their operations, Pub/Sub triggers the tagger service.

  9. For each table, the tagger service logs the results of the backup services and updates the backup state in the Cloud Storage metadata layer.




## Products used

This reference architecture uses the following Google Cloud products:

  * [ BigQuery](https://cloud.google.com/bigquery): An enterprise data warehouse that helps you manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence. 
  * [ Cloud Logging](https://cloud.google.com/logging): A real-time log management system with storage, search, analysis, and alerting.
  * [ Pub/Sub](https://cloud.google.com/pubsub): An asynchronous and scalable messaging service that decouples services that produce messages from services that process those messages.
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Cloud Scheduler](https://cloud.google.com/scheduler/docs/overview): A fully managed enterprise-grade cron job scheduler that lets you set up scheduled units of work to be executed at defined times or regular intervals.
  * [ Datastore](https://cloud.google.com/datastore): A highly scalable NoSQL database for your web and mobile applications. 



## Use cases

This section provides examples of use cases for which you can use this architecture.

### Backup automation

As an example, your company might operate in a regulated industry and use BigQuery as the main data warehouse. Even when your company follows best practices in software development, code review, and release engineering, there's still a risk of data loss or data corruption due to human errors. In a regulated industry, you need to minimize this risk as much as possible.

Examples of these human errors include the following:

  * Accidental deletion of tables.
  * Data corruption due to erroneous data pipeline logic.



These types of human errors can usually be resolved with the [time travel](https://docs.cloud.google.com/bigquery/docs/time-travel) feature, which lets you recover data from up to seven days ago. In addition, BigQuery also offers a [fail-safe period](https://docs.cloud.google.com/bigquery/docs/time-travel#fail-safe), during which deleted data is retained in fail-safe storage for an additional seven days after the time travel window. That data is available for emergency recovery through Cloud Customer Care. However, if your company doesn't discover and fix such errors within this combined timeframe, the deleted data is no longer recoverable from its last stable state.

To mitigate this, we recommend that you execute regular backups for any BigQuery tables that can't be reconstructed from source data (for example, historical records or KPIs with evolving business logic).

Your company could use basic scripts to back up tens of tables. However, if you need to regularly back up hundreds or thousands of tables across the organization, you need a scalable automation solution that can do the following:

  * Handle different Google Cloud API limits.
  * Provide a standardized framework for defining backup policies.
  * Provide transparency and monitoring capabilities for the backup operations.



### Backup policies

Your company might also require that the backup policies be defined by the following groups of people:

  * Data owners, who are most familiar with the tables and can set the appropriate _table-level backup policies_.
  * Data governance team, who ensure that a _fallback policy_ is in place to cover any tables that don't have a table-level policy. The fallback policy ensures that certain datasets, projects, and folders are backed up to comply with your company's data retention regulations.



In the deployment for this reference architecture, there are two ways to define the backup policies for tables, and they can be used together:

  * **Data owner configuration** (decentralized): a table-level backup policy, which is manually attached to a table.

    * The data owner defines a table-level JSON file that's stored in a common bucket.
    * Manual policies take precedence over fallback policies when the solution determines the backup policy of a table.
    * For details in the deployment, see [Set table-level backup policies](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment#set-table-level-backup-policies).
  * **Organization default configuration** (centralized): a fallback policy, which applies only to tables that don't have manually-attached policies.

    * A data governance team defines a central JSON file in Terraform, as part of the solution.
    * The fallback policy offers default backup strategies on folder, project, dataset, and table levels.
    * For details in the deployment, see [Define fallback backup policies](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment#define-fallback-policies).



### Backup versus replication

A _backup_ process makes a copy of the table data from a certain point in time, so that it can be restored if the data is lost or corrupted. Backups can be run as a one-time occurrence or recurrently (through a scheduled query or workflow). In BigQuery, point-in-time backups can be achieved with snapshots. You can use snapshots to keep copies of the data beyond the seven-day time travel period within the same storage location as the source data. BigQuery snapshots are particularly helpful for recovering data after human errors that lead to data loss or corruption, rather than recovering from regional failures. BigQuery offers a Service Level Objective (SLO) of [99.9% to 99.99%](https://cloud.google.com/bigquery/sla), depending on the edition.

By contrast, _replication_ is the continuous process of copying database changes to a secondary (or replica) database in a different location. In BigQuery, [cross-region replication](https://docs.cloud.google.com/bigquery/docs/data-replication) can help provide geo-redundancy by creating read-only copies of the data in secondary Google Cloud [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones), which are different from the source data region. However, BigQuery cross-region replication isn't intended for use as a disaster recovery plan for total-region [outage scenarios](https://docs.cloud.google.com/bigquery/docs/data-replication#outage_scenarios). For resilience against regional disasters, consider using [BigQuery managed disaster recovery](https://docs.cloud.google.com/bigquery/docs/managed-disaster-recovery).

BigQuery cross-region replication provides a synchronized read-only copy of the data in a region that is close to the data consumers. These data copies enable collocated joins and avoid cross-regional traffic and cost. However, in cases of data corruption due to human error, replication alone can't help with recovery, because the corrupted data is automatically copied to the replica. In such cases, point-in-time backups (snapshots) are a better choice.

The following table shows a summarized comparison of backup methods and replication:

Method | Frequency | Storage location | Use cases | Costs  
---|---|---|---|---  
Backup  
  
(Snapshots or Cloud Storage export) | One-time or recurrently | Same as the source table data | Restore original data, beyond the time travel period | Snapshots incur [storage charges](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro#storage_costs) for data changes in the snapshot only  
  
Exports can incur standard [storage charges](https://cloud.google.com/storage/pricing#cloud-storage-pricing)  
  
See Cost optimization  
Cross-region replication | Continuously | Remote | Create a replica in another region  
  
One-time migrations between regions | Incurs [charges for storing data](https://cloud.google.com/bigquery/pricing#storage) in the replica  
  
Incurs [data replication](https://cloud.google.com/bigquery/pricing#data_replication) costs  
  
## Design considerations

This section provides guidance for you to consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, cost optimization, operational efficiency, and performance.

### Security, privacy, and compliance

The deployment incorporates the following security measures in its design and implementation:

  * The [network ingress](https://docs.cloud.google.com/run/docs/securing/ingress) setting for Cloud Run accepts only _internal_ traffic, to restrict access from the internet. It also allows only authenticated users and service accounts to call the services.
  * Each Cloud Run service and Pub/Sub subscription uses a separate service account, which has only the required permissions assigned to it. This mitigates the risks associated with using one service account for the system and follows the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).



For privacy considerations, the solution doesn't collect or process personally identifiable information (PII). However, if the source tables have exposed PII, the backups taken of those tables also include this exposed data. The owner of the source data is responsible for protecting any PII in the source tables (for example, by applying [column-level security](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro), [data masking](https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro), or [redaction](https://docs.cloud.google.com/sensitive-data-protection/docs/classification-redaction)). The backups are secure only when the source data is secured. Another approach is to make sure that projects, datasets, or buckets that hold backup data with exposed PII have the required Identity and Access Management (IAM) policies that restrict access to only authorized users.

As a general-purpose solution, the reference deployment doesn't necessarily comply with a particular industry's specific requirements.

### Reliability

This section describes features and design considerations for reliability.

#### Failure mitigation with granularity

To take backups of thousands of tables, it's likely that you might reach API limits for the underlying Google Cloud products (for example, [snapshot](https://docs.cloud.google.com/bigquery/quotas#table_snapshots) and [export](https://docs.cloud.google.com/bigquery/quotas#export_jobs) operation limits for each project). However, if the backup of one table fails due to misconfiguration or other transient issues, that shouldn't affect the overall execution and ability to back up other tables.

To mitigate potential failures, the reference deployment decouples the processing steps by using granular Cloud Run services and connecting them through Pub/Sub. If a table backup request fails at the final tagger service step, Pub/Sub retries only this step and it doesn't retry the entire process.

Breaking down the flow into multiple Cloud Run services, instead of multiple endpoints hosted under one Cloud Run service, helps provide granular control of each service configuration. The level of configuration depends on the service's capabilities and the APIs that it communicates with. For example, the dispatcher service executes once per run, but it requires a substantial amount of time to list all the tables within the BigQuery backup scope. Therefore, the dispatcher service requires higher time-out and memory settings. However, the Cloud Run service for BigQuery snapshots executes once per table in a single run, and completes in less time than the dispatcher service. Therefore, the Cloud Run service requires a different set of configurations at the service level.

#### Data consistency

Data consistency across tables and views is crucial for maintaining a reliable backup strategy. Because data is continuously updated and modified, backups taken at different times might capture different states of your dataset. These backups in different states can lead to inconsistencies when you restore data, particularly for tables that belong to the same functional dataset. For example, restoring a sales table to a point in time that's different from its corresponding inventory table could create a mismatch in available stock. Similarly, database views that aggregate data from multiple tables can be particularly sensitive to inconsistencies. Restoring these views without ensuring that the underlying tables are in a consistent state could lead to inaccurate or misleading results. Therefore, when you design your BigQuery backup policies and frequencies, it's imperative to consider this consistency and ensure that your restored data accurately reflects the real-world state of your dataset at a given point in time.

For example, in the deployment for this reference architecture, data consistency is controlled through the following two configurations in the backup policies. These configurations compute the exact table snapshot time through [time travel](https://docs.cloud.google.com/bigquery/docs/time-travel#time_travel), without necessarily backing up all tables at the same time.

  * `backup_cron`: Controls the frequency with which a table is backed up. The start timestamp of a run is used as a reference point for time travel calculation for all tables that are backed up in this run.
  * `backup_time_travel_offset_days`: Controls how many days in the past should be subtracted from the reference point in time (run start time), to compute the exact time travel version of the table.



#### Automated backup restoration

Although this reference architecture focuses on backup automation at scale, you can consider restoring these backups in an automated way as well. This additional automation can provide similar benefits to those of the backup automation, including improved recovery efficiency and speed, with less downtime. Because the solution keeps track of all backup parameters and results through the tagger service, you could develop a similar architecture to apply the restoration operations at scale.

For example, you could create a solution based on an on-demand trigger that sends a scope of BigQuery data to a dispatcher service, which dispatches one request per table to a configurator service. The configurator service could fetch the backup history that you want for a particular table. The configurator service could then pass it on to either a _BigQuery snapshot restoration service_ or _Cloud Storage restoration service_ to apply the restoration operation accordingly. Lastly, a tagger service could store the results of these operations in a state store. By doing so, the automated restoration framework can benefit from the same design objectives as the backup framework detailed in this document.

### Cost optimization

The framework of this architecture provides backup policies that set the following parameters for overall cost optimization:

  * **Backup method** : The framework offers the following two backup methods: 
    * **BigQuery snapshots** , which incur storage costs based on [updated and deleted data](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro#storage_costs) compared to the base table. Therefore, snapshots are more cost effective for tables that are append-only or have limited updates.
    * **BigQuery exports to Cloud Storage** , which incur standard storage charges. However, for large tables that follow a truncate and load approach, it's more cost effective to back them up as exports in less expensive [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes).
  * **Snapshot expiration** : The time to live (TTL) is set for a single table snapshot, to avoid incurring [storage costs](https://cloud.google.com/bigquery/pricing#storage) for the snapshot indefinitely. Storage costs can grow over time if tables have no expiration.



### Operational efficiency

This section describes features and considerations for operational efficiency.

#### Granular and scalable backup policies

One of the goals of this framework is operational efficiency by scaling up business output while keeping business input relatively low and manageable. For example, the output is a high number of regularly backed up tables, while the input is a small number of maintained backup policies and configurations.

In addition to allowing backup policies at the table level, the framework also allows for policies at the dataset, project, folder, and global level. This means that with a few configurations at higher levels (for example, the folder or project level), hundreds or thousands of tables can be backed up regularly, at scale.

#### Observability

With an automation framework, it's critical that you understand the statuses of the processes. For example, you should be able to find the information for the following common queries:

  * The backup policy that is used by the system for each table.
  * The backup history and backup locations of each table.
  * The overall status of a single run (the number of processed tables and failed tables).
  * The fatal errors that occurred in a single run, and the components or steps of the process in which they occurred.



To provide this information, the deployment writes structured logs to Cloud Logging at each execution step that uses a Cloud Run service. The logs include the input, output, and errors, along with other progress checkpoints. A log sink routes these logs to a BigQuery table. You can run a number of queries to [monitor runs and get reports](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment#monitor_and_report) for common observability use cases. For more information about logs and queries in BigQuery, see [View logs routed to BigQuery](https://docs.cloud.google.com/logging/docs/export/bigquery).

### Performance optimization

To handle thousands of tables at each run, the solution processes backup requests in parallel. The dispatcher service lists all of the tables that are included within the BigQuery backup scope and it generates one backup request per table at each run. This enables the application to process thousands of requests and tables in parallel, not sequentially.

Some of these requests might initially fail for temporary reasons such as reaching the limits of the underlying Google Cloud APIs or experiencing network issues. Until the requests are completed, Pub/Sub automatically retries the requests with the exponential backoff retry policy. If there are fatal errors such as invalid backup destinations or missing permissions, the errors are logged and the execution of that particular table request is terminated without affecting the overall run.

#### Limits

The following quotas and limits apply to this architecture.

For table snapshots, the following applies for each backup operation project that you specify:

  * One project can run up to 100 concurrent table snapshot jobs.
  * One project can run up to 50,000 table snapshot jobs per day.
  * One project can run up to 50 table snapshot jobs per table per day.



For details, see [Table snapshots](https://docs.cloud.google.com/bigquery/quotas#table_snapshots).

For export jobs (exports to Cloud Storage), the following applies:

  * You can export up to 50 TiB of data per day from a project for free, by using the shared slot pool.
  * One project can run up to 100,000 exports per day. To extend this limit, create a slot reservation.



For more information about extending these limits, see [Export jobs](https://docs.cloud.google.com/bigquery/quotas#export_jobs).

Regarding concurrency limits, this architecture uses Pub/Sub to automatically retry requests that fail due to these limits, until they're served by the API. However, for other limits on the number of operations per project per day, these could be mitigated by either a [quota-increase request](https://docs.cloud.google.com/docs/quotas/view-manage), or by spreading the backup operations (snapshots or exports) across multiple projects. To spread operations across projects, configure the backup policies as described in the following deployment sections:

  * [Define fallback backup policies](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment#define-fallback-policies)
  * [Configure additional backup operation projects](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment#additional-backup-projects)
  * [Set table-level backup policies](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment#set-table-level-backup-policies)



## Deployment

To deploy this architecture, see [Deploy scalable BigQuery backup automation](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment).

## What's next

  * Learn more about BigQuery: 
    * [BigQuery table snapshots](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro)
    * [BigQuery table exports to Cloud Storage](https://docs.cloud.google.com/bigquery/docs/exporting-data)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Karim Wadie](https://www.linkedin.com/in/karimwadie) | Strategic Cloud Engineer

Other contributors: 

  * [Chris DeForeest](https://www.linkedin.com/in/chris-deforeest) | Site Reliability Engineer
  * [Eyal Ben Ivri](https://www.linkedin.com/in/eyalbenivri) | Cloud Solutions Architect
  * [Jason Davenport](https://www.linkedin.com/in/davenportjw) | Developer Advocate
  * [Jaliya Ekanayake](https://www.linkedin.com/in/jaliya) | Engineering Manager
  * [Muhammad Zain](https://www.linkedin.com/in/muhammad-zain-ul-islam-96a87994) | Strategic Cloud Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-09-17 UTC."],[],[]] 
