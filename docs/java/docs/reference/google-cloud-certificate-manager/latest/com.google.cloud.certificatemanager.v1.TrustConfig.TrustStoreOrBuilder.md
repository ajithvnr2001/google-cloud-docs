---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig.TrustStoreOrBuilder
title: Interface TrustConfig.TrustStoreOrBuilder (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:40.448195+00:00
---

# Interface TrustConfig.TrustStoreOrBuilder (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig.TrustStoreOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TrustConfig.TrustStoreOrBuilder (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.2  0.4.0  0.3.1  0.2.0  0.1.1 
    
    
    public static interface TrustConfig.TrustStoreOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIntermediateCas(int index)
    
    
    public abstract TrustConfig.IntermediateCA getIntermediateCas(int index)

Set of intermediate CA certificates used for the path building phase of chain validation.

The field is currently not supported if TrustConfig is used for the workload certificate feature.

` repeated .google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA intermediate_cas = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TrustConfig.IntermediateCA](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA)` |   
  
### getIntermediateCasCount()
    
    
    public abstract int getIntermediateCasCount()

Set of intermediate CA certificates used for the path building phase of chain validation.

The field is currently not supported if TrustConfig is used for the workload certificate feature.

` repeated .google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA intermediate_cas = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getIntermediateCasList()
    
    
    public abstract List<TrustConfig.IntermediateCA> getIntermediateCasList()

Set of intermediate CA certificates used for the path building phase of chain validation.

The field is currently not supported if TrustConfig is used for the workload certificate feature.

` repeated .google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA intermediate_cas = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[IntermediateCA](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA)>` |   
  
### getIntermediateCasOrBuilder(int index)
    
    
    public abstract TrustConfig.IntermediateCAOrBuilder getIntermediateCasOrBuilder(int index)

Set of intermediate CA certificates used for the path building phase of chain validation.

The field is currently not supported if TrustConfig is used for the workload certificate feature.

` repeated .google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA intermediate_cas = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TrustConfig.IntermediateCAOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig.IntermediateCAOrBuilder)` |   
  
### getIntermediateCasOrBuilderList()
    
    
    public abstract List<? extends TrustConfig.IntermediateCAOrBuilder> getIntermediateCasOrBuilderList()

Set of intermediate CA certificates used for the path building phase of chain validation.

The field is currently not supported if TrustConfig is used for the workload certificate feature.

` repeated .google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA intermediate_cas = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.certificatemanager.v1.TrustConfig.IntermediateCAOrBuilder>` |   
  
### getTrustAnchors(int index)
    
    
    public abstract TrustConfig.TrustAnchor getTrustAnchors(int index)

List of Trust Anchors to be used while performing validation against a given TrustStore.

`repeated .google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor trust_anchors = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TrustConfig.TrustAnchor](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor)` |   
  
### getTrustAnchorsCount()
    
    
    public abstract int getTrustAnchorsCount()

List of Trust Anchors to be used while performing validation against a given TrustStore.

`repeated .google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor trust_anchors = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTrustAnchorsList()
    
    
    public abstract List<TrustConfig.TrustAnchor> getTrustAnchorsList()

List of Trust Anchors to be used while performing validation against a given TrustStore.

`repeated .google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor trust_anchors = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TrustAnchor](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor)>` |   
  
### getTrustAnchorsOrBuilder(int index)
    
    
    public abstract TrustConfig.TrustAnchorOrBuilder getTrustAnchorsOrBuilder(int index)

List of Trust Anchors to be used while performing validation against a given TrustStore.

`repeated .google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor trust_anchors = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TrustConfig.TrustAnchorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig.TrustAnchorOrBuilder)` |   
  
### getTrustAnchorsOrBuilderList()
    
    
    public abstract List<? extends TrustConfig.TrustAnchorOrBuilder> getTrustAnchorsOrBuilderList()

List of Trust Anchors to be used while performing validation against a given TrustStore.

`repeated .google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor trust_anchors = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.certificatemanager.v1.TrustConfig.TrustAnchorOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
