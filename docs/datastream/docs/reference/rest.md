---
url: https://docs.cloud.google.com/datastream/docs/reference/rest/
title: Datastream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:24.885460+00:00
---

# Datastream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Reference ](https://docs.cloud.google.com/datastream/docs/reference/rest)



Send feedback 

#  Datastream API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.connectionProfiles
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.privateConnections
  * REST Resource: v1.projects.locations.privateConnections.routes
  * REST Resource: v1.projects.locations.streams
  * REST Resource: v1.projects.locations.streams.objects



## Service: datastream.googleapis.com

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://datastream.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://datastream.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[fetchStaticIps](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations/fetchStaticIps)` |  `GET /v1/{name}:fetchStaticIps`   
The FetchStaticIps API call exposes the static IP addresses used by Datastream.  
`[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.connectionProfiles](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles/create)` |  `POST /v1/{parent}/connectionProfiles`   
Use this method to create a connection profile in a project and location.  
`[delete](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles/delete)` |  `DELETE /v1/{name}`   
Use this method to delete a connection profile.  
`[discover](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles/discover)` |  `POST /v1/{parent}/connectionProfiles:discover`   
Use this method to discover a connection profile.  
`[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles/get)` |  `GET /v1/{name}`   
Use this method to get details about a connection profile.  
`[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles/list)` |  `GET /v1/{parent}/connectionProfiles`   
Use this method to list connection profiles created in a project and location.  
`[patch](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles/patch)` |  `PATCH /v1/{connectionProfile.name}`   
Use this method to update the parameters of a connection profile.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.privateConnections](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections)

Methods  
---  
`[create](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections/create)` |  `POST /v1/{parent}/privateConnections`   
Use this method to create a private connectivity configuration.  
`[delete](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections/delete)` |  `DELETE /v1/{name}`   
Use this method to delete a private connectivity configuration.  
`[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections/get)` |  `GET /v1/{name}`   
Use this method to get details about a private connectivity configuration.  
`[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections/list)` |  `GET /v1/{parent}/privateConnections`   
Use this method to list private connectivity configurations in a project and location.  
  
## REST Resource: [v1.projects.locations.privateConnections.routes](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections.routes)

Methods  
---  
`[create](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections.routes/create)` |  `POST /v1/{parent}/routes`   
Use this method to create a route for a private connectivity configuration in a project and location.  
`[delete](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections.routes/delete)` |  `DELETE /v1/{name}`   
Use this method to delete a route.  
`[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections.routes/get)` |  `GET /v1/{name}`   
Use this method to get details about a route.  
`[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections.routes/list)` |  `GET /v1/{parent}/routes`   
Use this method to list routes created for a private connectivity configuration in a project and location.  
  
## REST Resource: [v1.projects.locations.streams](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams)

Methods  
---  
`[create](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/create)` |  `POST /v1/{parent}/streams`   
Use this method to create a stream.  
`[delete](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/delete)` |  `DELETE /v1/{name}`   
Use this method to delete a stream.  
`[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/get)` |  `GET /v1/{name}`   
Use this method to get details about a stream.  
`[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/list)` |  `GET /v1/{parent}/streams`   
Use this method to list streams in a project and location.  
`[patch](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/patch)` |  `PATCH /v1/{stream.name}`   
Use this method to update the configuration of a stream.  
`[run](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/run)` |  `POST /v1/{name}:run`   
Use this method to start, resume or recover a stream with a non default CDC strategy.  
  
## REST Resource: [v1.projects.locations.streams.objects](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects)

Methods  
---  
`[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/get)` |  `GET /v1/{name}`   
Use this method to get details about a stream object.  
`[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/list)` |  `GET /v1/{parent}/objects`   
Use this method to list the objects of a specific stream.  
`[lookup](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/lookup)` |  `POST /v1/{parent}/objects:lookup`   
Use this method to look up a stream object by its source object identifier.  
`[startBackfillJob](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/startBackfillJob)` |  `POST /v1/{object}:startBackfillJob`   
Use this method to start a backfill job for the specified stream object.  
`[stopBackfillJob](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams.objects/stopBackfillJob)` |  `POST /v1/{object}:stopBackfillJob`   
Use this method to stop a backfill job for the specified stream object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
