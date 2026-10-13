---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TargetId
title: Interface TargetId (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:08.369982+00:00
---

# Interface TargetId (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TargetId

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TargetId (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public interface TargetId extends Serializable

TargetId defines the scope a data operation can be applied to. See Also: [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId), [AuthorizedViewId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.AuthorizedViewId)

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

## Methods 

### scopedForAuthorizedView()
    
    
    public abstract boolean scopedForAuthorizedView()

**Internal Only** : This feature is not stable for application use.

Returns true if this TargetId object represents id for an authorized view (rather than a table/materialized view).

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### scopedForMaterializedView()
    
    
    public abstract boolean scopedForMaterializedView()

**Internal Only** : This feature is not stable for application use.

Returns true if this TargetId object represents id for an materialized view (rather than a table/authorized view).

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### toResourceName(String projectId, String instanceId)
    
    
    public abstract String toResourceName(String projectId, String instanceId)

**Internal Only** : This feature is not stable for application use.

Combines the table or authorized view id with the projectId and instanceId to form the actual resource name in the request protobuf.

This method is considered an internal implementation detail and not meant to be used by applications.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
