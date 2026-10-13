---
url: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields/create/
title: Method: projects.locations.tagTemplates.fields.create \u00a0|\u00a0 Data Catalog Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:11.845415+00:00
---

# Method: projects.locations.tagTemplates.fields.create  |  Data Catalog Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields/create/

Data Catalog API methods that are related to Data Catalog search and metadata are deprecated and will be discontinued on June 1, 2026. See [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). Methods that are related to policy tags and policy tag taxonomies are not deprecated. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Data Catalog ](https://docs.cloud.google.com/products)
  * [ Documentation ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/data-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.tagTemplates.fields.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Data Catalog is deprecated. Please use Dataplex Universal Catalog instead.

Creates a field in a tag template.

You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project).

### HTTP request

`POST https://datacatalog.googleapis.com/v1/{parent}/fields`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the project and the template location [region](https://cloud.google.com/data-catalog/docs/concepts/regions). It takes the form `projects/{project}/locations/{location}/tagTemplates/{tagtemplate}`.  
  
### Query parameters

Parameters  
---  
`tagTemplateFieldId` |  `string` Required. The ID of the tag template field to create.Note: Adding a required field to an existing template is _not_ allowed.Field IDs can contain letters (both uppercase and lowercase), numbers (0-9), underscores (_) and dashes (-). Field IDs must be at least 1 character long and at most 128 characters long. Field IDs must also be unique within their template.  
  
### Request body

The request body contains an instance of `[TagTemplateField](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields#TagTemplateField)`.

### Response body

If successful, the response body contains a newly created instance of `[TagTemplateField](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates.fields#TagTemplateField)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
