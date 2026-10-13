---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/setDefaultBranch/
title: Method: projects.locations.catalogs.setDefaultBranch \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:11.614895+00:00
---

# Method: projects.locations.catalogs.setDefaultBranch  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/setDefaultBranch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.setDefaultBranch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Set a specified branch id as default branch. API methods such as `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#google.cloud.retail.v2.SearchService.Search)`, `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2.ProductService.GetProduct)`, `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2.ProductService.ListProducts)` will treat requests using "default_branch" to the actual branch id set as default.

For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting `[SearchRequest.branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.branch)` to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting `[SearchRequest.branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.branch)` to `projects/*/locations/*/catalogs/*/branches/1`.

Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as `[SearchRequest.branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.branch)` to route the traffic to this staging branch.

CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one.

More specifically:

  * PredictionService will only return product IDs from branch {newBranch}.
  * SearchService will only return product IDs from branch {newBranch} (if branch is not explicitly set).
  * UserEventService will only join events with products from branch {newBranch}.



### HTTP request

`POST https://retail.googleapis.com/v2/{catalog=projects/*/locations/*/catalogs/*}:setDefaultBranch`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`catalog` |  `string` Full resource name of the catalog, such as `projects/*/locations/global/catalogs/default_catalog`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "branchId": string,
      "note": string,
      "force": boolean
    }  
  
Fields  
---  
`branchId` |  `string` The final component of the resource name of a branch.This field must be one of "0", "1" or "2". Otherwise, an INVALID_ARGUMENT error is returned.If there are no sufficient active products in the targeted branch and `[force](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/setDefaultBranch#body.request_body.FIELDS.force)` is not set, a FAILED_PRECONDITION error is returned.  
`note` |  `string` Some note on this request, this can be retrieved by `[CatalogService.GetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getDefaultBranch#google.cloud.retail.v2.CatalogService.GetDefaultBranch)` before next valid default branch set occurs.This field must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`force` |  `boolean` If set to true, it permits switching to a branch with `[branchId](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/setDefaultBranch#body.request_body.FIELDS.branch_id)` even if it has no sufficient active products.  
  
### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `catalog` resource:

  * `retail.catalogs.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
