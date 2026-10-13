---
url: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.taxonomies/patch/
title: Method: projects.locations.taxonomies.patch \u00a0|\u00a0 Data Catalog Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:26.257401+00:00
---

# Method: projects.locations.taxonomies.patch  |  Data Catalog Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.taxonomies/patch/

Data Catalog API methods that are related to Data Catalog search and metadata are deprecated and will be discontinued on June 1, 2026. See [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). Methods that are related to policy tags and policy tag taxonomies are not deprecated. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Data Catalog ](https://docs.cloud.google.com/products)
  * [ Documentation ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/data-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.taxonomies.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates a taxonomy.

### HTTP request

`PATCH https://datacatalog.googleapis.com/v1beta1/{taxonomy.name}`

### Path parameters

Parameters  
---  
`taxonomy.name` |  `string` Identifier. Resource name of this taxonomy, whose format is: "projects/{projectNumber}/locations/{locationId}/taxonomies/{id}". It takes the form `projects/{project}/locations/{location}/taxonomies/{taxonomies}`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask> If not set, defaults to all of the fields that are allowed to update.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Taxonomy](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.taxonomies#Taxonomy)`.

### Response body

If successful, the response body contains an instance of `[Taxonomy](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.taxonomies#Taxonomy)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
