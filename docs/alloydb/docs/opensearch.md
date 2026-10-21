---
url: https://docs.cloud.google.com/alloydb/docs/opensearch/
title: Access OpenSearch data from AlloyDB \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:41.401816+00:00
---

# Access OpenSearch data from AlloyDB  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/opensearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Access OpenSearch data from AlloyDB Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — OpenSearch FDW**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can access and search data stored in OpenSearch using the external search integration in AlloyDB. This integration lets you join OpenSearch indexes with relational tables in AlloyDB without moving or copying data.

## Before you begin

Before you begin, make sure that you've completed the following:

  * [Create a cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create).

  * [Enable outbound connectivity](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#add-outbound-connectivity) on your primary AlloyDB instance.

  * [Create and configure OpenSearch](https://docs.opensearch.org/latest/install-and-configure/index/) with an accessible public endpoint.

  * Enable the [security plugin](https://docs.opensearch.org/latest/security/configuration/disable-enable-security/) on your OpenSearch cluster and [create a read-only user](https://docs.opensearch.org/latest/security/access-control/users-roles/#defining-read-only-roles) in the internal users database. AlloyDB uses these credentials to access your OpenSearch cluster.




## Store OpenSearch credentials in Secret Manager

AlloyDB stores and reads your OpenSearch credentials from Secret Manager. For more information on how to use Secret Manager, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

Ensure that your AlloyDB service account has the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role to read the secret from Secret Manager. For more information, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

## Enable and configure the `external_search_fdw` extension

To start your integration with OpenSearch, configure access to your OpenSearch cluster through a foreign data server.

  1. Enable the `external_search_fdw` extension.
         
         CREATE EXTENSION external_search_fdw;
         

  2. Create a server for your OpenSearch cluster.
         
         CREATE SERVER OPENSEARCH_SERVER_NAME
         FOREIGN DATA WRAPPER external_search_fdw
         OPTIONS (
           server 'OPENSEARCH_SERVER_HOST_PORT',
           search_provider 'opensearch',
           auth_mode 'secret_manager',
           auth_method 'Basic',
           secret_path 'SECRET_PATH'
         );
         

Replace the following variables:

     * `OPENSEARCH_SERVER_NAME`: name for your foreign data server. For example, `opensearch`.

     * `OPENSEARCH_SERVER_HOST_PORT`: public-facing URL (endpoint) for your OpenSearch cluster.

     * `SECRET_PATH`: Secret Manager path to your OpenSearch authentication credentials. For example, `projects/123456789012/secrets/opensearch-credentials/versions/1`. `123456789012` represents your Google Cloud project ID.

  3. Define the PostgreSQL user mapping for the OpenSearch server. Note that PostgreSQL FDWs require this user mapping to function. AlloyDB authenticates using the REST authorization header.
         
         CREATE USER MAPPING FOR CURRENT_USER
         SERVER OPENSEARCH_SERVER_NAME;
         

  4. Map the schema of your OpenSearch index to a PostgreSQL foreign table.
         
         CREATE FOREIGN TABLE OPENSEARCH_FD_TABLE(
             metadata external_search_fdw_schema.OpaqueMetadata,
             OPENSEARCH_FIELDS)
                SERVER OPENSEARCH_SERVER_NAME
                OPTIONS(
                     remote_table_name 'OPENSEARCH_INDEX_NAME'
                );
         

Replace the following new variables:

     * `OPENSEARCH_FD_TABLE`: the name of the foreign data table that represents your OpenSearch table. For example, `my-fd-opensearch-table`.

     * `OPENSEARCH_FIELDS`: a comma-separated list where each entry uses the format `opensearch_field_name PG_DATA_TYPE`. For a list of supported OpenSearch data types and their corresponding PostgreSQL types, see Supported data types.

     * `OPENSEARCH_INDEX_NAME`: the name of your OpenSearch index. For example, `my-opensearch-index`.




### Supported data types

AlloyDB supports the following OpenSearch data types:

Data type(s) | AlloyDB type  
---|---  
[`alias`](https://opensearch.org/docs/latest/field-types/supported-field-types/alias/) |  PostgreSQL type for the field that `alias` is referencing   
[`binary`](https://opensearch.org/docs/latest/field-types/supported-field-types/binary/) |  [`bytea`](https://www.postgresql.org/docs/17/datatype-binary.html)  
[`boolean`](https://opensearch.org/docs/latest/field-types/supported-field-types/boolean/) |  [`BOOLEAN`](https://www.postgresql.org/docs/17/datatype-boolean.html)  
[`byte`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/),  [`short`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/) |  [`SMALLINT`](https://www.postgresql.org/docs/17/datatype-numeric.html#DATATYPE-INT)  
[`date`](https://opensearch.org/docs/latest/field-types/supported-field-types/date/) |  [`TIMESTAMPTZ`](https://www.postgresql.org/docs/17/datatype-datetime.html)  
[`double`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/),  [`scaled_float`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/) |  [`DOUBLE PRECISION`](https://www.postgresql.org/docs/17/datatype-numeric.html#DATATYPE-FLOAT)  
[`float`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/),  [`half_float`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/) |  [`REAL`](https://www.postgresql.org/docs/17/datatype-numeric.html#DATATYPE-FLOAT)  
[`integer`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/) |  [`INTEGER`](https://www.postgresql.org/docs/17/datatype-numeric.html#DATATYPE-INT)  
[`long`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/) |  [`BIGINT`](https://www.postgresql.org/docs/17/datatype-numeric.html#DATATYPE-INT)  
[`object`](https://opensearch.org/docs/latest/field-types/supported-field-types/object/),  [`flattened`](https://opensearch.org/docs/latest/field-types/supported-field-types/flattened/) |  [`jsonb`](https://www.postgresql.org/docs/17/datatype-json.html)  
[`text`](https://opensearch.org/docs/latest/field-types/supported-field-types/text/),  [`keyword`](https://opensearch.org/docs/latest/field-types/supported-field-types/keyword/),  `constant_keyword`,  `wildcard` |  [`TEXT`](https://www.postgresql.org/docs/17/datatype-character.html)  
[`unsigned_long`](https://opensearch.org/docs/latest/field-types/supported-field-types/numeric/) |  [`NUMERIC`](https://www.postgresql.org/docs/17/datatype-numeric.html#DATATYPE-NUMERIC-DECIMAL)  
  
## Query your OpenSearch data

AlloyDB takes SQL queries and converts them to OpenSearch REST API queries.

To query your OpenSearch data, you have the following options:

  * Standard SQL queries
  * Query DSL
  * Hybrid searches



### Standard SQL queries

You can use standard SQL with Lucene syntax for the search expression.
    
    
    SELECT id, body
    FROM OPENSEARCH_FD_TABLE
    WHERE FILTER
    ORDER BY metadata <@> 'QUERY';
    

Replace the following variables:

  * `OPENSEARCH_FD_TABLE`: The name of the foreign data table that represents your OpenSearch table. For example, `my-fd-opensearch-table`.

  * (Optional) `FILTER`: The filter to apply to your OpenSearch query. For example, `a = 10 AND b < 105`.

  * `QUERY`: The query to send to OpenSearch. For example, `body:database`.




### Query DSL

For advanced use cases, use OpenSearch JSON-style Query DSL.
    
    
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

**Note:** For Query DSL, you're only expected to propagate the query, filter, and sort expressions.

### Hybrid searches

To perform a hybrid search on your OpenSearch data, join OpenSearch token search results with AlloyDB vector search results.
    
    
    SELECT *
    FROM ai.hybrid_search(
      ARRAY[
        '{"limit": LIMIT,
          "weight": WEIGHT,
          "table_name": OPENSEARCH_FD_TABLE,
          "key_column": "id",
          "query_text_input": "QUERY"}'::jsonb
      ])
    ORDER BY score DESC;
    

Replace the following variables:

  * `LIMIT`: number of results to return. For example, `10`.

  * `WEIGHT`: contribution of this search entry to the overall Reciprocal Rank Fusion (RRF). For example, `0.5`.

  * `OPENSEARCH_FD_TABLE`: name of the foreign data table that represents your OpenSearch table. For example, `my-fd-opensearch-table`.

  * `QUERY`: query to send to OpenSearch. For example, `"opensearch_field_name:\"cloud databases\""` searches for the phrase "cloud databases" in the `opensearch_field_name` field.


**Note:** The data_type field in the search entry, as well as the id_type, fusion_algorithm, and include_json_output function parameters, are optional and use default values. For example, the fusion algorithm defaults to RRF.

### Pushdown examples

To make queries more efficient, AlloyDB attempts to push down the following aspects of the query directly into the API call made to OpenSearch:

  * `SELECT` fields
  * `WHERE` filters
  * `ORDER BY` sorts
  * `LIMIT`



For example queries that illustrate which aspects AlloyDB is and isn't able to push down, see the following table.

Query type | Query example | Query elements pushed down  
---|---|---  
Unfiltered queries | 
    
    
    SELECT id, body
    FROM opensearch_table
    ORDER BY metadata <@> 'body:foo' DESC
    LIMIT 10;

| 

  * `SELECT` fields
  * `ORDER BY ... DESC` sort
  * `LIMIT`

  
Exact text match | 
    
    
    SELECT id, body
    FROM opensearch_table
    WHERE body = 'foo'
    LIMIT 10;

| 

  * `SELECT` fields
  * `WHERE` filter
  * `LIMIT`

  
Single-field expressions | 
    
    
    SELECT id, body
    FROM opensearch_table
    WHERE id > 10
    ORDER BY metadata <@> 'body:foo'
    LIMIT 10;

| 

  * `SELECT` fields
  * `WHERE` filter

  
Constant expressions | 
    
    
    SELECT id, body
    FROM opensearch_table
    WHERE id > (1+1)
    LIMIT 10;

| 

  * `SELECT` fields
  * `WHERE` filter
  * `LIMIT`

  
Expressions with functions | 
    
    
    SELECT id, body
    FROM opensearch_table
    WHERE id > CEIL(3.14)
    LIMIT 10;

| 

  * `SELECT` fields

  
Multi-field expressions | 
    
    
    SELECT id, body
    FROM opensearch_table
    WHERE dbl_field < flt_field
    LIMIT 10;

| 

  * `SELECT` fields

  
Score filtering | 
    
    
    SELECT id, body, (metadata <@> 'body:bar') AS score
    FROM opensearch_table
    WHERE score > 0.5
    ORDER by score desc
    LIMIT 10;

| 

  * `SELECT` fields
  * `ORDER BY ... DESC` sort

  
`LIKE` and similar operators | 
    
    
    SELECT id, body
    FROM opensearch_table
    WHERE id > 10 AND body LIKE '%foo%'
    LIMIT 10;

| 

  * `SELECT` fields
  * `WHERE id > 10` filter

  
Raw queries | 
    
    
    SELECT id, body
    FROM opensearch_table
    WHERE id < 10
    ORDER BY metadata <@> $${"query": { "match_all": {}}}$$ DESC
    LIMIT 10;

| 

  * `SELECT` fields
  * `ORDER BY ... DESC` sort

  
  
## Troubleshooting

If you encounter authentication or connectivity issues when querying your OpenSearch cluster, check the following common causes:

  * **HTTP 401 or 403 authentication errors:** Verify that your OpenSearch secret in Secret Manager contains a string formatted as `username:password` and that your AlloyDB service account has the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role.
  * **Connection timeouts:** Verify that outbound public IP connectivity is enabled on your primary AlloyDB instance and that your OpenSearch firewall allows incoming connections on the specified port.



## Limitations

Before connecting AlloyDB to OpenSearch, understand the following limitations:

  * OpenSearch integration is only available on PostgreSQL major version `17` and higher.

  * AlloyDB reads, but doesn't write to, OpenSearch data.

  * AlloyDB doesn't automatically index your database data into OpenSearch. You are responsible for populating your OpenSearch indexes and maintaining consistency between the data in AlloyDB and the indexed data in OpenSearch.

  * AlloyDB doesn't automatically synchronize schemas with OpenSearch. If your OpenSearch index schema changes, you must manually update the schema of the corresponding PostgreSQL foreign table.

  * Specialized OpenSearch types, such as [`geo_point`](https://opensearch.org/docs/latest/field-types/supported-field-types/geo-point/) are not supported. For the full list of supported data types, see Supported data types.

  * You must use Basic authentication (username and password) configured in your OpenSearch cluster.




## What's next

  * Learn how to [Access Elasticsearch data](https://docs.cloud.google.com/alloydb/docs/elastic-search).
  * Learn how to [Access Solr data](https://docs.cloud.google.com/alloydb/docs/solr-search).
  * Learn how to [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
