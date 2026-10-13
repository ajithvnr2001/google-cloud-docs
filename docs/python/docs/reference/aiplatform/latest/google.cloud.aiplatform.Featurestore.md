---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Featurestore
title: Class Featurestore (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:42.014103+00:00
---

# Class Featurestore (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Featurestore

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Featurestore (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    Featurestore(
        featurestore_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Managed featurestore resource for Vertex AI.

## Properties 

### create_time

Time this resource was created.

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

### Featurestore
    
    
    Featurestore(
        featurestore_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves an existing managed featurestore given a featurestore resource name or a featurestore ID.

Example Usage:
    
    
    my_featurestore = aiplatform.Featurestore(
        featurestore_name='projects/123/locations/us-central1/featurestores/my_featurestore_id'
    )
    or
    my_featurestore = aiplatform.Featurestore(
        featurestore_name='my_featurestore_id'
    )
    

**Parameters**  
---  
**Name** | **Description**  
`featurestore_name` |  `str`   
Required. A fully-qualified featurestore resource name or a featurestore ID. Example: "projects/123/locations/us-central1/featurestores/my_featurestore_id" or "my_featurestore_id" when project and location are initialized or passed.  
`project` |  `str`   
Optional. Project to retrieve featurestore from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve featurestore from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this Featurestore. Overrides credentials set in aiplatform.init.  
  
### batch_serve_to_bq
    
    
    batch_serve_to_bq(
        bq_destination_output_uri: str,
        serving_feature_ids: typing.Dict[str, typing.List[str]],
        read_instances_uri: str,
        pass_through_fields: typing.Optional[typing.List[str]] = None,
        feature_destination_fields: typing.Optional[typing.Dict[str, str]] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        serve_request_timeout: typing.Optional[float] = None,
        sync: bool = True,
    ) -> google.cloud.aiplatform.featurestore.featurestore.Featurestore

Batch serves feature values to BigQuery destination

**Exceptions**  
---  
**Type** | **Description**  
`NotFound` | if the BigQuery destination Dataset does not exist.  
`FailedPrecondition` | if the BigQuery destination Dataset/Table is in a different project.  
**Returns**  
---  
**Type** | **Description**  
`Featurestore` | The featurestore resource object batch read feature values from.  
  
### batch_serve_to_df
    
    
    batch_serve_to_df(
        serving_feature_ids: typing.Dict[str, typing.List[str]],
        read_instances_df: pd.DataFrame,
        pass_through_fields: typing.Optional[typing.List[str]] = None,
        feature_destination_fields: typing.Optional[typing.Dict[str, str]] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        serve_request_timeout: typing.Optional[float] = None,
        bq_dataset_id: typing.Optional[str] = None,
    ) -> pd.DataFrame

Batch serves feature values to pandas DataFrame

**Note:** Calling this method will automatically create and delete a temporary bigquery dataset in the same GCP project, which will be used as the intermediary storage for batch serve feature values from featurestore to dataframe. 

**Parameters**  
---  
**Name** | **Description**  
`serving_feature_ids` |  `Dict[str, List[str]]`   
Required. A user defined dictionary to define the entity_types and their features for batch serve/read. The keys of the dictionary are the serving entity_type ids and the values are lists of serving feature ids in each entity_type. .. rubric:: Example serving_feature_ids = { 'my_entity_type_id_1': ['feature_id_1_1', 'feature_id_1_2'], 'my_entity_type_id_2': ['feature_id_2_1', 'feature_id_2_2'], }  
`read_instances_df` |  `pd.DataFrame`   
Required. Read_instances_df is a pandas DataFrame containing the read instances. Each read instance should consist of exactly one read timestamp and one or more entity IDs identifying entities of the corresponding EntityTypes whose Features are requested. Each output instance contains Feature values of requested entities concatenated together as of the read time. An example read_instances_df may be pd.DataFrame( data=[ { "my_entity_type_id_1": "my_entity_type_id_1_entity_1", "my_entity_type_id_2": "my_entity_type_id_2_entity_1", "timestamp": "2020-01-01T10:00:00.123Z" ], ) An example batch_serve_output_df may be pd.DataFrame( data=[ { "my_entity_type_id_1": "my_entity_type_id_1_entity_1", "my_entity_type_id_2": "my_entity_type_id_2_entity_1", "foo": "feature_id_1_1_feature_value", "feature_id_1_2": "feature_id_1_2_feature_value", "feature_id_2_1": "feature_id_2_1_feature_value", "bar": "feature_id_2_2_feature_value", "timestamp": "2020-01-01T10:00:00.123Z" ], ) Timestamp in each read instance must be millisecond-aligned. The columns can be in any order. Values in the timestamp column must use the RFC 3339 format, e.g. `2012-07-30T10:43:17.123Z`.  
`pass_through_fields` |  `List[str]`   
Optional. When not empty, the specified fields in the read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity. For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes.  
`feature_destination_fields` |  `Dict[str, str]`   
Optional. A user defined dictionary to map a feature's fully qualified resource name to its destination field name. If the destination field name is not defined, the feature ID will be used as its destination field name. .. rubric:: Example feature_destination_fields = { 'projects/123/locations/us-central1/featurestores/fs_id/entityTypes/et_id1/features/f_id11': 'foo', 'projects/123/locations/us-central1/featurestores/fs_id/entityTypes/et_id2/features/f_id22': 'bar', }  
`serve_request_timeout` |  `float`   
Optional. The timeout for the serve request in seconds.  
`bq_dataset_id` |  `str`   
Optional. The full dataset ID for the BigQuery dataset to use for temporarily staging data. If specified, caller must have `bigquery.tables.create` permissions for Dataset.  
`start_time` |  `timestamp_pb2.Timestamp`   
Optional. Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision.  
**Returns**  
---  
**Type** | **Description**  
`pd.DataFrame` | The pandas DataFrame containing feature values from batch serving.  
  
### batch_serve_to_gcs
    
    
    batch_serve_to_gcs(
        gcs_destination_output_uri_prefix: str,
        gcs_destination_type: str,
        serving_feature_ids: typing.Dict[str, typing.List[str]],
        read_instances_uri: str,
        pass_through_fields: typing.Optional[typing.List[str]] = None,
        feature_destination_fields: typing.Optional[typing.Dict[str, str]] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        serve_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore.featurestore.Featurestore

Batch serves feature values to GCS destination

**Exceptions**  
---  
**Type** | **Description**  
`ValueErro` | if gcs_destination_type is not supported.:  
**Returns**  
---  
**Type** | **Description**  
`Featurestore` | The featurestore resource object batch read feature values from.  
  
### create
    
    
    create(
        featurestore_id: str,
        online_store_fixed_node_count: typing.Optional[int] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        encryption_spec_key_name: typing.Optional[str] = None,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore.featurestore.Featurestore

Creates a Featurestore resource.

Example Usage:
    
    
    my_featurestore = aiplatform.Featurestore.create(
        featurestore_id='my_featurestore_id',
    )
    

### create_entity_type
    
    
    create_entity_type(
        entity_type_id: str,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore.entity_type.EntityType

Creates an EntityType resource in this Featurestore.

Example Usage:
    
    
    my_featurestore = aiplatform.Featurestore.create(
        featurestore_id='my_featurestore_id'
    )
    my_entity_type = my_featurestore.create_entity_type(
        entity_type_id='my_entity_type_id',
    )
    

**Parameters**  
---  
**Name** | **Description**  
`entity_type_id` |  `str`   
Required. The ID to use for the EntityType, which will become the final component of the EntityType's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a featurestore.  
`description` |  `str`   
Optional. Description of the EntityType.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your EntityTypes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one EntityType (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`sync` |  `bool`   
Optional. Whether to execute this creation synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
  
### delete
    
    
    delete(sync: bool = True, force: bool = False) -> None

Deletes this Featurestore resource. If force is set to True, all entityTypes in this Featurestore will be deleted prior to featurestore deletion, and all features in each entityType will be deleted prior to each entityType deletion.

WARNING: This deletion is permanent.

### delete_entity_types
    
    
    delete_entity_types(
        entity_type_ids: typing.List[str], sync: bool = True, force: bool = False
    ) -> None

Deletes entity_type resources in this Featurestore given their entity_type IDs. WARNING: This deletion is permanent.

### get_entity_type
    
    
    get_entity_type(
        entity_type_id: str,
    ) -> google.cloud.aiplatform.featurestore.entity_type.EntityType

Retrieves an existing managed entityType in this Featurestore.

**Parameter**  
---  
**Name** | **Description**  
`entity_type_id` |  `str`   
Required. The managed entityType resource ID in this Featurestore.  
  
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
  
### list_entity_types
    
    
    list_entity_types(
        filter: typing.Optional[str] = None, order_by: typing.Optional[str] = None
    ) -> typing.List[google.cloud.aiplatform.featurestore.entity_type.EntityType]

Lists existing managed entityType resources in this Featurestore.

Example Usage:
    
    
    my_featurestore = aiplatform.Featurestore(
        featurestore_name='my_featurestore_id',
    )
    my_featurestore.list_entity_types()
    

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. Lists the EntityTypes that match the filter expression. The following filters are supported: - `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. - `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. - `labels`: Supports key-value equality as well as key presence. Examples: - `create_time > "2020-01-31T15:30:00.000000Z" OR update_time > "2020-01-31T15:30:00.000000Z"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. - `labels.active = yes AND labels.env = prod` \--> EntityTypes having both (active: yes) and (env: prod) labels. - `labels.env: *` \--> Any EntityType which has a label with 'env' as the key.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: - `entity_type_id` \- `create_time` \- `update_time`  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        labels: typing.Optional[typing.Dict[str, str]] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        update_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore.featurestore.Featurestore

Updates an existing managed featurestore resource.

Example Usage:
    
    
    my_featurestore = aiplatform.Featurestore(
        featurestore_name='my_featurestore_id',
    )
    my_featurestore.update(
        labels={'update my key': 'update my value'},
    )
    

**Parameters**  
---  
**Name** | **Description**  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Featurestores. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`update_request_timeout` |  `float`   
Optional. The timeout for the update request in seconds.  
  
### update_online_store
    
    
    update_online_store(
        fixed_node_count: int,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        update_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore.featurestore.Featurestore

Updates the online store of an existing managed featurestore resource.

Example Usage:
    
    
    my_featurestore = aiplatform.Featurestore(
        featurestore_name='my_featurestore_id',
    )
    my_featurestore.update_online_store(
        fixed_node_count=2,
    )
    

**Parameters**  
---  
**Name** | **Description**  
`fixed_node_count` |  `int`   
Required. Config for online serving resources, can only update the node count to >= 1.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`update_request_timeout` |  `float`   
Optional. The timeout for the update request in seconds.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
