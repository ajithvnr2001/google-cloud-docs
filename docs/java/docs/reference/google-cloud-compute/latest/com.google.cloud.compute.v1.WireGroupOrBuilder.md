---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupOrBuilder
title: Interface WireGroupOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:15.261503+00:00
---

# Interface WireGroupOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WireGroupOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface WireGroupOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsEndpoints(String key)
    
    
    public abstract boolean containsEndpoints(String key)

A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows:

  * Key: an RFC1035 user-specified label.
  * Value: an Endpoint object.



`map<string, .google.cloud.compute.v1.WireGroupEndpoint> endpoints = 287085950; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdminEnabled()
    
    
    public abstract boolean getAdminEnabled()

Indicates whether the wires in the wire group are enabled. When false, the wires in the wire group are disabled. When true and when there is simultaneously no wire-specific override of `adminEnabled` to false, a given wire is enabled. Defaults to true.

`optional bool admin_enabled = 445675089;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The adminEnabled.  
  
### getCreationTimestamp()
    
    
    public abstract String getCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The creationTimestamp.  
  
### getCreationTimestampBytes()
    
    
    public abstract ByteString getCreationTimestampBytes()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for creationTimestamp.  
  
### getDescription()
    
    
    public abstract String getDescription()

An optional description of the wire group.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

An optional description of the wire group.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getEndpoints() (deprecated)
    
    
    public abstract Map<String,WireGroupEndpoint> getEndpoints()

Use [#getEndpointsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupOrBuilder#com_google_cloud_compute_v1_WireGroupOrBuilder_getEndpointsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[WireGroupEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupEndpoint)>` |   
  
### getEndpointsCount()
    
    
    public abstract int getEndpointsCount()

A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows:

  * Key: an RFC1035 user-specified label.
  * Value: an Endpoint object.



`map<string, .google.cloud.compute.v1.WireGroupEndpoint> endpoints = 287085950; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEndpointsMap()
    
    
    public abstract Map<String,WireGroupEndpoint> getEndpointsMap()

A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows:

  * Key: an RFC1035 user-specified label.
  * Value: an Endpoint object.



`map<string, .google.cloud.compute.v1.WireGroupEndpoint> endpoints = 287085950; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[WireGroupEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupEndpoint)>` |   
  
### getEndpointsOrDefault(String key, WireGroupEndpoint defaultValue)
    
    
    public abstract WireGroupEndpoint getEndpointsOrDefault(String key, WireGroupEndpoint defaultValue)

A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows:

  * Key: an RFC1035 user-specified label.
  * Value: an Endpoint object.



`map<string, .google.cloud.compute.v1.WireGroupEndpoint> endpoints = 287085950; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[WireGroupEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupEndpoint)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WireGroupEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupEndpoint)` |   
  
### getEndpointsOrThrow(String key)
    
    
    public abstract WireGroupEndpoint getEndpointsOrThrow(String key)

A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows:

  * Key: an RFC1035 user-specified label.
  * Value: an Endpoint object.



`map<string, .google.cloud.compute.v1.WireGroupEndpoint> endpoints = 287085950; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WireGroupEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupEndpoint)` |   
  
### getId()
    
    
    public abstract long getId()

Output only. [Output Only] The unique identifier for the resource type. The server generates this identifier.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getKind()
    
    
    public abstract String getKind()

Output only. [Output Only] Type of the resource. Alwayscompute#wireGroups for wire groups.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. [Output Only] Type of the resource. Alwayscompute#wireGroups for wire groups.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getName()
    
    
    public abstract String getName()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getReconciling()
    
    
    public abstract boolean getReconciling()

Output only. [Output Only] Indicates whether there are wire changes yet to be processed.

`optional bool reconciling = 432155787;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconciling.  
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getTopology()
    
    
    public abstract WireGroupTopology getTopology()

Output only. Topology details for the wire group configuration.

`optional .google.cloud.compute.v1.WireGroupTopology topology = 122274415;`

**Returns**  
---  
**Type** | **Description**  
`[WireGroupTopology](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupTopology)` | The topology.  
  
### getTopologyOrBuilder()
    
    
    public abstract WireGroupTopologyOrBuilder getTopologyOrBuilder()

Output only. Topology details for the wire group configuration.

`optional .google.cloud.compute.v1.WireGroupTopology topology = 122274415;`

**Returns**  
---  
**Type** | **Description**  
`[WireGroupTopologyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupTopologyOrBuilder)` |   
  
### getWireProperties()
    
    
    public abstract WireProperties getWireProperties()

Properties for all wires in the wire group.

`optional .google.cloud.compute.v1.WireProperties wire_properties = 303111469;`

**Returns**  
---  
**Type** | **Description**  
`[WireProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireProperties)` | The wireProperties.  
  
### getWirePropertiesOrBuilder()
    
    
    public abstract WirePropertiesOrBuilder getWirePropertiesOrBuilder()

Properties for all wires in the wire group.

`optional .google.cloud.compute.v1.WireProperties wire_properties = 303111469;`

**Returns**  
---  
**Type** | **Description**  
`[WirePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WirePropertiesOrBuilder)` |   
  
### getWires(int index)
    
    
    public abstract Wire getWires(int index)

Output only. The single/redundant wire(s) managed by the wire group.

`repeated .google.cloud.compute.v1.Wire wires = 113139854;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Wire](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Wire)` |   
  
### getWiresCount()
    
    
    public abstract int getWiresCount()

Output only. The single/redundant wire(s) managed by the wire group.

`repeated .google.cloud.compute.v1.Wire wires = 113139854;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getWiresList()
    
    
    public abstract List<Wire> getWiresList()

Output only. The single/redundant wire(s) managed by the wire group.

`repeated .google.cloud.compute.v1.Wire wires = 113139854;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Wire](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Wire)>` |   
  
### getWiresOrBuilder(int index)
    
    
    public abstract WireOrBuilder getWiresOrBuilder(int index)

Output only. The single/redundant wire(s) managed by the wire group.

`repeated .google.cloud.compute.v1.Wire wires = 113139854;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WireOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireOrBuilder)` |   
  
### getWiresOrBuilderList()
    
    
    public abstract List<? extends WireOrBuilder> getWiresOrBuilderList()

Output only. The single/redundant wire(s) managed by the wire group.

`repeated .google.cloud.compute.v1.Wire wires = 113139854;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.compute.v1.WireOrBuilder>` |   
  
### hasAdminEnabled()
    
    
    public abstract boolean hasAdminEnabled()

Indicates whether the wires in the wire group are enabled. When false, the wires in the wire group are disabled. When true and when there is simultaneously no wire-specific override of `adminEnabled` to false, a given wire is enabled. Defaults to true.

`optional bool admin_enabled = 445675089;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adminEnabled field is set.  
  
### hasCreationTimestamp()
    
    
    public abstract boolean hasCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTimestamp field is set.  
  
### hasDescription()
    
    
    public abstract boolean hasDescription()

An optional description of the wire group.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasId()
    
    
    public abstract boolean hasId()

Output only. [Output Only] The unique identifier for the resource type. The server generates this identifier.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasKind()
    
    
    public abstract boolean hasKind()

Output only. [Output Only] Type of the resource. Alwayscompute#wireGroups for wire groups.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasReconciling()
    
    
    public abstract boolean hasReconciling()

Output only. [Output Only] Indicates whether there are wire changes yet to be processed.

`optional bool reconciling = 432155787;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reconciling field is set.  
  
### hasSelfLink()
    
    
    public abstract boolean hasSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasTopology()
    
    
    public abstract boolean hasTopology()

Output only. Topology details for the wire group configuration.

`optional .google.cloud.compute.v1.WireGroupTopology topology = 122274415;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the topology field is set.  
  
### hasWireProperties()
    
    
    public abstract boolean hasWireProperties()

Properties for all wires in the wire group.

`optional .google.cloud.compute.v1.WireProperties wire_properties = 303111469;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the wireProperties field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
