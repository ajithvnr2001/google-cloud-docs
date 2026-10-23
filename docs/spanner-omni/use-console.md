---
url: https://docs.cloud.google.com/spanner-omni/use-console/
title: Use the Spanner Omni console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:32.734984+00:00
---

# Use the Spanner Omni console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/use-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Use the Spanner Omni console Stay organized with collections  Save and categorize content based on your preferences. 

Spanner Omni includes the Spanner Omni console that shows the health and other important information about your deployments.

## Start the Spanner Omni console

Download the Spanner Omni console to run a single instance for your entire deployment. For more information, see [Download Spanner Omni](https://docs.cloud.google.com/spanner-omni/download).

### Use the Spanner Omni console with single-server deployments

To start the Spanner Omni console with a single-server deployment:

  1. Follow the steps in [Set up Spanner Omni](https://docs.cloud.google.com/spanner-omni/setup).

  2. Run the `start-single-server` command to start the Spanner server.

  3. Start the Spanner Omni console. If you are using containers, run the following command:
         
         docker exec -it spanneromni /google/spanner/bin/omni-jre/bin/java -jar /google/spanner/bin/spanner-console
         

The Spanner Omni console uses the same flags that the Spanner Omni CLI uses.

     * To run with TLS, use:
           
           docker exec -it spanneromni /google/spanner/bin/omni-jre/bin/java -jar \
               /google/spanner/bin/spanner-console \
               --ca-certificate-file=PATH_TO_CA_FILE
           

     * To run with mTLS, use:
           
           docker exec -it spanneromni /google/spanner/bin/omni-jre/bin/java -jar \
               /google/spanner/bin/spanner-console \
               --ca-certificate-file=PATH_TO_CA_FILE \
               --client-certificate-directory=PATH_TO_CLIENT_CERT_DIR
           

Replace the following:

     * `PATH_TO_CA_FILE`: the path to the Certificate Authority (CA) certificate file.
     * `PATH_TO_CLIENT_CERT_DIR`: the path to the client certificate directory.
  4. In your browser, go to `http://localhost:15026` to access the Spanner Omni console.




### Use the Spanner Omni console with zonal, regional, and multi-cluster deployments

For Kubernetes-based deployments, the Spanner Omni console is deployed when you create a deployment. To access the Spanner Omni console, in your browser, go to `http://HOST_ADDRESS:15026`.

Replace HOST_ADDRESS with the `EXTERNAL_IP` for `spanner-omni-console` that's in the output of the following command:
    
    
    kubectl get svc -n spanner-ns
    

## Spanner Omni console features

The Spanner Omni console includes several pages that provide insights into your deployment.

### Overview

The **Overview** page is the central dashboard for your Spanner Omni deployment. It provides the following high-level information about the health, status, and resource utilization of your Spanner nodes:

#### Deployment information

This section lists details for your deployment:

  * **Deployment ID** : A unique identifier for your current Spanner Omni deployment. You specify this ID when you create the deployment.

  * **Database version** : The specific version of the Spanner Omni software that you are running (for example, `2026.r4-lts`).

  * **Edition** : The edition of Spanner Omni license installed on the deployment.

  * **License type** : The type of license installed on the deployment. For more information about Spanner Omni editions and license types, see [Spanner Omni editions overview](https://docs.cloud.google.com/spanner-omni/editions-overview#compare-editions-licenses).

  * **License expiration** : The date when the deployment's license expires.




#### Deployment configuration

  * **CPU utilization** : A real-time chart that shows the processing load across your deployment. You can toggle between **Zone** and **Server** to see utilization.

  * **Resource table** : Provides a detailed view of the components in your deployment with the following information. Servers are grouped by zone.

Column | Description  
---|---  
Resource name | The name of the zone or specific Spanner Omni server node.  
Type | 
    * **Zone** : Shows the type of zone (for example, read-write, read-only, or witness). 
    * **Spanner Omni server** : Individual nodes running the Spanner Omni service. The Spanner Omni console identifies root servers specifically.   
Status | Indicates whether the resource is healthy (for example, `Ready`).  
Location | The physical or logical region that hosts the zone (for example, `us-central1`).  
vCPUs, Memory, Storage used | The current resource allocation and utilization for each node and zone.  



### Databases

The **Databases** page provides a centralized view of all databases in your Spanner Omni deployment. The table on this page includes the following information:

Column | Description  
---|---  
Database name | The unique identifier for your database (for example, `retail`, `ycsbdb`).  
Dialect |  The SQL dialect that the database supports: 

  * **GOOGLE_STANDARD_SQL** : The default dialect, offering full Spanner feature support.
  * **POSTGRESQL** : A PostgreSQL-compatible interface.

  
CPU utilization | The percentage of CPU resources the database consumes. This helps you identify high-load databases.  
Tables | The total number of user-defined tables in the database.  
Version retention period | The duration for which Spanner Omni retains historical data for point-in-time recovery (for example, `1h`).  
  
### Backups

The **Backups** page provides a comprehensive view of all backups associated with your Spanner Omni deployment. Backups are transactionally and externally consistent snapshots of your database that Spanner Omni stores in external storage solutions.

For more information, see [Spanner Omni backups](https://docs.cloud.google.com/spanner-omni/backups).

#### Total backup storage

The **Total backup storage** section displays the cumulative size of all backups that you store in your external storage (for example, Amazon Simple Storage Service (Amazon S3), Cloud Storage, or Amazon S3-compatible local storage).

#### Backups table

The backups table shows the following information for each backup:

Column | Description  
---|---  
Backup name | The unique identifier for the backup.  
Source database | The name of the database from which the Spanner Omni console created the backup.  
Status |  The current state of the backup. Common statuses include: 

  * **Ready** : The backup is complete and available for restoration.
  * **Creating** : The backup is in progress.
  * **Expiring soon** : The backup is near its user-specified expiration date.

  
Backup size | The size of the backup data in storage.  
Creation time | The timestamp when the Spanner Omni server initiated the backup process.  
Snapshot time (or Version time) | The point in time that the backup represents. All data in the backup is a consistent snapshot of the database at this moment.  
Expiration time | The date and time when Spanner Omni deletes the backup.  
  
### System insights

The **System Insights** page provides granular observability for your Spanner Omni deployment, which lets you monitor system health, analyze performance, and debug issues.

You can customize the data displayed on the dashboard with the following filters:

  * **Zones** : Filter metrics for specific deployment zones.

  * **Servers** : Drill down into individual server nodes.

  * **Databases** : View metrics for a specific database or the entire deployment.

  * **Time Range** : Select a lookback window from 1 hour up to 7 days.




#### CPU utilization

This section monitors the processing load across your deployment. You can group this metric by:

  * **Zone** : Identify load imbalances between physical locations.

  * **Priority** : See how resources are divided between high, medium, and low priority tasks.

  * **Operation Type** : Break down usage by user-initiated tasks like reads, writes, and commits.




#### Latency

This section tracks the speed of your operations:

  * **Request Latency** : The time taken for individual API requests.

  * **Transaction Latency** : The total time for complete database transactions.

  * **Percentiles** : For example, view this at the 50th percentile (`P50`) for median performance. However, troubleshooting often requires checking `P90` or `P99`.




#### Throughput and operations

This section shows you the following information:

  * **Throughput** : The volume of data the system reads from or writes to the deployment (measured in bytes per second).

  * **Operations per second** : The total count of API calls the system processes.




#### Lock wait time

This metric measures the cumulative time transactions spend waiting for locks. Spikes in this metric, especially when paired with high latency and normal CPU usage, often indicate lock contention.

#### Storage metrics

  * **Storage capacity** : The total and available storage space on the underlying file system, which the Spanner Omni console groups by zone.

  * **Storage utilization** : The number of bytes your databases use. The Spanner Omni data compaction process might cause temporary fluctuations in these numbers.




#### File system performance

This section provides insights into the performance of the underlying storage layer (`SpanhostFS`):

  * **File system latency** : The time taken for low-level I/O operations (read, write, and flush).

  * **File system throughput** : The rate of data transfer at the file system level.




### Query insights

The **Query Insights** page helps you detect and diagnose performance issues for your SQL queries and DML (`INSERT`, `UPDATE`, and `DELETE`) statements. Use Query Insights to identify inefficient queries that might contribute to high CPU utilization.

  * **Detection** : Determine if your queries are the primary cause of your deployment's CPU load.

  * **Identification** : Pinpoint the specific queries or application request tags that are the most resource-intensive.

  * **Analysis** : Use granular metrics like latency and row counts to understand why a query might be slow.




#### Database load by execution time (all queries)

**Database load by execution time** displays the aggregate CPU usage for all queries over time. To show the load for a specific database, use a database filter.

#### Top N queries and tags

This section provides a time-series view of the queries or tags that are causing the most database load within the selected timeframe.

#### Top queries and tags table

The table lists the top-consuming queries and tags. You can use this to identify the most resource-intensive queries in your query workload.

Column | Description  
---|---  
Fingerprint | A unique identifier for a specific query "shape."  
Query or Request tag | The normalized SQL text of the query. If your application provides a request tag in the query options, the Spanner Omni console displays that tag instead, letting you group related queries (for example, `checkout_process`).  
Query type | The type of operation (for example, `QUERY`).  
CPU (%) | The percentage of the total database CPU resources this query consumes during the interval.  
Execution count | The total number of times the Spanner Omni console executed the query.  
Avg latency (ms) | The average time taken to complete the query, including network time between servers.  
Avg rows scanned | The average number of rows Spanner Omni reads to process the query. High scanned-to-returned ratios often indicate missing or inefficient indexes.  
Avg rows returned | The average number of rows the Spanner Omni console sends back to your application.  
Bytes returned | The average amount of data the Spanner Omni console returns per execution.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
