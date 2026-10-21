---
url: https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-lakehouse/
title: About cross-cloud data access \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:16:41.039642+00:00
---

# About cross-cloud data access  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-lakehouse/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  About cross-cloud data access Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, email [biglake-help@google.com](mailto:biglake-help@google.com).

The cross-cloud data access feature lets you query data stored in other cloud providers directly from Google Cloud without migrating files or building complex ETL pipelines with Cross-Cloud Interconnect.

As part of _borderless Lakehouse_ , this capability lets you perform unified analytics and apply AI across your distributed datasets using BigQuery, standalone Apache Spark environments, or [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs).

In addition to analytical queries, you can use your remote data for AI-driven insights and governance:

  * [**Conversational Analytics**](https://docs.cloud.google.com/lakehouse/docs/conversational-analytics): Build specialized agents grounded in your exact data sources, including cross-cloud tables, to analyze data across clouds from a single conversation.
  * [**Knowledge Catalog**](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources): Use Knowledge Catalog features for data profiling and insights with remote data sources.



## Use cases

Lakehouse supports several key use cases for accessing data across multiple cloud providers:

  * **Reduced data movement** lets you query data stored in other cloud environments directly, simplifying data access and processing.
  * **Unified analytics** lets you perform advanced analytics with consistent features and hardware optimization across all your data, regardless of where it resides.
  * **Borderless AI and ML** lets you apply AI models, autonomous agents, and machine learning directly to your remote data without migrating it.



## Architecture

The following diagram illustrates the Lakehouse cross-cloud data access architecture:

![Architecture of Lakehouse cross-cloud data access across
      Google Cloud, Amazon Web Services \(AWS\), and SaaS partners.](https://docs.cloud.google.com/static/lakehouse/images/cross-cloud-data-access-diagram.svg)**Architecture of Lakehouse connects Google Cloud AI and analytics engines to external cloud catalogs, object storage, and SaaS partners.**

The preceding diagram illustrates the architecture across Google Cloud and external cloud and SaaS environments:

  * **Google Cloud** : provides AI, governance, analytics, and cross-cloud data access across remote datasets: 
    * **AI agents and experiences** : builds autonomous agents in [Conversational Analytics](https://docs.cloud.google.com/lakehouse/docs/conversational-analytics) and Gemini Enterprise that search for data and semantic meaning in Knowledge Catalog and execute queries through analytics and processing engines.
    * **Knowledge Catalog** : delivers [unified governance and data lineage](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources), along with [data insights](https://docs.cloud.google.com/lakehouse/docs/dataplex-insights-support), profiling, and data products, by syncing metadata and lineage from Lakehouse.
    * **Analytics and processing engines** : runs BigQuery SQL, BigQuery AI, and Looker workloads, or processes remote data with [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs) and open engines (Apache Spark, Apache Flink, and Trino) by resolving metadata and reading tables through Lakehouse.
    * **Lakehouse cross-cloud data access** : queries remote data in place without file migration or ETL pipelines: 
      * **Metadata synchronization** : discovers and synchronizes table metadata over Apache Iceberg REST and Delta Sharing using the [Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs), authenticates through OpenID Connect (OIDC) or Secret Manager, and vends scoped temporary credentials.
      * **Cross-cloud capabilities (AWS)** : caches read data blocks in Google Cloud using a block-level read-through cache (**Intelligent caching (local cache)**), and routes traffic over Dedicated Cross-Cloud Interconnect (CCI), Partner Interconnect, or the internet (with TLS) using **Cross-cloud network transport**.
  * **External cloud and SaaS data sources** : hosts the remote catalogs, SaaS data clouds, and object storage: 
    * **External cloud and SaaS catalogs** : synchronizes metadata from **Cloud data catalogs** (AWS Glue Data Catalog on AWS, and Databricks Unity Catalog and Snowflake Horizon Catalog on AWS or Google Cloud) and **SaaS data clouds** (Salesforce Data Cloud, Workday Data Lake on AWS or Google Cloud, and SAP Business Data Cloud (BDC)) over the Iceberg REST API and Delta Sharing (for SAP BDC).
    * **External cloud object storage (AWS)** : stores Apache Iceberg tables (Parquet data files) and Amazon S3 Tables in Amazon S3 for direct block reads over CCI or the internet (with TLS).



## How accessing cross-cloud data works

Lakehouse queries remote data using the following process:

  1. **Metadata discovery:** Google Cloud's _Lakehouse_ connects to remote Apache Iceberg REST catalogs, such as Databricks Unity or AWS Glue. Lakehouse discovers the data without copying any files. Depending on the remote catalog provider, Lakehouse authenticates securely through Secret Manager or OIDC token federation with Google as the identity provider.
  2. **Secure transport:** Choosing to route traffic over a private interconnect (for example, Dedicated CCI or Partner Interconnect) significantly reduces data transfer costs compared to the public internet and makes latency highly predictable.
  3. **Optimized execution:** As queries read data from remote clouds, Lakehouse temporarily caches those data segments locally within Google Cloud on specialized storage. Subsequent queries use the local cache, which avoids a significant portion of cross-cloud egress charges.



## Supported catalogs

Lakehouse supports querying data from the following remote catalog providers:

  * **[Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks):** Hosted on Amazon Web Services (AWS) or Google Cloud.
  * **[AWS Glue](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue):** Hosted on AWS.
  * **[Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake):** Hosted on AWS or Google Cloud.
  * **[Workday Data Lake](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday):** Hosted on AWS or Google Cloud.
  * **[SAP Business Data Cloud (BDC)](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc):** Hosted on AWS, Microsoft Azure, or Google Cloud using the SAP BDC connector.



## Core concepts

This section describes the key components essential to using cross-cloud data access feature.

### Metadata layer

The metadata layer connects to remote Apache Iceberg REST catalog endpoints to synchronize Iceberg resource (namespace, table) metadata based on a refresh interval. Lakehouse authenticates securely with OAuth credentials stored in Secret Manager or OIDC token federation.

### Transport layer

The transport layer allows BigQuery and open-source engines to query the data using the synchronized metadata from the metadata layer. For certain types of remote catalogs, Lakehouse supports querying data over the public internet or a dedicated private interconnect.

Select the transport method that matches your architectural and security requirements:

###  Customer-owned (CCI) 

You can configure BigQuery to query data stored in AWS Amazon S3 buckets over a private Cross-Cloud Interconnect using either [**Dedicated Cross-Cloud Interconnect**](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process) or [**Partner Cross-Cloud Interconnect**](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview).

Using a private interconnect provides the following benefits:

  * **Enhanced security:** Data travels across a private network connection between Google Cloud and AWS, avoiding the public internet.
  * **Reduced costs:** Potentially lower egress charges from AWS compared to internet egress, especially when combined with your private interconnect capacity.
  * **Consistent performance:** More predictable network latency and bandwidth compared to the public internet.



#### Architecture overview

To enable private querying, you configure a path from BigQuery to your AWS Amazon S3 bucket through your private interconnect. A key component in the Google Cloud Virtual Private Cloud (VPC) (VPC) is an Internal Load Balancer (ILB). The ILB distributes requests from BigQuery to the private endpoints for Amazon S3 within your AWS VPC, which are provisioned using AWS PrivateLink.

Using an ILB with multiple Elastic Network Interfaces (ENIs) as backends is essential for load balancing, scalability, and high availability. This applies whether you use Dedicated CCI or Partner Interconnect.

The private query workflow follows this process:

  1. BigQuery uses a connection configured with a Service Directory service.
  2. Service Directory resolves the service name to the internal IP address of the Google Cloud ILB.
  3. The ILB receives the requests from BigQuery and distributes them to configured backends.
  4. The ILB backends are Hybrid Connectivity Network Endpoint Groups (NEGs), each pointing to the private IP address of an ENI in your AWS VPC.
  5. Traffic flows from the ILB, through the NEGs, across the private interconnect, to the AWS ENIs.
  6. The AWS ENIs, part of an Amazon S3 VPC Interface Endpoint (AWS PrivateLink), provide private access to the Amazon S3 service.



###  Public internet (no CCI) 

If you do not configure a private interconnect, queries to your remote catalog travel over the public internet by default.

When querying data over the public internet, consider the following implications:

  * **Standard encryption:** Data access requests and data transfers are encrypted in transit using standard TLS protocols across the public internet.
  * **Egress costs:** Data transfer incurs standard internet egress charges from your remote cloud provider (for example, AWS), which are typically higher than private interconnect egress rates.
  * **Variable latency:** Network performance, bandwidth, and latency depend on public internet routing and congestion, resulting in less predictable query execution times compared to a dedicated private interconnect.
  * **Simplified setup:** Requires no additional networking infrastructure, VPC peering, or Service Directory configuration in Google Cloud or your remote cloud provider.



#### Architecture overview

When querying data over the public internet, Lakehouse connects directly to your remote catalog and object storage endpoints without requiring private Google Cloud or remote cloud networking infrastructure.

The public internet query workflow follows this process:

  1. BigQuery initiates a query against a remote table defined in your Lakehouse catalog.
  2. Lakehouse authenticates securely with your remote Apache Iceberg catalog using credentials stored in Secret Manager or OIDC token federation.
  3. Lakehouse retrieves the table metadata and manifest files across the public internet to identify the relevant underlying data files (for example, in AWS Amazon S3).
  4. Data access requests for the underlying objects are sent directly from Google Cloud over the public internet using standard TLS encryption.
  5. The remote storage service verifies the request using temporary, scoped credentials vended by Lakehouse and returns the requested data blocks across the public internet to Google Cloud.



### Intelligent caching

When you query remote cloud data, Lakehouse automatically caches retrieved data blocks locally within Google Cloud. Caching is enabled automatically for all cross-cloud queries to help minimize egress fees from remote cloud providers. Subsequent queries targeting cached data read directly from local Google Cloud storage instead of refetching the data across clouds.

**Egress cost savings**

On the initial query execution, Lakehouse fetches the required data blocks from the remote cloud provider and populates the local cache. Subsequent queries targeting the same data blocks read directly from the local Google Cloud cache instead of refetching the data across clouds.

For workloads with repeated query patterns over the same dataset, caching reduces cross-cloud egress fees by serving data requests from local storage. Actual egress cost savings depend on factors such as query access patterns, data modification rates, and cache retention in the target Google Cloud region.

**Verifying cache usage and egress cost savings in job statistics**

To verify cache hit rates and egress cost savings for a query, inspect the query statistics in the BigQuery console or API (`JobStatistics2`). Because a query can reference data across multiple providers, the job statistics provide a repeated `object_storage_stats` (`objectStorageStats`) field with an entry for each cloud provider accessed during execution.

Each `object_storage_stats` entry reports the following metrics:

  * **`cloud_provider`** (`cloudProvider`): The cloud provider hosting the object storage (for example, `AWS` or `AZURE`).
  * **`cache_bytes_read`** (`cacheBytesRead`): The total bytes read from the local Google Cloud cache, avoiding a remote object storage read.
  * **`object_storage_bytes_read`** (`objectStorageBytesRead`): The total bytes read directly from the remote cloud provider's object storage.



**Data residency and jurisdiction considerations**

Creating a remote catalog or connection in a Google Cloud region stores cached data at rest locally within that target region.

If your remote cloud data resides in a different geographic region or jurisdiction (for example, AWS Amazon S3 in the European Union paired with BigQuery compute in `us-east4`), cross-cloud querying stores data-at-rest cached copies of remote data in the target Google Cloud region. The user or administrator creating the connection or catalog must ensure that cross-jurisdiction caching complies with their organization's data residency, sovereignty, and compliance requirements.

**Encryption and CMEK support**

Customer-managed encryption keys (CMEK) aren't supported for Lakehouse caching. All cached data blocks are encrypted at rest using default Google-owned and Google-managed encryption keys.

If your organization enforces the **Restrict Non-CMEK Services** organization policy constraint (`constraints/gcp.restrictNonCmekServices`), Lakehouse automatically disables caching for queries that access restricted tables. The queries still execute successfully but they do not cache data blocks or benefit from cache-related egress savings.

## What's next

  * Set up a cross-cloud connection for [AWS Glue](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue), [Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks), [Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake), [Workday Data Lake](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday), or [SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
