---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/
title: API Reference \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:40:39.355615+00:00
---

# API Reference  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  API Reference Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1beta1.projects.locations.multicastConsumerAssociations
  * REST Resource: v1beta1.projects.locations.multicastDomainActivations
  * REST Resource: v1beta1.projects.locations.multicastDomainGroups
  * REST Resource: v1beta1.projects.locations.multicastDomains
  * REST Resource: v1beta1.projects.locations.multicastGroupConsumerActivations
  * REST Resource: v1beta1.projects.locations.multicastGroupProducerActivations
  * REST Resource: v1beta1.projects.locations.multicastGroupRangeActivations
  * REST Resource: v1beta1.projects.locations.multicastGroupRanges
  * REST Resource: v1beta1.projects.locations.multicastProducerAssociations
  * REST Resource: v1.projects.locations.multicastConsumerAssociations
  * REST Resource: v1.projects.locations.multicastDomainActivations
  * REST Resource: v1.projects.locations.multicastDomainGroups
  * REST Resource: v1.projects.locations.multicastDomains
  * REST Resource: v1.projects.locations.multicastGroupConsumerActivations
  * REST Resource: v1.projects.locations.multicastGroupProducerActivations
  * REST Resource: v1.projects.locations.multicastGroupRangeActivations
  * REST Resource: v1.projects.locations.multicastGroupRanges
  * REST Resource: v1.projects.locations.multicastProducerAssociations



## Service: networkservices.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * [https://networkservices.googleapis.com/$discovery/rest?version=v1&labels=MULTICAST_V1&key={API_KEY}](https://networkservices.googleapis.com/$discovery/rest?version=v1&labels=MULTICAST_V1&key={API_KEY})
  * [https://networkservices.googleapis.com/$discovery/rest?version=v1beta1&labels=MULTICAST_PREVIEW&key={API_KEY}](https://networkservices.googleapis.com/$discovery/rest?version=v1beta1&labels=MULTICAST_PREVIEW&key={API_KEY})



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://networkservices.googleapis.com`



## REST Resource: [v1beta1.projects.locations.multicastConsumerAssociations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastConsumerAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastConsumerAssociations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastConsumerAssociations`   
Creates a new multicast consumer association in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastConsumerAssociations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastConsumerAssociations/*}`   
Deletes a single multicast consumer association.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastConsumerAssociations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastConsumerAssociations/*}`   
Gets details of a single multicast consumer association.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastConsumerAssociations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastConsumerAssociations`   
Lists multicast consumer associations in a given project and location.  
  
## REST Resource: [v1beta1.projects.locations.multicastDomainActivations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastDomainActivations`   
Creates a new multicast domain activation in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastDomainActivations/*}`   
Deletes a single multicast domain activation.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastDomainActivations/*}`   
Gets details of a single multicast domain activation.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastDomainActivations`   
Lists multicast domain activations in a given project and location.  
`[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/patch)` |  `PATCH /v1beta1/{multicastDomainActivation.name=projects/*/locations/*/multicastDomainActivations/*}`   
Updates the parameters of a single multicast domain activation.  
  
## REST Resource: [v1beta1.projects.locations.multicastDomainGroups](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastDomainGroups`   
Creates a new multicast domain group in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastDomainGroups/*}`   
Deletes a single multicast domain.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastDomainGroups/*}`   
Gets details of a single multicast domain group.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastDomainGroups`   
Lists multicast domain groups in a given project and location.  
  
## REST Resource: [v1beta1.projects.locations.multicastDomains](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomains)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomains/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastDomains`   
Creates a new multicast domain in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomains/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastDomains/*}`   
Deletes a single multicast domain.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomains/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastDomains/*}`   
Gets details of a single multicast domain.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomains/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastDomains`   
Lists multicast domains in a given project and location.  
  
## REST Resource: [v1beta1.projects.locations.multicastGroupConsumerActivations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastGroupConsumerActivations`   
Creates a new multicast group consumer activation in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastGroupConsumerActivations/*}`   
Deletes a single multicast group consumer activation.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastGroupConsumerActivations/*}`   
Gets details of a single multicast group consumer activation.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastGroupConsumerActivations`   
Lists multicast group consumer activations in a given project and location.  
`[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/patch)` |  `PATCH /v1beta1/{multicastGroupConsumerActivation.name=projects/*/locations/*/multicastGroupConsumerActivations/*}`   
Updates the parameters of a single multicast group consumer activation.  
  
## REST Resource: [v1beta1.projects.locations.multicastGroupProducerActivations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupProducerActivations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupProducerActivations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastGroupProducerActivations`   
Creates a new multicast group consumer activation in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupProducerActivations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastGroupProducerActivations/*}`   
Deletes a single multicast group consumer activation.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupProducerActivations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastGroupProducerActivations/*}`   
Gets details of a single multicast group consumer activation.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupProducerActivations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastGroupProducerActivations`   
Lists multicast group consumer activations in a given project and location.  
  
## REST Resource: [v1beta1.projects.locations.multicastGroupRangeActivations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRangeActivations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRangeActivations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastGroupRangeActivations`   
Creates a new multicast group range activation in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRangeActivations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastGroupRangeActivations/*}`   
Deletes a single multicast group range activation.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRangeActivations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastGroupRangeActivations/*}`   
Gets details of a single multicast group range activation.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRangeActivations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastGroupRangeActivations`   
Lists multicast group range activationsin a given project and location.  
`[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRangeActivations/patch)` |  `PATCH /v1beta1/{multicastGroupRangeActivation.name=projects/*/locations/*/multicastGroupRangeActivations/*}`   
Updates the parameters of a single multicast group range activation.  
  
## REST Resource: [v1beta1.projects.locations.multicastGroupRanges](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastGroupRanges`   
Creates a new multicast group range in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastGroupRanges/*}`   
Deletes a single multicast group range.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastGroupRanges/*}`   
Gets details of a single multicast group range.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastGroupRanges`   
Lists multicast group ranges in a given project and location.  
`[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/patch)` |  `PATCH /v1beta1/{multicastGroupRange.name=projects/*/locations/*/multicastGroupRanges/*}`   
Updates the parameters of a single multicast group range.  
  
## REST Resource: [v1beta1.projects.locations.multicastProducerAssociations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastProducerAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastProducerAssociations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/multicastProducerAssociations`   
Creates a new multicast producer association in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastProducerAssociations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/multicastProducerAssociations/*}`   
Deletes a single multicast consumer association.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastProducerAssociations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/multicastProducerAssociations/*}`   
Gets details of a single multicast producer association.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastProducerAssociations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/multicastProducerAssociations`   
Lists multicast producer associations in a given project and location.  
  
## REST Resource: [v1.projects.locations.multicastConsumerAssociations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastConsumerAssociations`   
Creates a new multicast consumer association in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastConsumerAssociations/*}`   
Deletes a single multicast consumer association.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations/get)` |  `GET /v1/{name=projects/*/locations/*/multicastConsumerAssociations/*}`   
Gets details of a single multicast consumer association.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastConsumerAssociations`   
Lists multicast consumer associations in a given project and location.  
  
## REST Resource: [v1.projects.locations.multicastDomainActivations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastDomainActivations`   
Creates a new multicast domain activation in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastDomainActivations/*}`   
Deletes a single multicast domain activation.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/get)` |  `GET /v1/{name=projects/*/locations/*/multicastDomainActivations/*}`   
Gets details of a single multicast domain activation.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastDomainActivations`   
Lists multicast domain activations in a given project and location.  
`[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/patch)` |  `PATCH /v1/{multicastDomainActivation.name=projects/*/locations/*/multicastDomainActivations/*}`   
Updates the parameters of a single multicast domain activation.  
  
## REST Resource: [v1.projects.locations.multicastDomainGroups](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastDomainGroups`   
Creates a new multicast domain group in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastDomainGroups/*}`   
Deletes a single multicast domain.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups/get)` |  `GET /v1/{name=projects/*/locations/*/multicastDomainGroups/*}`   
Gets details of a single multicast domain group.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastDomainGroups`   
Lists multicast domain groups in a given project and location.  
  
## REST Resource: [v1.projects.locations.multicastDomains](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastDomains`   
Creates a new multicast domain in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastDomains/*}`   
Deletes a single multicast domain.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/get)` |  `GET /v1/{name=projects/*/locations/*/multicastDomains/*}`   
Gets details of a single multicast domain.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastDomains`   
Lists multicast domains in a given project and location.  
  
## REST Resource: [v1.projects.locations.multicastGroupConsumerActivations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastGroupConsumerActivations`   
Creates a new multicast group consumer activation in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastGroupConsumerActivations/*}`   
Deletes a single multicast group consumer activation.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/get)` |  `GET /v1/{name=projects/*/locations/*/multicastGroupConsumerActivations/*}`   
Gets details of a single multicast group consumer activation.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastGroupConsumerActivations`   
Lists multicast group consumer activations in a given project and location.  
`[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/patch)` |  `PATCH /v1/{multicastGroupConsumerActivation.name=projects/*/locations/*/multicastGroupConsumerActivations/*}`   
Updates the parameters of a single multicast group consumer activation.  
  
## REST Resource: [v1.projects.locations.multicastGroupProducerActivations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastGroupProducerActivations`   
Creates a new multicast group consumer activation in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastGroupProducerActivations/*}`   
Deletes a single multicast group consumer activation.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations/get)` |  `GET /v1/{name=projects/*/locations/*/multicastGroupProducerActivations/*}`   
Gets details of a single multicast group consumer activation.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastGroupProducerActivations`   
Lists multicast group consumer activations in a given project and location.  
  
## REST Resource: [v1.projects.locations.multicastGroupRangeActivations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastGroupRangeActivations`   
Creates a new multicast group range activation in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastGroupRangeActivations/*}`   
Deletes a single multicast group range activation.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/get)` |  `GET /v1/{name=projects/*/locations/*/multicastGroupRangeActivations/*}`   
Gets details of a single multicast group range activation.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastGroupRangeActivations`   
Lists multicast group range activationsin a given project and location.  
`[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/patch)` |  `PATCH /v1/{multicastGroupRangeActivation.name=projects/*/locations/*/multicastGroupRangeActivations/*}`   
Updates the parameters of a single multicast group range activation.  
  
## REST Resource: [v1.projects.locations.multicastGroupRanges](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastGroupRanges`   
Creates a new multicast group range in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastGroupRanges/*}`   
Deletes a single multicast group range.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/get)` |  `GET /v1/{name=projects/*/locations/*/multicastGroupRanges/*}`   
Gets details of a single multicast group range.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastGroupRanges`   
Lists multicast group ranges in a given project and location.  
`[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/patch)` |  `PATCH /v1/{multicastGroupRange.name=projects/*/locations/*/multicastGroupRanges/*}`   
Updates the parameters of a single multicast group range.  
  
## REST Resource: [v1.projects.locations.multicastProducerAssociations](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations/create)` |  `POST /v1/{parent=projects/*/locations/*}/multicastProducerAssociations`   
Creates a new multicast producer association in a given project and location.  
`[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/multicastProducerAssociations/*}`   
Deletes a single multicast consumer association.  
`[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations/get)` |  `GET /v1/{name=projects/*/locations/*/multicastProducerAssociations/*}`   
Gets details of a single multicast producer association.  
`[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations/list)` |  `GET /v1/{parent=projects/*/locations/*}/multicastProducerAssociations`   
Lists multicast producer associations in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
