---
url: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations/setConfig/
title: Method: projects.locations.setConfig \u00a0|\u00a0 Data Catalog Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:52.336467+00:00
---

# Method: projects.locations.setConfig  |  Data Catalog Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations/setConfig/

Data Catalog API methods that are related to Data Catalog search and metadata are deprecated and will be discontinued on June 1, 2026. See [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). Methods that are related to policy tags and policy tag taxonomies are not deprecated. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Data Catalog ](https://docs.cloud.google.com/products)
  * [ Documentation ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/data-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.setConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Data Catalog is deprecated. Please use Dataplex Universal Catalog instead.

Sets the configuration related to the migration to Dataplex Universal Catalog for an organization or project.

### HTTP request

`POST https://datacatalog.googleapis.com/v1/{name}:setConfig`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The organization or project whose config is being specified. It takes the form `projects/{project}/locations/{location}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // Union field configuration can be only one of the following:
      "tagTemplateMigration": enum ([TagTemplateMigration](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/TagTemplateMigration)),
      "catalogUiExperience": enum ([CatalogUIExperience](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/CatalogUIExperience))
      // End of list of possible types for union field configuration.
    }  
  
Fields  
---  
Union field `configuration`. The configuration field to set. `configuration` can be only one of the following:  
`tagTemplateMigration` |  `enum (`[TagTemplateMigration](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/TagTemplateMigration)`)` Opt-in status for the migration of Tag Templates to Dataplex Universal Catalog.  
`catalogUiExperience` |  `enum (`[CatalogUIExperience](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/CatalogUIExperience)`)` Opt-in status for the UI switch to Dataplex Universal Catalog.  
  
### Response body

If successful, the response body contains an instance of `[MigrationConfig](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/MigrationConfig)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `datacatalog.migrationConfig.set`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
