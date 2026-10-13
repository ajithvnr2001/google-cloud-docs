---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.CreateVpnConnectionRequestOrBuilder
title: Interface CreateVpnConnectionRequestOrBuilder (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:01.307562+00:00
---

# Interface CreateVpnConnectionRequestOrBuilder (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.CreateVpnConnectionRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateVpnConnectionRequestOrBuilder (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CreateVpnConnectionRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getParent()
    
    
    public abstract String getParent()

Required. The parent location where this vpn connection will be created.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent location where this vpn connection will be created.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRequestId()
    
    
    public abstract String getRequestId()

A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.

`string request_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided.

`string request_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### getVpnConnection()
    
    
    public abstract VpnConnection getVpnConnection()

Required. The VPN connection to create.

` .google.cloud.edgecontainer.v1.VpnConnection vpn_connection = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[VpnConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.VpnConnection)` | The vpnConnection.  
  
### getVpnConnectionId()
    
    
    public abstract String getVpnConnectionId()

Required. The VPN connection identifier.

`string vpn_connection_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The vpnConnectionId.  
  
### getVpnConnectionIdBytes()
    
    
    public abstract ByteString getVpnConnectionIdBytes()

Required. The VPN connection identifier.

`string vpn_connection_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for vpnConnectionId.  
  
### getVpnConnectionOrBuilder()
    
    
    public abstract VpnConnectionOrBuilder getVpnConnectionOrBuilder()

Required. The VPN connection to create.

` .google.cloud.edgecontainer.v1.VpnConnection vpn_connection = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[VpnConnectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.VpnConnectionOrBuilder)` |   
  
### hasVpnConnection()
    
    
    public abstract boolean hasVpnConnection()

Required. The VPN connection to create.

` .google.cloud.edgecontainer.v1.VpnConnection vpn_connection = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vpnConnection field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
