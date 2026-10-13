---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Model/
title: BigQuery Client - Class Model (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:48.090007+00:00
---

# BigQuery Client - Class Model (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class Model (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class Model.

A [BigQuery ML](https://cloud.google.com/bigquery-ml/docs/) Model represents what an ML system has learned from the training data.

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
The model's ID.  
`datasetId` |  `string`   
The dataset's ID.  
`projectId` |  `string`   
The project's ID.  
`info` |  `array`   
[optional] The model data.  
`location` |  `array`   
[optional] The location of the model.  
  
### info

See also:

  * [Model resource documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/models)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### reload

See also:

  * [Models get API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/models/get)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### id

Retrieves the model's ID.

Example:
    
    
     echo $model->id();
    

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### identity

Retrieves the model's identity.

An identity provides a description of a resource that is nested in nature.

Example:
    
    
    echo $model->identity()['modelId'];
    

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### delete

See also:

  * [Models delete API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/models/delete)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
  
### exists

Check whether or not the model exists.

Example:
    
    
    echo $model->exists();
    

**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### update

See also:

  * [Model's patch API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/models/patch)
  * [Patch (Partial Update)](https://cloud.google.com/bigquery/docs/api-performance#patch)



**Parameters**  
---  
**Name** | **Description**  
`metadata` |  `array`   
The available options for metadata are outlined at the [Model Resource API docs](https://cloud.google.com/bigquery/docs/reference/rest/v2/models)  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### extract

See also:

  * [Jobs insert API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert)



**Parameters**  
---  
**Name** | **Description**  
`destination` |  `string|Google\Cloud\Storage\StorageObject`   
The destination object. May be a Google\Cloud\Storage\StorageObject or a URI pointing to a Google Cloud Storage object in the format of `gs://{bucket-name}/{object-name}`.  
`options` |  `array`   
[optional] Please see the [upstream API documentation for Job configuration](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job) for the available options.  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
