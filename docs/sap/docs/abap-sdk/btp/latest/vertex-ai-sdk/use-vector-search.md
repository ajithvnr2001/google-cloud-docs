---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-vector-search/
title: Use Agent Platform Vector Search \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:37.238563+00:00
---

# Use Agent Platform Vector Search  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-vector-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Use Agent Platform Vector Search Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-vector-search)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/use-vector-search)



This document describes how to use [Agent Platform Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) to perform vector similarity searches by using the Agent Platform SDK for ABAP. With Vector Search, you can find semantically similar data points within large datasets by using high-dimensional vectors. You can use Vector Search for tasks such as image and text retrieval to match items based on semantic meaning rather than exact keywords.

Using Vector Search with your SAP enterprise data provides the following benefits:

  * **Improve search relevance** : Retrieve relevant search results across structured and unstructured SAP data stored in different systems.

  * **Search unstructured data** : Use Vector Search to extract information from unstructured data within SAP systems, such as product data, customer data, customer reviews, support tickets, or internal documents.

  * **Build recommendation and conversational tools** : Provide personalized and context-aware interactions by using Vector Search for product recommendations, chatbots, and other customer-facing applications.

  * **Identify data patterns** : Detect relationships and patterns across SAP datasets to support operational decision-making.

  * **Integrate with generative AI** : Combine Vector Search with generative AI models to build retrieval-augmented generation (RAG) applications in SAP.




## How to use Vector Search

The Agent Platform SDK for ABAP provides classes and methods to build and query Vector Search applications in your ABAP environment. To use Vector Search in your SAP applications, complete the following steps:

  1. Generate embeddings for your enterprise data.
  2. Upload the embeddings to a Cloud Storage bucket.
  3. Create a vector index and associate the vector index with the Cloud Storage bucket that contains the embeddings. You can create two types of indexes, depending on how frequently you update your data:

     * Batch index: Updated in batches at scheduled intervals, for example, weekly or monthly.
     * Stream index: Updated in real time as new data is added to your datastore.
  4. Create an index endpoint and deploy the vector index to the endpoint to run queries. An index endpoint works as a server instance that accepts query requests for your index.

  5. Query the index endpoint by using an entity ID, a search string, or an embedding.




## Create and manage a vector index

To prepare your enterprise data for semantic search, create a vector index, deploy this index to an endpoint, and maintain it with batch or stream updates by using the `/GOOG/CL_VECTOR_INDEX` class.

### Before you begin

Make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.



#### Generate embeddings

Vector Search requires vector embeddings of your enterprise data to build and structure the search index. For information about how to generate embeddings for your enterprise data by using the Agent Platform SDK for ABAP, see [Generate embeddings](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/generate-embeddings).

#### Upload embeddings to Cloud Storage

Upload your embeddings to a Cloud Storage bucket so that you can associate the embeddings with a vector index. Even if you have generated your embedding files outside Google Cloud, you can upload those embedding files to a Cloud Storage bucket.

For information about how to send the embeddings that are generated by using the Agent Platform SDK for ABAP to a Cloud Storage bucket, see [Store embeddings in Cloud Storage](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/generate-embeddings#store-embeddings-gcs).

### Instantiate the vector index class

To create and manage your vector index, instantiate the `/GOOG/CL_VECTOR_INDEX` class by passing the client key configured for authentication:
    
    
    DATA(lo_vector_index) = NEW /goog/cl_vector_index( iv_key_name = 'CLIENT_KEY' ).
    

Replace `CLIENT_KEY` with the client key configured for authentication.

### Create a vector index

To create a vector index, use the `CREATE_TREE_AH_INDEX` method of the `/GOOG/CL_VECTOR_INDEX` class. This method creates an index based on the Tree-AH (Tree-Asymmetric Hashing) algorithm.
    
    
    lo_vector_index->create_tree_ah_index( iv_display_name               = 'INDEX_NAME'
                                          iv_description                 = 'INDEX_DESCRIPTION'
                                          iv_location_id                 = 'LOCATION_ID'
                                          iv_gcs_content_uri             = 'CONTENT_URI'
                                          iv_dimensions                  = 'DIMENSIONS'
                                          iv_approximate_neighbors_count = 'NEIGHBORS_COUNT'
                                          iv_index_update_method         = 'INDEX_UPDATE_METHOD'
                                          iv_distance_measure_type       = 'DISTANCE_MEASURE_TYPE'
                                          iv_shard_size                  = 'SHARD_SIZE'
                                          iv_leaf_node_embedding_count   = 'LEAF_NODE_EMBEDDING_COUNT'
                                          iv_leaf_nodes_to_search        = 'LEAF_NODE_TO_SEARCH'
                                          iv_etag                        = 'ETAG'
                                          iv_cloud_kms_encryption_key    = 'KEY_FOR_ENCRYPTION' ).
    

Replace the following:

  * `INDEX_NAME`: Display name of the index.
  * `INDEX_DESCRIPTION`: Description of the index.
  * `LOCATION_ID`: Google Cloud region where the index is stored. For information about the available locations, see [Agent Platform locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations).
  * `CONTENT_URI`: URI of the Cloud Storage bucket containing the embeddings, which is used to build the index.
  * `DIMENSIONS`: Number of dimensions of the input vectors.
  * `NEIGHBORS_COUNT`: Number of neighbors to find through approximate search before reordering is performed.
  * `INDEX_UPDATE_METHOD`: Update mode of the index: `BATCH_UPDATE` or `STREAM_UPDATE`.
  * `DISTANCE_MEASURE_TYPE`: The algorithm used to calculate the distance between data points and the query vector. For more information, see [Distance measure type](https://docs.cloud.google.com/vertex-ai/docs/vector-search/configuring-indexes#distance-measure-type).
  * `SHARD_SIZE`: Size of each [shard](https://docs.cloud.google.com/vertex-ai/docs/vector-search/configuring-indexes#shard-size). When an index is large, it is sharded based on the specified shard size. During serving, each shard is served on a separate node and scales independently.
  * `LEAF_NODE_EMBEDDING_COUNT`: Number of embeddings on each leaf node. The default value is `1000`.
  * `LEAF_NODE_TO_SEARCH`: The percentage of leaf nodes that a query searches. This value must be from 1 to 100, inclusive. The default value is `10` (`10%`).
  * `ETAG`: An ETag value to perform consistent read-modify-write updates.
  * `KEY_FOR_ENCRYPTION`: [Cloud KMS](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/cmek) resource identifier of the customer-managed encryption key (CMEK).



### Create a vector index endpoint

To create a vector index endpoint, use the `CREATE_INDEX_ENDPOINT` method of the `/GOOG/CL_VECTOR_INDEX` class.
    
    
    lo_vector_index->create_index_endpoint( iv_display_name             = 'INDEX_ENDPOINT_NAME'
                                            iv_description              = 'INDEX_ENDPOINT_DESCRIPTION'
                                            iv_location_id              = 'LOCATION_ID'
                                            iv_public_endpoint_enabled  = 'ENABLE_PUBLIC_ENDPOINT'
                                            iv_etag                     = 'ETAG'
                                            iv_cloud_kms_encryption_key = 'KEY_FOR_ENCRYPTION' ).
    

Replace the following:

  * `INDEX_ENDPOINT_NAME`: Display name of the index endpoint.
  * `INDEX_ENDPOINT_DESCRIPTION`: Description of the index endpoint.
  * `LOCATION_ID`: Google Cloud region where you want to create the index endpoint. For information about the available locations, see [Agent Platform locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations).
  * `ENABLE_PUBLIC_ENDPOINT`: If the deployed index is accessible through a public endpoint, then set this parameter to `ABAP_TRUE`.
  * `ETAG`: An ETag value to perform consistent read-modify-write updates.
  * `KEY_FOR_ENCRYPTION`: [Cloud KMS](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/cmek) resource identifier of the customer-managed encryption key (CMEK).



### Deploy a vector index to an index endpoint

To deploy a vector index to an index endpoint, use the `DEPLOY_INDEX` method of the `/GOOG/CL_VECTOR_INDEX` class.
    
    
    lo_vector_index->deploy_index( iv_deployed_index_id    = 'DEPLOYMENT_ID'
                                  iv_location_id           = 'LOCATION_ID'
                                  iv_index_id              = 'INDEX_ID'
                                  iv_index_endpoint_id     = 'INDEX_ENDPOINT_ID'
                                  iv_min_replica_count     = 'MIN_REPLICA_COUNT'
                                  iv_max_replica_count     = 'MAX_REPLICA_COUNT'
                                  iv_enable_access_logging = 'ENABLE_ACCESS_LOGGING'
                                  iv_deployment_group      = 'DEPLOYMENT_GROUP' ).
    

Replace the following:

  * `DEPLOYMENT_ID`: ID of the index deployment.
  * `LOCATION_ID`: Google Cloud region where you want to deploy the index. For information about the available locations, see [Agent Platform locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations).
  * `INDEX_ID`: Resource name of the index.
  * `INDEX_ENDPOINT_ID`: Resource name of the index endpoint to deploy to.
  * `MIN_REPLICA_COUNT`: Minimum number of machine replicas for the deployed model.
  * `MAX_REPLICA_COUNT`: Maximum number of machine replicas for the deployed model.
  * `ENABLE_ACCESS_LOGGING`: To send access logs for a private endpoint to Cloud Logging, set this parameter to `ABAP_TRUE`.
  * `DEPLOYMENT_GROUP`: Name of the deployment group, for example, `test`, `prod`.



### Update and rebuild a vector index

To return relevant Vector Search results for an enterprise AI solution, you also need to keep the index updated with the latest enterprise data.

#### Update a batch index

To update a batch index with new data in a Cloud Storage bucket, use the `PATCH_TREE_AH_INDEX` method of the `/GOOG/CL_VECTOR_INDEX` class.
    
    
    lo_vector_index->patch_tree_ah_index( iv_index_id              = 'INDEX_ID'
                                          iv_gcs_content_uri       = 'CONTENT_URI'
                                          iv_location_id           = 'LOCATION_ID'
                                          iv_is_complete_overwrite = 'IS_COMPLETE_OVERWRITE' ).
    

Replace the following:

  * `INDEX_ID`: Resource name of the index.
  * `CONTENT_URI`: URI of the Cloud Storage bucket that contains the embeddings for the latest enterprise data.
  * `LOCATION_ID`: Google Cloud region of the index.
  * `IS_COMPLETE_OVERWRITE`: To completely overwrite the index with data in the given Cloud Storage bucket, set this parameter to `ABAP_TRUE`.



You can use the following example architecture flow to update a batch index with your SAP data:

  * Update the Cloud Storage bucket with embeddings for the latest data by using the [`/GOOG/CL_STORAGE_V1`](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_storage_v1) class, through an SAP background job. For non-SAP data, this can also be done through a process outside SAP.
  * Trigger batch index updates by using the `PATCH_TREE_AH_INDEX` method of the `/GOOG/CL_VECTOR_INDEX` class through an SAP background job that's scheduled at regular intervals.



#### Update a stream index

To upsert data points in a stream index, use the `UPSERT_DATAPOINTS` method of the `/GOOG/CL_VECTOR_INDEX` class.
    
    
    lo_vector_index->upsert_datapoints( iv_index_id     = 'INDEX_ID'
                                        iv_location_id  = 'LOCATION_ID'
                                        iv_datapoint_id = 'ENTITY_ID'
                                        it_embeddings   = 'EMBEDDINGS' ).
    

Replace the following:

  * `INDEX_ID`: Resource name of the index.
  * `LOCATION_ID`: Google Cloud region of the index.
  * `ENTITY_ID`: The ID of the entity to insert or update.
  * `EMBEDDINGS`: Embeddings to upsert for the data point.



To remove information for a data point from a stream index, use the `REMOVE_DATAPOINTS` method of the `/GOOG/CL_VECTOR_INDEX` class.
    
    
    lo_vector_index->remove_datapoints( iv_index_id     = 'INDEX_ID'
                                        iv_location_id  = 'LOCATION_ID'
                                        iv_datapoint_id = 'ENTITY_ID' ).
    

Replace the following:

  * `INDEX_ID`: Resource name of the index.
  * `LOCATION_ID`: Google Cloud region of the index.
  * `ENTITY_ID`: Entity ID to remove.



Upsert and remove operations occur in real time for the index.

You can use the following example architecture flow to update a stream index with your SAP data:

  * Identify the placeholders in your enterprise SAP solution, such as BADIs, exits, enhancements, and custom SAP logic, which are points for SAP data change.
  * Trigger the upsert or remove operation for SAP data from the stream index by using the `UPSERT_DATAPOINTS` and `REMOVE_DATAPOINTS` methods of the `/GOOG/CL_VECTOR_INDEX` class, from your identified placeholder.



### Get the status of the vector index operations

Google Cloud performs the following tasks as long-running operations (LRO):

  * Creating a vector index or index endpoint
  * Deploying an index to an index endpoint
  * Updating a batch vector index



To determine the long-running operation ID, resource ID of the Agent Platform artifacts, and error messages, the SDK provides the `/GOOG/CL_VECTORINDEX_RESPONSE` class.

The SDK chains the response captured by the `/GOOG/CL_VECTORINDEX_RESPONSE` class to the requests made through the methods of the `/GOOG/CL_VECTOR_INDEX` class, so that you can directly access the response in a single statement without requiring variables to store the intermediate results.

#### Get the long-running operation ID

To get the long-running operation ID for each vector search task, you can use the `GET_LRO` method of the `/GOOG/CL_VECTORINDEX_RESPONSE` class. After executing a task, you can call the `GET_LRO` method with the same instance to get the corresponding long-running operation ID.

The following code sample illustrates how to get the long-running operation ID for a batch index update task:
    
    
    DATA(lv_patch_index_lro) = lo_vector_index->patch_tree_ah_index(
                                                  iv_index_id              = 'INDEX_ID'
                                                  iv_gcs_content_uri       = 'CONTENT_URI'
                                                  iv_location_id           = 'LOCATION_ID'
                                                  iv_is_complete_overwrite = 'IS_COMPLETE_OVERWRITE'
                                            )->get_lro( ).
    

Replace the following:

  * `INDEX_ID`: Resource name of the index.
  * `CONTENT_URI`: URI of the Cloud Storage bucket that contains the embeddings for the latest enterprise data.
  * `LOCATION_ID`: Google Cloud region of the index.
  * `IS_COMPLETE_OVERWRITE`: To completely overwrite the index with data in the given Cloud Storage bucket, set this parameter to `ABAP_TRUE`.

**Note:** Upsert and removal of data points from a stream index are executed in real time and don't return any long-running operation ID.

#### Get the status of the long-running operation

Every long-running operation has a status associated with it. To determine whether a long-running operation succeeded, check the operation status.

To determine or continually monitor the status of a long-running operation for any Agent Platform-related tasks, use the `GET_LRO_STATUS` method of the `/GOOG/CL_VERTEX_AI_SDK_UTILITY` class.
    
    
    /goog/cl_vertex_ai_sdk_utility=>get_lro_status(
        EXPORTING
            iv_key           = 'CLIENT_KEY'
            iv_operations_id = 'LONG_RUNNING_OPERATION_ID'
            iv_location_id   = 'LOCATION_ID'
        IMPORTING
            ev_is_done       = DATA(lv_is_done)          "Is the long-running operation complete
            ev_is_successful = DATA(lv_is_successful)    "Is the long-running operation successful
            ev_error_code    = DATA(lv_error_code)       "Error code in the long-running operation in case of errors
            ev_error_message = DATA(lv_error_message) ). "Error message in the long-running operation in case of errors
    

Replace the following:

  * `CLIENT_KEY`: Client key for authentication.
  * `LONG_RUNNING_OPERATION_ID`: Long-running operation ID.
  * `LOCATION_ID`: Google Cloud region of the index.



#### Get the resource ID of the Gemini Enterprise Agent Platform artifact

To determine the resource ID of the created index, created index endpoint, deployed index, or updated index, use the `GET_ID` method of the `/GOOG/CL_VECTORINDEX_RESPONSE` class.

After executing a task, you can call the `GET_ID` method with the same instance to get the corresponding resource ID.

The following code sample illustrates how to get the ID of the index being created after calling the `CREATE_TREE_AH_INDEX` method of the `/GOOG/CL_VECTOR_INDEX` class:
    
    
    DATA(lv_id) = lo_vector_index->create_tree_ah_index(
                                    iv_display_name                = 'INDEX_NAME'
                                    iv_location_id                 = 'LOCATION_ID'
                                    iv_gcs_content_uri             = 'CONTENT_URI'
                                    iv_dimensions                  = 'DIMENSIONS'
                                    iv_approximate_neighbors_count = 'NEIGHBORS_COUNT'
                                    iv_leaf_node_embedding_count   = 'LEAF_NODE_EMBEDDING_COUNT'
                                    iv_leaf_nodes_to_search        = 'LEAF_NODE_TO_SEARCH'
                                )->get_id( ).
    

Replace the following:

  * `INDEX_NAME`: Display name of the index.
  * `LOCATION_ID`: Google Cloud region of the index.
  * `CONTENT_URI`: URI of the Cloud Storage bucket containing the embeddings, which is used to build the index.
  * `DIMENSIONS`: Number of dimensions of the input vectors.
  * `NEIGHBORS_COUNT`: Neighbors to find through approximate search before reordering is performed.
  * `LEAF_NODE_EMBEDDING_COUNT`: Number of embeddings on each leaf node. The default value is `1000`.
  * `LEAF_NODE_TO_SEARCH`: The percentage of leaf nodes that a query searches. This value must be from 1 to 100, inclusive. The default value is `10` (`10%`).



#### Get the error code and the error message

Errors might occur when triggering vector index tasks through the Agent Platform SDK for ABAP.

To get the error code and the error message respectively (if any) after triggering a task, use the `GET_ERROR_CODE` and `GET_ERROR_MESSAGE` methods of the `/GOOG/CL_VECTORINDEX_RESPONSE` class.

After executing a task, you can call the `GET_ERROR_CODE` and `GET_ERROR_MESSAGE` methods with the same instance to get the corresponding error code or error message.

The following code sample illustrates how to display the error code and error message if the creation of an index fails:
    
    
    DATA(lo_vectorindex_response) = lo_vector_index->create_tree_ah_index(
                                                      iv_display_name                = 'INDEX_NAME'
                                                      iv_location_id                 = 'LOCATION_ID'
                                                      iv_gcs_content_uri             = 'CONTENT_URI'
                                                      iv_dimensions                  = 'DIMENSIONS'
                                                      iv_approximate_neighbors_count = 'NEIGHBORS_COUNT'
                                                      iv_leaf_node_embedding_count   = 'LEAF_NODE_EMBEDDING_COUNT'
                                                      iv_leaf_nodes_to_search        = 'LEAF_NODE_TO_SEARCH' ).
    IF lo_vectorindex_response->get_error_code( ) IS NOT INITIAL.
      DATA(lv_err_code) = lo_vectorindex_response->get_error_code( ).
      DATA(lv_err_msg) = lo_vectorindex_response->get_error_message( ).
      out->write( |Error Code- { lv_err_code }| ).
    ENDIF.
    

Replace the following:

  * `INDEX_NAME`: Display name of the index.
  * `LOCATION_ID`: Google Cloud region of the index.
  * `CONTENT_URI`: URI of the Cloud Storage bucket containing the embeddings, which is used to build the index.
  * `DIMENSIONS`: Number of dimensions of the input vectors.
  * `NEIGHBORS_COUNT`: Neighbors to find through approximate search before reordering is performed.
  * `LEAF_NODE_EMBEDDING_COUNT`: Number of embeddings on each leaf node. The default value is `1000`.
  * `LEAF_NODE_TO_SEARCH`: The percentage of leaf nodes that a query searches. This value must be from 1 to 100, inclusive. The default value is `10` (`10%`).



## Search nearest neighbors

You can search a deployed vector index for nearest neighbors by using an entity ID, a search string, or an embedding.

### Before you begin

Make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * [Configured the Vector Search parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-vector-search-parameters).



### Instantiate the class for Vector Search

To invoke Vector Search, you can instantiate the `/GOOG/CL_VECTOR_SEARCH` class. You instantiate the class by passing the search key, which is configured in the [Vector Search parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-vector-search-parameters).
    
    
    DATA(lo_vector_search) = NEW /goog/cl_vector_search( iv_search_name = 'SEARCH_KEY' ).
    

Replace `SEARCH_KEY` with the search key, which is configured in the [Vector Search parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-vector-search-parameters).

### Search by using an entity ID

To query a vector index by using an entity ID, use the `FIND_NEIGHBORS_BY_ENTITY_ID` method of the `/GOOG/CL_VECTOR_SEARCH` class. Entity IDs correspond to the data points stored in your vector index.
    
    
    lo_vector_search->find_neighbors_by_entity_id( iv_entity_id             = 'ENTITY_ID'
                                                   iv_neighbor_count        = 'NEIGHBOR_COUNT'
                                                   iv_return_full_datapoint = 'RETURN_FULL_DATAPOINT' ).
    

**Note:** If the searched data point is not present in the index, then Vector Search returns an error.

Replace the following:

  * `ENTITY_ID`: Entity ID to search.
  * `NEIGHBOR_COUNT`: Number of nearest neighbors to retrieve for the query.
  * `RETURN_FULL_DATAPOINT`: To return the vector embeddings for the retrieved data points, set this parameter to `ABAP_TRUE`.



### Search by using a search string

To query a vector index by using a search string, use the `FIND_NEIGHBORS_BY_STRING` method of the `/GOOG/CL_VECTOR_SEARCH` class.

The SDK first converts your search string into embeddings, and then retrieves the nearest neighbors for the query.
    
    
    DATA(lo_response) = lo_vector_search->find_neighbors_by_string(
                                            iv_search_string         = 'SEARCH_STRING'
                                            iv_embeddings_model_key  = 'MODEL_KEY'
                                            iv_neighbor_count        = 'NEIGHBOR_COUNT'
                                            iv_return_full_datapoint = 'RETURN_FULL_DATAPOINT' ).
    

Replace the following:

  * `SEARCH_STRING`: Input search string.
  * `MODEL_KEY`: The model key for generating embeddings, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `NEIGHBOR_COUNT`: Number of nearest neighbors to retrieve for the query.
  * `RETURN_FULL_DATAPOINT`: To return the vector embeddings for the retrieved data points, set this parameter to `ABAP_TRUE`.



### Search by using an embedding

To query a vector index by using embeddings, use the `FIND_NEIGHBORS_BY_EMBEDDING` method of the `/GOOG/CL_VECTOR_SEARCH` class.
    
    
    DATA(lo_response) = lo_vector_search->find_neighbors_by_embeddings(
                                            iv_neighbor_count        = 'NEIGHBOR_COUNT'
                                            iv_return_full_datapoint = 'RETURN_FULL_DATAPOINT'
                                            it_embeddings            = 'EMBEDDINGS' ).
    

Replace the following:

  * `NEIGHBOR_COUNT`: Number of nearest neighbors to retrieve for the query.
  * `RETURN_FULL_DATAPOINT`: To return the vector embeddings for the retrieved data points, set this parameter to `ABAP_TRUE`.
  * `EMBEDDINGS`: Input embeddings.



### Get the search response

To receive processed responses from the model, the SDK provides the `/GOOG/CL_VECTORSEARCH_RESPONSE` ABAP class.

The SDK chains the response captured by the `/GOOG/CL_VECTORSEARCH_RESPONSE` class to the requests made through the methods of the `/GOOG/CL_VECTOR_SEARCH` class, so that you can directly access the response in a single statement without requiring variables to store the intermediate results.

#### Get the nearest neighbors for the search query

To determine the nearest neighbors for a search query by using an entity ID, search string, or embedding, use the `GET_NEAREST_NEIGHBOR` and `GET_NEAREST_NEIGHBORS` methods of the `/GOOG/CL_VECTORSEARCH_RESPONSE` class.

Call these methods in a chain after executing the search query by using the methods `FIND_NEIGHBORS_BY_STRING`, `FIND_NEIGHBORS_BY_EMBEDDING`, and `FIND_NEIGHBORS_BY_ENTITY_ID` of the `/GOOG/CL_VECTOR_SEARCH` class.

  * To get the nearest neighbor for the searched data point, string, or embeddings, call the `GET_NEAREST_NEIGHBOR` method. The response of this method lists the ID of the closest data point, its distance from the search query, and the feature vector associated with it in the index.

The following code sample illustrates how to get the nearest neighbor for a search string:
        
        DATA(ls_nearest_neighbor) = lo_vector_search->find_neighbors_by_string(
                                                        iv_search_string         = 'SEARCH_STRING'
                                                        iv_embeddings_model_key  = 'MODEL_KEY'
                                                        iv_neighbor_count        = 'NEIGHBOR_COUNT'
                                                        iv_return_full_datapoint = 'RETURN_FULL_DATAPOINT'
                                                   )->get_nearest_neighbor( ).
        

Replace the following:

    * `SEARCH_STRING`: Input search string.
    * `MODEL_KEY`: The model key for generating embeddings, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
    * `NEIGHBOR_COUNT`: Number of nearest neighbors to retrieve for the query.
    * `RETURN_FULL_DATAPOINT`: To return the vector embeddings for the retrieved data points, set this parameter to `ABAP_TRUE`.
  * To get the set of nearest neighbors for the searched data point, string, or embeddings, call the `GET_NEAREST_NEIGHBORS` method. The response of this method is a table of closest data points, listing the data point IDs, their distance from the search query, and the feature vector associated with them in the index.

The following code sample illustrates how to get the nearest neighbors for a search string:
        
        DATA(lt_nearest_neighbors) = lo_vector_search->find_neighbors_by_string(
                                                         iv_search_string         = 'SEARCH_STRING'
                                                         iv_embeddings_model_key  = 'MODEL_KEY'
                                                         iv_neighbor_count        = 'NEIGHBOR_COUNT'
                                                         iv_return_full_datapoint = 'RETURN_FULL_DATAPOINT'
                                                    )->get_nearest_neighbors( ).
        

Replace the following:

    * `SEARCH_STRING`: Input search string.
    * `MODEL_KEY`: The model key for generating embeddings, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
    * `NEIGHBOR_COUNT`: Number of nearest neighbors to retrieve for the query.
    * `RETURN_FULL_DATAPOINT`: To return the vector embeddings for the retrieved data points, set this parameter to `ABAP_TRUE`.



### Get the distance of the fetched neighbor

To determine the distance of a fetched response from the searched query, you can use the `GET_DATAPOINT_DISTANCE` method of the `/GOOG/CL_VECTORSEARCH_RESPONSE` class.

Distance in the search response represents a measure of dissimilarity between the query (string, embedding, or entity ID) and a retrieved result vector. The meaning of the distance value depends on the distance measure type that you select when you create the index.

The distance value shows how relevant each search result is to your query. Results with lower distances indicate closer matches, while those with higher distances are less relevant.

The following code sample illustrates how to get the distance of the nearest neighbor for a search string:
    
    
    DATA(lo_vectorsearch_response) = lo_vector_search->find_neighbors_by_string(
                                                         iv_search_string         = 'SEARCH_STRING'
                                                         iv_embeddings_model_key  = 'MODEL_KEY'
                                                         iv_neighbor_count        = 'NEIGHBOR_COUNT'
                                                         iv_return_full_datapoint = 'RETURN_FULL_DATAPOINT' ).
    DATA(ls_nearest_neighbor) = lo_vectorsearch_response->get_nearest_neighbor( ).
    DATA(lv_distance) = lo_vectorsearch_response->get_datapoint_distance( iv_datapoint_id = ls_nearest_neighbor-datapoint_id ).
    

Replace the following:

  * `SEARCH_STRING`: Input search string.
  * `MODEL_KEY`: The model key for generating embeddings, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `NEIGHBOR_COUNT`: Number of nearest neighbors to retrieve for the query.
  * `RETURN_FULL_DATAPOINT`: To return the vector embeddings for the retrieved data points, set this parameter to `ABAP_TRUE`.



### Retrieve the embeddings vector of the fetched neighbor

To determine the embeddings vector of the fetched response from the searched query, use the `GET_DATAPOINT_FEATURE_VECTOR` method of the `/GOOG/CL_VECTORSEARCH_RESPONSE` class.

To retrieve an embeddings vector, you must set the `IV_RETURN_FULL_DATAPOINT` parameter to `ABAP_TRUE` when calling the `FIND_NEIGHBORS_BY_STRING`, `FIND_NEIGHBORS_BY_EMBEDDING`, or `FIND_NEIGHBORS_BY_ENTITY_ID` methods.

The following code sample illustrates how to retrieve the feature vector of the nearest neighbor for a search string:
    
    
    DATA(lo_vectorsearch_response) = lo_vector_search->find_neighbors_by_string(
                                                         iv_search_string         = 'SEARCH_STRING'
                                                         iv_embeddings_model_key  = 'MODEL_KEY'
                                                         iv_neighbor_count        = 'NEIGHBOR_COUNT'
                                                         iv_return_full_datapoint = 'RETURN_FULL_DATAPOINT' ).
    DATA(ls_nearest_neighbor) = lo_vectorsearch_response->get_nearest_neighbor( ).
    DATA(lt_feature_vector) = lo_vectorsearch_response->get_datapoint_feature_vector( iv_datapoint_id = ls_nearest_neighbor-datapoint_id ).
    

Replace the following:

  * `SEARCH_STRING`: Input search string.
  * `MODEL_KEY`: The model key for generating embeddings, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `NEIGHBOR_COUNT`: Number of nearest neighbors to retrieve for the query.
  * `RETURN_FULL_DATAPOINT`: To return the vector embeddings for the retrieved data points, set this parameter to `ABAP_TRUE`.



## What's next

  * Learn about [Vector Search terminology](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview#terminology).

  * Learn about [application development with the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer).

  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
