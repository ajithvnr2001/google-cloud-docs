---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.UpdatePrivateOfferDocumentRequestOrBuilder
title: Interface UpdatePrivateOfferDocumentRequestOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:01.685451+00:00
---

# Interface UpdatePrivateOfferDocumentRequestOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.UpdatePrivateOfferDocumentRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdatePrivateOfferDocumentRequestOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface UpdatePrivateOfferDocumentRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPrivateOfferDocument()
    
    
    public abstract PrivateOfferDocument getPrivateOfferDocument()

Required. The resource being updated.

` .google.cloud.commerceproducer.v1beta.PrivateOfferDocument private_offer_document = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)` | The privateOfferDocument.  
  
### getPrivateOfferDocumentOrBuilder()
    
    
    public abstract PrivateOfferDocumentOrBuilder getPrivateOfferDocumentOrBuilder()

Required. The resource being updated.

` .google.cloud.commerceproducer.v1beta.PrivateOfferDocument private_offer_document = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferDocumentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocumentOrBuilder)` |   
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

Optional. The list of fields to update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The special value "*" means full replacement. If unspecified, all fields present in the request will be overwritten.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

Optional. The list of fields to update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The special value "*" means full replacement. If unspecified, all fields present in the request will be overwritten.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### hasPrivateOfferDocument()
    
    
    public abstract boolean hasPrivateOfferDocument()

Required. The resource being updated.

` .google.cloud.commerceproducer.v1beta.PrivateOfferDocument private_offer_document = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateOfferDocument field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

Optional. The list of fields to update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The special value "*" means full replacement. If unspecified, all fields present in the request will be overwritten.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
