---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.StudioDatasourceReferencesOrBuilder
title: Interface StudioDatasourceReferencesOrBuilder (0.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:44.899148+00:00
---

# Interface StudioDatasourceReferencesOrBuilder (0.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.StudioDatasourceReferencesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StudioDatasourceReferencesOrBuilder (0.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.0 (latest)  0.23.0  0.22.0  0.21.0  0.19.0  0.16.0  0.15.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface StudioDatasourceReferencesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getStudioReferences(int index)
    
    
    public abstract StudioDatasourceReference getStudioReferences(int index)

Optional. The references to the studio datasources.

` repeated .google.cloud.geminidataanalytics.v1.StudioDatasourceReference studio_references = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StudioDatasourceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.StudioDatasourceReference)` |   
  
### getStudioReferencesCount()
    
    
    public abstract int getStudioReferencesCount()

Optional. The references to the studio datasources.

` repeated .google.cloud.geminidataanalytics.v1.StudioDatasourceReference studio_references = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStudioReferencesList()
    
    
    public abstract List<StudioDatasourceReference> getStudioReferencesList()

Optional. The references to the studio datasources.

` repeated .google.cloud.geminidataanalytics.v1.StudioDatasourceReference studio_references = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StudioDatasourceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.StudioDatasourceReference)>` |   
  
### getStudioReferencesOrBuilder(int index)
    
    
    public abstract StudioDatasourceReferenceOrBuilder getStudioReferencesOrBuilder(int index)

Optional. The references to the studio datasources.

` repeated .google.cloud.geminidataanalytics.v1.StudioDatasourceReference studio_references = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StudioDatasourceReferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.StudioDatasourceReferenceOrBuilder)` |   
  
### getStudioReferencesOrBuilderList()
    
    
    public abstract List<? extends StudioDatasourceReferenceOrBuilder> getStudioReferencesOrBuilderList()

Optional. The references to the studio datasources.

` repeated .google.cloud.geminidataanalytics.v1.StudioDatasourceReference studio_references = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.geminidataanalytics.v1.StudioDatasourceReferenceOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
