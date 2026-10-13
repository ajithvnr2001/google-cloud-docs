---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourceOrBuilder
title: Interface DataSourceOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:38.966251+00:00
---

# Interface DataSourceOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataSourceOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DataSourceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDataSourceId()
    
    
    public abstract long getDataSourceId()

Output only. The data source id.

`int64 data_source_id = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The dataSourceId.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. The displayed data source name in the Merchant Center UI.

`string display_name = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. The displayed data source name in the Merchant Center UI.

`string display_name = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getFileInput()
    
    
    public abstract FileInput getFileInput()

Optional. The field is used only when data is managed through a file.

` .google.shopping.merchant.datasources.v1.FileInput file_input = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FileInput](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.FileInput)` | The fileInput.  
  
### getFileInputOrBuilder()
    
    
    public abstract FileInputOrBuilder getFileInputOrBuilder()

Optional. The field is used only when data is managed through a file.

` .google.shopping.merchant.datasources.v1.FileInput file_input = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FileInputOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.FileInputOrBuilder)` |   
  
### getInput()
    
    
    public abstract DataSource.Input getInput()

Output only. Determines the type of input to the data source. Based on the input some settings might not work. Only generic data sources can be created through the API.

` .google.shopping.merchant.datasources.v1.DataSource.Input input = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataSource.Input](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource.Input)` | The input.  
  
### getInputValue()
    
    
    public abstract int getInputValue()

Output only. Determines the type of input to the data source. Based on the input some settings might not work. Only generic data sources can be created through the API.

` .google.shopping.merchant.datasources.v1.DataSource.Input input = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for input.  
  
### getLocalInventoryDataSource()
    
    
    public abstract LocalInventoryDataSource getLocalInventoryDataSource()

The [local inventory](https://support.google.com/merchants/answer/7023001) data source.

` .google.shopping.merchant.datasources.v1.LocalInventoryDataSource local_inventory_data_source = 6; `

**Returns**  
---  
**Type** | **Description**  
`[LocalInventoryDataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.LocalInventoryDataSource)` | The localInventoryDataSource.  
  
### getLocalInventoryDataSourceOrBuilder()
    
    
    public abstract LocalInventoryDataSourceOrBuilder getLocalInventoryDataSourceOrBuilder()

The [local inventory](https://support.google.com/merchants/answer/7023001) data source.

` .google.shopping.merchant.datasources.v1.LocalInventoryDataSource local_inventory_data_source = 6; `

**Returns**  
---  
**Type** | **Description**  
`[LocalInventoryDataSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.LocalInventoryDataSourceOrBuilder)` |   
  
### getMerchantReviewDataSource()
    
    
    public abstract MerchantReviewDataSource getMerchantReviewDataSource()

The [merchant review](https://support.google.com/merchants/answer/7045996) data source.

` .google.shopping.merchant.datasources.v1.MerchantReviewDataSource merchant_review_data_source = 12; `

**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewDataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.MerchantReviewDataSource)` | The merchantReviewDataSource.  
  
### getMerchantReviewDataSourceOrBuilder()
    
    
    public abstract MerchantReviewDataSourceOrBuilder getMerchantReviewDataSourceOrBuilder()

The [merchant review](https://support.google.com/merchants/answer/7045996) data source.

` .google.shopping.merchant.datasources.v1.MerchantReviewDataSource merchant_review_data_source = 12; `

**Returns**  
---  
**Type** | **Description**  
`[MerchantReviewDataSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.MerchantReviewDataSourceOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Required. Identifier. The name of the data source. Format: `accounts/{account}/dataSources/{datasource}`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. Identifier. The name of the data source. Format: `accounts/{account}/dataSources/{datasource}`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPrimaryProductDataSource()
    
    
    public abstract PrimaryProductDataSource getPrimaryProductDataSource()

The [primary data source](https://support.google.com/merchants/answer/7439058) for local and online products.

` .google.shopping.merchant.datasources.v1.PrimaryProductDataSource primary_product_data_source = 4; `

**Returns**  
---  
**Type** | **Description**  
`[PrimaryProductDataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.PrimaryProductDataSource)` | The primaryProductDataSource.  
  
### getPrimaryProductDataSourceOrBuilder()
    
    
    public abstract PrimaryProductDataSourceOrBuilder getPrimaryProductDataSourceOrBuilder()

The [primary data source](https://support.google.com/merchants/answer/7439058) for local and online products.

` .google.shopping.merchant.datasources.v1.PrimaryProductDataSource primary_product_data_source = 4; `

**Returns**  
---  
**Type** | **Description**  
`[PrimaryProductDataSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.PrimaryProductDataSourceOrBuilder)` |   
  
### getProductReviewDataSource()
    
    
    public abstract ProductReviewDataSource getProductReviewDataSource()

The [product review](https://support.google.com/merchants/answer/7045996) data source.

` .google.shopping.merchant.datasources.v1.ProductReviewDataSource product_review_data_source = 9; `

**Returns**  
---  
**Type** | **Description**  
`[ProductReviewDataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.ProductReviewDataSource)` | The productReviewDataSource.  
  
### getProductReviewDataSourceOrBuilder()
    
    
    public abstract ProductReviewDataSourceOrBuilder getProductReviewDataSourceOrBuilder()

The [product review](https://support.google.com/merchants/answer/7045996) data source.

` .google.shopping.merchant.datasources.v1.ProductReviewDataSource product_review_data_source = 9; `

**Returns**  
---  
**Type** | **Description**  
`[ProductReviewDataSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.ProductReviewDataSourceOrBuilder)` |   
  
### getPromotionDataSource()
    
    
    public abstract PromotionDataSource getPromotionDataSource()

The [promotion](https://support.google.com/merchants/answer/2906014) data source.

`.google.shopping.merchant.datasources.v1.PromotionDataSource promotion_data_source = 8; `

**Returns**  
---  
**Type** | **Description**  
`[PromotionDataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.PromotionDataSource)` | The promotionDataSource.  
  
### getPromotionDataSourceOrBuilder()
    
    
    public abstract PromotionDataSourceOrBuilder getPromotionDataSourceOrBuilder()

The [promotion](https://support.google.com/merchants/answer/2906014) data source.

`.google.shopping.merchant.datasources.v1.PromotionDataSource promotion_data_source = 8; `

**Returns**  
---  
**Type** | **Description**  
`[PromotionDataSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.PromotionDataSourceOrBuilder)` |   
  
### getRegionalInventoryDataSource()
    
    
    public abstract RegionalInventoryDataSource getRegionalInventoryDataSource()

The [regional inventory](https://support.google.com/merchants/answer/7439058) data source.

` .google.shopping.merchant.datasources.v1.RegionalInventoryDataSource regional_inventory_data_source = 7; `

**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryDataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.RegionalInventoryDataSource)` | The regionalInventoryDataSource.  
  
### getRegionalInventoryDataSourceOrBuilder()
    
    
    public abstract RegionalInventoryDataSourceOrBuilder getRegionalInventoryDataSourceOrBuilder()

The [regional inventory](https://support.google.com/merchants/answer/7439058) data source.

` .google.shopping.merchant.datasources.v1.RegionalInventoryDataSource regional_inventory_data_source = 7; `

**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryDataSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.RegionalInventoryDataSourceOrBuilder)` |   
  
### getSupplementalProductDataSource()
    
    
    public abstract SupplementalProductDataSource getSupplementalProductDataSource()

The [supplemental data source](https://support.google.com/merchants/answer/7439058) for local and online products.

` .google.shopping.merchant.datasources.v1.SupplementalProductDataSource supplemental_product_data_source = 5; `

**Returns**  
---  
**Type** | **Description**  
`[SupplementalProductDataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.SupplementalProductDataSource)` | The supplementalProductDataSource.  
  
### getSupplementalProductDataSourceOrBuilder()
    
    
    public abstract SupplementalProductDataSourceOrBuilder getSupplementalProductDataSourceOrBuilder()

The [supplemental data source](https://support.google.com/merchants/answer/7439058) for local and online products.

` .google.shopping.merchant.datasources.v1.SupplementalProductDataSource supplemental_product_data_source = 5; `

**Returns**  
---  
**Type** | **Description**  
`[SupplementalProductDataSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.SupplementalProductDataSourceOrBuilder)` |   
  
### getTypeCase()
    
    
    public abstract DataSource.TypeCase getTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[DataSource.TypeCase](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource.TypeCase)` |   
  
### hasFileInput()
    
    
    public abstract boolean hasFileInput()

Optional. The field is used only when data is managed through a file.

` .google.shopping.merchant.datasources.v1.FileInput file_input = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fileInput field is set.  
  
### hasLocalInventoryDataSource()
    
    
    public abstract boolean hasLocalInventoryDataSource()

The [local inventory](https://support.google.com/merchants/answer/7023001) data source.

` .google.shopping.merchant.datasources.v1.LocalInventoryDataSource local_inventory_data_source = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the localInventoryDataSource field is set.  
  
### hasMerchantReviewDataSource()
    
    
    public abstract boolean hasMerchantReviewDataSource()

The [merchant review](https://support.google.com/merchants/answer/7045996) data source.

` .google.shopping.merchant.datasources.v1.MerchantReviewDataSource merchant_review_data_source = 12; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the merchantReviewDataSource field is set.  
  
### hasPrimaryProductDataSource()
    
    
    public abstract boolean hasPrimaryProductDataSource()

The [primary data source](https://support.google.com/merchants/answer/7439058) for local and online products.

` .google.shopping.merchant.datasources.v1.PrimaryProductDataSource primary_product_data_source = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the primaryProductDataSource field is set.  
  
### hasProductReviewDataSource()
    
    
    public abstract boolean hasProductReviewDataSource()

The [product review](https://support.google.com/merchants/answer/7045996) data source.

` .google.shopping.merchant.datasources.v1.ProductReviewDataSource product_review_data_source = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productReviewDataSource field is set.  
  
### hasPromotionDataSource()
    
    
    public abstract boolean hasPromotionDataSource()

The [promotion](https://support.google.com/merchants/answer/2906014) data source.

`.google.shopping.merchant.datasources.v1.PromotionDataSource promotion_data_source = 8; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the promotionDataSource field is set.  
  
### hasRegionalInventoryDataSource()
    
    
    public abstract boolean hasRegionalInventoryDataSource()

The [regional inventory](https://support.google.com/merchants/answer/7439058) data source.

` .google.shopping.merchant.datasources.v1.RegionalInventoryDataSource regional_inventory_data_source = 7; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the regionalInventoryDataSource field is set.  
  
### hasSupplementalProductDataSource()
    
    
    public abstract boolean hasSupplementalProductDataSource()

The [supplemental data source](https://support.google.com/merchants/answer/7439058) for local and online products.

` .google.shopping.merchant.datasources.v1.SupplementalProductDataSource supplemental_product_data_source = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the supplementalProductDataSource field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
