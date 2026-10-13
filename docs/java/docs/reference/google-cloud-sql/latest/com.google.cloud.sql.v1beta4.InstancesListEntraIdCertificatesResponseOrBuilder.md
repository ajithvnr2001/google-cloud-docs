---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.InstancesListEntraIdCertificatesResponseOrBuilder
title: Interface InstancesListEntraIdCertificatesResponseOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:57.934606+00:00
---

# Interface InstancesListEntraIdCertificatesResponseOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.InstancesListEntraIdCertificatesResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InstancesListEntraIdCertificatesResponseOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface InstancesListEntraIdCertificatesResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActiveVersion()
    
    
    public abstract String getActiveVersion()

The `sha1_fingerprint` of the active certificate from `certs`.

`string active_version = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The activeVersion.  
  
### getActiveVersionBytes()
    
    
    public abstract ByteString getActiveVersionBytes()

The `sha1_fingerprint` of the active certificate from `certs`.

`string active_version = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for activeVersion.  
  
### getCerts(int index)
    
    
    public abstract SslCert getCerts(int index)

List of Entra ID certificates for the instance.

`repeated .google.cloud.sql.v1beta4.SslCert certs = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SslCert](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SslCert)` |   
  
### getCertsCount()
    
    
    public abstract int getCertsCount()

List of Entra ID certificates for the instance.

`repeated .google.cloud.sql.v1beta4.SslCert certs = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCertsList()
    
    
    public abstract List<SslCert> getCertsList()

List of Entra ID certificates for the instance.

`repeated .google.cloud.sql.v1beta4.SslCert certs = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SslCert](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SslCert)>` |   
  
### getCertsOrBuilder(int index)
    
    
    public abstract SslCertOrBuilder getCertsOrBuilder(int index)

List of Entra ID certificates for the instance.

`repeated .google.cloud.sql.v1beta4.SslCert certs = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SslCertOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SslCertOrBuilder)` |   
  
### getCertsOrBuilderList()
    
    
    public abstract List<? extends SslCertOrBuilder> getCertsOrBuilderList()

List of Entra ID certificates for the instance.

`repeated .google.cloud.sql.v1beta4.SslCert certs = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.sql.v1beta4.SslCertOrBuilder>` |   
  
### getKind()
    
    
    public abstract String getKind()

This is always `sql#instancesListEntraIdCertificates`.

`string kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

This is always `sql#instancesListEntraIdCertificates`.

`string kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
