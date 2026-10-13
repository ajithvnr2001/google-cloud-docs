---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings
title: Google Analytics Admin V1alpha Client - Class EnhancedMeasurementSettings (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:05.389495+00:00
---

# Google Analytics Admin V1alpha Client - Class EnhancedMeasurementSettings (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EnhancedMeasurementSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class EnhancedMeasurementSettings (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class EnhancedMeasurementSettings.

Singleton resource under a web DataStream, configuring measurement of additional site interactions and content.

Generated from protobuf message `google.analytics.admin.v1alpha.EnhancedMeasurementSettings`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Output only. Resource name of the Enhanced Measurement Settings. Format: properties/{property_id}/dataStreams/{data_stream}/enhancedMeasurementSettings Example: "properties/1000/dataStreams/2000/enhancedMeasurementSettings"  
`↳ stream_enabled` |  `bool`   
Indicates whether Enhanced Measurement Settings will be used to automatically measure interactions and content on this web stream. Changing this value does not affect the settings themselves, but determines whether they are respected.  
`↳ scrolls_enabled` |  `bool`   
If enabled, capture scroll events each time a visitor gets to the bottom of a page.  
`↳ outbound_clicks_enabled` |  `bool`   
If enabled, capture an outbound click event each time a visitor clicks a link that leads them away from your domain.  
`↳ site_search_enabled` |  `bool`   
If enabled, capture a view search results event each time a visitor performs a search on your site (based on a query parameter).  
`↳ video_engagement_enabled` |  `bool`   
If enabled, capture video play, progress, and complete events as visitors view embedded videos on your site.  
`↳ file_downloads_enabled` |  `bool`   
If enabled, capture a file download event each time a link is clicked with a common document, compressed file, application, video, or audio extension.  
`↳ page_changes_enabled` |  `bool`   
If enabled, capture a page view event each time the website changes the browser history state.  
`↳ form_interactions_enabled` |  `bool`   
If enabled, capture a form interaction event each time a visitor interacts with a form on your website. False by default.  
`↳ search_query_parameter` |  `string`   
Required. URL query parameters to interpret as site search parameters. Max length is 1024 characters. Must not be empty.  
`↳ uri_query_parameter` |  `string`   
Additional URL query parameters. Max length is 1024 characters.  
  
### getName

Output only. Resource name of the Enhanced Measurement Settings.

Format: properties/{property_id}/dataStreams/{data_stream}/enhancedMeasurementSettings Example: "properties/1000/dataStreams/2000/enhancedMeasurementSettings"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Resource name of the Enhanced Measurement Settings.

Format: properties/{property_id}/dataStreams/{data_stream}/enhancedMeasurementSettings Example: "properties/1000/dataStreams/2000/enhancedMeasurementSettings"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStreamEnabled

Indicates whether Enhanced Measurement Settings will be used to automatically measure interactions and content on this web stream.

Changing this value does not affect the settings themselves, but determines whether they are respected.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setStreamEnabled

Indicates whether Enhanced Measurement Settings will be used to automatically measure interactions and content on this web stream.

Changing this value does not affect the settings themselves, but determines whether they are respected.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getScrollsEnabled

If enabled, capture scroll events each time a visitor gets to the bottom of a page.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setScrollsEnabled

If enabled, capture scroll events each time a visitor gets to the bottom of a page.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOutboundClicksEnabled

If enabled, capture an outbound click event each time a visitor clicks a link that leads them away from your domain.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setOutboundClicksEnabled

If enabled, capture an outbound click event each time a visitor clicks a link that leads them away from your domain.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSiteSearchEnabled

If enabled, capture a view search results event each time a visitor performs a search on your site (based on a query parameter).

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setSiteSearchEnabled

If enabled, capture a view search results event each time a visitor performs a search on your site (based on a query parameter).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getVideoEngagementEnabled

If enabled, capture video play, progress, and complete events as visitors view embedded videos on your site.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setVideoEngagementEnabled

If enabled, capture video play, progress, and complete events as visitors view embedded videos on your site.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFileDownloadsEnabled

If enabled, capture a file download event each time a link is clicked with a common document, compressed file, application, video, or audio extension.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setFileDownloadsEnabled

If enabled, capture a file download event each time a link is clicked with a common document, compressed file, application, video, or audio extension.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageChangesEnabled

If enabled, capture a page view event each time the website changes the browser history state.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setPageChangesEnabled

If enabled, capture a page view event each time the website changes the browser history state.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFormInteractionsEnabled

If enabled, capture a form interaction event each time a visitor interacts with a form on your website.

False by default.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setFormInteractionsEnabled

If enabled, capture a form interaction event each time a visitor interacts with a form on your website.

False by default.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSearchQueryParameter

Required. URL query parameters to interpret as site search parameters.

Max length is 1024 characters. Must not be empty.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSearchQueryParameter

Required. URL query parameters to interpret as site search parameters.

Max length is 1024 characters. Must not be empty.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUriQueryParameter

Additional URL query parameters.

Max length is 1024 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUriQueryParameter

Additional URL query parameters.

Max length is 1024 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
