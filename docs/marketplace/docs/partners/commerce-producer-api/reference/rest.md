---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/
title: Cloud Commerce Producer API \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:11.120334+00:00
---

# Cloud Commerce Producer API  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  Cloud Commerce Producer API Stay organized with collections  Save and categorize content based on your preferences. 

Partner API for the Cloud Commerce Producer API Early Access.

  * REST Resource: v1beta.projects.locations
  * REST Resource: v1beta.projects.locations.consumerEnforcementActions
  * REST Resource: v1beta.projects.locations.operations
  * REST Resource: v1beta.projects.locations.privateOffers
  * REST Resource: v1beta.projects.locations.privateOffers.documents
  * REST Resource: v1beta.projects.locations.services
  * REST Resource: v1beta.projects.locations.services.skus
  * REST Resource: v1beta.projects.locations.services.standardOffers
  * REST Resource: v1beta.projects.locations.skuGroups



## Service: commerceproducer.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://commerceproducer.googleapis.com/$discovery/rest?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://commerceproducer.googleapis.com`



## REST Resource: [v1beta.projects.locations](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations/get)` |  `GET /v1beta/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations/list)` |  `GET /v1beta/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta.projects.locations.consumerEnforcementActions](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions)

Methods  
---  
`[create](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/consumerEnforcementActions`   
Creates a ConsumerEnforcementAction resource.  
`[delete](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/consumerEnforcementActions/*}`   
Deletes a ConsumerEnforcementAction resource.  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/get)` |  `GET /v1beta/{name=projects/*/locations/*/consumerEnforcementActions/*}`   
Gets a ConsumerEnforcementAction resource by name.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/consumerEnforcementActions`   
Lists ConsumerEnforcementActions under a parent location.  
`[patch](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/patch)` |  `PATCH /v1beta/{consumerEnforcementAction.name=projects/*/locations/*/consumerEnforcementActions/*}`   
Updates an existing ConsumerEnforcementAction resource.  
  
## REST Resource: [v1beta.projects.locations.operations](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.operations/cancel)` |  `POST /v1beta/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.operations/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.operations/get)` |  `GET /v1beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.operations/list)` |  `GET /v1beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta.projects.locations.privateOffers](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers)

Methods  
---  
`[cancel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/cancel)` |  `POST /v1beta/{name=projects/*/locations/*/privateOffers/*}:cancel`   
Cancels the target PrivateOffer.  
`[create](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/privateOffers`   
Creates a new PrivateOffer in a given project and location.  
`[delete](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/privateOffers/*}`   
Deletes the target PrivateOffer.  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/get)` |  `GET /v1beta/{name=projects/*/locations/*/privateOffers/*}`   
Gets details of a single PrivateOffer.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/privateOffers`   
Lists PrivateOffers for the given parent.  
`[patch](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/patch)` |  `PATCH /v1beta/{privateOffer.name=projects/*/locations/*/privateOffers/*}`   
Updates the target PrivateOffer.  
`[publish](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/publish)` |  `POST /v1beta/{name=projects/*/locations/*/privateOffers/*}:publish`   
Publishes the target PrivateOffer.  
`[resolveAmendmentTarget](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/resolveAmendmentTarget)` |  `GET /v1beta/{parent=projects/*/locations/*}/privateOffers:resolveAmendmentTarget`   
Resolves the existing offer that must be amended when creating a new PrivateOffer.  
  
## REST Resource: [v1beta.projects.locations.privateOffers.documents](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents)

Methods  
---  
`[create](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/create)` |  `POST /v1beta/{parent=projects/*/locations/*/privateOffers/*}/documents`   
Creates a new PrivateOfferDocument in a given project and location.  
`[delete](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/privateOffers/*/documents/*}`   
Deletes the target PrivateOfferDocument.  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/get)` |  `GET /v1beta/{name=projects/*/locations/*/privateOffers/*/documents/*}`   
Gets details of a single PrivateOfferDocument.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/list)` |  `GET /v1beta/{parent=projects/*/locations/*/privateOffers/*}/documents`   
Lists PrivateOfferDocuments for the given parent.  
`[patch](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/patch)` |  `PATCH /v1beta/{privateOfferDocument.name=projects/*/locations/*/privateOffers/*/documents/*}`   
Updates the target PrivateOfferDocument.  
  
## REST Resource: [v1beta.projects.locations.services](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services)

Methods  
---  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services/get)` |  `GET /v1beta/{name=projects/*/locations/*/services/*}`   
Gets details of a single Service.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/services`   
Lists Services in a given project and location.  
  
## REST Resource: [v1beta.projects.locations.services.skus](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus)

Methods  
---  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus/get)` |  `GET /v1beta/{name=projects/*/locations/*/services/*/skus/*}`   
Gets details of a single Sku.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus/list)` |  `GET /v1beta/{parent=projects/*/locations/*/services/*}/skus`   
Lists Skus for the given parent.  
  
## REST Resource: [v1beta.projects.locations.services.standardOffers](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers)

Methods  
---  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers/get)` |  `GET /v1beta/{name=projects/*/locations/*/services/*/standardOffers/*}`   
Gets details of a single StandardOffer.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers/list)` |  `GET /v1beta/{parent=projects/*/locations/*/services/*}/standardOffers`   
Lists StandardOffers for the given parent.  
  
## REST Resource: [v1beta.projects.locations.skuGroups](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups)

Methods  
---  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups/get)` |  `GET /v1beta/{name=projects/*/locations/*/skuGroups/*}`   
Gets details of a single SkuGroup.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/skuGroups`   
Lists SkuGroups for the given parent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-15 UTC."],[],[]] 
