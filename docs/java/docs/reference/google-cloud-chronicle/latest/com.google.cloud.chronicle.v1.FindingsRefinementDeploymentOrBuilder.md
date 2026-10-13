---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.FindingsRefinementDeploymentOrBuilder
title: Interface FindingsRefinementDeploymentOrBuilder (0.37.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:09.049721+00:00
---

# Interface FindingsRefinementDeploymentOrBuilder (0.37.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.FindingsRefinementDeploymentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FindingsRefinementDeploymentOrBuilder (0.37.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.0 (latest)  0.33.0  0.32.0  0.31.0  0.29.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.2.0  0.1.0 
    
    
    public interface FindingsRefinementDeploymentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArchived()
    
    
    public abstract boolean getArchived()

The archive state of the findings refinement deployment. Cannot be set to true unless enabled is set to false. If currently set to true, enabled cannot be updated to true.

`bool archived = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The archived.  
  
### getDetectionExclusionApplication()
    
    
    public abstract DetectionExclusionApplication getDetectionExclusionApplication()

The resources which the detection exclusion is applied to.

` .google.cloud.chronicle.v1.DetectionExclusionApplication detection_exclusion_application = 5; `

**Returns**  
---  
**Type** | **Description**  
`[DetectionExclusionApplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DetectionExclusionApplication)` | The detectionExclusionApplication.  
  
### getDetectionExclusionApplicationOrBuilder()
    
    
    public abstract DetectionExclusionApplicationOrBuilder getDetectionExclusionApplicationOrBuilder()

The resources which the detection exclusion is applied to.

` .google.cloud.chronicle.v1.DetectionExclusionApplication detection_exclusion_application = 5; `

**Returns**  
---  
**Type** | **Description**  
`[DetectionExclusionApplicationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DetectionExclusionApplicationOrBuilder)` |   
  
### getEnabled()
    
    
    public abstract boolean getEnabled()

Whether the findings refinement is currently deployed continuously against incoming findings.

`bool enabled = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enabled.  
  
### getFindingsRefinementApplicationCase()
    
    
    public abstract FindingsRefinementDeployment.FindingsRefinementApplicationCase getFindingsRefinementApplicationCase()

**Returns**  
---  
**Type** | **Description**  
`[FindingsRefinementDeployment.FindingsRefinementApplicationCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.FindingsRefinementDeployment.FindingsRefinementApplicationCase)` |   
  
### getName()
    
    
    public abstract String getName()

Required. The resource name of the findings refinement deployment. Format: projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}/deployment

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The resource name of the findings refinement deployment. Format: projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}/deployment

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The timestamp when the findings refinement deployment was last updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when the findings refinement deployment was last updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasDetectionExclusionApplication()
    
    
    public abstract boolean hasDetectionExclusionApplication()

The resources which the detection exclusion is applied to.

` .google.cloud.chronicle.v1.DetectionExclusionApplication detection_exclusion_application = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the detectionExclusionApplication field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The timestamp when the findings refinement deployment was last updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
