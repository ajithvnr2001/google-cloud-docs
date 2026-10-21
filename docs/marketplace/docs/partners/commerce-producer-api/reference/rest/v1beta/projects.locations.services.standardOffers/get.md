---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers/get/
title: Method: projects.locations.services.standardOffers.get \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:16.379569+00:00
---

# Method: projects.locations.services.standardOffers.get  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  Method: projects.locations.services.standardOffers.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * StandardOfferView



Gets details of a single StandardOffer.

### HTTP request

`GET https://commerceproducer.googleapis.com/v1beta/{name=projects/*/locations/*/services/*/standardOffers/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the resource  
  
### Query parameters

Parameters  
---  
`view` |  `enum (`[StandardOfferView](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers/get#StandardOfferView)`)` Optional. The view of the StandardOffer to return. If unspecified, the default view is BASIC.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[StandardOffer](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#StandardOffer)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `commerceproducer.standardOffers.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## StandardOfferView

Controls which fields are returned in a StandardOffer returned by the API. <https://google.aip.dev/157>

Enums  
---  
`STANDARD_OFFER_VIEW_UNSPECIFIED` | The default / unset value. The API will default to the BASIC view.  
`STANDARD_OFFER_VIEW_BASIC` | Include basic metadata about the StandardOffer, but not the full contents. This is the default value (for both List and Get requests).  
`STANDARD_OFFER_VIEW_FULL` | Include everything.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
