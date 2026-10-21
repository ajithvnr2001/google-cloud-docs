---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories
title: REST Resource: projects.locations.brands.stores.inventories \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:08.314300+00:00
---

# REST Resource: projects.locations.brands.stores.inventories  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  REST Resource: projects.locations.brands.stores.inventories Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Inventory
    * JSON representation
  * Status
  * Methods



## Resource: Inventory

An inventory resource for a store.

JSON representation  
---  
      
    
    {
      "name": string,
      "itemId": string,
      "modifierId": string,
      "posId": string,
      "quantity": integer,
      "status": enum ([Status](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories#Status))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the inventory. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/inventories/{inventory}  
`itemId` |  `string` Required. The item ID that this inventory belongs to.  
`modifierId` |  `string` Optional. The modifier ID that this inventory belongs to.  
`posId` |  `string` Optional. The point of sale (POS) ID associated with this inventory.  
`quantity` |  `integer` Optional. The quantity of the item/modifier in stock.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories#Status)`)` Optional. The status of the inventory.  
  
## Status

Availability status of the inventory.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified status.  
`IN_STOCK` | The item/modifier is in stock.  
`OUT_OF_STOCK` | The item/modifier is out of stock.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/create)`

|  Creates an inventory.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/delete)`

|  Deletes the specified inventory.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/get)`

|  Gets an inventory.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/list)`

|  Lists inventories.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/patch)`

|  Updates the specified inventory.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-09 UTC."],[],[]] 
