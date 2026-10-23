---
url: https://docs.cloud.google.com/alloydb/docs/solr-search/
title: Access Solr data from AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:12.234519+00:00
---

# Access Solr data from AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/solr-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Access Solr data from AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Solr FDW**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can access and search data stored in [Apache Solr](https://solr.apache.org/) using the external search integration in AlloyDB for PostgreSQL.

## Before you begin

Before you begin, make sure that you've completed the following:

  * [Add outbound public IP connectivity](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#add-outbound-connectivity) on your primary AlloyDB instance.

  * Deploy and run your Solr cluster with an accessible public-facing URL.




## Store Solr credentials in Secret Manager

AlloyDB stores and reads your Solr credentials from Secret Manager. For Basic authentication, the value of the secret in Secret Manager must be a base64-encoded string in the format `username:password`. For more information on how to use Secret Manager, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

Ensure that your AlloyDB service account has the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role to read the secret from Secret Manager. For more information, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

## Enable and configure the `external_search_fdw` extension

To start your integration with Solr, configure access to your Solr cluster through a foreign data server.
    
    
    CREATE EXTENSION external_search_fdw;
    
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

  * `SOLR_SERVER_HOST_PORT`: Public-facing URL for your SOLR cluster. For example, `https://node1.solr.test.com:8983`.

  * `AUTH_METHOD`: type of authentication to use. For example, `Basic`.

  * `SECRET_PATH`: Secret Manager path to your Solr authentication credentials. For example, `projects/123456789012/secrets/apikey/versions/1`. `123456789012` represents your Google Cloud project ID.



  1. Define the PostgreSQL user mapping for the Solr server. Note that PostgreSQL FDWs require this user mapping to function. AlloyDB authenticates using the REST authorization header.
         
         CREATE USER MAPPING FOR CURRENT_USER
         SERVER SOLR_SERVER_NAME;
         

  2. Map the schema of your Solr collection to a PostgreSQL foreign table.
         
         CREATE FOREIGN TABLE SOLR_FD_TABLE(
             metadata external_search_fdw_schema.OpaqueMetadata,
             SOLR_FIELDS)
                SERVER SOLR_SERVER_NAME
                OPTIONS(
                     remote_table_name 'SOLR_COLLECTION_NAME'
                     unique_key_sort_suffix 'UNIQUE_KEY_SORT_SUFFIX'
                );
         

Replace the following new variables:

     * `SOLR_FD_TABLE`: name of the foreign data table that represents your Solr table. For example, `my-fd-solr-table`.

     * `SOLR_FIELDS`: a comma-separated list where each entry follows the format `solr_field_name PG_DATA_TYPE`. For a list of supported Solr data types and their corresponding PostgreSQL types, see [Supported data types](https://docs.cloud.google.com/alloydb/docs/elastic-search#supported-data-types).

     * `UNIQUE_KEY_SORT_SUFFIX`: (Optional) the unique key field in Solr, or a comma-separated list of multiple fields with their sort orders, for example, `myid0 ASC, myid1 DESC`, used for pagination. Defaults to `id`.

     * `PG_DATA_TYPE`: the PostgreSQL type you want to map it to. Common examples include:

       * `TEXT` for string data.
       * `INTEGER` for numeric data.
     * `SOLR_COLLECTION_NAME`: name of your Solr collection. For example, `my-solr-collection`.




## Query your Solr data

AlloyDB takes SQL queries and converts them to Solr REST API queries.

To query your Solr data, you have the following options:

  * Standard SQL queries
  * Query DSL
  * Hybrid searches



### Standard SQL queries

You can use standard SQL with [Lucene syntax](https://solr.apache.org/guide/solr/latest/query-guide/standard-query-parser.html) for the search expression.
    
    
    SELECT id, body
    FROM SOLR_FD_TABLE
    WHERE FILTER
    ORDER BY metadata <@> 'QUERY';
    

Replace the following variables:

  * `SOLR_FD_TABLE`: name of the foreign data table that represents your Solr table. For example, `my-fd-solr-table`.

  * (Optional) `FILTER`: filter to apply to your Solr query. For example, `AND qubits < 105`.

  * `QUERY`: query to send to Solr. For example, `body:database`.




### Query DSL

For advanced use cases, use Solr JSON-style [Query DSL](https://solr.apache.org/guide/solr/latest/query-guide/json-query-dsl.html).
    
    
    SELECT id, title
    FROM SOLR_FD_TABLE
    ORDER BY metadata <@> $${
      "query": "title:solr",
      "filter": ["category:software", "inStock:true"],
      "sort": "price desc"
    }$$
    LIMIT 1;
    

Replace `SOLR_FD_TABLE` with the name of the foreign data table that represents your Solr table. For example, `my-fd-solr-table`.

**Note:** For Query DSL, you're only expected to propagate the `query`, `filter`, and `sort` expressions.

### Hybrid searches

To perform a [hybrid search](https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search#hybrid-search) on your Solr data, join Solr token search results with AlloyDB vector search results.
    
    
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

  * `WEIGHT`: contribution of this search entry to the overall Reciprocal Rank Fusion (RRF). For example, `0.5`.

  * `SOLR_FD_TABLE`: name of the foreign data table that represents your Solr table. For example, `my-fd-solr-table`.

  * `QUERY`: query to send to Solr. For example, `"solr_field_name:\"cloud databases\""` searches for the phrase "cloud databases" in the `solr_field_name` field.


**Note:** The `data_type` field in the search entry, as well as the `id_type`, `fusion_algorithm`, and `include_json_output` function parameters, are optional and use default values. For example, the fusion algorithm defaults to `RRF`.

## Troubleshooting

If you encounter authentication or connectivity issues when querying your Solr cluster, check the following common causes:

  * **HTTP 401 or 403 authentication errors:** Verify that your Solr secret in Secret Manager contains a base64-encoded string in the format `username:password` and that the service account used by AlloyDB has the `secretmanager.secretAccessor` permission.
  * **Connection timeouts:** Verify that outbound public IP connectivity is enabled on your primary AlloyDB instance and that your Solr firewall allows incoming connections on the specified port.



## Limitations

Before connecting AlloyDB to Solr, acknowledge the following limitations:

  * Solr integration is only available on PostgreSQL major version `17` and up.

  * AlloyDB reads, but doesn't write to, Solr data.

  * AlloyDB doesn't automatically index your database data into Solr. You are responsible for populating your Solr collections and maintaining consistency between the data in AlloyDB and the indexed data in Solr.

  * AlloyDB doesn't automatically synchronize schemas with Solr. If your Solr collection schema changes, you must manually update the schema of the corresponding PostgreSQL foreign table.

  * Unlike Elasticsearch, Solr doesn't have predefined JSON-typed fields. You must map the JSON-typed fields to `TEXT` or `jsonb`-formatted strings.

  * Solr requires a unique key in the sort expression for pagination to work correctly. By default, the `id` field is used. You can specify a custom field, or a comma-separated list of multiple fields along with their individual sort orders, for example, `myid0 ASC, myid1 DESC`, using the `unique_key_sort_suffix` option when you create the foreign table.




## What's next

  * Learn how to [Access OpenSearch data](https://docs.cloud.google.com/alloydb/docs/opensearch).
  * Learn how to [Access Elasticsearch data](https://docs.cloud.google.com/alloydb/docs/elastic-search).
  * Learn how to [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
