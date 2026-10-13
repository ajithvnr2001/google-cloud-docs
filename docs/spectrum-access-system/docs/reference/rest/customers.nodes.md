---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes
title: REST Resource: customers.nodes \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:20.732961+00:00
---

# REST Resource: customers.nodes  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Reference ](https://docs.cloud.google.com/spectrum-access-system/docs/apis)



Send feedback 

#  REST Resource: customers.nodes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Node
    * JSON representation
  * Methods



## Resource: Node

The Node.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "sasUserIds": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name.   
`displayName` |  `string` The node's display name.   
`sasUserIds[]` |  `string` User ids used by the devices belonging to this node.   
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes/create)`

|  Creates a new `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)`.  
  
### `[delete](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes/delete)`

|  Deletes a `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)`.  
  
### `[get](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes/get)`

|  Returns a requested `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)`.  
  
### `[list](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes/list)`

|  Lists `[nodes](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)`.  
  
### `[move](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes/move)`

|  Moves a `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)` under another `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)` or `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers#Customer)`.  
  
### `[patch](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes/patch)`

|  Updates an existing `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
