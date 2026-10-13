---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addFulfillmentPlaces/
title: Method: projects.locations.catalogs.branches.products.addFulfillmentPlaces \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:27.468819+00:00
---

# Method: projects.locations.catalogs.branches.products.addFulfillmentPlaces  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addFulfillmentPlaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.branches.products.addFulfillmentPlaces Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



We recommend that you use the `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addLocalInventories#google.cloud.retail.v2beta.ProductService.AddLocalInventories)` method instead of the `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addFulfillmentPlaces#google.cloud.retail.v2beta.ProductService.AddFulfillmentPlaces)` method. `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addLocalInventories#google.cloud.retail.v2beta.ProductService.AddLocalInventories)` achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally adds place IDs to `[Product.fulfillment_info.place_ids](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.place_ids)`.

This process is asynchronous and does not require the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` queried by `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2beta.ProductService.GetProduct)` or `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2beta.ProductService.ListProducts)`.

The returned `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`s will be obsolete after 1 day, and `[operations.get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations/get#google.longrunning.Operations.GetOperation)` API will return NOT_FOUND afterwards.

If conflicting updates are issued, the `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`s associated with the stale updates will not be marked as `[done](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.done)` until being obsolete.

### HTTP request

`POST https://retail.googleapis.com/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`product` |  `string` Required. Full resource name of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.If the caller does not have permission to access the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "type": string,
      "placeIds": [
        string
      ],
      "addTime": string,
      "allowMissing": boolean
    }  
  
Fields  
---  
`type` |  `string` Required. The fulfillment type, including commonly used types (such as pickup in store and same day delivery), and custom types.Supported values:

  * "pickup-in-store"
  * "ship-to-store"
  * "same-day-delivery"
  * "next-day-delivery"
  * "custom-type-1"
  * "custom-type-2"
  * "custom-type-3"
  * "custom-type-4"
  * "custom-type-5"

If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned.This field directly corresponds to `[Product.fulfillment_info.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)`.  
`placeIds[]` |  `string` Required. The IDs for this `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addFulfillmentPlaces#body.request_body.FIELDS.type)`, such as the store IDs for "pickup-in-store" or the region IDs for "same-day-delivery" to be added for this `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addFulfillmentPlaces#body.request_body.FIELDS.type)`. Duplicate IDs will be automatically ignored.At least 1 value is required, and a maximum of 2000 values are allowed. Each value must be a string with a length limit of 10 characters, matching the pattern `[a-zA-Z0-9_-]+`, such as "store1" or "REGION-2". Otherwise, an INVALID_ARGUMENT error is returned.If the total number of place IDs exceeds 2000 for this `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addFulfillmentPlaces#body.request_body.FIELDS.type)` after adding, then the update will be rejected.  
`addTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the fulfillment updates are issued, used to prevent out-of-order updates on fulfillment information. If not provided, the internal system time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`allowMissing` |  `boolean` If set to true, and the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` is not found, the fulfillment information will still be processed and retained for at most 1 day and processed once the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` is created. If set to false, a NOT_FOUND error is returned if the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` is not found.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `product` resource:

  * `retail.products.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
