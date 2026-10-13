---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeployRequest.ModelConfigOrBuilder
title: Interface DeployRequest.ModelConfigOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:56.224603+00:00
---

# Interface DeployRequest.ModelConfigOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeployRequest.ModelConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DeployRequest.ModelConfigOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface DeployRequest.ModelConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAcceptEula()
    
    
    public abstract boolean getAcceptEula()

Optional. Whether the user accepts the End User License Agreement (EULA) for the model.

`bool accept_eula = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The acceptEula.  
  
### getContainerSpec()
    
    
    public abstract ModelContainerSpec getContainerSpec()

Optional. The specification of the container that is to be used when deploying. If not set, the default container spec will be used.

` .google.cloud.aiplatform.v1beta1.ModelContainerSpec container_spec = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelContainerSpec)` | The containerSpec.  
  
### getContainerSpecOrBuilder()
    
    
    public abstract ModelContainerSpecOrBuilder getContainerSpecOrBuilder()

Optional. The specification of the container that is to be used when deploying. If not set, the default container spec will be used.

` .google.cloud.aiplatform.v1beta1.ModelContainerSpec container_spec = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelContainerSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelContainerSpecOrBuilder)` |   
  
### getHuggingFaceAccessToken()
    
    
    public abstract String getHuggingFaceAccessToken()

Optional. The Hugging Face read access token used to access the model artifacts of gated models.

`string hugging_face_access_token = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The huggingFaceAccessToken.  
  
### getHuggingFaceAccessTokenBytes()
    
    
    public abstract ByteString getHuggingFaceAccessTokenBytes()

Optional. The Hugging Face read access token used to access the model artifacts of gated models.

`string hugging_face_access_token = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for huggingFaceAccessToken.  
  
### getHuggingFaceCacheEnabled()
    
    
    public abstract boolean getHuggingFaceCacheEnabled()

Optional. If true, the model will deploy with a cached version instead of directly downloading the model artifacts from Hugging Face. This is suitable for VPC-SC users with limited internet access.

`bool hugging_face_cache_enabled = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The huggingFaceCacheEnabled.  
  
### getModelDisplayName()
    
    
    public abstract String getModelDisplayName()

Optional. The user-specified display name of the uploaded model. If not set, a default name will be used.

`string model_display_name = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The modelDisplayName.  
  
### getModelDisplayNameBytes()
    
    
    public abstract ByteString getModelDisplayNameBytes()

Optional. The user-specified display name of the uploaded model. If not set, a default name will be used.

`string model_display_name = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for modelDisplayName.  
  
### getModelUserId()
    
    
    public abstract String getModelUserId()

Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. When not provided, Vertex AI will generate a value for this ID. When Model Registry model is provided, this field will be ignored.

This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.

`string model_user_id = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The modelUserId.  
  
### getModelUserIdBytes()
    
    
    public abstract ByteString getModelUserIdBytes()

Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. When not provided, Vertex AI will generate a value for this ID. When Model Registry model is provided, this field will be ignored.

This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.

`string model_user_id = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for modelUserId.  
  
### hasContainerSpec()
    
    
    public abstract boolean hasContainerSpec()

Optional. The specification of the container that is to be used when deploying. If not set, the default container spec will be used.

` .google.cloud.aiplatform.v1beta1.ModelContainerSpec container_spec = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the containerSpec field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
