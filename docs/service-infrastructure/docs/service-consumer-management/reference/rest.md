---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/
title: Service Consumer Management API \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:40.192916+00:00
---

# Service Consumer Management API  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Service Consumer Management API Stay organized with collections  Save and categorize content based on your preferences. 

Manages the service consumers of a Service Infrastructure service.

  * REST Resource: v1beta1.operations
  * REST Resource: v1beta1.services.consumerQuotaMetrics
  * REST Resource: v1beta1.services.consumerQuotaMetrics.limits
  * REST Resource: v1beta1.services.consumerQuotaMetrics.limits.producerOverrides
  * REST Resource: v1.operations
  * REST Resource: v1.services
  * REST Resource: v1.services.tenancyUnits



## Service: serviceconsumermanagement.googleapis.com

We recommend that you call this service using Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to call this service using your own libraries, you should use the following information when making the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://serviceconsumermanagement.googleapis.com/$discovery/rest?version=v1>
  * <https://serviceconsumermanagement.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary) is a base URL that specifies the network address of an API service. One service may have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://serviceconsumermanagement.googleapis.com`



## REST Resource: [v1beta1.operations](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/operations)

Methods  
---  
`[get](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/operations/get)` |  `GET /v1beta1/{name=operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1beta1.services.consumerQuotaMetrics](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics)

Methods  
---  
`[get](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics/get)` |  `GET /v1beta1/{name=services/*/*/*/consumerQuotaMetrics/*}`   
Retrieves a summary of quota information for a specific quota metric.  
`[importProducerOverrides](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics/importProducerOverrides)` |  `POST /v1beta1/{parent=services/*/*/*}/consumerQuotaMetrics:importProducerOverrides`   
Create or update multiple producer overrides atomically, all on the same consumer, but on many different metrics or limits.  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics/list)` |  `GET /v1beta1/{parent=services/*/*/*}/consumerQuotaMetrics`   
Retrieves a summary of all quota information about this consumer that is visible to the service producer, for each quota metric defined by the service.  
  
## REST Resource: [v1beta1.services.consumerQuotaMetrics.limits](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits)

Methods  
---  
`[get](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits/get)` |  `GET /v1beta1/{name=services/*/*/*/consumerQuotaMetrics/*/limits/*}`   
Retrieves a summary of quota information for a specific quota limit.  
  
## REST Resource: [v1beta1.services.consumerQuotaMetrics.limits.producerOverrides](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides)

Methods  
---  
`[create](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides/create)` |  `POST /v1beta1/{parent=services/*/*/*/consumerQuotaMetrics/*/limits/*}/producerOverrides`   
Creates a producer override.  
`[delete](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides/delete)` |  `DELETE /v1beta1/{name=services/*/*/*/consumerQuotaMetrics/*/limits/*/producerOverrides/*}`   
Deletes a producer override.  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides/list)` |  `GET /v1beta1/{parent=services/*/*/*/consumerQuotaMetrics/*/limits/*}/producerOverrides`   
Lists all producer overrides on this limit.  
`[patch](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides/patch)` |  `PATCH /v1beta1/{name=services/*/*/*/consumerQuotaMetrics/*/limits/*/producerOverrides/*}`   
Updates a producer override.  
  
## Service: serviceconsumermanagement.googleapis.com

We recommend that you call this service using Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to call this service using your own libraries, you should use the following information when making the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://serviceconsumermanagement.googleapis.com/$discovery/rest?version=v1>
  * <https://serviceconsumermanagement.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary) is a base URL that specifies the network address of an API service. One service may have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://serviceconsumermanagement.googleapis.com`



## REST Resource: [v1.operations](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/operations/cancel)` |  `POST /v1/{name=operations/**}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/operations/delete)` |  `DELETE /v1/{name=operations/**}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/operations/get)` |  `GET /v1/{name=operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/operations/list)` |  `GET /v1/{name}`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.services](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services)

Methods  
---  
`[search](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services/search)` |  `GET /v1/{parent=services/*}:search`   
Search tenancy units for a managed service.  
  
## REST Resource: [v1.services.tenancyUnits](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits)

Methods  
---  
`[addProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/addProject)` |  `POST /v1/{parent=services/*/*/*/tenancyUnits/*}:addProject`   
Add a new tenant project to the tenancy unit.  
`[applyProjectConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig)` |  `POST /v1/{name=services/*/*/*/tenancyUnits/*}:applyProjectConfig`   
Apply a configuration to an existing tenant project.  
`[attachProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject)` |  `POST /v1/{name=services/*/*/*/tenancyUnits/*}:attachProject`   
Attach an existing project to the tenancy unit as a new tenant resource.  
`[create](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/create)` |  `POST /v1/{parent=services/*/*/*}/tenancyUnits`   
Creates a tenancy unit with no tenant resources.  
`[delete](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/delete)` |  `DELETE /v1/{name=services/*/*/*/tenancyUnits/*}`   
Delete a tenancy unit.  
`[deleteProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject)` |  `POST /v1/{name=services/*/*/*/tenancyUnits/*}:deleteProject`   
Deletes the specified project resource identified by a tenant resource tag.  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/list)` |  `GET /v1/{parent=services/*/*/*}/tenancyUnits`   
Find the tenancy unit for a managed service and service consumer.  
`[removeProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/removeProject)` |  `POST /v1/{name=services/*/*/*/tenancyUnits/*}:removeProject`   
Removes the specified project resource identified by a tenant resource tag.  
`[undeleteProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject)` |  `POST /v1/{name=services/*/*/*/tenancyUnits/*}:undeleteProject`   
Attempts to undelete a previously deleted tenant project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
