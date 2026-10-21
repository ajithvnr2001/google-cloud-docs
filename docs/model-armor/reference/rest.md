---
url: https://docs.cloud.google.com/model-armor/reference/rest/
title: Model Armor API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:46:29.431718+00:00
---

# Model Armor API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Reference ](https://docs.cloud.google.com/model-armor/reference/libraries)



Send feedback 

#  Model Armor API Stay organized with collections  Save and categorize content based on your preferences. 

Model Armor helps you protect against risks like prompt injection, harmful content, and data leakage in generative AI applications by letting you define policies that filter user prompts and model responses. Note that the global endpoint is supported only with getFloorSetting and updateFloorSetting methods.

  * REST Resource: v1.folders.locations
  * REST Resource: v1.organizations.locations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.templates



## Service: modelarmor.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://modelarmor.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://modelarmor.googleapis.com`



## REST Resource: [v1.folders.locations](https://docs.cloud.google.com/model-armor/reference/rest/v1/folders.locations)

Methods  
---  
`[getFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/folders.locations/getFloorSetting)` |  `GET /v1/{name=folders/*/locations/*/floorSetting}`   
Gets details of a single floor setting of a project  
`[updateFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/folders.locations/updateFloorSetting)` |  `PATCH /v1/{floorSetting.name=folders/*/locations/*/floorSetting}`   
Updates the parameters of a single floor setting of a project  
  
## REST Resource: [v1.organizations.locations](https://docs.cloud.google.com/model-armor/reference/rest/v1/organizations.locations)

Methods  
---  
`[getFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/organizations.locations/getFloorSetting)` |  `GET /v1/{name=organizations/*/locations/*/floorSetting}`   
Gets details of a single floor setting of a project  
`[updateFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/organizations.locations/updateFloorSetting)` |  `PATCH /v1/{floorSetting.name=organizations/*/locations/*/floorSetting}`   
Updates the parameters of a single floor setting of a project  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations/getFloorSetting)` |  `GET /v1/{name=projects/*/locations/*/floorSetting}`   
Gets details of a single floor setting of a project  
`[list](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
`[updateFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations/updateFloorSetting)` |  `PATCH /v1/{floorSetting.name=projects/*/locations/*/floorSetting}`   
Updates the parameters of a single floor setting of a project  
  
## REST Resource: [v1.projects.locations.templates](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates)

Methods  
---  
`[create](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/create)` |  `POST /v1/{parent=projects/*/locations/*}/templates`   
Creates a new Template in a given project and location.  
`[delete](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/delete)` |  `DELETE /v1/{name=projects/*/locations/*/templates/*}`   
Deletes a single Template.  
`[get](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/get)` |  `GET /v1/{name=projects/*/locations/*/templates/*}`   
Gets details of a single Template.  
`[list](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/list)` |  `GET /v1/{parent=projects/*/locations/*}/templates`   
Lists Templates in a given project and location.  
`[patch](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/patch)` |  `PATCH /v1/{template.name=projects/*/locations/*/templates/*}`   
Updates the parameters of a single Template.  
`[sanitizeModelResponse](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse)` |  `POST /v1/{name=projects/*/locations/*/templates/*}:sanitizeModelResponse`   
Sanitizes Model Response.  
`[sanitizeUserPrompt](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeUserPrompt)` |  `POST /v1/{name=projects/*/locations/*/templates/*}:sanitizeUserPrompt`   
Sanitizes User Prompt.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
