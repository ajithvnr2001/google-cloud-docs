---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.RouterOrBuilder
title: Interface RouterOrBuilder (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:22.366405+00:00
---

# Interface RouterOrBuilder (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.RouterOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RouterOrBuilder (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface RouterOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Labels associated with this resource.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBgp()
    
    
    public abstract Router.Bgp getBgp()

BGP information specific to this router.

`.google.cloud.edgenetwork.v1.Router.Bgp bgp = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Router.Bgp](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router.Bgp)` | The bgp.  
  
### getBgpOrBuilder()
    
    
    public abstract Router.BgpOrBuilder getBgpOrBuilder()

BGP information specific to this router.

`.google.cloud.edgenetwork.v1.Router.Bgp bgp = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Router.BgpOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router.BgpOrBuilder)` |   
  
### getBgpPeer(int index)
    
    
    public abstract Router.BgpPeer getBgpPeer(int index)

BGP peers.

`repeated .google.cloud.edgenetwork.v1.Router.BgpPeer bgp_peer = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Router.BgpPeer](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router.BgpPeer)` |   
  
### getBgpPeerCount()
    
    
    public abstract int getBgpPeerCount()

BGP peers.

`repeated .google.cloud.edgenetwork.v1.Router.BgpPeer bgp_peer = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBgpPeerList()
    
    
    public abstract List<Router.BgpPeer> getBgpPeerList()

BGP peers.

`repeated .google.cloud.edgenetwork.v1.Router.BgpPeer bgp_peer = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BgpPeer](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router.BgpPeer)>` |   
  
### getBgpPeerOrBuilder(int index)
    
    
    public abstract Router.BgpPeerOrBuilder getBgpPeerOrBuilder(int index)

BGP peers.

`repeated .google.cloud.edgenetwork.v1.Router.BgpPeer bgp_peer = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Router.BgpPeerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router.BgpPeerOrBuilder)` |   
  
### getBgpPeerOrBuilderList()
    
    
    public abstract List<? extends Router.BgpPeerOrBuilder> getBgpPeerOrBuilderList()

BGP peers.

`repeated .google.cloud.edgenetwork.v1.Router.BgpPeer bgp_peer = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.edgenetwork.v1.Router.BgpPeerOrBuilder>` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when the router was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when the router was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. A free-text description of the resource. Max length 1024 characters.

`string description = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. A free-text description of the resource. Max length 1024 characters.

`string description = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getInterface(int index)
    
    
    public abstract Router.Interface getInterface(int index)

Router interfaces.

`repeated .google.cloud.edgenetwork.v1.Router.Interface interface = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Router.Interface](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router.Interface)` |   
  
### getInterfaceCount()
    
    
    public abstract int getInterfaceCount()

Router interfaces.

`repeated .google.cloud.edgenetwork.v1.Router.Interface interface = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInterfaceList()
    
    
    public abstract List<Router.Interface> getInterfaceList()

Router interfaces.

`repeated .google.cloud.edgenetwork.v1.Router.Interface interface = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Interface](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router.Interface)>` |   
  
### getInterfaceOrBuilder(int index)
    
    
    public abstract Router.InterfaceOrBuilder getInterfaceOrBuilder(int index)

Router interfaces.

`repeated .google.cloud.edgenetwork.v1.Router.Interface interface = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Router.InterfaceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router.InterfaceOrBuilder)` |   
  
### getInterfaceOrBuilderList()
    
    
    public abstract List<? extends Router.InterfaceOrBuilder> getInterfaceOrBuilderList()

Router interfaces.

`repeated .google.cloud.edgenetwork.v1.Router.Interface interface = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.edgenetwork.v1.Router.InterfaceOrBuilder>` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.RouterOrBuilder#com_google_cloud_edgenetwork_v1_RouterOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Labels associated with this resource.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Labels associated with this resource.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Labels associated with this resource.

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

Labels associated with this resource.

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

Required. The canonical resource name of the router.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The canonical resource name of the router.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

Required. The canonical name of the network to which this router belongs. The name is in the form of `projects/{project}/locations/{location}/zones/{zone}/networks/{network}`.

` string network = 6 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

Required. The canonical name of the network to which this router belongs. The name is in the form of `projects/{project}/locations/{location}/zones/{zone}/networks/{network}`.

` string network = 6 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getRouteAdvertisements(int index)
    
    
    public abstract String getRouteAdvertisements(int index)

Optional. A list of CIDRs in IP/Length format to advertise northbound as static routes from this router.

`repeated string route_advertisements = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The routeAdvertisements at the given index.  
  
### getRouteAdvertisementsBytes(int index)
    
    
    public abstract ByteString getRouteAdvertisementsBytes(int index)

Optional. A list of CIDRs in IP/Length format to advertise northbound as static routes from this router.

`repeated string route_advertisements = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the routeAdvertisements at the given index.  
  
### getRouteAdvertisementsCount()
    
    
    public abstract int getRouteAdvertisementsCount()

Optional. A list of CIDRs in IP/Length format to advertise northbound as static routes from this router.

`repeated string route_advertisements = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of routeAdvertisements.  
  
### getRouteAdvertisementsList()
    
    
    public abstract List<String> getRouteAdvertisementsList()

Optional. A list of CIDRs in IP/Length format to advertise northbound as static routes from this router.

`repeated string route_advertisements = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the routeAdvertisements.  
  
### getState()
    
    
    public abstract ResourceState getState()

Output only. Current stage of the resource to the device by config push.

` .google.cloud.edgenetwork.v1.ResourceState state = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceState](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ResourceState)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. Current stage of the resource to the device by config push.

` .google.cloud.edgenetwork.v1.ResourceState state = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The time when the router was last updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time when the router was last updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasBgp()
    
    
    public abstract boolean hasBgp()

BGP information specific to this router.

`.google.cloud.edgenetwork.v1.Router.Bgp bgp = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bgp field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when the router was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The time when the router was last updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
