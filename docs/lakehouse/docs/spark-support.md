---
url: https://docs.cloud.google.com/lakehouse/docs/spark-support/
title: Use Apache Spark with the Lakehouse runtime catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:50:06.256833+00:00
---

# Use Apache Spark with the Lakehouse runtime catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/spark-support/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Use Apache Spark with the Lakehouse runtime catalog Stay organized with collections  Save and categorize content based on your preferences. 

Apache Spark connects to _borderless Lakehouse_ through the _Lakehouse runtime catalog_. This integration uses the _Apache Iceberg REST catalog endpoint_ to provide a standard interface for discovering and managing Apache Iceberg tables.

To get started, see the following guides:

  * [Set up the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog)

  * [Create and query an Iceberg table using the Google Cloud CLI (Quickstart)](https://docs.cloud.google.com/lakehouse/docs/query-iceberg-tables-with-lakehouse)

  * [Set up Spark and Hive with the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore)




## Spark configuration properties

Configure your Spark session or job submission with the following properties to connect to the Apache Iceberg REST catalog endpoint:

Property | Value | Description  
---|---|---  
`spark.sql.catalog.CATALOG_NAME` | `org.apache.iceberg.spark.SparkCatalog` | Registers the Apache Iceberg Spark catalog implementation.  
`spark.sql.catalog.CATALOG_NAME.type` | `rest` | Specifies the REST catalog type.  
`spark.sql.catalog.CATALOG_NAME.uri` | `https://biglake.googleapis.com/iceberg/v1/restcatalog` | Specifies the Apache Iceberg REST catalog endpoint URI in the Lakehouse runtime catalog. To route requests to a [regional endpoint](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints), use `https://biglake.LOCATION.rep.googleapis.com/iceberg/v1/restcatalog`.  
`spark.sql.catalog.CATALOG_NAME.warehouse` | `bl://projects/PROJECT_ID/catalogs/CATALOG_ID` | Specifies the warehouse path for a multiple-bucket catalog in the Lakehouse runtime catalog. For a single-bucket catalog, use `gs://CLOUD_STORAGE_BUCKET_NAME`.  
`spark.sql.catalog.CATALOG_NAME.header.x-goog-user-project` | `PROJECT_ID` | Specifies the Google Cloud project ID for billing and quota on Lakehouse runtime catalog requests.  
`spark.sql.catalog.CATALOG_NAME.rest.auth.type` | `org.apache.iceberg.gcp.auth.GoogleAuthManager` | Configures Google Cloud authentication for the Apache Iceberg REST catalog endpoint.  
`spark.sql.catalog.CATALOG_NAME.io-impl` | `org.apache.iceberg.gcp.gcs.GCSFileIO` | Specifies the Cloud Storage `FileIO` implementation for Apache Iceberg. Required when using credential vending mode.  
`spark.sql.catalog.CATALOG_NAME.header.X-Iceberg-Access-Delegation` | `vended-credentials` | Requests short-lived, downscoped storage credentials from the Lakehouse runtime catalog during table load when using [credential vending mode](https://docs.cloud.google.com/lakehouse/docs/credential-vending).  
`spark.sql.extensions` | `org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions` | Enables Apache Iceberg SQL extensions and optimizations in Spark.  
`spark.sql.defaultCatalog` | `CATALOG_NAME` | Optional: sets the default catalog for the Spark session.  
  
Replace the following:

  * `CATALOG_NAME`: the catalog name identifier configured in your Spark session (for example, `my_catalog`).

  * `LOCATION`: the Google Cloud region where your catalog is located when using a regional endpoint (for example, `us-central1`).

  * `PROJECT_ID`: your Google Cloud project ID.

  * `CATALOG_ID`: the ID of your catalog in the Lakehouse runtime catalog.

  * `CLOUD_STORAGE_BUCKET_NAME`: the name of the Cloud Storage bucket associated with a single-bucket catalog.




For more configuration details, see [Configure client application](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#configure-catalog) and the official [Apache Iceberg Spark documentation](https://iceberg.apache.org/docs/latest/spark-configuration/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
