---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResultOrBuilder
title: Interface ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResultOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:58.435792+00:00
---

# Interface ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResultOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResultOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResultOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.0.6 
    
    
    public static interface ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResultOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCheckIndex()
    
    
    public abstract String getCheckIndex()

The index of the check.

`string check_index = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The checkIndex.  
  
### getCheckIndexBytes()
    
    
    public abstract ByteString getCheckIndexBytes()

The index of the check.

`string check_index = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for checkIndex.  
  
### getCheckName()
    
    
    public abstract String getCheckName()

The name of the check.

`string check_name = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The checkName.  
  
### getCheckNameBytes()
    
    
    public abstract ByteString getCheckNameBytes()

The name of the check.

`string check_name = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for checkName.  
  
### getCheckSetIndex()
    
    
    public abstract String getCheckSetIndex()

The index of the check set.

`string check_set_index = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The checkSetIndex.  
  
### getCheckSetIndexBytes()
    
    
    public abstract ByteString getCheckSetIndexBytes()

The index of the check set.

`string check_set_index = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for checkSetIndex.  
  
### getCheckSetName()
    
    
    public abstract String getCheckSetName()

The name of the check set.

`string check_set_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The checkSetName.  
  
### getCheckSetNameBytes()
    
    
    public abstract ByteString getCheckSetNameBytes()

The name of the check set.

`string check_set_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for checkSetName.  
  
### getCheckSetScope()
    
    
    public abstract ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope getCheckSetScope()

The scope of the check set.

` .google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope check_set_scope = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope](https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope)` | The checkSetScope.  
  
### getCheckSetScopeOrBuilder()
    
    
    public abstract ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScopeOrBuilder getCheckSetScopeOrBuilder()

The scope of the check set.

` .google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope check_set_scope = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScopeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScopeOrBuilder)` |   
  
### getCheckType()
    
    
    public abstract String getCheckType()

The type of the check.

`string check_type = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The checkType.  
  
### getCheckTypeBytes()
    
    
    public abstract ByteString getCheckTypeBytes()

The type of the check.

`string check_type = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for checkType.  
  
### getExplanation()
    
    
    public abstract String getExplanation()

User-friendly explanation of this check result.

`string explanation = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The explanation.  
  
### getExplanationBytes()
    
    
    public abstract ByteString getExplanationBytes()

User-friendly explanation of this check result.

`string explanation = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for explanation.  
  
### getVerdict()
    
    
    public abstract ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict getVerdict()

The verdict of this check.

` .google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict verdict = 7; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict](https://docs.cloud.google.com/java/docs/reference/google-cloud-binary-authorization/latest/com.google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict)` | The verdict.  
  
### getVerdictValue()
    
    
    public abstract int getVerdictValue()

The verdict of this check.

` .google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict verdict = 7; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for verdict.  
  
### hasCheckSetScope()
    
    
    public abstract boolean hasCheckSetScope()

The scope of the check set.

` .google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope check_set_scope = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the checkSetScope field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
