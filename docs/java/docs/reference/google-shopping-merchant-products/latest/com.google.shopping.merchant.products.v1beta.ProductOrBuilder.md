---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductOrBuilder
title: Interface ProductOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:20.564006+00:00
---

# Interface ProductOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProductOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ProductOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAttributes()
    
    
    public abstract Attributes getAttributes()

Output only. A list of product attributes.

` .google.shopping.merchant.products.v1beta.Attributes attributes = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Attributes](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.Attributes)` | The attributes.  
  
### getAttributesOrBuilder()
    
    
    public abstract AttributesOrBuilder getAttributesOrBuilder()

Output only. A list of product attributes.

` .google.shopping.merchant.products.v1beta.Attributes attributes = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AttributesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.AttributesOrBuilder)` |   
  
### getAutomatedDiscounts()
    
    
    public abstract AutomatedDiscounts getAutomatedDiscounts()

Output only. The automated discounts information for the product.

` .google.shopping.merchant.products.v1beta.AutomatedDiscounts automated_discounts = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AutomatedDiscounts](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.AutomatedDiscounts)` | The automatedDiscounts.  
  
### getAutomatedDiscountsOrBuilder()
    
    
    public abstract AutomatedDiscountsOrBuilder getAutomatedDiscountsOrBuilder()

Output only. The automated discounts information for the product.

` .google.shopping.merchant.products.v1beta.AutomatedDiscounts automated_discounts = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AutomatedDiscountsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.AutomatedDiscountsOrBuilder)` |   
  
### getChannel()
    
    
    public abstract Channel.ChannelEnum getChannel()

Output only. The [channel](https://support.google.com/merchants/answer/7361332) of the product.

` .google.shopping.type.Channel.ChannelEnum channel = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Channel.ChannelEnum` | The channel.  
  
### getChannelValue()
    
    
    public abstract int getChannelValue()

Output only. The [channel](https://support.google.com/merchants/answer/7361332) of the product.

` .google.shopping.type.Channel.ChannelEnum channel = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for channel.  
  
### getContentLanguage()
    
    
    public abstract String getContentLanguage()

Output only. The two-letter [ISO 639-1](http://en.wikipedia.org/wiki/ISO_639-1) language code for the product.

`string content_language = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The contentLanguage.  
  
### getContentLanguageBytes()
    
    
    public abstract ByteString getContentLanguageBytes()

Output only. The two-letter [ISO 639-1](http://en.wikipedia.org/wiki/ISO_639-1) language code for the product.

`string content_language = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for contentLanguage.  
  
### getCustomAttributes(int index)
    
    
    public abstract CustomAttribute getCustomAttributes(int index)

Output only. A list of custom (merchant-provided) attributes. It can also be used to submit any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as additional attributes used for Buy on Google.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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

Output only. A list of custom (merchant-provided) attributes. It can also be used to submit any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as additional attributes used for Buy on Google.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCustomAttributesList()
    
    
    public abstract List<CustomAttribute> getCustomAttributesList()

Output only. A list of custom (merchant-provided) attributes. It can also be used to submit any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as additional attributes used for Buy on Google.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.shopping.type.CustomAttribute>` |   
  
### getCustomAttributesOrBuilder(int index)
    
    
    public abstract CustomAttributeOrBuilder getCustomAttributesOrBuilder(int index)

Output only. A list of custom (merchant-provided) attributes. It can also be used to submit any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as additional attributes used for Buy on Google.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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

Output only. A list of custom (merchant-provided) attributes. It can also be used to submit any attribute of the data specification in its generic form (for example, `{ "name": "size type", "value": "regular" }`). This is useful for submitting attributes not explicitly exposed by the API, such as additional attributes used for Buy on Google.

` repeated .google.shopping.type.CustomAttribute custom_attributes = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.type.CustomAttributeOrBuilder>` |   
  
### getDataSource()
    
    
    public abstract String getDataSource()

Output only. The primary data source of the product.

`string data_source = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataSource.  
  
### getDataSourceBytes()
    
    
    public abstract ByteString getDataSourceBytes()

Output only. The primary data source of the product.

`string data_source = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataSource.  
  
### getFeedLabel()
    
    
    public abstract String getFeedLabel()

Output only. The feed label lets you categorize and identify your products. The maximum allowed characters is 20 and the supported characters are`A-Z`, `0-9`, hyphen and underscore. The feed label must not include any spaces. For more information, see [Using feed labels](https://support.google.com/merchants/answer/14994087)

`string feed_label = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The feedLabel.  
  
### getFeedLabelBytes()
    
    
    public abstract ByteString getFeedLabelBytes()

Output only. The feed label lets you categorize and identify your products. The maximum allowed characters is 20 and the supported characters are`A-Z`, `0-9`, hyphen and underscore. The feed label must not include any spaces. For more information, see [Using feed labels](https://support.google.com/merchants/answer/14994087)

`string feed_label = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for feedLabel.  
  
### getName()
    
    
    public abstract String getName()

The name of the product. Format: `accounts/{account}/products/{product}` where the last section `product` consists of 4 parts: `channel~content_language~feed_label~offer_id` example for product name is `accounts/123/products/online~en~US~sku123`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The name of the product. Format: `accounts/{account}/products/{product}` where the last section `product` consists of 4 parts: `channel~content_language~feed_label~offer_id` example for product name is `accounts/123/products/online~en~US~sku123`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOfferId()
    
    
    public abstract String getOfferId()

Output only. Your unique identifier for the product. This is the same for the product input and processed product. Leading and trailing whitespaces are stripped and multiple whitespaces are replaced by a single whitespace upon submission. See the [product data specification](https://support.google.com/merchants/answer/188494#id) for details.

`string offer_id = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The offerId.  
  
### getOfferIdBytes()
    
    
    public abstract ByteString getOfferIdBytes()

Output only. Your unique identifier for the product. This is the same for the product input and processed product. Leading and trailing whitespaces are stripped and multiple whitespaces are replaced by a single whitespace upon submission. See the [product data specification](https://support.google.com/merchants/answer/188494#id) for details.

`string offer_id = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for offerId.  
  
### getProductStatus()
    
    
    public abstract ProductStatus getProductStatus()

Output only. The status of a product, data validation issues, that is, information about a product computed asynchronously.

` .google.shopping.merchant.products.v1beta.ProductStatus product_status = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProductStatus](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductStatus)` | The productStatus.  
  
### getProductStatusOrBuilder()
    
    
    public abstract ProductStatusOrBuilder getProductStatusOrBuilder()

Output only. The status of a product, data validation issues, that is, information about a product computed asynchronously.

` .google.shopping.merchant.products.v1beta.ProductStatus product_status = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProductStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductStatusOrBuilder)` |   
  
### getVersionNumber()
    
    
    public abstract long getVersionNumber()

Output only. Represents the existing version (freshness) of the product, which can be used to preserve the right order when multiple updates are done at the same time.

If set, the insertion is prevented when version number is lower than the current version number of the existing product. Re-insertion (for example, product refresh after 30 days) can be performed with the current `version_number`.

Only supported for insertions into primary data sources.

If the operation is prevented, the aborted exception will be thrown.

`optional int64 version_number = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The versionNumber.  
  
### hasAttributes()
    
    
    public abstract boolean hasAttributes()

Output only. A list of product attributes.

` .google.shopping.merchant.products.v1beta.Attributes attributes = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the attributes field is set.  
  
### hasAutomatedDiscounts()
    
    
    public abstract boolean hasAutomatedDiscounts()

Output only. The automated discounts information for the product.

` .google.shopping.merchant.products.v1beta.AutomatedDiscounts automated_discounts = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the automatedDiscounts field is set.  
  
### hasProductStatus()
    
    
    public abstract boolean hasProductStatus()

Output only. The status of a product, data validation issues, that is, information about a product computed asynchronously.

` .google.shopping.merchant.products.v1beta.ProductStatus product_status = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productStatus field is set.  
  
### hasVersionNumber()
    
    
    public abstract boolean hasVersionNumber()

Output only. Represents the existing version (freshness) of the product, which can be used to preserve the right order when multiple updates are done at the same time.

If set, the insertion is prevented when version number is lower than the current version number of the existing product. Re-insertion (for example, product refresh after 30 days) can be performed with the current `version_number`.

Only supported for insertions into primary data sources.

If the operation is prevented, the aborted exception will be thrown.

`optional int64 version_number = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the versionNumber field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
