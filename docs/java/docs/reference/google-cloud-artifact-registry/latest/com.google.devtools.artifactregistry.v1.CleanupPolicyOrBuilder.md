---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1.CleanupPolicyOrBuilder
title: Interface CleanupPolicyOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:07.945147+00:00
---

# Interface CleanupPolicyOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1.CleanupPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CleanupPolicyOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  0.5.0  0.4.0 
    
    
    public interface CleanupPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAction()
    
    
    public abstract CleanupPolicy.Action getAction()

Policy action.

`.google.devtools.artifactregistry.v1.CleanupPolicy.Action action = 3;`

**Returns**  
---  
**Type** | **Description**  
`[CleanupPolicy.Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1.CleanupPolicy.Action)` | The action.  
  
### getActionValue()
    
    
    public abstract int getActionValue()

Policy action.

`.google.devtools.artifactregistry.v1.CleanupPolicy.Action action = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for action.  
  
### getCondition()
    
    
    public abstract CleanupPolicyCondition getCondition()

Policy condition for matching versions.

`.google.devtools.artifactregistry.v1.CleanupPolicyCondition condition = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CleanupPolicyCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1.CleanupPolicyCondition)` | The condition.  
  
### getConditionOrBuilder()
    
    
    public abstract CleanupPolicyConditionOrBuilder getConditionOrBuilder()

Policy condition for matching versions.

`.google.devtools.artifactregistry.v1.CleanupPolicyCondition condition = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CleanupPolicyConditionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1.CleanupPolicyConditionOrBuilder)` |   
  
### getConditionTypeCase()
    
    
    public abstract CleanupPolicy.ConditionTypeCase getConditionTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[CleanupPolicy.ConditionTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1.CleanupPolicy.ConditionTypeCase)` |   
  
### getId()
    
    
    public abstract String getId()

The user-provided ID of the cleanup policy.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

The user-provided ID of the cleanup policy.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getMostRecentVersions()
    
    
    public abstract CleanupPolicyMostRecentVersions getMostRecentVersions()

Policy condition for retaining a minimum number of versions. May only be specified with a Keep action.

` .google.devtools.artifactregistry.v1.CleanupPolicyMostRecentVersions most_recent_versions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[CleanupPolicyMostRecentVersions](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1.CleanupPolicyMostRecentVersions)` | The mostRecentVersions.  
  
### getMostRecentVersionsOrBuilder()
    
    
    public abstract CleanupPolicyMostRecentVersionsOrBuilder getMostRecentVersionsOrBuilder()

Policy condition for retaining a minimum number of versions. May only be specified with a Keep action.

` .google.devtools.artifactregistry.v1.CleanupPolicyMostRecentVersions most_recent_versions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[CleanupPolicyMostRecentVersionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1.CleanupPolicyMostRecentVersionsOrBuilder)` |   
  
### hasCondition()
    
    
    public abstract boolean hasCondition()

Policy condition for matching versions.

`.google.devtools.artifactregistry.v1.CleanupPolicyCondition condition = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the condition field is set.  
  
### hasMostRecentVersions()
    
    
    public abstract boolean hasMostRecentVersions()

Policy condition for retaining a minimum number of versions. May only be specified with a Keep action.

` .google.devtools.artifactregistry.v1.CleanupPolicyMostRecentVersions most_recent_versions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mostRecentVersions field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
