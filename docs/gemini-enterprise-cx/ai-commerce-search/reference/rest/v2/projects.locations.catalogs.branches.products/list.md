---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list/
title: Method: projects.locations.catalogs.branches.products.list \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:13.278520+00:00
---

# Method: projects.locations.catalogs.branches.products.list  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.branches.products.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Gets a list of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s.

### HTTP request

`GET https://retail.googleapis.com/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent branch resource name, such as `projects/*/locations/global/catalogs/default_catalog/branches/0`. Use `default_branch` as the branch ID, to list products under the default branch.If the caller does not have permission to list `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s under this branch, regardless of whether or not this branch exists, a PERMISSION_DENIED error is returned.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s to return. If unspecified, defaults to 100. The maximum allowed value is 1000. Values above 1000 will be coerced to 1000.If this field is negative, an INVALID_ARGUMENT error is returned.  
`pageToken` |  `string` A page token `[ListProductsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list#body.ListProductsResponse.FIELDS.next_page_token)`, received from a previous `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2.ProductService.ListProducts)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2.ProductService.ListProducts)` must match the call that provided the page token. Otherwise, an INVALID_ARGUMENT error is returned.  
`filter` |  `string` A filter to apply on the list results. Supported features:

  * List all the products under the parent branch if `[filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list#body.QUERY_PARAMETERS.filter)` is unset.
  * List `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s sharing the same `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`. For example: `primaryProductId = "some_product_id"`
  * List `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s bundled in a `[Product.Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`. For example: `collection_product_id = "some_product_id"`
  * List `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s with a partibular type. For example: `type = "PRIMARY"` `type = "VARIANT"` `type = "COLLECTION"`

If the field is unrecognizable, an INVALID_ARGUMENT error is returned.If the specified `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` or `[Product.Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` does not exist, a NOT_FOUND error is returned.  
`readMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The fields of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` to return in the responses. If not set or empty, the following fields are returned:

  * `[Product.name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.name)`
  * `[Product.id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.id)`
  * `[Product.title](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.title)`
  * `[Product.uri](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.uri)`
  * `[Product.images](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.images)`
  * `[Product.price_info](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.price_info)`
  * `[Product.brands](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.brands)`

If "*" is provided, all fields are returned. `[Product.name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.name)` is always returned no matter what mask is set.If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2.ProductService.ListProducts)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "products": [
        {
          object ([Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`products[]` |  `object (`[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`)` The `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s.  
`nextPageToken` |  `string` A token that can be sent as `[ListProductsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `retail.products.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
