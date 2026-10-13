---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterAutoscalingOrBuilder
title: Interface ClusterAutoscalingOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:04.264609+00:00
---

# Interface ClusterAutoscalingOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterAutoscalingOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClusterAutoscalingOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface ClusterAutoscalingOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAutopilotGeneralProfile()
    
    
    public abstract ClusterAutoscaling.AutopilotGeneralProfile getAutopilotGeneralProfile()

Autopilot general profile for the cluster, which defines the configuration for the cluster.

` .google.container.v1.ClusterAutoscaling.AutopilotGeneralProfile autopilot_general_profile = 14; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscaling.AutopilotGeneralProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterAutoscaling.AutopilotGeneralProfile)` | The autopilotGeneralProfile.  
  
### getAutopilotGeneralProfileValue()
    
    
    public abstract int getAutopilotGeneralProfileValue()

Autopilot general profile for the cluster, which defines the configuration for the cluster.

` .google.container.v1.ClusterAutoscaling.AutopilotGeneralProfile autopilot_general_profile = 14; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for autopilotGeneralProfile.  
  
### getAutoprovisioningLocations(int index)
    
    
    public abstract String getAutoprovisioningLocations(int index)

The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes can be created by NAP.

`repeated string autoprovisioning_locations = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The autoprovisioningLocations at the given index.  
  
### getAutoprovisioningLocationsBytes(int index)
    
    
    public abstract ByteString getAutoprovisioningLocationsBytes(int index)

The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes can be created by NAP.

`repeated string autoprovisioning_locations = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the autoprovisioningLocations at the given index.  
  
### getAutoprovisioningLocationsCount()
    
    
    public abstract int getAutoprovisioningLocationsCount()

The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes can be created by NAP.

`repeated string autoprovisioning_locations = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of autoprovisioningLocations.  
  
### getAutoprovisioningLocationsList()
    
    
    public abstract List<String> getAutoprovisioningLocationsList()

The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes can be created by NAP.

`repeated string autoprovisioning_locations = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the autoprovisioningLocations.  
  
### getAutoprovisioningNodePoolDefaults()
    
    
    public abstract AutoprovisioningNodePoolDefaults getAutoprovisioningNodePoolDefaults()

AutoprovisioningNodePoolDefaults contains defaults for a node pool created by NAP.

` .google.container.v1.AutoprovisioningNodePoolDefaults autoprovisioning_node_pool_defaults = 4; `

**Returns**  
---  
**Type** | **Description**  
`[AutoprovisioningNodePoolDefaults](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutoprovisioningNodePoolDefaults)` | The autoprovisioningNodePoolDefaults.  
  
### getAutoprovisioningNodePoolDefaultsOrBuilder()
    
    
    public abstract AutoprovisioningNodePoolDefaultsOrBuilder getAutoprovisioningNodePoolDefaultsOrBuilder()

AutoprovisioningNodePoolDefaults contains defaults for a node pool created by NAP.

` .google.container.v1.AutoprovisioningNodePoolDefaults autoprovisioning_node_pool_defaults = 4; `

**Returns**  
---  
**Type** | **Description**  
`[AutoprovisioningNodePoolDefaultsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutoprovisioningNodePoolDefaultsOrBuilder)` |   
  
### getAutoscalingProfile()
    
    
    public abstract ClusterAutoscaling.AutoscalingProfile getAutoscalingProfile()

Defines autoscaling behaviour.

`.google.container.v1.ClusterAutoscaling.AutoscalingProfile autoscaling_profile = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscaling.AutoscalingProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterAutoscaling.AutoscalingProfile)` | The autoscalingProfile.  
  
### getAutoscalingProfileValue()
    
    
    public abstract int getAutoscalingProfileValue()

Defines autoscaling behaviour.

`.google.container.v1.ClusterAutoscaling.AutoscalingProfile autoscaling_profile = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for autoscalingProfile.  
  
### getDefaultComputeClassConfig()
    
    
    public abstract DefaultComputeClassConfig getDefaultComputeClassConfig()

Default compute class is a configuration for default compute class.

`.google.container.v1.DefaultComputeClassConfig default_compute_class_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[DefaultComputeClassConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DefaultComputeClassConfig)` | The defaultComputeClassConfig.  
  
### getDefaultComputeClassConfigOrBuilder()
    
    
    public abstract DefaultComputeClassConfigOrBuilder getDefaultComputeClassConfigOrBuilder()

Default compute class is a configuration for default compute class.

`.google.container.v1.DefaultComputeClassConfig default_compute_class_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[DefaultComputeClassConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DefaultComputeClassConfigOrBuilder)` |   
  
### getEnableNodeAutoprovisioning()
    
    
    public abstract boolean getEnableNodeAutoprovisioning()

Enables automatic node pool creation and deletion.

`bool enable_node_autoprovisioning = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableNodeAutoprovisioning.  
  
### getResourceLimits(int index)
    
    
    public abstract ResourceLimit getResourceLimits(int index)

Contains global constraints regarding minimum and maximum amount of resources in the cluster.

`repeated .google.container.v1.ResourceLimit resource_limits = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResourceLimit](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceLimit)` |   
  
### getResourceLimitsCount()
    
    
    public abstract int getResourceLimitsCount()

Contains global constraints regarding minimum and maximum amount of resources in the cluster.

`repeated .google.container.v1.ResourceLimit resource_limits = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourceLimitsList()
    
    
    public abstract List<ResourceLimit> getResourceLimitsList()

Contains global constraints regarding minimum and maximum amount of resources in the cluster.

`repeated .google.container.v1.ResourceLimit resource_limits = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResourceLimit](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceLimit)>` |   
  
### getResourceLimitsOrBuilder(int index)
    
    
    public abstract ResourceLimitOrBuilder getResourceLimitsOrBuilder(int index)

Contains global constraints regarding minimum and maximum amount of resources in the cluster.

`repeated .google.container.v1.ResourceLimit resource_limits = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResourceLimitOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceLimitOrBuilder)` |   
  
### getResourceLimitsOrBuilderList()
    
    
    public abstract List<? extends ResourceLimitOrBuilder> getResourceLimitsOrBuilderList()

Contains global constraints regarding minimum and maximum amount of resources in the cluster.

`repeated .google.container.v1.ResourceLimit resource_limits = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.ResourceLimitOrBuilder>` |   
  
### hasAutoprovisioningNodePoolDefaults()
    
    
    public abstract boolean hasAutoprovisioningNodePoolDefaults()

AutoprovisioningNodePoolDefaults contains defaults for a node pool created by NAP.

` .google.container.v1.AutoprovisioningNodePoolDefaults autoprovisioning_node_pool_defaults = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autoprovisioningNodePoolDefaults field is set.  
  
### hasDefaultComputeClassConfig()
    
    
    public abstract boolean hasDefaultComputeClassConfig()

Default compute class is a configuration for default compute class.

`.google.container.v1.DefaultComputeClassConfig default_compute_class_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the defaultComputeClassConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
