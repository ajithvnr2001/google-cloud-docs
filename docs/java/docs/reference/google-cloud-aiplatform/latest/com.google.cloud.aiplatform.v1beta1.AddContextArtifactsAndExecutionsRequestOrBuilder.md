---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AddContextArtifactsAndExecutionsRequestOrBuilder
title: Interface AddContextArtifactsAndExecutionsRequestOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:07.592609+00:00
---

# Interface AddContextArtifactsAndExecutionsRequestOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AddContextArtifactsAndExecutionsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AddContextArtifactsAndExecutionsRequestOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface AddContextArtifactsAndExecutionsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArtifacts(int index)
    
    
    public abstract String getArtifacts(int index)

The resource names of the Artifacts to attribute to the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`

`repeated string artifacts = 2 [(.google.api.resource_reference) = { ... }`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The artifacts at the given index.  
  
### getArtifactsBytes(int index)
    
    
    public abstract ByteString getArtifactsBytes(int index)

The resource names of the Artifacts to attribute to the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`

`repeated string artifacts = 2 [(.google.api.resource_reference) = { ... }`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the artifacts at the given index.  
  
### getArtifactsCount()
    
    
    public abstract int getArtifactsCount()

The resource names of the Artifacts to attribute to the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`

`repeated string artifacts = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of artifacts.  
  
### getArtifactsList()
    
    
    public abstract List<String> getArtifactsList()

The resource names of the Artifacts to attribute to the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`

`repeated string artifacts = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the artifacts.  
  
### getContext()
    
    
    public abstract String getContext()

Required. The resource name of the Context that the Artifacts and Executions belong to. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`

` string context = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The context.  
  
### getContextBytes()
    
    
    public abstract ByteString getContextBytes()

Required. The resource name of the Context that the Artifacts and Executions belong to. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`

` string context = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for context.  
  
### getExecutions(int index)
    
    
    public abstract String getExecutions(int index)

The resource names of the Executions to associate with the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`

`repeated string executions = 3 [(.google.api.resource_reference) = { ... }`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The executions at the given index.  
  
### getExecutionsBytes(int index)
    
    
    public abstract ByteString getExecutionsBytes(int index)

The resource names of the Executions to associate with the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`

`repeated string executions = 3 [(.google.api.resource_reference) = { ... }`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the executions at the given index.  
  
### getExecutionsCount()
    
    
    public abstract int getExecutionsCount()

The resource names of the Executions to associate with the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`

`repeated string executions = 3 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of executions.  
  
### getExecutionsList()
    
    
    public abstract List<String> getExecutionsList()

The resource names of the Executions to associate with the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`

`repeated string executions = 3 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the executions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
