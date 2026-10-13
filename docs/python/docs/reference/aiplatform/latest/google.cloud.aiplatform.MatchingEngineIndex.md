---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndex
title: Class MatchingEngineIndex (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:45.332727+00:00
---

# Class MatchingEngineIndex (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndex

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MatchingEngineIndex (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    MatchingEngineIndex(
        index_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Matching Engine index resource for Vertex AI.

## Properties 

### create_time

Time this resource was created.

### deployed_indexes

Returns a list of deployed index references that originate from this index.

### description

Description of the index.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### gca_resource

The underlying resource proto representation.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### resource_name

Full qualified resource name.

### update_time

Time this resource was last updated.

## Methods 

### MatchingEngineIndex
    
    
    MatchingEngineIndex(
        index_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves an existing index given an index name or ID.

Example Usage:
    
    
    my_index = aiplatform.MatchingEngineIndex(
        index_name='projects/123/locations/us-central1/indexes/my_index_id'
    )
    or
    my_index = aiplatform.MatchingEngineIndex(
        index_name='my_index_id'
    )
    

**Parameters**  
---  
**Name** | **Description**  
`index_name` |  `str`   
Required. A fully-qualified index resource name or a index ID. Example: "projects/123/locations/us-central1/indexes/my_index_id" or "my_index_id" when project and location are initialized or passed.  
`project` |  `str`   
Optional. Project to retrieve index from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve index from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this Index. Overrides credentials set in aiplatform.init.  
  
### create_brute_force_index
    
    
    create_brute_force_index(
        display_name: str,
        contents_delta_uri: typing.Optional[str] = None,
        dimensions: typing.Optional[int] = None,
        distance_measure_type: typing.Optional[
            google.cloud.aiplatform.matching_engine.matching_engine_index_config.DistanceMeasureType
        ] = None,
        feature_norm_type: typing.Optional[
            google.cloud.aiplatform.matching_engine.matching_engine_index_config.FeatureNormType
        ] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        index_update_method: typing.Optional[str] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        create_request_timeout: typing.Optional[float] = None,
        shard_size: typing.Optional[str] = None,
    ) -> google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex

Creates a MatchingEngineIndex resource that uses the brute force algorithm.

Example Usage:
    
    
    my_index = aiplatform.Index.create_brute_force_index(
        display_name="my_display_name",
        contents_delta_uri="gs://my_bucket/embeddings",
        dimensions=1,
        approximate_neighbors_count=150,
        distance_measure_type=matching_engine_index_config.DistanceMeasureType.SQUARED_L2_DISTANCE,
        description="my description",
        labels={ "label_name": "label_value" },
    )
    

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The display name of the Index. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`contents_delta_uri` |  `str`   
Optional. Allows inserting the initial contents of the Matching Engine Index. The string must be a valid Google Cloud Storage directory path. The expected structure and format of the files this URI points to is described at <https://cloud.google.com/vertex-ai/docs/vector-search/setup/format-structure>  
`dimensions` |  `int`   
Required. The number of dimensions of the input vectors.  
`distance_measure_type` |  `matching_engine_index_config.DistanceMeasureType`   
Optional. The distance measure used in nearest neighbor search.  
`feature_norm_type` |  `matching_engine_index_config.FeatureNormType`   
Optional. The feature norm type used in nearest neighbor search.  
`description` |  `str`   
Optional. The description of the Index.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Index. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one Index(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`project` |  `str`   
Optional. Project to create EntityType in. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to create EntityType in. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create EntityTypes. Overrides credentials set in aiplatform.init.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`sync` |  `bool`   
Optional. Whether to execute this creation synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`index_update_method` |  `str`   
Optional. The update method to use with this index. Choose stream_update or batch_update. If not set, batch update will be used by default.  
`encryption_spec_key_name` |  `str`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the index. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this index and all sub-resources of this index will be secured by this key. The key needs to be in the same region as where the index is created.  
`create_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
`shard_size` |  `str`   
Optional. The size of each shard. Index will get resharded based on specified shard size. During serving, each shard will be served on a separate node and will scale independently. If not set, shard size is default to SHARD_SIZE_MEDIUM. Choose one of the following: SHARD_SIZE_SMALL SHARD_SIZE_MEDIUM SHARD_SIZE_LARGE SHARD_SIZE_SO_DYNAMIC  
  
### create_tree_ah_index
    
    
    create_tree_ah_index(
        display_name: str,
        contents_delta_uri: typing.Optional[str] = None,
        dimensions: typing.Optional[int] = None,
        approximate_neighbors_count: typing.Optional[int] = None,
        leaf_node_embedding_count: typing.Optional[int] = None,
        leaf_nodes_to_search_percent: typing.Optional[float] = None,
        distance_measure_type: typing.Optional[
            google.cloud.aiplatform.matching_engine.matching_engine_index_config.DistanceMeasureType
        ] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        index_update_method: typing.Optional[str] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        create_request_timeout: typing.Optional[float] = None,
        shard_size: typing.Optional[str] = None,
        feature_norm_type: typing.Optional[
            google.cloud.aiplatform.matching_engine.matching_engine_index_config.FeatureNormType
        ] = None,
    ) -> google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex

Creates a MatchingEngineIndex resource that uses the tree-AH algorithm.

Example Usage:
    
    
    my_index = aiplatform.Index.create_tree_ah_index(
        display_name="my_display_name",
        contents_delta_uri="gs://my_bucket/embeddings",
        dimensions=1,
        approximate_neighbors_count=150,
        distance_measure_type=matching_engine_index_config.DistanceMeasureType.SQUARED_L2_DISTANCE,
        leaf_node_embedding_count=100,
        leaf_nodes_to_search_percent=50,
        description="my description",
        labels={ "label_name": "label_value" },
    )
    

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The display name of the Index. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`contents_delta_uri` |  `str`   
Optional. Allows inserting the initial contents of the Matching Engine Index. The string must be a valid Google Cloud Storage directory path. The expected structure and format of the files this URI points to is described at <https://cloud.google.com/vertex-ai/docs/vector-search/setup/format-structure>  
`dimensions` |  `int`   
Required. The number of dimensions of the input vectors.  
`approximate_neighbors_count` |  `int`   
Required. The default number of neighbors to find via approximate search before exact reordering is performed. Exact reordering is a procedure where results returned by an approximate search algorithm are reordered via a more expensive distance computation.  
`leaf_node_embedding_count` |  `int`   
Optional. Number of embeddings on each leaf node. The default value is 1000 if not set.  
`leaf_nodes_to_search_percent` |  `float`   
Optional. The default percentage of leaf nodes that any query may be searched. Must be in range 1-100, inclusive. The default value is 10 (means 10%) if not set.  
`distance_measure_type` |  `matching_engine_index_config.DistanceMeasureType`   
Optional. The distance measure used in nearest neighbor search.  
`feature_norm_type` |  `matching_engine_index_config.FeatureNormType`   
Optional. The feature norm type used in nearest neighbor search.  
`description` |  `str`   
Optional. The description of the Index.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Index. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one Index(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`project` |  `str`   
Optional. Project to create EntityType in. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to create EntityType in. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create EntityTypes. Overrides credentials set in aiplatform.init.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`sync` |  `bool`   
Optional. Whether to execute this creation synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`index_update_method` |  `str`   
Optional. The update method to use with this index. Choose STREAM_UPDATE or BATCH_UPDATE. If not set, batch update will be used by default.  
`encryption_spec_key_name` |  `str`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the index. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this index and all sub-resources of this index will be secured by this key. The key needs to be in the same region as where the index is created.  
`create_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
`shard_size` |  `str`   
Optional. The size of each shard. Index will get resharded based on specified shard size. During serving, each shard will be served on a separate node and will scale independently. Choose one of the following: SHARD_SIZE_SMALL SHARD_SIZE_MEDIUM SHARD_SIZE_LARGE SHARD_SIZE_SO_DYNAMIC  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### import_embeddings
    
    
    import_embeddings(
        config: google.cloud.aiplatform_v1beta1.types.index_service.ImportIndexRequest.ConnectorConfig,
        is_complete_overwrite: typing.Optional[bool] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        import_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex

Imports embeddings from an external source, e.g., BigQuery.

**Parameters**  
---  
**Name** | **Description**  
`config` |  `aiplatform.compat.types.index_service.ConnectorConfig`   
Required. The configuration for importing data from an external source.  
`is_complete_overwrite` |  `bool`   
Optional. If true, completely replace existing index data. Must be true for streaming update indexes.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`import_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        parent: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Vertex AI Resource.

Example Usage:

aiplatform.BatchPredictionJobs.list( filter='state="JOB_STATE_SUCCEEDED" AND display_name="my_job"', )

aiplatform.Model.list(order_by="create_time desc, display_name")

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: `display_name`, `create_time`, `update_time`  
`project` |  `str`   
Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.  
`parent` |  `str`   
Optional. The parent resource name if any to retrieve list from.  
  
### remove_datapoints
    
    
    remove_datapoints(
        datapoint_ids: typing.Sequence[str],
    ) -> google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex

Remove datapoints for this index.

**Parameter**  
---  
**Name** | **Description**  
`datapoints_ids` |  `Sequence[str]`   
Required. The list of datapoints ids to be deleted.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update_embeddings
    
    
    update_embeddings(
        contents_delta_uri: str,
        is_complete_overwrite: typing.Optional[bool] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        update_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex

Updates the embeddings for this index.

**Parameters**  
---  
**Name** | **Description**  
`contents_delta_uri` |  `str`   
Required. Allows inserting, updating or deleting the contents of the Matching Engine Index. The string must be a valid Google Cloud Storage directory path. The expected structure and format of the files this URI points to is described at <https://cloud.google.com/vertex-ai/docs/vector-search/setup/format-structure>  
`is_complete_overwrite` |  `bool`   
Optional. If this field is set together with contentsDeltaUri when calling IndexService.UpdateIndex, then existing content of the Index will be replaced by the data from the contentsDeltaUri.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`update_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
  
### update_metadata
    
    
    update_metadata(
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        update_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex

Updates the metadata for this index.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The display name of the Index. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`description` |  `str`   
Optional. The description of the Index.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Indexs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one Index (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`update_request_timeout` |  `float`   
Optional. The timeout for the request in seconds.  
  
### upsert_datapoints
    
    
    upsert_datapoints(
        datapoints: typing.Sequence[google.cloud.aiplatform_v1.types.index.IndexDatapoint],
        update_mask: typing.Optional[typing.Sequence[str]] = None,
    ) -> google.cloud.aiplatform.matching_engine.matching_engine_index.MatchingEngineIndex

Upsert datapoints to this index.

**Parameters**  
---  
**Name** | **Description**  
`datapoints` |  `Sequence[gca_matching_engine_index.IndexDatapoint]`   
Required. Datapoints to be upserted to this index.  
`update_mask` |  `Sequence[str]`   
Optional. Update mask is used to specify the fields to be overwritten in the datapoints by the update. The fields specified in the update_mask are relative to each IndexDatapoint inside datapoints, not the full request. Updatable fields: Use `all_restricts` to update both `restricts` and `numeric_restricts`. Use `embedding_metadata` to update `embedding_metadata`.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
