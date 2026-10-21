---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/purge/
title: Method: projects.locations.catalogs.branches.products.purge \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:18:20.834072+00:00
---

# Method: projects.locations.catalogs.branches.products.purge  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/purge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.branches.products.purge Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Permanently deletes all selected `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s under a branch.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s, this operation could take hours to complete. Before the operation completes, some `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s may still be returned by `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2alpha.ProductService.GetProduct)` or `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2alpha.ProductService.ListProducts)`.

Depending on the number of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s, this operation could take hours to complete. To get a sample of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s that would be deleted, set `[PurgeProductsRequest.force](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/purge#body.request_body.FIELDS.force)` to false.

### HTTP request

`POST https://retail.googleapis.com/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the branch under which the products are created. The format is `projects/${projectId}/locations/global/catalogs/${catalogId}/branches/${branchId}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": string,
      "force": boolean
    }  
  
Fields  
---  
`filter` |  `string` Required. The filter string to specify the products to be deleted with a length limit of 5,000 characters.Empty string filter is not allowed. "*" implies delete all items in a branch.The eligible fields for filtering are:

  * `availability`: Double quoted `[Product.availability](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.availability)` string.
  * `createTime` : in ISO 8601 "zulu" format.

Supported syntax:

  * Comparators (">", "<", ">=", "<=", "="). Examples:
  * createTime <= "2015-02-13T17:05:46Z"
  * availability = "IN_STOCK"
  * Conjunctions ("AND") Examples:
  * createTime <= "2015-02-13T17:05:46Z" AND availability = "PREORDER"
  * Disjunctions ("OR") Examples:
  * createTime <= "2015-02-13T17:05:46Z" OR availability = "IN_STOCK"
  * Can support nested queries. Examples:
  * (createTime <= "2015-02-13T17:05:46Z" AND availability = "PREORDER") OR (createTime >= "2015-02-14T13:03:32Z" AND availability = "IN_STOCK")
  * Filter Limits:
  * Filter should not contain more than 6 conditions.
  * Max nesting depth should not exceed 2 levels.

Examples queries: * Delete back order products created before a timestamp. createTime <= "2015-02-13T17:05:46Z" OR availability = "BACKORDER"  
`force` |  `boolean` Actually perform the purge. If `force` is set to false, the method will return the expected purge count without deleting any products.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `retail.products.purge`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
