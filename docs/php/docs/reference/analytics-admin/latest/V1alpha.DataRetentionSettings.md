---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings
title: Google Analytics Admin V1alpha Client - Class DataRetentionSettings (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:00.996669+00:00
---

# Google Analytics Admin V1alpha Client - Class DataRetentionSettings (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class DataRetentionSettings (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class DataRetentionSettings.

Settings values for data retention. This is a singleton resource.

Generated from protobuf message `google.analytics.admin.v1alpha.DataRetentionSettings`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. Resource name for this DataRetentionSetting resource. Format: properties/{property}/dataRetentionSettings  
`↳ event_data_retention` |  `int`   
Required. The length of time that event-level data is retained.  
`↳ user_data_retention` |  `int`   
Required. The length of time that user-level data is retained.  
`↳ reset_user_data_on_new_activity` |  `bool`   
If true, reset the retention period for the user identifier with every event from that user.  
  
### getName

Identifier. Resource name for this DataRetentionSetting resource.

Format: properties/{property}/dataRetentionSettings

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Resource name for this DataRetentionSetting resource.

Format: properties/{property}/dataRetentionSettings

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventDataRetention

Required. The length of time that event-level data is retained.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [RetentionDuration](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings.RetentionDuration).  
  
### setEventDataRetention

Required. The length of time that event-level data is retained.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [RetentionDuration](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings.RetentionDuration).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUserDataRetention

Required. The length of time that user-level data is retained.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [RetentionDuration](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings.RetentionDuration).  
  
### setUserDataRetention

Required. The length of time that user-level data is retained.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [RetentionDuration](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataRetentionSettings.RetentionDuration).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResetUserDataOnNewActivity

If true, reset the retention period for the user identifier with every event from that user.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setResetUserDataOnNewActivity

If true, reset the retention period for the user identifier with every event from that user.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
