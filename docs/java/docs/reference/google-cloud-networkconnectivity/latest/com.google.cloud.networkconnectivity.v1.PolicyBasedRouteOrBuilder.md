---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRouteOrBuilder
title: Interface PolicyBasedRouteOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:00.014163+00:00
---

# Interface PolicyBasedRouteOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRouteOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PolicyBasedRouteOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 
    
    
    public interface PolicyBasedRouteOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

User-defined labels.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time when the policy-based route was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time when the policy-based route was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. An optional description of this resource. Provide this field when you create the resource.

`string description = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. An optional description of this resource. Provide this field when you create the resource.

`string description = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getFilter()
    
    
    public abstract PolicyBasedRoute.Filter getFilter()

Required. The filter to match L4 traffic.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.Filter filter = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.Filter](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.Filter)` | The filter.  
  
### getFilterOrBuilder()
    
    
    public abstract PolicyBasedRoute.FilterOrBuilder getFilterOrBuilder()

Required. The filter to match L4 traffic.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.Filter filter = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.FilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.FilterOrBuilder)` |   
  
### getInterconnectAttachment()
    
    
    public abstract PolicyBasedRoute.InterconnectAttachment getInterconnectAttachment()

Optional. The interconnect attachments that this policy-based route applies to.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.InterconnectAttachment interconnect_attachment = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.InterconnectAttachment)` | The interconnectAttachment.  
  
### getInterconnectAttachmentOrBuilder()
    
    
    public abstract PolicyBasedRoute.InterconnectAttachmentOrBuilder getInterconnectAttachmentOrBuilder()

Optional. The interconnect attachments that this policy-based route applies to.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.InterconnectAttachment interconnect_attachment = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.InterconnectAttachmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.InterconnectAttachmentOrBuilder)` |   
  
### getKind()
    
    
    public abstract String getKind()

Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for policy-based Route resources.

`string kind = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for policy-based Route resources.

`string kind = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRouteOrBuilder#com_google_cloud_networkconnectivity_v1_PolicyBasedRouteOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

User-defined labels.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

User-defined labels.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

User-defined labels.

`map<string, string> labels = 4;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

User-defined labels.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Immutable. A unique name of the resource in the form of `projects/{project_number}/locations/global/PolicyBasedRoutes/{policy_based_route_id}`

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Immutable. A unique name of the resource in the form of `projects/{project_number}/locations/global/PolicyBasedRoutes/{policy_based_route_id}`

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

Required. Fully-qualified URL of the network that this route applies to, for example: projects/my-project/global/networks/my-network.

` string network = 6 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

Required. Fully-qualified URL of the network that this route applies to, for example: projects/my-project/global/networks/my-network.

` string network = 6 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNextHopCase()
    
    
    public abstract PolicyBasedRoute.NextHopCase getNextHopCase()

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.NextHopCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.NextHopCase)` |   
  
### getNextHopIlbIp()
    
    
    public abstract String getNextHopIlbIp()

Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported.

`string next_hop_ilb_ip = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextHopIlbIp.  
  
### getNextHopIlbIpBytes()
    
    
    public abstract ByteString getNextHopIlbIpBytes()

Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported.

`string next_hop_ilb_ip = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextHopIlbIp.  
  
### getNextHopOtherRoutes()
    
    
    public abstract PolicyBasedRoute.OtherRoutes getNextHopOtherRoutes()

Optional. Other routes that will be referenced to determine the next hop of the packet.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.OtherRoutes next_hop_other_routes = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.OtherRoutes](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.OtherRoutes)` | The nextHopOtherRoutes.  
  
### getNextHopOtherRoutesValue()
    
    
    public abstract int getNextHopOtherRoutesValue()

Optional. Other routes that will be referenced to determine the next hop of the packet.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.OtherRoutes next_hop_other_routes = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for nextHopOtherRoutes.  
  
### getPriority()
    
    
    public abstract int getPriority()

Optional. The priority of this policy-based route. Priority is used to break ties in cases where there are more than one matching policy-based routes found. In cases where multiple policy-based routes are matched, the one with the lowest-numbered priority value wins. The default value is

  1. The priority value must be from 1 to 65535, inclusive.



`int32 priority = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The priority.  
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. Server-defined fully-qualified URL for this resource.

`string self_link = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. Server-defined fully-qualified URL for this resource.

`string self_link = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getTargetCase()
    
    
    public abstract PolicyBasedRoute.TargetCase getTargetCase()

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.TargetCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.TargetCase)` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Time when the policy-based route was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Time when the policy-based route was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getVirtualMachine()
    
    
    public abstract PolicyBasedRoute.VirtualMachine getVirtualMachine()

Optional. VM instances that this policy-based route applies to.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.VirtualMachine virtual_machine = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.VirtualMachine](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.VirtualMachine)` | The virtualMachine.  
  
### getVirtualMachineOrBuilder()
    
    
    public abstract PolicyBasedRoute.VirtualMachineOrBuilder getVirtualMachineOrBuilder()

Optional. VM instances that this policy-based route applies to.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.VirtualMachine virtual_machine = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.VirtualMachineOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.VirtualMachineOrBuilder)` |   
  
### getWarnings(int index)
    
    
    public abstract PolicyBasedRoute.Warnings getWarnings(int index)

Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.

` repeated .google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings warnings = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.Warnings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings)` |   
  
### getWarningsCount()
    
    
    public abstract int getWarningsCount()

Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.

` repeated .google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings warnings = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getWarningsList()
    
    
    public abstract List<PolicyBasedRoute.Warnings> getWarningsList()

Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.

` repeated .google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings warnings = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Warnings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings)>` |   
  
### getWarningsOrBuilder(int index)
    
    
    public abstract PolicyBasedRoute.WarningsOrBuilder getWarningsOrBuilder(int index)

Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.

` repeated .google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings warnings = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute.WarningsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.WarningsOrBuilder)` |   
  
### getWarningsOrBuilderList()
    
    
    public abstract List<? extends PolicyBasedRoute.WarningsOrBuilder> getWarningsOrBuilderList()

Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.

` repeated .google.cloud.networkconnectivity.v1.PolicyBasedRoute.Warnings warnings = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.networkconnectivity.v1.PolicyBasedRoute.WarningsOrBuilder>` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time when the policy-based route was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasFilter()
    
    
    public abstract boolean hasFilter()

Required. The filter to match L4 traffic.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.Filter filter = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the filter field is set.  
  
### hasInterconnectAttachment()
    
    
    public abstract boolean hasInterconnectAttachment()

Optional. The interconnect attachments that this policy-based route applies to.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.InterconnectAttachment interconnect_attachment = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the interconnectAttachment field is set.  
  
### hasNextHopIlbIp()
    
    
    public abstract boolean hasNextHopIlbIp()

Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported.

`string next_hop_ilb_ip = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nextHopIlbIp field is set.  
  
### hasNextHopOtherRoutes()
    
    
    public abstract boolean hasNextHopOtherRoutes()

Optional. Other routes that will be referenced to determine the next hop of the packet.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.OtherRoutes next_hop_other_routes = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nextHopOtherRoutes field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Time when the policy-based route was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
### hasVirtualMachine()
    
    
    public abstract boolean hasVirtualMachine()

Optional. VM instances that this policy-based route applies to.

` .google.cloud.networkconnectivity.v1.PolicyBasedRoute.VirtualMachine virtual_machine = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the virtualMachine field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
