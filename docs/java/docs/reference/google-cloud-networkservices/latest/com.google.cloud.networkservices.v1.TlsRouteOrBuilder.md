---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRouteOrBuilder
title: Interface TlsRouteOrBuilder (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:22.462024+00:00
---

# Interface TlsRouteOrBuilder (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRouteOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TlsRouteOrBuilder (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface TlsRouteOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Set of label tags associated with the TlsRoute resource.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

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

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. A free-text description of the resource. Max length 1024 characters.

`string description = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. A free-text description of the resource. Max length 1024 characters.

`string description = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getGateways(int index)
    
    
    public abstract String getGateways(int index)

Optional. Gateways defines a list of gateways this TlsRoute is attached to, as one of the routing rules to route the requests served by the gateway.

Each gateway reference should match the pattern: `projects/*/locations/*/gateways/<gateway_name>`

` repeated string gateways = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gateways at the given index.  
  
### getGatewaysBytes(int index)
    
    
    public abstract ByteString getGatewaysBytes(int index)

Optional. Gateways defines a list of gateways this TlsRoute is attached to, as one of the routing rules to route the requests served by the gateway.

Each gateway reference should match the pattern: `projects/*/locations/*/gateways/<gateway_name>`

` repeated string gateways = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the gateways at the given index.  
  
### getGatewaysCount()
    
    
    public abstract int getGatewaysCount()

Optional. Gateways defines a list of gateways this TlsRoute is attached to, as one of the routing rules to route the requests served by the gateway.

Each gateway reference should match the pattern: `projects/*/locations/*/gateways/<gateway_name>`

` repeated string gateways = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of gateways.  
  
### getGatewaysList()
    
    
    public abstract List<String> getGatewaysList()

Optional. Gateways defines a list of gateways this TlsRoute is attached to, as one of the routing rules to route the requests served by the gateway.

Each gateway reference should match the pattern: `projects/*/locations/*/gateways/<gateway_name>`

` repeated string gateways = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the gateways.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRouteOrBuilder#com_google_cloud_networkservices_v1_TlsRouteOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Set of label tags associated with the TlsRoute resource.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Set of label tags associated with the TlsRoute resource.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Set of label tags associated with the TlsRoute resource.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. Set of label tags associated with the TlsRoute resource.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMeshes(int index)
    
    
    public abstract String getMeshes(int index)

Optional. Meshes defines a list of meshes this TlsRoute is attached to, as one of the routing rules to route the requests served by the mesh.

Each mesh reference should match the pattern: `projects/*/locations/*/meshes/<mesh_name>`

The attached Mesh should be of a type SIDECAR

` repeated string meshes = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The meshes at the given index.  
  
### getMeshesBytes(int index)
    
    
    public abstract ByteString getMeshesBytes(int index)

Optional. Meshes defines a list of meshes this TlsRoute is attached to, as one of the routing rules to route the requests served by the mesh.

Each mesh reference should match the pattern: `projects/*/locations/*/meshes/<mesh_name>`

The attached Mesh should be of a type SIDECAR

` repeated string meshes = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the meshes at the given index.  
  
### getMeshesCount()
    
    
    public abstract int getMeshesCount()

Optional. Meshes defines a list of meshes this TlsRoute is attached to, as one of the routing rules to route the requests served by the mesh.

Each mesh reference should match the pattern: `projects/*/locations/*/meshes/<mesh_name>`

The attached Mesh should be of a type SIDECAR

` repeated string meshes = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of meshes.  
  
### getMeshesList()
    
    
    public abstract List<String> getMeshesList()

Optional. Meshes defines a list of meshes this TlsRoute is attached to, as one of the routing rules to route the requests served by the mesh.

Each mesh reference should match the pattern: `projects/*/locations/*/meshes/<mesh_name>`

The attached Mesh should be of a type SIDECAR

` repeated string meshes = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the meshes.  
  
### getName()
    
    
    public abstract String getName()

Identifier. Name of the TlsRoute resource. It matches pattern `projects/*/locations/*/tlsRoutes/tls_route_name>`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Name of the TlsRoute resource. It matches pattern `projects/*/locations/*/tlsRoutes/tls_route_name>`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRules(int index)
    
    
    public abstract TlsRoute.RouteRule getRules(int index)

Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.

` repeated .google.cloud.networkservices.v1.TlsRoute.RouteRule rules = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TlsRoute.RouteRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute.RouteRule)` |   
  
### getRulesCount()
    
    
    public abstract int getRulesCount()

Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.

` repeated .google.cloud.networkservices.v1.TlsRoute.RouteRule rules = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRulesList()
    
    
    public abstract List<TlsRoute.RouteRule> getRulesList()

Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.

` repeated .google.cloud.networkservices.v1.TlsRoute.RouteRule rules = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RouteRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute.RouteRule)>` |   
  
### getRulesOrBuilder(int index)
    
    
    public abstract TlsRoute.RouteRuleOrBuilder getRulesOrBuilder(int index)

Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.

` repeated .google.cloud.networkservices.v1.TlsRoute.RouteRule rules = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TlsRoute.RouteRuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute.RouteRuleOrBuilder)` |   
  
### getRulesOrBuilderList()
    
    
    public abstract List<? extends TlsRoute.RouteRuleOrBuilder> getRulesOrBuilderList()

Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.

` repeated .google.cloud.networkservices.v1.TlsRoute.RouteRule rules = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.networkservices.v1.TlsRoute.RouteRuleOrBuilder>` |   
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. Server-defined URL of this resource

`string self_link = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. Server-defined URL of this resource

`string self_link = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getTargetProxies(int index)
    
    
    public abstract String getTargetProxies(int index)

Optional. TargetProxies defines a list of TargetTcpProxies this TlsRoute is attached to, as one of the routing rules to route the requests served by the TargetTcpProxy.

Each TargetTcpProxy reference should match the pattern: `projects/*/locations/*/targetTcpProxies/<target_tcp_proxy_name>`

` repeated string target_proxies = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetProxies at the given index.  
  
### getTargetProxiesBytes(int index)
    
    
    public abstract ByteString getTargetProxiesBytes(int index)

Optional. TargetProxies defines a list of TargetTcpProxies this TlsRoute is attached to, as one of the routing rules to route the requests served by the TargetTcpProxy.

Each TargetTcpProxy reference should match the pattern: `projects/*/locations/*/targetTcpProxies/<target_tcp_proxy_name>`

` repeated string target_proxies = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the targetProxies at the given index.  
  
### getTargetProxiesCount()
    
    
    public abstract int getTargetProxiesCount()

Optional. TargetProxies defines a list of TargetTcpProxies this TlsRoute is attached to, as one of the routing rules to route the requests served by the TargetTcpProxy.

Each TargetTcpProxy reference should match the pattern: `projects/*/locations/*/targetTcpProxies/<target_tcp_proxy_name>`

` repeated string target_proxies = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of targetProxies.  
  
### getTargetProxiesList()
    
    
    public abstract List<String> getTargetProxiesList()

Optional. TargetProxies defines a list of TargetTcpProxies this TlsRoute is attached to, as one of the routing rules to route the requests served by the TargetTcpProxy.

Each TargetTcpProxy reference should match the pattern: `projects/*/locations/*/targetTcpProxies/<target_tcp_proxy_name>`

` repeated string target_proxies = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the targetProxies.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
