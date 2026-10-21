---
url: https://docs.cloud.google.com/feeds/datastream-release-notes.xml
title: Datastream - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:45.113668+00:00
---

# Datastream - Release notes

> Source: https://docs.cloud.google.com/feeds/datastream-release-notes.xml

tag:google.com,2016:datastream-release-notesDatastream - Release notesGoogle Cloud Platform2026-10-09T00:00:00-07:00October 09, 2026tag:google.com,2016:datastream-release-notes#October_09_20262026-10-09T00:00:00-07:00Feature 

Datastream now supports replicating SQL Server `GEOMETRY` and `GEOGRAPHY` spatial data types.

For more information, see the following:

  * [Map SQL Server data types to Datastream unified types](https://docs.cloud.google.com/datastream/docs/unified-types#map-sqlserver)
  * [Data type mappings in BigQuery](https://docs.cloud.google.com/datastream/docs/bq-map-data-types)

]]> September 30, 2026tag:google.com,2016:datastream-release-notes#September_30_20262026-09-30T00:00:00-07:00Feature 

Datastream now supports partial backfill for SQL Server, Spanner, Oracle, PostgreSQL, and MySQL sources. Partial backfill lets you load a specific subset of data from the source into the destination by providing a SQL `WHERE` clause as a custom filter.

For more information, see [Initiate partial backfill](https://docs.cloud.google.com/datastream/docs/manage-backfill-for-the-objects-of-a-stream#initiatepartialbackfill).

]]> September 16, 2026tag:google.com,2016:datastream-release-notes#September_16_20262026-09-16T00:00:00-07:00Feature 

Datastream now supports MongoDB extended JSON canonical mode as the default format for new streams from MongoDB sources to BigQuery destinations.

Canonical mode provides higher data fidelity by explicitly labeling every BSON type to prevent precision loss during data exchange.

For more information, see the following:

  * [Stream data from MongoDB databases](https://docs.cloud.google.com/datastream/docs/sources-mongodb)
  * [MongoDB data types in BigQuery](https://docs.cloud.google.com/datastream/docs/bq-map-data-types#mongodb-data-types)

]]> August 31, 2026tag:google.com,2016:datastream-release-notes#August_31_20262026-08-31T00:00:00-07:00Feature 

You can now create a Datastream stream directly from the overview page of your Cloud SQL instances using the automated flow.

For more information, see [Create a Cloud SQL stream using the automated flow](https://docs.cloud.google.com/datastream/docs/create-a-stream-automated).

]]> July 31, 2026tag:google.com,2016:datastream-release-notes#July_31_20262026-07-31T00:00:00-07:00Feature 

You can now replicate change data from Workday with Datastream. For more information, see [Stream data from Workday](https://docs.cloud.google.com/datastream/docs/sources-workday).

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

]]> July 29, 2026tag:google.com,2016:datastream-release-notes#July_29_20262026-07-29T00:00:00-07:00Feature 

You can now create a Datastream stream directly from the instance or database overview page in Spanner using the automated flow.

For more information, see [Create a Spanner stream using the automated flow](https://docs.cloud.google.com/datastream/docs/create-spanner-stream-automated).

]]> July 15, 2026tag:google.com,2016:datastream-release-notes#July_15_20262026-07-15T00:00:00-07:00Feature 

You can now replicate change data from the following application sources with Datastream:

  * [ServiceNow](https://docs.cloud.google.com/datastream/docs/sources-servicenow)
  * [Salesforce Marketing Cloud](https://docs.cloud.google.com/datastream/docs/sources-salesforce-marketing-cloud)
  * [Microsoft Dataverse](https://docs.cloud.google.com/datastream/docs/sources-dataverse)



This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

]]> June 02, 2026tag:google.com,2016:datastream-release-notes#June_02_20262026-06-02T00:00:00-07:00Feature 

Datastream now offers a free tier for change data capture (CDC) data processed from Google Cloud sources, such as AlloyDB for PostgreSQL and Spanner. You get the first 100 GiB of CDC data for free per billing account, per month.

For more information, see the [Pricing](https://cloud.google.com/datastream/pricing) page.

]]> April 16, 2026tag:google.com,2016:datastream-release-notes#April_16_20262026-04-16T00:00:00-07:00Feature 

You can now create a Datastream stream directly from the overview page of your AlloyDB for PostgreSQL instance using the automated flow. The automated flow simplifies the process of moving data to BigQuery by reducing the number of steps that you need to perform.

For more information, see [Create an AlloyDB for PostgreSQL stream using the automated flow](https://docs.cloud.google.com/datastream/docs/create-alloydb-stream-automated).

]]> April 10, 2026tag:google.com,2016:datastream-release-notes#April_10_20262026-04-10T00:00:00-07:00Feature 

Datastream is now integrated with Knowledge Catalog. This integration lets you search for and browse your Datastream resources, such as streams, connection profiles, and connectivity configurations directly in Knowledge Catalog.

For more information, see [the documentation](https://docs.cloud.google.com/datastream/docs/knowledge-catalog-integration).

]]> April 07, 2026tag:google.com,2016:datastream-release-notes#April_07_20262026-04-07T00:00:00-07:00Feature 

You can now use the [Datastream remote MCP server](https://docs.cloud.google.com/datastream/docs/use-datastream-mcp) to enable LLM agents to perform data-related tasks, such as managing and monitoring your streams, connection profiles, and stream objects.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

]]> January 28, 2026tag:google.com,2016:datastream-release-notes#January_28_20262026-01-28T00:00:00-08:00Feature 

Datastream now supports Spanner as a source. For more information, see the [Datastream documentation](https://docs.cloud.google.com/datastream/docs/sources-spanner).

]]> December 17, 2025tag:google.com,2016:datastream-release-notes#December_17_20252025-12-17T00:00:00-08:00Feature 

Datastream is now available in the following regions:

  * `europe-west10` (Berlin)
  * `europe-west12` (Turin)
  * `me-central1` (Doha)
  * `me-west1` (Tel Aviv)



For the list of all available regions, see [IP allowlists and regions](https://cloud.google.com/datastream/docs/ip-allowlists-and-regions).

]]> November 17, 2025tag:google.com,2016:datastream-release-notes#November_17_20252025-11-17T00:00:00-08:00Feature 

Datastream now supports partitioning and clustering for BigQuery destinations. For more information, see [the documentation](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

]]> September 30, 2025tag:google.com,2016:datastream-release-notes#September_30_20252025-09-30T00:00:00-07:00Feature 

Datastream support for Salesforce as a source is now [generally available (GA)](https://cloud.google.com/products/#product-launch-stages). For more information, see [the documentation](https://cloud.google.com/datastream/docs/sources-salesforce).

]]> September 23, 2025tag:google.com,2016:datastream-release-notes#September_23_20252025-09-23T00:00:00-07:00Feature 

Datastream support for MongoDB as a source is now [generally available (GA)](https://cloud.google.com/products/#product-launch-stages). For more information, see [the documentation](https://docs.cloud.google.com/datastream/docs/sources-mongodb).

]]> June 30, 2025tag:google.com,2016:datastream-release-notes#June_30_20252025-06-30T00:00:00-07:00Feature 

Datastream is now available in the `northamerica-south1` (Mexico) region. For the list of all available regions, see [IP allowlists and regions](https://cloud.google.com/datastream/docs/ip-allowlists-and-regions).

]]> June 23, 2025tag:google.com,2016:datastream-release-notes#June_23_20252025-06-23T00:00:00-07:00Feature 

Datastream now supports BigLake Iceberg tables as a destination both in the Google Cloud console and the Datastream API.

For more information, see the [Datastream documentation](https://cloud.google.com/datastream/docs/destination-blmt).

]]> May 26, 2025tag:google.com,2016:datastream-release-notes#May_26_20252025-05-26T00:00:00-07:00Feature 

Datastream now supports MongoDB as a source. The feature is in **Preview**.

For more information, see the [Datastream documentation](https://cloud.google.com/datastream/docs/sources-mongodb).

]]> May 15, 2025tag:google.com,2016:datastream-release-notes#May_15_20252025-05-15T00:00:00-07:00Feature 

Global transaction identifier (GTID)-based replication for MySQL sources is now [generally available (GA)](https://cloud.google.com/products/#product-launch-stages).

]]> May 13, 2025tag:google.com,2016:datastream-release-notes#May_13_20252025-05-13T00:00:00-07:00Feature 

Datastream is now available in the `europe-north2` (Stockholm) region. For the list of all available regions, see [IP allowlists and regions](https://cloud.google.com/datastream/docs/ip-allowlists-and-regions).

]]> May 05, 2025tag:google.com,2016:datastream-release-notes#May_05_20252025-05-05T00:00:00-07:00Feature 

You can now use Private Service Connect interfaces as a private connectivity method in Datastream. For more information, see [the documentation](https://cloud.google.com/datastream/docs/psc-interfaces).

]]> April 09, 2025tag:google.com,2016:datastream-release-notes#April_09_20252025-04-09T00:00:00-07:00Feature 

The Datastream API now supports streaming data to BigLake managed tables. For more information, see [Stream data to BigLake managed tables (BLMT)](https://cloud.google.com/datastream/docs/destination-bigquery#stream-to-blmt).

]]> March 20, 2025tag:google.com,2016:datastream-release-notes#March_20_20252025-03-20T00:00:00-07:00Feature 

You can now use Secret Manager to securely store authentication resources with Datastream. For more information, see [Use Secret Manager to store sensitive data](https://cloud.google.com/datastream/docs/use-secret-manager).

]]> February 27, 2025tag:google.com,2016:datastream-release-notes#February_27_20252025-02-27T00:00:00-08:00Feature 

Datastream now supports Salesforce as a source. The feature is in **Preview**.

For more information, see the [Datastream documentation](https://cloud.google.com/datastream/docs/sources-salesforce).

]]> December 09, 2024tag:google.com,2016:datastream-release-notes#December_09_20242024-12-09T00:00:00-08:00Feature 

Datastream now supports binary log reader as a CDC method for Oracle sources. The feature is in **Preview**.

For more information, see the [Datastream documentation](https://cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files#access-redo).

]]> November 12, 2024tag:google.com,2016:datastream-release-notes#November_12_20242024-11-12T00:00:00-08:00Feature 

Datastream now supports global transaction identifier (GTID)-based replication for MySQL sources. The feature is in **Preview**.

GTID-based replication supports failovers and managed database clusters, such as Cloud SQL Enterprise Plus edition. For more information, see the [Datastream documentation](https://cloud.google.com/datastream/docs/sources-mysql#gtid).

]]> October 23, 2024tag:google.com,2016:datastream-release-notes#October_23_20242024-10-23T00:00:00-07:00Feature 

Datastream is now available in the `europe-southwest1` (Madrid) region. For the list of all available regions, see [IP allowlists and regions](https://cloud.google.com/datastream/docs/ip-allowlists-and-regions).

]]> October 18, 2024tag:google.com,2016:datastream-release-notes#October_18_20242024-10-18T00:00:00-07:00Feature 

Datastream is now available in the `us-south1` (Dallas) region. For the list of all available regions, see [IP allowlists and regions](https://cloud.google.com/datastream/docs/ip-allowlists-and-regions).

]]> October 11, 2024tag:google.com,2016:datastream-release-notes#October_11_20242024-10-11T00:00:00-07:00Feature 

Datastream is now available in the `me-central2` (Dammam) region. For the list of all available regions, see [IP allowlists and regions](https://cloud.google.com/datastream/docs/ip-allowlists-and-regions).

]]>
