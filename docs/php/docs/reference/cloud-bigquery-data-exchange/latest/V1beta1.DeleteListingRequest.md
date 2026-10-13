---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery-data-exchange/latest/V1beta1.DeleteListingRequest
title: Google Cloud BigQuery Data Exchange V1beta1 Client - Class DeleteListingRequest (0.7.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:18.059714+00:00
---

# Google Cloud BigQuery Data Exchange V1beta1 Client - Class DeleteListingRequest (0.7.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery-data-exchange/latest/V1beta1.DeleteListingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud BigQuery Data Exchange V1beta1 Client - Class DeleteListingRequest (0.7.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.3 (latest)  0.6.3  0.5.2  0.4.7  0.3.3  0.2.6 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud BigQuery Data Exchange V1beta1 Client class DeleteListingRequest.

Message for deleting a listing.

Generated from protobuf message `google.cloud.bigquery.dataexchange.v1beta1.DeleteListingRequest`

## Namespace

Google \ Cloud \ BigQuery \ DataExchange \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Required. Resource name of the listing to delete. e.g. `projects/myproject/locations/US/dataExchanges/123/listings/456`.  
  
### getName

Required. Resource name of the listing to delete.

e.g. `projects/myproject/locations/US/dataExchanges/123/listings/456`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Required. Resource name of the listing to delete.

e.g. `projects/myproject/locations/US/dataExchanges/123/listings/456`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
Required. Resource name of the listing to delete. e.g. `projects/myproject/locations/US/dataExchanges/123/listings/456`. Please see AnalyticsHubServiceClient::listingName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteListingRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery-data-exchange/latest/V1beta1.DeleteListingRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
