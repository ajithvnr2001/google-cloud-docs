---
url: https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.BigQueryDestination
title: Google Cloud Capacity Planner V1beta Client - Class BigQueryDestination (0.2.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:09.407485+00:00
---

# Google Cloud Capacity Planner V1beta Client - Class BigQueryDestination (0.2.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.BigQueryDestination

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Capacity Planner V1beta Client - Class BigQueryDestination (0.2.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.4 (latest)  0.1.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Capacity Planner V1beta Client class BigQueryDestination.

A BigQuery destination for exporting assets to.

Generated from protobuf message `google.cloud.capacityplanner.v1beta.BigQueryDestination`

## Namespace

Google \ Cloud \ CapacityPlanner \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ dataset` |  `string`   
Required. The BigQuery dataset in format "projects/{projectId}/datasets/{datasetId}", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error.  
`↳ table` |  `string`   
Required. The BigQuery table to which the snapshot result should be written.  
`↳ partition_key` |  `int`   
Optional. The partition key for BigQuery partitioned table.  
`↳ write_disposition` |  `int`   
Optional. Specifies the action that occurs if the destination table or partition already exists.  
`↳ create_disposition` |  `int`   
Optional. Specifies the action that occurs if the destination table does not exist  
`↳ gcs_location` |  `string`   
Optional. Specifies the Cloud Storage location. Users can choose to provide a location for Cloud Storage bucket to store the exported data. (as it is possible that some locations are restricted via org policy for that project) Temporary Cloud Storage bucket creation is an interim step for BigQuery upload. If no value is provided, the default location used will be 'US'.  
  
### getDataset

Required. The BigQuery dataset in format "projects/{projectId}/datasets/{datasetId}", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDataset

Required. The BigQuery dataset in format "projects/{projectId}/datasets/{datasetId}", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTable

Required. The BigQuery table to which the snapshot result should be written.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTable

Required. The BigQuery table to which the snapshot result should be written.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPartitionKey

Optional. The partition key for BigQuery partitioned table.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [PartitionKey](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.BigQueryDestination.PartitionKey).  
  
### setPartitionKey

Optional. The partition key for BigQuery partitioned table.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [PartitionKey](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.BigQueryDestination.PartitionKey).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getWriteDisposition

Optional. Specifies the action that occurs if the destination table or partition already exists.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [WriteDisposition](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.BigQueryDestination.WriteDisposition).  
  
### setWriteDisposition

Optional. Specifies the action that occurs if the destination table or partition already exists.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [WriteDisposition](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.BigQueryDestination.WriteDisposition).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateDisposition

Optional. Specifies the action that occurs if the destination table does not exist

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [CreateDisposition](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.BigQueryDestination.CreateDisposition).  
  
### setCreateDisposition

Optional. Specifies the action that occurs if the destination table does not exist

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [CreateDisposition](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.BigQueryDestination.CreateDisposition).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGcsLocation

Optional. Specifies the Cloud Storage location.

Users can choose to provide a location for Cloud Storage bucket to store the exported data. (as it is possible that some locations are restricted via org policy for that project) Temporary Cloud Storage bucket creation is an interim step for BigQuery upload. If no value is provided, the default location used will be 'US'.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setGcsLocation

Optional. Specifies the Cloud Storage location.

Users can choose to provide a location for Cloud Storage bucket to store the exported data. (as it is possible that some locations are restricted via org policy for that project) Temporary Cloud Storage bucket creation is an interim step for BigQuery upload. If no value is provided, the default location used will be 'US'.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
