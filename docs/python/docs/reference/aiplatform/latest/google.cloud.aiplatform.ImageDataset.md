---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ImageDataset
title: Class ImageDataset (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:43.741214+00:00
---

# Class ImageDataset (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ImageDataset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImageDataset (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    ImageDataset(
        dataset_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

A managed image dataset resource for Vertex AI.

Use this class to work with a managed image dataset. To create a managed image dataset, you need a datasource file in CSV format and a schema file in YAML format. A schema is optional for a custom model. You put the CSV file and the schema into Cloud Storage buckets.

Use image data for the following objectives:

  * Single-label classification. For more information, see [Prepare image training data for single-label classification](https://cloud.google.com/vertex-ai/docs/image-data/classification/prepare-data#single-label-classification).
  * Multi-label classification. For more information, see [Prepare image training data for multi-label classification](https://cloud.google.com/vertex-ai/docs/image-data/classification/prepare-data#multi-label-classification).
  * Object detection. For more information, see [Prepare image training data for object detection](https://cloud.google.com/vertex-ai/docs/image-data/object-detection/prepare-data).



The following code shows you how to create an image dataset by importing data from a CSV datasource file and a YAML schema file. The schema file you use depends on whether your image dataset is used for single-label classification, multi-label classification, or object detection.
    
    
    my_dataset = aiplatform.ImageDataset.create(
        display_name="my-image-dataset",
        gcs_source=['gs://path/to/my/image-dataset.csv'],
        import_schema_uri=['gs://path/to/my/schema.yaml']
    )
    

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

### metadata_schema_uri

The metadata schema uri of this dataset resource.

### name

Name of this resource.

### resource_name

Full qualified resource name.

### update_time

Time this resource was last updated.

## Methods 

### ImageDataset
    
    
    ImageDataset(
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
        import_schema_uri: typing.Optional[str] = None,
        data_item_labels: typing.Optional[typing.Dict] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.datasets.image_dataset.ImageDataset

Creates a new image dataset.

Optionally imports data into the dataset when a source and `import_schema_uri` are passed in.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of the dataset. The name must contain 128 or fewer UTF-8 characters.  
`gcs_source` |  `Union[str, Sequence[str]]`   
Optional. The URI to one or more Google Cloud Storage buckets that contain your datasets. For example, `str: "gs://bucket/file.csv"` or `Sequence[str]: ["gs://bucket/file1.csv", "gs://bucket/file2.csv"]`.  
`import_schema_uri` |  `str`   
Optional. A URI for a YAML file stored in Cloud Storage that describes the import schema used to validate the dataset. The schema is an [OpenAPI 3.0.2 Schema](https://tinyurl.com/y538mdwt) object.  
`data_item_labels` |  `Dict`   
Optional. A dictionary of label information. Each dictionary item contains a label and a label key. Each image in the dataset includes one dictionary of label information. If a data item is added or merged into a dataset, and that data item contains an image that's identical to an image that’s already in the dataset, then the data items are merged. If two identical labels are detected during the merge, each with a different label key, then one of the label and label key dictionary items is randomly chosen to be into the merged data item. Images and documents are compared using their binary data (bytes), not on their content. If annotation labels are referenced in a schema specified by the `import_schema_url` parameter, then the labels in the `data_item_labels` dictionary are overriden by the annotations.  
`project` |  `str`   
Optional. The name of the Google Cloud project to which this `ImageDataset` is uploaded. This overrides the project that was set by `aiplatform.init`.  
`location` |  `str`   
Optional. The Google Cloud region where this dataset is uploaded. This region overrides the region that was set by `aiplatform.init`.  
`credentials` |  `auth_credentials.Credentials`   
Optional. The credentials that are used to upload the `ImageDataset`. These credentials override the credentials set by `aiplatform.init`.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings that contain metadata that's sent with the request.  
`labels` |  `Dict[str, str]`   
Optional. Labels with user-defined metadata to organize your Vertex AI Tensorboards. The maximum length of a key and of a value is 64 unicode characters. Labels and keys can contain only lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (system labels are excluded). For more information and examples of using labels, see [Using labels to organize Google Cloud Platform resources](https://goo.gl/xmQnxf). System reserved label keys are prefixed with `aiplatform.googleapis.com/` and are immutable.  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key that's used to protect the dataset. The format of the key is `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If `encryption_spec_key_name` is set, this image dataset and all of its sub-resources are secured by this key. This `encryption_spec_key_name` overrides the `encryption_spec_key_name` set by `aiplatform.init`.  
`sync` |  `bool`   
If `true`, the `create` method creates an image dataset synchronously. If `false`, the `create` method creates an image dataset asynchronously.  
`create_request_timeout` |  `float`   
Optional. The number of seconds for the timeout of the create request.  
**Returns**  
---  
**Type** | **Description**  
`image_dataset (ImageDataset)` | An instantiated representation of the managed `ImageDataset` resource.  
  
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
    
    
    import_data(
        gcs_source: typing.Union[str, typing.Sequence[str]],
        import_schema_uri: str,
        data_item_labels: typing.Optional[typing.Dict] = None,
        sync: bool = True,
        import_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.datasets.dataset._Dataset

Upload data to existing managed dataset.

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
