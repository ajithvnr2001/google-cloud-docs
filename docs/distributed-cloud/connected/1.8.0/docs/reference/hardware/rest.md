---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/
title: GDC Hardware Management API \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:21.557469+00:00
---

# GDC Hardware Management API  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/apis)



Send feedback 

#  GDC Hardware Management API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.hardware
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1alpha.projects.locations.orders
  * REST Resource: v1alpha.projects.locations.orders.changeLogEntries
  * REST Resource: v1alpha.projects.locations.orders.comments
  * REST Resource: v1alpha.projects.locations.orders.hardwareGroups
  * REST Resource: v1alpha.projects.locations.sites
  * REST Resource: v1alpha.projects.locations.skus
  * REST Resource: v1alpha.projects.locations.zones



## Service: gdchardwaremanagement.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://gdchardwaremanagement.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://gdchardwaremanagement.googleapis.com`



## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.hardware)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.hardware/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/hardware`   
Creates new hardware in a given project and location.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.hardware/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/hardware/*}`   
Deletes hardware.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.hardware/get)` |  `GET /v1alpha/{name=projects/*/locations/*/hardware/*}`   
Gets hardware details.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.hardware/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/hardware`   
Lists hardware in a given project and location.  
`[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.hardware/patch)` |  `PATCH /v1alpha/{hardware.name=projects/*/locations/*/hardware/*}`   
Updates hardware parameters.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations.orders](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/orders`   
Creates a new order in a given project and location.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/orders/*}`   
Deletes an order.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/get)` |  `GET /v1alpha/{name=projects/*/locations/*/orders/*}`   
Gets details of an order.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/orders`   
Lists orders in a given project and location.  
`[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/patch)` |  `PATCH /v1alpha/{order.name=projects/*/locations/*/orders/*}`   
Updates the parameters of an order.  
`[submit](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/submit)` |  `POST /v1alpha/{name=projects/*/locations/*/orders/*}:submit`   
Submits an order.  
  
## REST Resource: [v1alpha.projects.locations.orders.changeLogEntries](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.changeLogEntries)

Methods  
---  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.changeLogEntries/get)` |  `GET /v1alpha/{name=projects/*/locations/*/orders/*/changeLogEntries/*}`   
Gets details of a change to an order.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.changeLogEntries/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/orders/*}/changeLogEntries`   
Lists the changes made to an order.  
  
## REST Resource: [v1alpha.projects.locations.orders.comments](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/orders/*}/comments`   
Creates a new comment on an order.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments/get)` |  `GET /v1alpha/{name=projects/*/locations/*/orders/*/comments/*}`   
Gets the content of a comment.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/orders/*}/comments`   
Lists the comments on an order.  
`[recordAction](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments/recordAction)` |  `POST /v1alpha/{name=projects/*/locations/*/orders/*/comments/*}:recordAction`   
Record Action on a Comment.  
  
## REST Resource: [v1alpha.projects.locations.orders.hardwareGroups](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/orders/*}/hardwareGroups`   
Creates a new hardware group in a given order.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/orders/*/hardwareGroups/*}`   
Deletes a hardware group.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/get)` |  `GET /v1alpha/{name=projects/*/locations/*/orders/*/hardwareGroups/*}`   
Gets details of a hardware group.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/orders/*}/hardwareGroups`   
Lists hardware groups in a given order.  
`[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/patch)` |  `PATCH /v1alpha/{hardwareGroup.name=projects/*/locations/*/orders/*/hardwareGroups/*}`   
Updates the parameters of a hardware group.  
  
## REST Resource: [v1alpha.projects.locations.sites](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.sites)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.sites/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/sites`   
Creates a new site in a given project and location.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.sites/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/sites/*}`   
Deletes a site.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.sites/get)` |  `GET /v1alpha/{name=projects/*/locations/*/sites/*}`   
Gets details of a site.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.sites/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/sites`   
Lists sites in a given project and location.  
`[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.sites/patch)` |  `PATCH /v1alpha/{site.name=projects/*/locations/*/sites/*}`   
Updates the parameters of a site.  
  
## REST Resource: [v1alpha.projects.locations.skus](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.skus)

Methods  
---  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.skus/get)` |  `GET /v1alpha/{name=projects/*/locations/*/skus/*}`   
Gets details of an SKU.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.skus/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/skus`   
Lists SKUs for a given project and location.  
  
## REST Resource: [v1alpha.projects.locations.zones](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/zones`   
Creates a new zone in a given project and location.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/zones/*}`   
Deletes a zone.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/get)` |  `GET /v1alpha/{name=projects/*/locations/*/zones/*}`   
Gets details of a zone.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/zones`   
Lists zones in a given project and location.  
`[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/patch)` |  `PATCH /v1alpha/{zone.name=projects/*/locations/*/zones/*}`   
Updates the parameters of a zone.  
`[signal](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/signal)` |  `POST /v1alpha/{name=projects/*/locations/*/zones/*}:signal`   
Signals the state of a zone.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
