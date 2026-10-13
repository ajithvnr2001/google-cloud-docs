---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewOrBuilder
title: Interface MerchantReviewOrBuilder (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:03.198070+00:00
---

# Interface MerchantReviewOrBuilder (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MerchantReviewOrBuilder (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface MerchantReviewOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCustomAttributes(int index)
    
    
    public abstract CustomAttribute getCustomAttributes(int index)

Optional. A list of custom (merchant-provided) attributes. It can also be used for submitting any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as experimental attributes. Maximum allowed number of characters for each custom attribute is 10240 (represents sum of characters for name and value). Maximum 2500 custom attributes can be set per product, with total size of 102.4kB. Underscores in custom attribute names are replaced by spaces upon insertion.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.CustomAttribute` |   
  
### getCustomAttributesCount()
    
    
    public abstract int getCustomAttributesCount()

Optional. A list of custom (merchant-provided) attributes. It can also be used for submitting any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as experimental attributes. Maximum allowed number of characters for each custom attribute is 10240 (represents sum of characters for name and value). Maximum 2500 custom attributes can be set per product, with total size of 102.4kB. Underscores in custom attribute names are replaced by spaces upon insertion.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCustomAttributesList()
    
    
    public abstract List<CustomAttribute> getCustomAttributesList()

Optional. A list of custom (merchant-provided) attributes. It can also be used for submitting any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as experimental attributes. Maximum allowed number of characters for each custom attribute is 10240 (represents sum of characters for name and value). Maximum 2500 custom attributes can be set per product, with total size of 102.4kB. Underscores in custom attribute names are replaced by spaces upon insertion.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.shopping.type.CustomAttribute>` |   
  
### getCustomAttributesOrBuilder(int index)
    
    
    public abstract CustomAttributeOrBuilder getCustomAttributesOrBuilder(int index)

Optional. A list of custom (merchant-provided) attributes. It can also be used for submitting any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as experimental attributes. Maximum allowed number of characters for each custom attribute is 10240 (represents sum of characters for name and value). Maximum 2500 custom attributes can be set per product, with total size of 102.4kB. Underscores in custom attribute names are replaced by spaces upon insertion.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.CustomAttributeOrBuilder` |   
  
### getCustomAttributesOrBuilderList()
    
    
    public abstract List<? extends CustomAttributeOrBuilder> getCustomAttributesOrBuilderList()

Optional. A list of custom (merchant-provided) attributes. It can also be used for submitting any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as experimental attributes. Maximum allowed number of characters for each custom attribute is 10240 (represents sum of characters for name and value). Maximum 2500 custom attributes can be set per product, with total size of 102.4kB. Underscores in custom attribute names are replaced by spaces upon insertion.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.type.CustomAttributeOrBuilder>` |   
  
### getDataSource()
    
    
    public abstract String getDataSource()

Output only. The primary data source of the merchant review.

`string data_source = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataSource.  
  
### getDataSourceBytes()
    
    
    public abstract ByteString getDataSourceBytes()

Output only. The primary data source of the merchant review.

`string data_source = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataSource.  
  
### getMerchantReviewAttributes()
    
    
    public abstract MerchantReviewAttributes getMerchantReviewAttributes()

Optional. A list of merchant review attributes.

` .google.shopping.merchant.reviews.v1beta.MerchantReviewAttributes merchant_review_attributes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewAttributes](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewAttributes)` | The merchantReviewAttributes.  
  
### getMerchantReviewAttributesOrBuilder()
    
    
    public abstract MerchantReviewAttributesOrBuilder getMerchantReviewAttributesOrBuilder()

Optional. A list of merchant review attributes.

` .google.shopping.merchant.reviews.v1beta.MerchantReviewAttributes merchant_review_attributes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewAttributesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewAttributesOrBuilder)` |   
  
### getMerchantReviewId()
    
    
    public abstract String getMerchantReviewId()

Required. The user provided merchant review ID to uniquely identify the merchant review.

`string merchant_review_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The merchantReviewId.  
  
### getMerchantReviewIdBytes()
    
    
    public abstract ByteString getMerchantReviewIdBytes()

Required. The user provided merchant review ID to uniquely identify the merchant review.

`string merchant_review_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for merchantReviewId.  
  
### getMerchantReviewStatus()
    
    
    public abstract MerchantReviewStatus getMerchantReviewStatus()

Output only. The status of a merchant review, data validation issues, that is, information about a merchant review computed asynchronously.

` .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus merchant_review_status = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewStatus](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus)` | The merchantReviewStatus.  
  
### getMerchantReviewStatusOrBuilder()
    
    
    public abstract MerchantReviewStatusOrBuilder getMerchantReviewStatusOrBuilder()

Output only. The status of a merchant review, data validation issues, that is, information about a merchant review computed asynchronously.

` .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus merchant_review_status = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.MerchantReviewStatusOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The name of the merchant review. Format: `"{merchantreview.name=accounts/{account}/merchantReviews/{merchantReview}}"`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The name of the merchant review. Format: `"{merchantreview.name=accounts/{account}/merchantReviews/{merchantReview}}"`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### hasMerchantReviewAttributes()
    
    
    public abstract boolean hasMerchantReviewAttributes()

Optional. A list of merchant review attributes.

` .google.shopping.merchant.reviews.v1beta.MerchantReviewAttributes merchant_review_attributes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the merchantReviewAttributes field is set.  
  
### hasMerchantReviewStatus()
    
    
    public abstract boolean hasMerchantReviewStatus()

Output only. The status of a merchant review, data validation issues, that is, information about a merchant review computed asynchronously.

` .google.shopping.merchant.reviews.v1beta.MerchantReviewStatus merchant_review_status = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the merchantReviewStatus field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
