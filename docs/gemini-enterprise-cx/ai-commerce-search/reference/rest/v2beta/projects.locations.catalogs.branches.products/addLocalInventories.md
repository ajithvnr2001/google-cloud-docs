---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addLocalInventories/
title: Method: projects.locations.catalogs.branches.products.addLocalInventories \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:27.064991+00:00
---

# Method: projects.locations.catalogs.branches.products.addLocalInventories  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/addLocalInventories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.branches.products.addLocalInventories Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Updates local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` at a list of places, while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` queried by `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2beta.ProductService.GetProduct)` or `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2beta.ProductService.ListProducts)`.

Local inventory information can only be modified using this method. `[ProductService.CreateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/create#google.cloud.retail.v2beta.ProductService.CreateProduct)` and `[ProductService.UpdateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/patch#google.cloud.retail.v2beta.ProductService.UpdateProduct)` has no effect on local inventories.

The returned `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`s will be obsolete after 1 day, and `[operations.get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations/get#google.longrunning.Operations.GetOperation)` API will return NOT_FOUND afterwards.

If conflicting updates are issued, the `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`s associated with the stale updates will not be marked as `[done](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.done)` until being obsolete.

### HTTP request

`POST https://retail.googleapis.com/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories`

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
      "localInventories": [
        {
          object ([LocalInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.LocalInventory))
        }
      ],
      "addMask": string,
      "addTime": string,
      "allowMissing": boolean
    }  
  
Fields  
---  
`localInventories[]` |  `object (`[LocalInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.LocalInventory)`)` Required. A list of inventory information at difference places. Each place is identified by its place ID. At most 3000 inventories are allowed per request.  
`addMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Indicates which inventory fields in the provided list of `[LocalInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.LocalInventory)` to update. The field is updated to the provided value.If a field is set while the place does not have a previous local inventory, the local inventory at that store is created.If a field is set while the value of that field is not provided, the original field value, if it exists, is deleted.If the mask is not set or set with empty paths, all inventory fields will be updated.If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`addTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the inventory updates are issued. Used to prevent out-of-order updates on local inventory fields. If not provided, the internal system time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`allowMissing` |  `boolean` If set to true, and the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` is not found, the local inventory will still be processed and retained for at most 1 day and processed once the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` is created. If set to false, a NOT_FOUND error is returned if the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` is not found.  
  
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
