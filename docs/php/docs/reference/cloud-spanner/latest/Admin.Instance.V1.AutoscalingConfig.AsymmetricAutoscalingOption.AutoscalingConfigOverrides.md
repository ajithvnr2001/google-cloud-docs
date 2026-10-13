---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides
title: Cloud Spanner V1 Client - Class AutoscalingConfigOverrides (2.11.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:48.239905+00:00
---

# Cloud Spanner V1 Client - Class AutoscalingConfigOverrides (2.11.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Spanner V1 Client - Class AutoscalingConfigOverrides (2.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

Reference documentation and code samples for the Cloud Spanner V1 Client class AutoscalingConfigOverrides.

Overrides the top-level autoscaling configuration for the replicas identified by `replica_selection`. All fields in this message are optional. Any unspecified fields will use the corresponding values from the top-level autoscaling configuration.

Generated from protobuf message `google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides`

## Namespace

Google \ Cloud \ Spanner \ Admin \ Instance \ V1 \ AutoscalingConfig \ AsymmetricAutoscalingOption

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ autoscaling_limits` |  `[Google\Cloud\Spanner\Admin\Instance\V1\AutoscalingConfig\AutoscalingLimits](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingLimits)`   
Optional. If specified, overrides the min/max limit in the top-level autoscaling configuration for the selected replicas.  
`↳ autoscaling_target_high_priority_cpu_utilization_percent` |  `int`   
Optional. If specified, overrides the autoscaling target high_priority_cpu_utilization_percent in the top-level autoscaling configuration for the selected replicas.  
`↳ autoscaling_target_total_cpu_utilization_percent` |  `int`   
Optional. If specified, overrides the autoscaling target `total_cpu_utilization_percent` in the top-level autoscaling configuration for the selected replicas.  
`↳ disable_high_priority_cpu_autoscaling` |  `bool`   
Optional. If true, disables high priority CPU autoscaling for the selected replicas and ignores [high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getHighPriorityCpuUtilizationPercent__) in the top-level autoscaling configuration. When setting this field to true, setting [autoscaling_target_high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetHighPriorityCpuUtilizationPercent__) field to a non-zero value for the same replica is not supported. If false, the [autoscaling_target_high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetHighPriorityCpuUtilizationPercent__) field in the replica will be used if set to a non-zero value. Otherwise, the [high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getHighPriorityCpuUtilizationPercent__) field in the top-level autoscaling configuration will be used. Setting both [disable_high_priority_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableHighPriorityCpuAutoscaling__) and [disable_total_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableTotalCpuAutoscaling__) to true for the same replica is not supported.  
`↳ disable_total_cpu_autoscaling` |  `bool`   
Optional. If true, disables total CPU autoscaling for the selected replicas and ignores [total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getTotalCpuUtilizationPercent__) in the top-level autoscaling configuration. When setting this field to true, setting [autoscaling_target_total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetTotalCpuUtilizationPercent__) field to a non-zero value for the same replica is not supported. If false, the [autoscaling_target_total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetTotalCpuUtilizationPercent__) field in the replica will be used if set to a non-zero value. Otherwise, the [total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getTotalCpuUtilizationPercent__) field in the top-level autoscaling configuration will be used. Setting both [disable_high_priority_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableHighPriorityCpuAutoscaling__) and [disable_total_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableTotalCpuAutoscaling__) to true for the same replica is not supported.  
  
### getAutoscalingLimits

Optional. If specified, overrides the min/max limit in the top-level autoscaling configuration for the selected replicas.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Spanner\Admin\Instance\V1\AutoscalingConfig\AutoscalingLimits](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingLimits)|null` |   
  
### hasAutoscalingLimits

### clearAutoscalingLimits

### setAutoscalingLimits

Optional. If specified, overrides the min/max limit in the top-level autoscaling configuration for the selected replicas.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Cloud\Spanner\Admin\Instance\V1\AutoscalingConfig\AutoscalingLimits](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingLimits)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAutoscalingTargetHighPriorityCpuUtilizationPercent

Optional. If specified, overrides the autoscaling target high_priority_cpu_utilization_percent in the top-level autoscaling configuration for the selected replicas.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setAutoscalingTargetHighPriorityCpuUtilizationPercent

Optional. If specified, overrides the autoscaling target high_priority_cpu_utilization_percent in the top-level autoscaling configuration for the selected replicas.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAutoscalingTargetTotalCpuUtilizationPercent

Optional. If specified, overrides the autoscaling target `total_cpu_utilization_percent` in the top-level autoscaling configuration for the selected replicas.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setAutoscalingTargetTotalCpuUtilizationPercent

Optional. If specified, overrides the autoscaling target `total_cpu_utilization_percent` in the top-level autoscaling configuration for the selected replicas.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisableHighPriorityCpuAutoscaling

Optional. If true, disables high priority CPU autoscaling for the selected replicas and ignores [high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getHighPriorityCpuUtilizationPercent__) in the top-level autoscaling configuration.

When setting this field to true, setting [autoscaling_target_high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetHighPriorityCpuUtilizationPercent__) field to a non-zero value for the same replica is not supported. If false, the [autoscaling_target_high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetHighPriorityCpuUtilizationPercent__) field in the replica will be used if set to a non-zero value. Otherwise, the [high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getHighPriorityCpuUtilizationPercent__) field in the top-level autoscaling configuration will be used. Setting both [disable_high_priority_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableHighPriorityCpuAutoscaling__) and [disable_total_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableTotalCpuAutoscaling__) to true for the same replica is not supported.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDisableHighPriorityCpuAutoscaling

Optional. If true, disables high priority CPU autoscaling for the selected replicas and ignores [high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getHighPriorityCpuUtilizationPercent__) in the top-level autoscaling configuration.

When setting this field to true, setting [autoscaling_target_high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetHighPriorityCpuUtilizationPercent__) field to a non-zero value for the same replica is not supported. If false, the [autoscaling_target_high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetHighPriorityCpuUtilizationPercent__) field in the replica will be used if set to a non-zero value. Otherwise, the [high_priority_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getHighPriorityCpuUtilizationPercent__) field in the top-level autoscaling configuration will be used. Setting both [disable_high_priority_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableHighPriorityCpuAutoscaling__) and [disable_total_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableTotalCpuAutoscaling__) to true for the same replica is not supported.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisableTotalCpuAutoscaling

Optional. If true, disables total CPU autoscaling for the selected replicas and ignores [total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getTotalCpuUtilizationPercent__) in the top-level autoscaling configuration.

When setting this field to true, setting [autoscaling_target_total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetTotalCpuUtilizationPercent__) field to a non-zero value for the same replica is not supported. If false, the [autoscaling_target_total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetTotalCpuUtilizationPercent__) field in the replica will be used if set to a non-zero value. Otherwise, the [total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getTotalCpuUtilizationPercent__) field in the top-level autoscaling configuration will be used. Setting both [disable_high_priority_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableHighPriorityCpuAutoscaling__) and [disable_total_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableTotalCpuAutoscaling__) to true for the same replica is not supported.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDisableTotalCpuAutoscaling

Optional. If true, disables total CPU autoscaling for the selected replicas and ignores [total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getTotalCpuUtilizationPercent__) in the top-level autoscaling configuration.

When setting this field to true, setting [autoscaling_target_total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetTotalCpuUtilizationPercent__) field to a non-zero value for the same replica is not supported. If false, the [autoscaling_target_total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getAutoscalingTargetTotalCpuUtilizationPercent__) field in the replica will be used if set to a non-zero value. Otherwise, the [total_cpu_utilization_percent](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AutoscalingTargets#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AutoscalingTargets__getTotalCpuUtilizationPercent__) field in the top-level autoscaling configuration will be used. Setting both [disable_high_priority_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableHighPriorityCpuAutoscaling__) and [disable_total_cpu_autoscaling](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides#_Google_Cloud_Spanner_Admin_Instance_V1_AutoscalingConfig_AsymmetricAutoscalingOption_AutoscalingConfigOverrides__getDisableTotalCpuAutoscaling__) to true for the same replica is not supported.

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

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
