---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MoveTableToDatabaseRequest
title: Google Cloud Dataproc Metastore V1beta Client - Class MoveTableToDatabaseRequest (1.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:12.106111+00:00
---

# Google Cloud Dataproc Metastore V1beta Client - Class MoveTableToDatabaseRequest (1.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MoveTableToDatabaseRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc Metastore V1beta Client - Class MoveTableToDatabaseRequest (1.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.4  1.1.1  1.0.4  0.11.5  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.1  0.4.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataproc Metastore V1beta Client class MoveTableToDatabaseRequest.

Request message for [DataprocMetastore.MoveTableToDatabase](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1beta_Client_DataprocMetastoreClient__moveTableToDatabase__).

Generated from protobuf message `google.cloud.metastore.v1beta.MoveTableToDatabaseRequest`

## Namespace

Google \ Cloud \ Metastore \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ service` |  `string`   
Required. The relative resource name of the metastore service to mutate metadata, in the following format: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`↳ table_name` |  `string`   
Required. The name of the table to be moved.  
`↳ db_name` |  `string`   
Required. The name of the database where the table resides.  
`↳ destination_db_name` |  `string`   
Required. The name of the database where the table should be moved.  
  
### getService

Required. The relative resource name of the metastore service to mutate metadata, in the following format: `projects/{project_id}/locations/{location_id}/services/{service_id}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setService

Required. The relative resource name of the metastore service to mutate metadata, in the following format: `projects/{project_id}/locations/{location_id}/services/{service_id}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTableName

Required. The name of the table to be moved.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTableName

Required. The name of the table to be moved.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDbName

Required. The name of the database where the table resides.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDbName

Required. The name of the database where the table resides.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDestinationDbName

Required. The name of the database where the table should be moved.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDestinationDbName

Required. The name of the database where the table should be moved.

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

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
