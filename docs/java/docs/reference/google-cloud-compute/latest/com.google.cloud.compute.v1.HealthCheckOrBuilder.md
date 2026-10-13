---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthCheckOrBuilder
title: Interface HealthCheckOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:45.777102+00:00
---

# Interface HealthCheckOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthCheckOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HealthCheckOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface HealthCheckOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCheckIntervalSec()
    
    
    public abstract int getCheckIntervalSec()

How often (in seconds) to send a health check. The default value is 5 seconds.

`optional int32 check_interval_sec = 345561006;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The checkIntervalSec.  
  
### getCreationTimestamp()
    
    
    public abstract String getCreationTimestamp()

Output only. [Output Only] Creation timestamp in3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The creationTimestamp.  
  
### getCreationTimestampBytes()
    
    
    public abstract ByteString getCreationTimestampBytes()

Output only. [Output Only] Creation timestamp in3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for creationTimestamp.  
  
### getDescription()
    
    
    public abstract String getDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getGrpcHealthCheck()
    
    
    public abstract GRPCHealthCheck getGrpcHealthCheck()

`optional .google.cloud.compute.v1.GRPCHealthCheck grpc_health_check = 85529574;`

**Returns**  
---  
**Type** | **Description**  
`[GRPCHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GRPCHealthCheck)` | The grpcHealthCheck.  
  
### getGrpcHealthCheckOrBuilder()
    
    
    public abstract GRPCHealthCheckOrBuilder getGrpcHealthCheckOrBuilder()

`optional .google.cloud.compute.v1.GRPCHealthCheck grpc_health_check = 85529574;`

**Returns**  
---  
**Type** | **Description**  
`[GRPCHealthCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GRPCHealthCheckOrBuilder)` |   
  
### getGrpcTlsHealthCheck()
    
    
    public abstract GRPCTLSHealthCheck getGrpcTlsHealthCheck()

`optional .google.cloud.compute.v1.GRPCTLSHealthCheck grpc_tls_health_check = 267273258; `

**Returns**  
---  
**Type** | **Description**  
`[GRPCTLSHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GRPCTLSHealthCheck)` | The grpcTlsHealthCheck.  
  
### getGrpcTlsHealthCheckOrBuilder()
    
    
    public abstract GRPCTLSHealthCheckOrBuilder getGrpcTlsHealthCheckOrBuilder()

`optional .google.cloud.compute.v1.GRPCTLSHealthCheck grpc_tls_health_check = 267273258; `

**Returns**  
---  
**Type** | **Description**  
`[GRPCTLSHealthCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GRPCTLSHealthCheckOrBuilder)` |   
  
### getHealthyThreshold()
    
    
    public abstract int getHealthyThreshold()

A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.

`optional int32 healthy_threshold = 403212361;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The healthyThreshold.  
  
### getHttp2HealthCheck()
    
    
    public abstract HTTP2HealthCheck getHttp2HealthCheck()

`optional .google.cloud.compute.v1.HTTP2HealthCheck http2_health_check = 11360986;`

**Returns**  
---  
**Type** | **Description**  
`[HTTP2HealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HTTP2HealthCheck)` | The http2HealthCheck.  
  
### getHttp2HealthCheckOrBuilder()
    
    
    public abstract HTTP2HealthCheckOrBuilder getHttp2HealthCheckOrBuilder()

`optional .google.cloud.compute.v1.HTTP2HealthCheck http2_health_check = 11360986;`

**Returns**  
---  
**Type** | **Description**  
`[HTTP2HealthCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HTTP2HealthCheckOrBuilder)` |   
  
### getHttpHealthCheck()
    
    
    public abstract HTTPHealthCheck getHttpHealthCheck()

`optional .google.cloud.compute.v1.HTTPHealthCheck http_health_check = 412586940;`

**Returns**  
---  
**Type** | **Description**  
`[HTTPHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HTTPHealthCheck)` | The httpHealthCheck.  
  
### getHttpHealthCheckOrBuilder()
    
    
    public abstract HTTPHealthCheckOrBuilder getHttpHealthCheckOrBuilder()

`optional .google.cloud.compute.v1.HTTPHealthCheck http_health_check = 412586940;`

**Returns**  
---  
**Type** | **Description**  
`[HTTPHealthCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HTTPHealthCheckOrBuilder)` |   
  
### getHttpsHealthCheck()
    
    
    public abstract HTTPSHealthCheck getHttpsHealthCheck()

`optional .google.cloud.compute.v1.HTTPSHealthCheck https_health_check = 436046905;`

**Returns**  
---  
**Type** | **Description**  
`[HTTPSHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HTTPSHealthCheck)` | The httpsHealthCheck.  
  
### getHttpsHealthCheckOrBuilder()
    
    
    public abstract HTTPSHealthCheckOrBuilder getHttpsHealthCheckOrBuilder()

`optional .google.cloud.compute.v1.HTTPSHealthCheck https_health_check = 436046905;`

**Returns**  
---  
**Type** | **Description**  
`[HTTPSHealthCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HTTPSHealthCheckOrBuilder)` |   
  
### getId()
    
    
    public abstract long getId()

[Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getKind()
    
    
    public abstract String getKind()

Output only. Type of the resource.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. Type of the resource.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getLogConfig()
    
    
    public abstract HealthCheckLogConfig getLogConfig()

Configure logging on this health check.

`optional .google.cloud.compute.v1.HealthCheckLogConfig log_config = 351299741;`

**Returns**  
---  
**Type** | **Description**  
`[HealthCheckLogConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthCheckLogConfig)` | The logConfig.  
  
### getLogConfigOrBuilder()
    
    
    public abstract HealthCheckLogConfigOrBuilder getLogConfigOrBuilder()

Configure logging on this health check.

`optional .google.cloud.compute.v1.HealthCheckLogConfig log_config = 351299741;`

**Returns**  
---  
**Type** | **Description**  
`[HealthCheckLogConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthCheckLogConfigOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRegion()
    
    
    public abstract String getRegion()

Output only. [Output Only] Region where the health check resides. Not applicable to global health checks.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The region.  
  
### getRegionBytes()
    
    
    public abstract ByteString getRegionBytes()

Output only. [Output Only] Region where the health check resides. Not applicable to global health checks.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for region.  
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

[Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

[Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getSourceRegions(int index)
    
    
    public abstract String getSourceRegions(int index)

The list of cloud regions from which health checks are performed. If any regions are specified, then exactly 3 regions should be specified. The region names must be valid names of Google Cloud regions. This can only be set for global health check. If this list is non-empty, then there are restrictions on what other health check fields are supported and what other resources can use this health check:

  * SSL, HTTP2, GRPC, and GRPC_WITH_TLS protocols are not supported.
  * The TCP request field is not supported.
  * The proxyHeader field for HTTP, HTTPS, and TCP is not supported.
  * The checkIntervalSec field must be at least 30.
  * The health check cannot be used with BackendService nor with managed instance group auto-healing.



`repeated string source_regions = 405568475;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceRegions at the given index.  
  
### getSourceRegionsBytes(int index)
    
    
    public abstract ByteString getSourceRegionsBytes(int index)

The list of cloud regions from which health checks are performed. If any regions are specified, then exactly 3 regions should be specified. The region names must be valid names of Google Cloud regions. This can only be set for global health check. If this list is non-empty, then there are restrictions on what other health check fields are supported and what other resources can use this health check:

  * SSL, HTTP2, GRPC, and GRPC_WITH_TLS protocols are not supported.
  * The TCP request field is not supported.
  * The proxyHeader field for HTTP, HTTPS, and TCP is not supported.
  * The checkIntervalSec field must be at least 30.
  * The health check cannot be used with BackendService nor with managed instance group auto-healing.



`repeated string source_regions = 405568475;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the sourceRegions at the given index.  
  
### getSourceRegionsCount()
    
    
    public abstract int getSourceRegionsCount()

The list of cloud regions from which health checks are performed. If any regions are specified, then exactly 3 regions should be specified. The region names must be valid names of Google Cloud regions. This can only be set for global health check. If this list is non-empty, then there are restrictions on what other health check fields are supported and what other resources can use this health check:

  * SSL, HTTP2, GRPC, and GRPC_WITH_TLS protocols are not supported.
  * The TCP request field is not supported.
  * The proxyHeader field for HTTP, HTTPS, and TCP is not supported.
  * The checkIntervalSec field must be at least 30.
  * The health check cannot be used with BackendService nor with managed instance group auto-healing.



`repeated string source_regions = 405568475;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of sourceRegions.  
  
### getSourceRegionsList()
    
    
    public abstract List<String> getSourceRegionsList()

The list of cloud regions from which health checks are performed. If any regions are specified, then exactly 3 regions should be specified. The region names must be valid names of Google Cloud regions. This can only be set for global health check. If this list is non-empty, then there are restrictions on what other health check fields are supported and what other resources can use this health check:

  * SSL, HTTP2, GRPC, and GRPC_WITH_TLS protocols are not supported.
  * The TCP request field is not supported.
  * The proxyHeader field for HTTP, HTTPS, and TCP is not supported.
  * The checkIntervalSec field must be at least 30.
  * The health check cannot be used with BackendService nor with managed instance group auto-healing.



`repeated string source_regions = 405568475;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the sourceRegions.  
  
### getSslHealthCheck()
    
    
    public abstract SSLHealthCheck getSslHealthCheck()

`optional .google.cloud.compute.v1.SSLHealthCheck ssl_health_check = 280032440;`

**Returns**  
---  
**Type** | **Description**  
`[SSLHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SSLHealthCheck)` | The sslHealthCheck.  
  
### getSslHealthCheckOrBuilder()
    
    
    public abstract SSLHealthCheckOrBuilder getSslHealthCheckOrBuilder()

`optional .google.cloud.compute.v1.SSLHealthCheck ssl_health_check = 280032440;`

**Returns**  
---  
**Type** | **Description**  
`[SSLHealthCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SSLHealthCheckOrBuilder)` |   
  
### getTcpHealthCheck()
    
    
    public abstract TCPHealthCheck getTcpHealthCheck()

`optional .google.cloud.compute.v1.TCPHealthCheck tcp_health_check = 469980419;`

**Returns**  
---  
**Type** | **Description**  
`[TCPHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TCPHealthCheck)` | The tcpHealthCheck.  
  
### getTcpHealthCheckOrBuilder()
    
    
    public abstract TCPHealthCheckOrBuilder getTcpHealthCheckOrBuilder()

`optional .google.cloud.compute.v1.TCPHealthCheck tcp_health_check = 469980419;`

**Returns**  
---  
**Type** | **Description**  
`[TCPHealthCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TCPHealthCheckOrBuilder)` |   
  
### getTimeoutSec()
    
    
    public abstract int getTimeoutSec()

How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.

`optional int32 timeout_sec = 79994995;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The timeoutSec.  
  
### getType()
    
    
    public abstract String getType()

Specifies the type of the healthCheck, either TCP,SSL, HTTP, HTTPS,HTTP2, GRPC or GRPC_WITH_TLS. Exactly one of the protocol-specific health check fields must be specified, which must match type field. Check the Type enum for the list of possible values.

`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The type.  
  
### getTypeBytes()
    
    
    public abstract ByteString getTypeBytes()

Specifies the type of the healthCheck, either TCP,SSL, HTTP, HTTPS,HTTP2, GRPC or GRPC_WITH_TLS. Exactly one of the protocol-specific health check fields must be specified, which must match type field. Check the Type enum for the list of possible values.

`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for type.  
  
### getUnhealthyThreshold()
    
    
    public abstract int getUnhealthyThreshold()

A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.

`optional int32 unhealthy_threshold = 227958480;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The unhealthyThreshold.  
  
### hasCheckIntervalSec()
    
    
    public abstract boolean hasCheckIntervalSec()

How often (in seconds) to send a health check. The default value is 5 seconds.

`optional int32 check_interval_sec = 345561006;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the checkIntervalSec field is set.  
  
### hasCreationTimestamp()
    
    
    public abstract boolean hasCreationTimestamp()

Output only. [Output Only] Creation timestamp in3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTimestamp field is set.  
  
### hasDescription()
    
    
    public abstract boolean hasDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasGrpcHealthCheck()
    
    
    public abstract boolean hasGrpcHealthCheck()

`optional .google.cloud.compute.v1.GRPCHealthCheck grpc_health_check = 85529574;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the grpcHealthCheck field is set.  
  
### hasGrpcTlsHealthCheck()
    
    
    public abstract boolean hasGrpcTlsHealthCheck()

`optional .google.cloud.compute.v1.GRPCTLSHealthCheck grpc_tls_health_check = 267273258; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the grpcTlsHealthCheck field is set.  
  
### hasHealthyThreshold()
    
    
    public abstract boolean hasHealthyThreshold()

A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.

`optional int32 healthy_threshold = 403212361;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the healthyThreshold field is set.  
  
### hasHttp2HealthCheck()
    
    
    public abstract boolean hasHttp2HealthCheck()

`optional .google.cloud.compute.v1.HTTP2HealthCheck http2_health_check = 11360986;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the http2HealthCheck field is set.  
  
### hasHttpHealthCheck()
    
    
    public abstract boolean hasHttpHealthCheck()

`optional .google.cloud.compute.v1.HTTPHealthCheck http_health_check = 412586940;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the httpHealthCheck field is set.  
  
### hasHttpsHealthCheck()
    
    
    public abstract boolean hasHttpsHealthCheck()

`optional .google.cloud.compute.v1.HTTPSHealthCheck https_health_check = 436046905;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the httpsHealthCheck field is set.  
  
### hasId()
    
    
    public abstract boolean hasId()

[Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasKind()
    
    
    public abstract boolean hasKind()

Output only. Type of the resource.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasLogConfig()
    
    
    public abstract boolean hasLogConfig()

Configure logging on this health check.

`optional .google.cloud.compute.v1.HealthCheckLogConfig log_config = 351299741;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the logConfig field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/\[-a-z0-9\]*\[a-z0-9\])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasRegion()
    
    
    public abstract boolean hasRegion()

Output only. [Output Only] Region where the health check resides. Not applicable to global health checks.

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the region field is set.  
  
### hasSelfLink()
    
    
    public abstract boolean hasSelfLink()

[Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasSslHealthCheck()
    
    
    public abstract boolean hasSslHealthCheck()

`optional .google.cloud.compute.v1.SSLHealthCheck ssl_health_check = 280032440;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sslHealthCheck field is set.  
  
### hasTcpHealthCheck()
    
    
    public abstract boolean hasTcpHealthCheck()

`optional .google.cloud.compute.v1.TCPHealthCheck tcp_health_check = 469980419;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tcpHealthCheck field is set.  
  
### hasTimeoutSec()
    
    
    public abstract boolean hasTimeoutSec()

How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.

`optional int32 timeout_sec = 79994995;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeoutSec field is set.  
  
### hasType()
    
    
    public abstract boolean hasType()

Specifies the type of the healthCheck, either TCP,SSL, HTTP, HTTPS,HTTP2, GRPC or GRPC_WITH_TLS. Exactly one of the protocol-specific health check fields must be specified, which must match type field. Check the Type enum for the list of possible values.

`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the type field is set.  
  
### hasUnhealthyThreshold()
    
    
    public abstract boolean hasUnhealthyThreshold()

A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.

`optional int32 unhealthy_threshold = 227958480;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the unhealthyThreshold field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
