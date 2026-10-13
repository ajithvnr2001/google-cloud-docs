---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.savedColumnSets
title: REST Resource: projects.locations.instances.users.savedColumnSets \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:13.215598+00:00
---

# REST Resource: projects.locations.instances.users.savedColumnSets  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.savedColumnSets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.users.savedColumnSets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SavedColumnSet
    * JSON representation
  * Methods



## Resource: SavedColumnSet

Represents a SavedColumnSet from a Chronicle user. This contains a set of columns. which will be shown in the UI tables. This resource can also be shared with other users in the same customer.

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        object ([EntryMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EntryMetadata))
      },
      "displayName": string,
      "columnIds": [
        string
      ],
      "description": string,
      "owner": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the SavedColumnSet. Format: projects/{project}/locations/{location}/instances/{instance}/users/{user}/savedColumnSets/{savedColumnSet} Although note that it is not user settable.  
`metadata` |  `object (`[EntryMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EntryMetadata)`)` Optional. Metadata about the SavedColumn.  
`displayName` |  `string` Required. Name of the SavedColumnSet to be shown in the UI.  
`columnIds[]` |  `string` Required. The list of column ids to show in the table.  
`description` |  `string` Optional. Description of the overall SavedColumnSet, to be shown in the UI.  
`owner` |  `boolean` Optional. Whether the current user is the owner of the SavedColumnSet.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.savedColumnSets/create)`

|  Endpoint for adding a new saved column set to the specified instance.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.savedColumnSets/delete)`

|  Endpoint for deleting a saved column set.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.savedColumnSets/get)`

|  Endpoint for getting a user's saved column set.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.savedColumnSets/list)`

|  Endpoint for listing the saved column sets.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.savedColumnSets/patch)`

|  Endpoint for updating user data saved column set  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
