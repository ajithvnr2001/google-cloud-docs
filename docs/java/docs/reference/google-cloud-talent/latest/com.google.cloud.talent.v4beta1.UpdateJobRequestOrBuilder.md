---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.UpdateJobRequestOrBuilder
title: Interface UpdateJobRequestOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:41.824051+00:00
---

# Interface UpdateJobRequestOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.UpdateJobRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdateJobRequestOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.6  2.2.9 
    
    
    public interface UpdateJobRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getJob()
    
    
    public abstract Job getJob()

Required. The Job to be updated.

`.google.cloud.talent.v4beta1.Job job = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.Job)` | The job.  
  
### getJobOrBuilder()
    
    
    public abstract JobOrBuilder getJobOrBuilder()

Required. The Job to be updated.

`.google.cloud.talent.v4beta1.Job job = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[JobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.JobOrBuilder)` |   
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

Strongly recommended for the best service experience.

If update_mask is provided, only the specified fields in job are updated. Otherwise all the fields are updated.

A field mask to restrict the fields that are updated. Only top level fields of Job are supported.

`.google.protobuf.FieldMask update_mask = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

Strongly recommended for the best service experience.

If update_mask is provided, only the specified fields in job are updated. Otherwise all the fields are updated.

A field mask to restrict the fields that are updated. Only top level fields of Job are supported.

`.google.protobuf.FieldMask update_mask = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### hasJob()
    
    
    public abstract boolean hasJob()

Required. The Job to be updated.

`.google.cloud.talent.v4beta1.Job job = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the job field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

Strongly recommended for the best service experience.

If update_mask is provided, only the specified fields in job are updated. Otherwise all the fields are updated.

A field mask to restrict the fields that are updated. Only top level fields of Job are supported.

`.google.protobuf.FieldMask update_mask = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
