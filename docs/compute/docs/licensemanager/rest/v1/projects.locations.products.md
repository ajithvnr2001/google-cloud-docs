---
url: https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products
title: REST Resource: projects.locations.products \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:54:13.598743+00:00
---

# REST Resource: projects.locations.products  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.locations.products Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Product
    * JSON representation
  * State
  * Methods



## Resource: Product

Products for Google SPLA.

JSON representation  
---  
      
    
    {
      "name": string,
      "version": string,
      "productCompany": string,
      "state": enum ([State](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products#State)),
      "sku": string,
      "description": string,
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Full name of the product resource. ex "projects/1/locations/us-central1/products/office-2021"  
`version` |  `string` Required. Version of the product.  
`productCompany` |  `string` Required. Company that released the product.  
`state` |  `enum (`[State](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products#State)`)` Output only. State of the product.  
`sku` |  `string` Required. SKU for mapping to the Billing/Subscription resource.  
`description` |  `string` Required. Human-readable, detailed description of the Product  
`displayName` |  `string` Required. Human-readable name of the Product  
  
## State

State of the product.

Enums  
---  
`STATE_UNSPECIFIED` | The Status of the product is unknown.  
`STATE_PROVISIONING` | Product is under provisioning stage.  
`STATE_RUNNING` | Product is ok to run on instances.  
`STATE_TERMINATING` | The product is about to terminate or has been announced for termination.  
`STATE_TERMINATED` | The product has been terminated.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products/get)`

|  Gets details of a single Product.  
  
### `[list](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products/list)`

|  Lists Products in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
