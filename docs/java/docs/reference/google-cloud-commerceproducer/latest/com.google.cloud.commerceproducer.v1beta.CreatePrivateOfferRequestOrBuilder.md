---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CreatePrivateOfferRequestOrBuilder
title: Interface CreatePrivateOfferRequestOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:24.258059+00:00
---

# Interface CreatePrivateOfferRequestOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CreatePrivateOfferRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreatePrivateOfferRequestOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface CreatePrivateOfferRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getParent()
    
    
    public abstract String getParent()

Required. Value for parent.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. Value for parent.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getPrivateOffer()
    
    
    public abstract PrivateOffer getPrivateOffer()

Required. The resource being created

` .google.cloud.commerceproducer.v1beta.PrivateOffer private_offer = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` | The privateOffer.  
  
### getPrivateOfferOrBuilder()
    
    
    public abstract PrivateOfferOrBuilder getPrivateOfferOrBuilder()

Required. The resource being created

` .google.cloud.commerceproducer.v1beta.PrivateOffer private_offer = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferOrBuilder)` |   
  
### hasPrivateOffer()
    
    
    public abstract boolean hasPrivateOffer()

Required. The resource being created

` .google.cloud.commerceproducer.v1beta.PrivateOffer private_offer = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateOffer field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
