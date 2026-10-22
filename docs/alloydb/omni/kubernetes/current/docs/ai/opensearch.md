---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/opensearch/
title: Access OpenSearch data from AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:10:02.759352+00:00
---

# Access OpenSearch data from AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/opensearch/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)



Send feedback 

#  Access OpenSearch data from AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down




**Preview — OpenSearch FDW**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can access and search data stored in [OpenSearch](https://opensearch.org/) using the external search integration in AlloyDB Omni. This integration lets you perform federated search across existing OpenSearch indexes and your relational tables without copying or moving data.

**Note:** AlloyDB Omni using RPM and the AlloyDB Omni RPM orchestrator aren't supported.

## Before you begin

Before you begin, complete the following:

  * [Install AlloyDB Omni using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes). 
  * [Deploy and configure OpenSearch with an accessible public endpoint](https://docs.opensearch.org/latest/install-and-configure/index/). 
  * Enable the [security plugin](https://docs.opensearch.org/latest/security/configuration/disable-enable-security/) on your OpenSearch cluster and [create a read-only user](https://docs.opensearch.org/latest/security/access-control/users-roles/#defining-read-only-roles) in the internal users database. AlloyDB Omni uses these credentials to access your OpenSearch cluster. 



## Store OpenSearch credentials in Secret Manager

AlloyDB Omni stores and reads your OpenSearch credentials from Secret Manager. For Basic HTTP authentication, the value of the secret in Secret Manager must be a string formatted as `username:password`. For more information on how to use Secret Manager, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

Make sure that the service account that AlloyDB Omni uses has the `secretmanager.secretAccessor` permission to read the secret from Secret Manager. For more information, see [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

## Enable and configure the `external_search_fdw` extension

To start your integration with OpenSearch, configure access to your OpenSearch cluster through a foreign data server.

  1. Connect to your database and enable the extension:
         
         CREATE EXTENSION external_search_fdw;
         

  2. Create a foreign server:
         
         CREATE SERVER OPENSEARCH_SERVER_NAME
         FOREIGN DATA WRAPPER external_search_fdw
         OPTIONS (
           server 'OPENSEARCH_SERVER_HOST_PORT',
           search_provider 'opensearch',
           auth_mode 'secret_manager',
           auth_method 'AUTH_METHOD',
           secret_path 'SECRET_PATH'
         );
         

Replace the following variables:

     * `OPENSEARCH_SERVER_NAME`: name for your foreign data server. For example, `opensearch`.

     * `OPENSEARCH_SERVER_HOST_PORT`: public-facing URL for your OpenSearch cluster. For example, `https://search-my-domain.us-east-1.es.amazonaws.com:443`.

     * `AUTH_METHOD`: type of authentication to use. For example, `Basic`.

     * `SECRET_PATH`: Secret Manager path to your OpenSearch authentication credentials. For example, `projects/PROJECT_ID/secrets/opensearch-credentials/versions/1`.

  3. Define the user mapping for the OpenSearch server:
         
         CREATE USER MAPPING FOR CURRENT_USER
         SERVER OPENSEARCH_SERVER_NAME;
         

  4. Map the schema of your OpenSearch index to a PostgreSQL foreign table:
         
         CREATE FOREIGN TABLE OPENSEARCH_FD_TABLE(
             metadata external_search_fdw_schema.OpaqueMetadata,
             OPENSEARCH_FIELDS)
                SERVER OPENSEARCH_SERVER_NAME
                OPTIONS(
                     remote_table_name 'OPENSEARCH_INDEX_NAME'
                );
         

Replace the following variables:

     * `OPENSEARCH_FD_TABLE`: the name of the foreign data table that represents your OpenSearch table. For example, `my-fd-opensearch-table`.

     * `OPENSEARCH_FIELDS`: a comma-separated list where each entry follows the format `opensearch_field_name PG_DATA_TYPE`. For a list of supported OpenSearch data types and their corresponding PostgreSQL types, see [Supported data types](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/elastic-search#supported-data-types).

     * `OPENSEARCH_INDEX_NAME`: the name of your OpenSearch index. For example, `my-opensearch-index`.




## Query your OpenSearch data

AlloyDB Omni converts SQL queries to OpenSearch REST API queries.

### Standard SQL queries

You can use standard SQL with Lucene syntax for the search expression.
    
    
    SELECT id, body
    FROM OPENSEARCH_FD_TABLE
    WHERE FILTER
    ORDER BY metadata <@> 'QUERY';
    

Replace the following variables:

  * `OPENSEARCH_FD_TABLE`: name of the foreign data table that represents your OpenSearch table. For example, `my-fd-opensearch-table`.

  * `FILTER`: (Optional) filter to apply to your OpenSearch query. For example, `a = 10 AND b < 105`.

  * `QUERY`: query to send to OpenSearch. For example, `body:database`.




## Query DSL

For advanced use cases, use OpenSearch JSON-style Query Domain Specific Language (DSL).
    
    
    SELECT id, title
    FROM OPENSEARCH_FD_TABLE
    ORDER BY metadata <@> $${
      "query": {
        "bool": {
          "must": { "match": { "title": "opensearch" } },
          "filter": { "term": { "category": "software" } }
        }
      },
      "sort": [
        { "price": { "order": "desc" } }
      ]
    }$$
    LIMIT 1;
    

Replace `OPENSEARCH_FD_TABLE` with the name of the foreign data table that represents your OpenSearch table. For example, `my-fd-opensearch-table`.

**Note:** For Query DSL, you only need to propagate the `query`, `filter`, and `sort` expressions.

### Hybrid searches

To perform a [hybrid search](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/run-hybrid-vector-similarity-search#hybrid-search) on your OpenSearch data, join OpenSearch token search results with AlloyDB Omni vector search results.
    
    
    SELECT *
    FROM ai.hybrid_search(
      ARRAY[
        '{"limit": LIMIT,
          "weight": WEIGHT,
          "table_name": "OPENSEARCH_FD_TABLE",
          "key_column": "id",
          "query_text_input": "QUERY"}'::jsonb
      ])
    ORDER BY score DESC;
    

Replace the following variables:

  * `LIMIT`: number of results to return. For example, `10`.

  * `WEIGHT`: contribution of this search entry to the overall Reciprocal Rank Fusion (RRF). For example, `0.5`. If you don't provide weights, they are distributed evenly. For more information, see [Hybrid search function parameters](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/reference/hybrid-search-function-parameters).

  * `OPENSEARCH_FD_TABLE`: name of the foreign data table that represents your OpenSearch table. For example, `my-fd-opensearch-table`.

  * `QUERY`: query to send to OpenSearch. For example, `body:database`.


**Note:** The `data_type` field in the search entry, as well as the `id_type`, `fusion_algorithm`, and `include_json_output` function parameters, are optional and use default values. For example, the fusion algorithm defaults to `RRF`.

## Troubleshooting

If you encounter authentication or connectivity issues when querying your OpenSearch cluster, check the following:

  * **HTTP 401 or 403 authentication errors** : verify that your OpenSearch secret in Secret Manager contains a string formatted as `username:password` and that your service account has the `secretmanager.secretAccessor` permission.

  * **Connection timeouts** : verify network rules and firewall configuration between AlloyDB Omni and your OpenSearch endpoint.




## Limitations

  * **Read-only** : AlloyDB Omni reads, but doesn't write to, OpenSearch data.

  * **Data management** : AlloyDB Omni doesn't automatically index your database data into OpenSearch. You are responsible for populating your OpenSearch indexes and maintaining consistency between the data in AlloyDB Omni and the indexed data in OpenSearch.

  * **Schema management** : AlloyDB Omni doesn't automatically synchronize schemas with OpenSearch. If your OpenSearch index schema changes, manually update the schema of the corresponding PostgreSQL foreign table.

  * **Unsupported types** : specialized OpenSearch types, such as geospatial types, aren't supported.

  * **Authentication** : you must use Basic authentication (username and password) configured in your OpenSearch cluster.




## What's next

  * Learn how to [Access Elasticsearch data](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/elastic-search).

  * Learn how to [Access Solr data](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/solr-search).

  * Learn how to [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/run-hybrid-vector-similarity-search).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
