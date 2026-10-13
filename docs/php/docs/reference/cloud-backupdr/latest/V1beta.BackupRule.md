---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupRule
title: Google Cloud Backup Dr V1beta Client - Class BackupRule (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:07.858712+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupRule (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupRule (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupRule.

`BackupRule` binds the backup schedule to a retention policy.

Generated from protobuf message `google.cloud.backupdr.v1beta.BackupRule`

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
`↳ standard_schedule` |  `[StandardSchedule](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.StandardSchedule)`   
Optional. Defines a schedule that runs within the confines of a defined window of time.  
`↳ rule_id` |  `string`   
Required. Immutable. The unique id of this `BackupRule`. The `rule_id` is unique per `BackupPlan`.The `rule_id` must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /[a-z][a-z0-9-]{,62}/.  
`↳ backup_retention_days` |  `int`   
Required. Configures the duration for which backup data will be kept. It is defined in “days”. The value should be greater than or equal to minimum enforced retention of the backup vault. Minimum value is 1 and maximum value is 36159 for custom retention on-demand backup. Minimum and maximum values are workload specific for all other rules. Note: Longer retention can lead to higher storage costs post introductory trial. We recommend starting with a short duration of 3 days or less.  
  
### getStandardSchedule

Optional. Defines a schedule that runs within the confines of a defined window of time.

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.StandardSchedule)|null` |   
  
### hasStandardSchedule

### setStandardSchedule

Optional. Defines a schedule that runs within the confines of a defined window of time.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[StandardSchedule](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.StandardSchedule)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRuleId

Required. Immutable. The unique id of this `BackupRule`. The `rule_id` is unique per `BackupPlan`.The `rule_id` must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /[a-z][a-z0-9-]{,62}/.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRuleId

Required. Immutable. The unique id of this `BackupRule`. The `rule_id` is unique per `BackupPlan`.The `rule_id` must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /[a-z][a-z0-9-]{,62}/.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupRetentionDays

Required. Configures the duration for which backup data will be kept. It is defined in “days”. The value should be greater than or equal to minimum enforced retention of the backup vault.

Minimum value is 1 and maximum value is 36159 for custom retention on-demand backup. Minimum and maximum values are workload specific for all other rules. Note: Longer retention can lead to higher storage costs post introductory trial. We recommend starting with a short duration of 3 days or less.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setBackupRetentionDays

Required. Configures the duration for which backup data will be kept. It is defined in “days”. The value should be greater than or equal to minimum enforced retention of the backup vault.

Minimum value is 1 and maximum value is 36159 for custom retention on-demand backup. Minimum and maximum values are workload specific for all other rules. Note: Longer retention can lead to higher storage costs post introductory trial. We recommend starting with a short duration of 3 days or less.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupScheduleOneof

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
