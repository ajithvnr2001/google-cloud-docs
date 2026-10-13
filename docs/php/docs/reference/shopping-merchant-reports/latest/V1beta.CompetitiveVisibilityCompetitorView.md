---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reports/latest/V1beta.CompetitiveVisibilityCompetitorView
title: Google Shopping Merchant Reports V1beta Client - Class CompetitiveVisibilityCompetitorView (1.4.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:02.447243+00:00
---

# Google Shopping Merchant Reports V1beta Client - Class CompetitiveVisibilityCompetitorView (1.4.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reports/latest/V1beta.CompetitiveVisibilityCompetitorView

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Reports V1beta Client - Class CompetitiveVisibilityCompetitorView (1.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.2 (latest)  1.3.0  1.2.1  1.1.3  1.0.0  0.10.0  0.9.1  0.8.4  0.7.3  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Reports V1beta Client class CompetitiveVisibilityCompetitorView.

Fields available for query in `competitive_visibility_competitor_view` table.

[Competitive visibility](https://support.google.com/merchants/answer/11366442) report with businesses with similar visibility. Values are only set for fields requested explicitly in the request's search query.

Generated from protobuf message `google.shopping.merchant.reports.v1beta.CompetitiveVisibilityCompetitorView`

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
`↳ date` |  `[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)`   
Date of this row. A condition on `date` is required in the `WHERE` clause.  
`↳ domain` |  `string`   
Domain of your competitor or your domain, if 'is_your_domain' is true. Required in the `SELECT` clause. Cannot be filtered on in the 'WHERE' clause.  
`↳ is_your_domain` |  `bool`   
True if this row contains data for your domain. Cannot be filtered on in the 'WHERE' clause.  
`↳ report_country_code` |  `string`   
Country where impressions appeared. Required in the `SELECT` clause. A condition on `report_country_code` is required in the `WHERE` clause.  
`↳ report_category_id` |  `int|string`   
Google product category ID to calculate the report for, represented in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436). Required in the `SELECT` clause. A condition on `report_category_id` is required in the `WHERE` clause.  
`↳ traffic_source` |  `int`   
Traffic source of impressions. Required in the `SELECT` clause.  
`↳ rank` |  `int|string`   
Position of the domain in the similar businesses ranking for the selected keys (`date`, `report_category_id`, `report_country_code`, `traffic_source`) based on impressions. 1 is the highest. Cannot be filtered on in the 'WHERE' clause.  
`↳ ads_organic_ratio` |  `float`   
[Ads / organic ratio](https://support.google.com/merchants/answer/11366442#zippy=%2Cads-free-ratio) shows how often the domain receives impressions from Shopping ads compared to organic traffic. The number is rounded and bucketed. Cannot be filtered on in the 'WHERE' clause.  
`↳ page_overlap_rate` |  `float`   
[Page overlap rate](https://support.google.com/merchants/answer/11366442#zippy=%2Cpage-overlap-rate) shows how frequently competing retailers’ offers are shown together with your offers on the same page. Cannot be filtered on in the 'WHERE' clause.  
`↳ higher_position_rate` |  `float`   
[Higher position rate](https://support.google.com/merchants/answer/11366442#zippy=%2Chigher-position-rate) shows how often a competitor’s offer got placed in a higher position on the page than your offer. Cannot be filtered on in the 'WHERE' clause.  
`↳ relative_visibility` |  `float`   
[Relative visibility](https://support.google.com/merchants/answer/11366442#zippy=%2Crelative-visibility) shows how often your competitors’ offers are shown compared to your offers. In other words, this is the number of displayed impressions of a competitor retailer divided by the number of your displayed impressions during a selected time range for a selected product category and country. Cannot be filtered on in the 'WHERE' clause.  
  
### getDate

Date of this row.

A condition on `date` is required in the `WHERE` clause.

**Returns**  
---  
**Type** | **Description**  
`[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)|null` |   
  
### hasDate

### clearDate

### setDate

Date of this row.

A condition on `date` is required in the `WHERE` clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDomain

Domain of your competitor or your domain, if 'is_your_domain' is true.

Required in the `SELECT` clause. Cannot be filtered on in the 'WHERE' clause.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasDomain

### clearDomain

### setDomain

Domain of your competitor or your domain, if 'is_your_domain' is true.

Required in the `SELECT` clause. Cannot be filtered on in the 'WHERE' clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIsYourDomain

True if this row contains data for your domain.

Cannot be filtered on in the 'WHERE' clause.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasIsYourDomain

### clearIsYourDomain

### setIsYourDomain

True if this row contains data for your domain.

Cannot be filtered on in the 'WHERE' clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReportCountryCode

Country where impressions appeared.

Required in the `SELECT` clause. A condition on `report_country_code` is required in the `WHERE` clause.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasReportCountryCode

### clearReportCountryCode

### setReportCountryCode

Country where impressions appeared.

Required in the `SELECT` clause. A condition on `report_country_code` is required in the `WHERE` clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReportCategoryId

Google product category ID to calculate the report for, represented in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

Required in the `SELECT` clause. A condition on `report_category_id` is required in the `WHERE` clause.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### hasReportCategoryId

### clearReportCategoryId

### setReportCategoryId

Google product category ID to calculate the report for, represented in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

Required in the `SELECT` clause. A condition on `report_category_id` is required in the `WHERE` clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTrafficSource

Traffic source of impressions.

Required in the `SELECT` clause.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasTrafficSource

### clearTrafficSource

### setTrafficSource

Traffic source of impressions.

Required in the `SELECT` clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRank

Position of the domain in the similar businesses ranking for the selected keys (`date`, `report_category_id`, `report_country_code`, `traffic_source`) based on impressions. 1 is the highest.

Cannot be filtered on in the 'WHERE' clause.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### hasRank

### clearRank

### setRank

Position of the domain in the similar businesses ranking for the selected keys (`date`, `report_category_id`, `report_country_code`, `traffic_source`) based on impressions. 1 is the highest.

Cannot be filtered on in the 'WHERE' clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdsOrganicRatio

[Ads / organic ratio](https://support.google.com/merchants/answer/11366442#zippy=%2Cads-free-ratio) shows how often the domain receives impressions from Shopping ads compared to organic traffic. The number is rounded and bucketed.

Cannot be filtered on in the 'WHERE' clause.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasAdsOrganicRatio

### clearAdsOrganicRatio

### setAdsOrganicRatio

[Ads / organic ratio](https://support.google.com/merchants/answer/11366442#zippy=%2Cads-free-ratio) shows how often the domain receives impressions from Shopping ads compared to organic traffic. The number is rounded and bucketed.

Cannot be filtered on in the 'WHERE' clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageOverlapRate

[Page overlap rate](https://support.google.com/merchants/answer/11366442#zippy=%2Cpage-overlap-rate) shows how frequently competing retailers’ offers are shown together with your offers on the same page.

Cannot be filtered on in the 'WHERE' clause.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasPageOverlapRate

### clearPageOverlapRate

### setPageOverlapRate

[Page overlap rate](https://support.google.com/merchants/answer/11366442#zippy=%2Cpage-overlap-rate) shows how frequently competing retailers’ offers are shown together with your offers on the same page.

Cannot be filtered on in the 'WHERE' clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getHigherPositionRate

[Higher position rate](https://support.google.com/merchants/answer/11366442#zippy=%2Chigher-position-rate) shows how often a competitor’s offer got placed in a higher position on the page than your offer.

Cannot be filtered on in the 'WHERE' clause.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasHigherPositionRate

### clearHigherPositionRate

### setHigherPositionRate

[Higher position rate](https://support.google.com/merchants/answer/11366442#zippy=%2Chigher-position-rate) shows how often a competitor’s offer got placed in a higher position on the page than your offer.

Cannot be filtered on in the 'WHERE' clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRelativeVisibility

[Relative visibility](https://support.google.com/merchants/answer/11366442#zippy=%2Crelative-visibility) shows how often your competitors’ offers are shown compared to your offers.

In other words, this is the number of displayed impressions of a competitor retailer divided by the number of your displayed impressions during a selected time range for a selected product category and country. Cannot be filtered on in the 'WHERE' clause.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasRelativeVisibility

### clearRelativeVisibility

### setRelativeVisibility

[Relative visibility](https://support.google.com/merchants/answer/11366442#zippy=%2Crelative-visibility) shows how often your competitors’ offers are shown compared to your offers.

In other words, this is the number of displayed impressions of a competitor retailer divided by the number of your displayed impressions during a selected time range for a selected product category and country. Cannot be filtered on in the 'WHERE' clause.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
