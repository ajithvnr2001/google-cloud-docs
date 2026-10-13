---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TabularDataset
title: Class TabularDataset (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:53.457415+00:00
---

# Class TabularDataset (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TabularDataset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TabularDataset (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    TabularDataset(
        dataset_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

A managed tabular dataset resource for Vertex AI.

Use this class to work with tabular datasets. You can use a CSV file, BigQuery, or a pandas [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) to create a tabular dataset. For more information about paging through BigQuery data, see [Read data with BigQuery API using pagination](https://cloud.google.com/bigquery/docs/paging-results). For more information about tabular data, see [Tabular data](https://cloud.google.com/vertex-ai/docs/training-overview#tabular_data).

The following code shows you how to create and import a tabular dataset with a CSV file.
    
    
    my_dataset = aiplatform.TabularDataset.create(
        display_name="my-dataset", gcs_source=['gs://path/to/my/dataset.csv'])
    

Contrary to unstructured datasets, creating and importing a tabular dataset can only be done in a single step.

If you create a tabular dataset with a pandas [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), you need to use a BigQuery table to stage the data for Vertex AI:
    
    
    my_dataset = aiplatform.TabularDataset.create_from_dataframe(
        df_source=my_pandas_dataframe,
        staging_path=f"bq://{bq_dataset_id}.table-unique"
    )
    

## Properties 

### column_names

Retrieve the columns for the dataset by extracting it from the Google Cloud Storage or Google BigQuery source.

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | When no valid source is found.  
  
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

### metadata_schema_uri

The metadata schema uri of this dataset resource.

### name

Name of this resource.

### resource_name

Full qualified resource name.

### update_time

Time this resource was last updated.

## Methods 

### TabularDataset
    
    
    TabularDataset(
        dataset_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves an existing managed dataset given a dataset name or ID.

**Parameters**  
---  
**Name** | **Description**  
`dataset_name` |  `str`   
Required. A fully-qualified dataset resource name or dataset ID. Example: "projects/123/locations/us-central1/datasets/456" or "456" when project and location are initialized or passed.  
`project` |  `str`   
Optional project to retrieve dataset from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional location to retrieve dataset from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Custom credentials to use to retrieve this Dataset. Overrides credentials set in aiplatform.init.  
  
### create
    
    
    create(
        display_name: typing.Optional[str] = None,
        gcs_source: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        bq_source: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.datasets.tabular_dataset.TabularDataset

Creates a tabular dataset.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of the dataset. The name must contain 128 or fewer UTF-8 characters.  
`gcs_source` |  `Union[str, Sequence[str]]`   
Optional. The URI to one or more Google Cloud Storage buckets that contain your datasets. For example, `str: "gs://bucket/file.csv"` or `Sequence[str]: ["gs://bucket/file1.csv", "gs://bucket/file2.csv"]`. Either `gcs_source` or `bq_source` must be specified.  
`bq_source` |  `str`   
Optional. The URI to a BigQuery table that's used as an input source. For example, `bq://project.dataset.table_name`. Either `gcs_source` or `bq_source` must be specified.  
`project` |  `str`   
Optional. The name of the Google Cloud project to which this `TabularDataset` is uploaded. This overrides the project that was set by `aiplatform.init`.  
`location` |  `str`   
Optional. The Google Cloud region where this dataset is uploaded. This region overrides the region that was set by `aiplatform.init`.  
`credentials` |  `auth_credentials.Credentials`   
Optional. The credentials that are used to upload the `TabularDataset`. These credentials override the credentials set by `aiplatform.init`.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings that contain metadata that's sent with the request.  
`labels` |  `Dict[str, str]`   
Optional. Labels with user-defined metadata to organize your Vertex AI Tensorboards. The maximum length of a key and of a value is 64 unicode characters. Labels and keys can contain only lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (system labels are excluded). For more information and examples of using labels, see [Using labels to organize Google Cloud Platform resources](https://goo.gl/xmQnxf). System reserved label keys are prefixed with `aiplatform.googleapis.com/` and are immutable.  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key that's used to protect the dataset. The format of the key is `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If `encryption_spec_key_name` is set, this `TabularDataset` and all of its sub-resources are secured by this key. This `encryption_spec_key_name` overrides the `encryption_spec_key_name` set by `aiplatform.init`.  
`sync` |  `bool`   
If `true`, the `create` method creates a tabular dataset synchronously. If `false`, the `create` method creates a tabular dataset asynchronously.  
`create_request_timeout` |  `float`   
Optional. The number of seconds for the timeout of the create request.  
**Returns**  
---  
**Type** | **Description**  
`tabular_dataset (TabularDataset)` | An instantiated representation of the managed `TabularDataset` resource.  
  
### create_from_dataframe
    
    
    create_from_dataframe(
        df_source: pd.DataFrame,
        staging_path: str,
        bq_schema: typing.Optional[typing.Union[str, bigquery.SchemaField]] = None,
        display_name: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> TabularDataset

Creates a new tabular dataset from a pandas `DataFrame`.

**Parameters**  
---  
**Name** | **Description**  
`df_source` |  `pd.DataFrame`   
Required. A pandas [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) containing the source data for ingestion as a `TabularDataset`. This method uses the data types from the provided `DataFrame` when the `TabularDataset` is created.  
`staging_path` |  `str`   
Required. The BigQuery table used to stage the data for Vertex AI. Because Vertex AI maintains a reference to this source to create the `TabularDataset`, you shouldn't delete this BigQuery table. For example: `bq://my-project.my-dataset.my-table`. If the specified BigQuery table doesn't exist, then the table is created for you. If the provided BigQuery table already exists, and the schemas of the BigQuery table and your DataFrame match, then the data in your local `DataFrame` is appended to the table. The location of the BigQuery table must conform to the [BigQuery location requirements](https://cloud.google.com/vertex-ai/docs/general/locations#bq-locations).  
`bq_schema` |  `Optional[Union[str, bigquery.SchemaField]]`   
Optional. If not set, BigQuery autodetects the schema using the column types of your `DataFrame`. If set, BigQuery uses the schema you provide when the staging table is created. For more information, see the BigQuery [`LoadJobConfig.schema`](https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.LoadJobConfig#google_cloud_bigquery_job_LoadJobConfig_schema) property.  
`display_name` |  `str`   
Optional. The user-defined name of the `Dataset`. The name must contain 128 or fewer UTF-8 characters.  
`project` |  `str`   
Optional. The project to upload this dataset to. This overrides the project set using `aiplatform.init`.  
`location` |  `str`   
Optional. The location to upload this dataset to. This overrides the location set using `aiplatform.init`.  
`credentials` |  `auth_credentials.Credentials`   
Optional. The custom credentials used to upload this dataset. This overrides credentials set using `aiplatform.init`.  
**Returns**  
---  
**Type** | **Description**  
`tabular_dataset (TabularDataset)` | An instantiated representation of the managed `TabularDataset` resource.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### export_data
    
    
    export_data(output_dir: str) -> typing.Sequence[str]

Exports data to output dir to GCS.

**Parameter**  
---  
**Name** | **Description**  
`output_dir` |  `str`   
Required. The Google Cloud Storage location where the output is to be written to. In the given directory a new directory will be created with name: `export-data-` where timestamp is in YYYYMMDDHHMMSS format. All export output will be written into that directory. Inside that directory, annotations with the same schema will be grouped into sub directories which are named with the corresponding annotations' schema title. Inside these sub directories, a schema.yaml will be created to describe the output format. If the uri doesn't end with '/', a '/' will be automatically appended. The directory is created if it doesn't exist.  
**Returns**  
---  
**Type** | **Description**  
`exported_files (Sequence[str])` | All of the files that are exported in this export operation.  
  
### export_data_for_custom_training
    
    
    export_data_for_custom_training(
        output_dir: str,
        annotation_filter: typing.Optional[str] = None,
        saved_query_id: typing.Optional[str] = None,
        annotation_schema_uri: typing.Optional[str] = None,
        split: typing.Optional[
            typing.Union[typing.Dict[str, str], typing.Dict[str, float]]
        ] = None,
    ) -> typing.Dict[str, typing.Any]

Exports data to output dir to GCS for custom training use case.

Example annotation_schema_uri (image classification): gs://google-cloud-aiplatform/schema/dataset/annotation/image_classification_1.0.0.yaml

Example split (filter split): { "training_filter": "labels.aiplatform.googleapis.com/ml_use=training", "validation_filter": "labels.aiplatform.googleapis.com/ml_use=validation", "test_filter": "labels.aiplatform.googleapis.com/ml_use=test", } Example split (fraction split): { "training_fraction": 0.7, "validation_fraction": 0.2, "test_fraction": 0.1, }

**Parameters**  
---  
**Name** | **Description**  
`output_dir` |  `str`   
Required. The Google Cloud Storage location where the output is to be written to. In the given directory a new directory will be created with name: `export-data-` where timestamp is in YYYYMMDDHHMMSS format. All export output will be written into that directory. Inside that directory, annotations with the same schema will be grouped into sub directories which are named with the corresponding annotations' schema title. Inside these sub directories, a schema.yaml will be created to describe the output format. If the uri doesn't end with '/', a '/' will be automatically appended. The directory is created if it doesn't exist.  
`annotation_filter` |  `str`   
Optional. An expression for filtering what part of the Dataset is to be exported. Only Annotations that match this filter will be exported. The filter syntax is the same as in `ListAnnotations][DatasetService.ListAnnotations]`.  
`saved_query_id` |  `str`   
Optional. The ID of a SavedQuery (annotation set) under this Dataset used for filtering Annotations for training. Only used for custom training data export use cases. Only applicable to Datasets that have SavedQueries. Only Annotations that are associated with this SavedQuery are used in respectively training. When used in conjunction with annotations_filter, the Annotations used for training are filtered by both saved_query_id and annotations_filter. Only one of saved_query_id and annotation_schema_uri should be specified as both of them represent the same thing: problem type.  
`annotation_schema_uri` |  `str`   
Optional. The Cloud Storage URI that points to a YAML file describing the annotation schema. The schema is defined as an OpenAPI 3.0.2 Schema Object. The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/, note that the chosen schema must be consistent with metadata_schema_uri of this Dataset. Only used for custom training data export use cases. Only applicable if this Dataset that have DataItems and Annotations. Only Annotations that both match this schema and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on. When used in conjunction with annotations_filter, the Annotations used for training are filtered by both annotations_filter and annotation_schema_uri.  
`split` |  `Union[Dict[str, str], Dict[str, float]]`   
The instructions how the export data should be split between the training, validation and test sets.  
**Returns**  
---  
**Type** | **Description**  
`export_data_response (Dict)` | Response message for DatasetService.ExportData in Dictionary format.  
  
### import_data
    
    
    import_data()

Upload data to existing managed dataset.

**Parameters**  
---  
**Name** | **Description**  
`gcs_source` |  `Union[str, Sequence[str]]`   
Required. Google Cloud Storage URI(-s) to the input file(s). May contain wildcards. For more information on wildcards, see <https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames>. .. rubric:: Examples str: "gs://bucket/file.csv" Sequence[str]: ["gs://bucket/file1.csv", "gs://bucket/file2.csv"]  
`import_schema_uri` |  `str`   
Required. Points to a YAML file stored on Google Cloud Storage describing the import format. Validation will be done against the schema. The schema is defined as an `OpenAPI 3.0.2 Schema Object <https://tinyurl.com/y538mdwt>`__.  
`data_item_labels` |  `Dict`   
Labels that will be applied to newly imported DataItems. If an identical DataItem as one being imported already exists in the Dataset, then these labels will be appended to these of the already existing one, and if labels with identical key is imported before, the old label value will be overwritten. If two DataItems are identical in the same import data operation, the labels will be combined and if key collision happens in this case, one of the values will be picked randomly. Two DataItems are considered identical if their content bytes are identical (e.g. image bytes or pdf bytes). These labels will be overridden by Annotation labels specified inside index file referenced by `import_schema_uri`, e.g. jsonl file. This arg is not for specifying the annotation name or the training target of your data, but for some global labels of the dataset. E.g., 'data_item_labels={"aiplatform.googleapis.com/ml_use":"training"}' specifies that all the uploaded data are used for training.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`import_request_timeout` |  `float`   
Optional. The timeout for the import request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`dataset (Dataset)` | Instantiated representation of the managed dataset resource.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Dataset resource.

Example Usage:

aiplatform.TabularDataset.list( filter='labels.my_key="my_value"', order_by='display_name' )

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
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        *,
        display_name: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        description: typing.Optional[str] = None,
        update_request_timeout: typing.Optional[float] = None
    ) -> google.cloud.aiplatform.datasets.dataset._Dataset

Update the dataset. Updatable fields:

  * `display_name`
  * `description`
  * `labels`



**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of the Dataset. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`labels` |  `Dict[str, str]`   
Optional. Labels with user-defined metadata to organize your Tensorboards. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded). See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`description` |  `str`   
Optional. The description of the Dataset.  
`update_request_timeout` |  `float`   
Optional. The timeout for the update request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`dataset (Dataset)` | Updated dataset.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
