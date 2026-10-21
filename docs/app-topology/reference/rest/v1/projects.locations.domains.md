---
url: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains
title: REST Resource: projects.locations.domains \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:13.490956+00:00
---

# REST Resource: projects.locations.domains  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  REST Resource: projects.locations.domains Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Domain
    * JSON representation
  * Methods



## Resource: Domain

Domain is a pre-defined topology query domain. Each topology domain contains a set of nodes and edges.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The pre-defined topology domain. Currently only SRE, DEVOPS, and SECURITY are available. Format: `projects/{project}/locations/{location}/domains/{domain}`  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains/get)`

|  Retrieves the specified topology domain.  
  
### `[getSchema](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains/getSchema)`

|  Retrieves the schema for the specified topology domain.  
  
### `[list](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains/list)`

|  Lists the topology domains available in a specific location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
