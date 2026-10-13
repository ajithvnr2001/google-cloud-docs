---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.protos.google.cloud.binaryauthorization.v1.Service.CreateAttestorRequestOrBuilder
title: Interface Service.CreateAttestorRequestOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:44.476843+00:00
---

# Interface Service.CreateAttestorRequestOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.protos.google.cloud.binaryauthorization.v1.Service.CreateAttestorRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Service.CreateAttestorRequestOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.0.6 
    
    
    public static interface Service.CreateAttestorRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAttestor()
    
    
    public abstract Resources.Attestor getAttestor()

Required. The initial attestor value. The service will overwrite the attestor name field with the resource name, in the format `projects/*/attestors/*`.

` .google.cloud.binaryauthorization.v1.Attestor attestor = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Resources.Attestor](https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.protos.google.cloud.binaryauthorization.v1.Resources.Attestor)` | The attestor.  
  
### getAttestorId()
    
    
    public abstract String getAttestorId()

Required. The attestors ID.

`string attestor_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The attestorId.  
  
### getAttestorIdBytes()
    
    
    public abstract ByteString getAttestorIdBytes()

Required. The attestors ID.

`string attestor_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for attestorId.  
  
### getAttestorOrBuilder()
    
    
    public abstract Resources.AttestorOrBuilder getAttestorOrBuilder()

Required. The initial attestor value. The service will overwrite the attestor name field with the resource name, in the format `projects/*/attestors/*`.

` .google.cloud.binaryauthorization.v1.Attestor attestor = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Resources.AttestorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.protos.google.cloud.binaryauthorization.v1.Resources.AttestorOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The parent of this attestor.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent of this attestor.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasAttestor()
    
    
    public abstract boolean hasAttestor()

Required. The initial attestor value. The service will overwrite the attestor name field with the resource name, in the format `projects/*/attestors/*`.

` .google.cloud.binaryauthorization.v1.Attestor attestor = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the attestor field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
