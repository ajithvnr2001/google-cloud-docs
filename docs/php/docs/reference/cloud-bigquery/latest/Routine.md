---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Routine/
title: BigQuery Client - Class Routine (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:48.538023+00:00
---

# BigQuery Client - Class Routine (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Routine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class Routine (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class Routine.

[Routines](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines) are used-defined functions or stored procedures.

Example:
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    $bigquery = new BigQueryClient();
    $dataset = $bigquery->dataset('my_dataset');
    $routine = $dataset->routine('my_routine');
    

## Namespace

Google \ Cloud \ BigQuery

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `Connection\ConnectionInterface`   
A connection to the BigQuery API. This object is created by BigQueryClient, and should not be instantiated outside of this client.  
`id` |  `string`   
The routine ID.  
`datasetId` |  `string`   
The dataset ID.  
`projectId` |  `string`   
The project ID.  
`info` |  `array`   
[optional] An optional representation of the routine resource.  
  
### identity

Get the routine identity.

An identity provides a description of a nested resource.

Example:
    
    
    $identity = $routine->identity();
    echo $identity['routineId'];
    

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### info

See also:

  * [Get Routines API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines/get)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### reload

See also:

  * [Get Routines API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines/get)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### exists

See also:

  * [Get Routines API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines/get)



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

  * [Update Routines API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines/update)



**Parameters**  
---  
**Name** | **Description**  
`metadata` |  `array`   
The full routine resource with desired modifications.  
`options` |  `array`   
Configuration options  
`↳ updateMask` |  `array`   
A list of field paths to be modified. Nested key names should be dot-separated, e.g. `returnType.typeKind`. Google Cloud PHP will attempt to infer this value on your behalf. You may use this field to limit which parts of the resource are updated, should you choose to provide the full resource as the `$metadata` argument.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### delete

See also:

  * [Delete Routines API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines/delete)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
