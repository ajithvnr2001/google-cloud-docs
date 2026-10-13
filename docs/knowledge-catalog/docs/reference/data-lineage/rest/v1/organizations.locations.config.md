---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/organizations.locations.config
title: REST Resource: organizations.locations.config \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:52.950781+00:00
---

# REST Resource: organizations.locations.config  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/organizations.locations.config

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  REST Resource: organizations.locations.config Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Config
    * JSON representation
  * Methods



## Resource: Config

Configuration for Data Lineage. Defines different configuration options for Lineage customers to control behaviour of lineage systems.

JSON representation  
---  
      
    
    {
      "name": string,
      "ingestion": {
        object ([Ingestion](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/folders.locations.config#Config.Ingestion))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the config. Format: `organizations/{organization_id}/locations/global/config` `folders/{folder_id}/locations/global/config` `projects/{projectId}/locations/global/config` `projects/{project_number}/locations/global/config`  
`ingestion` |  `object (`[Ingestion](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/folders.locations.config#Config.Ingestion)`)` Optional. Ingestion rule for Data Lineage ingestion.  
`etag` |  `string` Optional. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a config from overwriting each other. It is required that systems make use of the `etag` in the read-modify-write cycle to perform config updates in order to avoid race conditions: An `etag` is returned in the response to `config.get`, and systems are expected to put that etag in the request to `config.patch` to ensure that their change will be applied to the same version of the config. If an `etag` is not provided in the call to `config.patch`, then the existing config, if any, will be overwritten.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/organizations.locations.config/get)`

|  Get the Config for a given resource.  
  
### `[patch](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/organizations.locations.config/patch)`

|  Update the Config for a given resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
