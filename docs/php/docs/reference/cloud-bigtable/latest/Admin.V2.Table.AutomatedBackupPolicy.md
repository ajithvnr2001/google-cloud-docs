---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.AutomatedBackupPolicy
title: Cloud Bigtable V2 Client - Class AutomatedBackupPolicy (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:55.211985+00:00
---

# Cloud Bigtable V2 Client - Class AutomatedBackupPolicy (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table.AutomatedBackupPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class AutomatedBackupPolicy (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class AutomatedBackupPolicy.

Defines an automated backup policy for a table

Generated from protobuf message `google.bigtable.admin.v2.Table.AutomatedBackupPolicy`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2 \ Table

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ retention_period` |  `Google\Protobuf\Duration`   
Required. How long the automated backups should be retained. Values must be at least 3 days and at most 90 days.  
`↳ frequency` |  `Google\Protobuf\Duration`   
How frequently automated backups should occur. The only supported value at this time is 24 hours. An undefined frequency is treated as 24 hours.  
`↳ locations` |  `string[]`   
Optional. A list of Cloud Bigtable zones where automated backups are allowed to be created. If empty, automated backups will be created in all zones of the instance. Locations are in the format `projects/{project}/locations/{zone}`. This field can only set for tables in Enterprise Plus instances.  
`↳ keep_hot_duration` |  `Google\Protobuf\Duration`   
Optional. The amount of time that the automated backups remain hot. If specified, the backups created by this policy are `HOT` backups. If not specified, the backups are `STANDARD` backups. The value must be at least 24 hours and at most 10 days, and can't exceed the policy's `retention_period`. Only SSD instances support `HOT` automated backups.  
`↳ disabled` |  `bool`   
Optional. If `true`, automated backups are explicitly disabled on this table. This allows users to opt out of default enablement.  
  
### getRetentionPeriod

Required. How long the automated backups should be retained. Values must be at least 3 days and at most 90 days.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasRetentionPeriod

### clearRetentionPeriod

### setRetentionPeriod

Required. How long the automated backups should be retained. Values must be at least 3 days and at most 90 days.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFrequency

How frequently automated backups should occur. The only supported value at this time is 24 hours. An undefined frequency is treated as 24 hours.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasFrequency

### clearFrequency

### setFrequency

How frequently automated backups should occur. The only supported value at this time is 24 hours. An undefined frequency is treated as 24 hours.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLocations

Optional. A list of Cloud Bigtable zones where automated backups are allowed to be created. If empty, automated backups will be created in all zones of the instance. Locations are in the format `projects/{project}/locations/{zone}`.

This field can only set for tables in Enterprise Plus instances.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setLocations

Optional. A list of Cloud Bigtable zones where automated backups are allowed to be created. If empty, automated backups will be created in all zones of the instance. Locations are in the format `projects/{project}/locations/{zone}`.

This field can only set for tables in Enterprise Plus instances.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getKeepHotDuration

Optional. The amount of time that the automated backups remain hot.

If specified, the backups created by this policy are `HOT` backups. If not specified, the backups are `STANDARD` backups. The value must be at least 24 hours and at most 10 days, and can't exceed the policy's `retention_period`. Only SSD instances support `HOT` automated backups.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasKeepHotDuration

### clearKeepHotDuration

### setKeepHotDuration

Optional. The amount of time that the automated backups remain hot.

If specified, the backups created by this policy are `HOT` backups. If not specified, the backups are `STANDARD` backups. The value must be at least 24 hours and at most 10 days, and can't exceed the policy's `retention_period`. Only SSD instances support `HOT` automated backups.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisabled

Optional. If `true`, automated backups are explicitly disabled on this table. This allows users to opt out of default enablement.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDisabled

Optional. If `true`, automated backups are explicitly disabled on this table. This allows users to opt out of default enablement.

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

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
