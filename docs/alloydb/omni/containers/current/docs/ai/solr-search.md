---
url: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/solr-search/
title: Access Apache Solr data from AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:36.811683+00:00
---

# Access Apache Solr data from AlloyDB Omni  |  AlloyDB Omni using containers: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/solr-search/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)



Send feedback 

#  Access Apache Solr data from AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down




**Preview — Solr FDW**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can access and search data stored in [Apache Solr](https://solr.apache.org/) using the external search integration in AlloyDB Omni. This integration lets you offload intensive full-text search, complex query parsing, and advanced faceting workloads from your operational database to Solr, improving query latency and overall system throughput.

**Note:** AlloyDB Omni using RPM and the AlloyDB Omni RPM orchestrator are not supported.

## Before you begin

Before you begin, complete the following:

  * [Install AlloyDB Omni using containers](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/deploy-vm). 
  * [Deploy and run Apache Solr in production](https://solr.apache.org/guide/solr/latest/deployment-guide/taking-solr-to-production.html). 



## Store Solr credentials in Secret Manager

AlloyDB Omni stores and reads your Solr credentials from Secret Manager. For Basic HTTP authentication, the value of the secret in Secret Manager must be a base64-encoded string in the format `username:password`. For more information on how to use Secret Manager, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

Make sure that the service account that AlloyDB Omni uses has the `secretmanager.secretAccessor` permission to read the secret from Secret Manager. For more information, see [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

## Enable and configure the `external_search_fdw` extension

To start your integration with Solr, configure access to your Solr cluster through a foreign data server.

  1. Connect to your database and enable the extension:
         
         CREATE EXTENSION external_search_fdw;
         

  2. Create a foreign server:
         
         CREATE SERVER SOLR_SERVER_NAME
         FOREIGN DATA WRAPPER external_search_fdw
         OPTIONS (
           server 'SOLR_SERVER_HOST_PORT',
           search_provider 'solr',
           auth_mode 'secret_manager',
           auth_method 'AUTH_METHOD',
           secret_path 'SECRET_PATH'
         );
         

Replace the following variables:

     * `SOLR_SERVER_NAME`: name for your foreign data server. For example, `solr`.

     * `SOLR_SERVER_HOST_PORT`: Public-facing URL for your Solr cluster. For example, `https://node1.solr.test.com:8983`.

     * `AUTH_METHOD`: type of authentication to use. For example, `Basic`.

     * `SECRET_PATH`: Secret Manager path to your Solr authentication credentials. For example, `projects/PROJECT_ID/secrets/apikey/versions/1`.

  3. Define the user mapping for the Solr server:
         
         CREATE USER MAPPING FOR CURRENT_USER
         SERVER SOLR_SERVER_NAME;
         

  4. Map the schema of your Solr collection to a PostgreSQL foreign table.
         
         CREATE FOREIGN TABLE SOLR_FD_TABLE(
             metadata external_search_fdw_schema.OpaqueMetadata,
             SOLR_FIELDS)
                SERVER SOLR_SERVER_NAME
                OPTIONS(
                     remote_table_name 'SOLR_COLLECTION_NAME',
                     unique_key_sort_suffix 'UNIQUE_KEY_SORT_SUFFIX'
         );
         

Replace the following variables:

     * `SOLR_FD_TABLE`: the name of the foreign data table that represents your Solr table. For example, `my-fd-solr-table`.

     * `SOLR_FIELDS`: a comma-separated list where each entry follows the format `solr_field_name PG_DATA_TYPE`. For a list of supported Solr data types and their corresponding PostgreSQL types, see [Supported data types](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/elastic-search#supported-data-types).

     * `UNIQUE_KEY_SORT_SUFFIX`: (Optional) the unique key field in Solr, or a comma-separated list of multiple fields with their sort orders—for example, `myid0 ASC, myid1 DESC`, used for pagination. Defaults to `id`.

     * `PG_DATA_TYPE`: the PostgreSQL type that you want to map it to. For example:

       * `TEXT` for string data.
       * `INTEGER` for numeric data.
     * `SOLR_COLLECTION_NAME`: the name of your Solr collection. For example, `my-solr-collection`.




## Query your Solr data

AlloyDB Omni converts SQL queries to Solr REST API queries.

### Standard SQL queries

For the search expression, you can use standard SQL with [Lucene syntax](https://solr.apache.org/guide/solr/latest/query-guide/standard-query-parser.html).
    
    
    SELECT id, body
    FROM SOLR_FD_TABLE
    WHERE FILTER
    ORDER BY metadata <@> 'QUERY';
    

Replace the following variables:

  * `SOLR_FD_TABLE`: name of the foreign data table that represents your Solr table. For example, `my-fd-solr-table`.

  * `FILTER`: (Optional) filter to apply to your Solr query. For example, `a = 10 AND qubits < 105`.

  * `QUERY`: query to send to Solr. For example, `body:database`.




## Query DSL

For advanced use cases — such as implementing nested queries, customized sorting, or complex filtering — use Solr JSON-style [Query DSL](https://solr.apache.org/guide/solr/latest/query-guide/json-query-dsl.html).
    
    
    SELECT id, title
    FROM SOLR_FD_TABLE
    ORDER BY metadata <@> $${
      "query": "title:solr",
      "filter": ["category:software", "inStock:true"],
      "sort": "price desc"
    }$$
    LIMIT 1;
    

Replace `SOLR_FD_TABLE` with the name of the foreign data table that represents your Solr table. For example, `my-fd-solr-table`.

**Note:** For Query DSL, you only need to propagate the `query`, `filter`, and `sort` expressions.

### Hybrid searches

To perform a [hybrid search](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/run-hybrid-vector-similarity-search#hybrid-search) on your Solr data, join Solr token search results with AlloyDB Omni vector search results.
    
    
    SELECT *
    FROM ai.hybrid_search(
      ARRAY[
        '{"limit": LIMIT,
          "weight": WEIGHT,
          "table_name": "SOLR_FD_TABLE",
          "key_column": "id",
          "query_text_input": "QUERY"}'::jsonb
      ])
    ORDER BY score DESC;
    

Replace the following variables:

  * `LIMIT`: number of results to return. For example, `10`.

  * `WEIGHT`: contribution of this search entry to the overall Reciprocal Rank Fusion (RRF). For example, `0.5`. If you don't provide weights, they are distributed evenly. For more information, see [Hybrid search function parameters](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/hybrid-search-function-parameters).

  * `SOLR_FD_TABLE`: name of the foreign data table that represents your Solr table. For example, `my-fd-solr-table`.

  * `QUERY`: query to send to Solr. For example, `body:database`.


**Note:** The `data_type` field in the search entry, as well as the `id_type`, `fusion_algorithm`, and `include_json_output` function parameters, are optional and use default values. For example, the fusion algorithm defaults to `RRF`.

## Troubleshooting

If you encounter authentication or connectivity issues when querying your Solr cluster, check the following:

  * **HTTP 401 or 403 authentication errors** : verify that your Solr secret in Secret Manager contains a base64-encoded string in the format `username:password` and that the service account that AlloyDB Omni uses has the `secretmanager.secretAccessor` permission.

  * **Connection timeouts** : verify network rules and firewall configuration between AlloyDB Omni and your Solr endpoint.




## Limitations

  * **Read-only** : AlloyDB Omni reads, but doesn't write to, Solr data.

  * **Data management** : AlloyDB Omni doesn't automatically index your database data into Solr. You're responsible for populating your Solr collections and maintaining consistency between the data in AlloyDB Omni and the indexed data in Solr.

  * **Schema management** : AlloyDB Omni doesn't automatically synchronize schemas with Solr. If your Solr collection schema changes, manually update the schema of the corresponding PostgreSQL foreign table.

  * **Unsupported types** : specialized Solr types, such as geospatial types, aren't supported.

  * **Stable sorting** : for pagination to work correctly, Solr requires a unique key in the sort expression. By default, the `id` field is used. To specify a custom field, or a comma-separated list of multiple fields along with their individual sort orders, use the `unique_key_sort_suffix` option when you create the foreign table. For example, specify `myid0 ASC, myid1 DESC`.




## What's next

  * Learn how to [Access OpenSearch data](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/opensearch).

  * Learn how to [Access Elasticsearch data](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/elastic-search).

  * Learn how to [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/run-hybrid-vector-similarity-search).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
