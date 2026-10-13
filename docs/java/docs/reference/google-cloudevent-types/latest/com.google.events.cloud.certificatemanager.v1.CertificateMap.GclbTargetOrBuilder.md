---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTargetOrBuilder
title: Interface CertificateMap.GclbTargetOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:05.037283+00:00
---

# Interface CertificateMap.GclbTargetOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTargetOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CertificateMap.GclbTargetOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTargetOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTargetOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTargetOrBuilder)


    
    
    public static interface CertificateMap.GclbTargetOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIpConfigs(int index)
    
    
    public abstract CertificateMap.GclbTarget.IpConfig getIpConfigs(int index)

Output only. IP configurations for this Target Proxy where the Certificate Map is serving.

` repeated .google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig ip_configs = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateMap.GclbTarget.IpConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig)` |   
  
### getIpConfigsCount()
    
    
    public abstract int getIpConfigsCount()

Output only. IP configurations for this Target Proxy where the Certificate Map is serving.

` repeated .google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig ip_configs = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getIpConfigsList()
    
    
    public abstract List<CertificateMap.GclbTarget.IpConfig> getIpConfigsList()

Output only. IP configurations for this Target Proxy where the Certificate Map is serving.

` repeated .google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig ip_configs = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[IpConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig)>` |   
  
### getIpConfigsOrBuilder(int index)
    
    
    public abstract CertificateMap.GclbTarget.IpConfigOrBuilder getIpConfigsOrBuilder(int index)

Output only. IP configurations for this Target Proxy where the Certificate Map is serving.

` repeated .google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig ip_configs = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateMap.GclbTarget.IpConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfigOrBuilder)` |   
  
### getIpConfigsOrBuilderList()
    
    
    public abstract List<? extends CertificateMap.GclbTarget.IpConfigOrBuilder> getIpConfigsOrBuilderList()

Output only. IP configurations for this Target Proxy where the Certificate Map is serving.

` repeated .google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig ip_configs = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfigOrBuilder>` |   
  
### getTargetHttpsProxy()
    
    
    public abstract String getTargetHttpsProxy()

Output only. This field returns the resource name in the following format: `//compute.googleapis.com/projects/*/global/targetHttpsProxies/*`.

`string target_https_proxy = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetHttpsProxy.  
  
### getTargetHttpsProxyBytes()
    
    
    public abstract ByteString getTargetHttpsProxyBytes()

Output only. This field returns the resource name in the following format: `//compute.googleapis.com/projects/*/global/targetHttpsProxies/*`.

`string target_https_proxy = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetHttpsProxy.  
  
### getTargetProxyCase()
    
    
    public abstract CertificateMap.GclbTarget.TargetProxyCase getTargetProxyCase()

**Returns**  
---  
**Type** | **Description**  
`[CertificateMap.GclbTarget.TargetProxyCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.certificatemanager.v1.CertificateMap.GclbTarget.TargetProxyCase)` |   
  
### getTargetSslProxy()
    
    
    public abstract String getTargetSslProxy()

Output only. This field returns the resource name in the following format: `//compute.googleapis.com/projects/*/global/targetSslProxies/*`.

`string target_ssl_proxy = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetSslProxy.  
  
### getTargetSslProxyBytes()
    
    
    public abstract ByteString getTargetSslProxyBytes()

Output only. This field returns the resource name in the following format: `//compute.googleapis.com/projects/*/global/targetSslProxies/*`.

`string target_ssl_proxy = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetSslProxy.  
  
### hasTargetHttpsProxy()
    
    
    public abstract boolean hasTargetHttpsProxy()

Output only. This field returns the resource name in the following format: `//compute.googleapis.com/projects/*/global/targetHttpsProxies/*`.

`string target_https_proxy = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the targetHttpsProxy field is set.  
  
### hasTargetSslProxy()
    
    
    public abstract boolean hasTargetSslProxy()

Output only. This field returns the resource name in the following format: `//compute.googleapis.com/projects/*/global/targetSslProxies/*`.

`string target_ssl_proxy = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the targetSslProxy field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
