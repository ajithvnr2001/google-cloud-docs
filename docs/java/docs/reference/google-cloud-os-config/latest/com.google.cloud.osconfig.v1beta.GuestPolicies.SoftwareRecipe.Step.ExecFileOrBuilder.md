---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.SoftwareRecipe.Step.ExecFileOrBuilder
title: Interface GuestPolicies.SoftwareRecipe.Step.ExecFileOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:48.052740+00:00
---

# Interface GuestPolicies.SoftwareRecipe.Step.ExecFileOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.SoftwareRecipe.Step.ExecFileOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GuestPolicies.SoftwareRecipe.Step.ExecFileOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static interface GuestPolicies.SoftwareRecipe.Step.ExecFileOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllowedExitCodes(int index)
    
    
    public abstract int getAllowedExitCodes(int index)

Defaults to [0]. A list of possible return values that the program can return to indicate a success.

`repeated int32 allowed_exit_codes = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowedExitCodes at the given index.  
  
### getAllowedExitCodesCount()
    
    
    public abstract int getAllowedExitCodesCount()

Defaults to [0]. A list of possible return values that the program can return to indicate a success.

`repeated int32 allowed_exit_codes = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of allowedExitCodes.  
  
### getAllowedExitCodesList()
    
    
    public abstract List<Integer> getAllowedExitCodesList()

Defaults to [0]. A list of possible return values that the program can return to indicate a success.

`repeated int32 allowed_exit_codes = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the allowedExitCodes.  
  
### getArgs(int index)
    
    
    public abstract String getArgs(int index)

Arguments to be passed to the provided executable.

`repeated string args = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The args at the given index.  
  
### getArgsBytes(int index)
    
    
    public abstract ByteString getArgsBytes(int index)

Arguments to be passed to the provided executable.

`repeated string args = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the args at the given index.  
  
### getArgsCount()
    
    
    public abstract int getArgsCount()

Arguments to be passed to the provided executable.

`repeated string args = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of args.  
  
### getArgsList()
    
    
    public abstract List<String> getArgsList()

Arguments to be passed to the provided executable.

`repeated string args = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the args.  
  
### getArtifactId()
    
    
    public abstract String getArtifactId()

The id of the relevant artifact in the recipe.

`string artifact_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The artifactId.  
  
### getArtifactIdBytes()
    
    
    public abstract ByteString getArtifactIdBytes()

The id of the relevant artifact in the recipe.

`string artifact_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for artifactId.  
  
### getLocalPath()
    
    
    public abstract String getLocalPath()

The absolute path of the file on the local filesystem.

`string local_path = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The localPath.  
  
### getLocalPathBytes()
    
    
    public abstract ByteString getLocalPathBytes()

The absolute path of the file on the local filesystem.

`string local_path = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for localPath.  
  
### getLocationTypeCase()
    
    
    public abstract GuestPolicies.SoftwareRecipe.Step.ExecFile.LocationTypeCase getLocationTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[GuestPolicies.SoftwareRecipe.Step.ExecFile.LocationTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.SoftwareRecipe.Step.ExecFile.LocationTypeCase)` |   
  
### hasArtifactId()
    
    
    public abstract boolean hasArtifactId()

The id of the relevant artifact in the recipe.

`string artifact_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the artifactId field is set.  
  
### hasLocalPath()
    
    
    public abstract boolean hasLocalPath()

The absolute path of the file on the local filesystem.

`string local_path = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the localPath field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
