---
url: https://docs.cloud.google.com/php/docs/reference/cloud-maintenance/latest/V1beta.ResourceMaintenance.Maintenance
title: Google Cloud Maintenance Api V1beta Client - Class Maintenance (0.5.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:50.626349+00:00
---

# Google Cloud Maintenance Api V1beta Client - Class Maintenance (0.5.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-maintenance/latest/V1beta.ResourceMaintenance.Maintenance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Maintenance Api V1beta Client - Class Maintenance (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.4.0  0.3.2  0.2.1  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Maintenance Api V1beta Client class Maintenance.

Maintenance is the maintenance details of a resource's maintenance.

Generated from protobuf message `google.cloud.maintenance.api.v1beta.ResourceMaintenance.Maintenance`

## Namespace

Google \ Cloud \ Maintenance \ Api \ V1beta \ ResourceMaintenance

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ maintenance_name` |  `string`   
Maintenance is the name of the corresponding maintenance resource following the standard naming scheme: `"{maintenance-id}"`  
`↳ title` |  `string`   
Output only. The title of the maintenance.  
`↳ description` |  `string`   
Output only. The description of the maintenance.  
`↳ category` |  `int`   
Output only. The category of the maintenance.  
  
### getMaintenanceName

Maintenance is the name of the corresponding maintenance resource following the standard naming scheme: `"{maintenance-id}"`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setMaintenanceName

Maintenance is the name of the corresponding maintenance resource following the standard naming scheme: `"{maintenance-id}"`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTitle

Output only. The title of the maintenance.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTitle

Output only. The title of the maintenance.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Output only. The description of the maintenance.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Output only. The description of the maintenance.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCategory

Output only. The category of the maintenance.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [MaintenanceCategory](https://docs.cloud.google.com/php/docs/reference/cloud-maintenance/latest/V1beta.MaintenanceCategory).  
  
### setCategory

Output only. The category of the maintenance.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [MaintenanceCategory](https://docs.cloud.google.com/php/docs/reference/cloud-maintenance/latest/V1beta.MaintenanceCategory).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
