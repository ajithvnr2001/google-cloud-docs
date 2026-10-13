---
url: https://docs.cloud.google.com/domains/docs/reference/rest/
title: Cloud Domains API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:11.350346+00:00
---

# Cloud Domains API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Reference ](https://docs.cloud.google.com/domains/docs/apis)



Send feedback 

#  Cloud Domains API Stay organized with collections  Save and categorize content based on your preferences. 

Enables management and configuration of domain names.

  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1beta1.projects.locations.registrations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.registrations



## Service: domains.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://domains.googleapis.com/$discovery/rest?version=v1>
  * <https://domains.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://domains.googleapis.com`



## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.registrations](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations)

Methods  
---  
`[configureContactSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/configureContactSettings)` |  `POST /v1beta1/{registration=projects/*/locations/*/registrations/*}:configureContactSettings`   
Updates a `Registration`'s contact settings.  
`[configureDnsSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/configureDnsSettings)` |  `POST /v1beta1/{registration=projects/*/locations/*/registrations/*}:configureDnsSettings`   
Updates a `Registration`'s DNS settings.  
`[configureManagementSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/configureManagementSettings)` |  `POST /v1beta1/{registration=projects/*/locations/*/registrations/*}:configureManagementSettings`   
Updates a `Registration`'s management settings.  
`[delete](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/registrations/*}`   
Deletes a `Registration` resource.  
`[export](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/export)   
**(deprecated)**` |  `POST /v1beta1/{name=projects/*/locations/*/registrations/*}:export`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.  
`[get](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/registrations/*}`   
Gets the details of a `Registration` resource.  
`[getIamPolicy](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/registrations/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[import](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/import)   
**(deprecated)**` |  `POST /v1beta1/{parent=projects/*/locations/*}/registrations:import`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Imports a domain name from [Google Domains](https://domains.google/) for use in Cloud Domains.  
`[initiatePushTransfer](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/initiatePushTransfer)` |  `POST /v1beta1/{registration=projects/*/locations/*/registrations/*}:initiatePushTransfer`   
Initiates the `Push Transfer` process to transfer the domain to another registrar.  
`[list](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/registrations`   
Lists the `Registration` resources in a project.  
`[patch](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/patch)` |  `PATCH /v1beta1/{registration.name=projects/*/locations/*/registrations/*}`   
Updates select fields of a `Registration` resource, notably `labels`.  
`[register](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/register)` |  `POST /v1beta1/{parent=projects/*/locations/*}/registrations:register`   
Registers a new domain name and creates a corresponding `Registration` resource.  
`[renewDomain](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/renewDomain)` |  `POST /v1beta1/{registration=projects/*/locations/*/registrations/*}:renewDomain`   
Renews a recently expired domain.  
`[resetAuthorizationCode](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/resetAuthorizationCode)` |  `POST /v1beta1/{registration=projects/*/locations/*/registrations/*}:resetAuthorizationCode`   
Resets the authorization code of the `Registration` to a new random string.  
`[retrieveAuthorizationCode](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/retrieveAuthorizationCode)` |  `GET /v1beta1/{registration=projects/*/locations/*/registrations/*}:retrieveAuthorizationCode`   
Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.  
`[retrieveImportableDomains](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/retrieveImportableDomains)   
**(deprecated)**` |  `GET /v1beta1/{location=projects/*/locations/*}/registrations:retrieveImportableDomains`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Lists domain names from [Google Domains](https://domains.google/) that can be imported to Cloud Domains using the `ImportDomain` method.  
`[retrieveRegisterParameters](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/retrieveRegisterParameters)` |  `GET /v1beta1/{location=projects/*/locations/*}/registrations:retrieveRegisterParameters`   
Gets parameters needed to register a new domain name, including price and up-to-date availability.  
`[retrieveTransferParameters](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/retrieveTransferParameters)   
**(deprecated)**` |  `GET /v1beta1/{location=projects/*/locations/*}/registrations:retrieveTransferParameters`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Gets parameters needed to transfer a domain name from another registrar to Cloud Domains.  
`[searchDomains](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/searchDomains)` |  `GET /v1beta1/{location=projects/*/locations/*}/registrations:searchDomains`   
Searches for available domain names similar to the provided query.  
`[setIamPolicy](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/registrations/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/registrations/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[transfer](https://docs.cloud.google.com/domains/docs/reference/rest/v1beta1/projects.locations.registrations/transfer)   
**(deprecated)**` |  `POST /v1beta1/{parent=projects/*/locations/*}/registrations:transfer`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Transfers a domain name from another registrar to Cloud Domains.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.registrations](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations)

Methods  
---  
`[configureContactSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureContactSettings)` |  `POST /v1/{registration=projects/*/locations/*/registrations/*}:configureContactSettings`   
Updates a `Registration`'s contact settings.  
`[configureDnsSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureDnsSettings)` |  `POST /v1/{registration=projects/*/locations/*/registrations/*}:configureDnsSettings`   
Updates a `Registration`'s DNS settings.  
`[configureManagementSettings](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureManagementSettings)` |  `POST /v1/{registration=projects/*/locations/*/registrations/*}:configureManagementSettings`   
Updates a `Registration`'s management settings.  
`[delete](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/registrations/*}`   
Deletes a `Registration` resource.  
`[export](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/export)   
**(deprecated)**` |  `POST /v1/{name=projects/*/locations/*/registrations/*}:export`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.  
`[get](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/get)` |  `GET /v1/{name=projects/*/locations/*/registrations/*}`   
Gets the details of a `Registration` resource.  
`[getIamPolicy](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/registrations/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[import](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/import)   
**(deprecated)**` |  `POST /v1/{parent=projects/*/locations/*}/registrations:import`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Imports a domain name from [Google Domains](https://domains.google/) for use in Cloud Domains.  
`[initiatePushTransfer](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/initiatePushTransfer)` |  `POST /v1/{registration=projects/*/locations/*/registrations/*}:initiatePushTransfer`   
Initiates the `Push Transfer` process to transfer the domain to another registrar.  
`[list](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/list)` |  `GET /v1/{parent=projects/*/locations/*}/registrations`   
Lists the `Registration` resources in a project.  
`[patch](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/patch)` |  `PATCH /v1/{registration.name=projects/*/locations/*/registrations/*}`   
Updates select fields of a `Registration` resource, notably `labels`.  
`[register](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/register)` |  `POST /v1/{parent=projects/*/locations/*}/registrations:register`   
Registers a new domain name and creates a corresponding `Registration` resource.  
`[renewDomain](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/renewDomain)` |  `POST /v1/{registration=projects/*/locations/*/registrations/*}:renewDomain`   
Renews a recently expired domain.  
`[resetAuthorizationCode](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/resetAuthorizationCode)` |  `POST /v1/{registration=projects/*/locations/*/registrations/*}:resetAuthorizationCode`   
Resets the authorization code of the `Registration` to a new random string.  
`[retrieveAuthorizationCode](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/retrieveAuthorizationCode)` |  `GET /v1/{registration=projects/*/locations/*/registrations/*}:retrieveAuthorizationCode`   
Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.  
`[retrieveImportableDomains](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/retrieveImportableDomains)   
**(deprecated)**` |  `GET /v1/{location=projects/*/locations/*}/registrations:retrieveImportableDomains`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Lists domain names from [Google Domains](https://domains.google/) that can be imported to Cloud Domains using the `ImportDomain` method.  
`[retrieveRegisterParameters](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/retrieveRegisterParameters)` |  `GET /v1/{location=projects/*/locations/*}/registrations:retrieveRegisterParameters`   
Gets parameters needed to register a new domain name, including price and up-to-date availability.  
`[retrieveTransferParameters](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/retrieveTransferParameters)   
**(deprecated)**` |  `GET /v1/{location=projects/*/locations/*}/registrations:retrieveTransferParameters`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Gets parameters needed to transfer a domain name from another registrar to Cloud Domains.  
`[searchDomains](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/searchDomains)` |  `GET /v1/{location=projects/*/locations/*}/registrations:searchDomains`   
Searches for available domain names similar to the provided query.  
`[setIamPolicy](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/registrations/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/registrations/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[transfer](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/transfer)   
**(deprecated)**` |  `POST /v1/{parent=projects/*/locations/*}/registrations:transfer`   
Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations)Transfers a domain name from another registrar to Cloud Domains.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
