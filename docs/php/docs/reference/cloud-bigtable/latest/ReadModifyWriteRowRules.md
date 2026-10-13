---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/ReadModifyWriteRowRules/
title: Cloud Bigtable Client - Class ReadModifyWriteRowRules (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:31.924238+00:00
---

# Cloud Bigtable Client - Class ReadModifyWriteRowRules (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/ReadModifyWriteRowRules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable Client - Class ReadModifyWriteRowRules (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable Client class ReadModifyWriteRowRules.

This is a builder class which builds read/modify/write rules specifying how the specified rows contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. This is intended to be used in combination with [Table::readModifyWriteRow()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Table#_Google_Cloud_Bigtable_Table__readModifyWriteRow__).

## Namespace

Google \ Cloud \ Bigtable

## Methods 

### append

Appends the value to the existing value of the cell. If targeted cell is unset, it will be treated as containing the empty string.

**Parameters**  
---  
**Name** | **Description**  
`familyName` |  `string`   
Family name of the row.  
`qualifier` |  `string`   
Column qualifier of the row.  
`value` |  `string`   
Value of the Column qualifier.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowRules](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/ReadModifyWriteRowRules)` | returns current ReadModifyWriteRowRules object.  
  
### increment

Adds `amount` to the existing value. If the targeted cell is unset, it will be treated as containing a zero. Otherwise, the targeted cell must containt an 8-byte value (interpreted as a 64-bit big-endian signed integer), or the entire request will fail.

**Parameters**  
---  
**Name** | **Description**  
`familyName` |  `string`   
Family name of the row.  
`qualifier` |  `string`   
Column qualifier of the row.  
`amount` |  `int`   
Amount to add to value of column qualifier.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowRules](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/ReadModifyWriteRowRules)` | returns current ReadModifyWriteRowRules object.  
  
### toProto

Returns proto representation of ReadModifyWriteRule.

**Returns**  
---  
**Type** | **Description**  
`array<[V2\ReadModifyWriteRule](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/V2.ReadModifyWriteRule)>` | Returns array of ReadModifyWriteRule rules.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
