---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CustomCanaryDeployment.PhaseConfigOrBuilder
title: Interface CustomCanaryDeployment.PhaseConfigOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:54.515643+00:00
---

# Interface CustomCanaryDeployment.PhaseConfigOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CustomCanaryDeployment.PhaseConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CustomCanaryDeployment.PhaseConfigOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CustomCanaryDeployment.PhaseConfigOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.deploy.v1.CustomCanaryDeployment.PhaseConfigOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.deploy.v1.CustomCanaryDeployment.PhaseConfigOrBuilder)


    
    
    public static interface CustomCanaryDeployment.PhaseConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPercentage()
    
    
    public abstract int getPercentage()

Required. Percentage deployment for the phase.

`int32 percentage = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The percentage.  
  
### getPhaseId()
    
    
    public abstract String getPhaseId()

Required. The ID to assign to the `Rollout` phase. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`.

`string phase_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The phaseId.  
  
### getPhaseIdBytes()
    
    
    public abstract ByteString getPhaseIdBytes()

Required. The ID to assign to the `Rollout` phase. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`.

`string phase_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for phaseId.  
  
### getPostdeploy()
    
    
    public abstract Postdeploy getPostdeploy()

Optional. Configuration for the postdeploy job of this phase. If this is not configured, there will be no postdeploy job for this phase.

`.google.events.cloud.deploy.v1.Postdeploy postdeploy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Postdeploy](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.Postdeploy)` | The postdeploy.  
  
### getPostdeployOrBuilder()
    
    
    public abstract PostdeployOrBuilder getPostdeployOrBuilder()

Optional. Configuration for the postdeploy job of this phase. If this is not configured, there will be no postdeploy job for this phase.

`.google.events.cloud.deploy.v1.Postdeploy postdeploy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[PostdeployOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.PostdeployOrBuilder)` |   
  
### getPredeploy()
    
    
    public abstract Predeploy getPredeploy()

Optional. Configuration for the predeploy job of this phase. If this is not configured, there will be no predeploy job for this phase.

`.google.events.cloud.deploy.v1.Predeploy predeploy = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Predeploy](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.Predeploy)` | The predeploy.  
  
### getPredeployOrBuilder()
    
    
    public abstract PredeployOrBuilder getPredeployOrBuilder()

Optional. Configuration for the predeploy job of this phase. If this is not configured, there will be no predeploy job for this phase.

`.google.events.cloud.deploy.v1.Predeploy predeploy = 5;`

**Returns**  
---  
**Type** | **Description**  
`[PredeployOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.PredeployOrBuilder)` |   
  
### getProfiles(int index)
    
    
    public abstract String getProfiles(int index)

Skaffold profiles to use when rendering the manifest for this phase. These are in addition to the profiles list specified in the `DeliveryPipeline` stage.

`repeated string profiles = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The profiles at the given index.  
  
### getProfilesBytes(int index)
    
    
    public abstract ByteString getProfilesBytes(int index)

Skaffold profiles to use when rendering the manifest for this phase. These are in addition to the profiles list specified in the `DeliveryPipeline` stage.

`repeated string profiles = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the profiles at the given index.  
  
### getProfilesCount()
    
    
    public abstract int getProfilesCount()

Skaffold profiles to use when rendering the manifest for this phase. These are in addition to the profiles list specified in the `DeliveryPipeline` stage.

`repeated string profiles = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of profiles.  
  
### getProfilesList()
    
    
    public abstract List<String> getProfilesList()

Skaffold profiles to use when rendering the manifest for this phase. These are in addition to the profiles list specified in the `DeliveryPipeline` stage.

`repeated string profiles = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the profiles.  
  
### getVerify()
    
    
    public abstract boolean getVerify()

Whether to run verify tests after the deployment.

`bool verify = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The verify.  
  
### hasPostdeploy()
    
    
    public abstract boolean hasPostdeploy()

Optional. Configuration for the postdeploy job of this phase. If this is not configured, there will be no postdeploy job for this phase.

`.google.events.cloud.deploy.v1.Postdeploy postdeploy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postdeploy field is set.  
  
### hasPredeploy()
    
    
    public abstract boolean hasPredeploy()

Optional. Configuration for the predeploy job of this phase. If this is not configured, there will be no predeploy job for this phase.

`.google.events.cloud.deploy.v1.Predeploy predeploy = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the predeploy field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
