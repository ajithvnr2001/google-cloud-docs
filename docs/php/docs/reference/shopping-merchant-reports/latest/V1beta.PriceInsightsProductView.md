---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reports/latest/V1beta.PriceInsightsProductView
title: Google Shopping Merchant Reports V1beta Client - Class PriceInsightsProductView (1.4.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:25.228315+00:00
---

# Google Shopping Merchant Reports V1beta Client - Class PriceInsightsProductView (1.4.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reports/latest/V1beta.PriceInsightsProductView

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Reports V1beta Client - Class PriceInsightsProductView (1.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.2 (latest)  1.3.0  1.2.1  1.1.3  1.0.0  0.10.0  0.9.1  0.8.4  0.7.3  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Reports V1beta Client class PriceInsightsProductView.

Fields available for query in `price_insights_product_view` table.

[Price insights](https://support.google.com/merchants/answer/11916926) report. Values are only set for fields requested explicitly in the request's search query.

Generated from protobuf message `google.shopping.merchant.reports.v1beta.PriceInsightsProductView`

## Namespace

Google \ Shopping \ Merchant \ Reports \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ id` |  `string`   
REST ID of the product, in the form of `channel~languageCode~feedLabel~offerId`. Can be used to join data with the `product_view` table. Required in the `SELECT` clause.  
`↳ offer_id` |  `string`   
Merchant-provided id of the product.  
`↳ title` |  `string`   
Title of the product.  
`↳ brand` |  `string`   
Brand of the product.  
`↳ category_l1` |  `string`   
Product category (1st level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).  
`↳ category_l2` |  `string`   
Product category (2nd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).  
`↳ category_l3` |  `string`   
Product category (3rd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).  
`↳ category_l4` |  `string`   
Product category (4th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).  
`↳ category_l5` |  `string`   
Product category (5th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).  
`↳ product_type_l1` |  `string`   
Product type (1st level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).  
`↳ product_type_l2` |  `string`   
Product type (2nd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).  
`↳ product_type_l3` |  `string`   
Product type (3rd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).  
`↳ product_type_l4` |  `string`   
Product type (4th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).  
`↳ product_type_l5` |  `string`   
Product type (5th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).  
`↳ price` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
Current price of the product.  
`↳ suggested_price` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
Latest suggested price for the product.  
`↳ predicted_impressions_change_fraction` |  `float`   
Predicted change in impressions as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in impressions.  
`↳ predicted_clicks_change_fraction` |  `float`   
Predicted change in clicks as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in clicks.  
`↳ predicted_conversions_change_fraction` |  `float`   
Predicted change in conversions as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in conversions).  
`↳ effectiveness` |  `int`   
The predicted effectiveness of applying the price suggestion, bucketed.  
  
### getId

REST ID of the product, in the form of `channel~languageCode~feedLabel~offerId`. Can be used to join data with the `product_view` table.

Required in the `SELECT` clause.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasId

### clearId

### setId

REST ID of the product, in the form of `channel~languageCode~feedLabel~offerId`. Can be used to join data with the `product_view` table.

Required in the `SELECT` clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOfferId

Merchant-provided id of the product.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasOfferId

### clearOfferId

### setOfferId

Merchant-provided id of the product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTitle

Title of the product.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasTitle

### clearTitle

### setTitle

Title of the product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBrand

Brand of the product.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasBrand

### clearBrand

### setBrand

Brand of the product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCategoryL1

Product category (1st level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasCategoryL1

### clearCategoryL1

### setCategoryL1

Product category (1st level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCategoryL2

Product category (2nd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasCategoryL2

### clearCategoryL2

### setCategoryL2

Product category (2nd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCategoryL3

Product category (3rd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasCategoryL3

### clearCategoryL3

### setCategoryL3

Product category (3rd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCategoryL4

Product category (4th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasCategoryL4

### clearCategoryL4

### setCategoryL4

Product category (4th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCategoryL5

Product category (5th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasCategoryL5

### clearCategoryL5

### setCategoryL5

Product category (5th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProductTypeL1

Product type (1st level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasProductTypeL1

### clearProductTypeL1

### setProductTypeL1

Product type (1st level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProductTypeL2

Product type (2nd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasProductTypeL2

### clearProductTypeL2

### setProductTypeL2

Product type (2nd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProductTypeL3

Product type (3rd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasProductTypeL3

### clearProductTypeL3

### setProductTypeL3

Product type (3rd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProductTypeL4

Product type (4th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasProductTypeL4

### clearProductTypeL4

### setProductTypeL4

Product type (4th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProductTypeL5

Product type (5th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasProductTypeL5

### clearProductTypeL5

### setProductTypeL5

Product type (5th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPrice

Current price of the product.

**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)|null` |   
  
### hasPrice

### clearPrice

### setPrice

Current price of the product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSuggestedPrice

Latest suggested price for the product.

**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)|null` |   
  
### hasSuggestedPrice

### clearSuggestedPrice

### setSuggestedPrice

Latest suggested price for the product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPredictedImpressionsChangeFraction

Predicted change in impressions as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in impressions.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasPredictedImpressionsChangeFraction

### clearPredictedImpressionsChangeFraction

### setPredictedImpressionsChangeFraction

Predicted change in impressions as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in impressions.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPredictedClicksChangeFraction

Predicted change in clicks as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in clicks.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasPredictedClicksChangeFraction

### clearPredictedClicksChangeFraction

### setPredictedClicksChangeFraction

Predicted change in clicks as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in clicks.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPredictedConversionsChangeFraction

Predicted change in conversions as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in conversions).

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasPredictedConversionsChangeFraction

### clearPredictedConversionsChangeFraction

### setPredictedConversionsChangeFraction

Predicted change in conversions as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in conversions).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEffectiveness

The predicted effectiveness of applying the price suggestion, bucketed.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Effectiveness](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reports/latest/V1beta.PriceInsightsProductView.Effectiveness).  
  
### setEffectiveness

The predicted effectiveness of applying the price suggestion, bucketed.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Effectiveness](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reports/latest/V1beta.PriceInsightsProductView.Effectiveness).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
