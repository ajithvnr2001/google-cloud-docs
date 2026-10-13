---
url: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset
title: Module dataset (3.46.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:04.825855+00:00
---

# Module dataset (3.46.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module dataset (3.46.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.46.1 (latest)  3.46.0  3.45.2  3.44.0  3.43.0  3.42.3  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.31.0  3.30.0  3.29.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.1  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.2  3.16.0  3.15.0  3.14.1  3.13.0  3.12.0  3.11.4  3.4.0  3.3.6  3.2.0  3.1.0  3.0.1  2.34.4  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.27.1  2.26.0  2.25.2  2.24.1  2.23.3  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.0  1.28.2  1.27.2  1.26.1  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0 

Define API Datasets.

## Classes 

### [AccessEntry](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry)
    
    
    AccessEntry(
        role: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        entity_id: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = None,
        **kwargs
    )

Represents grant of an access role to an entity.

An entry must have exactly one of the allowed xref_EntityTypes. If anything but `view`, `routine`, or `dataset` are set, a `role` is also required. `role` is omitted for `view`, `routine`, `dataset`, because they are always read-only.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets>.

**Parameters**  
---  
**Name** | **Description**  
`role` |  `typing.Optional[str]`   
Role granted to the entity. The following string values are supported: `'READER'`, `'WRITER'`, `'OWNER'`. It may also be :data:`None` if the `entity_type` is `view`, `routine`, or `dataset`.  
`entity_type` |  `typing.Optional[str]`   
Type of entity being granted the role. See [EntityTypes](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.EntityTypes) for supported types.  
`entity_id` |  `typing.Union[typing.Dict[str, typing.Any], str, NoneType]`   
If the `entity_type` is not 'view', 'routine', or 'dataset', the `entity_id` is the `str` ID of the entity being granted the role. If the `entity_type` is 'view' or 'routine', the `entity_id` is a `dict` representing the view or routine from a different dataset to grant access to in the following format for views:: { 'projectId': string, 'datasetId': string, 'tableId': string } For routines:: { 'projectId': string, 'datasetId': string, 'routineId': string } If the `entity_type` is 'dataset', the `entity_id` is a `dict` that includes a 'dataset' field with a `dict` representing the dataset and a 'target_types' field with a `str` value of the dataset's resource type:: { 'dataset': { 'projectId': string, 'datasetId': string, }, 'target_types: 'VIEWS' }  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If a `view`, `routine`, or `dataset` has `role` set, or a non `view`, non `routine`, and non `dataset` **does not** have a `role` set. .. rubric:: Examples >>> entry = AccessEntry('OWNER', 'userByEmail', 'user@example.com') >>> view = { ... 'projectId': 'my-project', ... 'datasetId': 'my_dataset', ... 'tableId': 'my_table' ... } >>> entry = AccessEntry(None, 'view', view)  
  
### [Condition](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Condition)
    
    
    Condition(
        expression: str,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
    )

Represents a textual expression in the Common Expression Language (CEL) syntax.

Typically used for filtering or policy rules, such as in IAM Conditions or BigQuery row/column access policies.

See: <https://cloud.google.com/iam/docs/reference/rest/Shared.Types/Expr> <https://github.com/google/cel-spec>

**Parameters**  
---  
**Name** | **Description**  
`expression` |  `str`   
The condition expression string using CEL syntax. This is required. Example: `resource.type == "compute.googleapis.com/Instance"`  
`title` |  `Optional[str]`   
An optional title for the condition, providing a short summary. Example: `"Request is for a GCE instance"`  
`description` |  `Optional[str]`   
An optional description of the condition, providing a detailed explanation. Example: `"This condition checks whether the resource is a GCE instance."`  
  
### [Dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset)
    
    
    Dataset(dataset_ref)

Datasets are containers for tables.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets#resource-dataset>

**Parameter**  
---  
**Name** | **Description**  
`dataset_ref` |  `Union[[google.cloud.bigquery.dataset.DatasetReference](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.DatasetReference), str] .. note:: Fields marked as "Output Only" are populated by the server and will only be available after calling [get_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client).`   
A pointer to a dataset. If `dataset_ref` is a string, it must include both the project ID and the dataset ID, separated by `.`.  
  
### [DatasetListItem](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.DatasetListItem)
    
    
    DatasetListItem(resource)

A read-only dataset resource from a list operation.

For performance reasons, the BigQuery API only includes some of the dataset properties when listing datasets. Notably, xref_access_entries is missing.

For a full list of the properties that the BigQuery API returns, see the `REST documentation for datasets.list <https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets/list>`_.

**Parameter**  
---  
**Name** | **Description**  
`resource` |  `Dict[str, str]`   
A dataset-like resource object from a dataset list response. A `datasetReference` property is required.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `datasetReference` or one of its required members is missing from `resource`.  
  
### [DatasetReference](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.DatasetReference)
    
    
    DatasetReference(project: str, dataset_id: str)

DatasetReferences are pointers to datasets.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets#datasetreference>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `str`   
The ID of the project  
`dataset_id` |  `str`   
The ID of the dataset  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If either argument is not of type `str`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
