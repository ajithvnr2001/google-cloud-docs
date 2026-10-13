---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.CompetitiveVisibilityCompetitorViewOrBuilder
title: Interface CompetitiveVisibilityCompetitorViewOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:05.833146+00:00
---

# Interface CompetitiveVisibilityCompetitorViewOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.CompetitiveVisibilityCompetitorViewOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CompetitiveVisibilityCompetitorViewOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.46.0  0.44.0  0.43.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    public interface CompetitiveVisibilityCompetitorViewOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdsOrganicRatio()
    
    
    public abstract double getAdsOrganicRatio()

[Ads / organic ratio](https://support.google.com/merchants/answer/11366442#zippy=%2Cads-free-ratio) shows how often the domain receives impressions from Shopping ads compared to organic traffic. The number is rounded and bucketed.

Cannot be filtered on in the 'WHERE' clause.

`optional double ads_organic_ratio = 8;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The adsOrganicRatio.  
  
### getDate()
    
    
    public abstract Date getDate()

Date of this row.

A condition on `date` is required in the `WHERE` clause.

`.google.type.Date date = 1;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Date` | The date.  
  
### getDateOrBuilder()
    
    
    public abstract DateOrBuilder getDateOrBuilder()

Date of this row.

A condition on `date` is required in the `WHERE` clause.

`.google.type.Date date = 1;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.DateOrBuilder` |   
  
### getDomain()
    
    
    public abstract String getDomain()

Domain of your competitor or your domain, if 'is_your_domain' is true.

Required in the `SELECT` clause. Cannot be filtered on in the 'WHERE' clause.

`optional string domain = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The domain.  
  
### getDomainBytes()
    
    
    public abstract ByteString getDomainBytes()

Domain of your competitor or your domain, if 'is_your_domain' is true.

Required in the `SELECT` clause. Cannot be filtered on in the 'WHERE' clause.

`optional string domain = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for domain.  
  
### getHigherPositionRate()
    
    
    public abstract double getHigherPositionRate()

[Higher position rate](https://support.google.com/merchants/answer/11366442#zippy=%2Chigher-position-rate) shows how often a competitor’s offer got placed in a higher position on the page than your offer.

Cannot be filtered on in the 'WHERE' clause.

`optional double higher_position_rate = 10;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The higherPositionRate.  
  
### getIsYourDomain()
    
    
    public abstract boolean getIsYourDomain()

True if this row contains data for your domain.

Cannot be filtered on in the 'WHERE' clause.

`optional bool is_your_domain = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isYourDomain.  
  
### getPageOverlapRate()
    
    
    public abstract double getPageOverlapRate()

[Page overlap rate](https://support.google.com/merchants/answer/11366442#zippy=%2Cpage-overlap-rate) shows how frequently competing retailers’ offers are shown together with your offers on the same page.

Cannot be filtered on in the 'WHERE' clause.

`optional double page_overlap_rate = 9;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageOverlapRate.  
  
### getRank()
    
    
    public abstract long getRank()

Position of the domain in the similar businesses ranking for the selected keys (`date`, `report_category_id`, `report_country_code`, `traffic_source`) based on impressions. 1 is the highest.

Cannot be filtered on in the 'WHERE' clause.

`optional int64 rank = 7;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The rank.  
  
### getRelativeVisibility()
    
    
    public abstract double getRelativeVisibility()

[Relative visibility](https://support.google.com/merchants/answer/11366442#zippy=%2Crelative-visibility) shows how often your competitors’ offers are shown compared to your offers. In other words, this is the number of displayed impressions of a competitor retailer divided by the number of your displayed impressions during a selected time range for a selected product category and country.

Cannot be filtered on in the 'WHERE' clause.

`optional double relative_visibility = 11;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The relativeVisibility.  
  
### getReportCategoryId()
    
    
    public abstract long getReportCategoryId()

Google product category ID to calculate the report for, represented in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

Required in the `SELECT` clause. A condition on `report_category_id` is required in the `WHERE` clause.

`optional int64 report_category_id = 5;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reportCategoryId.  
  
### getReportCountryCode()
    
    
    public abstract String getReportCountryCode()

Country where impressions appeared.

Required in the `SELECT` clause. A condition on `report_country_code` is required in the `WHERE` clause.

`optional string report_country_code = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The reportCountryCode.  
  
### getReportCountryCodeBytes()
    
    
    public abstract ByteString getReportCountryCodeBytes()

Country where impressions appeared.

Required in the `SELECT` clause. A condition on `report_country_code` is required in the `WHERE` clause.

`optional string report_country_code = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for reportCountryCode.  
  
### getTrafficSource()
    
    
    public abstract TrafficSource.TrafficSourceEnum getTrafficSource()

Traffic source of impressions.

Required in the `SELECT` clause.

` optional .google.shopping.merchant.reports.v1alpha.TrafficSource.TrafficSourceEnum traffic_source = 6; `

**Returns**  
---  
**Type** | **Description**  
`[TrafficSource.TrafficSourceEnum](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.TrafficSource.TrafficSourceEnum)` | The trafficSource.  
  
### getTrafficSourceValue()
    
    
    public abstract int getTrafficSourceValue()

Traffic source of impressions.

Required in the `SELECT` clause.

` optional .google.shopping.merchant.reports.v1alpha.TrafficSource.TrafficSourceEnum traffic_source = 6; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for trafficSource.  
  
### hasAdsOrganicRatio()
    
    
    public abstract boolean hasAdsOrganicRatio()

[Ads / organic ratio](https://support.google.com/merchants/answer/11366442#zippy=%2Cads-free-ratio) shows how often the domain receives impressions from Shopping ads compared to organic traffic. The number is rounded and bucketed.

Cannot be filtered on in the 'WHERE' clause.

`optional double ads_organic_ratio = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adsOrganicRatio field is set.  
  
### hasDate()
    
    
    public abstract boolean hasDate()

Date of this row.

A condition on `date` is required in the `WHERE` clause.

`.google.type.Date date = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the date field is set.  
  
### hasDomain()
    
    
    public abstract boolean hasDomain()

Domain of your competitor or your domain, if 'is_your_domain' is true.

Required in the `SELECT` clause. Cannot be filtered on in the 'WHERE' clause.

`optional string domain = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the domain field is set.  
  
### hasHigherPositionRate()
    
    
    public abstract boolean hasHigherPositionRate()

[Higher position rate](https://support.google.com/merchants/answer/11366442#zippy=%2Chigher-position-rate) shows how often a competitor’s offer got placed in a higher position on the page than your offer.

Cannot be filtered on in the 'WHERE' clause.

`optional double higher_position_rate = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the higherPositionRate field is set.  
  
### hasIsYourDomain()
    
    
    public abstract boolean hasIsYourDomain()

True if this row contains data for your domain.

Cannot be filtered on in the 'WHERE' clause.

`optional bool is_your_domain = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the isYourDomain field is set.  
  
### hasPageOverlapRate()
    
    
    public abstract boolean hasPageOverlapRate()

[Page overlap rate](https://support.google.com/merchants/answer/11366442#zippy=%2Cpage-overlap-rate) shows how frequently competing retailers’ offers are shown together with your offers on the same page.

Cannot be filtered on in the 'WHERE' clause.

`optional double page_overlap_rate = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pageOverlapRate field is set.  
  
### hasRank()
    
    
    public abstract boolean hasRank()

Position of the domain in the similar businesses ranking for the selected keys (`date`, `report_category_id`, `report_country_code`, `traffic_source`) based on impressions. 1 is the highest.

Cannot be filtered on in the 'WHERE' clause.

`optional int64 rank = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rank field is set.  
  
### hasRelativeVisibility()
    
    
    public abstract boolean hasRelativeVisibility()

[Relative visibility](https://support.google.com/merchants/answer/11366442#zippy=%2Crelative-visibility) shows how often your competitors’ offers are shown compared to your offers. In other words, this is the number of displayed impressions of a competitor retailer divided by the number of your displayed impressions during a selected time range for a selected product category and country.

Cannot be filtered on in the 'WHERE' clause.

`optional double relative_visibility = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the relativeVisibility field is set.  
  
### hasReportCategoryId()
    
    
    public abstract boolean hasReportCategoryId()

Google product category ID to calculate the report for, represented in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

Required in the `SELECT` clause. A condition on `report_category_id` is required in the `WHERE` clause.

`optional int64 report_category_id = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reportCategoryId field is set.  
  
### hasReportCountryCode()
    
    
    public abstract boolean hasReportCountryCode()

Country where impressions appeared.

Required in the `SELECT` clause. A condition on `report_country_code` is required in the `WHERE` clause.

`optional string report_country_code = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reportCountryCode field is set.  
  
### hasTrafficSource()
    
    
    public abstract boolean hasTrafficSource()

Traffic source of impressions.

Required in the `SELECT` clause.

` optional .google.shopping.merchant.reports.v1alpha.TrafficSource.TrafficSourceEnum traffic_source = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trafficSource field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
