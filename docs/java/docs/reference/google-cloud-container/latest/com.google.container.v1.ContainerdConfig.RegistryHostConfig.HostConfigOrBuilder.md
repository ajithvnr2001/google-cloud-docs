---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.HostConfigOrBuilder
title: Interface ContainerdConfig.RegistryHostConfig.HostConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:10.423611+00:00
---

# Interface ContainerdConfig.RegistryHostConfig.HostConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.HostConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ContainerdConfig.RegistryHostConfig.HostConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public static interface ContainerdConfig.RegistryHostConfig.HostConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCa(int index)
    
    
    public abstract ContainerdConfig.RegistryHostConfig.CertificateConfig getCa(int index)

CA configures the registry host certificate.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfig ca = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig.RegistryHostConfig.CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfig)` |   
  
### getCaCount()
    
    
    public abstract int getCaCount()

CA configures the registry host certificate.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfig ca = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCaList()
    
    
    public abstract List<ContainerdConfig.RegistryHostConfig.CertificateConfig> getCaList()

CA configures the registry host certificate.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfig ca = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfig)>` |   
  
### getCaOrBuilder(int index)
    
    
    public abstract ContainerdConfig.RegistryHostConfig.CertificateConfigOrBuilder getCaOrBuilder(int index)

CA configures the registry host certificate.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfig ca = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig.RegistryHostConfig.CertificateConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigOrBuilder)` |   
  
### getCaOrBuilderList()
    
    
    public abstract List<? extends ContainerdConfig.RegistryHostConfig.CertificateConfigOrBuilder> getCaOrBuilderList()

CA configures the registry host certificate.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfig ca = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigOrBuilder>` |   
  
### getCapabilities(int index)
    
    
    public abstract ContainerdConfig.RegistryHostConfig.HostCapability getCapabilities(int index)

Capabilities represent the capabilities of the registry host, specifying what operations a host is capable of performing. If not set, containerd enables all capabilities by default.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.HostCapability capabilities = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig.RegistryHostConfig.HostCapability](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.HostCapability)` | The capabilities at the given index.  
  
### getCapabilitiesCount()
    
    
    public abstract int getCapabilitiesCount()

Capabilities represent the capabilities of the registry host, specifying what operations a host is capable of performing. If not set, containerd enables all capabilities by default.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.HostCapability capabilities = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of capabilities.  
  
### getCapabilitiesList()
    
    
    public abstract List<ContainerdConfig.RegistryHostConfig.HostCapability> getCapabilitiesList()

Capabilities represent the capabilities of the registry host, specifying what operations a host is capable of performing. If not set, containerd enables all capabilities by default.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.HostCapability capabilities = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HostCapability](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.HostCapability)>` | A list containing the capabilities.  
  
### getCapabilitiesValue(int index)
    
    
    public abstract int getCapabilitiesValue(int index)

Capabilities represent the capabilities of the registry host, specifying what operations a host is capable of performing. If not set, containerd enables all capabilities by default.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.HostCapability capabilities = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of capabilities at the given index.  
  
### getCapabilitiesValueList()
    
    
    public abstract List<Integer> getCapabilitiesValueList()

Capabilities represent the capabilities of the registry host, specifying what operations a host is capable of performing. If not set, containerd enables all capabilities by default.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.HostCapability capabilities = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for capabilities.  
  
### getClient(int index)
    
    
    public abstract ContainerdConfig.RegistryHostConfig.CertificateConfigPair getClient(int index)

Client configures the registry host client certificate and key.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPair client = 6; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig.RegistryHostConfig.CertificateConfigPair](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPair)` |   
  
### getClientCount()
    
    
    public abstract int getClientCount()

Client configures the registry host client certificate and key.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPair client = 6; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getClientList()
    
    
    public abstract List<ContainerdConfig.RegistryHostConfig.CertificateConfigPair> getClientList()

Client configures the registry host client certificate and key.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPair client = 6; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CertificateConfigPair](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPair)>` |   
  
### getClientOrBuilder(int index)
    
    
    public abstract ContainerdConfig.RegistryHostConfig.CertificateConfigPairOrBuilder getClientOrBuilder(int index)

Client configures the registry host client certificate and key.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPair client = 6; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig.RegistryHostConfig.CertificateConfigPairOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPairOrBuilder)` |   
  
### getClientOrBuilderList()
    
    
    public abstract List<? extends ContainerdConfig.RegistryHostConfig.CertificateConfigPairOrBuilder> getClientOrBuilderList()

Client configures the registry host client certificate and key.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPair client = 6; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.ContainerdConfig.RegistryHostConfig.CertificateConfigPairOrBuilder>` |   
  
### getDialTimeout()
    
    
    public abstract Duration getDialTimeout()

Specifies the maximum duration allowed for a connection attempt to complete. A shorter timeout helps reduce delays when falling back to the original registry if the mirror is unreachable. Maximum allowed value is 180s. If not set, containerd sets default 30s. The value should be a decimal number of seconds with an `s` suffix.

`.google.protobuf.Duration dial_timeout = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The dialTimeout.  
  
### getDialTimeoutOrBuilder()
    
    
    public abstract DurationOrBuilder getDialTimeoutOrBuilder()

Specifies the maximum duration allowed for a connection attempt to complete. A shorter timeout helps reduce delays when falling back to the original registry if the mirror is unreachable. Maximum allowed value is 180s. If not set, containerd sets default 30s. The value should be a decimal number of seconds with an `s` suffix.

`.google.protobuf.Duration dial_timeout = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getHeader(int index)
    
    
    public abstract ContainerdConfig.RegistryHostConfig.RegistryHeader getHeader(int index)

Header configures the registry host headers.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeader header = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig.RegistryHostConfig.RegistryHeader](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeader)` |   
  
### getHeaderCount()
    
    
    public abstract int getHeaderCount()

Header configures the registry host headers.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeader header = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeaderList()
    
    
    public abstract List<ContainerdConfig.RegistryHostConfig.RegistryHeader> getHeaderList()

Header configures the registry host headers.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeader header = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RegistryHeader](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeader)>` |   
  
### getHeaderOrBuilder(int index)
    
    
    public abstract ContainerdConfig.RegistryHostConfig.RegistryHeaderOrBuilder getHeaderOrBuilder(int index)

Header configures the registry host headers.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeader header = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig.RegistryHostConfig.RegistryHeaderOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeaderOrBuilder)` |   
  
### getHeaderOrBuilderList()
    
    
    public abstract List<? extends ContainerdConfig.RegistryHostConfig.RegistryHeaderOrBuilder> getHeaderOrBuilderList()

Header configures the registry host headers.

` repeated .google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeader header = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.ContainerdConfig.RegistryHostConfig.RegistryHeaderOrBuilder>` |   
  
### getHost()
    
    
    public abstract String getHost()

Host configures the registry host/mirror. It supports fully qualified domain names (FQDNs) and IP addresses. Specifying scheme, port or path is supported. Scheme can only be http or https. Wildcards are NOT supported. Examples:

  * `my.customdomain.com`
  * `<https://my.customdomain.com/path>`
  * `10.0.1.2:5000`



`string host = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The host.  
  
### getHostBytes()
    
    
    public abstract ByteString getHostBytes()

Host configures the registry host/mirror. It supports fully qualified domain names (FQDNs) and IP addresses. Specifying scheme, port or path is supported. Scheme can only be http or https. Wildcards are NOT supported. Examples:

  * `my.customdomain.com`
  * `<https://my.customdomain.com/path>`
  * `10.0.1.2:5000`



`string host = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for host.  
  
### getOverridePath()
    
    
    public abstract boolean getOverridePath()

OverridePath is used to indicate the host's API root endpoint is defined in the URL path rather than by the API specification. This may be used with non-compliant OCI registries which are missing the /v2 prefix. If not set, containerd sets default false.

`bool override_path = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The overridePath.  
  
### hasDialTimeout()
    
    
    public abstract boolean hasDialTimeout()

Specifies the maximum duration allowed for a connection attempt to complete. A shorter timeout helps reduce delays when falling back to the original registry if the mirror is unreachable. Maximum allowed value is 180s. If not set, containerd sets default 30s. The value should be a decimal number of seconds with an `s` suffix.

`.google.protobuf.Duration dial_timeout = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dialTimeout field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
