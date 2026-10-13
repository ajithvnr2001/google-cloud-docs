---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.PageInfoOrBuilder
title: Interface PageInfoOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:41.667873+00:00
---

# Interface PageInfoOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.PageInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PageInfoOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface PageInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPageCategory()
    
    
    public abstract String getPageCategory()

The most specific category associated with a category page.

To represent full path of category, use '>' sign to separate different hierarchies. If '>' is part of the category name, replace it with other character(s).

Category pages include special pages such as sales or promotions. For instance, a special sale page may have the category hierarchy: `"pageCategory" : "Sales > 2017 Black Friday Deals"`.

Required for `view-category-page` events. Other event types should not set this field. Otherwise, an `INVALID_ARGUMENT` error is returned.

`string page_category = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageCategory.  
  
### getPageCategoryBytes()
    
    
    public abstract ByteString getPageCategoryBytes()

The most specific category associated with a category page.

To represent full path of category, use '>' sign to separate different hierarchies. If '>' is part of the category name, replace it with other character(s).

Category pages include special pages such as sales or promotions. For instance, a special sale page may have the category hierarchy: `"pageCategory" : "Sales > 2017 Black Friday Deals"`.

Required for `view-category-page` events. Other event types should not set this field. Otherwise, an `INVALID_ARGUMENT` error is returned.

`string page_category = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageCategory.  
  
### getPageviewId()
    
    
    public abstract String getPageviewId()

A unique ID of a web page view.

This should be kept the same for all user events triggered from the same pageview. For example, an item detail page view could trigger multiple events as the user is browsing the page. The `pageview_id` property should be kept the same for all these events so that they can be grouped together properly.

When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically.

`string pageview_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageviewId.  
  
### getPageviewIdBytes()
    
    
    public abstract ByteString getPageviewIdBytes()

A unique ID of a web page view.

This should be kept the same for all user events triggered from the same pageview. For example, an item detail page view could trigger multiple events as the user is browsing the page. The `pageview_id` property should be kept the same for all these events so that they can be grouped together properly.

When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically.

`string pageview_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageviewId.  
  
### getReferrerUri()
    
    
    public abstract String getReferrerUri()

The referrer URL of the current page.

When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically. However, some browser privacy restrictions may cause this field to be empty.

`string referrer_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The referrerUri.  
  
### getReferrerUriBytes()
    
    
    public abstract ByteString getReferrerUriBytes()

The referrer URL of the current page.

When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically. However, some browser privacy restrictions may cause this field to be empty.

`string referrer_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for referrerUri.  
  
### getUri()
    
    
    public abstract String getUri()

Complete URL (window.location.href) of the user's current page.

When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically. Maximum length 5,000 characters.

`string uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uri.  
  
### getUriBytes()
    
    
    public abstract ByteString getUriBytes()

Complete URL (window.location.href) of the user's current page.

When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically. Maximum length 5,000 characters.

`string uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uri.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
