---
url: https://docs.cloud.google.com/lakehouse/docs/regional-endpoints/
title: Lakehouse regional endpoints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:56.184144+00:00
---

# Lakehouse regional endpoints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/regional-endpoints/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Lakehouse regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use [Private Service Connect regional endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints) to access resources in the Lakehouse runtime catalog. Regional endpoints let you run your workloads in a manner that complies with [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) and data sovereignty requirements, where your request traffic is routed directly to the region specified in the endpoint.

## Overview

Regional endpoints restrict requests to proceed only if the affected catalog resource exists in the location specified by the endpoint. For example, if you use the endpoint `https://biglake.us-central1.rep.googleapis.com` to access a catalog, namespace, or table, then the request only proceeds if the catalog is located in `us-central1`.

Unlike global endpoints, where requests can be routed through a different location from where the resource resides, regional endpoints restrict your requests to the location specified by the endpoint where the resource resides. Regional endpoints terminate Transport Layer Security (TLS) sessions in the location specified by the endpoint for requests received from the internet, other Google Cloud resources such as Compute Engine virtual machines, on-premises services using Cloud VPN or Cloud Interconnect, and Virtual Private Clouds (VPCs).

Regional endpoints help to ensure data residency by keeping your in-transit catalog requests within the location specified by the endpoint. For more information about how service metadata is handled, see [Note on service data](https://docs.cloud.google.com/assured-workloads/docs/data-residency#service-data).

**Note:** Lakehouse uses the BigLake API (`biglake.googleapis.com`). When configuring regional endpoints for the Lakehouse runtime catalog, use the `biglake.LOCATION.rep.googleapis.com` hostname.

The following catalog endpoints in the Lakehouse runtime catalog are available for use with regional endpoints:

Catalog endpoint | Regional endpoint URL | Reference  
---|---|---  
[Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint) | `https://biglake.LOCATION.rep.googleapis.com/iceberg/v1/restcatalog` | [REST](https://docs.cloud.google.com/lakehouse/docs/reference/rest)  
[Apache Hive catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore) (Preview) | `https://biglake.LOCATION.rep.googleapis.com/hive/v1` | [REST](https://docs.cloud.google.com/lakehouse/docs/reference/rest)  
  
## Supported locations

You can use regional endpoints with the Lakehouse runtime catalog in the following locations:

  * Asia-Pacific

    * Delhi `asia-south2`
    * Mumbai `asia-south1`
  * Europe

    * Belgium `europe-west1`
    * Berlin `europe-west10`
    * Frankfurt `europe-west3`
    * London `europe-west2`
    * Milan `europe-west8`
    * Netherlands `europe-west4`
    * Paris `europe-west9`
    * Zürich `europe-west6`
  * Middle East

    * Dammam `me-central2`
  * Americas

    * Columbus, Ohio `us-east5`
    * Dallas `us-south1`
    * Iowa `us-central1`
    * Las Vegas `us-west4`
    * Los Angeles `us-west2`
    * Montréal `northamerica-northeast1`
    * Northern Virginia `us-east4`
    * Oregon `us-west1`
    * Salt Lake City `us-west3`
    * South Carolina `us-east1`
    * Toronto `northamerica-northeast2`



## Supported operations and storage locations

Regional endpoints can only be used to perform operations that access or mutate catalog resources replicated in the location specified by the endpoint:

  * **Regional catalog isolation** : Listing catalogs through `https://biglake.LOCATION.rep.googleapis.com` returns only catalogs located in `LOCATION`. Requests to get, update, or delete a catalog, namespace, or table located outside of `LOCATION` return a `404 NOT_FOUND` error.
  * **Default storage location** : When you create a catalog using a regional endpoint, the Cloud Storage bucket specified in `default_location` for a multiple-bucket catalog ([`CATALOG_TYPE_BIGLAKE`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs#CatalogType)) or the bucket associated with a single-bucket catalog ([`CATALOG_TYPE_GCS_BUCKET`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs#CatalogType)) must reside in `LOCATION`.
  * **Multiple-bucket catalog restricted locations** : For multiple-bucket catalogs, you can configure additional Cloud Storage buckets in `restricted_locations` as long as those buckets reside within the same geographic jurisdiction (such as the US or Europe) as `LOCATION`. For more information, see [Multiple-bucket catalog](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#storage-multiple-buckets).



## Limitations and restrictions

Regional endpoints cannot be used to perform the following operations:

  * Operations that read or modify catalogs, namespaces, or tables located outside of the region specified by the endpoint.
  * Multi-region endpoint routing (such as `US` or `EU`). Regional endpoints must specify a single region.



Keep in mind the following restrictions when using regional endpoints:

  * Regional endpoints don't support [mutual Transport Layer Security (mTLS)](https://docs.cloud.google.com/chrome-enterprise-premium/docs/understand-mtls).
  * Using a regional endpoint doesn't by itself restrict users from creating resources in other regions or calling the global endpoint (`biglake.googleapis.com`). To enforce regional restrictions, configure the [Organization Policy Service resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) and restrict global API endpoint usage.



## Configure tools and query engines

You can configure the Google Cloud CLI, Apache Spark, Trino, and direct REST API requests to use regional endpoints.

### gcloud CLI

To configure the gcloud CLI to use regional endpoints with `gcloud biglake` commands, set the `api_endpoint_overrides/biglake` property to the regional endpoint that you want to use:
    
    
    gcloud config set api_endpoint_overrides/biglake https://biglake.LOCATION.rep.googleapis.com/
    

Alternatively, you can set the `CLOUDSDK_API_ENDPOINT_OVERRIDES_BIGLAKE` environment variable for individual commands:
    
    
    CLOUDSDK_API_ENDPOINT_OVERRIDES_BIGLAKE=https://biglake.LOCATION.rep.googleapis.com/ \
        gcloud biglake iceberg catalogs list --project=PROJECT_ID
    

Replace the following:

  * `LOCATION`: the supported region for your catalog (for example, `us-central1`).
  * `PROJECT_ID`: your Google Cloud project ID.



### Apache Spark

When configuring an Spark session to connect to the Apache Iceberg REST catalog endpoint, set the `spark.sql.catalog.CATALOG_NAME.uri` property to the regional endpoint URL:
    
    
    from pyspark.sql import SparkSession
    
    catalog_name = "CATALOG_NAME"
    spark = SparkSession.builder.appName("APP_NAME") \
        .config('spark.sql.defaultCatalog', 'CATALOG_NAME') \
        .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
        .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
        .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.LOCATION.rep.googleapis.com/iceberg/v1/restcatalog') \
        .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'bl://projects/PROJECT_ID/catalogs/CATALOG_ID') \
        .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
        .config(f'spark.sql.catalog.{catalog_name}.rest.auth.type', 'org.apache.iceberg.gcp.auth.GoogleAuthManager') \
        .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'org.apache.iceberg.gcp.gcs.GCSFileIO') \
        .config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation', 'vended-credentials') \
        .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
        .getOrCreate()

Replace the following:

  * `CATALOG_NAME`: a name for the local Spark catalog (for example, `my_catalog`).
  * `APP_NAME`: a name for your Spark session.
  * `LOCATION`: the supported region where the catalog is located (for example, `us-central1`).
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your multiple-bucket catalog.



For more configuration options, see [Set up the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#configure-catalog).

### Trino

When creating a Managed Service for Apache Spark cluster with the Trino component, set `trino-catalog:CATALOG_NAME.iceberg.rest-catalog.uri` to the regional endpoint URL:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --enable-component-gateway \
        --region=LOCATION \
        --image-version=DATAPROC_VERSION \
        --network=NETWORK_ID \
        --optional-components=TRINO \
        --properties="\
        trino-catalog:CATALOG_NAME.connector.name=iceberg,\
        trino-catalog:CATALOG_NAME.iceberg.catalog.type=rest,\
        trino-catalog:CATALOG_NAME.iceberg.rest-catalog.uri=https://biglake.LOCATION.rep.googleapis.com/iceberg/v1/restcatalog,\
        trino-catalog:CATALOG_NAME.iceberg.rest-catalog.warehouse=bl://projects/PROJECT_ID/catalogs/CATALOG_ID,\
        trino-catalog:CATALOG_NAME.iceberg.rest-catalog.biglake.project-id=PROJECT_ID,\
        trino-catalog:CATALOG_NAME.iceberg.rest-catalog.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager"

Replace the following:

  * `CLUSTER_NAME`: a name for your cluster.
  * `LOCATION`: the supported region for your cluster and catalog.
  * `DATAPROC_VERSION`: the Managed Service for Apache Spark image version (for example, `2.2`).
  * `NETWORK_ID`: the cluster network ID.
  * `CATALOG_NAME`: the name of your Trino catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your multiple-bucket catalog.



### REST APIs

Instead of sending a REST request to the global endpoint (`https://biglake.googleapis.com`), send the request to the regional endpoint in the following format: `https://biglake.LOCATION.rep.googleapis.com`.

For example, to list catalogs in `LOCATION` using the Apache Iceberg REST catalog endpoint extensions API:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "x-goog-user-project: PROJECT_ID" \
        "https://biglake.LOCATION.rep.googleapis.com/iceberg/v1/restcatalog/extensions/projects/PROJECT_ID/catalogs"

## Restrict global API endpoint usage

To help enforce the use of regional endpoints, use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint (`biglake.googleapis.com`). For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

The following example organization policy YAML file denies requests to the global `biglake.googleapis.com` endpoint while allowing requests to regional endpoints:
    
    
    name: projects/PROJECT_ID/policies/gcp.restrictEndpointUsage
    spec:
      rules:
      - values:
          deniedValues:
          - under:services/biglake.googleapis.com
    

## What's next

  * Learn more about the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint).
  * [Set up the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog).
  * Learn about [Identity and Access Management and access control](https://docs.cloud.google.com/lakehouse/docs/iam-and-access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
