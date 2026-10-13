---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/
title: BeyondCorp API \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:05.183373+00:00
---

# BeyondCorp API  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  BeyondCorp API Stay organized with collections  Save and categorize content based on your preferences. 

Chrome Enterprise Premium is a secure enterprise browsing solution that provides secure access to applications and resources, and offers integrated threat and data protection. It adds an extra layer of security to safeguard your Chrome browser environment, including Data Loss Prevention (DLP), real-time URL and file scanning, and Context-Aware Access for SaaS and web apps.

  * REST Resource: v1.organizations.locations.operations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.appConnections
  * REST Resource: v1.projects.locations.appConnectors
  * REST Resource: v1.projects.locations.appGateways
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.securityGateways
  * REST Resource: v1.projects.locations.securityGateways.applications



## Service: beyondcorp.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://beyondcorp.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://beyondcorp.googleapis.com`



## REST Resource: [v1.organizations.locations.operations](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/organizations.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/organizations.locations.operations/cancel)` |  `POST /v1/{name=organizations/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/organizations.locations.operations/delete)` |  `DELETE /v1/{name=organizations/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/organizations.locations.operations/get)` |  `GET /v1/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/organizations.locations.operations/list)` |  `GET /v1/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.appConnections](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections)

Methods  
---  
`[create](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/create)` |  `POST /v1/{parent=projects/*/locations/*}/appConnections`   
Creates a new AppConnection in a given project and location.  
`[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/delete)` |  `DELETE /v1/{name=projects/*/locations/*/appConnections/*}`   
Deletes a single AppConnection.  
`[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/get)` |  `GET /v1/{name=projects/*/locations/*/appConnections/*}`   
Gets details of a single AppConnection.  
`[getIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/appConnections/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/list)` |  `GET /v1/{parent=projects/*/locations/*}/appConnections`   
Lists AppConnections in a given project and location.  
`[patch](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/patch)` |  `PATCH /v1/{appConnection.name=projects/*/locations/*/appConnections/*}`   
Updates the parameters of a single AppConnection.  
`[resolve](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/resolve)` |  `GET /v1/{parent=projects/*/locations/*}/appConnections:resolve`   
Resolves AppConnections details for a given AppConnector.  
`[setIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/appConnections/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnections/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/appConnections/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.appConnectors](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors)

Methods  
---  
`[create](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/create)` |  `POST /v1/{parent=projects/*/locations/*}/appConnectors`   
Creates a new AppConnector in a given project and location.  
`[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/delete)` |  `DELETE /v1/{name=projects/*/locations/*/appConnectors/*}`   
Deletes a single AppConnector.  
`[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/get)` |  `GET /v1/{name=projects/*/locations/*/appConnectors/*}`   
Gets details of a single AppConnector.  
`[getIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/appConnectors/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/list)` |  `GET /v1/{parent=projects/*/locations/*}/appConnectors`   
Lists AppConnectors in a given project and location.  
`[patch](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/patch)` |  `PATCH /v1/{appConnector.name=projects/*/locations/*/appConnectors/*}`   
Updates the parameters of a single AppConnector.  
`[reportStatus](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/reportStatus)` |  `POST /v1/{appConnector=projects/*/locations/*/appConnectors/*}:reportStatus`   
Report status for a given connector.  
`[resolveInstanceConfig](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig)` |  `GET /v1/{appConnector=projects/*/locations/*/appConnectors/*}:resolveInstanceConfig`   
Gets instance configuration for a given AppConnector.  
`[setIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/appConnectors/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/appConnectors/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.appGateways](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appGateways)

Methods  
---  
`[create](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appGateways/create)` |  `POST /v1/{parent=projects/*/locations/*}/appGateways`   
Creates a new AppGateway in a given project and location.  
`[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appGateways/delete)` |  `DELETE /v1/{name=projects/*/locations/*/appGateways/*}`   
Deletes a single AppGateway.  
`[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appGateways/get)` |  `GET /v1/{name=projects/*/locations/*/appGateways/*}`   
Gets details of a single AppGateway.  
`[getIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appGateways/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/appGateways/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appGateways/list)` |  `GET /v1/{parent=projects/*/locations/*}/appGateways`   
Lists AppGateways in a given project and location.  
`[setIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appGateways/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/appGateways/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appGateways/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/appGateways/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.securityGateways](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways)

Methods  
---  
`[create](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/create)` |  `POST /v1/{parent=projects/*/locations/*}/securityGateways`   
Creates a new Security Gateway in a given project and location.  
`[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/delete)` |  `DELETE /v1/{name=projects/*/locations/*/securityGateways/*}`   
Deletes a single SecurityGateway.  
`[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/get)` |  `GET /v1/{name=projects/*/locations/*/securityGateways/*}`   
Gets details of a single SecurityGateway.  
`[getIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/securityGateways/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/list)` |  `GET /v1/{parent=projects/*/locations/*}/securityGateways`   
Lists SecurityGateways in a given project and location.  
`[patch](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/patch)` |  `PATCH /v1/{securityGateway.name=projects/*/locations/*/securityGateways/*}`   
Updates the parameters of a single SecurityGateway.  
`[setIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/securityGateways/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/securityGateways/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.securityGateways.applications](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications)

Methods  
---  
`[create](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/create)` |  `POST /v1/{parent=projects/*/locations/*/securityGateways/*}/applications`   
Creates a new Application in a given project and location.  
`[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/delete)` |  `DELETE /v1/{name=projects/*/locations/*/securityGateways/*/applications/*}`   
Deletes a single application.  
`[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/get)` |  `GET /v1/{name=projects/*/locations/*/securityGateways/*/applications/*}`   
Gets details of a single Application.  
`[getIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/securityGateways/*/applications/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/list)` |  `GET /v1/{parent=projects/*/locations/*/securityGateways/*}/applications`   
Lists Applications in a given project and location.  
`[patch](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/patch)` |  `PATCH /v1/{application.name=projects/*/locations/*/securityGateways/*/applications/*}`   
Updates the parameters of a single Application.  
`[setIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/securityGateways/*/applications/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways.applications/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/securityGateways/*/applications/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-02 UTC."],[],[]] 
