---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.NormalizedBoundingPolyOrBuilder
title: Interface NormalizedBoundingPolyOrBuilder (0.215.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:49.890180+00:00
---

# Interface NormalizedBoundingPolyOrBuilder (0.215.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.NormalizedBoundingPolyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NormalizedBoundingPolyOrBuilder (0.215.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.215.0 (latest)  0.214.0  0.213.0  0.211.0  0.208.0  0.207.0  0.205.0  0.203.0  0.202.0  0.201.0  0.200.0  0.198.0  0.196.0  0.195.0  0.194.0  0.193.0  0.192.0  0.190.0  0.188.0  0.187.0  0.184.0  0.183.0  0.182.0  0.180.0  0.179.0  0.178.0  0.177.0  0.176.0  0.175.0  0.174.0  0.173.0  0.172.0  0.171.0  0.169.0  0.168.0  0.167.0  0.166.0  0.165.0  0.164.0  0.163.0  0.162.0  0.161.0  0.160.0  0.159.0  0.157.0  0.156.0  0.155.0  0.154.0  0.153.0  0.152.0  0.151.0  0.150.0  0.149.0  0.148.0  0.147.0  0.144.0  0.143.0  0.142.0  0.141.0  0.140.0  0.139.0  0.138.0  0.137.0  0.136.0  0.135.0  0.134.0  0.133.0  0.132.0  0.131.0  0.129.0  0.128.0  0.127.0  0.126.0  0.125.0  0.124.0  0.123.7  0.122.11 
    
    
    public interface NormalizedBoundingPolyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNormalizedVertices(int index)
    
    
    public abstract NormalizedVertex getNormalizedVertices(int index)

The bounding polygon normalized vertices.

`repeated .google.cloud.datalabeling.v1beta1.NormalizedVertex normalized_vertices = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NormalizedVertex](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.NormalizedVertex)` |   
  
### getNormalizedVerticesCount()
    
    
    public abstract int getNormalizedVerticesCount()

The bounding polygon normalized vertices.

`repeated .google.cloud.datalabeling.v1beta1.NormalizedVertex normalized_vertices = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNormalizedVerticesList()
    
    
    public abstract List<NormalizedVertex> getNormalizedVerticesList()

The bounding polygon normalized vertices.

`repeated .google.cloud.datalabeling.v1beta1.NormalizedVertex normalized_vertices = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NormalizedVertex](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.NormalizedVertex)>` |   
  
### getNormalizedVerticesOrBuilder(int index)
    
    
    public abstract NormalizedVertexOrBuilder getNormalizedVerticesOrBuilder(int index)

The bounding polygon normalized vertices.

`repeated .google.cloud.datalabeling.v1beta1.NormalizedVertex normalized_vertices = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NormalizedVertexOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.NormalizedVertexOrBuilder)` |   
  
### getNormalizedVerticesOrBuilderList()
    
    
    public abstract List<? extends NormalizedVertexOrBuilder> getNormalizedVerticesOrBuilderList()

The bounding polygon normalized vertices.

`repeated .google.cloud.datalabeling.v1beta1.NormalizedVertex normalized_vertices = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.datalabeling.v1beta1.NormalizedVertexOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
