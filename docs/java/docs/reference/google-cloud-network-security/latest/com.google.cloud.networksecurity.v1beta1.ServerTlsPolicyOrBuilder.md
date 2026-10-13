---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ServerTlsPolicyOrBuilder
title: Interface ServerTlsPolicyOrBuilder (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:28.757326+00:00
---

# Interface ServerTlsPolicyOrBuilder (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ServerTlsPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ServerTlsPolicyOrBuilder (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4  0.5.1  0.4.4 
    
    
    public interface ServerTlsPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Set of label tags associated with the resource.

`map<string, string> labels = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowOpen()
    
    
    public abstract boolean getAllowOpen()

Determines if server allows plaintext connections. If set to true, server allows plain text connections. By default, it is set to false. This setting is not exclusive of other encryption modes. For example, if `allow_open` and `mtls_policy` are set, server allows both plain text and mTLS connections. See documentation of other encryption modes to confirm compatibility.

Consider using it if you wish to upgrade in place your deployment to TLS while having mixed TLS and non-TLS traffic reaching port :80.

`bool allow_open = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowOpen.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Free-text description of the resource.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Free-text description of the resource.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ServerTlsPolicyOrBuilder#com_google_cloud_networksecurity_v1beta1_ServerTlsPolicyOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Set of label tags associated with the resource.

`map<string, string> labels = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Set of label tags associated with the resource.

`map<string, string> labels = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Set of label tags associated with the resource.

`map<string, string> labels = 5;`

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

Set of label tags associated with the resource.

`map<string, string> labels = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMtlsPolicy()
    
    
    public abstract ServerTlsPolicy.MTLSPolicy getMtlsPolicy()

Defines a mechanism to provision peer validation certificates for peer to peer authentication (Mutual TLS - mTLS). If not specified, client certificate will not be requested. The connection is treated as TLS and not mTLS. If `allow_open` and `mtls_policy` are set, server allows both plain text and mTLS connections.

`.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.MTLSPolicy mtls_policy = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ServerTlsPolicy.MTLSPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.MTLSPolicy)` | The mtlsPolicy.  
  
### getMtlsPolicyOrBuilder()
    
    
    public abstract ServerTlsPolicy.MTLSPolicyOrBuilder getMtlsPolicyOrBuilder()

Defines a mechanism to provision peer validation certificates for peer to peer authentication (Mutual TLS - mTLS). If not specified, client certificate will not be requested. The connection is treated as TLS and not mTLS. If `allow_open` and `mtls_policy` are set, server allows both plain text and mTLS connections.

`.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.MTLSPolicy mtls_policy = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ServerTlsPolicy.MTLSPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.MTLSPolicyOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Required. Name of the ServerTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/serverTlsPolicies/{server_tls_policy}`

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. Name of the ServerTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/serverTlsPolicies/{server_tls_policy}`

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getServerCertificate()
    
    
    public abstract CertificateProvider getServerCertificate()

Defines a mechanism to provision server identity (public and private keys). Cannot be combined with `allow_open` as a permissive mode that allows both plain text and TLS is not supported.

`.google.cloud.networksecurity.v1beta1.CertificateProvider server_certificate = 7;`

**Returns**  
---  
**Type** | **Description**  
`[CertificateProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CertificateProvider)` | The serverCertificate.  
  
### getServerCertificateOrBuilder()
    
    
    public abstract CertificateProviderOrBuilder getServerCertificateOrBuilder()

Defines a mechanism to provision server identity (public and private keys). Cannot be combined with `allow_open` as a permissive mode that allows both plain text and TLS is not supported.

`.google.cloud.networksecurity.v1beta1.CertificateProvider server_certificate = 7;`

**Returns**  
---  
**Type** | **Description**  
`[CertificateProviderOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CertificateProviderOrBuilder)` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasMtlsPolicy()
    
    
    public abstract boolean hasMtlsPolicy()

Defines a mechanism to provision peer validation certificates for peer to peer authentication (Mutual TLS - mTLS). If not specified, client certificate will not be requested. The connection is treated as TLS and not mTLS. If `allow_open` and `mtls_policy` are set, server allows both plain text and mTLS connections.

`.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.MTLSPolicy mtls_policy = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mtlsPolicy field is set.  
  
### hasServerCertificate()
    
    
    public abstract boolean hasServerCertificate()

Defines a mechanism to provision server identity (public and private keys). Cannot be combined with `allow_open` as a permissive mode that allows both plain text and TLS is not supported.

`.google.cloud.networksecurity.v1beta1.CertificateProvider server_certificate = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serverCertificate field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
