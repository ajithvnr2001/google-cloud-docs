---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.audit.v1.RequestMetadataOrBuilder
title: Interface RequestMetadataOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:20.371068+00:00
---

# Interface RequestMetadataOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.audit.v1.RequestMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RequestMetadataOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.audit.v1.RequestMetadataOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.audit.v1.RequestMetadataOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.audit.v1.RequestMetadataOrBuilder)


    
    
    public interface RequestMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCallerIp()
    
    
    public abstract String getCallerIp()

The IP address of the caller. For caller from internet, this will be public IPv4 or IPv6 address. For caller from a Compute Engine VM with external IP address, this will be the VM's external IP address. For caller from a Compute Engine VM without external IP address, if the VM is in the same organization (or project) as the accessed resource, `caller_ip` will be the VM's internal IPv4 address, otherwise the `caller_ip` will be redacted to "gce-internal-ip". See <https://cloud.google.com/compute/docs/vpc/> for more information.

`string caller_ip = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The callerIp.  
  
### getCallerIpBytes()
    
    
    public abstract ByteString getCallerIpBytes()

The IP address of the caller. For caller from internet, this will be public IPv4 or IPv6 address. For caller from a Compute Engine VM with external IP address, this will be the VM's external IP address. For caller from a Compute Engine VM without external IP address, if the VM is in the same organization (or project) as the accessed resource, `caller_ip` will be the VM's internal IPv4 address, otherwise the `caller_ip` will be redacted to "gce-internal-ip". See <https://cloud.google.com/compute/docs/vpc/> for more information.

`string caller_ip = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for callerIp.  
  
### getCallerNetwork()
    
    
    public abstract String getCallerNetwork()

The network of the caller. Set only if the network host project is part of the same GCP organization (or project) as the accessed resource. See <https://cloud.google.com/compute/docs/vpc/> for more information. This is a scheme-less URI full resource name. For example: "//compute.googleapis.com/projects/PROJECT_ID/global/networks/NETWORK_ID"

`string caller_network = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The callerNetwork.  
  
### getCallerNetworkBytes()
    
    
    public abstract ByteString getCallerNetworkBytes()

The network of the caller. Set only if the network host project is part of the same GCP organization (or project) as the accessed resource. See <https://cloud.google.com/compute/docs/vpc/> for more information. This is a scheme-less URI full resource name. For example: "//compute.googleapis.com/projects/PROJECT_ID/global/networks/NETWORK_ID"

`string caller_network = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for callerNetwork.  
  
### getCallerSuppliedUserAgent()
    
    
    public abstract String getCallerSuppliedUserAgent()

The user agent of the caller. This information is not authenticated and should be treated accordingly. For example:

  * `google-api-python-client/1.4.0`: The request was made by the Google API client for Python.
  * `Cloud SDK Command Line Tool apitools-client/1.0 gcloud/0.9.62`: The request was made by the Google Cloud SDK CLI (gcloud).
  * `AppEngine-Google; (+<http://code.google.com/appengine>; appid: s~my-project`: The request was made from the `my-project` App Engine app.



`string caller_supplied_user_agent = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The callerSuppliedUserAgent.  
  
### getCallerSuppliedUserAgentBytes()
    
    
    public abstract ByteString getCallerSuppliedUserAgentBytes()

The user agent of the caller. This information is not authenticated and should be treated accordingly. For example:

  * `google-api-python-client/1.4.0`: The request was made by the Google API client for Python.
  * `Cloud SDK Command Line Tool apitools-client/1.0 gcloud/0.9.62`: The request was made by the Google Cloud SDK CLI (gcloud).
  * `AppEngine-Google; (+<http://code.google.com/appengine>; appid: s~my-project`: The request was made from the `my-project` App Engine app.



`string caller_supplied_user_agent = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for callerSuppliedUserAgent.  
  
### getDestinationAttributes()
    
    
    public abstract AttributeContext.Peer getDestinationAttributes()

The destination of a network activity, such as accepting a TCP connection. In a multi hop network activity, the destination represents the receiver of the last hop. Only two fields are used in this message, Peer.port and Peer.ip. These fields are optionally populated by those services utilizing the IAM condition feature.

`.google.rpc.context.AttributeContext.Peer destination_attributes = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.context.AttributeContext.Peer` | The destinationAttributes.  
  
### getDestinationAttributesOrBuilder()
    
    
    public abstract AttributeContext.PeerOrBuilder getDestinationAttributesOrBuilder()

The destination of a network activity, such as accepting a TCP connection. In a multi hop network activity, the destination represents the receiver of the last hop. Only two fields are used in this message, Peer.port and Peer.ip. These fields are optionally populated by those services utilizing the IAM condition feature.

`.google.rpc.context.AttributeContext.Peer destination_attributes = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.context.AttributeContext.PeerOrBuilder` |   
  
### getRequestAttributes()
    
    
    public abstract AttributeContext.Request getRequestAttributes()

Request attributes used in IAM condition evaluation. This field contains request attributes like request time and access levels associated with the request. To get the whole view of the attributes used in IAM condition evaluation, the user must also look into `AuditLog.authentication_info.resource_attributes`.

`.google.rpc.context.AttributeContext.Request request_attributes = 7;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.context.AttributeContext.Request` | The requestAttributes.  
  
### getRequestAttributesOrBuilder()
    
    
    public abstract AttributeContext.RequestOrBuilder getRequestAttributesOrBuilder()

Request attributes used in IAM condition evaluation. This field contains request attributes like request time and access levels associated with the request. To get the whole view of the attributes used in IAM condition evaluation, the user must also look into `AuditLog.authentication_info.resource_attributes`.

`.google.rpc.context.AttributeContext.Request request_attributes = 7;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.context.AttributeContext.RequestOrBuilder` |   
  
### hasDestinationAttributes()
    
    
    public abstract boolean hasDestinationAttributes()

The destination of a network activity, such as accepting a TCP connection. In a multi hop network activity, the destination represents the receiver of the last hop. Only two fields are used in this message, Peer.port and Peer.ip. These fields are optionally populated by those services utilizing the IAM condition feature.

`.google.rpc.context.AttributeContext.Peer destination_attributes = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the destinationAttributes field is set.  
  
### hasRequestAttributes()
    
    
    public abstract boolean hasRequestAttributes()

Request attributes used in IAM condition evaluation. This field contains request attributes like request time and access levels associated with the request. To get the whole view of the attributes used in IAM condition evaluation, the user must also look into `AuditLog.authentication_info.resource_attributes`.

`.google.rpc.context.AttributeContext.Request request_attributes = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the requestAttributes field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
