---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/elastic-search/
title: Access Elasticsearch data from AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:04:04.998986+00:00
---

# Access Elasticsearch data from AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/elastic-search/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)



Send feedback 

#  Access Elasticsearch data from AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/elastic-search)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/elastic-search)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/elastic-search)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/elastic-search)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/elastic-search)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/elastic-search)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/elastic-search)



**Preview — Elasticsearch FDW**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can access and search data stored in [Elasticsearch](https://www.elastic.co/elasticsearch) by creating a foreign data wrapper (FDW) and a foreign table in AlloyDB Omni.

**Note:** AlloyDB Omni using RPM and the AlloyDB Omni RPM orchestrator are not supported.

## Before you begin

Before you begin, complete the following:

  * [Install AlloyDB Omni using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes). 
  * [Deploy](https://www.elastic.co/docs/deploy-manage/deploy/deployment-comparison) and [run Elasticsearch in production](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments). 
  * Create a read-only [**Personal/User** API key](https://www.elastic.co/docs/deploy-manage/api-keys/elasticsearch-api-keys) that AlloyDB Omni can use to access your Elasticsearch cluster. 



## Create a service account

AlloyDB Omni requires a service account with Google Cloud to authenticate and use Secret Manager. AlloyDB Omni uses Secret Manager to store your Elasticsearch API key.

If you haven't already created a service account for AlloyDB Omni, create one following these steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with Google Cloud. You grant this service account permissions to access Secret Manager in Create a database cluster with AlloyDB AI. 

  2. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) and save it in JSON format to the `private-key.json` file, then download it.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  3. Store the key in a permanent location on your file system. It resides at this location for the lifetime of your AlloyDB Omni server.

Note its location on your file system; you need it for subsequent steps.

  4. [Create a Kubernetes secret using the service account key](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/install-with-alloydb-ai#create-key).




## Store Elasticsearch API key in Secret Manager

AlloyDB Omni stores and reads your Elasticsearch API key from Secret Manager. For more information on how to use Secret Manager, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

Make sure that you give your AlloyDB Omni service account permission to read the secret. For more information, see [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

## Create a database cluster with AlloyDB AI

To create a database cluster with AlloyDB AI, see [Install AlloyDB AI in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/install-with-alloydb-ai#enable-alloydb-ai). To access and query data with Elasticsearch, you don't need to specify the `vertexAI*` configurations.

## Enable and configure the external_search_fdw extension

To start your integration with Elasticsearch, complete the following instructions to enable and configure the [`external_search_fdw`](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/extensions#external_search_fdw) AlloyDB Omni extension:

  1. Enable the `external_search_fdw` extension.
         
         CREATE EXTENSION external_search_fdw;
         

  2. Configure access to your Elasticsearch cluster through a foreign data server.
         
         CREATE SERVER ELASTICSEARCH_SERVER_NAME
         FOREIGN DATA WRAPPER external_search_fdw
         OPTIONS (server 'ELASTICSEARCH_SERVER_HOST_PORT',
                  search_provider 'elastic',
                  auth_mode 'secret_manager',
                  auth_method 'AUTH_METHOD',
                  secret_path 'SECRET_PATH',
                  max_deadline_ms 'MAX_DEADLINE',
                  pagination_num_results 'PAGINATION_NUM_RESULTS',
                  pagination_context_timeout_ms 'PAGINATION_CONTEXT_TIMEOUT');
         

Replace the following variables:

     * `ELASTICSEARCH_SERVER_NAME`: name for your foreign data server. For example, `my-elasticsearch-server`.

     * `ELASTICSEARCH_SERVER_HOST_PORT`: Public-facing URL for your Elasticsearch cluster. For example, `https://node1.elastic.test.com:9200`.

     * `AUTH_METHOD`: type of authentication to use. You can choose between the following options:

       * `ApiKey`: Elasticsearch [**Personal/User** API key](https://www.elastic.co/docs/deploy-manage/api-keys/elasticsearch-api-keys).

       * `Basic`: Elasticsearch username and password.

     * `SECRET_PATH`: Secret Manager path to your Elasticsearch authentication credentials. For example, `projects/123456789012/secrets/apikey/versions/1`. `123456789012` represents your Google Cloud project ID.

     * (Optional) `MAX_DEADLINE`: maximum amount of time, in milliseconds, that AlloyDB Omni waits for a response from Elasticsearch. Set this value based on the locations of your AlloyDB Omni and Elasticsearch instances. The default value is `10000`.

     * (Optional) `PAGINATION_NUM_RESULTS`: max number of results fetched per batch from Elasticsearch. If more results are requested, AlloyDB Omni retrieves the results in multiple batches of this size. The default value is `32`.

     * (Optional) `PAGINATION_CONTEXT_TIMEOUT`: amount of time, in milliseconds, that Elasticsearch keeps the pagination request context active. The default value is `30000`.

  3. Define the PostgreSQL user mapping for the Elasticsearch server. Note that PostgreSQL FDWs require this user mapping to function. AlloyDB Omni authenticates using the REST authorization header.
         
         CREATE USER MAPPING FOR CURRENT_USER
                SERVER ELASTICSEARCH_SERVER_NAME;
         

  4. Configure the schema for your Elasticsearch data through a foreign data table.
         
         CREATE FOREIGN TABLE ELASTICSEARCH_FD_TABLE(
             metadata external_search_fdw_schema.OpaqueMetadata,
             ELASTICSEARCH_FIELDS)
                SERVER ELASTICSEARCH_SERVER_NAME
                OPTIONS(remote_table_name 'ELASTICSEARCH_INDEX_NAME');
         

Replace the following new variables:

     * `ELASTICSEARCH_FD_TABLE`: name of the foreign data table that represents your Elasticsearch table. For example, `my-fd-elasticsearch-table`.

     * `ELASTICSEARCH_FIELDS`: comma-separated list of Elasticsearch field schema definitions in the following format: `elasticsearch_field_name PG_DATA_TYPE`. For example, `elasticsearch_boolean_field_name BOOLEAN, elasticsearch_double_field_name DOUBLE PRECISION`. These fields must match the field names in Elasticsearch unless the `remote_field_name` option is appended. For example, `elasticsearch_foo OPTIONS (remote_field_name 'elasticsearch_FOO')`.

For the list of Elasticsearch data types that can be defined for AlloyDB Omni, see Supported data types.

     * `ELASTICSEARCH_INDEX_NAME`: name of your Elasticsearch index. For example, `my-elasticsearch-index`.




### Supported data types

AlloyDB Omni supports the following Elasticsearch data types:

Data type(s) | PostgreSQL type  
---|---  
[`alias`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/field-alias) |  PostgreSQL type for the field that `alias` is referencing   
[`binary`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/binary) |  [`bytea`](https://www.postgresql.org/docs/18/datatype-binary.html)  
[`boolean`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/boolean) |  [`BOOLEAN`](https://www.postgresql.org/docs/18/datatype-boolean.html)  
[`byte`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number),  [`short`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number) |  [`SMALLINT`](https://www.postgresql.org/docs/18/datatype-numeric.html#DATATYPE-INT)  
[`date`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/date) |  [`TIMESTAMPTZ`](https://www.postgresql.org/docs/18/datatype-datetime.html)  
[`double`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number),  [`scaled_float`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number) |  [`DOUBLE PRECISION`](https://www.postgresql.org/docs/18/datatype-numeric.html#DATATYPE-FLOAT)  
[`float`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number),  [`half_float`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number) |  [`REAL`](https://www.postgresql.org/docs/18/datatype-numeric.html#DATATYPE-FLOAT)  
[`integer`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number) |  [`INTEGER`](https://www.postgresql.org/docs/18/datatype-numeric.html#DATATYPE-INT)  
[`long`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number) |  [`BIGINT`](https://www.postgresql.org/docs/18/datatype-numeric.html#DATATYPE-INT)  
[`object`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/object),  [`flattened`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/flattened) |  [`jsonb`](https://www.postgresql.org/docs/18/datatype-json.html)  
[`text`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/text),  [`annotated_text`](https://www.elastic.co/docs/reference/elasticsearch/plugins/mapper-annotated-text-usage),  [`keyword`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/keyword#keyword-field-type),  [`constant_keyword`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/keyword#constant-keyword-field-type),  [`wildcard`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/keyword#wildcard-field-type) |  [`TEXT`](https://www.postgresql.org/docs/18/datatype-character.html)  
[`unsigned_long`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number) |  [`NUMERIC`](https://www.postgresql.org/docs/18/datatype-numeric.html#DATATYPE-NUMERIC-DECIMAL)  
  
## Query your Elasticsearch data

AlloyDB Omni takes SQL queries and converts them to Elasticsearch REST API queries. During this conversion, AlloyDB Omni attempts to push down as much query logic as possible without changing the query's identity, including the SQL query's `LIMIT`. However, there are cases where you might specify not to push down certain Elasticsearch fields or where query logic cannot be pushed down. For example, [`LIKE`](https://www.postgresql.org/docs/18/functions-matching.html#FUNCTIONS-LIKE) and other text-matching operators cannot be pushed down. For more examples of what can and can't be pushed down, see Pushdown examples.

In scenarios where the `LIMIT` is set higher than `pagination_num_results` or where `LIMIT` is not specified or cannot be pushed down, AlloyDB Omni uses the [Scroll API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-scroll), which can be resource-intensive.

Because the Scroll API can be resource-intensive, we recommend examining your queries using `EXPLAIN VERBOSE` to see which APIs are used. Limiting the use of the Scroll API and using `LIMIT` improves performance.

To query your Elasticsearch data, you have the following options:

  * Standard SQL queries
  * Query DSL
  * Hybrid searches



### Standard SQL queries

Standard SQL queries can be written using Elasticsearch's [Lucene](https://www.elastic.co/docs/explore-analyze/query-filter/languages/lucene-query-syntax) syntax.

To perform a standard SQL query, see the following example query:
    
    
    SELECT id, body
    FROM ELASTICSEARCH_FD_TABLE
    WHERE FILTER
    ORDER BY metadata <@> 'QUERY';
    

Replace the following variables:

  * `ELASTICSEARCH_FD_TABLE`: name of the foreign data table that represents your Elasticsearch table. For example, `my-fd-elasticsearch-table`.

  * (Optional) `FILTER`: filter to apply to your Elasticsearch query. For example, `AND qubits < 105`.

  * `QUERY`: query to send to Elasticsearch. For a few example queries, see the following list:

    * `body:quantum body:computing`
    * `body:(quantum computing)`
    * `body:(quantum AND computing)`
    * `body:"quantum computing"`
    * `body:"quantum computing" AND qubits:[* TO 105}`



### Query DSL

[Query DSL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl) is Elasticsearch's full-featured, JSON-style query language recommended for advanced use cases. Query DSL lets you perform complex searches, filtering, and aggregations that can't be expressed in SQL query syntax.

To perform queries using [Query DSL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl), see the following example query:
    
    
    SELECT id, body
    FROM ELASTICSEARCH_FD_TABLE
    ORDER BY
      metadata <@> $${
        "query": {
          "bool": {
            "must": [
              {
                "query_string": {
                  "query" : "QUERY"
                }
              }
            ],
            "filter": [
              {
                "range": { 
                  "id": { 
                    "lt": "10"
                  }
                }
              }
            ]
          }
        },
        "sort": [
          {
            "id": {
              "order": "desc"
            }
          }
        ]
      }$$
    LIMIT 1;
    

Replace the following variables:

  * `ELASTICSEARCH_FD_TABLE`: name of the foreign data table that represents your Elasticsearch table. For example, `my-fd-elasticsearch-table`.

  * `QUERY`: query to send to Elasticsearch. For example, `"elasticsearch_field_name:\"quantum computing\" OR int_field:[* TO 3]"`.




Note that for Query DSL, you're only expected to propagate the `query`, `filter`, and `sort` expressions.

### Hybrid searches

To perform a [hybrid search](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/run-hybrid-vector-similarity-search#hybrid-search) on your Elasticsearch data, see the following example search:
    
    
    SELECT *
    FROM
      ai.hybrid_search(
        ARRAY[
          '{"limit": LIMIT,
            "data_type": "external_search_fdw",
            "weight": WEIGHT,
            "table_name": "ELASTICSEARCH_FD_TABLE",
            "key_column": "DOCUMENT_ID_COLUMN_NAME",
            "query_text_input": QUERY}'::jsonb],
        NULL::TEXT,
        'RRF',
        FALSE)
    ORDER BY score DESC;
    

Replace the following variables:

  * `LIMIT`: number of results to return. For example, `3`.

  * `WEIGHT`: contribution of this search entry to the overall Reciprocal Rank Fusion (RRF). For example, `0.5`. If you don't provide weights, they are distributed evenly. For more information, see [Hybrid search function parameters](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/ai/hybrid-search-function-parameters).

  * `ELASTICSEARCH_FD_TABLE`: name of the foreign data table that represents your Elasticsearch table. For example, `my-fd-elasticsearch-table`.

  * `DOCUMENT_ID_COLUMN_NAME`: name of the document ID column.

  * `QUERY`: query to send to Elasticsearch. For example, `"elasticsearch_field_name:\"quantum computing\""` searches for the phrase "quantum computing" in the `elasticsearch_field_name` field. All query types mentioned in Supported data types can be used in your query.




For more information on the parameters available for hybrid searches, see [Hybrid search function parameters](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/hybrid-search-function-parameters).

### Pushdown examples

To make queries more efficient, AlloyDB Omni attempts to push down the following aspects of the query directly into the API call made to Elasticsearch:

  * `SELECT` fields
  * `WHERE` filters
  * `ORDER BY` sorts
  * `LIMIT`



For example queries that show which aspects AlloyDB Omni is and isn't able to push down, see the following table.

Query type | Query example | Query elements pushed down  
---|---|---  
Unfiltered queries | 
    
    
    SELECT id, body
    FROM elasticsearch_table
    ORDER BY metadata <@> 'body:foo' DESC
    LIMIT 10;

| 

  * `SELECT` fields
  * `ORDER BY ... DESC` sort
  * `LIMIT`

  
Exact text match | 
    
    
    SELECT id, body
    FROM elasticsearch_table
    WHERE body = 'foo'
    LIMIT 10;

| 

  * `SELECT` fields
  * `WHERE` filter
  * `LIMIT`

  
Single-field expressions | 
    
    
    SELECT id, body
    FROM elasticsearch_table
    WHERE id > 10
    ORDER BY metadata <@> 'body:foo'
    LIMIT 10;

| 

  * `SELECT` fields
  * `WHERE` filter

  
Constant expressions | 
    
    
    SELECT id, body
    FROM elasticsearch_table
    WHERE id > (1+1)
    LIMIT 10;

| 

  * `SELECT` fields
  * `WHERE` filter
  * `LIMIT`

  
Expressions with functions | 
    
    
    SELECT id, body
    FROM elasticsearch_table
    WHERE id > CEIL(3.14)
    LIMIT 10;

| 

  * `SELECT` fields

  
Multi-field expressions | 
    
    
    SELECT id, body
    FROM elasticsearch_table
    WHERE dbl_field < flt_field
    LIMIT 10;

| 

  * `SELECT` fields

  
Score filtering | 
    
    
    SELECT id, body, (metadata <@> 'body:bar') AS score
    FROM elasticsearch_table
    WHERE score > 0.5
    ORDER by score desc
    LIMIT 10;

| 

  * `SELECT` fields
  * `ORDER BY ... DESC` sort

  
`LIKE` and similar operators | 
    
    
    SELECT id, body
    FROM elasticsearch_table
    WHERE id > 10 AND body LIKE '%foo%'
    LIMIT 10;

| 

  * `SELECT` fields
  * `WHERE id > 10` filter

  
Raw queries | 
    
    
    SELECT id, body
    FROM elasticsearch_table
    WHERE id < 10
    ORDER BY metadata <@> $${"query": { "match_all": {}}}$$ DESC
    LIMIT 10;

| 

  * `SELECT` fields
  * `ORDER BY ... DESC` sort

  
  
## Troubleshooting

If you encounter authentication or connectivity issues when querying your Elasticsearch cluster, check the following:

  * HTTP 401 or 403 authentication errors: verify that your Elasticsearch secret in Secret Manager contains valid authentication credentials for your `auth_method` (`ApiKey` or `Basic`), and verify that your service account has the `secretmanager.secretAccessor` permission.
  * Connection timeouts: verify network rules and firewall configuration between AlloyDB Omni and your Elasticsearch endpoint.

**Note:** Elasticsearch is a trademark of Elastic NV and is not affiliated with Google LLC.

## Limitations

  * AlloyDB Omni reads, but doesn't write to, Elasticsearch data.

  * You are responsible for synchronizing data between AlloyDB Omni and Elasticsearch.

  * Specialized Elasticsearch types, such as [`geo_point`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape) aren't supported. For more information, see Supported data types.




## What's next

  * Learn how to [Access OpenSearch data](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/opensearch).
  * Learn how to [Access Solr data](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/solr-search).
  * Learn how to [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/run-hybrid-vector-similarity-search).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
