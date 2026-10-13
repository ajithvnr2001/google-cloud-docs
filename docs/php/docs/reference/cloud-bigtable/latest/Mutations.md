---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Mutations/
title: Cloud Bigtable Client - Class Mutations (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:40.913815+00:00
---

# Cloud Bigtable Client - Class Mutations (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Mutations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable Client - Class Mutations (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable Client class Mutations.

Represents a Mutation to perform data operation on Bigtable table.

This is used to insert,update, delete operation on row in Bigtable table.

## Namespace

Google \ Cloud \ Bigtable

## Methods 

### upsert

Creates Insert/Update mutation for a row.

**Parameters**  
---  
**Name** | **Description**  
`family` |  `string`   
Family name of the row.  
`qualifier` |  `string`   
Column qualifier of the row.  
`value` |  `string`   
Value of the column qualifier.  
`timeStamp` |  `string|int`   
[optional] A timestamp value, in microseconds. Use the value `-1` to utilize the current Bigtable server time. _Defaults to_ * the current local system time.  
**Returns**  
---  
**Type** | **Description**  
`[Mutations](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Mutations)` | returns current Mutations object.  
  
### deleteFromFamily

Creates delete from family mutation for a row.

**Parameter**  
---  
**Name** | **Description**  
`family` |  `string`   
Family name of the row.  
**Returns**  
---  
**Type** | **Description**  
`[Mutations](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Mutations)` | returns current Mutations object.  
  
### deleteFromColumn

Creates delete from column mutation for a row.

**Parameters**  
---  
**Name** | **Description**  
`family` |  `string`   
Family name of the row.  
`qualifier` |  `string`   
Column qualifier of the row.  
`timeRange` |  `array`   
[optional] Array of values value, in microseconds to delete from column, keyed by `start` and `end` representing time range window. `start` **Defaults to** 0 `end` **Defaults to** infinity  
**Returns**  
---  
**Type** | **Description**  
`[Mutations](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Mutations)` | returns current Mutations object.  
  
### deleteRow

Creates delete row mutation for a row.

**Returns**  
---  
**Type** | **Description**  
`[Mutations](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Mutations)` | returns current Mutations object.  
  
### toProto

Returns protobuf representation of Mutations.

**Returns**  
---  
**Type** | **Description**  
`array` | returns array of protobuf representation of Mutations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
