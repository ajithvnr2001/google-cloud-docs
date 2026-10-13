---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.ImportProcessorVersionRequestOrBuilder
title: Interface ImportProcessorVersionRequestOrBuilder (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:04.064181+00:00
---

# Interface ImportProcessorVersionRequestOrBuilder (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.ImportProcessorVersionRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportProcessorVersionRequestOrBuilder (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 
    
    
    public interface ImportProcessorVersionRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExternalProcessorVersionSource()
    
    
    public abstract ImportProcessorVersionRequest.ExternalProcessorVersionSource getExternalProcessorVersionSource()

The source processor version to import from. It can be from a different environment and region than the destination processor.

` .google.cloud.documentai.v1beta3.ImportProcessorVersionRequest.ExternalProcessorVersionSource external_processor_version_source = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ImportProcessorVersionRequest.ExternalProcessorVersionSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.ImportProcessorVersionRequest.ExternalProcessorVersionSource)` | The externalProcessorVersionSource.  
  
### getExternalProcessorVersionSourceOrBuilder()
    
    
    public abstract ImportProcessorVersionRequest.ExternalProcessorVersionSourceOrBuilder getExternalProcessorVersionSourceOrBuilder()

The source processor version to import from. It can be from a different environment and region than the destination processor.

` .google.cloud.documentai.v1beta3.ImportProcessorVersionRequest.ExternalProcessorVersionSource external_processor_version_source = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ImportProcessorVersionRequest.ExternalProcessorVersionSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.ImportProcessorVersionRequest.ExternalProcessorVersionSourceOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The destination processor name to create the processor version in. Format: `projects/{project}/locations/{location}/processors/{processor}`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The destination processor name to create the processor version in. Format: `projects/{project}/locations/{location}/processors/{processor}`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getProcessorVersionSource()
    
    
    public abstract String getProcessorVersionSource()

The source processor version to import from. The source processor version and destination processor need to be in the same environment and region.

`string processor_version_source = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The processorVersionSource.  
  
### getProcessorVersionSourceBytes()
    
    
    public abstract ByteString getProcessorVersionSourceBytes()

The source processor version to import from. The source processor version and destination processor need to be in the same environment and region.

`string processor_version_source = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for processorVersionSource.  
  
### getSourceCase()
    
    
    public abstract ImportProcessorVersionRequest.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[ImportProcessorVersionRequest.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.ImportProcessorVersionRequest.SourceCase)` |   
  
### hasExternalProcessorVersionSource()
    
    
    public abstract boolean hasExternalProcessorVersionSource()

The source processor version to import from. It can be from a different environment and region than the destination processor.

` .google.cloud.documentai.v1beta3.ImportProcessorVersionRequest.ExternalProcessorVersionSource external_processor_version_source = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the externalProcessorVersionSource field is set.  
  
### hasProcessorVersionSource()
    
    
    public abstract boolean hasProcessorVersionSource()

The source processor version to import from. The source processor version and destination processor need to be in the same environment and region.

`string processor_version_source = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the processorVersionSource field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
