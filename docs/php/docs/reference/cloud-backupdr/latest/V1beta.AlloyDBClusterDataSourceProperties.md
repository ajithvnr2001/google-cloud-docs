---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AlloyDBClusterDataSourceProperties
title: Google Cloud Backup Dr V1beta Client - Class AlloyDBClusterDataSourceProperties (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:02.935638+00:00
---

# Google Cloud Backup Dr V1beta Client - Class AlloyDBClusterDataSourceProperties (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AlloyDBClusterDataSourceProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class AlloyDBClusterDataSourceProperties (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class AlloyDBClusterDataSourceProperties.

AlloyDBClusterDataSourceProperties represents the properties of a AlloyDB cluster resource that are stored in the DataSource.

.

Generated from protobuf message `google.cloud.backupdr.v1beta.AlloyDBClusterDataSourceProperties`

## Namespace

Google \ Cloud \ BackupDR \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Output only. Name of the AlloyDB cluster backed up by the datasource.  
`↳ pitr_windows` |  `array<[AlloyDbPitrWindow](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AlloyDbPitrWindow)>`   
Output only. Point in time recovery windows. The order is guaranteed to be ascending by start time.  
`↳ cluster_uid` |  `string`   
Output only. The cluster UID of the AlloyDB cluster backed up by the datasource.  
  
### getName

Output only. Name of the AlloyDB cluster backed up by the datasource.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Name of the AlloyDB cluster backed up by the datasource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPitrWindows

Output only. Point in time recovery windows.

The order is guaranteed to be ascending by start time.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[AlloyDbPitrWindow](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AlloyDbPitrWindow)>` |   
  
### setPitrWindows

Output only. Point in time recovery windows.

The order is guaranteed to be ascending by start time.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[AlloyDbPitrWindow](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AlloyDbPitrWindow)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getClusterUid

Output only. The cluster UID of the AlloyDB cluster backed up by the datasource.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setClusterUid

Output only. The cluster UID of the AlloyDB cluster backed up by the datasource.

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
