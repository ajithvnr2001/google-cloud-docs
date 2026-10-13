---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.EntityType
title: Class EntityType (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:37.986646+00:00
---

# Class EntityType (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.EntityType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EntityType (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    EntityType(
        entity_type_name: str,
        featurestore_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Public managed EntityType resource for Vertex AI.

## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### featurestore_name

Full qualified resource name of the managed featurestore in which this EntityType is.

### gca_resource

The underlying resource proto representation.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### preview

Exposes features available in preview for this class.

### resource_name

Full qualified resource name.

### update_time

Time this resource was last updated.

## Methods 

### EntityType
    
    
    EntityType(
        entity_type_name: str,
        featurestore_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves an existing managed entityType given an entityType resource name or an entity_type ID.

Example Usage:
    
    
    my_entity_type = aiplatform.EntityType(
        entity_type_name='projects/123/locations/us-central1/featurestores/my_featurestore_id/                entityTypes/my_entity_type_id'
    )
    or
    my_entity_type = aiplatform.EntityType(
        entity_type_name='my_entity_type_id',
        featurestore_id='my_featurestore_id',
    )
    

**Parameters**  
---  
**Name** | **Description**  
`entity_type_name` |  `str`   
Required. A fully-qualified entityType resource name or an entity_type ID. Example: "projects/123/locations/us-central1/featurestores/my_featurestore_id/entityTypes/my_entity_type_id" or "my_entity_type_id" when project and location are initialized or passed, with featurestore_id passed.  
`featurestore_id` |  `str`   
Optional. Featurestore ID of an existing featurestore to retrieve entityType from, when entity_type_name is passed as entity_type ID.  
`project` |  `str`   
Optional. Project to retrieve entityType from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve entityType from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this EntityType. Overrides credentials set in aiplatform.init.  
  
### batch_create_features
    
    
    batch_create_features(
        feature_configs: typing.Dict[
            str, typing.Dict[str, typing.Union[bool, int, typing.Dict[str, str], str]]
        ],
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
    ) -> google.cloud.aiplatform.featurestore._entity_type._EntityType

Batch creates Feature resources in this EntityType.

Example Usage:
    
    
    my_entity_type = aiplatform.EntityType(
        entity_type_name='my_entity_type_id',
        featurestore_id='my_featurestore_id',
    )
    my_entity_type.batch_create_features(
        feature_configs={
            "my_feature_id1": {
                    "value_type": "INT64",
                },
            "my_feature_id2": {
                    "value_type": "BOOL",
                },
            "my_feature_id3": {
                    "value_type": "STRING",
                },
        }
    )
    

### create
    
    
    create(
        entity_type_id: str,
        featurestore_name: str,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore._entity_type._EntityType

Creates an EntityType resource in a Featurestore.

Example Usage:
    
    
    my_entity_type = aiplatform.EntityType.create(
        entity_type_id='my_entity_type_id',
        featurestore_name='projects/123/locations/us-central1/featurestores/my_featurestore_id'
    )
    or
    my_entity_type = aiplatform.EntityType.create(
        entity_type_id='my_entity_type_id',
        featurestore_name='my_featurestore_id',
    )
    

### create_feature
    
    
    create_feature(
        feature_id: str,
        value_type: str,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore.feature.Feature

Creates a Feature resource in this EntityType.

Example Usage:
    
    
    my_entity_type = aiplatform.EntityType(
        entity_type_name='my_entity_type_id',
        featurestore_id='my_featurestore_id',
    )
    my_feature = my_entity_type.create_feature(
        feature_id='my_feature_id',
        value_type='INT64',
    )
    

**Parameters**  
---  
**Name** | **Description**  
`feature_id` |  `str`   
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name, which is immutable. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType.  
`value_type` |  `str`   
Required. Immutable. Type of Feature value. One of BOOL, BOOL_ARRAY, DOUBLE, DOUBLE_ARRAY, INT64, INT64_ARRAY, STRING, STRING_ARRAY, BYTES.  
`description` |  `str`   
Optional. Description of the Feature.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`sync` |  `bool`   
Optional. Whether to execute this creation synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
  
### delete
    
    
    delete(sync: bool = True, force: bool = False) -> None

Deletes this EntityType resource. If force is set to True, all features in this EntityType will be deleted prior to entityType deletion.

WARNING: This deletion is permanent.

**Exceptions**  
---  
**Type** | **Description**  
`FailedPrecondition` | If features are created in this EntityType and force = False.  
  
### delete_features
    
    
    delete_features(feature_ids: typing.List[str], sync: bool = True) -> None

Deletes feature resources in this EntityType given their feature IDs. WARNING: This deletion is permanent.

### get_feature
    
    
    get_feature(
        feature_id: str,
    ) -> google.cloud.aiplatform.featurestore.feature.Feature

Retrieves an existing managed feature in this EntityType.

**Parameter**  
---  
**Name** | **Description**  
`feature_id` |  `str`   
Required. The managed feature resource ID in this EntityType.  
  
### get_featurestore
    
    
    get_featurestore() -> (
        google.cloud.aiplatform.featurestore.featurestore.Featurestore
    )

Retrieves the managed featurestore in which this EntityType is.

### ingest_from_bq
    
    
    ingest_from_bq(
        feature_ids: typing.List[str],
        feature_time: typing.Union[str, datetime.datetime],
        bq_source_uri: str,
        feature_source_fields: typing.Optional[typing.Dict[str, str]] = None,
        entity_id_field: typing.Optional[str] = None,
        disable_online_serving: typing.Optional[bool] = None,
        worker_count: typing.Optional[int] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        ingest_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore._entity_type._EntityType

Ingest feature values from BigQuery.

### ingest_from_df
    
    
    ingest_from_df(
        feature_ids: typing.List[str],
        feature_time: typing.Union[str, datetime.datetime],
        df_source: pd.DataFrame,
        feature_source_fields: typing.Optional[typing.Dict[str, str]] = None,
        entity_id_field: typing.Optional[str] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        ingest_request_timeout: typing.Optional[float] = None,
    ) -> _EntityType

Ingest feature values from DataFrame.

**Note:** Calling this method will automatically create and delete a temporary bigquery dataset in the same GCP project, which will be used as the intermediary storage for ingesting feature values from dataframe to featurestore. The call will return upon ingestion completes, where the feature values will be ingested into the entity_type. 

**Parameters**  
---  
**Name** | **Description**  
`feature_ids` |  `List[str]`   
Required. IDs of the Feature to import values of. The Features must exist in the target EntityType, or the request will fail.  
`feature_time` |  `Union[str, datetime.datetime]`   
Required. The feature_time can be one of: - The source column that holds the Feature timestamp for all Feature values in each entity. Note: The dtype of the source column should be `datetime64`. - A single Feature timestamp for all entities being imported. The timestamp must not have higher than millisecond precision. Example: feature_time = datetime.datetime(year=2022, month=1, day=1, hour=11, minute=59, second=59) or feature_time_str = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds") feature_time = datetime.datetime.strptime(feature_time_str, "%Y-%m-%d %H:%M:%S.%f")  
`df_source` |  `pd.DataFrame`   
Required. Pandas DataFrame containing the source data for ingestion.  
`feature_source_fields` |  `Dict[str, str]`   
Optional. User defined dictionary to map ID of the Feature for importing values of to the source column for getting the Feature values from. Specify the features whose ID and source column are not the same. If not provided, the source column need to be the same as the Feature ID. .. rubric:: Example feature_ids = ['my_feature_id_1', 'my_feature_id_2', 'my_feature_id_3'] feature_source_fields = { 'my_feature_id_1': 'my_feature_id_1_source_field', } Note: The source column of 'my_feature_id_1' is 'my_feature_id_1_source_field', The source column of 'my_feature_id_2' is the ID of the feature, same for 'my_feature_id_3'.  
`entity_id_field` |  `str`   
Optional. Source column that holds entity IDs. If not provided, entity IDs are extracted from the column named `entity_id`.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`ingest_request_timeout` |  `float`   
Optional. The timeout for the ingest request in seconds.  
  
### ingest_from_gcs
    
    
    ingest_from_gcs(
        feature_ids: typing.List[str],
        feature_time: typing.Union[str, datetime.datetime],
        gcs_source_uris: typing.Union[str, typing.List[str]],
        gcs_source_type: str,
        feature_source_fields: typing.Optional[typing.Dict[str, str]] = None,
        entity_id_field: typing.Optional[str] = None,
        disable_online_serving: typing.Optional[bool] = None,
        worker_count: typing.Optional[int] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync: bool = True,
        ingest_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore._entity_type._EntityType

Ingest feature values from GCS.

**Exceptions**  
---  
**Type** | **Description**  
`ValueErro` | if gcs_source_type is not supported.:  
  
### list
    
    
    list(
        featurestore_name: str,
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.featurestore._entity_type._EntityType]

Lists existing managed entityType resources in a featurestore, given a featurestore resource name or a featurestore ID.

Example Usage:
    
    
    my_entityTypes = aiplatform.EntityType.list(
        featurestore_name='projects/123/locations/us-central1/featurestores/my_featurestore_id'
    )
    or
    my_entityTypes = aiplatform.EntityType.list(
        featurestore_name='my_featurestore_id'
    )
    

**Parameters**  
---  
**Name** | **Description**  
`featurestore_name` |  `str`   
Required. A fully-qualified featurestore resource name or a featurestore ID of an existing featurestore to list entityTypes in. Example: "projects/123/locations/us-central1/featurestores/my_featurestore_id" or "my_featurestore_id" when project and location are initialized or passed.  
`filter` |  `str`   
Optional. Lists the EntityTypes that match the filter expression. The following filters are supported: - `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. - `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. - `labels`: Supports key-value equality as well as key presence. Examples: - `create_time > "2020-01-31T15:30:00.000000Z" OR update_time > "2020-01-31T15:30:00.000000Z"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. - `labels.active = yes AND labels.env = prod` \--> EntityTypes having both (active: yes) and (env: prod) labels. - `labels.env: *` \--> Any EntityType which has a label with 'env' as the key.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: - `entity_type_id` \- `create_time` \- `update_time`  
`project` |  `str`   
Optional. Project to list entityTypes in. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to list entityTypes in. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to list entityTypes. Overrides credentials set in aiplatform.init.  
  
### list_features
    
    
    list_features(
        filter: typing.Optional[str] = None, order_by: typing.Optional[str] = None
    ) -> typing.List[google.cloud.aiplatform.featurestore.feature.Feature]

Lists existing managed feature resources in this EntityType.

Example Usage:
    
    
    my_entity_type = aiplatform.EntityType(
        entity_type_name='my_entity_type_id',
        featurestore_id='my_featurestore_id',
    )
    my_entityType.list_features()
    

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. Lists the Features that match the filter expression. The following filters are supported: - `value_type`: Supports = and != comparisons. - `create_time`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format. - `update_time`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format. - `labels`: Supports key-value equality as well as key presence. Examples: - `value_type = DOUBLE` \--> Features whose type is DOUBLE. - `create_time > "2020-01-31T15:30:00.000000Z" OR update_time > "2020-01-31T15:30:00.000000Z"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z. - `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels. - `labels.env: *` \--> Any Feature which has a label with 'env' as the key.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: - `feature_id` \- `value_type` \- `create_time` \- `update_time`  
  
### read
    
    
    read(
        entity_ids: typing.Union[str, typing.List[str]],
        feature_ids: typing.Union[str, typing.List[str]] = "*",
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        read_request_timeout: typing.Optional[float] = None,
    ) -> pd.DataFrame

Reads feature values for given feature IDs of given entity IDs in this EntityType.

**Parameters**  
---  
**Name** | **Description**  
`entity_ids` |  `Union[str, List[str]]`   
Required. ID for a specific entity, or a list of IDs of entities to read Feature values of. The maximum number of IDs is 100 if a list.  
`feature_ids` |  `Union[str, List[str]]`   
Required. ID for a specific feature, or a list of IDs of Features in the EntityType for reading feature values. Default to "*", where value of all features will be read.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`read_request_timeout` |  `float`   
Optional. The timeout for the read request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`pd.DataFrame` | entities' feature values in DataFrame  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        request_metadata: typing.Sequence[typing.Tuple[str, str]] = (),
        update_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.featurestore._entity_type._EntityType

Updates an existing managed entityType resource.

Example Usage:
    
    
    my_entity_type = aiplatform.EntityType(
        entity_type_name='my_entity_type_id',
        featurestore_id='my_featurestore_id',
    )
    my_entity_type.update(
        description='update my description',
    )
    

**Parameters**  
---  
**Name** | **Description**  
`description` |  `str`   
Optional. Description of the EntityType.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your EntityTypes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Required. Strings which should be sent along with the request as metadata.  
`update_request_timeout` |  `float`   
Optional. The timeout for the update request in seconds.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

### write_feature_values
    
    
    write_feature_values(
        instances: typing.Union[
            typing.List[
                google.cloud.aiplatform_v1.types.featurestore_online_service.WriteFeatureValuesPayload
            ],
            typing.Dict[
                str,
                typing.Dict[
                    str,
                    typing.Union[
                        int,
                        str,
                        float,
                        bool,
                        bytes,
                        typing.List[int],
                        typing.List[str],
                        typing.List[float],
                        typing.List[bool],
                    ],
                ],
            ],
            pd.DataFrame,
        ],
        feature_time: typing.Union[str, datetime.datetime] = None,
    ) -> EntityType

Streaming ingestion. Write feature values directly to Feature Store.
    
    
    my_entity_type = aiplatform.EntityType(
        entity_type_name="my_entity_type_id",
        featurestore_id="my_featurestore_id",
    )
    
    # writing feature values from a pandas DataFrame without feature timestamp column.
    # In this case, current timestamp will be applied to all data.
    my_dataframe = pd.DataFrame(
        data = [
            {"entity_id": "movie_01", "average_rating": 4.9}
        ],
        columns=["entity_id", "average_rating"],
    )
    my_dataframe = my_df.set_index("entity_id")
    
    my_entity_type.write_feature_values(
        instances=my_df
    )
    
    # writing feature values from a pandas DataFrame with feature timestamp column
    # Example of datetime creation.
    feature_time = datetime.datetime(year=2022, month=1, day=1, hour=11, minute=59, second=59)
    or
    feature_time_str = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
    feature_time = datetime.datetime.strptime(feature_time_str, "%Y-%m-%d %H:%M:%S.%f")
    
    my_dataframe = pd.DataFrame(
        data = [
            {"entity_id": "movie_01", "average_rating": 4.9,
            "feature_timestamp": feature_time}
        ],
        columns=["entity_id", "average_rating", "feature_timestamp"],
    )
    
    my_dataframe = my_df.set_index("entity_id")
    my_entity_type.write_feature_values(
        instances=my_df, feature_time="feature_timestamp"
    )
    
    # writing feature values with a timestamp. The timestamp will be applied to the entire Dataframe.
    my_dataframe = pd.DataFrame(
        data = [
            {"entity_id": "movie_01", "average_rating": 4.9}
        ],
        columns=["entity_id", "average_rating"],
    )
    my_dataframe = my_df.set_index("entity_id")
    my_entity_type.write_feature_values(
        instances=my_df, feature_time=feature_time
    )
    
    # writing feature values from a Python dict without timestamp column.
    # In this case, current timestamp will be applied to all data.
    my_data_dict = {
            "movie_02" : {"average_rating": 3.7}
    }
    
    my_entity_type.write_feature_values(
        instances=my_data_dict
    )
    
    # writing feature values from a Python dict with timestamp column
    my_data_dict = {
            "movie_02" : {"average_rating": 3.7, "feature_timestamp": timestmap}}
    }
    
    my_entity_type.write_feature_values(
        instances=my_data_dict, feature_time="feature_timestamp"
    )
    
    # writing feature values from a Python dict and apply the same Feature_Timestamp
    my_data_dict = {
            "movie_02" : {"average_rating": 3.7}
    }
    
    my_entity_type.write_feature_values(
        instances=my_data_dict, feature_time=feature_time
    )
    
    # writing feature values from a list of WriteFeatureValuesPayload objects
    payloads = [
        gca_featurestore_online_service.WriteFeatureValuesPayload(
            entity_id="movie_03",
            feature_values={
                    "average_rating": featurestore_online_service.FeatureValue(
                            string_value="test",
                            metadata=featurestore_online_service.FeatureValue.Metadata(
                                    generate_time=timestmap
                            )
                   }
            }
        )
    ]
    # when instance is WriteFeatureValuesPayload,
    # feature_time param of write_feature_values() is ignored.
    my_entity_type.write_feature_values(
        instances=payloads
    )
    
    # reading back written feature values
    my_entity_type.read(
        entity_ids=["movie_01", "movie_02", "movie_03"]
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
