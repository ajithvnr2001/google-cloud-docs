---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableRequest
title: Cloud Bigtable V2 Client - Class CreateTableRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:40.274346+00:00
---

# Cloud Bigtable V2 Client - Class CreateTableRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class CreateTableRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class CreateTableRequest.

Request message for [google.bigtable.admin.v2.BigtableTableAdmin.CreateTable](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createTable__)

Generated from protobuf message `google.bigtable.admin.v2.CreateTableRequest`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The unique name of the instance in which to create the table. Values are of the form `projects/{project}/instances/{instance}`.  
`↳ table_id` |  `string`   
Required. The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`. Maximum 50 characters.  
`↳ table` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)`   
Required. The Table to create.  
`↳ initial_splits` |  `array<[CreateTableRequest\Split](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableRequest.Split)>`   
The optional list of row keys that will be used to initially split the table into several tablets (tablets are similar to HBase regions). Given two split keys, `s1` and `s2`, three tablets will be created, spanning the key ranges: `[, s1), [s1, s2), [s2, )`. Example: * * Row keys := `["a", "apple", "custom", "customer_1", "customer_2",` `"other", "zz"]` * * initial_split_keys := `["apple", "customer_1", "customer_2", "other"]` * * Key assignment: - Tablet 1 `[, apple) => {"a"}.` \- Tablet 2 `[apple, customer_1) => {"apple", "custom"}.` \- Tablet 3 `[customer_1, customer_2) => {"customer_1"}.` \- Tablet 4 `[customer_2, other) => {"customer_2"}.` \- Tablet 5 `[other, ) => {"other", "zz"}.`  
  
### getParent

Required. The unique name of the instance in which to create the table.

Values are of the form `projects/{project}/instances/{instance}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The unique name of the instance in which to create the table.

Values are of the form `projects/{project}/instances/{instance}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTableId

Required. The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`.

Maximum 50 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTableId

Required. The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`.

Maximum 50 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTable

Required. The Table to create.

**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)|null` |   
  
### hasTable

### clearTable

### setTable

Required. The Table to create.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInitialSplits

The optional list of row keys that will be used to initially split the table into several tablets (tablets are similar to HBase regions).

Given two split keys, `s1` and `s2`, three tablets will be created, spanning the key ranges: `[, s1), [s1, s2), [s2, )`. Example:

  * Row keys := `["a", "apple", "custom", "customer_1", "customer_2",` `"other", "zz"]`
  * initial_split_keys := `["apple", "customer_1", "customer_2", "other"]`
  * Key assignment:
    * Tablet 1 `[, apple) => {"a"}.`
    * Tablet 2 `[apple, customer_1) => {"apple", "custom"}.`
    * Tablet 3 `[customer_1, customer_2) => {"customer_1"}.`
    * Tablet 4 `[customer_2, other) => {"customer_2"}.`
    * Tablet 5 `[other, ) => {"other", "zz"}.`



**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[CreateTableRequest\Split](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableRequest.Split)>` |   
  
### setInitialSplits

The optional list of row keys that will be used to initially split the table into several tablets (tablets are similar to HBase regions).

Given two split keys, `s1` and `s2`, three tablets will be created, spanning the key ranges: `[, s1), [s1, s2), [s2, )`. Example:

  * Row keys := `["a", "apple", "custom", "customer_1", "customer_2",` `"other", "zz"]`
  * initial_split_keys := `["apple", "customer_1", "customer_2", "other"]`
  * Key assignment:
    * Tablet 1 `[, apple) => {"a"}.`
    * Tablet 2 `[apple, customer_1) => {"apple", "custom"}.`
    * Tablet 3 `[customer_1, customer_2) => {"customer_1"}.`
    * Tablet 4 `[customer_2, other) => {"customer_2"}.`
    * Tablet 5 `[other, ) => {"other", "zz"}.`



**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[CreateTableRequest\Split](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableRequest.Split)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The unique name of the instance in which to create the table. Values are of the form `projects/{project}/instances/{instance}`. Please see BigtableTableAdminClient::instanceName() for help formatting this field.  
`tableId` |  `string`   
Required. The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`. Maximum 50 characters.  
`table` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table)`   
Required. The Table to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreateTableRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateTableRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
