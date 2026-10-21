---
url: https://docs.cloud.google.com/cloud-ftp/reference/rest/
title: Cloud FTP API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:41.234530+00:00
---

# Cloud FTP API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ APIs & Reference ](https://docs.cloud.google.com/cloud-ftp/apis)



Send feedback 

#  Cloud FTP API Stay organized with collections  Save and categorize content based on your preferences. 

A managed, cloud-native solution to move data in and out of Google Cloud by using SSH File Transfer Protocol (SFTP).

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.servers
  * REST Resource: v1.projects.locations.servers.users



## Service: ftp.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://ftp.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://ftp.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.servers](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers)

Methods  
---  
`[create](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/create)` |  `POST /v1/{parent=projects/*/locations/*}/servers`   
Creates a new Server in a given project and location.  
`[delete](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/delete)` |  `DELETE /v1/{name=projects/*/locations/*/servers/*}`   
Deletes a single Server.  
`[get](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/get)` |  `GET /v1/{name=projects/*/locations/*/servers/*}`   
Gets details of a single Server.  
`[list](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/list)` |  `GET /v1/{parent=projects/*/locations/*}/servers`   
Lists Servers in a given project and location.  
`[patch](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/patch)` |  `PATCH /v1/{server.name=projects/*/locations/*/servers/*}`   
Updates the parameters of a single Server.  
`[start](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/start)` |  `POST /v1/{name=projects/*/locations/*/servers/*}:start`   
Starts a stopping/stopped Server.  
`[stop](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/stop)` |  `POST /v1/{name=projects/*/locations/*/servers/*}:stop`   
Stops an active Server.  
  
## REST Resource: [v1.projects.locations.servers.users](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users)

Methods  
---  
`[create](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/create)` |  `POST /v1/{parent=projects/*/locations/*/servers/*}/users`   
Creates a new User in a given project and location and Server.  
`[delete](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/delete)` |  `DELETE /v1/{name=projects/*/locations/*/servers/*/users/*}`   
Deletes a single User.  
`[get](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/get)` |  `GET /v1/{name=projects/*/locations/*/servers/*/users/*}`   
Gets details of a single User.  
`[list](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/list)` |  `GET /v1/{parent=projects/*/locations/*/servers/*}/users`   
Lists Users in a given project and location.  
`[patch](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/patch)` |  `PATCH /v1/{user.name=projects/*/locations/*/servers/*/users/*}`   
Updates the parameters of a single User.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
