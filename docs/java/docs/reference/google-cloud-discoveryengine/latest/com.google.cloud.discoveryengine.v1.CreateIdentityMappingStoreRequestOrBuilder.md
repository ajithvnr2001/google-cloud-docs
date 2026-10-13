---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateIdentityMappingStoreRequestOrBuilder
title: Interface CreateIdentityMappingStoreRequestOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:21.529310+00:00
---

# Interface CreateIdentityMappingStoreRequestOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateIdentityMappingStoreRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateIdentityMappingStoreRequestOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CreateIdentityMappingStoreRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCmekConfigName()
    
    
    public abstract String getCmekConfigName()

Resource name of the CmekConfig to use for protecting this Identity Mapping Store.

`string cmek_config_name = 5 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cmekConfigName.  
  
### getCmekConfigNameBytes()
    
    
    public abstract ByteString getCmekConfigNameBytes()

Resource name of the CmekConfig to use for protecting this Identity Mapping Store.

`string cmek_config_name = 5 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cmekConfigName.  
  
### getCmekOptionsCase()
    
    
    public abstract CreateIdentityMappingStoreRequest.CmekOptionsCase getCmekOptionsCase()

**Returns**  
---  
**Type** | **Description**  
`[CreateIdentityMappingStoreRequest.CmekOptionsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateIdentityMappingStoreRequest.CmekOptionsCase)` |   
  
### getDisableCmek()
    
    
    public abstract boolean getDisableCmek()

Identity Mapping Store without CMEK protections. If a default CmekConfig is set for the project, setting this field will override the default CmekConfig as well.

`bool disable_cmek = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableCmek.  
  
### getIdentityMappingStore()
    
    
    public abstract IdentityMappingStore getIdentityMappingStore()

Required. The Identity Mapping Store to create.

` .google.cloud.discoveryengine.v1.IdentityMappingStore identity_mapping_store = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)` | The identityMappingStore.  
  
### getIdentityMappingStoreId()
    
    
    public abstract String getIdentityMappingStoreId()

Required. The ID of the Identity Mapping Store to create.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.

`string identity_mapping_store_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The identityMappingStoreId.  
  
### getIdentityMappingStoreIdBytes()
    
    
    public abstract ByteString getIdentityMappingStoreIdBytes()

Required. The ID of the Identity Mapping Store to create.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.

`string identity_mapping_store_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for identityMappingStoreId.  
  
### getIdentityMappingStoreOrBuilder()
    
    
    public abstract IdentityMappingStoreOrBuilder getIdentityMappingStoreOrBuilder()

Required. The Identity Mapping Store to create.

` .google.cloud.discoveryengine.v1.IdentityMappingStore identity_mapping_store = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasCmekConfigName()
    
    
    public abstract boolean hasCmekConfigName()

Resource name of the CmekConfig to use for protecting this Identity Mapping Store.

`string cmek_config_name = 5 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cmekConfigName field is set.  
  
### hasDisableCmek()
    
    
    public abstract boolean hasDisableCmek()

Identity Mapping Store without CMEK protections. If a default CmekConfig is set for the project, setting this field will override the default CmekConfig as well.

`bool disable_cmek = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the disableCmek field is set.  
  
### hasIdentityMappingStore()
    
    
    public abstract boolean hasIdentityMappingStore()

Required. The Identity Mapping Store to create.

` .google.cloud.discoveryengine.v1.IdentityMappingStore identity_mapping_store = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the identityMappingStore field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
