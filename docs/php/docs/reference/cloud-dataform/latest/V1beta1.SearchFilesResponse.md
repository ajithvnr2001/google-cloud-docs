---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.SearchFilesResponse
title: Google Cloud Dataform V1beta1 Client - Class SearchFilesResponse (0.17.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:09.271603+00:00
---

# Google Cloud Dataform V1beta1 Client - Class SearchFilesResponse (0.17.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.SearchFilesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataform V1beta1 Client - Class SearchFilesResponse (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.3  0.12.0  0.11.0  0.10.1  0.9.2  0.8.1  0.7.0  0.6.0  0.5.1  0.4.7  0.3.0  0.2.3  0.1.6 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataform V1beta1 Client class SearchFilesResponse.

Client-facing representation of a file search response.

Generated from protobuf message `google.cloud.dataform.v1beta1.SearchFilesResponse`

## Namespace

Google \ Cloud \ Dataform \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ search_results` |  `array<[SearchResult](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.SearchResult)>`   
List of matched results.  
`↳ next_page_token` |  `string`   
Optional. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### getSearchResults

List of matched results.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[SearchResult](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.SearchResult)>` |   
  
### setSearchResults

List of matched results.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[SearchResult](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.SearchResult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNextPageToken

Optional. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setNextPageToken

Optional. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

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

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
