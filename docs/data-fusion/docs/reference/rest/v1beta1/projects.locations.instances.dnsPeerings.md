---
url: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings
title: REST Resource: projects.locations.instances.dnsPeerings \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:10.569828+00:00
---

# REST Resource: projects.locations.instances.dnsPeerings  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  REST Resource: projects.locations.instances.dnsPeerings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DnsPeering
    * JSON representation
  * Methods



## Resource: DnsPeering

DNS peering configuration. These configurations are used to create DNS peering with the customer Cloud DNS.

JSON representation  
---  
      
    
    {
      "name": string,
      "domain": string,
      "description": string,
      "targetProject": string,
      "targetNetwork": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the dns peering zone. Format: projects/{project}/locations/{location}/instances/{instance}/dnsPeerings/{dnsPeering}  
`domain` |  `string` Required. The dns name suffix of the zone.  
`description` |  `string` Optional. Optional description of the dns zone.  
`targetProject` |  `string` Optional. Optional target project to which dns peering should happen.  
`targetNetwork` |  `string` Optional. Optional target network to which dns peering should happen.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/create)`

|  Creates DNS peering on the given resource.  
  
### `[delete](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/delete)`

|  Deletes DNS peering on the given resource.  
  
### `[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/list)`

|  Lists DNS peerings for a given resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-29 UTC."],[],[]] 
