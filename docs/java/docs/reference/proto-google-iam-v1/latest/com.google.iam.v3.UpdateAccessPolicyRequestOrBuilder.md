---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3.UpdateAccessPolicyRequestOrBuilder
title: Interface UpdateAccessPolicyRequestOrBuilder (1.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:44.650292+00:00
---

# Interface UpdateAccessPolicyRequestOrBuilder (1.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3.UpdateAccessPolicyRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdateAccessPolicyRequestOrBuilder (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.73.0 (latest)  1.69.0  1.68.0  1.67.0  1.65.0  1.62.0  1.61.0  1.60.1  1.59.1  1.58.2  1.57.0  1.56.3  1.55.0  1.54.2  1.53.0  1.52.0  1.51.0  1.49.1  1.48.0  1.47.0  1.46.0  1.45.1  1.44.0  1.43.0  1.41.0  1.40.1  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.0  1.29.0  1.28.0  1.27.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.0  1.18.1  1.17.1  1.16.1  1.10.0  1.9.3  1.8.0  1.7.0  1.6.23  1.5.1  1.4.1  1.3.4  1.2.12 
    
    
    public interface UpdateAccessPolicyRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccessPolicy()
    
    
    public abstract AccessPolicy getAccessPolicy()

Required. The access policy to update.

The access policy's `name` field is used to identify the policy to update.

`.google.iam.v3.AccessPolicy access_policy = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3.AccessPolicy)` | The accessPolicy.  
  
### getAccessPolicyOrBuilder()
    
    
    public abstract AccessPolicyOrBuilder getAccessPolicyOrBuilder()

Required. The access policy to update.

The access policy's `name` field is used to identify the policy to update.

`.google.iam.v3.AccessPolicy access_policy = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AccessPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3.AccessPolicyOrBuilder)` |   
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

Optional. If set, validate the request and preview the update, but do not actually post it.

`bool validate_only = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
### hasAccessPolicy()
    
    
    public abstract boolean hasAccessPolicy()

Required. The access policy to update.

The access policy's `name` field is used to identify the policy to update.

`.google.iam.v3.AccessPolicy access_policy = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accessPolicy field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
