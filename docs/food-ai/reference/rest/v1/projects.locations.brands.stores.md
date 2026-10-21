---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores
title: REST Resource: projects.locations.brands.stores \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:06.537051+00:00
---

# REST Resource: projects.locations.brands.stores  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  REST Resource: projects.locations.brands.stores Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Store
    * JSON representation
    * StoreStatus
      * JSON representation
    * State
    * StoreMetadata
      * JSON representation
    * Address
      * JSON representation
    * StoreHours
      * JSON representation
    * Daypart
      * JSON representation
  * Methods



## Resource: Store

An individual store for a brand.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "status": {
        object ([StoreStatus](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.StoreStatus))
      },
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/TimeZone))
      },
      "storeMetadata": {
        object ([StoreMetadata](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.StoreMetadata))
      },
      "tags": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The store name. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this store was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this store was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `object (`[StoreStatus](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.StoreStatus)`)` Required. The status of the store.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/TimeZone)`)` Required. The time zone of the store. This is used to determine which menu daypart to use for the store at a given time and for any time-based overrides.  
`storeMetadata` |  `object (`[StoreMetadata](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.StoreMetadata)`)` Optional. Metadata for the store.  
`tags[]` |  `string` Optional. Tags associated with the store.  
  
### StoreStatus

The status of the store.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.State))
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.State)`)` Optional. The state of the store.  
  
### State

The status of the store.

Enums  
---  
`STATE_UNSPECIFIED` | The store is in an unspecified state.  
`ACTIVE` | The store is active.  
`DISABLED` | The store is disabled.  
  
### StoreMetadata

Metadata for the store.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "contactEmail": string,
      "address": {
        object ([Address](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.Address))
      },
      "storeHours": [
        {
          object ([StoreHours](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.StoreHours))
        }
      ],
      "dayparts": [
        {
          object ([Daypart](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.Daypart))
        }
      ],
      "phoneNumber": string
    }  
  
Fields  
---  
`displayName` |  `string` Optional. The display name of the store to be used in UI and customer-facing elements.  
`contactEmail` |  `string` Optional. The email address of the store to be provided to customers.  
`address` |  `object (`[Address](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.Address)`)` Optional. The address information for the store.  
`storeHours[]` |  `object (`[StoreHours](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.StoreHours)`)` Optional. The open hours of the store.  
`dayparts[]` |  `object (`[Daypart](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store.Daypart)`)` Optional. Dayparts defined for the store.  
`phoneNumber` |  `string` Optional. The main phone number of the store to take orders, ask for catering, make general inquiries, and make reservations.  
  
### Address

The address information for the store.

JSON representation  
---  
      
    
    {
      "streetAddress": string,
      "city": string,
      "state": string,
      "country": string,
      "postalCode": string,
      "latitude": number,
      "longitude": number,
      "googleMapsUrl": string
    }  
  
Fields  
---  
`streetAddress` |  `string` Optional. The street address of the store.  
`city` |  `string` Optional. The city of the store.  
`state` |  `string` Optional. The state of the store.  
`country` |  `string` Optional. The country of the store.  
`postalCode` |  `string` Optional. The postal code of the store.  
`latitude` |  `number` Optional. The latitude of the store.  
`longitude` |  `number` Optional. The longitude of the store.  
`googleMapsUrl` |  `string` Optional. The Google Maps URL for the store.  
  
### StoreHours

The operating hours of the store.

JSON representation  
---  
      
    
    {
      "fulfillmentMethod": enum ([FulfillmentMethod](https://docs.cloud.google.com/food-ai/reference/rest/v1/FulfillmentMethod)),
      "schedules": [
        {
          object ([Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1/Schedule))
        }
      ]
    }  
  
Fields  
---  
`fulfillmentMethod` |  `enum (`[FulfillmentMethod](https://docs.cloud.google.com/food-ai/reference/rest/v1/FulfillmentMethod)`)` Optional. The fulfillment method of the store hours, for instance "PICKUP", "DELIVERY", etc. If unspecified, the store hours are assumed to be applicable to all fulfillment methods.  
`schedules[]` |  `object (`[Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1/Schedule)`)` Optional. The operating hours for the store for the specified fulfillmentMethod.  
  
### Daypart

A daypart for the store.

JSON representation  
---  
      
    
    {
      "id": string,
      "schedules": [
        {
          object ([Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1/Schedule))
        }
      ],
      "displayName": string
    }  
  
Fields  
---  
`id` |  `string` Optional. The day part id, for instance "BREAKFAST", "LUNCH", etc.  
`schedules[]` |  `object (`[Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1/Schedule)`)` Optional. Daypart active hours.  
`displayName` |  `string` Optional. Specifies an optional display name for this daypart.  
  
## Methods  
  
---  
  
### `[batchDelete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchDelete)`

|  Batch deletes stores.  
  
### `[batchUpdate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchUpdate)`

|  Batch updates stores.  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/create)`

|  Creates a store.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/delete)`

|  Deletes the specified store.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/get)`

|  Gets a store.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/list)`

|  Lists stores.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/patch)`

|  Update the specified store.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-09 UTC."],[],[]] 
