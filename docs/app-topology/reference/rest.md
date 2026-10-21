---
url: https://docs.cloud.google.com/app-topology/reference/rest/
title: App Topology API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:12.426551+00:00
---

# App Topology API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  App Topology API Stay organized with collections  Save and categorize content based on your preferences. 

Correlate data to answer questions about the health, performance, and security posture of your resources.

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.discoveredResourcesTopology
  * REST Resource: v1.projects.locations.domains
  * REST Resource: v1.projects.locations.domains.schema
  * REST Resource: v1.projects.locations.operations



## Service: apptopology.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://apptopology.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://apptopology.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.discoveredResourcesTopology](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology)

Methods  
---  
`[generate](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate)` |  `POST /v1/{name=projects/*/locations/*/discoveredResourcesTopology}:generate`   
Generate the topology for all resources in the given project.  
  
## REST Resource: [v1.projects.locations.domains](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains)

Methods  
---  
`[get](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains/get)` |  `GET /v1/{name=projects/*/locations/*/domains/*}`   
Retrieves the specified topology domain.  
`[getSchema](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains/getSchema)` |  `GET /v1/{name=projects/*/locations/*/domains/*/schema}`   
Retrieves the schema for the specified topology domain.  
`[list](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains/list)` |  `GET /v1/{parent=projects/*/locations/*}/domains`   
Lists the topology domains available in a specific location.  
  
## REST Resource: [v1.projects.locations.domains.schema](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema)

Methods  
---  
`[explore](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema/explore)` |  `POST /v1/{name=projects/*/locations/*/domains/*/schema}:explore`   
Explores the topology schema starting from given node types or label names up to a specified hop depth.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
