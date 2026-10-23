---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/replication/
title: Replication overview \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:44.285920+00:00
---

# Replication overview  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Replication overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Data Fusion Replication lets you create copies of your data continuously and in real time from operational datastores, such as SQL Server and MySQL, into [BigQuery](https://docs.cloud.google.com/bigquery/docs).

To use Replication, choose one of the following ways:

  * Create a new instance of Cloud Data Fusion and add the Replication app.
  * Add the Replication app to an existing instance.



Benefits include:

  * Identifying schema incompatibilities, connectivity issues, and missing features prior to starting replication, then provides corrective actions.

  * Using the latest operational data in real time for analysis within BigQuery. You use log-based replication directly into BigQuery from Microsoft SQL Server (using [SQL Server CDC](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view)) and MySQL (using [MySQL Binary Log](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html)).

  * Change data capture (CDC) providing a representation of data that has changed in a stream, allowing computations and processing to focus specifically on the most recently changed records. This minimizes outbound data charges on sensitive production systems.

  * Enterprise scalability supporting high-volume transactional databases Initial loads of data to BigQuery are supported with zero-downtime snapshot replication, to make the data warehouse ready for consuming changes continuously. Once the initial snapshot is done, high-throughput, continuous replication of changes starts in real time.

  * The dashboards helping you get real-time insights into replication performance. It's useful for identifying bottlenecks and monitoring data delivery SLAs.

  * Including support for Data Residency, Customer-Managed Encryption Keys (CMEK) and VPC Service Controls. Integration of Cloud Data Fusion within Google Cloud ensures that the highest levels of enterprise security and privacy are observed while making the latest data available in your data warehouse for analytics.




## Recommended pricing

When Replication runs, you're charged for the Managed Service for Apache Spark cluster and you incur processing costs for BigQuery. To optimize these costs, we strongly recommend that you use [BigQuery flat rate pricing](https://cloud.google.com/bigquery/pricing#flat_rate_pricing).

For more information, see the Cloud Data Fusion [Pricing](https://cloud.google.com/data-fusion/pricing) page.

## Replication entities

Entity | Description  
---|---  
Replication | Replication is a capability of Cloud Data Fusion that makes it possible to replicate data continuously at low-latency from operational datastores into analytical data warehouses. Create a replication job by configuring a source and a target with optional transformations.  
Source | Reads database, table, or column change events and makes them available for further processing in a replication job. A replication job contains one source, which relies upon a change capture solution to provide the changes. There can be multiple sources for a database, each with a different change capture solution. A source is a pluggable module built using the plugin architecture of CDAP. If a source is not available to meet your needs, you can build your own by implementing the source interface, and then upload it to CDAP or Cloud Data Fusion.  
Target | Writes changes received from a source into a target database. A replication job contains one target. A target is a pluggable module built using the plugin architecture of CDAP. If a target is not available to meet your needs, you can build your own by implementing the target interface then upload it to CDAP or Cloud Data Fusion.  
Source properties | Configures the source, including connection details, source database and table names, credentials, and other properties.  
Target properties | Configures the target, including connection details, target database and table names, credentials, and other properties.  
Replication job properties | Configures replication job including failure thresholds, staging areas, notifications, and validation settings.  
Draft | A saved, partially completed replication job. When the replication job definition is complete, it can be started.   
Events | Change events in the source to be replicated to the target. Events include inserts, updates, deletes, and DDL (Data Definition Language) changes.  
Insert | Addition of new records in the source.  
Update | Update to existing records in the source.  
Delete | Removal of existing records in the source.  
DDL change | An event that contains a schema change, such as a change in the data type or name.  
Logs | The operational logs of a replication job.  
Replication job detail | A detail page with replication job information, such as its current state, operational metrics, historical view over time, validation results, and its configuration.  
Dashboard | A page that lists the state of all change data capture activities, including throughput, latency, failure rates, and validation results.  
  
## Actions

Actions | Description  
---|---  
Deploy | Creating a new replication job by following a web interface flow to specify a source, target, and their configuration.  
Save | Saving a partially created replication job to resume creation later.  
Delete | Deleting an existing replication job. Only stopped pipelines can be deleted.  
Start | Starting a replication job. If there are changes to be processed, the replication job enters the `active` state; otherwise, it enters the `waiting` state.  
Stop | Stopping a replication job. The replication job stops processing changes from the source.  
View logs | Viewing logs of a replication job for debugging or other analysis.  
Search | Searching for a replication job by its name, description, or other replication job metadata.  
Assess | Assessing the impact of replication prior to starting replication. Assessing a replication job generates an assessment report that flags schema incompatibilities and missing features.  
  
## Monitoring

Replicator states | Description  
---|---  
Deployed | The replication job is deployed, but not started. In this state, a replication job does not replicate events.   
Starting | The replication job is initializing, and is not ready to replicate changes.  
Running | The replication job is started, and is replicating changes.  
Stopping | The replication job is stopping.  
Stopped | The replication job is stopped.  
Failed | The replication job failed due to fatal errors.  
  
## Table states

Concept | Description  
---|---  
Snapshotting | The replication job is taking a snapshot of the current state of the table prior to replicating changes.  
Replicating | The replication job is replicating changes from the source table into the destination table.  
Failing | The replication job is failing to replicate changes from the source table due to error.  
  
## Metrics

Concept | Description  
---|---  
Inserts | The number of inserts applied to the target in the selected time period.  
Updates | The number of updates applied to the target in the selected time period.  
Deletes | The number of deletes applied to the target in the selected time period.  
DDLs | The number of DDL changes applied to the target in the selected time period.  
Throughput | The number of events and the number of bytes replicated to the target in the selected time period.  
Latency | The latency at which data is replicated to the target in the selected time period.  
  
## Components

Component | Description  
---|---  
Service | Oversees the end-to-end orchestration of replication jobs, and provides capabilities for designing, deploying, managing, and monitoring replication jobs. It runs inside the Cloud Data Fusion tenant project (the tenant project is hidden from the user). Its status is displayed on the **System Admin** page of the Cloud Data Fusion web interface.  
State Management | The service manages the state of each replication job in a Cloud Storage bucket in the customer project. The bucket can be configured when the replication job is created. It stores the current offsets and replication state of each replication job.  
Execution | Managed Service for Apache Spark clusters provide the execution environment of replication jobs, which run in your project. replication jobs execute using [ CDAP workers](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480346382/Workers). The size and characteristics of the execution environment are configured with Compute Engine profiles.  
Source database | Your production operational database that replicates into your target database. This database can be located on-premises or on Google Cloud. Cloud Data Fusion Replication supports MySQL, Microsoft SQL Server, and Oracle source databases.  
Change tracking solution | Instead of running on an agent that runs on the source database, Cloud Data Fusion relies on a change tracking solution to read changes in the source database. The solution can be a component of the source database or a separately licensed, third-party solution. In the latter case, the change tracking solution runs on-premises, colocated with the source database, or on Google Cloud. Each source must be associated with a change tracking solution.  


  1. **SQL Server**
     * **Supported solution:** [SQL Server CDC](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server) (change tracking tables)
     * **Additional software:** No
     * **License/cost:** N/A
     * **Comments:** Available SQL Server 2016 and later
  2. **MySQL**
     * **Supported solution:** [ MySQL binary log](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html)
     * **Additional software:** No
     * **License/cost:** N/A
     * **Comments:** N/A
  3. **Oracle**
     * **Supported solution:**[ Oracle LogMiner](https://docs.oracle.com/en/database/oracle/oracle-database/18/sutil/oracle-logminer-utility.html#GUID-3417B738-374C-4EE3-B15C-3A66E01AE2B5)
     * **Additional software:** No
     * **License/cost:** N/A
     * **Comments:** See the [versions supported by Datastream](https://docs.cloud.google.com/datastream/docs/sources#versionsfororaclesourcedb)

  
Target database | The destination location for replication and analysis. Cloud Data Fusion supports the BigQuery target database.  
Authentication | Authentication mechanisms vary according to the source database or change tracking software. When using the built-in capabilities of source databases, such as SQL Server and MySQL, database logins are used for authentication. When using change tracking software, the authentication mechanism of the software is used.  
  
### Connectivity

The following table describes the network connections required for Replication, and the security mechanisms they use.

From | To | Optional | Protocol | Network | Auth Security | Purpose  
---|---|---|---|---|---|---  
Service (Tenant Project) | Source DB | Yes | Depends on Replication source. JDBC for direct database connection. | Peering + Firewall rules + VPN/Interconnect + Router | DB Login | Needed at design, not execution, time Functions: Table listing, Assessment (optional steps; replication can continue without them)  
Service (Tenant Project) | Cloud Storage | No | Cloud API | VPC-SC | IAM | State Management: Offsets, Replication states  
Managed Service for Apache Spark (your project) | Source DB | No | Depends on source. JDBC for direct DB connection. | Peering + Firewall rules + VPN/Interconnect + Router | DB Login | Needed at execution time, for reading changes from source DB to replicate to target  
Managed Service for Apache Spark (your project) | Cloud Storage | No | Cloud API | VPC-SC | IAM | State Management: Offsets, Replication states  
Managed Service for Apache Spark (your project) | BigQuery | No | Cloud API | VPC-SC | IAM | Needed at execution time to apply changes from the source DB to the target  
**Note:** Replication inherits the networking and security capabilities of Cloud Data Fusion, such as [Private IP](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip), [VPC-SC](https://docs.cloud.google.com/data-fusion/docs/how-to/using-vpc-sc), and [CMEK](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys).

## What's next

  * Refer to the [Replication API reference](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref).
  * Refer to the [data type mappings for Replication](https://docs.cloud.google.com/data-fusion/docs/reference/replication-data-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
