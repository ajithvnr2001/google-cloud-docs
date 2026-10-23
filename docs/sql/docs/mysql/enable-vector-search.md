---
url: https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search/
title: Enable and disable vector search \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:46.136853+00:00
---

# Enable and disable vector search  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Enable and disable vector search Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Note** : To use the general availability ([GA](https://cloud.google.com/products#product-launch-stages)) version of MySQL vector search, the maintenance version of your instance must be version `MYSQL_8_0_36.R20241208.01_00` or later. For information about how to upgrade your instance to a later version that supports GA vector embeddings, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).   
  
For information about the syntax and behavior of vector embeddings for the [Preview](https://cloud.google.com/products#product-launch-stages) version of this feature, see [Work with vector embeddings (Preview)](https://docs.cloud.google.com/sql/docs/mysql/work-with-vectors-preview).   
  
If you're already using the GA version of vector search in Cloud SQL for MySQL 8.0 or 8.4 and want to upgrade to Cloud SQL for MySQL 9.7, then review the [differences in MySQL vector support in Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/vector-search#version-differences) before you [perform the major version upgrade to Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). 

This section describes how to configure your Cloud SQL instance to support the storage, indexing, and querying of vector embeddings.

Both Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition instances support vector embeddings. All versions of MySQL 8.0.36+ are supported.

## Before you begin

Make sure you have the Cloud SQL Admin and Compute Viewer roles on your user account.

For more information, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions).

## Enable vector search functionality using the database flag

To turn on support for storing vector embeddings in your database in Cloud SQL for MySQL 8.4 and earlier, enable the `cloudsql_vector` MySQL database flag.

If you're using Cloud SQL for MySQL 9.7 or later, then enable the `cloudsql_vector` MySQL database flag to add support for creating vector indexes and for performing [ANN search](https://docs.cloud.google.com/sql/docs/mysql/vector-search#ann_search)
    
    
    gcloud sql instances patch INSTANCE_NAME \
     --database-flags=FLAGS
    

Replace the following:

  * INSTANCE_NAME: the name of the instance where you want to enable vector search functionality.
  * FLAGS: configure the following MySQL flag on your instance:

    * `cloudsql_vector`: set this flag to `on` to enable Cloud SQL vector search functionality. This flag is off by default. When you configure the flag, your command looks similar to the following:
          
          gcloud sql instances patch my-instance \
          --database-flags=cloudsql_vector=on
          

The `cloudsql_vector` flag is static. After you update the instance with the flag (by turning it on or off), your instance restarts automatically in order for the configuration changes to take effect.




For more information about how to configure database flags for MySQL, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

## Disable vector embeddings

Before you disable vector embeddings on your instance, you must explicitly drop all vector indexes on the instance. To learn how to find a list of vector indexes on the instance, see [Monitor vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes#monitor_vector_indexes).

Disabling vector embeddings support prevents you from creating new vector embedding columns if you're using MySQL 8.4 or earlier. If you're using MySQL 9.7 or later, you're prevented from creating vector indexes. It also prevents you from using the `approx_distance` function for vector searches. To turn off support for vector embeddings, set the `cloudsql_vector` flag to `off`. After you configure this static flag, the instance restarts automatically for the configuration change to take effect.

To disable support for vector embeddings, set the `cloudsql_vector` flag to `off`.

For example:
    
    
    gcloud sql instances patch INSTANCE_NAME \
     --database-flags=cloudsql_vector=off
    

Replace INSTANCE_NAME with the name of the instance on which you're turning off vector embedding support.

## What's next

  * Read the [overview about vector search on Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/vector-search).
  * Learn how to [generate vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings#generate_vector_embeddings_based_on_row_data).
  * Learn how to [create vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes).
  * Learn how to [perform searches on vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
