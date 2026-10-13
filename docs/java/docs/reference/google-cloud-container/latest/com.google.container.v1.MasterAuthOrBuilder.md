---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthOrBuilder
title: Interface MasterAuthOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:39.940669+00:00
---

# Interface MasterAuthOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MasterAuthOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MasterAuthOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface MasterAuthOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getClientCertificate()
    
    
    public abstract String getClientCertificate()

Output only. Base64-encoded public certificate used by clients to authenticate to the cluster endpoint. Issued only if client_certificate_config is set.

`string client_certificate = 101 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientCertificate.  
  
### getClientCertificateBytes()
    
    
    public abstract ByteString getClientCertificateBytes()

Output only. Base64-encoded public certificate used by clients to authenticate to the cluster endpoint. Issued only if client_certificate_config is set.

`string client_certificate = 101 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientCertificate.  
  
### getClientCertificateConfig()
    
    
    public abstract ClientCertificateConfig getClientCertificateConfig()

Configuration for client certificate authentication on the cluster. For clusters before v1.12, if no configuration is specified, a client certificate is issued.

`.google.container.v1.ClientCertificateConfig client_certificate_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ClientCertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClientCertificateConfig)` | The clientCertificateConfig.  
  
### getClientCertificateConfigOrBuilder()
    
    
    public abstract ClientCertificateConfigOrBuilder getClientCertificateConfigOrBuilder()

Configuration for client certificate authentication on the cluster. For clusters before v1.12, if no configuration is specified, a client certificate is issued.

`.google.container.v1.ClientCertificateConfig client_certificate_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ClientCertificateConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClientCertificateConfigOrBuilder)` |   
  
### getClientKey()
    
    
    public abstract String getClientKey()

Output only. Base64-encoded private key used by clients to authenticate to the cluster endpoint.

`string client_key = 102 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientKey.  
  
### getClientKeyBytes()
    
    
    public abstract ByteString getClientKeyBytes()

Output only. Base64-encoded private key used by clients to authenticate to the cluster endpoint.

`string client_key = 102 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientKey.  
  
### getClusterCaCertificate()
    
    
    public abstract String getClusterCaCertificate()

Output only. Base64-encoded public certificate that is the root of trust for the cluster.

`string cluster_ca_certificate = 100 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clusterCaCertificate.  
  
### getClusterCaCertificateBytes()
    
    
    public abstract ByteString getClusterCaCertificateBytes()

Output only. Base64-encoded public certificate that is the root of trust for the cluster.

`string cluster_ca_certificate = 100 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clusterCaCertificate.  
  
### getPassword() (deprecated)
    
    
    public abstract String getPassword()

**Deprecated.** _google.container.v1.MasterAuth.password is deprecated. See google/container/v1/cluster_service.proto;l=2243_

The password to use for HTTP basic authentication to the master endpoint. Because the master endpoint is open to the Internet, you should create a strong password. If a password is provided for cluster creation, username must be non-empty.

Warning: basic authentication is deprecated, and will be removed in GKE control plane versions 1.19 and newer. For a list of recommended authentication methods, see: <https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication>

`string password = 2 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The password.  
  
### getPasswordBytes() (deprecated)
    
    
    public abstract ByteString getPasswordBytes()

**Deprecated.** _google.container.v1.MasterAuth.password is deprecated. See google/container/v1/cluster_service.proto;l=2243_

The password to use for HTTP basic authentication to the master endpoint. Because the master endpoint is open to the Internet, you should create a strong password. If a password is provided for cluster creation, username must be non-empty.

Warning: basic authentication is deprecated, and will be removed in GKE control plane versions 1.19 and newer. For a list of recommended authentication methods, see: <https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication>

`string password = 2 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for password.  
  
### getUsername() (deprecated)
    
    
    public abstract String getUsername()

**Deprecated.** _google.container.v1.MasterAuth.username is deprecated. See google/container/v1/cluster_service.proto;l=2232_

The username to use for HTTP basic authentication to the master endpoint. For clusters v1.6.0 and later, basic authentication can be disabled by leaving username unspecified (or setting it to the empty string).

Warning: basic authentication is deprecated, and will be removed in GKE control plane versions 1.19 and newer. For a list of recommended authentication methods, see: <https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication>

`string username = 1 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The username.  
  
### getUsernameBytes() (deprecated)
    
    
    public abstract ByteString getUsernameBytes()

**Deprecated.** _google.container.v1.MasterAuth.username is deprecated. See google/container/v1/cluster_service.proto;l=2232_

The username to use for HTTP basic authentication to the master endpoint. For clusters v1.6.0 and later, basic authentication can be disabled by leaving username unspecified (or setting it to the empty string).

Warning: basic authentication is deprecated, and will be removed in GKE control plane versions 1.19 and newer. For a list of recommended authentication methods, see: <https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication>

`string username = 1 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for username.  
  
### hasClientCertificateConfig()
    
    
    public abstract boolean hasClientCertificateConfig()

Configuration for client certificate authentication on the cluster. For clusters before v1.12, if no configuration is specified, a client certificate is issued.

`.google.container.v1.ClientCertificateConfig client_certificate_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clientCertificateConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
