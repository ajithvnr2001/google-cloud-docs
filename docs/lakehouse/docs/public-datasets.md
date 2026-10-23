---
url: https://docs.cloud.google.com/lakehouse/docs/public-datasets/
title: Borderless Lakehouse public datasets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:46.506614+00:00
---

# Borderless Lakehouse public datasets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/public-datasets/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Resources ](https://docs.cloud.google.com/lakehouse/docs/release-notes)



Send feedback 

#  Borderless Lakehouse public datasets Stay organized with collections  Save and categorize content based on your preferences. 

_Borderless Lakehouse_ hosts high-quality public datasets served through the [Apache Iceberg REST Catalog](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint), making them available to the general public as part of the [Google Cloud Public Dataset Program](https://cloud.google.com/datasets).

These datasets are available for read-only access, and you can access and integrate them into your applications using Apache Spark, Trino, Flink, or BigQuery. Google pays for the storage of these datasets and provides public access to the data through Lakehouse. You pay only for the queries that you perform on the data.

The goal of these public datasets is to lower the barrier to entry for Iceberg. You don't need to manage infrastructure to learn Iceberg, you need to connect. You can use these datasets to:

  * Use BigQuery (through Lakehouse) to query these tables directly using SQL, combining them with your private data.
  * Test your OSS engine (for example, Spark, Trino, or Flink) configurations against a live REST Catalog.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Lakehouse API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Lakehouse API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)




Before you connect with Apache Spark, you must have the following:

  * [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) set up in your environment.



## Public dataset locations

Each public dataset is stored in a specific location such as `US` or `EU`. The Lakehouse public datasets are stored in the `US` multi-region [location](https://docs.cloud.google.com/bigquery/docs/locations). When you query a public dataset, ensure your processing location is compatible with the dataset location.

## Access public datasets using Apache Spark

Because Lakehouse public datasets are served through the [Iceberg REST Catalog](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint), you can access them from Apache Spark and other compatible engines. You can connect to the public dataset using any standard Spark environment such as on-premises, Managed Service for Apache Spark, or other cloud vendors.

### Connect with Apache Spark

Use the following configuration flags when starting your Spark SQL session. These flags configure a catalog named `lakehouse-sample` pointing to the public REST endpoint:
    
    
    spark-sql \
      --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.10.0,org.apache.iceberg:iceberg-gcp-bundle:1.10.0 \
      --conf spark.hadoop.hive.cli.print.header=true \
      --conf spark.sql.catalog.bqms=org.apache.iceberg.spark.SparkCatalog \
      --conf spark.sql.catalog.bqms.type=rest \
      --conf spark.sql.catalog.bqms.uri=https://biglake.googleapis.com/iceberg/v1/restcatalog \
      --conf spark.sql.catalog.bqms.warehouse=gs://CATALOG_NAME \
      --conf spark.sql.catalog.bqms.header.x-goog-user-project=PROJECT_ID \
      --conf spark.sql.catalog.bqms.rest.auth.type=google \
      --conf spark.sql.catalog.bqms.io-impl=org.apache.iceberg.gcp.gcs.GCSFileIO \
      --conf spark.sql.catalog.bqms.header.X-Iceberg-Access-Delegation=vended-credentials \
      --conf spark.sql.defaultCatalog=lakehouse-sample
    

Replace the following:

  * `CATALOG_NAME`: the public dataset catalog name, such as `lakehouse-public-data` or `biglake-public-nyc-taxi-iceberg`.
  * `PROJECT_ID`: your Google Cloud project ID.



### Connect with PySpark and Managed Service for Apache Spark

You can also use a managed, serverless Spark notebook in Managed Service for Apache Spark to query the tables without creating or managing a cluster:
    
    
    from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
    from google.cloud.dataproc_spark_connect import DataprocSparkSession
    
    PROJECT_ID = "PROJECT_ID"
    spark_catalog = "CATALOG_NAME"
    
    session = Session()
    session.runtime_config.properties = {
      "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
      f"spark.sql.catalog.{spark_catalog}": "org.apache.iceberg.spark.SparkCatalog",
      f"spark.sql.catalog.{spark_catalog}.type": "rest",
      f"spark.sql.catalog.{spark_catalog}.uri": "https://biglake.googleapis.com/iceberg/v1/restcatalog",
      f"spark.sql.catalog.{spark_catalog}.rest.auth.type": "org.apache.iceberg.gcp.auth.GoogleAuthManager",
      f"spark.sql.catalog.{spark_catalog}.io-impl": "org.apache.iceberg.gcp.gcs.GCSFileIO",
      f"spark.sql.catalog.{spark_catalog}.header.X-Iceberg-Access-Delegation": "vended-credentials",
      f"spark.sql.catalog.{spark_catalog}.warehouse": f"gs://{spark_catalog}",
      f"spark.sql.catalog.{spark_catalog}.header.x-goog-user-project": PROJECT_ID,
    }
    
    spark = (
       DataprocSparkSession.builder
         .appName("Lakehouse Public Data Demo")
         .dataprocSessionConfig(session)
         .getOrCreate()
    )
    spark.conf.set("spark.sql.defaultCatalog", spark_catalog)
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_NAME`: the public dataset catalog name, such as `lakehouse-public-data` or `biglake-public-nyc-taxi-iceberg`.



### Example queries

Once connected, you have full SQL access to the datasets.

#### Query Wikipedia pageviews and GitHub commits

When connected to the `lakehouse-public-data` catalog in a PySpark session, you can query monthly Wikipedia view counts for BigQuery-related articles:
    
    
    df1 = spark.sql("""
    SELECT
      title,
      wiki,
      SUM(views) AS total_views
    FROM wikipedia.pageviews_2026
    WHERE datehour >= TIMESTAMP '2026-01-01 00:00:00'
      AND datehour <  TIMESTAMP '2026-02-01 00:00:00'
      AND LOWER(title) LIKE '%bigquery%'
    GROUP BY title, wiki
    ORDER BY total_views DESC
    LIMIT 20
    """)
    df1.show(10)
    

You can also retrieve recent GitHub commits referencing Iceberg:
    
    
    df2 = spark.sql("""
    SELECT
      commits.commit,
      commits.subject,
      commits.message,
      commits.author.name AS author_name,
      timestamp_seconds(commits.committer.date.seconds) AS commit_time,
      repo_name
    FROM github_repos.commits AS commits
    WHERE LOWER(commits.subject) LIKE '%iceberg%'
       OR LOWER(commits.message) LIKE '%iceberg%'
    ORDER BY commit_time DESC
    LIMIT 50
    """)
    df2.show(10)
    

#### Query the NYC Taxi dataset

The NYC Taxi dataset is available in the `biglake-public-nyc-taxi-iceberg` catalog, modeled as an Iceberg table to demonstrate partitioning and metadata capabilities.

The following query aggregates millions of records to find the average fare and trip distance by passenger count. It demonstrates how Iceberg efficiently scans data files without needing to list directories by using partition pruning:
    
    
    SELECT
        passenger_count,
        COUNT(1) AS num_trips,
        ROUND(AVG(total_amount), 2) AS avg_fare,
        ROUND(AVG(trip_distance), 2) AS avg_distance
    FROM
        lakehouse-sample.public_data.nyc_taxicab
    WHERE
        data_file_year = 2021
        AND passenger_count > 0
    GROUP BY
        passenger_count
    ORDER BY
        num_trips DESC;
    

One of Iceberg's most powerful features is Time Travel. You can query the table as it existed at a specific point in the past. The following query lets you audit changes by comparing the row count of the current version versus a specific snapshot:
    
    
    -- Compare the row count of the current version vs. a specific snapshot
    SELECT
        'Current State' AS version,
        COUNT(*) AS count
    FROM lakehouse-sample.public_data.nyc_taxicab
    UNION ALL
    SELECT
        'Past State' AS version,
        COUNT(*) AS count
    FROM lakehouse-sample.public_data.nyc_taxicab VERSION AS OF 2943559336503196801Q;
    

By querying the history metadata table (for example, `SELECT * FROM lakehouse-sample.public_data.nyc_taxicab.history`), you can find snapshot IDs and travel back to see how the dataset grew over time.

For more information, see [Use the Iceberg REST catalog with Cloud Storage](https://docs.cloud.google.com/lakehouse/docs/use-lakehouse-metastore-iceberg-rest-catalog).

## Available datasets

Lakehouse provides public datasets and sample tables that you can query as Apache Iceberg tables across two public catalogs: `lakehouse-public-data` and `biglake-public-nyc-taxi-iceberg`.

### `lakehouse-public-data` catalog

The `lakehouse-public-data` catalog (`gs://lakehouse-public-data`) includes the following namespaces and tables in Apache Iceberg format.

#### `austin_bikeshare`

The `austin_bikeshare` namespace includes the following tables:

Name | Description  
---|---  
`bikeshare_trips` | Austin Bikeshare trip records, including trip duration, start and end timestamps, and station details.  
  
#### `bls`

The `bls` namespace includes economic statistics provided by the US Bureau of Labor Statistics:

Name | Description  
---|---  
`cpi_u` | Consumer Price Index for All Urban Consumers (CPI-U) series data.  
`unemployment_cps` | Current Population Survey (CPS) unemployment statistics.  
  
#### `census_bureau_acs`

The `census_bureau_acs` namespace includes the following tables:

Name | Description  
---|---  
`state_2020_5yr` | US Census Bureau American Community Survey (ACS) 5-year state-level estimates for 2020.  
  
#### `chicago_taxi_trips`

The `chicago_taxi_trips` namespace includes the following tables:

Name | Description  
---|---  
`taxi_trips` | Chicago taxi trip records, including trip timestamps, distance, fares, and pickup and dropoff locations.  
  
#### `crypto_ethereum`

The `crypto_ethereum` namespace includes the following tables:

Name | Description  
---|---  
`transactions` | Ethereum blockchain transaction records, including sender and recipient addresses, value, and gas metrics.  
  
#### `ga4_obfuscated_sample_ecommerce`

The `ga4_obfuscated_sample_ecommerce` namespace includes the following tables:

Name | Description  
---|---  
`events_20210131` | Obfuscated Google Analytics 4 event data emulating a web ecommerce implementation for January 31, 2021.  
  
#### `geo_openstreetmap`

The `geo_openstreetmap` namespace includes the following tables:

Name | Description  
---|---  
`planet_features` | OpenStreetMap global geographic features, including feature types, tags, and geometries.  
  
#### `geo_us_boundaries`

The `geo_us_boundaries` namespace includes the following tables:

Name | Description  
---|---  
`zip_codes` | US ZIP Code boundaries, including city, county, state FIPS codes, and geographic geometries.  
  
#### `github_repos`

The `github_repos` namespace includes data from public, open source licensed repositories on GitHub:

Name | Description  
---|---  
`commits` | Unique Git commits from open source repositories on GitHub, grouped by repository.  
`contents` | Unique file contents of text files under 1 MiB on the `HEAD` branch.  
`languages` | Programming languages by repository as reported by the GitHub API.  
`licenses` | Open source license SPDX code for each repository.  
`sample_commits` | Sample of commits from the `commits` table.  
`sample_contents` | Randomly sampled 10% subset of text file contents from the `contents` table.  
`sample_files` | Sampled file metadata for files at `HEAD` from the top 400,000 repositories listed in `sample_repos`.  
`sample_repos` | Top 400,000 GitHub repositories by star count.  
  
#### `google_trends`

The `google_trends` namespace includes the following tables:

Name | Description  
---|---  
`top_terms` | Daily top 25 search terms in the United States with score, ranking, time, and designated market area (DMA).  
  
#### `imdb`

The `imdb` namespace includes the following tables:

Name | Description  
---|---  
`title_basics` | IMDb title metadata, including title type, primary and original titles, release year, runtime, and genres.  
`title_ratings` | IMDb user rating averages and vote counts for titles.  
  
#### `iowa_liquor_sales`

The `iowa_liquor_sales` namespace includes the following tables:

Name | Description  
---|---  
`sales` | Wholesale liquor purchase records in the State of Iowa by retailers for sale to individuals since 2012.  
  
#### `ml_datasets`

The `ml_datasets` namespace includes machine learning benchmark tables:

Name | Description  
---|---  
`census_adult_income` | Census adult income dataset used for classification tasks predicting whether income exceeds $50,000 per year.  
`penguins` | Palmer Archipelago penguin measurements, including species, island, culmen dimensions, flipper length, and body mass.  
`ulb_fraud_detection` | Anonymized credit card transactions by European cardholders from September 2013 for fraud detection benchmarking.  
  
#### `new_york_citibike`

The `new_york_citibike` namespace includes the following tables:

Name | Description  
---|---  
`citibike_trips` | New York City Citi Bike trip records, including trip duration, timestamps, station locations, and rider demographics.  
  
#### `new_york_taxi_trips`

The `new_york_taxi_trips` namespace includes the following tables:

Name | Description  
---|---  
`taxi_zone_geom` | NYC Taxi and Limousine Commission (TLC) taxi zone IDs, names, boroughs, and boundary geometries.  
`tlc_green_trips_2022` | NYC TLC green taxi trip records for 2022.  
`tlc_yellow_trips_2022` | NYC TLC yellow taxi trip records for 2022.  
  
#### `noaa_gsod`

The `noaa_gsod` namespace includes Global Surface Summary of the Day (GSOD) weather data from the National Oceanic and Atmospheric Administration (NOAA):

Name | Description  
---|---  
`gsod2023` | Daily global surface weather summary observations for 2023.  
`stations` | NOAA weather station metadata, including station identifiers, names, countries, states, and coordinates.  
  
#### `sec_quarterly_financials`

The `sec_quarterly_financials` namespace includes the following tables:

Name | Description  
---|---  
`numbers` | Numeric financial statement data extracted from US Securities and Exchange Commission (SEC) quarterly filings.  
  
#### `stackoverflow`

The `stackoverflow` namespace includes the following tables:

Name | Description  
---|---  
`posts_answers` | Stack Overflow answer posts, including body text, score, creation date, and author details.  
`posts_questions` | Stack Overflow question posts, including title, body text, tags, view count, and accepted answer ID.  
`users` | Stack Overflow user profiles, including display name, reputation, creation date, and badge counts.  
  
#### `tpc_ds_1g`

The `tpc_ds_1g` namespace includes TPC-DS 1 GB benchmark tables:

Name | Description  
---|---  
`date_dim` | TPC-DS date dimension table mapping calendar dates to fiscal periods, quarters, and holidays.  
`store_sales` | TPC-DS store sales fact table recording retail store transactions.  
  
#### `wikipedia`

The `wikipedia` namespace includes Wikimedia pageview statistics and Wikidata entities:

Name | Description  
---|---  
`pageviews_2015` | Hourly Wikipedia pageview counts for 2015, partitioned by date.  
`pageviews_2016` | Hourly Wikipedia pageview counts for 2016, partitioned by date.  
`pageviews_2017` | Hourly Wikipedia pageview counts for 2017, partitioned by date.  
`pageviews_2018` | Hourly Wikipedia pageview counts for 2018, partitioned by date.  
`pageviews_2019` | Hourly Wikipedia pageview counts for 2019, partitioned by date.  
`pageviews_2020` | Hourly Wikipedia pageview counts for 2020, partitioned by date.  
`pageviews_2021` | Hourly Wikipedia pageview counts for 2021, partitioned by date.  
`pageviews_2022` | Hourly Wikipedia pageview counts for 2022, partitioned by date.  
`pageviews_2023` | Hourly Wikipedia pageview counts for 2023, partitioned by date.  
`pageviews_2024` | Hourly Wikipedia pageview counts for 2024, partitioned by date.  
`pageviews_2025` | Hourly Wikipedia pageview counts for 2025, partitioned by date.  
`pageviews_2026` | Hourly Wikipedia pageview counts for 2026, partitioned by date.  
`table_activists` | Wikipedia pageview counts for articles about activists.  
`table_actors` | Wikipedia pageview counts for articles about actors.  
`table_alumni` | Wikipedia pageview counts for articles about alumni.  
`table_artists` | Wikipedia pageview counts for articles about artists.  
`table_athlete` | Wikipedia pageview counts for articles about athletes.  
`table_bands` | Wikipedia pageview counts for articles about musical bands.  
`table_born` | Wikipedia pageview counts for articles categorized by birth year.  
`table_businesspeople` | Wikipedia pageview counts for articles about businesspeople.  
`table_comedians` | Wikipedia pageview counts for articles about comedians.  
`table_composers` | Wikipedia pageview counts for articles about composers.  
`table_inventors` | Wikipedia pageview counts for articles about inventors.  
`table_politicians` | Wikipedia pageview counts for articles about politicians.  
`table_scientists` | Wikipedia pageview counts for articles about scientists.  
`table_singers` | Wikipedia pageview counts for articles about singers.  
`table_writers` | Wikipedia pageview counts for articles about writers.  
`wikidata` | Structured Wikidata knowledge base entities, including multilingual labels, descriptions, sitelinks, and claims.  
  
#### `world_bank_health_population`

The `world_bank_health_population` namespace includes World Bank health, nutrition, and population statistics:

Name | Description  
---|---  
`country_series_definitions` | Definitions and metadata linking country codes and indicator series codes.  
`country_summary` | Country metadata, including short and long names, ISO codes, currency units, and regions.  
`health_nutrition_population` | Annual health, nutrition, and population indicator values by country.  
`series_summary` | Metadata for health and population indicators, including definitions, units of measure, and periodicity.  
`series_times` | Time-series metadata and descriptions by indicator series code and year.  
  
#### `world_bank_wdi`

The `world_bank_wdi` namespace includes World Bank World Development Indicators (WDI) data:

Name | Description  
---|---  
`country_summary` | Country metadata, including short and long names, ISO codes, currency units, and income groups.  
`indicators_data` | Annual World Development Indicators values by country and indicator code.  
`series_summary` | Definitions, topics, and units of measure for World Development Indicators series.  
  
### `biglake-public-nyc-taxi-iceberg` catalog

The `biglake-public-nyc-taxi-iceberg` catalog (`gs://biglake-public-nyc-taxi-iceberg`) includes the following tables in the `public_data` namespace in Apache Iceberg format:

Name | Description  
---|---  
`nyc_taxicab` | NYC Taxi and Limousine Commission (TLC) Trip Record Data.  
`nyc_taxicab_2021` | NYC Taxi and Limousine Commission (TLC) Trip Record Data for 2021.  
  
## What's next

  * Learn more about [Apache Iceberg tables managed by Lakehouse](https://docs.cloud.google.com/lakehouse/docs/manage-tables).
  * Learn more about [Lakehouse runtime catalog Iceberg REST Catalog](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
