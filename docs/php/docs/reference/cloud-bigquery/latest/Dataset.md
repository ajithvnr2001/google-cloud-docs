---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Dataset/
title: BigQuery Client - Class Dataset (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:47.149474+00:00
---

# BigQuery Client - Class Dataset (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Dataset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class Dataset (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class Dataset.

[Datasets](https://cloud.google.com/bigquery/docs/datasets-intro) allow you to organize and control access to your tables.

## Namespace

Google \ Cloud \ BigQuery

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `Connection\ConnectionInterface`   
Represents a connection to BigQuery. This object is created by BigQueryClient, and should not be instantiated outside of this client.  
`id` |  `string`   
The dataset's ID.  
`projectId` |  `string`   
The project's ID.  
`mapper` |  `[ValueMapper](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ValueMapper)`   
  
`info` |  `array`   
[optional] The dataset's metadata.  
`location` |  `string|null`   
[optional] A default geographic location, used when no dataset metadata exists.  
  
### exists

Check whether or not the dataset exists.

Example:
    
    
    echo $dataset->exists();
    

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### delete

See also:

  * [Datasets delete API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets/delete)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ deleteContents` |  `bool`   
If true, delete all the tables in the dataset. If false and the dataset contains tables, the request will fail. **Defaults to** `false`.  
  
### update

See also:

  * [Datasets patch API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets/patch)
  * [Patch (Partial Update)](https://cloud.google.com/bigquery/docs/api-performance#patch)



**Parameters**  
---  
**Name** | **Description**  
`metadata` |  `array`   
The available options for metadata are outlined at the [Dataset Resource API docs](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)  
`options` |  `array`   
Configuration options.  
`↳ accessPolicyVersion` |  `int`   
Optional. Access policy schema version. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for conditional access policy binding in datasets must specify version 3. Dataset with no conditional role bindings in access policy may specify any valid value or leave the field unset. This field will be mapped to [IAM Policy version](https://cloud.google.com/iam/docs/policies#versions) and will be used to fetch policy from IAM. If unset or if 0 or 1 value is used for dataset with conditional bindings, access entry with condition will have role string appended by 'withcond' string followed by a hash value. For example : { "access": [ { "role": "roles/bigquery.dataViewer_with_conditionalbinding_7a34awqsda", "userByEmail": "user@example.com", } ] } Please refer <https://cloud.google.com/iam/docs/troubleshooting-withcond> for more details.  
`↳ updateMode` |  `string`   
Optional. Specifies the fields of dataset that update/patch operation is targeting. Acceptable values include "UPDATE_MODE_UNSPECIFIED", "UPDATE_METADATA", "UPDATE_ACL", "UPDATE_FULL". By default, both metadata and ACL fields are updated.  
  
### table

Lazily instantiates a table.

There are no network requests made at this point. To see the operations that can be performed on a dataset please see [Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table).

Example:
    
    
    $table = $dataset->table('myTableId');
    

**Parameter**  
---  
**Name** | **Description**  
`id` |  `string`   
The id of the table to request.  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)` |   
  
### tables

See also:

  * [Tables list API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/list)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ maxResults` |  `int`   
Maximum number of results to return per page.  
`↳ resultLimit` |  `int`   
Limit the number of results returned in total. **Defaults to** `0` (return all results).  
`↳ pageToken` |  `string`   
A previously-returned page token used to resume the loading of results from a specific point.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)<[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)>` |   
  
### createTable

See also:

  * [Tables insert API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/insert)



**Parameters**  
---  
**Name** | **Description**  
`id` |  `mixed`   
  
`options` |  `array`   
Configuration options.  
`↳ metadata` |  `array`   
The available options for metadata are outlined at the [Table Resource API docs](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)` |   
  
### model

Lazily instantiates a machine learning model in the dataset.

There are no network requests made at this point. To see the operations that can be performed on a model, please see [Model](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Model).

Example:
    
    
    $model = $dataset->model('my_model');
    echo $model->id();
    

**Parameters**  
---  
**Name** | **Description**  
`id` |  `string`   
The model's ID.  
`info` |  `array`   
[optional] The model resource data.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Model)` |   
  
### models

See also:

  * [Models list API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/models/list)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ maxResults` |  `int`   
Maximum number of results to return per page.  
`↳ resultLimit` |  `int`   
Limit the number of results returned in total. **Defaults to** `0` (return all results).  
`↳ pageToken` |  `string`   
A previously-returned page token used to resume the loading of results from a specific point.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)<[Model](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Model)>` |   
  
### routine

Lazily instantiates a routine.

There are no network requests made at this point. To see the operations that can be performed on a routine, please see [Routine](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Routine).

Example:
    
    
    $routine = $dataset->routine('my_routine');
    echo $routine->identity()['routineId'];
    

**Parameters**  
---  
**Name** | **Description**  
`id` |  `string`   
The routine's ID.  
`info` |  `array`   
[optional] The routine resource data.  
**Returns**  
---  
**Type** | **Description**  
`[Routine](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Routine)` |   
  
### routines

See also:

  * [List Routines API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines/list)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ maxResults` |  `int`   
Maximum number of results to return per page.  
`↳ resultLimit` |  `int`   
Limit the number of results returned in total. **Defaults to** `0` (return all results).  
`↳ pageToken` |  `string`   
A previously-returned page token used to resume the loading of results from a specific point.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)<[Model](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Model)>` |   
  
### createRoutine

See also:

  * [Insert Routines API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines/insert)



**Parameters**  
---  
**Name** | **Description**  
`id` |  `string`   
The routine ID.  
`metadata` |  `array`   
The available options for metadata are outlined at the [Routine Resource API docs](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines). Omit `routineReference` as it is computed and appended by the client.  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`[Routine](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Routine)` |   
  
### info

See also:

  * [Datasets resource documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ accessPolicyVersion` |  `int`   
Optional. Access policy schema version. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for conditional access policy binding in datasets must specify version 3. Dataset with no conditional role bindings in access policy may specify any valid value or leave the field unset. This field will be mapped to [IAM Policy version](https://cloud.google.com/iam/docs/policies#versions) and will be used to fetch policy from IAM. If unset or if 0 or 1 value is used for dataset with conditional bindings, access entry with condition will have role string appended by 'withcond' string followed by a hash value. For example : { "access": [ { "role": "roles/bigquery.dataViewer_with_conditionalbinding_7a34awqsda", "userByEmail": "user@example.com", } ] } Please refer <https://cloud.google.com/iam/docs/troubleshooting-withcond> for more details.  
`↳ datasetView` |  `string`   
Optional. Specifies the view that determines which dataset information is returned. Acceptable values include "DATASET_VIEW_UNSPECIFIED", "METADATA", "ACL", "FULL". By default, metadata and ACL information are returned.  
  
### reload

See also:

  * [Datasets get API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets/get)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ accessPolicyVersion` |  `int`   
Optional. Access policy schema version. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for conditional access policy binding in datasets must specify version 3. Dataset with no conditional role bindings in access policy may specify any valid value or leave the field unset. This field will be mapped to [IAM Policy version](https://cloud.google.com/iam/docs/policies#versions) and will be used to fetch policy from IAM. If unset or if 0 or 1 value is used for dataset with conditional bindings, access entry with condition will have role string appended by 'withcond' string followed by a hash value. For example : { "access": [ { "role": "roles/bigquery.dataViewer_with_conditionalbinding_7a34awqsda", "userByEmail": "user@example.com", } ] } Please refer <https://cloud.google.com/iam/docs/troubleshooting-withcond> for more details.  
`↳ datasetView` |  `string`   
Optional. Specifies the view that determines which dataset information is returned. Acceptable values include "DATASET_VIEW_UNSPECIFIED", "METADATA", "ACL", "FULL". By default, metadata and ACL information are returned.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### id

Retrieves the dataset's ID.

Example:
    
    
    echo $dataset->id();
    

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### identity

Retrieves the dataset's identity.

An identity provides a description of a resource that is nested in nature.

Example:
    
    
    echo $dataset->identity()['projectId'];
    

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
